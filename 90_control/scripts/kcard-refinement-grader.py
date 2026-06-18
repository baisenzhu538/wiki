#!/usr/bin/env python3
"""Refinement depth grader: classify cards as format-only vs content-deep refinement.

Usage:
  python kcard-refinement-grader.py                    # Grade all cards
  python kcard-refinement-grader.py --card <id>        # Grade single card
  python kcard-refinement-grader.py --recent 7         # Last N days modified
"""

import argparse, json, re, yaml, sys
from pathlib import Path
from datetime import datetime, timezone, timedelta

ROOT = Path(__file__).resolve().parent.parent.parent
WIKI = ROOT / "30_wiki"
DIRS = ["concepts","frameworks","tools","cases","dark-knowledges","entities"]

# Depth signals: content refinement indicators
DEPTH_PATTERNS = [
    (r"\d+[%％]\s*(?:vs|对比|基准|benchmark)", 2, "data_comparison"),
    (r"(?:进入标准|Entry Criteria|适用条件|触发条件)", 2, "entry_criteria"),
    (r"(?:操作步骤|Protocol|Procedure|执行步骤|操作方法)", 2, "protocol"),
    (r"(?:失败模式|常见误区|反模式|不要用)", 2, "failure_modes"),
    (r"(?:案例|Case|真实.*例)", 2, "case_content"),
    (r"(?:检查清单|checklist|Checklist|自查)", 2, "checklist"),
    (r"(?:可迁移|跨域|跨场景|通用化)", 2, "transferable"),
    (r"(?:Burn line|核心洞察|一句话定义)", 1, "burn_line"),
    (r"(?:##\s*Critique|##\s*Constraints|##\s*Open Questions)", 1, "critique_section"),
    (r"(?:攻击者|Scholar|学者.*质疑|外部.*视角)", 2, "external_attacks"),
]

def grade_card(filepath: Path) -> dict:
    """Return refinement grade for a single card."""
    try:
        content = filepath.read_text(encoding="utf-8")
    except:
        return {"grade": "ERROR", "score": 0, "signals": []}

    if not content.startswith("---"):
        return {"grade": "SKIP", "score": 0, "signals": ["no_frontmatter"]}

    end = content.find("---", 3)
    if end == -1:
        return {"grade": "SKIP", "score": 0, "signals": ["bad_frontmatter"]}

    try:
        fm = yaml.safe_load(content[3:end])
    except:
        return {"grade": "SKIP", "score": 0, "signals": ["yaml_error"]}

    if not fm or not isinstance(fm, dict):
        return {"grade": "SKIP", "score": 0, "signals": ["empty_fm"]}

    status = str(fm.get("status", "")).strip().lower()
    body = content[end+3:]
    title = str(fm.get("title", ""))
    cid = str(fm.get("id", filepath.stem))

    # Format check: basic metadata completeness
    format_ok = all([
        fm.get("confidence") is not None,
        fm.get("trust_level") is not None,
        fm.get("diagnostic_signals") not in (None, [], ""),
        fm.get("source_refs") not in (None, [], ""),
    ])

    # Depth check: content refinement signals
    signals = []
    score = 0
    for pattern, weight, label in DEPTH_PATTERNS:
        if re.search(pattern, body, re.IGNORECASE):
            signals.append(label)
            score += weight

    # Classification
    if not format_ok:
        grade = "UNREFINED"
    elif score >= 6:
        grade = "A_CONTENT_DEEP"
    elif score >= 3:
        grade = "B_CONTENT_MODERATE"
    elif format_ok:
        grade = "C_FORMAT_ONLY"
    else:
        grade = "UNREFINED"

    return {
        "id": cid,
        "title": title[:80],
        "status": status,
        "grade": grade,
        "score": score,
        "signals": signals,
        "format_ok": format_ok,
    }


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--card", help="Grade single card by ID")
    parser.add_argument("--recent", type=int, help="Only cards modified in last N days")
    parser.add_argument("--json", action="store_true", help="JSON output")
    args = parser.parse_args()

    results = []
    cutoff = None
    if args.recent:
        cutoff = (datetime.now(timezone.utc) - timedelta(days=args.recent)).timestamp()

    for sub in DIRS:
        d = WIKI / sub
        if not d.is_dir(): continue
        for f in sorted(d.glob("*.md")):
            if f.name in ("index.md","log.md","contradictions.md"): continue
            if args.card and f.stem != args.card: continue
            if cutoff:
                try:
                    if f.stat().st_mtime < cutoff: continue
                except: continue
            r = grade_card(f)
            results.append(r)

    if args.json:
        print(json.dumps(results, ensure_ascii=False, indent=2))
        return

    # Summary
    counts = {}
    for r in results:
        g = r["grade"]
        counts[g] = counts.get(g, 0) + 1

    print(f"Cards graded: {len(results)}")
    for g in ["A_CONTENT_DEEP", "B_CONTENT_MODERATE", "C_FORMAT_ONLY", "UNREFINED", "SKIP"]:
        if g in counts:
            pct = counts[g] / len(results) * 100
            print(f"  {g}: {counts[g]} ({pct:.1f}%)")

    # Show C_FORMAT_ONLY cards (format only — these are the ones needing content upgrade)
    c_only = [r for r in results if r["grade"] == "C_FORMAT_ONLY"]
    if c_only:
        print(f"\n## Format-only cards ({len(c_only)} — metadata OK, content thin):")
        for r in sorted(c_only, key=lambda x: -x["score"])[:15]:
            print(f"  [{r['status']}] {r['id']}: {r['title'][:60]} (signals:{r['signals']})")
        if len(c_only) > 15:
            print(f"  ... and {len(c_only)-15} more")


if __name__ == "__main__":
    main()
