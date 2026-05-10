"""AI text toolkit — Gemini-powered extraction, classification, summarization, and more."""

from __future__ import annotations

from typing import Any, Dict, List, Literal, Optional

from ._client import _APIClient

_Model = Literal["gemini-2.0-flash", "gemini-2.0-flash-lite", "gemini-1.5-flash"]
_SummarizeStyle = Literal["paragraph", "bullets", "one_line"]
_TranslateTone = Literal["formal", "casual", "neutral"]
_RewriteTone = Literal[
    "formal",
    "casual",
    "concise",
    "persuasive",
    "friendly",
    "professional",
    "technical",
    "simple",
]


class AiText:
    """AI-powered text utilities backed by Gemini models.

    Covers structured extraction, classification, summarization, sentiment
    analysis, translation, rewriting, and named-entity recognition.

    Example::

        from toolkitapi import AiText

        ai = AiText(api_key="tk_...")
        result = ai.summarize(text="...", style="bullets")
    """

    def __init__(
        self,
        api_key: str,
        *,
        base_url: Optional[str] = None,
        timeout: float = 30.0,
    ) -> None:
        self._client = _APIClient(
            "ai-text", api_key, base_url=base_url, timeout=timeout
        )

    # ------------------------------------------------------------------ #
    #  Endpoints
    # ------------------------------------------------------------------ #

    def extract(
        self,
        *,
        text: str,
        schema: Dict[str, Any],
        model: _Model = "gemini-2.0-flash",
        temperature: float = 0.1,
    ) -> Any:
        """Extract structured data from free-form text matching a JSON Schema.

        Args:
            text: Raw text to extract structured data from (max 4000 chars).
            schema: JSON Schema describing the desired output structure.
            model: Gemini model to use.
            temperature: LLM temperature (0.0-1.0, lower = more deterministic).
        """
        return self._client.post(
            "ai/extract",
            body={
                "text": text,
                "schema": schema,
                "model": model,
                "temperature": temperature,
            },
        )

    def classify(
        self,
        *,
        text: str,
        categories: List[str],
        multi_label: bool = False,
        model: _Model = "gemini-2.0-flash",
        temperature: float = 0.1,
    ) -> Any:
        """Classify text into one (or many) of the supplied categories.

        Args:
            text: Text to classify (max 4000 chars).
            categories: 2-50 candidate category labels.
            multi_label: If True, allow multiple matching categories.
            model: Gemini model to use.
            temperature: LLM temperature (0.0-1.0).
        """
        return self._client.post(
            "ai/classify",
            body={
                "text": text,
                "categories": categories,
                "multi_label": multi_label,
                "model": model,
                "temperature": temperature,
            },
        )

    def summarize(
        self,
        *,
        text: str,
        max_length: int = 150,
        style: _SummarizeStyle = "paragraph",
        model: _Model = "gemini-2.0-flash",
        temperature: float = 0.3,
    ) -> Any:
        """Summarize text in paragraph, bullet, or one-line form.

        Args:
            text: Text to summarize (max 8000 chars).
            max_length: Target summary length in words (10-1000).
            style: Output style — ``paragraph``, ``bullets``, or ``one_line``.
            model: Gemini model to use.
            temperature: LLM temperature (0.0-1.0).
        """
        return self._client.post(
            "ai/summarize",
            body={
                "text": text,
                "max_length": max_length,
                "style": style,
                "model": model,
                "temperature": temperature,
            },
        )

    def sentiment(
        self,
        *,
        text: str,
        model: _Model = "gemini-2.0-flash",
        temperature: float = 0.1,
    ) -> Any:
        """Analyze sentiment (positive/negative/neutral) and intensity.

        Args:
            text: Text to analyze (max 4000 chars).
            model: Gemini model to use.
            temperature: LLM temperature (0.0-1.0).
        """
        return self._client.post(
            "ai/sentiment",
            body={"text": text, "model": model, "temperature": temperature},
        )

    def translate(
        self,
        *,
        text: str,
        target_language: str,
        source_language: Optional[str] = None,
        tone: _TranslateTone = "neutral",
        model: _Model = "gemini-2.0-flash",
        temperature: float = 0.3,
    ) -> Any:
        """Translate text between languages with optional tone control.

        Args:
            text: Text to translate (max 4000 chars).
            target_language: Target language (e.g. ``"Spanish"``, ``"ja"``).
            source_language: Source language; auto-detected if omitted.
            tone: ``formal``, ``casual``, or ``neutral``.
            model: Gemini model to use.
            temperature: LLM temperature (0.0-1.0).
        """
        return self._client.post(
            "ai/translate",
            body={
                "text": text,
                "target_language": target_language,
                "source_language": source_language,
                "tone": tone,
                "model": model,
                "temperature": temperature,
            },
        )

    def rewrite(
        self,
        *,
        text: str,
        tone: _RewriteTone,
        instructions: Optional[str] = None,
        model: _Model = "gemini-2.0-flash",
        temperature: float = 0.5,
    ) -> Any:
        """Rewrite text in a target tone with optional extra instructions.

        Args:
            text: Text to rewrite (max 4000 chars).
            tone: One of ``formal``, ``casual``, ``concise``, ``persuasive``,
                ``friendly``, ``professional``, ``technical``, ``simple``.
            instructions: Additional rewrite instructions (max 500 chars).
            model: Gemini model to use.
            temperature: LLM temperature (0.0-1.0).
        """
        return self._client.post(
            "ai/rewrite",
            body={
                "text": text,
                "tone": tone,
                "instructions": instructions,
                "model": model,
                "temperature": temperature,
            },
        )

    def entities(
        self,
        *,
        text: str,
        entity_types: Optional[List[str]] = None,
        model: _Model = "gemini-2.0-flash",
        temperature: float = 0.1,
    ) -> Any:
        """Extract named entities (people, places, organizations, etc.).

        Args:
            text: Text to extract entities from (max 4000 chars).
            entity_types: Entity types to extract (e.g. ``["person", "location"]``).
                When omitted, all types are returned.
            model: Gemini model to use.
            temperature: LLM temperature (0.0-1.0).
        """
        return self._client.post(
            "ai/entities",
            body={
                "text": text,
                "entity_types": entity_types,
                "model": model,
                "temperature": temperature,
            },
        )

    # ------------------------------------------------------------------ #
    #  Lifecycle
    # ------------------------------------------------------------------ #

    def close(self) -> None:
        """Close the underlying HTTP client."""
        self._client.close()

    def __enter__(self) -> "AiText":
        return self

    def __exit__(self, *args: Any) -> None:
        self.close()
