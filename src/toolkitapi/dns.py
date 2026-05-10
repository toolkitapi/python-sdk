"""Query a domain's DNS records from 20 public resolvers around the world. Returns per-resolver results, response times, and a consistency score showing what percentage of resolvers agree on the same answer."""

from __future__ import annotations

from typing import List, Dict, Any, Optional

from ._client import _APIClient


class DNS:
    """Check DNS propagation across global resolvers"""

    def __init__(
        self,
        api_key: str,
        *,
        base_url: Optional[str] = None,
        timeout: float = 30.0,
    ) -> None:
        self._client = _APIClient(
            "dns", api_key, base_url=base_url, timeout=timeout
        )

    # ------------------------------------------------------------------ #
    #  Propagation
    # ------------------------------------------------------------------ #

    def propagation(
        self,
        domain: str,
        *,
        type_: Optional[str] = None,
        format: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Check DNS propagation across global resolvers

        Args:
            domain: Domain to check (e.g. example.com)
            type_: DNS record type: A, AAAA, CNAME, MX, NS, TXT, SOA, CAA, PTR
            format: Response format: json or markdown
        """
        return self._client.get("propagation", params={"domain": domain, "type_": type_, "format": format})

    # ------------------------------------------------------------------ #
    #  Lookup
    # ------------------------------------------------------------------ #

    def lookup(
        self,
        domain: str,
        *,
        type_: Optional[str] = None,
        format: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Look up DNS records for a domain

        Args:
            domain: Domain to look up (e.g. example.com)
            type_: DNS record type: A, AAAA, CNAME, MX, NS, TXT, SOA, CAA, PTR, SRV
            format: Response format: json or markdown
        """
        return self._client.get("lookup", params={"domain": domain, "type_": type_, "format": format})

    def lookup_all(
        self,
        domain: str,
        *,
        format: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Look up all DNS record types for a domain

        Args:
            domain: Domain to look up (e.g. example.com)
            format: Response format: json or markdown
        """
        return self._client.get("lookup/all", params={"domain": domain, "format": format})

    def lookup_bulk(
        self,
        body: List[str],
        *,
        type_: Optional[str] = None,
        format: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Bulk DNS lookup for multiple domains

        Args:
            body: Request body.
            type_: DNS record type to query
            format: Response format: json or markdown
        """
        return self._client.post(
            "lookup/bulk",
            body=body,
            params={"type_": type_, "format": format},
        )

    # ------------------------------------------------------------------ #
    #  Compare Resolvers
    # ------------------------------------------------------------------ #

    def compare_resolvers(
        self,
        domain: str,
        *,
        format: Optional[str] = None,
        type_: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Compare DNS responses across major public resolvers

        Args:
            domain: Domain to query (e.g. github.com)
            format: Response format: json or markdown
            type_: DNS record type: A, AAAA, CNAME, MX, NS, TXT
        """
        return self._client.get("compare-resolvers", params={"domain": domain, "format": format, "type_": type_})

    # ------------------------------------------------------------------ #
    #  Doh Test
    # ------------------------------------------------------------------ #

    def doh_test(
        self,
        domain: str,
        *,
        format: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Test DNS-over-HTTPS and DNS-over-TLS providers

        Args:
            domain: Domain to resolve (e.g. github.com)
            format: Response format: json or markdown
        """
        return self._client.get("doh-test", params={"domain": domain, "format": format})

    # ------------------------------------------------------------------ #
    #  Idn
    # ------------------------------------------------------------------ #

    def idn(
        self,
        domain: str,
        *,
        format: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Convert between IDN (Unicode) and Punycode

        Args:
            domain: Domain name in Unicode or Punycode (e.g. münchen.de or xn--mnchen-3ya.de)
            format: Response format: json or markdown
        """
        return self._client.get("idn", params={"domain": domain, "format": format})

    # ------------------------------------------------------------------ #
    #  Whois
    # ------------------------------------------------------------------ #

    def whois(
        self,
        domain: str,
        *,
        format: Optional[str] = None,
    ) -> Dict[str, Any]:
        """WHOIS / RDAP lookup for a domain

        Args:
            domain: Domain to look up (e.g. example.com)
            format: Response format: json or markdown
        """
        return self._client.get("whois", params={"domain": domain, "format": format})

    def whois_bulk(
        self,
        body: List[str],
        *,
        format: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Bulk WHOIS / RDAP lookup

        Args:
            body: Request body.
            format: Response format: json or markdown
        """
        return self._client.post(
            "whois/bulk",
            body=body,
            params={"format": format},
        )

    # ------------------------------------------------------------------ #
    #  Domain Age
    # ------------------------------------------------------------------ #

    def domain_age(
        self,
        domain: str,
        *,
        format: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Check domain registration age

        Args:
            domain: Domain to check (e.g. github.com)
            format: Response format: json or markdown
        """
        return self._client.get("domain-age", params={"domain": domain, "format": format})

    # ------------------------------------------------------------------ #
    #  Available
    # ------------------------------------------------------------------ #

    def available(
        self,
        domain: str,
        *,
        format: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Check if a domain is available for registration

        Args:
            domain: Domain to check (e.g. example-test-12345.com)
            format: Response format: json or markdown
        """
        return self._client.get("available", params={"domain": domain, "format": format})

    def available_bulk(
        self,
        body: List[str],
        *,
        format: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Bulk domain availability check

        Args:
            body: Request body.
            format: Response format: json or markdown
        """
        return self._client.post(
            "available/bulk",
            body=body,
            params={"format": format},
        )

    # ------------------------------------------------------------------ #
    #  Subdomains
    # ------------------------------------------------------------------ #

    def subdomains(
        self,
        domain: str,
        *,
        format: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Discover subdomains via DNS brute-force

        Args:
            domain: Domain to enumerate (e.g. github.com)
            format: Response format: json or markdown
        """
        return self._client.get("subdomains", params={"domain": domain, "format": format})

    # ------------------------------------------------------------------ #
    #  Associated
    # ------------------------------------------------------------------ #

    def associated(
        self,
        domain: str,
        *,
        format: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Find associated infrastructure for a domain

        Args:
            domain: Domain to analyze (e.g. github.com)
            format: Response format: json or markdown
        """
        return self._client.get("associated", params={"domain": domain, "format": format})

    # ------------------------------------------------------------------ #
    #  Disposable
    # ------------------------------------------------------------------ #

    def disposable(
        self,
        domain: str,
        *,
        format: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Check if a domain is a disposable/temporary email provider

        Args:
            domain: Domain to check (e.g. mailinator.com)
            format: Response format: json or markdown
        """
        return self._client.get("disposable", params={"domain": domain, "format": format})

    # ------------------------------------------------------------------ #
    #  Tld Search
    # ------------------------------------------------------------------ #

    def tld_search(
        self,
        keyword: str,
        *,
        format: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Search keyword availability across 150+ TLDs

        Args:
            keyword: Keyword to search (e.g. 'myapp' checks myapp.com, myapp.io, etc.)
            format: Response format: json or markdown
        """
        return self._client.get("tld-search", params={"keyword": keyword, "format": format})

    # ------------------------------------------------------------------ #
    #  Health
    # ------------------------------------------------------------------ #

    def health(
        self,
        domain: str,
        *,
        format: Optional[str] = None,
    ) -> Dict[str, Any]:
        """DNS health audit and score

        Args:
            domain: Domain to audit (e.g. example.com)
            format: Response format: json or markdown
        """
        return self._client.get("health", params={"domain": domain, "format": format})

    # ------------------------------------------------------------------ #
    #  Certificate
    # ------------------------------------------------------------------ #

    def certificate(
        self,
        domain: str,
        *,
        port: Optional[int] = None,
        format: Optional[str] = None,
    ) -> Dict[str, Any]:
        """SSL/TLS certificate inspection

        Args:
            domain: Domain to inspect (e.g. github.com)
            port: Port to connect to (default: 443)
            format: Response format: json or markdown
        """
        return self._client.get("certificate", params={"domain": domain, "port": port, "format": format})

    # ------------------------------------------------------------------ #
    #  Dnssec
    # ------------------------------------------------------------------ #

    def dnssec(
        self,
        domain: str,
        *,
        format: Optional[str] = None,
    ) -> Dict[str, Any]:
        """DNSSEC validation check

        Args:
            domain: Domain to validate (e.g. cloudflare.com)
            format: Response format: json or markdown
        """
        return self._client.get("dnssec", params={"domain": domain, "format": format})

    # ------------------------------------------------------------------ #
    #  Security Headers
    # ------------------------------------------------------------------ #

    def security_headers(
        self,
        domain: str,
        *,
        format: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Audit HTTP security headers

        Args:
            domain: Domain to audit (e.g. github.com)
            format: Response format: json or markdown
        """
        return self._client.get("security-headers", params={"domain": domain, "format": format})

    # ------------------------------------------------------------------ #
    #  Zone Transfer
    # ------------------------------------------------------------------ #

    def zone_transfer(
        self,
        domain: str,
        *,
        format: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Test for zone transfer (AXFR) vulnerability

        Args:
            domain: Domain to test (e.g. example.com)
            format: Response format: json or markdown
        """
        return self._client.get("zone-transfer", params={"domain": domain, "format": format})

    # ------------------------------------------------------------------ #
    #  Typosquat
    # ------------------------------------------------------------------ #

    def typosquat(
        self,
        domain: str,
        *,
        format: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Detect typosquatting domains

        Args:
            domain: Domain to check for typosquats (e.g. google.com)
            format: Response format: json or markdown
        """
        return self._client.get("typosquat", params={"domain": domain, "format": format})

    # ------------------------------------------------------------------ #
    #  Blacklist
    # ------------------------------------------------------------------ #

    def blacklist(
        self,
        ip: str,
        *,
        format: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Check IP against 30 DNS blacklists

        Args:
            ip: IPv4 address to check (e.g. 8.8.8.8)
            format: Response format: json or markdown
        """
        return self._client.get("blacklist", params={"ip": ip, "format": format})

    # ------------------------------------------------------------------ #
    #  Tech Stack
    # ------------------------------------------------------------------ #

    def tech_stack(
        self,
        domain: str,
        *,
        format: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Detect web server technology and headers

        Args:
            domain: Domain to inspect (e.g. github.com)
            format: Response format: json or markdown
        """
        return self._client.get("tech-stack", params={"domain": domain, "format": format})

    # ------------------------------------------------------------------ #
    #  Ports
    # ------------------------------------------------------------------ #

    def port_scan(
        self,
        host: str,
        *,
        format: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Scan common TCP ports

        Args:
            host: Hostname or IP to scan (e.g. github.com)
            format: Response format: json or markdown
        """
        return self._client.get("ports", params={"host": host, "format": format})

    # ------------------------------------------------------------------ #
    #  Redirects
    # ------------------------------------------------------------------ #

    def redirects(
        self,
        url: str,
        *,
        format: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Trace HTTP redirect chain

        Args:
            url: URL to trace (e.g. http://github.com)
            format: Response format: json or markdown
        """
        return self._client.get("redirects", params={"url": url, "format": format})

    # ------------------------------------------------------------------ #
    #  Company Profile
    # ------------------------------------------------------------------ #

    def company_profile(
        self,
        domain: str,
        *,
        format: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Build a company profile from a domain

        Args:
            domain: Domain to profile (e.g. github.com)
            format: Response format: json or markdown
        """
        return self._client.get("company-profile", params={"domain": domain, "format": format})

    # ------------------------------------------------------------------ #
    #  Url Parse
    # ------------------------------------------------------------------ #

    def url_parse(
        self,
        url: str,
    ) -> Any:
        """Decompose a URL into its component parts

        Args:
            url: URL to decompose
        """
        return self._client.get("url-parse", params={"url": url})

    # ------------------------------------------------------------------ #
    #  Http Header Parse
    # ------------------------------------------------------------------ #

    def http_header_parse(
        self,
        body: Dict[str, Any],
    ) -> Any:
        """Parse raw HTTP headers into structured key-value pairs

        Args:
            body: Request body.
        """
        return self._client.post("http-header-parse", body=body)

    # ------------------------------------------------------------------ #
    #  Reverse
    # ------------------------------------------------------------------ #

    def reverse(
        self,
        ip: str,
        *,
        format: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Reverse DNS lookup with IP intelligence

        Args:
            ip: IPv4 or IPv6 address (e.g. 8.8.8.8)
            format: Response format: json or markdown
        """
        return self._client.get("reverse", params={"ip": ip, "format": format})

    # ------------------------------------------------------------------ #
    #  Asn
    # ------------------------------------------------------------------ #

    def asn(
        self,
        ip: str,
        *,
        format: Optional[str] = None,
    ) -> Dict[str, Any]:
        """ASN and IP intelligence lookup

        Args:
            ip: IPv4 address (e.g. 8.8.8.8)
            format: Response format: json or markdown
        """
        return self._client.get("asn", params={"ip": ip, "format": format})

    # ------------------------------------------------------------------ #
    #  Ip Calc
    # ------------------------------------------------------------------ #

    def ip_calc(
        self,
        cidr: str,
    ) -> Any:
        """IP subnet calculator

        Args:
            cidr: CIDR notation, e.g. 192.168.1.0/24
        """
        return self._client.get("ip-calc", params={"cidr": cidr})

    # ------------------------------------------------------------------ #
    #  Generate
    # ------------------------------------------------------------------ #

    def generate(
        self,
        domain: str,
        type_: str,
        *,
        spf_includes: Optional[str] = None,
        spf_ip4: Optional[str] = None,
        spf_ip6: Optional[str] = None,
        spf_policy: Optional[str] = None,
        dmarc_policy: Optional[str] = None,
        dmarc_rua: Optional[str] = None,
        dmarc_ruf: Optional[str] = None,
        dmarc_pct: Optional[int] = None,
        dmarc_sp: Optional[str] = None,
        mta_sts_id: Optional[str] = None,
        bimi_logo: Optional[str] = None,
        bimi_vmc: Optional[str] = None,
        tls_rpt_email: Optional[str] = None,
        format: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Generate DNS records from simple inputs

        Args:
            domain: Domain the record is for
            type_: Record type to generate: SPF, DMARC, MTA-STS, BIMI, TLS-RPT
            spf_includes: SPF: comma-separated include domains
            spf_ip4: SPF: comma-separated IPv4 addresses or CIDRs
            spf_ip6: SPF: comma-separated IPv6 addresses or CIDRs
            spf_policy: SPF: policy — ~all (softfail), -all (fail), ?all (neutral)
            dmarc_policy: DMARC: policy — none, quarantine, reject
            dmarc_rua: DMARC: aggregate report email address
            dmarc_ruf: DMARC: forensic report email address
            dmarc_pct: DMARC: percentage of messages to apply policy (1-100)
            dmarc_sp: DMARC: subdomain policy — none, quarantine, reject
            mta_sts_id: MTA-STS: policy ID (e.g. 20240101000000)
            bimi_logo: BIMI: URL to SVG logo
            bimi_vmc: BIMI: URL to VMC certificate (optional)
            tls_rpt_email: TLS-RPT: email to receive reports
            format: Response format: json or markdown
        """
        return self._client.get("generate", params={"domain": domain, "type_": type_, "spf_includes": spf_includes, "spf_ip4": spf_ip4, "spf_ip6": spf_ip6, "spf_policy": spf_policy, "dmarc_policy": dmarc_policy, "dmarc_rua": dmarc_rua, "dmarc_ruf": dmarc_ruf, "dmarc_pct": dmarc_pct, "dmarc_sp": dmarc_sp, "mta_sts_id": mta_sts_id, "bimi_logo": bimi_logo, "bimi_vmc": bimi_vmc, "tls_rpt_email": tls_rpt_email, "format": format})

    # ------------------------------------------------------------------ #
    #  Ns Performance
    # ------------------------------------------------------------------ #

    def ns_performance(
        self,
        domain: str,
        *,
        format: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Benchmark authoritative nameserver response times

        Args:
            domain: Domain to benchmark (e.g. github.com)
            format: Response format: json or markdown
        """
        return self._client.get("ns-performance", params={"domain": domain, "format": format})

    # ------------------------------------------------------------------ #
    #  Caa
    # ------------------------------------------------------------------ #

    def caa(
        self,
        domain: str,
        *,
        format: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Analyze CAA (Certificate Authority Authorization) records

        Args:
            domain: Domain to analyze (e.g. github.com)
            format: Response format: json or markdown
        """
        return self._client.get("caa", params={"domain": domain, "format": format})

    # ------------------------------------------------------------------ #
    #  Tlsa
    # ------------------------------------------------------------------ #

    def tlsa(
        self,
        domain: str,
        *,
        port: Optional[int] = None,
        format: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Look up TLSA/DANE records

        Args:
            domain: Domain to check (e.g. mail.example.com)
            port: Port to check TLSA for (default: 443)
            format: Response format: json or markdown
        """
        return self._client.get("tlsa", params={"domain": domain, "port": port, "format": format})

    # ------------------------------------------------------------------ #
    #  Status
    # ------------------------------------------------------------------ #

    def status_check(
        self,
    ) -> Dict[str, Any]:
        """Status Check
        """
        return self._client.get("status")

    # ------------------------------------------------------------------ #
    #  Lifecycle
    # ------------------------------------------------------------------ #

    def close(self) -> None:
        """Close the underlying HTTP client."""
        self._client.close()

    def __enter__(self) -> "DNS":
        return self

    def __exit__(self, *args: Any) -> None:
        self.close()
