#!/usr/bin/env python3
"""Web search tool for KDO agents — uses free APIs, no paid subscription needed.

Supports multiple backends:
  - bing: Bing Search API v7 (free tier: 1000/month, Azure key required)
  - duckduckgo: DuckDuckGo Instant Answer (free, no key, but limited results)
  - fallback: simple HTTP search (Google scrape, unreliable)

Usage:
  python web_search.py "query"                    # auto-select best available backend
  python web_search.py "query" --backend bing     # force specific backend
  python web_search.py "query" --json             # JSON output for agent consumption
"""

import json, os, sys, time, hashlib
from pathlib import Path
from urllib.request import Request, urlopen
from urllib.parse import quote_plus
from datetime import datetime, timedelta

CACHE_DIR = Path(__file__).parent / ".search_cache"
CACHE_TTL = 3600  # 1 hour

def _cache_key(query: str, backend: str) -> str:
    return hashlib.md5(f"{backend}:{query}".encode()).hexdigest()

def _cache_get(query: str, backend: str) -> list | None:
    if not CACHE_DIR.exists():
        return None
    key = _cache_key(query, backend)
    cache_file = CACHE_DIR / f"{key}.json"
    if not cache_file.exists():
        return None
    try:
        data = json.loads(cache_file.read_text(encoding="utf-8"))
        if time.time() - data.get("ts", 0) < CACHE_TTL:
            return data.get("results")
    except Exception:
        pass
    return None

def _cache_set(query: str, backend: str, results: list):
    CACHE_DIR.mkdir(parents=True, exist_ok=True)
    key = _cache_key(query, backend)
    (CACHE_DIR / f"{key}.json").write_text(json.dumps({
        "ts": time.time(), "results": results
    }, ensure_ascii=False), encoding="utf-8")


def search_bing(query: str, api_key: str = "") -> list[dict]:
    """Bing Search API v7. Free tier: 1000/month. Key from Azure portal."""
    key = api_key or os.getenv("BING_API_KEY", "")
    if not key:
        return [{"title": "ERROR", "snippet": "BING_API_KEY not set. Get free key at https://portal.azure.com", "url": ""}]

    url = f"https://api.bing.microsoft.com/v7.0/search?q={quote_plus(query)}&count=8&mkt=zh-CN"
    req = Request(url, headers={"Ocp-Apim-Subscription-Key": key})
    try:
        resp = json.loads(urlopen(req, timeout=10).read())
        results = []
        for item in resp.get("webPages", {}).get("value", []):
            results.append({
                "title": item.get("name", ""),
                "url": item.get("url", ""),
                "snippet": item.get("snippet", ""),
            })
        return results
    except Exception as e:
        return [{"title": "Bing Search Error", "snippet": str(e), "url": ""}]


def search_duckduckgo(query: str) -> list[dict]:
    """DuckDuckGo Instant Answer API. Free, no key needed."""
    url = f"https://api.duckduckgo.com/?q={quote_plus(query)}&format=json&no_html=1"
    try:
        resp = json.loads(urlopen(url, timeout=10).read())
        results = []
        for item in resp.get("RelatedTopics", [])[:8]:
            if isinstance(item, dict) and "Text" in item:
                results.append({
                    "title": item.get("FirstURL", "").split("/")[-1].replace("_", " "),
                    "url": item.get("FirstURL", ""),
                    "snippet": item.get("Text", ""),
                })
        if not results and resp.get("AbstractText"):
            results.append({
                "title": resp.get("AbstractSource", "DuckDuckGo"),
                "url": resp.get("AbstractURL", ""),
                "snippet": resp.get("AbstractText", ""),
            })
        return results if results else [{"title": "No results", "snippet": "DuckDuckGo returned no results", "url": ""}]
    except Exception as e:
        return [{"title": "DDG Error", "snippet": str(e), "url": ""}]


def search_cn_bing(query: str) -> list[dict]:
    """Scrape cn.bing.com search results. Zero config, works in China."""
    url = f"https://cn.bing.com/search?q={quote_plus(query)}&count=8"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36",
        "Accept-Language": "zh-CN,zh;q=0.9",
    }
    try:
        req = Request(url, headers=headers)
        html = urlopen(req, timeout=10).read().decode("utf-8", errors="ignore")
        # Simple extraction from Bing HTML
        results = []
        import re
        # Match Bing result blocks: <li class="b_algo"> ... <h2><a href="...">title</a></h2> ... <p>snippet</p>
        blocks = re.findall(r'<li class="b_algo"[^>]*>(.*?)</li>', html, re.DOTALL)
        for block in blocks[:8]:
            link_match = re.search(r'<a[^>]*href="(https?://[^"]+)"[^>]*>(.*?)</a>', block, re.DOTALL)
            snippet_match = re.search(r'<p[^>]*>(.*?)</p>', block, re.DOTALL)
            if link_match:
                title = re.sub(r'<[^>]+>', '', link_match.group(2))
                # Clean up title prefixes like "baidu.comhttps://..."
                title = re.sub(r'^[a-z]+\.[a-z]+https?://', 'https://', title)
                title = title.strip()
                snippet = re.sub(r'<[^>]+>', '', snippet_match.group(1)) if snippet_match else ""
                results.append({
                    "title": title.strip(),
                    "url": link_match.group(1),
                    "snippet": snippet.strip()[:300],
                })
        return results if results else [{"title": "No results", "snippet": "Bing returned no results for this query", "url": ""}]
    except Exception as e:
        return [{"title": "Bing Scrape Error", "snippet": str(e), "url": ""}]


def search(query: str, backend: str = "auto") -> list[dict]:
    """Main entry point. Auto-selects best available backend."""
    cached = _cache_get(query, backend)
    if cached:
        return cached

    results = []

    if backend == "bing":
        results = search_bing(query)
    elif backend == "duckduckgo":
        results = search_duckduckgo(query)
    elif backend == "cn_bing":
        results = search_cn_bing(query)
    elif backend == "auto":
        # Try Bing API first (best results), then cn.bing.com scrape
        bing_key = os.getenv("BING_API_KEY", "")
        if bing_key:
            results = search_bing(query)
        if not results or "ERROR" in results[0].get("title", ""):
            results = search_cn_bing(query)
        if not results or "ERROR" in results[0].get("title", ""):
            results = search_duckduckgo(query)

    if results:
        _cache_set(query, backend, results)
    return results


def _format_markdown(results: list[dict]) -> str:
    lines = []
    for i, r in enumerate(results, 1):
        title = r.get("title", "Untitled")
        url = r.get("url", "")
        snippet = r.get("snippet", "")
        lines.append(f"{i}. **{title}**")
        if url:
            lines.append(f"   {url}")
        lines.append(f"   {snippet}")
        lines.append("")
    return "\n".join(lines)


if __name__ == "__main__":
    import argparse
    p = argparse.ArgumentParser(description="KDO Web Search Tool")
    p.add_argument("query", help="Search query")
    p.add_argument("--backend", default="auto", choices=["auto", "bing", "duckduckgo", "cn_bing"])
    p.add_argument("--json", action="store_true", help="Output as JSON")
    args = p.parse_args()

    results = search(args.query, args.backend)

    if args.json:
        print(json.dumps(results, ensure_ascii=False, indent=2))
    else:
        print(f"# Search: {args.query}\n")
        print(_format_markdown(results))
        stats = f"\n*{len(results)} results · backend: {args.backend} · cached: {bool(_cache_get(args.query, args.backend))}*"
        print(stats)
