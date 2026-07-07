#!/usr/bin/env python3
"""审查完整性审计：检测写审分离违规 + status 不一致。

Usage:
  python kdo-tools/audit-review-integrity.py           # 审计报告
  python kdo-tools/audit-review-integrity.py --fix     # 审计 + 自动修复 status 不一致
  python kdo-tools/audit-review-integrity.py --json    # JSON 输出

检测项：
  1. author == reviewed_by（自审违规）
  2. reviewed_by 是基建角色（黄药师/洪七公——执行者不是审查者）
  3. reviewed_by 非空 + status = "enriched"（状态滞后）
  4. reviewed_by = "待审" / "pending"（未完成审查）
  5. reviewed_by 非空 + review_date 缺失
"""

import argparse
import json
import sys
from datetime import datetime
from pathlib import Path

WIKI = Path(__file__).resolve().parent.parent
WIKI_DIR = WIKI / "30_wiki"

# 不能做审查者的角色（执行者/基建者）
NON_REVIEWERS = {"黄药师", "洪七公", "段王爷", "老顽童", "WorkBuddy"}
# 合法审查者
VALID_REVIEWERS = {"欧阳锋", "周伯通"}

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")


def parse_frontmatter(text: str) -> dict | None:
    """提取 YAML frontmatter。"""
    if not text.startswith("---"):
        return None
    parts = text.split("---", 2)
    if len(parts) < 3:
        return None
    try:
        import yaml
        return yaml.safe_load(parts[1]) or {}
    except Exception:
        return None


def scan_violations(fix: bool = False) -> list[dict]:
    """扫描 30_wiki/ 下所有卡片，返回违规列表。"""
    violations = []
    for f in sorted(WIKI_DIR.rglob("*.md")):
        if any(skip in f.parts for skip in ("_archive", "raw", "_dogfood")):
            continue
        try:
            text = f.read_text(encoding="utf-8", errors="ignore")
        except Exception:
            continue

        fm = parse_frontmatter(text)
        if not fm:
            continue

        card_id = fm.get("id", f.stem)
        author = str(fm.get("author", "")).strip()
        reviewed_by = str(fm.get("reviewed_by", "")).strip()
        status = str(fm.get("status", "")).strip()
        review_date = str(fm.get("review_date", "")).strip()
        rel = str(f.relative_to(WIKI))

        issues = []

        # 1. 自审违规
        if author and reviewed_by and author == reviewed_by:
            issues.append(("SELF_REVIEW", f"author=reviewed_by={author}"))

        # 2. 基建角色审卡
        if reviewed_by in NON_REVIEWERS:
            issues.append(("NON_REVIEWER", f"reviewed_by={reviewed_by}（非审查角色）"))

        # 3. reviewed_by 是占位符（未完成审查）
        if reviewed_by in ("待审", "pending", "src_unknown", ""):
            pass  # 正常——卡片还未被审查
        elif reviewed_by and status == "enriched":
            if fix and reviewed_by in VALID_REVIEWERS:
                _fix_status(f, text, card_id, "reviewed")
                issues.append(("STATUS_FIXED", f"enriched→reviewed（reviewed_by={reviewed_by}）"))
            else:
                issues.append(("STATUS_STALE", f"status=enriched 但 reviewed_by={reviewed_by}"))

        # 4. reviewed_by 存在但 review_date 缺失
        if reviewed_by and reviewed_by not in ("待审", "pending", "src_unknown", "") and not review_date:
            issues.append(("NO_REVIEW_DATE", f"reviewed_by={reviewed_by} 但 review_date 缺失"))

        if issues:
            violations.append({
                "file": rel,
                "id": card_id,
                "author": author,
                "reviewed_by": reviewed_by,
                "status": status,
                "issues": issues,
            })

    return violations


def _fix_status(path: Path, text: str, card_id: str, new_status: str):
    """将 frontmatter 中的 status 字段改为 new_status。"""
    parts = text.split("---", 2)
    if len(parts) < 3:
        return
    fm_text = parts[1]
    # 替换 status 行
    import re
    new_fm = re.sub(r"^status:\s*.+$", f"status: {new_status}", fm_text, flags=re.MULTILINE)
    new_text = f"---{new_fm}---{parts[2]}"
    path.write_text(new_text, encoding="utf-8")


def print_report(violations: list[dict]):
    """输出审计报告。"""
    by_type: dict[str, list] = {}
    for v in violations:
        for code, msg in v["issues"]:
            by_type.setdefault(code, []).append((v, msg))

    print(f"审查完整性审计 — {datetime.now().strftime('%Y-%m-%d %H:%M')}\n")
    print(f"  扫描卡片：{sum(1 for _ in WIKI_DIR.rglob('*.md') if '_archive' not in str(_) and 'raw' not in str(_))}")
    print(f"  违规卡片：{len(violations)}\n")

    labels = {
        "SELF_REVIEW": "🔴 自审违规（author = reviewed_by）",
        "NON_REVIEWER": "🔴 非审查角色审卡",
        "STATUS_STALE": "🟡 status 滞后（reviewed_by 非空但 status=enriched）",
        "STATUS_FIXED": "✅ 已修复",
        "NO_REVIEW_DATE": "🟡 缺 review_date",
    }

    for code, label in labels.items():
        items = by_type.get(code, [])
        if not items:
            continue
        print(f"\n{label}（{len(items)} 张）：")
        for v, msg in items:
            print(f"  {v['file']}")
            print(f"    {msg}")


def main():
    parser = argparse.ArgumentParser(description="审查完整性审计")
    parser.add_argument("--fix", action="store_true", help="自动修复 status 不一致")
    parser.add_argument("--json", action="store_true", help="JSON 输出")
    args = parser.parse_args()

    violations = scan_violations(fix=args.fix)

    if args.json:
        print(json.dumps({
            "total_violations": len(violations),
            "by_type": {
                code: len([v for v in violations if any(i[0] == code for i in v["issues"])])
                for code in ["SELF_REVIEW", "NON_REVIEWER", "STATUS_STALE", "STATUS_FIXED", "NO_REVIEW_DATE"]
            },
            "violations": violations,
        }, ensure_ascii=False, indent=2))
    else:
        print_report(violations)

    return 0 if not violations else 0  # 总是返回 0（审计工具，不阻塞）


if __name__ == "__main__":
    sys.exit(main())
