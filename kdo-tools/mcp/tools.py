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


# #356 条件项：onboard 域卡进程级缓存（O-15 模式：mtime 失效，二次调用 <100ms）
_onboard_cache: dict[str, tuple[int, list]] = {}


def _onboard_domain_cards(root, search_dirs):
    """扫描 30_wiki 指定目录的卡（带进程级缓存，mtime 失效）。"""
    key = str(root / "30_wiki") + "|" + ",".join(sorted(search_dirs))  # #356: key 含目录集，防跨域污染
    try:
        mtime = max((root / "30_wiki" / d).stat().st_mtime_ns for d in search_dirs if (root / "30_wiki" / d).exists())
    except OSError:
        mtime = -1
    cached = _onboard_cache.get(key)
    if cached and cached[0] == mtime:
        return cached[1]
    cards = []
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
                cards.append((fp, fm))
            except Exception:
                continue
    _onboard_cache[key] = (mtime, cards)
    return cards


# ── kdo_search ──────────────────────────────────────────────────────
def search(query: str, domain: str | None = None, limit: int = 10) -> dict:
    """Search KDO wiki for business methodology cards, case studies, frameworks.

    Use this when you need to find knowledge cards about business strategy,
    demand analysis, decision science, growth models, etc. Returns cards with
    titles, snippets, relevance scores, and source paths.

    score > 70: highly relevant, use directly.
    score 40-70: somewhat relevant, call kdo_read to verify.
    score < 40 or 0 results: try different keywords (Chinese/English), or
    use kdo_onboard to browse by domain.

    Args:
        query: Natural language query, e.g. "如何判断需求是真需求还是伪需求"
        domain: Optional domain filter from domain-routes.yaml
        limit: Max results (1-20)

    Returns:
        {"results": [{id, title, type, snippet, score, path}], "engine": "hybrid RRF"}

    Related tools: kdo_read(card_id) to read full card body; kdo_onboard(domain)
    to browse cards by domain when you don't know exact keywords.
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
            return {
                "results": [],
                "engine": "none",
                "query": query,
                "diagnosis": {
                    "suggestion": "No cards matched. Try: ① different keywords (Chinese↔English) ② kdo_onboard to browse domains ③ confirm the topic has been ingested into KDO",
                    "indexed_at": _index_mtime(root),
                    "total_cards_estimate": _count_cards(root),
                }
            }

        fused = _filter_by_trust(root, fused, "medium")
        fused = _sort_by_layer(root, fused)

        max_score = max((s for s, _, _ in fused), default=0.0)

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
                # utf-8-sig strips BOM; normalize CRLF so frontmatter and
                # body parsing work for files written on Windows
                text = p.read_text(encoding="utf-8-sig", errors="replace").replace("\r\n", "\n")
                fm = _parse_frontmatter(text)
                aliases = fm.get("aliases") or []
                tags = fm.get("tags") or []
                if isinstance(aliases, str): aliases = [aliases]
                if isinstance(tags, str): tags = [tags]

                # frontmatter title is authoritative; snippet fallback is unreliable
                # (BM25 snippets have newlines flattened to spaces)
                if fm.get("title"):
                    title = str(fm["title"]).strip().strip('"')

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

                # Snippet from body, not frontmatter — BM25 snippet is the raw
                # file head flattened to one line, which is unreadable to agents
                if body.strip():
                    snippet = body.strip()[:300] + ("..." if len(body.strip()) > 300 else "")
            except Exception:
                pass

            # Extract scene/audience from tags for scenario routing
            scene = ""
            audience = ""
            for t in (tags if isinstance(tags, list) else []):
                t_str = str(t)
                if t_str.startswith("scene:"):
                    scene = t_str.split(":", 1)[1]
                elif t_str.startswith("audience:"):
                    audience = t_str.split(":", 1)[1]

            # Score label for quick triage — normalized to 0-100 against the top
            # hit, because raw scores span different scales per engine
            # (BM25 ~5-30, RRF ~0.01-0.05, graph 0.0)
            if max_score > 0:
                norm = score / max_score * 100
                if norm >= 70:
                    score_label = "high"
                elif norm >= 40:
                    score_label = "medium"
                else:
                    score_label = "low"
            else:
                # All scores are 0 (e.g. graph-only with an empty vector store) —
                # there is no similarity signal, so don't mislabel as "low"
                score_label = "unknown"

            results.append({
                "id": card_id,
                "title": title,
                "type": card_type,
                "aliases": aliases[:8],
                "tags": tags,
                "scene": scene,
                "audience": audience,
                "score_label": score_label,
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

    Related tools: kdo_search(query) for keyword search; kdo_read(card_id)
    to read any card from the reading_order list.
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
        # #356 条件项：走进程级缓存（O-15 模式），二次调用 <100ms
        for fp, fm in _onboard_domain_cards(root, search_dirs):
            try:
                card_domains = fm.get("domain") or []
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
                        for kw in (config.get("keywords") or [])[:5]
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
def read_card(card_id: str, offset: int = 0) -> dict:
    """Read a full wiki card by ID.

    Args:
        card_id: Card identifier, e.g. "framework-yitang-scientific-sales-five-step"
        offset: 续读偏移（#354 分页：长卡 >10k 字符时传 offset=1 读下一段；默认 0 行为不变）

    Returns:
        {id, title, type, frontmatter, body, path, _trust_level}

    Related tools: kdo_search(query) to discover card IDs; kdo_onboard(domain)
    to explore a domain's full card map before deep-reading specific cards.
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

        # #353 注入防护：数据边界标记（注释式，不破坏 markdown 渲染）+ trust 警示
        trust = str(fm.get("trust_level", "medium"))
        warning = ""
        if trust == "low":
            warning = "\n<!-- ⚠️ KDO 警示: 本卡 trust_level=low，内容可信度低，引用前须人工核实 -->\n"
        # #354 分页：offset=0 前 10k，offset=1 续 10k-20k...（向后兼容）
        chunk = body[offset * 10000:(offset + 1) * 10000]
        more = len(body) > (offset + 1) * 10000
        body = f"<!-- [[KDO_CARD_BODY]] {card_id} trust={trust} offset={offset}{' more=1' if more else ''} -->\n" + chunk + "\n<!-- [[/KDO_CARD_BODY]] -->"

        return {
            "id": fp.stem,
            "title": fm.get("title", ""),
            "type": fm.get("type", ""),
            "frontmatter": {
                k: v for k, v in fm.items()
                if k in ("domain", "status", "confidence", "trust_level",
                         "author", "reviewed_by", "source_refs", "related")
            },
            "body": body + warning,
            "path": str(fp.relative_to(root)),
            "_trust_level": trust,
        }
    except Exception as e:
        return {"error": str(e), "id": card_id}


