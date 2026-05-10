"""Hash a plaintext password using bcrypt, argon2, or scrypt."""

from __future__ import annotations

from typing import Dict, Any, Optional

from ._client import _APIClient


class Auth:
    """Hash a password"""

    def __init__(
        self,
        api_key: str,
        *,
        base_url: Optional[str] = None,
        timeout: float = 30.0,
    ) -> None:
        self._client = _APIClient(
            "auth", api_key, base_url=base_url, timeout=timeout
        )

    # ------------------------------------------------------------------ #
    #  Auth
    # ------------------------------------------------------------------ #

    def hash_password(
        self,
        body: Dict[str, Any],
    ) -> Dict[str, Any]:
        """Hash a password

        Args:
            body: Request body.
        """
        return self._client.post("auth/hash-password", body=body)

    def verify_password(
        self,
        body: Dict[str, Any],
    ) -> Dict[str, Any]:
        """Verify a password against a hash

        Args:
            body: Request body.
        """
        return self._client.post("auth/verify-password", body=body)

    def password_strength(
        self,
        body: Dict[str, Any],
    ) -> Dict[str, Any]:
        """Analyze password strength

        Args:
            body: Request body.
        """
        return self._client.post("auth/password-strength", body=body)

    def generate_password(
        self,
        *,
        body: Optional[Dict[str, Any]] = None,
    ) -> Dict[str, Any]:
        """Generate secure random passwords

        Args:
            body: Request body.
        """
        return self._client.post("auth/generate-password", body=body)

    def jwt_generate(
        self,
        body: Dict[str, Any],
    ) -> Dict[str, Any]:
        """Generate a JWT token

        Args:
            body: Request body.
        """
        return self._client.post("auth/jwt-generate", body=body)

    def jwt_verify(
        self,
        body: Dict[str, Any],
    ) -> Dict[str, Any]:
        """Verify a JWT token

        Args:
            body: Request body.
        """
        return self._client.post("auth/jwt-verify", body=body)

    def jwt_decode(
        self,
        body: Dict[str, Any],
    ) -> Dict[str, Any]:
        """Decode a JWT without verification

        Args:
            body: Request body.
        """
        return self._client.post("auth/jwt-decode", body=body)

    def totp_generate(
        self,
        *,
        issuer: Optional[str] = None,
        account_name: Optional[str] = None,
        digits: Optional[int] = None,
        period: Optional[int] = None,
        algorithm: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Generate a TOTP secret and QR code

        Args:
            issuer: Service/issuer name
            account_name: User account identifier
            digits: Number of digits in the OTP code (6 or 8)
            period: Time step in seconds
            algorithm: HMAC algorithm
        """
        return self._client.get("auth/totp-generate", params={"issuer": issuer, "account_name": account_name, "digits": digits, "period": period, "algorithm": algorithm})

    def totp_verify(
        self,
        body: Dict[str, Any],
    ) -> Dict[str, Any]:
        """Verify a TOTP code

        Args:
            body: Request body.
        """
        return self._client.post("auth/totp-verify", body=body)

    def generate_key(
        self,
        type_: str,
        *,
        length: Optional[int] = None,
        prefix: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Generate a random key or identifier

        Args:
            type_: Key type to generate (api-key, uuid-v4, nanoid, secret)
            length: Key length (defaults vary by type)
            prefix: Optional prefix for the key
        """
        return self._client.get("auth/generate-key", params={"type_": type_, "length": length, "prefix": prefix})

    def generate_keypair(
        self,
        body: Dict[str, Any],
    ) -> Dict[str, Any]:
        """Generate an asymmetric keypair

        Args:
            body: Request body.
        """
        return self._client.post("auth/generate-keypair", body=body)

    def encrypt(
        self,
        body: Dict[str, Any],
    ) -> Dict[str, Any]:
        """Encrypt plaintext with AES-256-GCM

        Args:
            body: Request body.
        """
        return self._client.post("auth/encrypt", body=body)

    def decrypt(
        self,
        body: Dict[str, Any],
    ) -> Dict[str, Any]:
        """Decrypt ciphertext with AES-256-GCM

        Args:
            body: Request body.
        """
        return self._client.post("auth/decrypt", body=body)

    def hash_string(
        self,
        body: Dict[str, Any],
    ) -> Dict[str, Any]:
        """Hash a string

        Args:
            body: Request body.
        """
        return self._client.post("auth/hash", body=body)

    def hmac_generate(
        self,
        body: Dict[str, Any],
    ) -> Dict[str, Any]:
        """Generate an HMAC

        Args:
            body: Request body.
        """
        return self._client.post("auth/hmac", body=body)

    def hmac_verify(
        self,
        body: Dict[str, Any],
    ) -> Dict[str, Any]:
        """Verify an HMAC signature

        Args:
            body: Request body.
        """
        return self._client.post("auth/hmac-verify", body=body)

    def base64_encode(
        self,
        body: Dict[str, Any],
    ) -> Dict[str, Any]:
        """Base64 encode a string

        Args:
            body: Request body.
        """
        return self._client.post("auth/base64-encode", body=body)

    def base64_decode(
        self,
        body: Dict[str, Any],
    ) -> Dict[str, Any]:
        """Base64 decode a string

        Args:
            body: Request body.
        """
        return self._client.post("auth/base64-decode", body=body)

    def encode_data(
        self,
        body: Dict[str, Any],
    ) -> Dict[str, Any]:
        """Encode or decode a string

        Args:
            body: Request body.
        """
        return self._client.post("auth/encode", body=body)

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

    def __enter__(self) -> "Auth":
        return self

    def __exit__(self, *args: Any) -> None:
        self.close()
