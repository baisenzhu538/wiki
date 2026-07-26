"""KDO MCP Tool Handlers — bridges KDO internals to MCP tool calls.

All functions return dicts (JSON-serializable). No MCP types here — this module
is pure business logic, testable without an MCP server.
"""

import json
import os
import sys
from pathlib import Path

# Ensure KDO source and wiki tools are importable
_KDO_SRC = Path(os.environ.get(
    "KDO_SRC",
    r"C:\Users\Administrator\Knowledge Delivery OS 0.0.1",
))
_WIKI_ROOT = Path(os.environ.get(
    "WIKI_ROOT",
    r"C:\Users\Administrator\Desktop\wiki",
))
if str(_KDO_SRC) not in sys.path:
    sys.path.insert(0, str(_KDO_SRC))
if str(_WIKI_ROOT) not in sys.path:
    sys.path.insert(0, str(_WIKI_ROOT))


def _get_root():
    return _WIKI_ROOT


# ── kdo_search ──────────────────────────────────────────────────────
def search(query: str, domain: str | None = None, limit: int = 10) -> dict:
    """RRF fusion search (Graph RAG + BM25 + MOC priority boost).

    Args:
        query: Natural language query, e.g. "销售过程 环节 阶段"
        domain: Optional domain filter from domain-routes.yaml
        limit: Max results (1-20)

    Returns:
        {"results": [{id, title, type, snippet, score, path}], "engine": "hybrid RRF"}
    """
    try:
        from kdo.commands.delivery import (
            _try_graph_query, _try_bm25_query, _rrf_fuse,
            _filter_by_trust, _sort_by_layer,
        )
        from kdo.workspace import safe_read

        root = _get_root()
        limit = max(1, min(limit, 20))

        graph = _try_graph_query(root, query, limit * 2) or []
        bm25 = _try_bm25_query(root, query, limit * 2) or []

        if graph and bm25:
            fused = _rrf_fuse(graph, bm25, root, query, limit)
            engine = "hybrid RRF (graph+BM25+MOC)"
        elif graph:
            fused = [(s, str(p), sn) for s, p, sn in graph[:limit]]
            engine = "graph RAG"
        elif bm25:
            fused = [(s, str(p), sn) for s, p, sn in bm25[:limit]]
            engine = "BM25"
        else:
            return {"results": [], "engine": "none", "query": query}

        fused = _filter_by_trust(root, fused, "medium")
        fused = _sort_by_layer(root, fused)

        results = []
        for score, path_str, snippet in fused[:limit]:
            p = Path(path_str)
            card_id = p.stem
            card_type = _infer_type(path_str)
            title = _extract_title(snippet)

            # Get freshness from file mtime
            try:
                mtime = p.stat().st_mtime
                from datetime import datetime
                updated_at = datetime.fromtimestamp(mtime).strftime("%Y-%m-%d")
            except Exception:
                updated_at = "unknown"

            # Extract full metadata for routing decisions (aliases, tags, position)
            aliases = []
            tags = []
            position = ""

            try:
                text = p.read_text(encoding="utf-8", errors="replace")
                fm = _parse_frontmatter(text)
                aliases = fm.get("aliases") or []
                tags = fm.get("tags") or []
                if isinstance(aliases, str): aliases = [aliases]
                if isinstance(tags, str): tags = [tags]

                # Extract定位声明 (first blockquote or meaningful line after frontmatter)
                body_start = text.find("\n---\n", 4)
                body = text[body_start + 5:] if body_start > 0 else text
                for line in body.strip().split("\n"):
                    stripped = line.strip()
                    if stripped.startswith(">"):
                        position = stripped.lstrip("> ").strip()
                        break
                    if stripped and not stripped.startswith("#"):
                        position = stripped[:200]
                        break
            except Exception:
                pass

            results.append({
                "id": card_id,
                "title": title,
                "type": card_type,
                "aliases": aliases[:8],
                "tags": tags,
                "position": position,
                "snippet": snippet[:500],
                "score": round(score, 3),
                "updated_at": updated_at,
                "path": str(p.relative_to(root)) if str(p).startswith(str(root)) else path_str,
            })

        return {"results": results, "engine": engine, "query": query}
    except Exception as e:
        return {"results": [], "engine": "error", "error": str(e), "query": query}


