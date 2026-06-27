#!/usr/bin/env python3
"""
Count wiki cards with no wikilinks (isolated cards) in 30_wiki.

Definitions:
- "outgoing isolated": card body contains zero [[wikilinks]]
- "true island": card has zero incoming AND zero outgoing wikilinks
- Counts can be grouped by frontmatter `type`.

Usage:
    python 90_control/scripts/count_wiki_islands.py
"""

import re
import yaml
from pathlib import Path
from collections import defaultdict

VAULT_ROOT = Path(__file__).resolve().parent.parent.parent
WIKI_DIR = VAULT_ROOT / "30_wiki"

LINK_RE = re.compile(r"\[\[([^\]]+)\]\]")
FRONTMATTER_RE = re.compile(r"^---\s*\n(.*?)\n---\s*\n", re.DOTALL)


def slugify(text: str) -> str:
    return re.sub(r"[^\w\-]", "", text.lower().replace(" ", "-").replace("_", "-"))[:60]


def extract_frontmatter(content: str):
    # Robust frontmatter extraction: handles CRLF and unusual spacing
    if content.startswith('---'):
        parts = content.split('---', 2)
        if len(parts) >= 3:
            try:
                fm = yaml.safe_load(parts[1])
                return fm if isinstance(fm, dict) else {}, parts[2]
            except yaml.YAMLError:
                return None, content
    return None, content


def clean_link(link: str) -> str:
    return link.strip("[] ").split("|")[0].strip()


def main():
    md_files = list(WIKI_DIR.rglob("*.md"))

    nodes = {}
    for fp in md_files:
        content = fp.read_text(encoding="utf-8", errors="ignore")
        fm, body = extract_frontmatter(content)
        if fm is None:
            continue

        title = fm.get("title", fp.stem)
        node_id = slugify(title) or slugify(fp.stem)
        rel = fp.relative_to(VAULT_ROOT).as_posix()
        nodes[node_id] = {
            "path": rel,
            "type": fm.get("type", "unknown"),
            "status": fm.get("status", "unknown"),
        }

    out_degree = defaultdict(int)
    in_degree = defaultdict(int)

    for fp in md_files:
        content = fp.read_text(encoding="utf-8", errors="ignore")
        fm, body = extract_frontmatter(content)
        if fm is None:
            continue

        title = fm.get("title", fp.stem)
        src_id = slugify(title) or slugify(fp.stem)
        if src_id not in nodes:
            continue

        # Body wikilinks
        for link in LINK_RE.findall(body):
            tgt_id = slugify(clean_link(link))
            if tgt_id in nodes and tgt_id != src_id:
                out_degree[src_id] += 1
                in_degree[tgt_id] += 1

        # Frontmatter related links
        related = fm.get("related") or []
        if isinstance(related, str):
            related = [related]
        for r in related:
            tgt_id = slugify(clean_link(r))
            if tgt_id in nodes and tgt_id != src_id:
                out_degree[src_id] += 1
                in_degree[tgt_id] += 1

    outgoing_isolated = []
    true_islands = []
    by_type = defaultdict(lambda: {"total": 0, "outgoing_isolated": 0, "true_island": 0})

    for nid, info in nodes.items():
        t = info["type"]
        by_type[t]["total"] += 1

        if out_degree[nid] == 0:
            outgoing_isolated.append(info)
            by_type[t]["outgoing_isolated"] += 1

        if out_degree[nid] == 0 and in_degree[nid] == 0:
            true_islands.append(info)
            by_type[t]["true_island"] += 1

    print(f"Total wiki pages with frontmatter: {len(nodes)}")
    print(f"Outgoing-isolated cards (0 outgoing links): {len(outgoing_isolated)}")
    print(f"True islands (0 incoming + 0 outgoing links): {len(true_islands)}")
    print()
    print("Breakdown by type:")
    print(f"{'type':18s} {'total':>7s} {'out_iso':>9s} {'island':>8s}")
    for t in sorted(by_type.keys(), key=lambda x: -by_type[x]["outgoing_isolated"]):
        d = by_type[t]
        print(f"{t:18s} {d['total']:7d} {d['outgoing_isolated']:9d} {d['true_island']:8d}")


if __name__ == "__main__":
    main()
