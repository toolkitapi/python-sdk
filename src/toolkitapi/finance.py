"""Finance toolkit — currency conversion and VAT/GST rate lookups."""

from __future__ import annotations

from typing import Any, Optional

from ._client import _APIClient


class Finance:
    """Currency conversion (ECB daily rates) and VAT/GST rate lookups.

    Example::

        from toolkitapi import Finance

        fin = Finance(api_key="tk_...")
        result = fin.convert_currency(amount=100, from_currency="USD", to_currency="EUR")
    """

    def __init__(
        self,
        api_key: str,
        *,
        base_url: Optional[str] = None,
        timeout: float = 30.0,
    ) -> None:
        self._client = _APIClient(
            "finance", api_key, base_url=base_url, timeout=timeout
        )

    # ------------------------------------------------------------------ #
    #  Endpoints
    # ------------------------------------------------------------------ #

    def convert_currency(
        self,
        *,
        amount: float,
        from_currency: str,
        to_currency: str,
    ) -> Any:
        """Convert an amount between two currencies using ECB daily rates.

        Args:
            amount: Amount to convert.
            from_currency: Source ISO-4217 currency code (e.g. ``"USD"``).
            to_currency: Target ISO-4217 currency code (e.g. ``"EUR"``).
        """
        return self._client.post(
            "finance/currency-convert",
            body={
                "amount": amount,
                "from_currency": from_currency,
                "to_currency": to_currency,
            },
        )

    def list_currencies(self) -> Any:
        """Return all supported currency codes and their full names."""
        return self._client.get("finance/currencies")

    def vat_rates(self, *, country: Optional[str] = None) -> Any:
        """Return standard and reduced VAT/GST rates, optionally filtered by country.

        Args:
            country: ISO country code (e.g. ``"DE"``, ``"GB"``). When omitted
                returns rates for all supported countries.
        """
        return self._client.get(
            "finance/vat-rates", params={"country": country}
        )

    # ------------------------------------------------------------------ #
    #  Lifecycle
    # ------------------------------------------------------------------ #

    def close(self) -> None:
        """Close the underlying HTTP client."""
        self._client.close()

    def __enter__(self) -> "Finance":
        return self

    def __exit__(self, *args: Any) -> None:
        self.close()
