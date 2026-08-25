#!/usr/bin/env python3
"""tech_inventory.py — 技术域存量盘点脚本（#533）：接管既有技术库第一步。

扫描目标库 .md 产出，按形态出三堆清单：
  可审：frontmatter 齐（title/type/status/created_at）+ 有来源标注（source_refs 非空非 src_unknown）
  返工：有 frontmatter 但缺字段 / 来源标注缺失或 src_unknown / 正文疑似占位
  废弃：无 frontmatter 且正文极短（<100 字）/ 纯占位空壳——接管时不值得救

用法：
  python kdo-tools/tech_inventory.py --root <目标库>            # 盘点打印
  python kdo-tools/tech_inventory.py --root <目标库> --json OUT # 机读清单落盘
"""
import argparse
import json
import re
import sys
from pathlib import Path

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")

REQUIRED_FM = ["title", "type", "status", "created_at"]
PLACEHOLDER_MARKERS = ["src_unknown", "TODO", "待补充", "待回填"]


def _split_fm(text: str) -> tuple[dict, str]:
    if not text.startswith("---\n"):
        return {}, text
    end = text.find("\n---\n", 4)
    if end == -1:
        return {}, text
    try:
        import yaml
        fm = yaml.safe_load(text[4:end])
        return (fm if isinstance(fm, dict) else {}), text[end + 5:]
    except Exception:
        return {}, text[end + 5:]


def classify_file(fp: Path, root: Path) -> tuple[str, str]:
    """返回 (pile, reason)。pile ∈ 可审/返工/废弃。"""
    try:
        text = fp.read_text(encoding="utf-8", errors="replace")
    except OSError as e:
        return "废弃", f"不可读: {e}"
    fm, body = _split_fm(text.replace("\r\n", "\n"))
    body_len = len(body.strip())

    if not fm:
        if body_len < 100:
            return "废弃", "无 frontmatter 且正文极短（空壳）"
        return "返工", "无 frontmatter（需补卡头）"
    missing = [k for k in REQUIRED_FM if not fm.get(k)]
    if missing:
        return "返工", f"frontmatter 缺字段: {','.join(missing)}"
    src = fm.get("source_refs")
    src_empty = (not src) or (isinstance(src, list) and all("src_unknown" in str(s) for s in src))
    if src_empty or (isinstance(src, str) and "src_unknown" in src):
        return "返工", "来源标注缺失/src_unknown（疑似无源规格）"
    if any(m in body for m in PLACEHOLDER_MARKERS):
        return "返工", "正文疑似占位（占位词命中）"
    return "可审", "frontmatter 齐+来源在位"


def inventory(root: Path) -> dict:
    piles: dict[str, list[dict]] = {"可审": [], "返工": [], "废弃": []}
    for fp in sorted(root.rglob("*.md")):
        if any(p.startswith(("_", ".")) for p in fp.relative_to(root).parts):
            continue
        pile, reason = classify_file(fp, root)
        piles[pile].append({"path": fp.relative_to(root).as_posix(), "reason": reason})
    return piles


def main() -> int:
    ap = argparse.ArgumentParser(description="技术域存量盘点三堆清单（#533）")
    ap.add_argument("--root", required=True, help="目标库目录")
    ap.add_argument("--json", dest="json_out", help="机读清单落盘路径")
    args = ap.parse_args()

    root = Path(args.root)
    if not root.is_dir():
        print(f"目录不存在: {root}")
        return 1
    piles = inventory(root)
    for pile in ("可审", "返工", "废弃"):
        print(f"{pile}: {len(piles[pile])} 件")
        for item in piles[pile][:5]:
            print(f"  - {item['path']}（{item['reason']}）")
        if len(piles[pile]) > 5:
            print(f"  … 等 {len(piles[pile])} 件")
    if args.json_out:
        Path(args.json_out).write_text(json.dumps(piles, ensure_ascii=False, indent=2), encoding="utf-8")
        print(f"📄 清单落盘: {args.json_out}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
