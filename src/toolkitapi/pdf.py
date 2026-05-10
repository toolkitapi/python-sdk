"""Merge 2-20 PDF documents into a single file in the order provided."""

from __future__ import annotations

from typing import Dict, Any, Optional

from ._client import _APIClient


class PDF:
    """Merge multiple PDFs into one"""

    def __init__(
        self,
        api_key: str,
        *,
        base_url: Optional[str] = None,
        timeout: float = 30.0,
    ) -> None:
        self._client = _APIClient(
            "pdf", api_key, base_url=base_url, timeout=timeout
        )

    # ------------------------------------------------------------------ #
    #  Pdf
    # ------------------------------------------------------------------ #

    def merge(
        self,
        body: Dict[str, Any],
    ) -> Dict[str, Any]:
        """Merge multiple PDFs into one

        Args:
            body: Request body.
        """
        return self._client.post("pdf/merge", body=body)

    def split(
        self,
        body: Dict[str, Any],
    ) -> Dict[str, Any]:
        """Split a PDF into parts

        Args:
            body: Request body.
        """
        return self._client.post("pdf/split", body=body)

    def rotate(
        self,
        body: Dict[str, Any],
    ) -> Dict[str, Any]:
        """Rotate PDF pages

        Args:
            body: Request body.
        """
        return self._client.post("pdf/rotate", body=body)

    def compress(
        self,
        body: Dict[str, Any],
    ) -> Dict[str, Any]:
        """Compress a PDF to reduce file size

        Args:
            body: Request body.
        """
        return self._client.post("pdf/compress", body=body)

    def watermark(
        self,
        body: Dict[str, Any],
    ) -> Dict[str, Any]:
        """Add a text watermark to PDF pages

        Args:
            body: Request body.
        """
        return self._client.post("pdf/watermark", body=body)

    def protect(
        self,
        body: Dict[str, Any],
    ) -> Dict[str, Any]:
        """Encrypt or decrypt a PDF

        Args:
            body: Request body.
        """
        return self._client.post("pdf/protect", body=body)

    def from_images(
        self,
        body: Dict[str, Any],
    ) -> Dict[str, Any]:
        """Combine images into a PDF

        Args:
            body: Request body.
        """
        return self._client.post("pdf/from-images", body=body)

    def from_template(
        self,
        body: Dict[str, Any],
    ) -> Dict[str, Any]:
        """Generate PDF from a Liquid template

        Args:
            body: Request body.
        """
        return self._client.post("pdf/from-template", body=body)

    def text_extract(
        self,
        body: Dict[str, Any],
    ) -> Dict[str, Any]:
        """Extract text from a PDF

        Args:
            body: Request body.
        """
        return self._client.post("pdf/text", body=body)

    def metadata(
        self,
        body: Dict[str, Any],
    ) -> Dict[str, Any]:
        """Read or update PDF metadata

        Args:
            body: Request body.
        """
        return self._client.post("pdf/metadata", body=body)

    def table_extract(
        self,
        body: Dict[str, Any],
    ) -> Dict[str, Any]:
        """Extract tables from a PDF

        Args:
            body: Request body.
        """
        return self._client.post("pdf/table-extract", body=body)

    def form_fields(
        self,
        body: Dict[str, Any],
    ) -> Dict[str, Any]:
        """Read or fill PDF form fields

        Args:
            body: Request body.
        """
        return self._client.post("pdf/form-fields", body=body)

    def info(
        self,
        body: Dict[str, Any],
    ) -> Dict[str, Any]:
        """Get structural information about a PDF

        Args:
            body: Request body.
        """
        return self._client.post("pdf/info", body=body)

    def ocr(
        self,
        body: Dict[str, Any],
    ) -> Dict[str, Any]:
        """Extract text from scanned/image PDFs using OCR

        Args:
            body: Request body.
        """
        return self._client.post("pdf/ocr", body=body)

    def to_images(
        self,
        body: Dict[str, Any],
    ) -> Dict[str, Any]:
        """Render PDF pages as images

        Args:
            body: Request body.
        """
        return self._client.post("pdf/to-images", body=body)

    def download_file(
        self,
        object_name: str,
    ) -> Any:
        """Download a processed file

        Args:
            object_name: 
        """
        return self._client.get("pdf/download/{object_name}", params={"object_name": object_name})

    def list_pdf_templates(
        self,
        *,
        category: Optional[str] = None,
    ) -> Dict[str, Any]:
        """List pre-built PDF templates

        Args:
            category: Filter templates by category. Available categories: business, certificate, report, events.
        """
        return self._client.get("pdf/templates", params={"category": category})

    def get_pdf_template(
        self,
        template_id: str,
    ) -> Dict[str, Any]:
        """Get a single PDF template

        Args:
            template_id: 
        """
        return self._client.get("pdf/templates/{template_id}", params={"template_id": template_id})

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

    def __enter__(self) -> "PDF":
        return self

    def __exit__(self, *args: Any) -> None:
        self.close()