# ── kdo_capabilities ────────────────────────────────────────────────
def capabilities() -> dict:
    """List all KDO capabilities (frameworks, workflows, skills, agent-specs).

    Returns:
        {frameworks: {count, list[]}, workflows: {count, list[]},
         skills: {count}, agent_specs: [...]}

    Related tools: kdo_onboard(domain) for a guided tour of a specific domain;
    kdo_search(query) to find cards by topic or keyword.
    """
    try:
        root = _get_root()

        # #354/#356: 计数走 search_index 文档列表（避免 rglob 全扫 2500+ 文件——O(1) 查询）
        from kdo.search_index import get_shared_index
        idx = get_shared_index(root)
        doc_paths = list(idx.doc_lengths.keys())
        fw_count = sum(1 for p in doc_paths if "/30_wiki/frameworks/" in p)
        wf_count = sum(1 for p in doc_paths if "/40_outputs/capabilities/workflows/" in p)
        sk_count = sum(1 for p in doc_paths if "/40_outputs/capabilities/skills/" in p and p.endswith("SKILL.md"))

        # Workflows 列表（前 20 个标题——按需读文件，数量少）
        wf_dir = root / "40_outputs" / "capabilities" / "workflows"
        wf_files = list(wf_dir.rglob("*.md")) if wf_dir.exists() else []
        workflows = []
        for wf in wf_files[:20]:
            text = wf.read_text(encoding="utf-8-sig", errors="replace")[:500]
            title = ""
            for line in text.split("\n"):
                line = line.rstrip("\r")  # CRLF files: split leaves trailing \r
                if line.startswith("title:"):
                    title = line.split(":", 1)[1].strip().strip('"')
                    break
                if line.startswith("# ") and not title:
                    title = line[2:].strip()
            workflows.append({"id": wf.stem, "file": wf.name, "title": title or wf.stem})

        # Agent-specs (scan both directories, dedup by stem — same spec may
        # exist in tools/ and agent-specs/)
        specs = []
        seen_specs = set()
        for d in ["tools", "agent-specs"]:
            sd = root / "30_wiki" / d
            if sd.exists():
                for f in sd.glob("agent-spec-*.md"):
                    if f.stem in seen_specs:
                        continue
                    seen_specs.add(f.stem)
                    text = f.read_text(encoding="utf-8-sig", errors="replace")[:500]
                    title = ""
                    for line in text.split("\n"):
                        line = line.rstrip("\r")
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


