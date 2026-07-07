#!/usr/bin/env python3
"""批量修复 reviewed_by: 欧阳锋 + status: enriched → status: reviewed。

Usage:
  python kdo-tools/fix-review-status.py           # dry-run，只报告不修改
  python kdo-tools/fix-review-status.py --apply   # 执行修改
"""

import re
import sys
from pathlib import Path

WIKI = Path(__file__).resolve().parent.parent
WIKI_DIR = WIKI / "30_wiki"

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")


def scan_and_fix(apply_fix: bool = False) -> list[dict]:
    """扫描并修复 reviewed_by: 欧阳锋 + status: enriched 的卡片。"""
    results = []
    for f in sorted(WIKI_DIR.rglob("*.md")):
        if any(skip in f.parts for skip in ("_archive", "raw", "_dogfood")):
            continue
        try:
            text = f.read_text(encoding="utf-8", errors="ignore")
        except Exception:
            continue
        if not text.startswith("---"):
            continue
        parts = text.split("---", 2)
        if len(parts) < 3:
            continue
        fm_text = parts[1]

        # 用正则直接匹配，避免 YAML 解析边缘情况
        status_match = re.search(r"^status:\s*(.+)$", fm_text, re.MULTILINE)
        reviewed_match = re.search(r"^reviewed_by:\s*(.+)$", fm_text, re.MULTILINE)

        if not status_match or not reviewed_match:
            continue

        status_val = status_match.group(1).strip()
        reviewed_val = reviewed_match.group(1).strip()

        # 只处理：reviewed_by 是欧阳锋 且 status 是 enriched
        if reviewed_val != "欧阳锋":
            continue
        if status_val != "enriched":
            continue

        rel = str(f.relative_to(WIKI))
        if apply_fix:
            new_fm = re.sub(
                r"^status:\s*.+$",
                "status: reviewed",
                fm_text,
                flags=re.MULTILINE,
            )
            new_text = f"---{new_fm}---{parts[2]}"
            f.write_text(new_text, encoding="utf-8")
            results.append({"file": rel, "action": "FIXED"})
        else:
            results.append({"file": rel, "action": "DRY_RUN"})

    return results


def main():
    apply_fix = "--apply" in sys.argv
    results = scan_and_fix(apply_fix)

    action = "✅ 已修复" if apply_fix else "🔍 DRY-RUN（未修改）"
    print(f"{action}：{len(results)} 张卡片")
    print(f"  reviewed_by: 欧阳锋 + status: enriched → status: reviewed\n")

    if not apply_fix and results:
        print("前 15 张：")
        for r in results[:15]:
            print(f"  {r['file']}")
        if len(results) > 15:
            print(f"  ... 还有 {len(results) - 15} 张")
        print(f"\n确认无误后执行：python kdo-tools/fix-review-status.py --apply")

    return 0


if __name__ == "__main__":
    sys.exit(main())
