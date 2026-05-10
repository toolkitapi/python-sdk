"""Resolve an IP address to its geographic location (city, region, country, coordinates)."""

from __future__ import annotations

from typing import Dict, Any, Optional

from ._client import _APIClient


class Geo:
    """IP geolocation lookup"""

    def __init__(
        self,
        api_key: str,
        *,
        base_url: Optional[str] = None,
        timeout: float = 30.0,
    ) -> None:
        self._client = _APIClient(
            "geo", api_key, base_url=base_url, timeout=timeout
        )

    # ------------------------------------------------------------------ #
    #  Geo
    # ------------------------------------------------------------------ #

    def ip_lookup(
        self,
        ip: str,
    ) -> Dict[str, Any]:
        """IP geolocation lookup

        Args:
            ip: IPv4 or IPv6 address to look up
        """
        return self._client.get("geo/ip-lookup", params={"ip": ip})

    def ip_threat(
        self,
        ip: str,
    ) -> Dict[str, Any]:
        """IP threat / anonymity detection

        Args:
            ip: IPv4 or IPv6 address to check
        """
        return self._client.get("geo/ip-threat", params={"ip": ip})

    def distance(
        self,
        body: Dict[str, Any],
    ) -> Dict[str, Any]:
        """Calculate distance between coordinates

        Args:
            body: Request body.
        """
        return self._client.post("geo/distance", body=body)

    def bounding_box(
        self,
        body: Dict[str, Any],
    ) -> Dict[str, Any]:
        """Calculate a geographic bounding box

        Args:
            body: Request body.
        """
        return self._client.post("geo/bounding-box", body=body)

    def center(
        self,
        body: Dict[str, Any],
    ) -> Dict[str, Any]:
        """Find the geographic center of coordinates

        Args:
            body: Request body.
        """
        return self._client.post("geo/center", body=body)

    def country_info(
        self,
        code: str,
    ) -> Dict[str, Any]:
        """Get country information by ISO code

        Args:
            code: ISO 3166-1 alpha-2 country code (e.g. US, GB, DE)
        """
        return self._client.get("geo/country-info", params={"code": code})

    def currency_info(
        self,
        code: str,
    ) -> Dict[str, Any]:
        """Get currency information by code

        Args:
            code: ISO 4217 currency code (e.g. USD, EUR, GBP)
        """
        return self._client.get("geo/currency-info", params={"code": code})

    def timezone_convert(
        self,
        timestamp: str,
        from_: str,
        to: str,
    ) -> Dict[str, Any]:
        """Convert a timestamp between timezones

        Args:
            timestamp: ISO 8601 timestamp (e.g. 2026-03-31T14:30:00)
            from_: Source IANA timezone (e.g. America/New_York)
            to: Target IANA timezone (e.g. Europe/London)
        """
        return self._client.get("geo/timezone-convert", params={"timestamp": timestamp, "from_": from_, "to": to})

    def timezone_by_coords(
        self,
        lat: float,
        lon: float,
    ) -> Dict[str, Any]:
        """Get timezone for coordinates

        Args:
            lat: Latitude
            lon: Longitude
        """
        return self._client.get("geo/timezone-by-coords", params={"lat": lat, "lon": lon})

    def timezone_info(
        self,
        timezone: str,
    ) -> Dict[str, Any]:
        """Get timezone details

        Args:
            timezone: IANA timezone name (e.g. America/New_York, Europe/London)
        """
        return self._client.get("geo/timezone-info", params={"timezone": timezone})

    def phone_validate(
        self,
        number: str,
        *,
        country: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Validate and parse a phone number (E.164)

        Args:
            number: Phone number to validate (any format)
            country: Default country code (ISO 3166-1 alpha-2)
        """
        return self._client.get("geo/phone-validate", params={"number": number, "country": country})

    def phone_validate_batch(
        self,
        body: Dict[str, Any],
    ) -> Dict[str, Any]:
        """Batch phone number validation

        Args:
            body: Request body.
        """
        return self._client.post("geo/phone-validate-batch", body=body)

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

    def __enter__(self) -> "Geo":
        return self

    def __exit__(self, *args: Any) -> None:
        self.close()
