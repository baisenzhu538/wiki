#!/usr/bin/env python3
"""
Agent 每日上下文自动存储——形成可复用的数据包。

每天每个Agent的对话存到 agent复盘/<agent>/daily-context/YYYY-MM-DD.md
不用手动触发——Agent在会话结束前按飞轮协议自动执行本脚本。

Usage:
  python kdo-tools/daily-context-save.py --agent <id> --input <对话文件>
  python kdo-tools/daily-context-save.py --agent <id> --text "<一句话摘要>"
"""

import argparse
import shutil
import sys
from datetime import datetime, timezone
from pathlib import Path

WIKI = Path(__file__).resolve().parent.parent
REVIEW_DIR = Path.home() / "Desktop" / "agent复盘"

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")


def cmd_save(args):
    agent = args.agent
    today = datetime.now().strftime("%Y-%m-%d")
    dest_dir = REVIEW_DIR / agent / "daily-context"
    dest_dir.mkdir(parents=True, exist_ok=True)
    dest = dest_dir / f"{today}.md"

    content = []
    content.append(f"# {agent} · {today} 上下文\n")

    if args.input:
        src = Path(args.input)
        if src.exists():
            content.append(src.read_text(encoding="utf-8", errors="ignore"))
        else:
            content.append(f"(输入文件不存在: {src})")
    elif args.text:
        content.append(args.text)
    else:
        content.append("(无内容)")

    dest.write_text("\n".join(content), encoding="utf-8")
    print(f"已保存：{dest}")
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
    p_save.add_argument("--input", help="对话文件路径")
    p_save.add_argument("--text", help="一句话摘要")

    p_list = sub.add_parser("list", help="列出历史上下文")
    p_list.add_argument("--agent", required=True)

    args = parser.parse_args()
    if args.cmd == "save":
        return cmd_save(args)
    elif args.cmd == "list":
        return cmd_list(args)


if __name__ == "__main__":
    sys.exit(main())
