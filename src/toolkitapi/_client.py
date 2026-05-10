"""Low-level HTTP client shared by every toolkit module.

Handles authentication, URL construction, request dispatch, and error
mapping so individual toolkit classes only need to declare thin wrappers.
"""

from __future__ import annotations

from typing import Any, Dict, Optional, Union

import httpx

from ._exceptions import (
    APIError,
    AuthenticationError,
    NotFoundError,
    RateLimitError,
    ServerError,
    ToolkitAPIError,
    ValidationError,
)

_DEFAULT_TIMEOUT: float = 30.0


class _APIClient:
    """Internal HTTP client scoped to a single toolkit subdomain.

    Parameters:
        toolkit: Toolkit identifier (e.g. ``"dns"``, ``"devtools"``).
        api_key: ToolkitAPI API key sent via the ``X-API-Key`` header.
            Either ``api_key`` or ``rapidapi_key`` must be provided.
        base_url: Override the default base URL — useful for local
            development / testing.
        rapidapi_key: RapidAPI subscription key.  When supplied, requests
            are sent with ``x-rapidapi-key`` / ``x-rapidapi-host`` headers
            instead of ``X-API-Key``, and ``rapidapi_host`` must also be set.
        rapidapi_host: RapidAPI host header value (e.g.
            ``"auth-security-api-jwt-hashing-encryption.p.rapidapi.com"``).
            Required when ``rapidapi_key`` is provided.
        timeout: Request timeout in seconds (default 30).
    """

    def __init__(
        self,
        toolkit: str,
        api_key: str = "",
        *,
        base_url: Optional[str] = None,
        rapidapi_key: Optional[str] = None,
        rapidapi_host: Optional[str] = None,
        timeout: float = _DEFAULT_TIMEOUT,
    ) -> None:
        if not api_key and not rapidapi_key:
            raise AuthenticationError(
                "Either api_key or rapidapi_key is required."
            )

        if rapidapi_key:
            if not rapidapi_host:
                raise AuthenticationError(
                    "rapidapi_host is required when using rapidapi_key."
                )
            self._base_url = (
                base_url.rstrip("/") if base_url else f"https://{rapidapi_host}"
            )
            headers: Dict[str, str] = {
                "x-rapidapi-key": rapidapi_key,
                "x-rapidapi-host": rapidapi_host,
                "Accept": "application/json",
            }
        else:
            self._base_url = (
                base_url.rstrip("/") if base_url else f"https://{toolkit}.toolkitapi.io"
            )
            headers = {
                "X-API-Key": api_key,
                "Accept": "application/json",
            }

        self._client = httpx.Client(
            base_url=self._base_url,
            headers=headers,
            timeout=timeout,
        )

    # --------------------------------------------------------------------- #
    # Public helpers
    # --------------------------------------------------------------------- #

    def get(
        self,
        path: str,
        params: Optional[Dict[str, Any]] = None,
    ) -> Any:
        """Send a GET request and return the parsed JSON body.

        Parameters:
            path: Endpoint path **without** the ``/v1/`` prefix
                  (e.g. ``"lookup"``, ``"seo/audit"``).
            params: Query-string parameters.  ``None`` values are
                    silently dropped.
        """
        clean = _strip_none(params) if params else None
        response = self._client.get(f"/v1/{path}", params=clean)
        return self._handle(response)

    def get_bytes(
        self,
        path: str,
        params: Optional[Dict[str, Any]] = None,
    ) -> bytes:
        """Send a GET request and return the raw response body as ``bytes``.

        Useful for endpoints that stream file downloads (e.g. the convert
        toolkit's ``GET /v1/convert/{category}`` routes).  Non-2xx
        responses are mapped to the same exceptions as :meth:`get`.

        Parameters:
            path: Endpoint path **without** the ``/v1/`` prefix.
            params: Query-string parameters.  ``None`` values are
                    silently dropped.
        """
        clean = _strip_none(params) if params else None
        response = self._client.get(f"/v1/{path}", params=clean)
        if response.is_success:
            return response.content
        # Delegate error handling to _handle, which will raise.
        self._handle(response)
        return b""  # unreachable, _handle always raises on non-success

    def post(
        self,
        path: str,
        body: Optional[Union[Dict[str, Any], list, str]] = None,
        params: Optional[Dict[str, Any]] = None,
    ) -> Any:
        """Send a POST request with a JSON body and return parsed JSON.

        Parameters:
            path: Endpoint path **without** the ``/v1/`` prefix.
            body: JSON-serialisable request body.  For ``dict`` bodies,
                  ``None`` values are silently dropped.  Lists, strings,
                  and other JSON-serialisable values are sent as-is.
            params: Optional query-string parameters.
        """
        if isinstance(body, dict):
            clean_body: Any = _strip_none(body)
        else:
            clean_body = body
        clean_params = _strip_none(params) if params else None
        response = self._client.post(
            f"/v1/{path}",
            json=clean_body,
            params=clean_params,
        )
        return self._handle(response)

    def delete(
        self,
        path: str,
        params: Optional[Dict[str, Any]] = None,
    ) -> Any:
        """Send a DELETE request and return the parsed JSON body.

        Parameters:
            path: Endpoint path **without** the ``/v1/`` prefix.
            params: Query-string parameters.  ``None`` values are
                    silently dropped.
        """
        clean = _strip_none(params) if params else None
        response = self._client.delete(f"/v1/{path}", params=clean)
        return self._handle(response)

    def close(self) -> None:
        """Close the underlying ``httpx.Client``."""
        self._client.close()

    # Context-manager support so callers can use ``with`` blocks.
    def __enter__(self) -> "_APIClient":
        return self

    def __exit__(self, *args: Any) -> None:
        self.close()

    # --------------------------------------------------------------------- #
    # Internals
    # --------------------------------------------------------------------- #

    def _handle(self, response: httpx.Response) -> Any:
        """Inspect the response status and raise the appropriate exception
        or return the parsed JSON payload."""
        if response.is_success:
            return response.json()

        # Try to extract a detail message from the JSON body.
        detail = ""
        try:
            data = response.json()
            detail = data.get("detail", "") or data.get("message", "")
        except Exception:
            detail = response.text[:300]

        status = response.status_code

        if status in (401, 403):
            raise AuthenticationError(detail or "Authentication failed.")
        if status == 404:
            raise NotFoundError(detail or "Resource not found.")
        if status in (400, 422):
            raise ValidationError(detail or "Invalid request parameters.")
        if status == 429:
            raise RateLimitError(detail or "Rate limit exceeded.")
        if 500 <= status < 600:
            raise ServerError(detail or "Internal server error.")

        raise APIError(status, detail or "Unexpected error.")


# --------------------------------------------------------------------- #
# Module-private helpers
# --------------------------------------------------------------------- #


def _strip_none(mapping: Dict[str, Any]) -> Dict[str, Any]:
    """Return a shallow copy of *mapping* with ``None`` values removed."""
    return {k: v for k, v in mapping.items() if v is not None}
