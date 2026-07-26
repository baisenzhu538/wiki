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
    instructions=(
        "KDO is a business knowledge factory with 244 frameworks, 106 skills, "
        "10 workflows, and 8 agent specs covering sales, strategy, decision-making, "
        "multimodal production, and more.\n\n"
        "WORKFLOW for every new topic:\n"
        "1. kdo_onboard — get the domain map (frameworks + tools + cases + reading order)\n"
        "2. kdo_search — find specific cards for your question\n"
        "3. kdo_read — get the full card content with sources and related links\n\n"
        "CRITICAL: Always call kdo_onboard first for new domains. It prevents you from "
        "mistaking a single tool card for the full framework — the most common error "
        "new agents make when querying knowledge bases."
    ),
)


# ── Tool: kdo_search ─────────────────────────────────────────────────
@mcp.tool()
async def kdo_search(
    query: str,
    domain: str | None = None,
    limit: int = 10,
) -> dict:
    """Search KDO like Google for business topics.

    Type a business question and get the most relevant knowledge cards back.
    Framework cards are always ranked first so you see the big picture before
    diving into individual tools or cases.

    Usage examples:
    - "销售过程分成几个环节" → finds the Sales Process Decomposition framework
    - "怎么给客户分层" → finds the Customer Segmentation tool
    - "科学决策有什么框架" → finds the Scientific Decision framework

    Each result includes the card ID, title, type (framework/tool/case/concept),
    a content snippet, and the card's last-modified date so you can judge freshness.

    Args:
        query: Your business question in Chinese or English
        domain: Optional. Narrow search to one domain (e.g. "销售管理", "AI协作")
        limit: Max results (1-20, default 10)
    """
    logger.info(f"kdo_search: query={query!r}, domain={domain!r}, limit={limit}")
    result = search(query=query, domain=domain, limit=limit)
    return result


# ── Tool: kdo_onboard ────────────────────────────────────────────────
@mcp.tool()
async def kdo_onboard(domain: str) -> dict:
    """Get a 3-minute overview of everything KDO knows about a topic.

    Returns the core frameworks (the big picture), key tools (how to apply),
    real case studies, and a suggested reading order. Call this FIRST when
    exploring any new domain — it prevents the most common mistake of
    treating a single tool card as the full methodology.

    Available domains: 销售管理, 多模态, 发布, 内容生产, AI协作, 调研, 决策,
    五步法, 需求分析, KDO

    Args:
        domain: Domain name. E.g. "销售管理", "多模态", "AI协作"
    """
    logger.info(f"kdo_onboard: domain={domain!r}")
    result = onboard(domain=domain)
    return result


# ── Tool: kdo_read ───────────────────────────────────────────────────
@mcp.tool()
async def kdo_read(card_id: str) -> dict:
    """Read a knowledge card in full — frontmatter metadata + complete body text.

    Use this AFTER kdo_search or kdo_onboard to get the complete content of a
    specific card. Returns the card's source references (so you can trace where
    each claim came from), related cards (so you can explore connections), and
    the full body text.

    Args:
        card_id: Card ID from search/onboard results.
                 E.g. "framework-yitang-scientific-sales-five-step"
    """
    logger.info(f"kdo_read: card_id={card_id!r}")
    result = read_card(card_id=card_id)
    return result


# ── Tool: kdo_capabilities ───────────────────────────────────────────
@mcp.tool()
async def kdo_capabilities() -> dict:
    """See what KDO has — total counts of frameworks, skills, workflows, and agents.

    Call this once when first connecting to understand KDO's scale.
    Then use kdo_onboard to dive into specific domains.
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
