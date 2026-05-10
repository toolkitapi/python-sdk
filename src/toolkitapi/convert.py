"""Convert inline data or a URL source between JSON, CSV, XML, YAML, and TOML."""

from __future__ import annotations

from typing import Dict, Any, Optional

from ._client import _APIClient


class Convert:
    """Convert between data formats"""

    def __init__(
        self,
        api_key: str,
        *,
        base_url: Optional[str] = None,
        timeout: float = 30.0,
    ) -> None:
        self._client = _APIClient(
            "convert", api_key, base_url=base_url, timeout=timeout
        )

    # ------------------------------------------------------------------ #
    #  Convert
    # ------------------------------------------------------------------ #

    def data(
        self,
        body: Dict[str, Any],
    ) -> Dict[str, Any]:
        """Convert between data formats

        Args:
            body: Request body.
        """
        return self._client.post("convert/data", body=body)

    def data_file(
        self,
        url: str,
        from_format: str,
        to_format: str,
        *,
        delimiter: Optional[str] = None,
        include_header: Optional[bool] = None,
        has_header: Optional[bool] = None,
        skip_rows: Optional[int] = None,
        root_element: Optional[str] = None,
        pretty: Optional[bool] = None,
        strip_namespaces: Optional[bool] = None,
        flow_style: Optional[bool] = None,
        filename: Optional[str] = None,
    ) -> Any:
        """Convert data format via URL (file download)

        Args:
            url: Public URL to fetch source data from
            from_format: Source format
            to_format: Target format
            delimiter: CSV delimiter
            include_header: Include CSV header row
            has_header: CSV input has header row
            skip_rows: Skip N rows in CSV input
            root_element: XML root element name
            pretty: Pretty-print XML
            strip_namespaces: Strip XML namespaces
            flow_style: YAML flow style
            filename: Download filename
        """
        return self._client.get("convert/data", params={"url": url, "from_format": from_format, "to_format": to_format, "delimiter": delimiter, "include_header": include_header, "has_header": has_header, "skip_rows": skip_rows, "root_element": root_element, "pretty": pretty, "strip_namespaces": strip_namespaces, "flow_style": flow_style, "filename": filename})

    def markup(
        self,
        body: Dict[str, Any],
    ) -> Dict[str, Any]:
        """Convert between markup formats

        Args:
            body: Request body.
        """
        return self._client.post("convert/markup", body=body)

    def markup_file(
        self,
        url: str,
        from_format: str,
        to_format: str,
        *,
        gfm: Optional[bool] = None,
        sanitize: Optional[bool] = None,
        preserve_links: Optional[bool] = None,
        preserve_tables: Optional[bool] = None,
        filename: Optional[str] = None,
    ) -> Any:
        """Convert markup format via URL (file download)

        Args:
            url: Public URL to fetch source content from
            from_format: Source format
            to_format: Target format
            gfm: GFM extensions
            sanitize: Sanitize HTML output
            preserve_links: Preserve links in text
            preserve_tables: Preserve tables in text
            filename: Download filename
        """
        return self._client.get("convert/markup", params={"url": url, "from_format": from_format, "to_format": to_format, "gfm": gfm, "sanitize": sanitize, "preserve_links": preserve_links, "preserve_tables": preserve_tables, "filename": filename})

    def json_to_typescript(
        self,
        body: Dict[str, Any],
    ) -> Any:
        """Generate TypeScript interfaces from JSON

        Args:
            body: Request body.
        """
        return self._client.post("convert/json-to-typescript", body=body)

    def document(
        self,
        body: Dict[str, Any],
    ) -> Dict[str, Any]:
        """Convert between document formats

        Args:
            body: Request body.
        """
        return self._client.post("convert/document", body=body)

    def document_file(
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
            from_format: Source format
            to_format: Target format
            pages: Page selection (e.g. '1-3,5')
            dpi: DPI for PDF→image
            page_size: Page size for HTML→PDF
            title: EPUB title
            author: EPUB author
            filename: Download filename
        """
        return self._client.get("convert/document", params={"url": url, "from_format": from_format, "to_format": to_format, "pages": pages, "dpi": dpi, "page_size": page_size, "title": title, "author": author, "filename": filename})

    def spreadsheet(
        self,
        body: Dict[str, Any],
    ) -> Dict[str, Any]:
        """Convert between spreadsheet formats

        Args:
            body: Request body.
        """
        return self._client.post("convert/spreadsheet", body=body)

    def spreadsheet_file(
        self,
        url: str,
        from_format: str,
        to_format: str,
        *,
        delimiter: Optional[str] = None,
        sheet_name: Optional[str] = None,
        filename: Optional[str] = None,
    ) -> Any:
        """Convert spreadsheet via URL (file download)

        Args:
            url: Public URL of the source file
            from_format: Source format
            to_format: Target format
            delimiter: CSV delimiter
            sheet_name: Worksheet name
            filename: Download filename
        """
        return self._client.get("convert/spreadsheet", params={"url": url, "from_format": from_format, "to_format": to_format, "delimiter": delimiter, "sheet_name": sheet_name, "filename": filename})

    def calendar(
        self,
        body: Dict[str, Any],
    ) -> Dict[str, Any]:
        """Convert between calendar and contact formats

        Args:
            body: Request body.
        """
        return self._client.post("convert/calendar", body=body)

    def presentation(
        self,
        body: Dict[str, Any],
    ) -> Dict[str, Any]:
        """Convert presentation to PDF

        Args:
            body: Request body.
        """
        return self._client.post("convert/presentation", body=body)

    def presentation_file(
        self,
        url: str,
        from_format: str,
        *,
        to_format: Optional[str] = None,
        filename: Optional[str] = None,
    ) -> Any:
        """Convert presentation via URL (file download)

        Args:
            url: Public URL of the source presentation
            from_format: Source format (pptx, ppt, odp)
            to_format: Target format (pdf)
            filename: Download filename
        """
        return self._client.get("convert/presentation", params={"url": url, "from_format": from_format, "to_format": to_format, "filename": filename})

    def ebook(
        self,
        body: Dict[str, Any],
    ) -> Dict[str, Any]:
        """Convert ebook formats

        Args:
            body: Request body.
        """
        return self._client.post("convert/ebook", body=body)

    def ebook_file(
        self,
        url: str,
        from_format: str,
        *,
        to_format: Optional[str] = None,
        filename: Optional[str] = None,
    ) -> Any:
        """Convert ebook via URL (file download)

        Args:
            url: Public URL of the source ebook
            from_format: Source format (mobi, azw, azw3, fb2, cbr, cbz)
            to_format: Target format (epub, pdf)
            filename: Download filename
        """
        return self._client.get("convert/ebook", params={"url": url, "from_format": from_format, "to_format": to_format, "filename": filename})

    def list_all_formats(
        self,
    ) -> Dict[str, Any]:
        """List all supported conversion formats
        """
        return self._client.get("convert/formats")

    def list_category_formats(
        self,
        category: str,
    ) -> Dict[str, Any]:
        """List conversion formats for a category

        Args:
            category: 
        """
        return self._client.get("convert/formats/{category}", params={"category": category})

    def poll_job_convert_jobs__job_id__get(
        self,
        job_id: str,
    ) -> Dict[str, Any]:
        """Poll async conversion job status

        Args:
            job_id: 
        """
        return self._client.get("convert/jobs/{job_id}", params={"job_id": job_id})

    def supported_formats(
        self,
    ) -> Dict[str, Any]:
        """List supported media conversion formats
        """
        return self._client.get("convert/supported-media-formats")

    def media(
        self,
        body: Dict[str, Any],
    ) -> Dict[str, Any]:
        """Convert a media file (video or audio)

        Args:
            body: Request body.
        """
        return self._client.post("convert/media", body=body)

    def media_get(
        self,
        url: str,
        source_format: str,
        target_format: str,
    ) -> Any:
        """Convert media via URL query params (streaming download)

        Args:
            url: Public URL of the source media file
            source_format: Source format (e.g. 'mp4')
            target_format: Target format (e.g. 'gif')
        """
        return self._client.get("convert/media", params={"url": url, "source_format": source_format, "target_format": target_format})

    def video_thumbnail(
        self,
        body: Dict[str, Any],
    ) -> Dict[str, Any]:
        """Extract a thumbnail frame from a video

        Args:
            body: Request body.
        """
        return self._client.post("convert/video-thumbnail", body=body)

    def media_info(
        self,
        body: Dict[str, Any],
    ) -> Dict[str, Any]:
        """Probe media file for metadata

        Args:
            body: Request body.
        """
        return self._client.post("convert/media-info", body=body)

    def download_file(
        self,
        object_name: str,
    ) -> Any:
        """Download a converted file

        Args:
            object_name: 
        """
        return self._client.get("convert/download/{object_name}", params={"object_name": object_name})

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

    def __enter__(self) -> "Convert":
        return self

    def __exit__(self, *args: Any) -> None:
        self.close()
