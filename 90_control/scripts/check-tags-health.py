#!/usr/bin/env python3
"""check-tags-health.py — 标签健康检查（#474 任务 2，挂 health-check 第 8 项）。

四指标（健康线见 #474 任务 2）：
  脏词率 (STRONG+PATTERN 负向 + 课程名/来源混入) / 总卡数          <5%
  来源轴覆盖率 有来源词卡 / 有来源字段卡                          >90%
  有轴域覆盖率 词池轴域卡 / 总卡数（随域轴建设提升，仅报告不硬卡）
  空值率 tags 缺失/空/格式异常卡数 / 总卡数                       <3%

退出码：0=PASS（全达标）；1=FAIL（有超线项）；2=tags-audit 加载失败（降级告警）
用法：python 90_control/scripts/check-tags-health.py [--json]
"""

from __future__ import annotations

import argparse
import importlib.util
import json
import sys
from pathlib import Path

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")

KDO_TOOLS = Path(__file__).resolve().parent.parent.parent / "kdo-tools"
WIKI_ROOT = Path(__file__).resolve().parent.parent.parent

LINES = {
    "dirty_rate": 5.0,       # %
    "source_coverage": 90.0,  # %
    "empty_rate": 3.0,       # %
}


def load_audit():
    spec = importlib.util.spec_from_file_location("tags_audit", KDO_TOOLS / "tags-audit.py")
    ta = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(ta)
    return ta


def main() -> int:
    ap = argparse.ArgumentParser(description="标签健康检查（#474）")
    ap.add_argument("--json", action="store_true")
    args = ap.parse_args()

    try:
        ta = load_audit()
        cards = ta.scan_cards()
        r = ta.audit(cards)
    except Exception as e:
        if args.json:
            print(json.dumps({"error": str(e)}, ensure_ascii=False))
        else:
            print(f"⚠️ [WARN] 标签健康检查加载失败（降级不阻断）: {e}")
        return 2

    total = r["total"] or 1
    dirty_rate = (len(r["dirty"]) + len(r["dirty_course"])) / total * 100
    has_source = len(r["source_missing"])
    # 有来源字段卡数：source_missing 只是"有来源字段但缺来源词"的子集——补算分母
    src_field_cards = 0
    for fp, fm in cards:
        if fm.get("source_person") or fm.get("source_context"):
            src_field_cards += 1
    source_coverage = (src_field_cards - has_source) / src_field_cards * 100 if src_field_cards else 100.0
    empty_rate = len(r["empty_bad"]) / total * 100
    axis_cards = sum(n for d, n in r["domain_counts"].items() if d in ta.AXIS_DOMAINS)
    axis_coverage = axis_cards / total * 100

    fails = []
    if dirty_rate >= LINES["dirty_rate"]:
        fails.append(f"脏词率 {dirty_rate:.1f}% ≥ {LINES['dirty_rate']}%")
    if source_coverage < LINES["source_coverage"]:
        fails.append(f"来源轴覆盖率 {source_coverage:.1f}% < {LINES['source_coverage']}%")
    if empty_rate >= LINES["empty_rate"]:
        fails.append(f"空值率 {empty_rate:.1f}% ≥ {LINES['empty_rate']}%")

    metrics = {
        "dirty_rate": round(dirty_rate, 1),
        "dirty_cards": len(r["dirty"]) + len(r["dirty_course"]),
        "source_coverage": round(source_coverage, 1),
        "source_missing": len(r["source_missing"]),
        "axis_coverage": round(axis_coverage, 1),
        "axis_cards": axis_cards,
        "empty_rate": round(empty_rate, 1),
        "empty_cards": len(r["empty_bad"]),
        "total_cards": total,
        "status": "FAIL" if fails else "PASS",
    }
    if args.json:
        print(json.dumps(metrics, ensure_ascii=False, indent=2))
        return 1 if fails else 0

    print(f"标签健康（#474）：总卡 {total} | 脏词率 {dirty_rate:.1f}%（线 {LINES['dirty_rate']}%）"
          f"| 来源轴覆盖率 {source_coverage:.1f}%（线 {LINES['source_coverage']}%）"
          f"| 有轴域覆盖率 {axis_coverage:.1f}%（随建设）| 空值率 {empty_rate:.1f}%（线 {LINES['empty_rate']}%）")
    if fails:
        print("[FAIL] " + "；".join(fails))
        return 1
    print("[PASS] 标签健康全达标")
    return 0


if __name__ == "__main__":
    sys.exit(main())
