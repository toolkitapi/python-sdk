"""Tests for package imports, the unified client, and core HTTP plumbing."""

from __future__ import annotations

from importlib.metadata import version as pkg_version

import httpx
import pytest

import toolkitapi
from toolkitapi import (
    Analytics,
    Auth,
    Barcode,
    Dev,
    DNS,
    Email,
    Geo,
    Image,
    Media,
    PDF,
    Scrape,
    Textanalysis,
    ToolkitAPI,
    Webhook,
    # Exceptions
    APIError,
    AuthenticationError,
    NotFoundError,
    RateLimitError,
    ServerError,
    ToolkitAPIError,
    ValidationError,
)
from toolkitapi._client import _APIClient

from conftest import MockTransport


ALL_TOOLKITS = [
    Analytics, Auth, Barcode, Dev, DNS, Email,
    Geo, Image, Media, PDF, Scrape, Textanalysis, Webhook,
]


# ------------------------------------------------------------------ #
#  Package-level checks
# ------------------------------------------------------------------ #


class TestPackageMeta:
    """Verify the top-level package exposes expected symbols."""

    def test_version_string(self):
        assert isinstance(toolkitapi.__version__, str)
        assert len(toolkitapi.__version__.split(".")) == 3, "version should be semver (major.minor.patch)"

    def test_version_matches_distribution_metadata(self):
        assert toolkitapi.__version__ == pkg_version("toolkitapi")

    def test_all_toolkits_importable(self):
        for cls in ALL_TOOLKITS:
            assert callable(cls)

    def test_all_exceptions_importable(self):
        exceptions = [
            ToolkitAPIError, AuthenticationError, NotFoundError,
            ValidationError, RateLimitError, ServerError, APIError,
        ]
        for exc in exceptions:
            assert issubclass(exc, ToolkitAPIError)

    def test_dunder_all_defined(self):
        assert hasattr(toolkitapi, "__all__")
        assert "ToolkitAPI" in toolkitapi.__all__
        assert "DNS" in toolkitapi.__all__
        assert "Webhook" in toolkitapi.__all__


# ------------------------------------------------------------------ #
#  Core _APIClient tests
# ------------------------------------------------------------------ #


class TestAPIClient:
    """Unit tests for the internal _APIClient."""

    def test_requires_api_key(self):
        with pytest.raises(AuthenticationError):
            _APIClient("dns", api_key="")

    def test_get_sends_correct_request(self, mock_transport: MockTransport):
        client = _APIClient("dns", api_key="tk_test")
        client._client = httpx.Client(
            base_url=client._base_url,
            headers={"X-API-Key": "tk_test", "Accept": "application/json"},
            transport=mock_transport,
        )

        result = client.get("lookup", params={"domain": "example.com", "type": "A"})

        assert result == {"ok": True}
        assert len(mock_transport.requests) == 1
        req = mock_transport.requests[0]
        assert req.method == "GET"
        assert "/v1/lookup" in str(req.url)
        assert "domain=example.com" in str(req.url)
        client.close()

    def test_post_sends_json_body(self, mock_transport: MockTransport):
        client = _APIClient("devtools", api_key="tk_test")
        client._client = httpx.Client(
            base_url=client._base_url,
            headers={"X-API-Key": "tk_test", "Accept": "application/json"},
            transport=mock_transport,
        )

        result = client.post("hash", body={"data": "hello", "algorithm": "sha256"})

        assert result == {"ok": True}
        req = mock_transport.requests[0]
        assert req.method == "POST"
        assert "/v1/hash" in str(req.url)
        import json
        body = json.loads(req.content)
        assert body["data"] == "hello"
        client.close()

    def test_none_values_stripped(self, mock_transport: MockTransport):
        client = _APIClient("dns", api_key="tk_test")
        client._client = httpx.Client(
            base_url=client._base_url,
            headers={"X-API-Key": "tk_test"},
            transport=mock_transport,
        )

        client.get("lookup", params={"domain": "example.com", "type": None})

        req = mock_transport.requests[0]
        assert "type" not in str(req.url)
        client.close()

    def test_trailing_underscore_query_keys_normalized(self, mock_transport: MockTransport):
        client = _APIClient("dns", api_key="tk_test")
        client._client = httpx.Client(
            base_url=client._base_url,
            headers={"X-API-Key": "tk_test", "Accept": "application/json"},
            transport=mock_transport,
        )

        client.get("lookup", params={"domain": "example.com", "type_": "MX"})

        req = mock_transport.requests[0]
        assert "type=MX" in str(req.url)
        assert "type_=" not in str(req.url)
        client.close()

    def test_context_manager(self, mock_transport: MockTransport):
        with _APIClient("dns", api_key="tk_test") as client:
            client._client = httpx.Client(
                base_url=client._base_url,
                headers={"X-API-Key": "tk_test"},
                transport=mock_transport,
            )
            client.get("status")

    def test_base_url_override(self):
        client = _APIClient("dns", api_key="tk_test", base_url="http://localhost:8000")
        assert client._base_url == "http://localhost:8000"
        client.close()


