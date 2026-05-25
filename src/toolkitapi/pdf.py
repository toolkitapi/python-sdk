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
        url: str,
        *,
        pages: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Split a PDF into parts

        Args:
            url: Public URL of a PDF document (http/https)
            pages: Page specification: 'all' for individual pages, or ranges like '1-3,5,8-10'
        """
        return self._client.get("pdf/split", params={"url": url, "pages": pages})

    def rotate(
        self,
        url: str,
        angle: int,
        *,
        pages: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Rotate PDF pages

        Args:
            url: Public URL of a PDF document (http/https)
            angle: Rotation angle: 90, 180, or 270 degrees clockwise
            pages: Pages to rotate (e.g. '1-3,5'). Omit to rotate all pages.
        """
        return self._client.get("pdf/rotate", params={"url": url, "angle": angle, "pages": pages})

    def compress(
        self,
        url: str,
    ) -> Dict[str, Any]:
        """Compress a PDF to reduce file size

        Args:
            url: Public URL of a PDF document (http/https)
        """
        return self._client.get("pdf/compress", params={"url": url})

    def watermark(
        self,
        url: str,
        text: str,
        *,
        font_size: Optional[int] = None,
        opacity: Optional[float] = None,
        angle: Optional[int] = None,
        pages: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Add a text watermark to PDF pages

        Args:
            url: Public URL of a PDF document (http/https)
            text: Watermark text to overlay
            font_size: Font size for the watermark text
            opacity: Watermark opacity (0.01-1.0)
            angle: Rotation angle for the watermark text in degrees
            pages: Pages to watermark (e.g. '1-3,5'). Omit for all pages.
        """
        return self._client.get("pdf/watermark", params={"url": url, "text": text, "font_size": font_size, "opacity": opacity, "angle": angle, "pages": pages})

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
        url: str,
        *,
        pages: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Extract text from a PDF

        Args:
            url: Public URL of a PDF document (http/https)
            pages: Pages to extract text from (e.g. '1-3,5'). Omit for all pages.
        """
        return self._client.get("pdf/text", params={"url": url, "pages": pages})

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
        url: str,
        *,
        pages: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Extract tables from a PDF

        Args:
            url: Public URL of a PDF document (http/https)
            pages: Pages to extract tables from (e.g. '1-3'). Omit for all pages.
        """
        return self._client.get("pdf/table-extract", params={"url": url, "pages": pages})

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
        url: str,
    ) -> Dict[str, Any]:
        """Get structural information about a PDF

        Args:
            url: Public URL of a PDF document (http/https)
        """
        return self._client.get("pdf/info", params={"url": url})

    def ocr(
        self,
        url: str,
        *,
        pages: Optional[str] = None,
        language: Optional[str] = None,
        dpi: Optional[int] = None,
    ) -> Dict[str, Any]:
        """Extract text from scanned/image PDFs using OCR

        Args:
            url: Public URL of a PDF document (http/https)
            pages: Pages to OCR (e.g. '1-3,5'). Omit for all pages.
            language: Tesseract language code (e.g. 'eng', 'fra', 'deu')
            dpi: Resolution in DPI for rendering pages to images before OCR
        """
        return self._client.get("pdf/ocr", params={"url": url, "pages": pages, "language": language, "dpi": dpi})

    def to_images(
        self,
        url: str,
        *,
        pages: Optional[str] = None,
        format: Optional[str] = None,
        dpi: Optional[int] = None,
    ) -> Dict[str, Any]:
        """Render PDF pages as images

        Args:
            url: Public URL of a PDF document (http/https)
            pages: Pages to render (e.g. '1-3,5'). Omit for all pages.
            format: Output image format: 'png' or 'jpeg'
            dpi: Resolution in dots per inch (72-600). Higher = larger, sharper images.
        """
        return self._client.get("pdf/to-images", params={"url": url, "pages": pages, "format": format, "dpi": dpi})

    def convert_document(
        self,
        url: str,
        from_format: str,
        to_format: str,
        *,
        pages: Optional[str] = None,
        dpi: Optional[int] = None,
        page_size: Optional[str] = None,
        title: Optional[str] = None,
        author: Optional[str] = None,
        filename: Optional[str] = None,
    ) -> Any:
        """Convert document via URL (file download)

        Args:
            url: Public URL of the source document
            from_format: Source format (pdf, docx, epub, html, doc, rtf, odt, txt)
            to_format: Target format (pdf, docx, epub, png, jpeg)
            pages: Page selection, e.g. '1-3,5' (pdf → images)
            dpi: DPI for PDF → image rendering
            page_size: Page size for HTML → PDF (A3/A4/A5/Letter/Legal)
            title: Title metadata (EPUB output)
            author: Author metadata (EPUB output)
            filename: Override download filename
        """
        return self._client.get("pdf/convert/document", params={"url": url, "from_format": from_format, "to_format": to_format, "pages": pages, "dpi": dpi, "page_size": page_size, "title": title, "author": author, "filename": filename})

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
