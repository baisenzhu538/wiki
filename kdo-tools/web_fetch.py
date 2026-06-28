#!/usr/bin/env python3
"""Simple URL fetcher for KDO agents. No API key needed.

Usage:
  python web_fetch.py "https://example.com"           # fetch and print markdown
  python web_fetch.py "https://example.com" --json    # JSON output
  python web_fetch.py "https://example.com" --text    # raw text only
"""

import json
import sys
from pathlib import Path
from urllib.request import Request, urlopen
from urllib.parse import urlparse
from datetime import datetime, timedelta
import hashlib
import os
import time

CACHE_DIR = Path(__file__).parent / ".fetch_cache"
CACHE_TTL = 3600


def _cache_key(url: str) -> str:
    return hashlib.md5(url.encode()).hexdigest()


def _cache_get(url: str) -> str | None:
    if not CACHE_DIR.exists():
        return None
    key = _cache_key(url)
    cf = CACHE_DIR / f"{key}.txt"
    if cf.exists() and time.time() - cf.stat().st_mtime < CACHE_TTL:
        return cf.read_text(encoding="utf-8", errors="ignore")
    return None


def _cache_set(url: str, content: str):
    CACHE_DIR.mkdir(parents=True, exist_ok=True)
    (CACHE_DIR / f"{_cache_key(url)}.txt").write_text(content, encoding="utf-8")


def fetch(url: str) -> dict:
    """Fetch a URL and return title + text."""
    cached = _cache_get(url)
    if cached:
        return {"url": url, "title": urlparse(url).netloc, "text": cached, "from_cache": True}

    headers = {
        "User-Agent": "Mozilla/5.0 (compatible; KDO-Fetch/1.0)",
        "Accept": "text/html,application/xhtml+xml",
    }
    try:
        req = Request(url, headers=headers)
        html = urlopen(req, timeout=15).read().decode("utf-8", errors="ignore")
    except Exception as e:
        return {"url": url, "title": "Fetch Error", "text": str(e), "error": True}

    # Basic HTML-to-text extraction
    import re
    title = urlparse(url).netloc
    tm = re.search(r"<title[^>]*>(.*?)</title>", html, re.IGNORECASE | re.DOTALL)
    if tm:
        title = re.sub(r"<[^>]+>", "", tm.group(1)).strip()

    # Strip tags, scripts, styles
    for tag in ["script", "style", "nav", "footer", "header", "aside"]:
        html = re.sub(f"<{tag}[^>]*>.*?</{tag}>", "", html, flags=re.DOTALL | re.IGNORECASE)
    text = re.sub(r"<[^>]+>", " ", html)
    text = re.sub(r"\s+", " ", text).strip()

    # Limit output
    if len(text) > 50000:
        text = text[:50000] + "\n\n... (truncated)"

    _cache_set(url, text)
    return {"url": url, "title": title, "text": text, "from_cache": False}


if __name__ == "__main__":
    import argparse
    p = argparse.ArgumentParser(description="KDO URL Fetcher")
    p.add_argument("url", help="URL to fetch")
    p.add_argument("--json", action="store_true")
    p.add_argument("--text", action="store_true", help="Raw text only")
    args = p.parse_args()

    result = fetch(args.url)

    if args.json:
        print(json.dumps(result, ensure_ascii=False, indent=2))
    elif args.text:
        print(result["text"])
    else:
        print(f"# {result['title']}\n")
        print(result["text"])
        cache_info = " (cached)" if result.get("from_cache") else ""
        print(f"\n*{len(result['text'])} chars · {result['url']}{cache_info}*")
