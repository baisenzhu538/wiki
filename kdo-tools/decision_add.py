#!/usr/bin/env python3
"""
kdo decision add — 决策记录模板化（#275 决策分类 + claim-state）

用法:
  python kdo-tools/decision_add.py add "标题" --type D1|D2|D3|D4 --claim observed|attested [--approver 王语嫣] [--dry-run]
  python kdo-tools/decision_add.py template            # 打印模板
"""
import argparse
import re
import sys
from datetime import date
from pathlib import Path

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")
if sys.platform == "win32":
    try:
        import ctypes
        ctypes.windll.kernel32.SetConsoleOutputCP(65001)
    except Exception:
        pass

WIKI = Path(__file__).resolve().parent.parent
DECISIONS = WIKI / ".agent" / "decisions.md"

TYPES = {"D1": "操作", "D2": "战术", "D3": "战略", "D4": "自我修改"}
CLAIMS = {"observed": "实证观察", "attested": "已核实声明"}
APPROVERS = ("王语嫣", "欧阳锋")


def _entry(title: str, dtype: str, claim: str, approver: str, body: str = "") -> str:
    today = date.today().isoformat()
    type_desc = f"D{dtype[1]} {TYPES[dtype]}"
    claim_desc = f"{claim}（{CLAIMS[claim]}）"
    approver_line = f"\n**批准人**：{approver}" if dtype == "D4" else ""
    if dtype == "D4" and not approver:
        raise ValueError("D4 决策必须指定批准人（王语嫣/欧阳锋）")
    return f"""---

## {today}：{title}

**类型**：{type_desc} / **claim-state**：{claim_desc}{approver_line}

**背景**：
{body or '（待填）'}

**决策**：
（待填）

**原因**：
（待填）

**否决的替代方案**：
（待填）

**后果**：
（待填）
"""


def cmd_add(args) -> int:
    try:
        entry = _entry(args.title, args.type, args.claim, args.approver or "", args.body or "")
    except ValueError as e:
        print(f"Error: {e}", file=sys.stderr)
        return 1
    if args.dry_run:
        print(f"[dry-run] 将追加到 {DECISIONS.name}:\n{entry}")
        return 0
    # 追加到文件末尾（保留已有内容）
    with DECISIONS.open("a", encoding="utf-8") as f:
        f.write(entry)
    # 校验：回读确认写入
    text = DECISIONS.read_text(encoding="utf-8")
    if title_marker(text, args.title):
        print(f"✅ 已追加决策：{args.title}（{args.type} / {args.claim}）")
        print(f"   位置：{DECISIONS}")
        return 0
    print("🔴 写入校验失败", file=sys.stderr)
    return 1


def title_marker(text: str, title: str) -> bool:
    return title in text


def main():
    p = argparse.ArgumentParser(description="kdo decision add — 决策记录模板化（#275）")
    sub = p.add_subparsers(dest="cmd")
    sub.add_parser("template", help="打印决策模板")
    a = sub.add_parser("add", help="追加决策条目")
    a.add_argument("title", help="决策标题")
    a.add_argument("--type", required=True, choices=["D1", "D2", "D3", "D4"], help="决策类型（D4=自我修改必须批准人）")
    a.add_argument("--claim", required=True, choices=["observed", "attested"], help="claim-state")
    a.add_argument("--approver", choices=list(APPROVERS), help="D4 必填：批准人")
    a.add_argument("--body", help="背景内容（可选）")
    a.add_argument("--dry-run", action="store_true", help="只预览不写入")
    args = p.parse_args()
    if args.cmd == "template":
        print(_entry("示例决策", "D2", "observed", ""))
        return 0
    if args.cmd == "add":
        return cmd_add(args)
    p.print_help()
    return 0


if __name__ == "__main__":
    sys.exit(main())