# ── kdo_onboard ─────────────────────────────────────────────────────
def onboard(domain: str) -> dict:
    """Domain fast onboarding — MOC-first guided tour.

    Returns the domain's framework, tools, cases, skills, and suggested reading order.
    Uses domain-routes.yaml for MOC index card discovery.

    Args:
        domain: Domain name or natural language description.
                E.g. "销售管理", "多模态", "AI协作"

    Returns:
        {domain, framework, tools[], cases[], skills[], reading_order[]}
    """
    try:
        import yaml
        root = _get_root()
        routes_path = root / "90_control" / "domain-routes.yaml"
        if not routes_path.exists():
            return {"error": "domain-routes.yaml not found", "domain": domain}

        routes = yaml.safe_load(routes_path.read_text(encoding="utf-8"))
        domains = routes.get("domains", {})

        # Match domain by name or keyword
        matched = None
        domain_lower = domain.lower()
        for dname, config in domains.items():
            if dname in domain or domain in dname:
                matched = (dname, config)
                break
        if not matched:
            for dname, config in domains.items():
                for kw in config.get("keywords", []):
                    if kw.lower() in domain_lower:
                        matched = (dname, config)
                        break
                if matched:
                    break

        if not matched:
            available = list(domains.keys())
            return {
                "domain": domain,
                "matched": False,
                "available_domains": available,
                "hint": f"Domain not found. Try one of: {', '.join(available)}",
            }

        dname, config = matched
        index_cards = config.get("index_cards", [])
        search_dirs = config.get("search_dirs", ["frameworks", "tools", "cases", "concepts"])

        # Scan for cards in this domain
        framework_cards = []
        tool_cards = []
        case_cards = []
        concept_cards = []

        wiki_dir = root / "30_wiki"
        for d in search_dirs:
            sd = wiki_dir / d
            if not sd.exists():
                continue
            for fp in sd.rglob("*.md"):
                if "_archive" in str(fp) or "raw" in str(fp):
                    continue
                try:
                    text = fp.read_text(encoding="utf-8", errors="replace")
                    fm = _parse_frontmatter(text)
                    card_domains = fm.get("domain", [])
                    if isinstance(card_domains, str):
                        card_domains = [card_domains]
                    card_title = fm.get("title", fp.stem)
                    card_type = fm.get("type", "concept")

                    # Match by domain field or keyword in title
                    dname_lower = dname.lower()
                    matches_domain = any(
                        dname_lower in str(d).lower() for d in card_domains
                    )
                    if not matches_domain:
                        title_lower = card_title.lower()
                        matches_domain = any(
                            kw.lower() in title_lower
                            for kw in config.get("keywords", [])[:5]
                        )
                    if not matches_domain:
                        continue

                    entry = {"id": fp.stem, "title": card_title}
                    if card_type == "framework":
                        framework_cards.append(entry)
                    elif card_type in ("tool", "tool-agent-spec"):
                        tool_cards.append(entry)
                    elif card_type == "case":
                        case_cards.append(entry)
                    else:
                        concept_cards.append(entry)
                except Exception:
                    continue

        # Build reading order
        reading_order = []
        for fw in framework_cards:
            reading_order.append({"step": f"理解框架", "card": fw["id"], "title": fw["title"]})
        for tool in tool_cards[:5]:
            reading_order.append({"step": "掌握工具", "card": tool["id"], "title": tool["title"]})
        for case in case_cards[:3]:
            reading_order.append({"step": "验证案例", "card": case["id"], "title": case["title"]})

        return {
            "domain": dname,
            "matched": True,
            "framework": framework_cards,
            "tools": tool_cards[:8],
            "cases": case_cards[:5],
            "concepts": concept_cards[:5],
            "reading_order": reading_order[:10],
            "index_cards": index_cards,
        }
    except Exception as e:
        return {"error": str(e), "domain": domain}