# ------------------------------------------------------------------ #
#  Error mapping tests
# ------------------------------------------------------------------ #


class TestErrorMapping:
    """Verify HTTP status codes map to the correct exception type."""

    @pytest.mark.parametrize(
        "status,expected_exc",
        [
            (401, AuthenticationError),
            (403, AuthenticationError),
            (404, NotFoundError),
            (400, ValidationError),
            (422, ValidationError),
            (429, RateLimitError),
            (500, ServerError),
            (502, ServerError),
            (503, ServerError),
        ],
    )
    def test_status_to_exception(
        self,
        mock_transport_factory,
        status: int,
        expected_exc: type,
    ):
        transport = mock_transport_factory(
            status_code=status,
            json_body={"detail": "test error"},
        )
        client = _APIClient("dns", api_key="tk_test")
        client._client = httpx.Client(
            base_url=client._base_url,
            headers={"X-API-Key": "tk_test"},
            transport=transport,
        )

        with pytest.raises(expected_exc):
            client.get("lookup", params={"domain": "example.com"})
        client.close()

    def test_unknown_status_raises_api_error(self, mock_transport_factory):
        transport = mock_transport_factory(
            status_code=418,
            json_body={"detail": "I'm a teapot"},
        )
        client = _APIClient("dns", api_key="tk_test")
        client._client = httpx.Client(
            base_url=client._base_url,
            headers={"X-API-Key": "tk_test"},
            transport=transport,
        )

        with pytest.raises(APIError) as exc_info:
            client.get("lookup")
        assert exc_info.value.status_code == 418
        client.close()


# ------------------------------------------------------------------ #
#  Unified ToolkitAPI client tests
# ------------------------------------------------------------------ #


class TestToolkitAPIClient:
    """Tests for the top-level ToolkitAPI unified client."""

    def test_lazy_instantiation(self):
        tk = ToolkitAPI(api_key="tk_test")
        _ = tk.dns
        _ = tk.analytics
        tk.close()

    def test_same_instance_returned(self):
        tk = ToolkitAPI(api_key="tk_test")
        dns1 = tk.dns
        dns2 = tk.dns
        assert dns1 is dns2
        tk.close()

    def test_all_properties_return_correct_types(self):
        tk = ToolkitAPI(api_key="tk_test")
        assert isinstance(tk.analytics, Analytics)
        assert isinstance(tk.auth, Auth)
        assert isinstance(tk.barcode, Barcode)
        assert isinstance(tk.dev, Dev)
        assert isinstance(tk.dns, DNS)
        assert isinstance(tk.email, Email)
        assert isinstance(tk.geo, Geo)
        assert isinstance(tk.image, Image)
        assert isinstance(tk.media, Media)
        assert isinstance(tk.pdf, PDF)
        assert isinstance(tk.scrape, Scrape)
        assert isinstance(tk.textanalysis, Textanalysis)
        assert isinstance(tk.webhook, Webhook)
        tk.close()


