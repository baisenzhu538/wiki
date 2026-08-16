#!/usr/bin/env python3
"""飞书文档 MCP Server — 操作型 MCP（#306）：lark-cli 能力封装为 MCP。

从"检索型 MCP（kdo_search）"扩展出"操作型 MCP"——飞书文档读写：
让飞书 agent 从"给建议"升级为"交付物"（WorkBuddy 最强点：说人话→干活→交付物）。

Usage:
    python kdo-tools/mcp/feishu_doc_server.py              # stdio transport
    python kdo-tools/mcp/feishu_doc_server.py --sse --port 8766  # SSE transport

MCP Tools exposed:
    feishu_doc_create  — 创建飞书文档（含内容写入）
    feishu_doc_fetch   — 读取飞书文档内容
    feishu_doc_update  — 更新飞书文档（追加/修改内容）
    feishu_doc_search  — 搜索飞书文档/Wiki/表格
"""

import argparse
import json
import logging
import subprocess
import sys
from pathlib import Path

# Log to stderr — stdout is the MCP transport channel
logging.basicConfig(
    stream=sys.stderr,
    level=logging.INFO,
    format="[feishu-doc-mcp] %(levelname)s %(message)s",
)
logger = logging.getLogger(__name__)

from mcp.server.fastmcp import FastMCP

# lark-cli 可执行文件（小昭实测 v1.0.81 全套可用）
LARK_CLI = r"C:\Users\Administrator\.workbuddy\binaries\node\cli-connector-packages\node_modules\@larksuite\cli\bin\lark-cli.exe"

# ── Server definition ────────────────────────────────────────────────
mcp = FastMCP(
    "feishu-doc",
    instructions=(
        "飞书文档操作助手——创建/读取/更新/搜索飞书文档。\n\n"
        "WORKFLOW:\n"
        "1. feishu_doc_search — 找到目标文档\n"
        "2. feishu_doc_fetch — 读取现有内容\n"
        "3. feishu_doc_create / feishu_doc_update — 生成/修改交付物\n\n"
        "CRITICAL: 只操作已授权文档空间，不越权；high-risk-write 操作（删除等）不在此工具集。"
    ),
)


def _run_lark(args: list[str], timeout: int = 60) -> dict:
    """执行 lark-cli 命令，返回 JSON 结果。"""
    cmd = [LARK_CLI] + args
    logger.info(f"lark-cli: {' '.join(args[:6])}...")
    try:
        result = subprocess.run(
            cmd, capture_output=True, text=True, timeout=timeout,
            encoding="utf-8", errors="replace",
        )
        # lark-cli 输出 JSON 到 stdout
        out = result.stdout.strip()
        if not out:
            return {"ok": False, "error": result.stderr.strip()[:300] or "no output"}
        try:
            return json.loads(out)
        except json.JSONDecodeError:
            return {"ok": True, "raw": out[:2000]}
    except subprocess.TimeoutExpired:
        return {"ok": False, "error": f"timeout after {timeout}s"}
    except Exception as e:
        return {"ok": False, "error": str(e)}


# ── Tool: feishu_doc_create ──────────────────────────────────────────
@mcp.tool()
async def feishu_doc_create(title: str, content: str = "") -> dict:
    """Create a Lark/Feishu document.

    Creates a new document with the given title and optional content.
    Use this when you need to deliver a document (e.g. meeting minutes,
    agenda, one-pager) to the user's Feishu.

    Args:
        title: Document title (e.g. "周例会纪要 2026-08-09")
        content: Optional initial content in Markdown format
    """
    logger.info(f"feishu_doc_create: title={title!r}, content_len={len(content)}")
    args = ["docs", "+create", "--title", title]
    if content:
        args += ["--content", content]
    return _run_lark(args)


# ── Tool: feishu_doc_fetch ───────────────────────────────────────────
@mcp.tool()
async def feishu_doc_fetch(doc_token: str) -> dict:
    """Fetch a Lark/Feishu document's content.

    Reads the full content of a document by its token. Use AFTER
    feishu_doc_search to get the document token.

    Args:
        doc_token: Document token (from search results or URL)
    """
    logger.info(f"feishu_doc_fetch: doc_token={doc_token!r}")
    return _run_lark(["docs", "+fetch", "--doc-token", doc_token])


# ── Tool: feishu_doc_update ──────────────────────────────────────────
@mcp.tool()
async def feishu_doc_update(doc: str, content: str, command: str = "append") -> dict:
    """Update a Lark/Feishu document's content.

    Appends or replaces content in an existing document. Use this to
    write meeting minutes, update checklists, or add agenda items.

    Args:
        doc: Document URL or token (e.g. "WwjtddlnxofROgxo4Y0cMx1Xnfc" or full URL)
        content: Content to write (Markdown format)
        command: Operation — "append" (default) or "overwrite"
    """
    logger.info(f"feishu_doc_update: doc={doc!r}, command={command}, content_len={len(content)}")
    args = ["docs", "+update", "--doc", doc, "--command", command,
            "--doc-format", "markdown", "--content", content]
    return _run_lark(args, timeout=90)


# ── Tool: feishu_doc_search ──────────────────────────────────────────
@mcp.tool()
async def feishu_doc_search(query: str, limit: int = 5) -> dict:
    """Search Lark/Feishu docs, Wiki, and spreadsheets.

    Finds documents by keyword. Returns matching docs with their tokens
    so you can then fetch or update them.

    Args:
        query: Search keyword (e.g. "周例会", "复盘会纪要")
        limit: Max results (default 5)
    """
    logger.info(f"feishu_doc_search: query={query!r}, limit={limit}")
    return _run_lark(["docs", "+search", "--query", query, "--limit", str(limit)])


# ── Main ─────────────────────────────────────────────────────────────
def main():
    parser = argparse.ArgumentParser(description="飞书文档 MCP Server (#306)")
    parser.add_argument("--sse", action="store_true", help="Use SSE transport instead of stdio")
    parser.add_argument("--port", type=int, default=8766, help="Port for SSE transport")
    parser.add_argument("--host", default="127.0.0.1", help="Host for SSE transport")
    args = parser.parse_args()

    logger.info(f"飞书文档 MCP Server v1.0.0 starting (transport={'sse' if args.sse else 'stdio'})")

    if args.sse:
        mcp.run(transport="sse", host=args.host, port=args.port)
    else:
        mcp.run(transport="stdio")


if __name__ == "__main__":
    main()
