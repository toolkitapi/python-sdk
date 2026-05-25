"""Create a temporary HTTP request bin that captures incoming requests.

Security note: treat ``bin_id`` and ``catch_url`` as sensitive values."""

from __future__ import annotations

from typing import Dict, Any, Optional

from ._client import _APIClient


class Webhook:
    """Create a request bin"""

    def __init__(
        self,
        api_key: str,
        *,
        base_url: Optional[str] = None,
        timeout: float = 30.0,
    ) -> None:
        self._client = _APIClient(
            "webhook", api_key, base_url=base_url, timeout=timeout
        )

    # ------------------------------------------------------------------ #
    #  Bins
    # ------------------------------------------------------------------ #

    def create_bin(
        self,
        *,
        body: Optional[Dict[str, Any]] = None,
    ) -> Dict[str, Any]:
        """Create a request bin

        Args:
            body: Request body.
        """
        return self._client.post("bins", body=body)

    def get_bin(
        self,
        bin_id: str,
    ) -> Dict[str, Any]:
        """Get bin details

        Args:
            bin_id: 
        """
        return self._client.get("bins/{bin_id}", params={"bin_id": bin_id})

    def delete_bin(
        self,
        bin_id: str,
    ) -> Dict[str, Any]:
        """Delete a bin

        Args:
            bin_id: 
        """
        return self._client.delete("bins/{bin_id}", params={"bin_id": bin_id})

    def list_requests(
        self,
        bin_id: str,
        *,
        limit: Optional[int] = None,
        offset: Optional[int] = None,
    ) -> Dict[str, Any]:
        """List captured requests

        Args:
            bin_id: 
            limit: 
            offset: 
        """
        return self._client.get("bins/{bin_id}/requests", params={"bin_id": bin_id, "limit": limit, "offset": offset})

    def get_request_detail(
        self,
        bin_id: str,
        request_id: str,
    ) -> Dict[str, Any]:
        """Get captured request detail

        Args:
            bin_id: 
            request_id: 
        """
        return self._client.get("bins/{bin_id}/requests/{request_id}", params={"bin_id": bin_id, "request_id": request_id})

    def replay_request(
        self,
        bin_id: str,
        request_id: str,
        body: Dict[str, Any],
    ) -> Dict[str, Any]:
        """Replay a captured request

        Args:
            bin_id: 
            request_id: 
            body: Request body.
        """
        return self._client.post(
            "bins/{bin_id}/requests/{request_id}/replay",
            body=body,
            params={"bin_id": bin_id, "request_id": request_id},
        )

    # ------------------------------------------------------------------ #
    #  Catch
    # ------------------------------------------------------------------ #

    def catch_request(
        self,
        bin_id: str,
    ) -> Any:
        """Catch and record an HTTP request

        Args:
            bin_id: 
        """
        return self._client.head("catch/{bin_id}", params={"bin_id": bin_id})

    def catch_request_2(
        self,
        bin_id: str,
    ) -> Any:
        """Catch and record an HTTP request

        Args:
            bin_id: 
        """
        return self._client.put("catch/{bin_id}", params={"bin_id": bin_id})

    def catch_request_3(
        self,
        bin_id: str,
    ) -> Any:
        """Catch and record an HTTP request

        Args:
            bin_id: 
        """
        return self._client.get("catch/{bin_id}", params={"bin_id": bin_id})

    def catch_request_4(
        self,
        bin_id: str,
    ) -> Any:
        """Catch and record an HTTP request

        Args:
            bin_id: 
        """
        return self._client.patch("catch/{bin_id}", params={"bin_id": bin_id})

    def catch_request_5(
        self,
        bin_id: str,
    ) -> Any:
        """Catch and record an HTTP request

        Args:
            bin_id: 
        """
        return self._client.options("catch/{bin_id}", params={"bin_id": bin_id})

    def catch_request_6(
        self,
        bin_id: str,
    ) -> Any:
        """Catch and record an HTTP request

        Args:
            bin_id: 
        """
        return self._client.delete("catch/{bin_id}", params={"bin_id": bin_id})

    def catch_request_7(
        self,
        bin_id: str,
    ) -> Any:
        """Catch and record an HTTP request

        Args:
            bin_id: 
        """
        return self._client.post("catch/{bin_id}", params={"bin_id": bin_id})

    # ------------------------------------------------------------------ #
    #  Mocks
    # ------------------------------------------------------------------ #

    def create_mock(
        self,
        *,
        body: Optional[Dict[str, Any]] = None,
    ) -> Dict[str, Any]:
        """Create a mock endpoint

        Args:
            body: Request body.
        """
        return self._client.post("mocks", body=body)

    def get_mock(
        self,
        mock_id: str,
    ) -> Dict[str, Any]:
        """Get mock endpoint details

        Args:
            mock_id: 
        """
        return self._client.get("mocks/{mock_id}", params={"mock_id": mock_id})

    def delete_mock(
        self,
        mock_id: str,
    ) -> Dict[str, Any]:
        """Delete a mock endpoint

        Args:
            mock_id: 
        """
        return self._client.delete("mocks/{mock_id}", params={"mock_id": mock_id})

    # ------------------------------------------------------------------ #
    #  Mock
    # ------------------------------------------------------------------ #

    def hit_mock(
        self,
        mock_id: str,
    ) -> Any:
        """Hit a mock endpoint

        Args:
            mock_id: 
        """
        return self._client.head("mock/{mock_id}", params={"mock_id": mock_id})

    def hit_mock_2(
        self,
        mock_id: str,
    ) -> Any:
        """Hit a mock endpoint

        Args:
            mock_id: 
        """
        return self._client.put("mock/{mock_id}", params={"mock_id": mock_id})

    def hit_mock_3(
        self,
        mock_id: str,
    ) -> Any:
        """Hit a mock endpoint

        Args:
            mock_id: 
        """
        return self._client.get("mock/{mock_id}", params={"mock_id": mock_id})

    def hit_mock_4(
        self,
        mock_id: str,
    ) -> Any:
        """Hit a mock endpoint

        Args:
            mock_id: 
        """
        return self._client.patch("mock/{mock_id}", params={"mock_id": mock_id})

    def hit_mock_5(
        self,
        mock_id: str,
    ) -> Any:
        """Hit a mock endpoint

        Args:
            mock_id: 
        """
        return self._client.options("mock/{mock_id}", params={"mock_id": mock_id})

    def hit_mock_6(
        self,
        mock_id: str,
    ) -> Any:
        """Hit a mock endpoint

        Args:
            mock_id: 
        """
        return self._client.delete("mock/{mock_id}", params={"mock_id": mock_id})

    def hit_mock_7(
        self,
        mock_id: str,
    ) -> Any:
        """Hit a mock endpoint

        Args:
            mock_id: 
        """
        return self._client.post("mock/{mock_id}", params={"mock_id": mock_id})

    # ------------------------------------------------------------------ #
    #  
    # ------------------------------------------------------------------ #

    def root__get(
        self,
    ) -> Any:
        """Root
        """
        return self._client.get("")

    # ------------------------------------------------------------------ #
    #  Status
    # ------------------------------------------------------------------ #

    def status(
        self,
    ) -> Any:
        """Status
        """
        return self._client.get("status")

    # ------------------------------------------------------------------ #
    #  Lifecycle
    # ------------------------------------------------------------------ #

    def close(self) -> None:
        """Close the underlying HTTP client."""
        self._client.close()

    def __enter__(self) -> "Webhook":
        return self

    def __exit__(self, *args: Any) -> None:
        self.close()