# ── kdo_read ────────────────────────────────────────────────────────
def read_card(card_id: str) -> dict:
    """Read a full wiki card by ID.

    Args:
        card_id: Card identifier, e.g. "framework-yitang-scientific-sales-five-step"

    Returns:
        {id, title, type, frontmatter, body, path}
    """
    try:
        root = _get_root()
        wiki = root / "30_wiki"
        fp = None
        for d in ["frameworks", "tools", "cases", "concepts", "dark-knowledges",
                   "skills", "methods", "systems", "agent-specs", "domains"]:
            candidate = wiki / d / f"{card_id}.md"
            if candidate.exists():
                fp = candidate
                break

        if not fp:
            return {"error": f"Card not found: {card_id}", "id": card_id}

        text = fp.read_text(encoding="utf-8", errors="replace")
        fm = _parse_frontmatter(text)
        body_start = text.find("\n---\n", 4)
        body = text[body_start + 5:] if body_start > 0 else text

        return {
            "id": fp.stem,
            "title": fm.get("title", ""),
            "type": fm.get("type", ""),
            "frontmatter": {
                k: v for k, v in fm.items()
                if k in ("domain", "status", "confidence", "trust_level",
                         "author", "reviewed_by", "source_refs", "related")
            },
            "body": body[:10000],  # cap at 10k chars
            "path": str(fp.relative_to(root)),
        }
    except Exception as e:
        return {"error": str(e), "id": card_id}


# ── kdo_capabilities ────────────────────────────────────────────────
def capabilities() -> dict:
    """List all KDO capabilities (frameworks, workflows, skills, agent-specs).

    Returns:
        {frameworks: {count, list[]}, workflows: {count, list[]},
         skills: {count}, agent_specs: [...]}
    """
    try:
        root = _get_root()

        # Frameworks
        fw_dir = root / "30_wiki" / "frameworks"
        fw_count = len(list(fw_dir.rglob("*.md"))) if fw_dir.exists() else 0

        # Workflows
        wf_dir = root / "40_outputs" / "capabilities" / "workflows"
        wf_files = list(wf_dir.rglob("*.md")) if wf_dir.exists() else []
        workflows = []
        for wf in wf_files[:20]:
            text = wf.read_text(encoding="utf-8", errors="replace")[:500]
            title = text.split("\n")[0].lstrip("# ").strip() if text else wf.stem
            workflows.append({"id": wf.stem, "file": wf.name, "title": title})

        # Skills
        sk_dir = root / "40_outputs" / "capabilities" / "skills"
        sk_count = sum(1 for _ in sk_dir.rglob("SKILL.md")) if sk_dir.exists() else 0

        # Agent-specs (scan both directories)
        specs = []
        for d in ["tools", "agent-specs"]:
            sd = root / "30_wiki" / d
            if sd.exists():
                for f in sd.glob("agent-spec-*.md"):
                    text = f.read_text(encoding="utf-8", errors="replace")[:500]
                    title = ""
                    for line in text.split("\n"):
                        if line.startswith("title:") or line.startswith("# "):
                            title = line.split(":", 1)[-1].strip().strip('"').lstrip("# ")
                            break
                    specs.append({"id": f.stem, "title": title or f.stem})

        return {
            "frameworks": {"count": fw_count},
            "workflows": {"count": len(wf_files), "list": workflows},
            "skills": {"count": sk_count},
            "agent_specs": specs,
        }
    except Exception as e:
        return {"error": str(e)}


# ── Helpers ──────────────────────────────────────────────────────────
def _infer_type(path_str: str) -> str:
    for t in ["frameworks", "tools", "cases", "concepts", "dark-knowledges",
              "skills", "methods", "systems", "agent-specs"]:
        if f"/{t}/" in path_str or f"\\{t}\\" in path_str:
            return t.rstrip("s")  # "frameworks" -> "framework"
    return "unknown"


def _extract_title(snippet: str) -> str:
    """Extract title from card snippet (usually in frontmatter)."""
    for line in snippet.split("\n"):
        if line.strip().startswith("title:"):
            return line.split("title:", 1)[1].strip().strip('"')
    first = snippet.strip().split("\n")[0]
    return first.lstrip("# ").strip()[:80]


def _parse_frontmatter(text: str) -> dict:
    if not text.startswith("---\n"):
        return {}
    end = text.find("\n---\n", 4)
    if end == -1:
        return {}
    try:
        import yaml
        return yaml.safe_load(text[4:end]) or {}
    except Exception:
        return {}