class TestDNSEndpoints:
    """Request-shape regression tests for DNS helpers."""

    def test_compare_resolvers_maps_type_param(self, mock_transport: MockTransport):
        dns = DNS(api_key="tk_test")
        dns._client._client = httpx.Client(
            base_url=dns._client._base_url,
            headers={"X-API-Key": "tk_test", "Accept": "application/json"},
            transport=mock_transport,
        )

        result = dns.compare_resolvers("example.com", type_="MX")

        assert result == {"ok": True}
        req = mock_transport.requests[0]
        assert req.method == "GET"
        assert "/v1/compare-resolvers" in str(req.url)
        assert "domain=example.com" in str(req.url)
        assert "type=MX" in str(req.url)
        assert "type_=" not in str(req.url)
        dns.close()

    def test_close_and_context(self):
        with ToolkitAPI(api_key="tk_test") as tk:
            assert isinstance(tk.dns, DNS)


# ------------------------------------------------------------------ #
#  Toolkit class smoke tests
# ------------------------------------------------------------------ #


class TestDNSSmoke:
    """Verify a DNS method correctly delegates to the HTTP client."""

    def test_lookup_calls_get(self, mock_transport: MockTransport):
        dns = DNS(api_key="tk_test")
        dns._client._client = httpx.Client(
            base_url=dns._client._base_url,
            headers={"X-API-Key": "tk_test"},
            transport=mock_transport,
        )

        result = dns.lookup(domain="example.com", type_="A")

        assert result == {"ok": True}
        req = mock_transport.requests[0]
        assert req.method == "GET"
        assert "/v1/lookup" in str(req.url)
        dns.close()


class TestScrapeSmoke:
    """Verify scrape helpers target the current scrape API."""

    def test_scrape_body(self, mock_transport: MockTransport):
        scrape = Scrape(api_key="tk_test")
        scrape._client._client = httpx.Client(
            base_url=scrape._client._base_url,
            headers={"X-API-Key": "tk_test"},
            transport=mock_transport,
        )

        result = scrape.scrape(body={"url": "https://example.com", "output": "markdown"})

        assert result == {"ok": True}
        req = mock_transport.requests[0]
        assert req.method == "POST"
        assert "/v1/scrape" in str(req.url)

        import json
        body = json.loads(req.content)
        assert body["url"] == "https://example.com"
        scrape.close()

    def test_pdf_extract_uses_current_pdf_route(self, mock_transport: MockTransport):
        scrape = Scrape(api_key="tk_test")
        scrape._client._client = httpx.Client(
            base_url=scrape._client._base_url,
            headers={"X-API-Key": "tk_test"},
            transport=mock_transport,
        )

        scrape.pdf_extract(body={"url": "https://example.com/test.pdf", "pages": "1-2"})

        req = mock_transport.requests[0]
        assert req.method == "POST"
        assert "/v1/scrape/pdf" in str(req.url)
        scrape.close()

    def test_parse_robots_uses_current_route(self, mock_transport: MockTransport):
        scrape = Scrape(api_key="tk_test")
        scrape._client._client = httpx.Client(
            base_url=scrape._client._base_url,
            headers={"X-API-Key": "tk_test"},
            transport=mock_transport,
        )

        scrape.parse_robots(url="https://example.com")

        req = mock_transport.requests[0]
        assert req.method == "GET"
        assert "/v1/scrape/robots" in str(req.url)
        scrape.close()


