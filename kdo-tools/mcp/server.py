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
import asyncio
import importlib
import json
import logging
import sys
from pathlib import Path

# #350 UTF-8 修复：stdin/stderr reconfigure utf-8（Windows 中文管道默认 cp936）
# 注意：不能动 sys.stdout——它是 MCP 传输通道，FastMCP 管理其缓冲，reconfigure 会破坏响应 flush
sys.stdin.reconfigure(encoding="utf-8")
sys.stderr.reconfigure(encoding="utf-8")

# Log to stderr — stdout is the MCP transport channel
logging.basicConfig(
    stream=sys.stderr,
    level=logging.INFO,
    format="[kdo-mcp] %(levelname)s %(message)s",
)
logger = logging.getLogger(__name__)

from mcp.server.fastmcp import FastMCP
from mcp.types import CallToolResult, TextContent, ToolAnnotations

# #353 协议合规：只读工具声明 + 错误契约（isError）+ 输出安全
_READONLY = ToolAnnotations(readOnlyHint=True)

import tools

# ── 热重载（#体检后续修）：工具调用前 stat tools.py mtime，变更即 reload ──
# 背景：server 是宿主拉起的长驻进程，tools.py 修完后进程仍跑旧代码，
# 无法从会话内部重启。此机制让 tools.py 的修复在下一次调用自动生效，
# 无需重启。安全性：tools.py 模块级状态仅 env 路径 + mtime 失效缓存，
# reload 丢弃缓存后自动重建；FastMCP 逐条串行处理，无并发重载风险。
_TOOLS_FILE = Path(__file__).parent / "tools.py"
_tools_mtime: int | None = None


def _maybe_reload_tools() -> None:
    """tools.py 变更检测 + 热重载。失败时保留旧模块并下次重试（不更新 mtime）。"""
    global _tools_mtime
    try:
        mtime = _TOOLS_FILE.stat().st_mtime_ns
    except OSError:
        return  # 文件暂时不可访问（如编辑器原子替换窗口），下次再查
    if _tools_mtime is None:
        _tools_mtime = mtime
        return
    if mtime == _tools_mtime:
        return
    try:
        importlib.reload(tools)
        _tools_mtime = mtime
        logger.info("[hot-reload] tools.py 已变更，热重载完成")
    except Exception as e:
        logger.warning(f"[hot-reload] 重载失败，继续用旧代码（下次调用重试）: {e}")


def _wrap(result):
    """#353: 工具返回含 error 键（内部兜底返回）→ 统一为协议级 isError。"""
    if isinstance(result, dict) and "error" in result:
        return CallToolResult(content=[TextContent(type="text", text=str(result["error"]))], isError=True)
    return result

# #351: 检索在主事件循环线程同步执行（LightRAG 内部 worker 依赖主线程
# get_event_loop；任何子线程/后台 loop 方案都会崩或静默卡死）。
# 阻塞问题用 warmup 解决：启动预热后调用走进程缓存 0s，事件循环占用可忽略，
# keepalive 正常。FastMCP 逐条处理消息天然串行，无需锁。

# ── Server definition ────────────────────────────────────────────────
# #354/#356: instructions 统计动态化（不写死数字——capabilities 走索引后统计廉价）
try:
    _caps = tools.capabilities()
    _fw = _caps.get("frameworks", {}).get("count", "?")
    _sk = _caps.get("skills", {}).get("count", "?")
    _wf = _caps.get("workflows", {}).get("count", "?")
    _sp = len(_caps.get("agent_specs", []))
except Exception:
    _fw = _sk = _wf = _sp = "?"