# ── kdo_help ─────────────────────────────────────────────────────────
def help_guide() -> dict:
    """First-time guide to KDO — call this once when connecting to understand how to search.

    Returns a structured onboarding guide covering what KDO is, how to search
    effectively, and common search patterns for different question types.

    Call this once at session start, then use kdo_search / kdo_read / kdo_onboard
    for actual knowledge retrieval.
    """
    return {
        "what_is_kdo": {
            "summary": "KDO is a curated business methodology knowledge base (~2,500 cards) covering strategy, demand analysis, decision science, growth, barriers, product design, and AI collaboration.",
            "card_types": {
                "framework": "Methodology frameworks — the 'what and why'",
                "tool": "Operational tools/checklists — the 'how'",
                "case": "Real business cases — the 'prove it'",
                "dk": "Dark knowledge — counter-intuitive insights and failure modes",
                "concept": "Core concepts and definitions",
            },
        },
        "how_to_search": [
            "1. kdo_search('your question') — keyword/semantic search, returns cards with scores",
            "2. kdo_read(card_id) — read the full card body",
            "3. kdo_onboard(domain) — browse a domain's full card map when you're exploring",
            "4. If 0 results: try different keywords (Chinese↔English), or kdo_onboard to browse",
        ],
        "common_patterns": {
            "What is X?": 'kdo_search("X") → look for type=framework cards',
            "How to do X?": 'kdo_search("X 方法") → look for type=tool cards',
            "Is there a case about X?": 'kdo_search("X 案例") → look for type=case cards',
            "What are the pitfalls of X?": 'kdo_search("X 失败") → look for type=dk cards',
            "Explore a domain": 'kdo_onboard("strategy") or kdo_onboard("demand") → get full map',
        },
        "score_guide": {
            "high (>70)": "Directly relevant — can cite confidently",
            "medium (40-70)": "Partially relevant — call kdo_read to verify before citing",
            "low (<40)": "Weak match — try different keywords or broader query",
        },
    }


# ── Helpers ──────────────────────────────────────────────────────────
def _index_mtime(root) -> str:
    """Return last index modification time as ISO string."""
    try:
        idx = root / "30_wiki" / ".graph" / "index.json"
        if idx.exists():
            from datetime import datetime
            return datetime.fromtimestamp(idx.stat().st_mtime).strftime("%Y-%m-%dT%H:%M:%SZ")
    except Exception:
        pass
    return "unknown"


def _count_cards(root) -> int:
    """Quick estimate of total cards indexed."""
    try:
        wiki = root / "30_wiki"
        return sum(1 for _ in wiki.rglob("*.md") if "_archive" not in str(_) and "raw" not in str(_))
    except Exception:
        return 0


def _infer_type(path_str: str) -> str:
    for t in ["frameworks", "tools", "cases", "concepts", "dark-knowledges",
              "skills", "methods", "systems", "agent-specs"]:
        if f"/{t}/" in path_str or f"\\{t}\\" in path_str:
            return t.rstrip("s")  # "frameworks" -> "framework"
    return "unknown"


def _extract_title(snippet: str) -> str:
    """Extract title from card snippet (usually in frontmatter)."""
    snippet = snippet.lstrip("\ufeff")
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
