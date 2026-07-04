#!/usr/bin/env python3
"""
扫描口述稿中的 Truman 操作演示段落。

Truman 说以下信号词时，通常是在摊开自己的操作过程——最高优先级标注：
  "我给你演示一下" "举个例子" "这是我真实的" "我给你们看一个"
  "你们感受一下" "准备好，惊喜来了" "来，我现场给你"
  "我给你看一个" "试一下啊" "你们试试"
  "这个建议是最近我用的特别开心的" "注意，所有你们未来"

Usage:
  python kdo-tools/scan-demo-sections.py <口述稿路径>
  python kdo-tools/scan-demo-sections.py --all   # 扫描 inbox 所有口述稿
"""

import argparse
import re
import sys
from pathlib import Path

WIKI = Path(__file__).resolve().parent.parent

SIGNAL_WORDS = [
    "我给你演示一下", "举个例子", "这是我真实的", "我给你们看一个",
    "你们感受一下", "准备好，惊喜来了", "来，我现场给你",
    "我给你看一个", "试一下啊", "你们试试",
    "这个建议是最近我用的特别开心的", "注意，所有你们未来",
    "我稍微解释一下", "我先不说过程", "直接说结果",
    "这个时候", "后来一次意外", "转折出现了",
]

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")


def scan_file(path: Path) -> list[dict]:
    """Scan a transcript for demo paragraphs. Returns list of {line, context, signal}."""
    text = path.read_text(encoding="utf-8", errors="ignore")
    lines = text.split("\n")
    results = []

    for i, line in enumerate(lines):
        for signal in SIGNAL_WORDS:
            if signal in line:
                # Extract surrounding context (5 lines before, 3 after)
                start = max(0, i - 5)
                end = min(len(lines), i + 4)
                context = "\n".join(lines[start:end])
                results.append({
                    "line": i + 1,
                    "signal": signal,
                    "trigger": line.strip()[:120],
                    "context": context[:500],
                })
                break  # one signal per line

    return results


def scan_all():
    """Scan all oral transcripts in inbox."""
    inbox = WIKI / "00_inbox"
    total = 0
    for pattern in ["*口述*.txt", "*口述*.md", "*逐字稿*"]:
        for f in inbox.rglob(pattern):
            results = scan_file(f)
            if results:
                print(f"\n{'='*60}")
                print(f"📄 {f.relative_to(WIKI)} — {len(results)} 处操作演示")
                print(f"{'='*60}")
                for r in results:
                    print(f"\n  L{r['line']} 🔴 {r['signal']}")
                    print(f"  {r['trigger']}")
                total += len(results)

    print(f"\n{'='*60}")
    print(f"总计: {total} 处操作演示段落")
    return total


def main():
    parser = argparse.ArgumentParser(description="扫描口述稿中的 Truman 操作演示段落")
    parser.add_argument("path", nargs="?", help="口述稿路径")
    parser.add_argument("--all", action="store_true", help="扫描 inbox 所有口述稿")
    args = parser.parse_args()

    if args.all:
        scan_all()
    elif args.path:
        p = Path(args.path)
        if not p.exists():
            print(f"File not found: {p}", file=sys.stderr)
            return 1
        results = scan_file(p)
        print(f"{p}: {len(results)} 处操作演示段落")
        for r in results:
            print(f"\n  L{r['line']} 🔴 {r['signal']}")
            print(f"  {r['trigger']}")
    else:
        parser.print_help()

    return 0


if __name__ == "__main__":
    sys.exit(main())
