"""ToolkitAPI — Official Python SDK for ToolkitAPI.io.

Quick-start with a single toolkit::

    from toolkitapi import DNS

    dns = DNS(api_key="tk_...")
    result = dns.lookup(domain="example.com", type="A")

Or use the unified client for multi-toolkit workflows::

    from toolkitapi import ToolkitAPI

    tk = ToolkitAPI(api_key="tk_...")
    dns_result = tk.dns.lookup(domain="example.com")
    scores = tk.textanalysis.readability(text="Hello world.")
    tk.close()
"""

from __future__ import annotations

from typing import Any, Dict, List, Optional, Type

from . import analytics as _analytics
from . import auth as _auth
from . import barcode as _barcode
from . import convert as _convert
from . import devtools as _devtools
from . import dns as _dns
from . import email as _email
from . import geo as _geo
from . import image as _image
from . import media as _media
from . import pdf as _pdf
from . import scrape as _scrape
from . import textanalysis as _textanalysis
from . import webhook as _webhook

from .analytics import Analytics
from .auth import Auth
from .barcode import Barcode
from .convert import Convert
from .devtools import Devtools
from .dns import DNS
from .email import Email
from .geo import Geo
from .image import Image
from .media import Media
from .pdf import PDF
from .scrape import Scrape
from .textanalysis import Textanalysis
from .webhook import Webhook
from ._exceptions import (
    APIError,
    AuthenticationError,
    NotFoundError,
    RateLimitError,
    ServerError,
    ToolkitAPIError,
    ValidationError,
)

__all__ = [
    "Analytics",
    "Auth",
    "Barcode",
    "Convert",
    "Devtools",
    "DNS",
    "Email",
    "Geo",
    "Image",
    "Media",
    "PDF",
    "Scrape",
    "Textanalysis",
    "Webhook",
    "ToolkitAPI"
]


__version__ = "2.0.0b1"


class ToolkitAPI:
    """Unified entry point for all ToolkitAPI services.

    Example::

        from toolkitapi import ToolkitAPI

        tk = ToolkitAPI(api_key="tk_...")
        print(tk.dns.lookup("example.com"))
        print(tk.auth.hash_password("mypassword"))
        tk.close()
    """

    def __init__(
        self,
        api_key: str,
        *,
        base_url: Optional[str] = None,
        timeout: float = 30.0,
    ) -> None:
        self._api_key = api_key
        self._base_url = base_url
        self._timeout = timeout

        self.analytics: _analytics.Analytics = _analytics.Analytics(api_key, base_url=base_url, timeout=timeout)  # type: ignore[valid-type]
        self.auth: _auth.Auth = _auth.Auth(api_key, base_url=base_url, timeout=timeout)  # type: ignore[valid-type]
        self.barcode: _barcode.Barcode = _barcode.Barcode(api_key, base_url=base_url, timeout=timeout)  # type: ignore[valid-type]
        self.convert: _convert.Convert = _convert.Convert(api_key, base_url=base_url, timeout=timeout)  # type: ignore[valid-type]
        self.devtools: _devtools.Devtools = _devtools.Devtools(api_key, base_url=base_url, timeout=timeout)  # type: ignore[valid-type]
        self.dns: _dns.DNS = _dns.DNS(api_key, base_url=base_url, timeout=timeout)  # type: ignore[valid-type]
        self.email: _email.Email = _email.Email(api_key, base_url=base_url, timeout=timeout)  # type: ignore[valid-type]
        self.geo: _geo.Geo = _geo.Geo(api_key, base_url=base_url, timeout=timeout)  # type: ignore[valid-type]
        self.image: _image.Image = _image.Image(api_key, base_url=base_url, timeout=timeout)  # type: ignore[valid-type]
        self.media: _media.Media = _media.Media(api_key, base_url=base_url, timeout=timeout)  # type: ignore[valid-type]
        self.pdf: _pdf.PDF = _pdf.PDF(api_key, base_url=base_url, timeout=timeout)  # type: ignore[valid-type]
        self.scrape: _scrape.Scrape = _scrape.Scrape(api_key, base_url=base_url, timeout=timeout)  # type: ignore[valid-type]
        self.textanalysis: _textanalysis.Textanalysis = _textanalysis.Textanalysis(api_key, base_url=base_url, timeout=timeout)  # type: ignore[valid-type]
        self.webhook: _webhook.Webhook = _webhook.Webhook(api_key, base_url=base_url, timeout=timeout)  # type: ignore[valid-type]

    def close(self) -> None:
        """Close all underlying HTTP clients."""
        self.analytics.close()
        self.auth.close()
        self.barcode.close()
        self.convert.close()
        self.devtools.close()
        self.dns.close()
        self.email.close()
        self.geo.close()
        self.image.close()
        self.media.close()
        self.pdf.close()
        self.scrape.close()
        self.textanalysis.close()
        self.webhook.close()

    def __enter__(self) -> "ToolkitAPI":
        return self

    def __exit__(self, *args: Any) -> None:
        self.close()
