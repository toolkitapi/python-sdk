"""Check CSV for ragged rows, empty rows, quoting issues, and other problems."""

from __future__ import annotations

from typing import Dict, Any, Optional

from ._client import _APIClient


class Devtools:
    """Json Validate"""

    def __init__(
        self,
        api_key: str,
        *,
        base_url: Optional[str] = None,
        timeout: float = 30.0,
    ) -> None:
        self._client = _APIClient(
            "devtools", api_key, base_url=base_url, timeout=timeout
        )

    # ------------------------------------------------------------------ #
    #  Json Validate
    # ------------------------------------------------------------------ #

    def json_validate(
        self,
        body: Dict[str, Any],
    ) -> Any:
        """Json Validate

        Args:
            body: Request body.
        """
        return self._client.post("json-validate", body=body)

    # ------------------------------------------------------------------ #
    #  Json Diff
    # ------------------------------------------------------------------ #

    def json_diff(
        self,
        body: Dict[str, Any],
    ) -> Any:
        """Json Diff

        Args:
            body: Request body.
        """
        return self._client.post("json-diff", body=body)

    # ------------------------------------------------------------------ #
    #  Yaml Validate
    # ------------------------------------------------------------------ #

    def yaml_validate(
        self,
        body: Dict[str, Any],
    ) -> Any:
        """Yaml Validate

        Args:
            body: Request body.
        """
        return self._client.post("yaml-validate", body=body)

    # ------------------------------------------------------------------ #
    #  Xml Validate
    # ------------------------------------------------------------------ #

    def xml_validate(
        self,
        body: Dict[str, Any],
    ) -> Any:
        """Xml Validate

        Args:
            body: Request body.
        """
        return self._client.post("xml-validate", body=body)

    # ------------------------------------------------------------------ #
    #  Toml Validate
    # ------------------------------------------------------------------ #

    def toml_validate(
        self,
        body: Dict[str, Any],
    ) -> Any:
        """Toml Validate

        Args:
            body: Request body.
        """
        return self._client.post("toml-validate", body=body)

    # ------------------------------------------------------------------ #
    #  Json Schema Validate
    # ------------------------------------------------------------------ #

    def json_schema_validate(
        self,
        body: Dict[str, Any],
    ) -> Any:
        """Json Schema Validate

        Args:
            body: Request body.
        """
        return self._client.post("json-schema-validate", body=body)

    # ------------------------------------------------------------------ #
    #  Jsonpath
    # ------------------------------------------------------------------ #

    def jsonpath_query(
        self,
        body: Dict[str, Any],
    ) -> Any:
        """Jsonpath Query

        Args:
            body: Request body.
        """
        return self._client.post("jsonpath", body=body)

    # ------------------------------------------------------------------ #
    #  Json To Schema
    # ------------------------------------------------------------------ #

    def json_to_schema(
        self,
        body: Dict[str, Any],
    ) -> Any:
        """Json To Schema

        Args:
            body: Request body.
        """
        return self._client.post("json-to-schema", body=body)

    # ------------------------------------------------------------------ #
    #  Csv Lint
    # ------------------------------------------------------------------ #

    def csv_lint(
        self,
        body: Dict[str, Any],
    ) -> Any:
        """Lint and validate CSV data

        Args:
            body: Request body.
        """
        return self._client.post("csv-lint", body=body)

    # ------------------------------------------------------------------ #
    #  Uuid
    # ------------------------------------------------------------------ #

    def generate_uuid(
        self,
        *,
        version: Optional[str] = None,
        count: Optional[int] = None,
    ) -> Any:
        """Generate Uuid

        Args:
            version: ID type
            count: How many to generate
        """
        return self._client.get("uuid", params={"version": version, "count": count})

    # ------------------------------------------------------------------ #
    #  Password Gen
    # ------------------------------------------------------------------ #

    def password_gen(
        self,
        *,
        length: Optional[int] = None,
        uppercase: Optional[bool] = None,
        lowercase: Optional[bool] = None,
        numbers: Optional[bool] = None,
        symbols: Optional[bool] = None,
        count: Optional[int] = None,
    ) -> Any:
        """Password Gen

        Args:
            length: Password length
            uppercase: 
            lowercase: 
            numbers: 
            symbols: 
            count: 
        """
        return self._client.get("password-gen", params={"length": length, "uppercase": uppercase, "lowercase": lowercase, "numbers": numbers, "symbols": symbols, "count": count})

    # ------------------------------------------------------------------ #
    #  Lorem Ipsum
    # ------------------------------------------------------------------ #

    def lorem_ipsum(
        self,
        *,
        paragraphs: Optional[int] = None,
        sentences: Optional[int] = None,
        words: Optional[int] = None,
    ) -> Any:
        """Lorem Ipsum

        Args:
            paragraphs: 
            sentences: 
            words: 
        """
        return self._client.get("lorem-ipsum", params={"paragraphs": paragraphs, "sentences": sentences, "words": words})

    # ------------------------------------------------------------------ #
    #  Fake Data
    # ------------------------------------------------------------------ #

    def fake_data(
        self,
        type_: str,
        *,
        count: Optional[int] = None,
    ) -> Any:
        """Fake Data

        Args:
            type_: Type of fake data
            count: 
        """
        return self._client.get("fake-data", params={"type_": type_, "count": count})

    # ------------------------------------------------------------------ #
    #  Regex Test
    # ------------------------------------------------------------------ #

    def regex_test(
        self,
        body: Dict[str, Any],
    ) -> Any:
        """Regex Test

        Args:
            body: Request body.
        """
        return self._client.post("regex-test", body=body)

    # ------------------------------------------------------------------ #
    #  Regex Extract
    # ------------------------------------------------------------------ #

    def regex_extract(
        self,
        body: Dict[str, Any],
    ) -> Any:
        """Regex Extract

        Args:
            body: Request body.
        """
        return self._client.post("regex-extract", body=body)

    # ------------------------------------------------------------------ #
    #  Regex Parse
    # ------------------------------------------------------------------ #

    def regex_parse(
        self,
        body: Dict[str, Any],
    ) -> Any:
        """Regex Parse

        Args:
            body: Request body.
        """
        return self._client.post("regex-parse", body=body)

    # ------------------------------------------------------------------ #
    #  Cron Parse
    # ------------------------------------------------------------------ #

    def cron_parse(
        self,
        expression: str,
        *,
        count: Optional[int] = None,
        tz: Optional[str] = None,
    ) -> Any:
        """Cron Parse

        Args:
            expression: Cron expression
            count: Number of next scheduled times
            tz: Timezone for output
        """
        return self._client.get("cron-parse", params={"expression": expression, "count": count, "tz": tz})

    # ------------------------------------------------------------------ #
    #  Cron Next
    # ------------------------------------------------------------------ #

    def cron_next(
        self,
        expression: str,
        *,
        count: Optional[int] = None,
        from_date: Optional[str] = None,
    ) -> Any:
        """Cron Next

        Args:
            expression: Cron expression
            count: Number of next executions
            from_date: Start date ISO 8601 (default: now)
        """
        return self._client.get("cron-next", params={"expression": expression, "count": count, "from_date": from_date})

    # ------------------------------------------------------------------ #
    #  Timestamp
    # ------------------------------------------------------------------ #

    def timestamp(
        self,
        *,
        ts: Optional[float] = None,
        iso: Optional[str] = None,
    ) -> Any:
        """Timestamp

        Args:
            ts: Unix timestamp
            iso: ISO 8601 datetime string
        """
        return self._client.get("timestamp", params={"ts": ts, "iso": iso})

    # ------------------------------------------------------------------ #
    #  User Agent
    # ------------------------------------------------------------------ #

    def user_agent(
        self,
        body: Dict[str, Any],
    ) -> Any:
        """User Agent

        Args:
            body: Request body.
        """
        return self._client.post("user-agent", body=body)

    # ------------------------------------------------------------------ #
    #  Color Convert
    # ------------------------------------------------------------------ #

    def color_convert(
        self,
        color: str,
    ) -> Any:
        """Color Convert

        Args:
            color: Color value, e.g. #FF5733 or rgb(255,87,51)
        """
        return self._client.get("color-convert", params={"color": color})

    # ------------------------------------------------------------------ #
    #  Base Convert
    # ------------------------------------------------------------------ #

    def base_convert(
        self,
        value: str,
        *,
        from_base: Optional[int] = None,
        to_base: Optional[int] = None,
    ) -> Any:
        """Base Convert

        Args:
            value: Number to convert
            from_base: Source base
            to_base: Target base
        """
        return self._client.get("base-convert", params={"value": value, "from_base": from_base, "to_base": to_base})

    # ------------------------------------------------------------------ #
    #  Semver Compare
    # ------------------------------------------------------------------ #

    def semver_compare(
        self,
        body: Dict[str, Any],
    ) -> Any:
        """Semver Compare

        Args:
            body: Request body.
        """
        return self._client.post("semver-compare", body=body)

    # ------------------------------------------------------------------ #
    #  Chmod Calc
    # ------------------------------------------------------------------ #

    def chmod_calc(
        self,
        mode: str,
    ) -> Any:
        """Chmod Calc

        Args:
            mode: Permission mode — octal (e.g. 755) or symbolic (e.g. rwxr-xr-x)
        """
        return self._client.get("chmod-calc", params={"mode": mode})

    # ------------------------------------------------------------------ #
    #  Env Parse
    # ------------------------------------------------------------------ #

    def env_parse(
        self,
        body: Dict[str, Any],
    ) -> Any:
        """Env Parse

        Args:
            body: Request body.
        """
        return self._client.post("env-parse", body=body)

    # ------------------------------------------------------------------ #
    #  Diff
    # ------------------------------------------------------------------ #

    def diff_text(
        self,
        body: Dict[str, Any],
    ) -> Any:
        """Diff Text

        Args:
            body: Request body.
        """
        return self._client.post("diff", body=body)

    # ------------------------------------------------------------------ #
    #  Slug
    # ------------------------------------------------------------------ #

    def slugify(
        self,
        body: Dict[str, Any],
    ) -> Any:
        """Slugify

        Args:
            body: Request body.
        """
        return self._client.post("slug", body=body)

    # ------------------------------------------------------------------ #
    #  Word Count
    # ------------------------------------------------------------------ #

    def word_count(
        self,
        body: Dict[str, Any],
    ) -> Any:
        """Word Count

        Args:
            body: Request body.
        """
        return self._client.post("word-count", body=body)

    # ------------------------------------------------------------------ #
    #  Sql Format
    # ------------------------------------------------------------------ #

    def sql_format(
        self,
        body: Dict[str, Any],
    ) -> Any:
        """Sql Format

        Args:
            body: Request body.
        """
        return self._client.post("sql-format", body=body)

    # ------------------------------------------------------------------ #
    #  Text Escape
    # ------------------------------------------------------------------ #

    def text_escape(
        self,
        body: Dict[str, Any],
    ) -> Any:
        """Text Escape

        Args:
            body: Request body.
        """
        return self._client.post("text-escape", body=body)

    # ------------------------------------------------------------------ #
    #  Text Truncate
    # ------------------------------------------------------------------ #

    def text_truncate(
        self,
        body: Dict[str, Any],
    ) -> Any:
        """Text Truncate

        Args:
            body: Request body.
        """
        return self._client.post("text-truncate", body=body)

    # ------------------------------------------------------------------ #
    #  Code Format
    # ------------------------------------------------------------------ #

    def code_format(
        self,
        body: Dict[str, Any],
    ) -> Any:
        """Code Format

        Args:
            body: Request body.
        """
        return self._client.post("code-format", body=body)

    # ------------------------------------------------------------------ #
    #  Liquid Render
    # ------------------------------------------------------------------ #

    def liquid_render(
        self,
        body: Dict[str, Any],
    ) -> Any:
        """Liquid Render

        Args:
            body: Request body.
        """
        return self._client.post("liquid-render", body=body)

    # ------------------------------------------------------------------ #
    #  Json Transform
    # ------------------------------------------------------------------ #

    def json_transform(
        self,
        body: Dict[str, Any],
    ) -> Any:
        """Json Transform

        Args:
            body: Request body.
        """
        return self._client.post("json-transform", body=body)

    # ------------------------------------------------------------------ #
    #  Math Eval
    # ------------------------------------------------------------------ #

    def math_eval(
        self,
        body: Dict[str, Any],
    ) -> Any:
        """Math Eval

        Args:
            body: Request body.
        """
        return self._client.post("math-eval", body=body)

    # ------------------------------------------------------------------ #
    #  Date Format
    # ------------------------------------------------------------------ #

    def date_format(
        self,
        body: Dict[str, Any],
    ) -> Any:
        """Date Format

        Args:
            body: Request body.
        """
        return self._client.post("date-format", body=body)

    # ------------------------------------------------------------------ #
    #  Json Flatten
    # ------------------------------------------------------------------ #

    def json_flatten(
        self,
        body: Dict[str, Any],
    ) -> Any:
        """Json Flatten

        Args:
            body: Request body.
        """
        return self._client.post("json-flatten", body=body)

    # ------------------------------------------------------------------ #
    #  Array Ops
    # ------------------------------------------------------------------ #

    def array_ops(
        self,
        body: Dict[str, Any],
    ) -> Any:
        """Array Ops

        Args:
            body: Request body.
        """
        return self._client.post("array-ops", body=body)

    # ------------------------------------------------------------------ #
    #  Number Format
    # ------------------------------------------------------------------ #

    def number_format(
        self,
        body: Dict[str, Any],
    ) -> Any:
        """Number Format

        Args:
            body: Request body.
        """
        return self._client.post("number-format", body=body)

    # ------------------------------------------------------------------ #
    #  Mock Data
    # ------------------------------------------------------------------ #

    def mock_data(
        self,
        body: Dict[str, Any],
    ) -> Any:
        """Mock Data

        Args:
            body: Request body.
        """
        return self._client.post("mock-data", body=body)

    # ------------------------------------------------------------------ #
    #  Mock Schema
    # ------------------------------------------------------------------ #

    def mock_schema(
        self,
        body: Dict[str, Any],
    ) -> Any:
        """Mock Schema

        Args:
            body: Request body.
        """
        return self._client.post("mock-schema", body=body)

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

    def __enter__(self) -> "Devtools":
        return self

    def __exit__(self, *args: Any) -> None:
        self.close()
