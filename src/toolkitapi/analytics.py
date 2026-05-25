"""Probe the schema of a remote CSV/JSON/Parquet file, generate an optimized ClickHouse SQL query from your natural language prompt, execute it, and return a preview of the results plus a plain-English summary.

MCP flow: call this first to get `dataset_id`, then call `/v1/datasets/{dataset_id}/schema`, `/v1/validate-chart`, and `/v1/visualize`.

Set `include_debug=true` to receive the generated SQL and execution metrics.

Client guidance: retry transient 5xx responses with exponential backoff. Do not retry 4xx responses without changing request input."""

from __future__ import annotations

from typing import Dict, Any

from ._client import _APIClient


class Analytics:
    """Analyze a remote dataset with natural language"""

    def __init__(
        self,
        api_key: str,
        *,
        base_url: Optional[str] = None,
        timeout: float = 30.0,
    ) -> None:
        self._client = _APIClient(
            "analytics", api_key, base_url=base_url, timeout=timeout
        )

    # ------------------------------------------------------------------ #
    #  Analyze
    # ------------------------------------------------------------------ #

    def analyze(
        self,
        body: Dict[str, Any],
    ) -> Dict[str, Any]:
        """Analyze a remote dataset with natural language

        Args:
            body: Request body.
        """
        return self._client.post("analyze", body=body)

    # ------------------------------------------------------------------ #
    #  Save
    # ------------------------------------------------------------------ #

    def save(
        self,
        body: Dict[str, Any],
    ) -> Dict[str, Any]:
        """Save analysis logic for replay

        Args:
            body: Request body.
        """
        return self._client.post("save", body=body)

    # ------------------------------------------------------------------ #
    #  Query
    # ------------------------------------------------------------------ #

    def run_saved_query(
        self,
        query_id: str,
        body: Dict[str, Any],
    ) -> Dict[str, Any]:
        """Re-execute saved analysis logic

        Args:
            query_id: 
            body: Request body.
        """
        return self._client.post(
            "query/{query_id}",
            body=body,
            params={"query_id": query_id},
        )

    # ------------------------------------------------------------------ #
    #  Visualize
    # ------------------------------------------------------------------ #

    def visualize(
        self,
        body: Dict[str, Any],
    ) -> Dict[str, Any]:
        """Generate a chart from a dataset

        Args:
            body: Request body.
        """
        return self._client.post("visualize", body=body)

    # ------------------------------------------------------------------ #
    #  Image
    # ------------------------------------------------------------------ #

    def download_generated_image(
        self,
        image_id: str,
    ) -> Any:
        """Download a generated chart image

        Args:
            image_id: 
        """
        return self._client.get("image/download/{image_id}", params={"image_id": image_id})

    # ------------------------------------------------------------------ #
    #  Validate Chart
    # ------------------------------------------------------------------ #

    def validate_chart(
        self,
        body: Dict[str, Any],
    ) -> Dict[str, Any]:
        """Validate a chart spec without executing

        Args:
            body: Request body.
        """
        return self._client.post("validate-chart", body=body)

    # ------------------------------------------------------------------ #
    #  Datasets
    # ------------------------------------------------------------------ #

    def get_schema(
        self,
        dataset_id: str,
    ) -> Dict[str, Any]:
        """Retrieve dataset schema

        Args:
            dataset_id: 
        """
        return self._client.get("datasets/{dataset_id}/schema", params={"dataset_id": dataset_id})

    def create_bundle(
        self,
        body: Dict[str, Any],
    ) -> Dict[str, Any]:
        """Register a multi-source bundle for joins

        Args:
            body: Request body.
        """
        return self._client.post("datasets/bundle", body=body)

    # ------------------------------------------------------------------ #
    #  Jobs
    # ------------------------------------------------------------------ #

    def get_job_status(
        self,
        job_id: str,
    ) -> Dict[str, Any]:
        """Poll async job status

        Args:
            job_id: 
        """
        return self._client.get("jobs/{job_id}", params={"job_id": job_id})

    # ------------------------------------------------------------------ #
    #  Status
    # ------------------------------------------------------------------ #

    def status(
        self,
    ) -> Dict[str, Any]:
        """Service health check
        """
        return self._client.get("status")

    # ------------------------------------------------------------------ #
    #  Lifecycle
    # ------------------------------------------------------------------ #

    def close(self) -> None:
        """Close the underlying HTTP client."""
        self._client.close()

    def __enter__(self) -> "Analytics":
        return self

    def __exit__(self, *args: Any) -> None:
        self.close()
