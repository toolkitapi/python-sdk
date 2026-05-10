"""Generate a QR code with custom colours, module shapes, and optional logo embedding."""

from __future__ import annotations

from typing import Dict, Any, Optional

from ._client import _APIClient


class Barcode:
    """Generate a styled QR code"""

    def __init__(
        self,
        api_key: str,
        *,
        base_url: Optional[str] = None,
        timeout: float = 30.0,
    ) -> None:
        self._client = _APIClient(
            "barcode", api_key, base_url=base_url, timeout=timeout
        )

    # ------------------------------------------------------------------ #
    #  Qr
    # ------------------------------------------------------------------ #

    def qr_generate(
        self,
        body: Dict[str, Any],
    ) -> Dict[str, Any]:
        """Generate a styled QR code

        Args:
            body: Request body.
        """
        return self._client.post("qr/generate", body=body)

    def qr_generate_get(
        self,
        data: str,
        *,
        size: Optional[int] = None,
        error_correction: Optional[str] = None,
        format: Optional[str] = None,
        fg_color: Optional[str] = None,
        bg_color: Optional[str] = None,
        module_shape: Optional[str] = None,
    ) -> Any:
        """Generate a QR code (raw image)

        Args:
            data: Text or URL to encode
            size: Image size in pixels
            error_correction: 
            format: 
            fg_color: Foreground hex colour
            bg_color: Background hex colour
            module_shape: 
        """
        return self._client.get("qr/generate", params={"data": data, "size": size, "error_correction": error_correction, "format": format, "fg_color": fg_color, "bg_color": bg_color, "module_shape": module_shape})

    def qr_decode(
        self,
        body: Dict[str, Any],
    ) -> Dict[str, Any]:
        """Decode QR code(s) from an image

        Args:
            body: Request body.
        """
        return self._client.post("qr/decode", body=body)

    def qr_bulk(
        self,
        body: Dict[str, Any],
    ) -> Dict[str, Any]:
        """Bulk-generate QR codes

        Args:
            body: Request body.
        """
        return self._client.post("qr/bulk", body=body)

    # ------------------------------------------------------------------ #
    #  Barcode
    # ------------------------------------------------------------------ #

    def generate(
        self,
        body: Dict[str, Any],
    ) -> Dict[str, Any]:
        """Generate a barcode

        Args:
            body: Request body.
        """
        return self._client.post("barcode/generate", body=body)

    def generate_get(
        self,
        data: str,
        *,
        barcode_type: Optional[str] = None,
        format: Optional[str] = None,
        include_text: Optional[bool] = None,
        fg_color: Optional[str] = None,
        bg_color: Optional[str] = None,
        module_height: Optional[float] = None,
        quiet_zone: Optional[float] = None,
    ) -> Any:
        """Generate a barcode (raw image)

        Args:
            data: Data to encode
            barcode_type: 
            format: 
            include_text: 
            fg_color: 
            bg_color: 
            module_height: 
            quiet_zone: 
        """
        return self._client.get("barcode/generate", params={"data": data, "barcode_type": barcode_type, "format": format, "include_text": include_text, "fg_color": fg_color, "bg_color": bg_color, "module_height": module_height, "quiet_zone": quiet_zone})

    def decode(
        self,
        body: Dict[str, Any],
    ) -> Dict[str, Any]:
        """Decode barcode(s) from an image

        Args:
            body: Request body.
        """
        return self._client.post("barcode/decode", body=body)

    def bulk(
        self,
        body: Dict[str, Any],
    ) -> Dict[str, Any]:
        """Bulk-generate barcodes

        Args:
            body: Request body.
        """
        return self._client.post("barcode/bulk", body=body)

    def types(
        self,
    ) -> Dict[str, Any]:
        """List supported barcode types
        """
        return self._client.get("barcode/types")

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

    def __enter__(self) -> "Barcode":
        return self

    def __exit__(self, *args: Any) -> None:
        self.close()
