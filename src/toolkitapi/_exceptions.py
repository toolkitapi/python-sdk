"""Custom exception classes for the ToolkitAPI SDK."""

from __future__ import annotations


class ToolkitAPIError(Exception):
    """Base exception for all ToolkitAPI errors."""


class AuthenticationError(ToolkitAPIError):
    """Raised when the API key is missing or invalid (401/403)."""


class NotFoundError(ToolkitAPIError):
    """Raised when the requested resource is not found (404)."""


class ValidationError(ToolkitAPIError):
    """Raised when the API rejects input parameters (400/422)."""


class RateLimitError(ToolkitAPIError):
    """Raised when the API rate limit is exceeded (429)."""


class ServerError(ToolkitAPIError):
    """Raised when the API returns a server error (5xx)."""


class APIError(ToolkitAPIError):
    """Raised for any other non-success HTTP status code.

    Attributes:
        status_code: The HTTP status code returned by the API.
        detail: The error detail message from the API response.
    """

    def __init__(self, status_code: int, detail: str) -> None:
        self.status_code = status_code
        self.detail = detail
        super().__init__(f"HTTP {status_code}: {detail}")
