"""Full email validation pipeline — syntax, MX, SMTP probe, disposable, free, role detection."""

from __future__ import annotations

from typing import Dict, Any, Optional

from ._client import _APIClient


class Email:
    """Full email validation"""

    def __init__(
        self,
        api_key: str,
        *,
        base_url: Optional[str] = None,
        timeout: float = 30.0,
    ) -> None:
        self._client = _APIClient(
            "email", api_key, base_url=base_url, timeout=timeout
        )

    # ------------------------------------------------------------------ #
    #  Email
    # ------------------------------------------------------------------ #

    def validate_email(
        self,
        email: str,
    ) -> Dict[str, Any]:
        """Full email validation

        Args:
            email: Email address to validate
        """
        return self._client.get("email/validate", params={"email": email})

    def validate_batch(
        self,
        body: Dict[str, Any],
    ) -> Dict[str, Any]:
        """Batch email validation

        Args:
            body: Request body.
        """
        return self._client.post("email/validate-batch", body=body)

    def catch_all(
        self,
        domain: str,
    ) -> Dict[str, Any]:
        """Detect catch-all / accept-all server

        Args:
            domain: Domain to check for catch-all configuration
        """
        return self._client.get("email/catch-all", params={"domain": domain})

    def role_check(
        self,
        email: str,
    ) -> Dict[str, Any]:
        """Role vs personal account detection

        Args:
            email: Email address to check
        """
        return self._client.get("email/role-check", params={"email": email})

    def normalize(
        self,
        email: str,
    ) -> Dict[str, Any]:
        """Normalize an email address

        Args:
            email: Email address to normalize
        """
        return self._client.get("email/normalize", params={"email": email})

    def provider(
        self,
        domain: str,
    ) -> Dict[str, Any]:
        """Identify email provider

        Args:
            domain: Domain or email address to identify the provider for
        """
        return self._client.get("email/provider", params={"domain": domain})

    def parse_headers(
        self,
        body: Dict[str, Any],
    ) -> Dict[str, Any]:
        """Parse raw email headers

        Args:
            body: Request body.
        """
        return self._client.post("email/headers", body=body)

    def spam_score(
        self,
        body: Dict[str, Any],
    ) -> Dict[str, Any]:
        """Score email content for spam signals

        Args:
            body: Request body.
        """
        return self._client.post("email/spam-score", body=body)

    def gravatar(
        self,
        email: str,
        *,
        size: Optional[int] = None,
    ) -> Dict[str, Any]:
        """Get Gravatar for an email address

        Args:
            email: Email address to look up
            size: Avatar image size in pixels
        """
        return self._client.get("email/gravatar", params={"email": email, "size": size})

    def mailto(
        self,
        body: Dict[str, Any],
    ) -> Dict[str, Any]:
        """Build or parse mailto: URIs

        Args:
            body: Request body.
        """
        return self._client.post("email/mailto", body=body)

    def form_spam_score(
        self,
        body: Dict[str, Any],
    ) -> Dict[str, Any]:
        """Score a form submission for spam likelihood

        Args:
            body: Request body.
        """
        return self._client.post("email/form-spam-score", body=body)

    def security(
        self,
        domain: str,
        *,
        format: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Email security posture check

        Args:
            domain: Domain to check (e.g. example.com)
            format: Response format: json or markdown
        """
        return self._client.get("email/security", params={"domain": domain, "format": format})

    def auth(
        self,
        body: str,
        *,
        sending_ip: Optional[str] = None,
        format: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Validate email authentication (SPF, DKIM, DMARC)

        Args:
            body: Request body.
            sending_ip: Sending server IP (optional — will try to parse from Received headers)
            format: Response format: json or markdown
        """
        return self._client.post(
            "email/auth",
            body=body,
            params={"sending_ip": sending_ip, "format": format},
        )

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

    def __enter__(self) -> "Email":
        return self

    def __exit__(self, *args: Any) -> None:
        self.close()
