# ToolkitAPI — Python SDK

[![PyPI version](https://img.shields.io/pypi/v/toolkitapi.svg)](https://pypi.org/project/toolkitapi/)
[![Python versions](https://img.shields.io/pypi/pyversions/toolkitapi.svg)](https://pypi.org/project/toolkitapi/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

> Public beta: the package name is live-ready for install as pip install toolkitapi.

Official Python SDK for [ToolkitAPI.io](https://toolkitapi.io) — a family of 16
focused HTTP APIs covering DNS, email, images, PDFs, scraping, screenshots,
AI-powered text tools, barcodes, finance data, media extraction, webhooks, and
more.

## Installation

```bash
pip install toolkitapi
```

Requires Python **3.9+** and [httpx](https://www.python-httpx.org/).

## Quick start

Use a single toolkit directly:

```python
from toolkitapi import DNS

dns = DNS(api_key="tk_...")
print(dns.lookup(domain="example.com"))
dns.close()
```

Or the unified client to access multiple toolkits with a single API key:

```python
from toolkitapi import ToolkitAPI

with ToolkitAPI(api_key="tk_...") as tk:
    dns_result = tk.dns.lookup(domain="example.com")
    scores = tk.textanalysis.readability(text="The quick brown fox.")
    png_bytes = tk.screenshot.capture(url="https://example.com")
```

Toolkit instances are created lazily on first property access and reused
thereafter. `close()` (or leaving the `with` block) tears down every HTTP
client that was opened.

## Toolkits

| Toolkit          | Class           | Highlights                                                           |
| ---------------- | --------------- | -------------------------------------------------------------------- |
| AI-Text          | `AiText`        | LLM-powered extraction, classification, sentiment, summarization     |
| Auth             | `Auth`          | JWT create/decode, TOTP, OAuth helpers, API-key generation           |
| Barcode          | `Barcode`       | Barcode and QR code generation, decoding, raw-image downloads        |
| Convert          | `Convert`       | Format (JSON/YAML/CSV/XML) and unit conversions                      |
| DevTools         | `DevTools`      | JSON/YAML/XML validators, regex tester, UUID, hashing, fake data     |
| DNS              | `DNS`           | DNS records, WHOIS, propagation, email auth, typosquat, SSL certs    |
| Email            | `Email`         | Validation, deliverability, disposable detection, SPF/DMARC          |
| Finance          | `Finance`       | Currency conversion, FX rates, VAT lookup                            |
| Geo              | `Geo`           | IP geolocation, reverse geocoding, distance/bearing, timezone        |
| Image            | `Image`         | Resize, convert, optimise, analyse, remove background                |
| Media            | `Media`         | YouTube metadata/transcripts, universal media extraction, crawling   |
| PDF              | `PDF`           | Generate, merge, split, extract, stamp, protect                      |
| Scrape           | `Scrape`        | Web scraping, readability, meta, SEO audits, broken-link checks      |
| Screenshot       | `Screenshot`    | Page/element/HTML/template rendering to PNG/JPG/PDF (sync + async)   |
| TextAnalysis     | `TextAnalysis`  | Readability, PII masking, profanity, similarity, summarize, language |
| Webhook          | `Webhook`       | Request bins, HTTP mocks, replay captured requests                   |

Full endpoint reference at <https://toolkitapi.io/docs>.

## Scrape toolkit examples

The scrape SDK now mirrors the current unified scrape API. You can fetch page content, request structured extraction, render JavaScript pages, and run specialized sitemap, robots, crawl, and PDF helpers from one client.

### Unified page scrape

```python
from toolkitapi import Scrape

scrape = Scrape(api_key="tk_...")

result = scrape.fetch(
    url="https://example.com/blog/post",
    output="markdown",
    extract={
        "article": True,
        "links": True,
        "meta_tags": True,
    },
)

print(result["content"])
print(result.get("article"))
scrape.close()
```

### JavaScript rendering

```python
with Scrape(api_key="tk_...") as scrape:
    result = scrape.render_page(
        url="https://example.com/app",
        wait_until="networkidle",
        output="text",
        scroll=True,
    )
    print(result["content"])
```

### PDF, sitemap, and robots helpers

```python
with Scrape(api_key="tk_...") as scrape:
    pdf = scrape.pdf_extract(url="https://example.com/report.pdf", pages="1-2")
    sitemap = scrape.parse_sitemap("https://example.com/sitemap.xml", limit=100)
    robots = scrape.parse_robots_txt("https://example.com")
```

### AI extraction and chunking

```python
with Scrape(api_key="tk_...") as scrape:
    result = scrape.ai_extract(
        url="https://example.com/product",
        schema={
            "type": "object",
            "properties": {
                "name": {"type": "string"},
                "price": {"type": "string"},
            },
        },
        prompt="Extract the product name and displayed price.",
        render_js=True,
    )
    print(result.get("ai_extract"))
```

## Authentication

Every request is authenticated by the `X-API-Key` header. Provide your key
when constructing a toolkit (or the unified `ToolkitAPI` client); it is
reused for every request in that session.

```python
tk = ToolkitAPI(api_key="tk_live_...")
```

## Error handling

All non-2xx responses raise an exception that inherits from
`toolkitapi.ToolkitAPIError`:

| Exception              | HTTP status |
| ---------------------- | ----------- |
| `AuthenticationError`  | 401, 403    |
| `ValidationError`      | 400, 422    |
| `NotFoundError`        | 404         |
| `RateLimitError`       | 429         |
| `ServerError`          | 5xx         |
| `APIError` (fallback)  | anything else — exposes `.status_code` and `.detail` |

```python
from toolkitapi import DNS, NotFoundError, RateLimitError

dns = DNS(api_key="tk_...")
try:
    dns.lookup(domain="does-not-exist.example")
except NotFoundError:
    ...
except RateLimitError:
    ...
```

## Async jobs (Screenshot, Media)

Some endpoints can enqueue work and return a job descriptor instead of
bytes. Pass `async_mode=True` to the relevant method, then poll the
returned job ID:

```python
job = tk.screenshot.capture(url="https://example.com", async_mode=True)
result = tk.screenshot.wait_for_job(job["job_id"], timeout=60)
png_bytes = tk.screenshot.download(result["object_name"])
```

## Binary downloads

Endpoints that return raw image/PDF bytes expose an optional
`output_path=` kwarg — pass a filename to stream the response directly to
disk instead of loading it into memory:

```python
tk.barcode.qr_raw_image(data="https://toolkitapi.io", output_path="qr.png")
```

## Configuration

- `timeout` — per-client request timeout (seconds). Defaults to 30s; 60s
  for heavier toolkits (`Image`, `PDF`, `Scrape`, `Screenshot`).
- `base_url` — override the API host (useful for staging or self-hosted
  deployments).

```python
dns = DNS(api_key="tk_...", timeout=10.0, base_url="https://staging.dns.toolkitapi.io")
```

## Development

```bash
cd sdk/python
pip install -e ".[test]"
pytest
```

## License

MIT — see `LICENSE` in the repository root.
