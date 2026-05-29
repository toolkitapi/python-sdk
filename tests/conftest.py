"""Shared test fixtures for the ToolkitAPI SDK test suite."""

from __future__ import annotations

import json
import sys
from pathlib import Path
from typing import Any

import httpx
import pytest


# Ensure tests import the local SDK under src/ rather than an installed package.
SRC_DIR = Path(__file__).resolve().parents[1] / "src"
if str(SRC_DIR) not in sys.path:
    sys.path.insert(0, str(SRC_DIR))


class MockTransport(httpx.BaseTransport):
    """Deterministic HTTP transport that returns canned JSON responses.

    Every request is recorded in ``self.requests`` so tests can assert on
    the method, URL, headers, query-string, and JSON body that the SDK sent.
    """

    def __init__(
        self,
        status_code: int = 200,
        json_body: Any = None,
    ) -> None:
        self.status_code = status_code
        self.json_body = json_body if json_body is not None else {"ok": True}
        self.requests: list[httpx.Request] = []

    def handle_request(self, request: httpx.Request) -> httpx.Response:
        self.requests.append(request)
        return httpx.Response(
            status_code=self.status_code,
            json=self.json_body,
            request=request,
        )


@pytest.fixture()
def mock_transport() -> MockTransport:
    """Return a fresh ``MockTransport`` that returns 200 ``{"ok": true}``."""
    return MockTransport()


@pytest.fixture()
def mock_transport_factory():
    """Factory fixture — call with ``(status_code, json_body)`` to customise."""
    def _factory(status_code: int = 200, json_body: Any = None) -> MockTransport:
        return MockTransport(status_code=status_code, json_body=json_body)
    return _factory