mcp = FastMCP(
    "kdo",
    instructions=(
        f"KDO is a business knowledge factory with {_fw} frameworks, {_sk} skills, "
        f"{_wf} workflows, and {_sp} agent specs covering sales, strategy, decision-making, "
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
@mcp.tool(annotations=_READONLY)
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
    try:
        _maybe_reload_tools()
        result = await tools.search(query=query, domain=domain, limit=limit)
        return _wrap(result)
    except Exception as e:
        logger.exception("kdo_search failed")  # 栈保留到 stderr
        return CallToolResult(content=[TextContent(type="text", text=f"kdo_search error: {e}")], isError=True)


# ── Tool: kdo_onboard ────────────────────────────────────────────────
@mcp.tool(annotations=_READONLY)
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
    try:
        _maybe_reload_tools()
        result = tools.onboard(domain=domain)
        return _wrap(result)
    except Exception as e:
        logger.exception("kdo_onboard failed")
        return CallToolResult(content=[TextContent(type="text", text=f"kdo_onboard error: {e}")], isError=True)


# ── Tool: kdo_read ───────────────────────────────────────────────────
@mcp.tool(annotations=_READONLY)
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
    try:
        _maybe_reload_tools()
        result = tools.read_card(card_id=card_id)
        return _wrap(result)
    except Exception as e:
        logger.exception("kdo_read failed")
        return CallToolResult(content=[TextContent(type="text", text=f"kdo_read error: {e}")], isError=True)


# ── Tool: kdo_help（#352 裁决：help_guide 死代码 → 注册为工具，首连引导有价值）───
@mcp.tool(annotations=_READONLY)
async def kdo_help() -> dict:
    """First-time onboarding guide — call this once when connecting.

    Returns what KDO is, how to search effectively, and common patterns
    for different question types. Then use kdo_search / kdo_onboard / kdo_read.
    """
    logger.info("kdo_help called")
    try:
        _maybe_reload_tools()
        result = tools.help_guide()
        return _wrap(result)
    except Exception as e:
        logger.exception("kdo_help failed")
        return CallToolResult(content=[TextContent(type="text", text=f"kdo_help error: {e}")], isError=True)


# ── Tool: kdo_capabilities ───────────────────────────────────────────
@mcp.tool(annotations=_READONLY)
async def kdo_capabilities() -> dict:
    """See what KDO has — total counts of frameworks, skills, workflows, and agents.

    Call this once when first connecting to understand KDO's scale.
    Then use kdo_onboard to dive into specific domains.
    """
    logger.info("kdo_capabilities called")
    try:
        _maybe_reload_tools()
        result = tools.capabilities()
        return _wrap(result)
    except Exception as e:
        logger.exception("kdo_capabilities failed")
        return CallToolResult(content=[TextContent(type="text", text=f"kdo_capabilities error: {e}")], isError=True)


# ── Main ─────────────────────────────────────────────────────────────
async def _warmup() -> None:
    """启动预热：主 loop 内预加载索引/LightRAG 缓存（LightRAG worker 依赖
    主线程 get_event_loop，且 initialize_storages 绑定查询 loop——必须在
    mcp.run_async 之前、同一事件循环内执行）。预热后调用走缓存 0s。"""
    try:
        logger.info("[warmup] 预加载检索缓存...")
        await tools.search(query="预热", limit=1)
        logger.info("[warmup] 完成")
    except Exception as e:
        logger.warning(f"[warmup] 失败（不阻塞，首次调用会慢）: {e}")


def main():
    parser = argparse.ArgumentParser(description="KDO MCP Server")
    parser.add_argument("--sse", action="store_true", help="[DEPRECATED] Use SSE transport (MCP 2025-06-18 规范：SSE→Streamable HTTP；当前无客户端在用，迁移见 P3)")
    parser.add_argument("--port", type=int, default=8765, help="Port for SSE transport (default: 8765)")
    parser.add_argument("--host", default="127.0.0.1", help="Host for SSE transport")
    args = parser.parse_args()

    logger.info(f"KDO MCP Server v1.0.0 starting (transport={'sse' if args.sse else 'stdio'})")

    if args.sse:
        mcp.run(transport="sse", host=args.host, port=args.port)
    else:
        # 启动预热：与主 loop 同一事件循环内执行，避免 LightRAG 跨 loop
        # 绑定（initialize_storages 绑定的 loop 必须与查询 loop 相同）。
        # mcp.run 内部是 anyio.run(self.run_stdio_async)——外层同样用
        # anyio.run 包 warmup + run_stdio_async，保证同一循环。
        import anyio

        async def _main_with_warmup():
            await _warmup()
            await mcp.run_stdio_async()

        anyio.run(_main_with_warmup)


if __name__ == "__main__":
    main()
