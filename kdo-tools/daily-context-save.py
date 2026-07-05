#!/usr/bin/env python3
"""
Agent 每日上下文自动存储——双写管线。

每次保存同时写入两个位置：
  1. 桌面 agent复盘/<agent>/daily-context/YYYY-MM-DD.md  （人看）
  2. 60_feedback/session-archives/YYYY-MM-DD/{agent-id}.md （Agent检索+kdo query可查）

Usage:
  python kdo-tools/daily-context-save.py save --agent <id> --text "<摘要>" [--before "<...>" --after "<...>"]
  python kdo-tools/daily-context-save.py list --agent <id>
"""

import argparse
import sys
from datetime import datetime, timezone
from pathlib import Path

WIKI = Path(__file__).resolve().parent.parent
REVIEW_DIR = Path.home() / "Desktop" / "agent复盘"
ARCHIVE_DIR = WIKI / "60_feedback" / "session-archives"

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")


def now_iso():
    return datetime.now(timezone.utc).isoformat()


def cmd_save(args):
    agent = args.agent
    today = datetime.now().strftime("%Y-%m-%d")
    ts = now_iso()
    session_id = f"{agent}-{today}"

    # Build frontmatter
    fm_lines = [
        "---",
        f"session_id: {session_id}",
        f"agent_id: {agent}",
        f"date: {today}",
        f"created_at: {ts}",
        f"updated_at: {ts}",
    ]
    if args.before:
        fm_lines.append(f'before: "{args.before[:200]}"')
    if args.after:
        fm_lines.append(f'after: "{args.after[:200]}"')
    fm_lines.append("---")
    fm = "\n".join(fm_lines)

    body = args.text or "(无内容)"
    content = f"{fm}\n\n# {agent} · {today}\n\n{body}\n"

    # Write 1: Desktop (human-readable)
    desktop_dir = REVIEW_DIR / agent / "daily-context"
    desktop_dir.mkdir(parents=True, exist_ok=True)
    desktop_path = desktop_dir / f"{today}.md"
    desktop_path.write_text(content, encoding="utf-8")

    # Write 2: Archive (agent-searchable, kdo query can find)
    archive_dir = ARCHIVE_DIR / today
    archive_dir.mkdir(parents=True, exist_ok=True)
    archive_path = archive_dir / f"{agent}.md"
    archive_path.write_text(content, encoding="utf-8")

    print(f"已保存：{desktop_path}")
    print(f"已存档：{archive_path.relative_to(WIKI)}")
    return 0


def cmd_list(args):
    agent = args.agent
    d = REVIEW_DIR / agent / "daily-context"
    if not d.exists():
        print("暂无上下文记录")
        return 0
    files = sorted(d.glob("*.md"), reverse=True)
    print(f"{agent} 每日上下文（{len(files)} 条）")
    for f in files[:10]:
        size = f.stat().st_size
        print(f"  {f.stem} — {size}B")
    return 0


def main():
    parser = argparse.ArgumentParser(description="Agent 每日上下文存储")
    sub = parser.add_subparsers(dest="cmd", required=True)

    p_save = sub.add_parser("save", help="保存今日上下文")
    p_save.add_argument("--agent", required=True)
    p_save.add_argument("--text", default="", help="上下文摘要")
    p_save.add_argument("--before", default="")
    p_save.add_argument("--after", default="")

    p_list = sub.add_parser("list", help="列出历史上下文")
    p_list.add_argument("--agent", required=True)

    args = parser.parse_args()
    if args.cmd == "save":
        return cmd_save(args)
    elif args.cmd == "list":
        return cmd_list(args)


if __name__ == "__main__":
    sys.exit(main())
