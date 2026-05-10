"""Compute Flesch-Kincaid, Gunning Fog, Coleman-Liau, and ARI readability
metrics for the given text."""

from __future__ import annotations

from typing import Dict, Any

from ._client import _APIClient


class Textanalysis:
    """Readability Score"""

    def __init__(
        self,
        api_key: str,
        *,
        base_url: Optional[str] = None,
        timeout: float = 30.0,
    ) -> None:
        self._client = _APIClient(
            "textanalysis", api_key, base_url=base_url, timeout=timeout
        )

    # ------------------------------------------------------------------ #
    #  Text
    # ------------------------------------------------------------------ #

    def readability_score(
        self,
        body: Dict[str, Any],
    ) -> Any:
        """Readability Score

        Args:
            body: Request body.
        """
        return self._client.post("text/readability", body=body)

    def summarize(
        self,
        body: Dict[str, Any],
    ) -> Any:
        """Summarize

        Args:
            body: Request body.
        """
        return self._client.post("text/summarize", body=body)

    def text_similarity(
        self,
        body: Dict[str, Any],
    ) -> Any:
        """Text Similarity

        Args:
            body: Request body.
        """
        return self._client.post("text/similarity", body=body)

    def text_diff(
        self,
        body: Dict[str, Any],
    ) -> Any:
        """Text Diff

        Args:
            body: Request body.
        """
        return self._client.post("text/diff", body=body)

    def data_mask(
        self,
        body: Dict[str, Any],
    ) -> Any:
        """Data Mask

        Args:
            body: Request body.
        """
        return self._client.post("text/pii-mask", body=body)

    def profanity_filter(
        self,
        body: Dict[str, Any],
    ) -> Any:
        """Profanity Filter

        Args:
            body: Request body.
        """
        return self._client.post("text/profanity", body=body)

    def word_frequency(
        self,
        body: Dict[str, Any],
    ) -> Any:
        """Word Frequency

        Args:
            body: Request body.
        """
        return self._client.post("text/word-frequency", body=body)

    def detect_language(
        self,
        body: Dict[str, Any],
    ) -> Any:
        """Detect Language

        Args:
            body: Request body.
        """
        return self._client.post("text/language", body=body)

    def transliterate_text(
        self,
        body: Dict[str, Any],
    ) -> Any:
        """Transliterate Text

        Args:
            body: Request body.
        """
        return self._client.post("text/transliterate", body=body)

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

    def __enter__(self) -> "Textanalysis":
        return self

    def __exit__(self, *args: Any) -> None:
        self.close()