class TestPDFSmoke:
    """Verify PDF helpers target the latest PDF toolkit routes."""

    def test_from_template_uses_current_route_and_payload(self, mock_transport: MockTransport):
        pdf = PDF(api_key="tk_test")
        pdf._client._client = httpx.Client(
            base_url=pdf._client._base_url,
            headers={"X-API-Key": "tk_test"},
            transport=mock_transport,
        )

        result = pdf.from_template(
            body={
                "template_url": "https://example.com/invoice.liquid",
                "variables": {"name": "Chris"},
                "strict": True,
                "page_size": "Letter",
            }
        )

        assert result == {"ok": True}
        req = mock_transport.requests[0]
        assert req.method == "POST"
        assert "/v1/pdf/from-template" in str(req.url)

        import json
        body = json.loads(req.content)
        assert body["template_url"] == "https://example.com/invoice.liquid"
        assert body["variables"]["name"] == "Chris"
        assert body["strict"] is True
        assert body["page_size"] == "Letter"
        pdf.close()

    def test_to_images_uses_latest_route(self, mock_transport: MockTransport):
        pdf = PDF(api_key="tk_test")
        pdf._client._client = httpx.Client(
            base_url=pdf._client._base_url,
            headers={"X-API-Key": "tk_test"},
            transport=mock_transport,
        )

        pdf.to_images(url="https://example.com/report.pdf", pages="1-2", format="jpeg", dpi=200)

        req = mock_transport.requests[0]
        assert req.method == "GET"
        assert "/v1/pdf/to-images" in str(req.url)
        pdf.close()

    def test_text_extract_uses_text_endpoint(self, mock_transport: MockTransport):
        pdf = PDF(api_key="tk_test")
        pdf._client._client = httpx.Client(
            base_url=pdf._client._base_url,
            headers={"X-API-Key": "tk_test"},
            transport=mock_transport,
        )

        pdf.text_extract(url="https://example.com/doc.pdf", pages="1-3")

        req = mock_transport.requests[0]
        assert req.method == "GET"
        assert "/v1/pdf/text" in str(req.url)
        pdf.close()


class TestImageSmoke:
    """Verify Image helpers target the latest Image toolkit routes."""

    def test_convert_image_body(self, mock_transport: MockTransport):
        image = Image(api_key="tk_test")
        image._client._client = httpx.Client(
            base_url=image._client._base_url,
            headers={"X-API-Key": "tk_test"},
            transport=mock_transport,
        )

        result = image.convert_image(body={
            "from_format": "png", "to_format": "webp",
            "url": "https://example.com/photo.png",
            "quality": 82, "width": 640,
        })

        assert result == {"ok": True}
        req = mock_transport.requests[0]
        assert req.method == "POST"
        assert "/v1/image/convert" in str(req.url)

        import json
        body = json.loads(req.content)
        assert body["from_format"] == "png"
        image.close()

    def test_from_template_uses_current_route_and_payload(self, mock_transport: MockTransport):
        image = Image(api_key="tk_test")
        image._client._client = httpx.Client(
            base_url=image._client._base_url,
            headers={"X-API-Key": "tk_test"},
            transport=mock_transport,
        )

        result = image.from_template(body={
            "template_url": "https://example.com/card.liquid",
            "variables": {"title": "Hello"},
            "width": 1200, "height": 630,
            "dark_mode": True, "format": "png",
        })

        assert result == {"ok": True}
        req = mock_transport.requests[0]
        assert req.method == "POST"
        assert "/v1/image/from-template" in str(req.url)

        import json
        body = json.loads(req.content)
        assert body["template_url"] == "https://example.com/card.liquid"
        image.close()


class TestTextAnalysisSmoke:
    """Verify a TextAnalysis method correctly delegates to the HTTP client."""

    def test_readability_calls_post(self, mock_transport: MockTransport):
        ta = Textanalysis(api_key="tk_test")
        ta._client._client = httpx.Client(
            base_url=ta._client._base_url,
            headers={"X-API-Key": "tk_test"},
            transport=mock_transport,
        )

        result = ta.readability_score(body={"text": "The quick brown fox."})

        assert result == {"ok": True}
        req = mock_transport.requests[0]
        assert req.method == "POST"
        assert "/v1/text/readability" in str(req.url)
        ta.close()


class TestWebhookSmoke:
    """Verify Webhook methods delegate correctly."""

    def test_create_bin_calls_post(self, mock_transport: MockTransport):
        wh = Webhook(api_key="tk_test")
        wh._client._client = httpx.Client(
            base_url=wh._client._base_url,
            headers={"X-API-Key": "tk_test"},
            transport=mock_transport,
        )

        result = wh.create_bin(body={"name": "test", "ttl_seconds": 3600})

        assert result == {"ok": True}
        req = mock_transport.requests[0]
        assert req.method == "POST"
        assert "/v1/bins" in str(req.url)
        wh.close()
