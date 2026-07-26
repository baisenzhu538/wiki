#!/usr/bin/env python3
"""KDO MCP Server — expose KDO knowledge base via Model Context Protocol.

Usage:
    python kdo-tools/mcp/server.py              # stdio transport (for MCP clients)
    python kdo-tools/mcp/server.py --sse --port 8765  # SSE transport (for remote agents)

MCP Tools exposed:
    kdo_search       — RRF fusion search (Graph RAG + BM25 + MOC)
    kdo_onboard      — Domain fast onboarding (MOC → framework → tools → cases)
    kdo_read         — Read full card content by ID
    kdo_capabilities — List all KDO capabilities

Design: Truman 建模四步法 → 解压展开 → MCP = framework-kdo-modeling-methodology 的
最外层编译产物。4 个 MCP Tool = 4 个 Feature（最小可操作能力单元），每个可独立调用、
跨工具迁移。
"""

import argparse
import json
import logging
import sys
from pathlib import Path

# Log to stderr — stdout is the MCP transport channel
logging.basicConfig(
    stream=sys.stderr,
    level=logging.INFO,
    format="[kdo-mcp] %(levelname)s %(message)s",
)
logger = logging.getLogger(__name__)

from mcp.server.fastmcp import FastMCP

from tools import search, onboard, read_card, capabilities

# ── Server definition ────────────────────────────────────────────────
mcp = FastMCP(
    "kdo",
    version="1.0.0",
    description="KDO Knowledge Delivery OS — AI-powered business knowledge factory",
)


# ── Tool: kdo_search ─────────────────────────────────────────────────
@mcp.tool()
async def kdo_search(
    query: str,
    domain: str | None = None,
    limit: int = 10,
) -> dict:
    """Search KDO knowledge base with RRF fusion (Graph RAG + BM25 + MOC priority).

    Use this when you need to find cards, frameworks, tools, or cases related to
    a business topic. Always use this BEFORE kdo_read — search first, then read
    the most relevant card for full details.

    The search engine combines vector similarity (for semantic understanding),
    BM25 keywords (for exact matching), and MOC domain priority (to surface the
    most important framework cards first).

    Args:
        query: Natural language query in Chinese or English.
               E.g. "销售过程分成几个环节", "customer segmentation framework"
        domain: Optional domain filter. If provided, search is scoped to that
                domain and MOC index cards get priority boost.
                E.g. "销售管理", "多模态", "AI协作"
        limit: Max results to return (1-20, default 10).

    Returns:
        Dictionary with:
        - results: list of {id, title, type, snippet, score, path}
        - engine: which search engine was used
        - query: the original query
    """
    logger.info(f"kdo_search: query={query!r}, domain={domain!r}, limit={limit}")
    result = search(query=query, domain=domain, limit=limit)
    return result


# ── Tool: kdo_onboard ────────────────────────────────────────────────
@mcp.tool()
async def kdo_onboard(domain: str) -> dict:
    """Fast-track onboarding to a KDO knowledge domain.

    Returns the domain's framework cards (the big picture), tool cards (how to
    apply it), case studies (real examples), and a suggested reading order.
    This is the FIRST tool to call when entering a new domain — it gives you
    the MOC (Map of Content) before you dive into individual cards.

    Think of it as: "Give me the 3-minute overview of everything we know about X."

    Args:
        domain: Domain name or description.
                E.g. "销售管理", "多模态", "AI协作", "调研", "内容生产"

    Returns:
        Dictionary with:
        - domain: matched domain name
        - framework: list of framework cards
        - tools: list of tool cards
        - cases: list of case studies
        - reading_order: suggested reading sequence
        - available_domains: (if no match) list of all domains
    """
    logger.info(f"kdo_onboard: domain={domain!r}")
    result = onboard(domain=domain)
    return result


# ── Tool: kdo_read ───────────────────────────────────────────────────
@mcp.tool()
async def kdo_read(card_id: str) -> dict:
    """Read the full content of a wiki card by its ID.

    Use this AFTER kdo_search or kdo_onboard — get the card ID from search
    results, then call kdo_read to get the complete card content including
    frontmatter metadata and body text.

    Args:
        card_id: Card identifier (filename without .md).
                 E.g. "framework-yitang-scientific-sales-five-step",
                 "tool-yitang-sales-process-decomposition"

    Returns:
        Dictionary with:
        - id: card identifier
        - title: card title
        - type: card type (framework/tool/case/concept/dk)
        - frontmatter: metadata (domain, status, confidence, related, etc.)
        - body: full card body text (capped at 10k characters)
        - path: relative path within the wiki
    """
    logger.info(f"kdo_read: card_id={card_id!r}")
    result = read_card(card_id=card_id)
    return result


# ── Tool: kdo_capabilities ───────────────────────────────────────────
@mcp.tool()
async def kdo_capabilities() -> dict:
    """List all KDO capabilities — frameworks, workflows, skills, and agent specs.

    Use this when you're new to KDO and want to know what's available, or when
    you need to discover which agent-specs and skills exist.

    Returns:
        Dictionary with:
        - frameworks: {count: N}
        - workflows: {count: N, list: [{id, file, title}]}
        - skills: {count: N}
        - agent_specs: [{id, title}]
    """
    logger.info("kdo_capabilities called")
    result = capabilities()
    return result


# ── Main ─────────────────────────────────────────────────────────────
def main():
    parser = argparse.ArgumentParser(description="KDO MCP Server")
    parser.add_argument("--sse", action="store_true", help="Use SSE transport instead of stdio")
    parser.add_argument("--port", type=int, default=8765, help="Port for SSE transport (default: 8765)")
    parser.add_argument("--host", default="127.0.0.1", help="Host for SSE transport")
    args = parser.parse_args()

    logger.info(f"KDO MCP Server v1.0.0 starting (transport={'sse' if args.sse else 'stdio'})")

    if args.sse:
        mcp.run(transport="sse", host=args.host, port=args.port)
    else:
        mcp.run(transport="stdio")


if __name__ == "__main__":
    main()
