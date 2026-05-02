#!/usr/bin/env python3
"""
Build Graph RAG index from 30_wiki/ markdown files.
Pure stdlib. No external dependencies.
Output: 30_wiki/.graph/index.json
"""

import json
import re
from pathlib import Path
from datetime import datetime

VAULT_ROOT = Path(__file__).resolve().parent.parent.parent
WIKI_DIR = VAULT_ROOT / "30_wiki"
GRAPH_DIR = VAULT_ROOT / "30_wiki" / ".graph"

LINK_RE = re.compile(r"\[\[(.*?)\]\]")
FRONTMATTER_RE = re.compile(r"^---\s*\n(.*?)\n---\s*\n", re.DOTALL)


def parse_simple_yaml(text: str) -> dict:
    """Parse simple YAML frontmatter (strings, lists, no nesting)."""
    result = {}
    current_key = None
    current_list = []
    in_list = False

    for line in text.splitlines():
        stripped = line.strip()
        if not stripped or stripped.startswith("#"):
            continue

        if stripped.startswith("-"):
            # List item
            item = stripped[1:].strip()
            if item.startswith('"') and item.endswith('"'):
                item = item[1:-1]
            elif item.startswith("'") and item.endswith("'"):
                item = item[1:-1]
            current_list.append(item)
            in_list = True
        else:
            if in_list and current_key:
                result[current_key] = current_list
                current_list = []
                in_list = False

            if ":" in stripped:
                key, val = stripped.split(":", 1)
                key = key.strip()
                val = val.strip()
                if val.startswith('"') and val.endswith('"'):
                    val = val[1:-1]
                elif val.startswith("'") and val.endswith("'"):
                    val = val[1:-1]
                elif val in ("true", "True"):
                    val = True
                elif val in ("false", "False"):
                    val = False
                elif val == "":
                    val = None
                current_key = key
                result[key] = val

    if in_list and current_key:
        result[current_key] = current_list

    return result


def extract_frontmatter(content: str) -> dict:
    m = FRONTMATTER_RE.match(content)
    if not m:
        return {}
    return parse_simple_yaml(m.group(1))


def extract_wikilinks(content: str) -> list:
    # Skip frontmatter
    m = FRONTMATTER_RE.match(content)
    if m:
        body = content[m.end():]
    else:
        body = content
    return LINK_RE.findall(body)


def slugify(text: str) -> str:
    return re.sub(r"[^\w\-]", "", text.lower().replace(" ", "-").replace("_", "-"))[:60]


def build_index():
    nodes = {}
    edges = []
    errors = []

    md_files = list(WIKI_DIR.rglob("*.md"))

    for fp in md_files:
        rel = fp.relative_to(VAULT_ROOT).as_posix()
        content = fp.read_text(encoding="utf-8")
        fm = extract_frontmatter(content)

        if not fm:
            errors.append({"file": rel, "error": "no frontmatter"})
            continue

        title = fm.get("title", fp.stem)
        node_id = slugify(title) or slugify(fp.stem)
        node_type = fm.get("type", "unknown")
        status = fm.get("status", "unknown")

        nodes[node_id] = {
            "id": node_id,
            "label": title,
            "type": node_type,
            "status": status,
            "path": rel,
            "frontmatter": {k: v for k, v in fm.items() if k != "frontmatter"},
        }

    # Second pass: build edges
    for fp in md_files:
        rel = fp.relative_to(VAULT_ROOT).as_posix()
        content = fp.read_text(encoding="utf-8")
        fm = extract_frontmatter(content)
        title = fm.get("title", fp.stem) if fm else fp.stem
        src_id = slugify(title) or slugify(fp.stem)

        if src_id not in nodes:
            continue

        # Links from frontmatter 'related'
        related = fm.get("related", []) if fm else []
        if isinstance(related, str):
            related = [related]
        for link in related:
            clean = link.strip("[] ")
            tgt_id = slugify(clean)
            if tgt_id in nodes and tgt_id != src_id:
                edges.append({
                    "from": src_id,
                    "to": tgt_id,
                    "relation": "related",
                    "source": "frontmatter",
                })

        # Links from body
        body_links = extract_wikilinks(content)
        for link in body_links:
            clean = link.split("|")[0].strip()  # Handle [[name|alias]]
            tgt_id = slugify(clean)
            if tgt_id in nodes and tgt_id != src_id:
                edges.append({
                    "from": src_id,
                    "to": tgt_id,
                    "relation": "links-to",
                    "source": "body",
                })

    index = {
        "meta": {
            "generated_at": datetime.now().isoformat(),
            "version": "0.1",
            "node_count": len(nodes),
            "edge_count": len(edges),
            "errors": len(errors),
        },
        "nodes": list(nodes.values()),
        "edges": edges,
        "errors": errors,
    }

    GRAPH_DIR.mkdir(parents=True, exist_ok=True)
    out_path = GRAPH_DIR / "index.json"
    out_path.write_text(json.dumps(index, ensure_ascii=False, indent=2), encoding="utf-8")

    print(f"Graph index built: {out_path}")
    print(f"  Nodes: {len(nodes)}")
    print(f"  Edges: {len(edges)}")
    print(f"  Errors: {len(errors)}")
    if errors:
        for e in errors[:5]:
            print(f"    - {e['file']}: {e['error']}")


if __name__ == "__main__":
    build_index()
