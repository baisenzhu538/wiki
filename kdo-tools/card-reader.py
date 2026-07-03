#!/usr/bin/env python3
"""
Minimal read-only card server for Hermes/飞书 agents.
Only GET. Never write.

Usage:
  python kdo-tools/card-reader.py --port 8899
  Then: GET /read?path=30_wiki/tools/tool-yitang-customer-segmentation-4step
        GET /search?q=用户分层&limit=5
"""

import json
import re
from http.server import HTTPServer, BaseHTTPRequestHandler
from pathlib import Path
from urllib.parse import urlparse, parse_qs

WIKI_ROOT = Path(__file__).resolve().parent.parent

def read_card(rel_path: str) -> dict | None:
    """Read a single card, returning frontmatter fields + body excerpt."""
    p = WIKI_ROOT / rel_path
    if not p.exists() or not p.suffix == ".md":
        return None
    text = p.read_text(encoding="utf-8", errors="ignore")
    result = {"path": rel_path, "title": p.stem}
    if text.startswith("---"):
        parts = text.split("---", 2)
        if len(parts) >= 3:
            result["body"] = parts[2][:3000]
    else:
        result["body"] = text[:3000]
    return result

def search_cards(query: str, limit: int = 5) -> list[dict]:
    """Simple keyword search across 30_wiki card frontmatter."""
    wiki = WIKI_ROOT / "30_wiki"
    results = []
    for p in wiki.rglob("*.md"):
        if "_archive" in str(p):
            continue
        try:
            text = p.read_text(encoding="utf-8", errors="ignore")
        except Exception:
            continue
        if query.lower() in text.lower():
            title = p.stem
            if text.startswith("---"):
                parts = text.split("---", 2)
                try:
                    import yaml
                    fm = yaml.safe_load(parts[1])
                    if fm and isinstance(fm, dict):
                        title = fm.get("title", p.stem)
                except Exception:
                    pass
            results.append({
                "path": str(p.relative_to(WIKI_ROOT)),
                "title": title,
                "excerpt": text[text.lower().find(query.lower()):][:200]
            })
        if len(results) >= limit:
            break
    return results

class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        parsed = urlparse(self.path)
        params = parse_qs(parsed.query)
        if parsed.path == "/read":
            path = params.get("path", [None])[0]
            if not path:
                self.send_error(400, "Missing ?path=")
                return
            card = read_card(path)
            if card is None:
                self.send_error(404, f"Card not found: {path}")
                return
            self._json(card)
        elif parsed.path == "/search":
            q = params.get("q", [""])[0]
            limit = int(params.get("limit", ["5"])[0])
            results = search_cards(q, limit)
            self._json(results)
        elif parsed.path == "/health":
            self._json({"status": "ok"})
        else:
            self.send_error(404)

    def _json(self, data):
        body = json.dumps(data, ensure_ascii=False, indent=2)
        self.send_response(200)
        self.send_header("Content-Type", "application/json; charset=utf-8")
        self.send_header("Access-Control-Allow-Origin", "*")
        self.end_headers()
        self.wfile.write(body.encode("utf-8"))

    def log_message(self, format, *args):
        pass  # silent

if __name__ == "__main__":
    import argparse
    p = argparse.ArgumentParser()
    p.add_argument("--port", type=int, default=8899)
    args = p.parse_args()
    server = HTTPServer(("127.0.0.1", args.port), Handler)
    print(f"card-reader ready: http://127.0.0.1:{args.port}")
    server.serve_forever()
