"""Run a comprehensive SEO audit on a page: meta tags, headings, images, OG, and more."""

from __future__ import annotations

from typing import Dict, Any, Optional

from ._client import _APIClient


class Scrape:
    """Full page SEO audit"""

    def __init__(
        self,
        api_key: str,
        *,
        base_url: Optional[str] = None,
        timeout: float = 30.0,
    ) -> None:
        self._client = _APIClient(
            "scrape", api_key, base_url=base_url, timeout=timeout
        )

    # ------------------------------------------------------------------ #
    #  Scrape
    # ------------------------------------------------------------------ #

    def seo_audit(
        self,
        url: str,
    ) -> Dict[str, Any]:
        """Full page SEO audit

        Args:
            url: URL to audit
        """
        return self._client.get("scrape/audit", params={"url": url})

    def seo_keyword_density(
        self,
        url: str,
    ) -> Dict[str, Any]:
        """Keyword density and readability analysis

        Args:
            url: URL to analyse
        """
        return self._client.get("scrape/keyword-density", params={"url": url})

    def seo_mobile_friendly(
        self,
        url: str,
    ) -> Dict[str, Any]:
        """Mobile-friendliness check

        Args:
            url: URL to check
        """
        return self._client.get("scrape/mobile-friendly", params={"url": url})

    def seo_broken_links(
        self,
        url: str,
    ) -> Dict[str, Any]:
        """Broken link checker

        Args:
            url: URL to check links on
        """
        return self._client.get("scrape/broken-links", params={"url": url})

    def seo_pagespeed(
        self,
        url: str,
    ) -> Dict[str, Any]:
        """Page speed metrics

        Args:
            url: URL to test
        """
        return self._client.get("scrape/pagespeed", params={"url": url})

    def seo_bulk_audit(
        self,
        body: Dict[str, Any],
    ) -> Dict[str, Any]:
        """Bulk SEO audit for multiple URLs

        Args:
            body: Request body.
        """
        return self._client.post("scrape/bulk-audit", body=body)

    def seo_compare(
        self,
        body: Dict[str, Any],
    ) -> Dict[str, Any]:
        """Side-by-side SEO comparison

        Args:
            body: Request body.
        """
        return self._client.post("scrape/compare", body=body)

    def scrape(
        self,
        body: Dict[str, Any],
    ) -> Dict[str, Any]:
        """Unified Scrape

        Args:
            body: Request body.
        """
        return self._client.post("scrape", body=body)

    def pdf_extract(
        self,
        body: Dict[str, Any],
    ) -> Any:
        """Extract PDF Text

        Args:
            body: Request body.
        """
        return self._client.post("scrape/pdf", body=body)

    def parse_sitemap(
        self,
        url: str,
        *,
        limit: Optional[int] = None,
        discover_links: Optional[bool] = None,
    ) -> Any:
        """Parse Sitemap

        Args:
            url: The sitemap.xml URL
            limit: Max URLs to return
            discover_links: Also scrape landing page for links
        """
        return self._client.get("scrape/sitemap", params={"url": url, "limit": limit, "discover_links": discover_links})

    def parse_robots(
        self,
        url: str,
    ) -> Any:
        """Parse robots.txt

        Args:
            url: Site URL or direct robots.txt URL
        """
        return self._client.get("scrape/robots", params={"url": url})

    def start_crawl(
        self,
        body: Dict[str, Any],
    ) -> Dict[str, Any]:
        """Start Multi-Page Crawl

        Args:
            body: Request body.
        """
        return self._client.post("scrape/crawl", body=body)

    def get_crawl_job(
        self,
        job_id: str,
    ) -> Dict[str, Any]:
        """Get Crawl Job Status

        Args:
            job_id: 
        """
        return self._client.get("scrape/crawl/{job_id}", params={"job_id": job_id})

    # ------------------------------------------------------------------ #
    #  Screenshot
    # ------------------------------------------------------------------ #

    def screenshot_png(
        self,
        body: Dict[str, Any],
        *,
        async_: Optional[bool] = None,
    ) -> Dict[str, Any]:
        """Capture webpage screenshot

        Args:
            body: Request body.
            async_: Return immediately with a download URL and capture in the background
        """
        return self._client.post(
            "screenshot",
            body=body,
            params={"async_": async_},
        )

    def screenshot_pdf(
        self,
        body: Dict[str, Any],
        *,
        async_: Optional[bool] = None,
    ) -> Dict[str, Any]:
        """Capture webpage as PDF

        Args:
            body: Request body.
            async_: Return immediately with a download URL and capture in the background
        """
        return self._client.post(
            "screenshot/pdf",
            body=body,
            params={"async_": async_},
        )

    def screenshot_element(
        self,
        body: Dict[str, Any],
        *,
        async_: Optional[bool] = None,
    ) -> Dict[str, Any]:
        """Capture specific page element

        Args:
            body: Request body.
            async_: Return immediately with a download URL and capture in the background
        """
        return self._client.post(
            "screenshot/element",
            body=body,
            params={"async_": async_},
        )

    def download_file(
        self,
        object_name: str,
    ) -> Any:
        """Download a screenshot

        Args:
            object_name: 
        """
        return self._client.get("screenshot/download/{object_name}", params={"object_name": object_name})

    # ------------------------------------------------------------------ #
    #  Fetch
    # ------------------------------------------------------------------ #

    def fetch(
        self,
        url: str,
        *,
        output: Optional[str] = None,
        render_js: Optional[bool] = None,
        proxy: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Fetch (GET shortcut)

        Args:
            url: The URL to scrape
            output: Output format: html, markdown, text, clean
            render_js: Use headless browser
            proxy: Proxy mode or country code
        """
        return self._client.get("fetch", params={"url": url, "output": output, "render_js": render_js, "proxy": proxy})

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

    def __enter__(self) -> "Scrape":
        return self

    def __exit__(self, *args: Any) -> None:
        self.close()
