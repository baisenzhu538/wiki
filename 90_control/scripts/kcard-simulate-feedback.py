#!/usr/bin/env python3
"""Card usage simulator — AI扮演用户，拿真实问题测试卡片可用性。

对标王欢"双角色对练"方法论：一个AI扮演用户提出问题，另一个AI读卡并诊断，
然后评判这张卡是否真的帮到了"用户"。

Usage:
  python kcard-simulate-feedback.py --card <id>           Test single card
  python kcard-simulate-feedback.py --domain <domain>      Test random cards in domain
  python kcard-simulate-feedback.py --batch 5              Test 5 random enriched cards
"""

import argparse, json, random, re, sys
from pathlib import Path
from collections import defaultdict

ROOT = Path(__file__).resolve().parent.parent.parent
WIKI = ROOT / "30_wiki"
FEEDBACK_DIR = ROOT / "60_feedback" / "simulated"


def load_card(filepath: Path) -> dict | None:
    """Load card frontmatter and body."""
    try:
        content = filepath.read_text(encoding="utf-8")
    except:
        return None
    if not content.startswith("---"):
        return None
    end = content.find("---", 3)
    if end == -1:
        return None
    import yaml
    try:
        fm = yaml.safe_load(content[3:end])
    except:
        return None
    if not fm or not isinstance(fm, dict):
        return None
    return {
        "id": str(fm.get("id", filepath.stem)),
        "title": str(fm.get("title", "")),
        "type": str(fm.get("type", "")),
        "domain": fm.get("domain", []),
        "status": str(fm.get("status", "")),
        "confidence": fm.get("confidence"),
        "signals": fm.get("diagnostic_signals", []),
        "body": content[end+3:],
        "path": str(filepath.relative_to(ROOT)),
    }


def simulate_user_question(card: dict) -> str:
    """Generate a realistic user question based on the card's signals."""
    signals = card.get("signals", [])
    if signals and isinstance(signals, list) and len(signals) > 0:
        s = signals[0]
        if isinstance(s, dict):
            return s.get("signal", f"我遇到了{card['title']}相关的问题")
        return str(s)
    # Fallback: generate from title
    return f"你能帮我理解{card['title']}吗？我遇到了相关问题。"


def check_card_usability(card: dict) -> dict:
    """Simulate: can an AI agent use this card to help a user?"""
    issues = []
    score = 10

    # 1. Can we identify the problem this card solves?
    if not card.get("title"):
        issues.append("MISSING_TITLE")
        score -= 3
    else:
        score += 0

    # 2. Does it have diagnostic signals to match user problems?
    signals = card.get("signals", [])
    if not signals or signals == []:
        issues.append("NO_DIAGNOSTIC_SIGNALS")
        score -= 2
    else:
        score += 1

    # 3. Is there actionable content (not just descriptions)?
    body = card.get("body", "")
    has_action = bool(re.search(r"(?:操作|步骤|方法|流程|动作|执行|使用|操作)", body))
    has_checklist = bool(re.search(r"(?:清单|checklist|检查|自查)", body, re.IGNORECASE))
    has_example = bool(re.search(r"(?:案例|Case|例如|比如|Example)", body, re.IGNORECASE))
    if not has_action:
        issues.append("NO_ACTIONABLE_CONTENT")
        score -= 2
    if has_action and has_checklist:
        score += 1
    if has_example:
        score += 1

    # 4. Are there boundary conditions (when NOT to use)?
    has_boundary = bool(re.search(r"(?:不要用|不适用|边界|失效|不适用|反例)", body))
    if not has_boundary:
        issues.append("NO_BOUNDARY_CONDITIONS")
        score -= 1

    # 5. Can an agent extract structured steps?
    has_structured = bool(re.search(r"(?:## |### |\|.*\|.*\|)", body))
    if not has_structured:
        issues.append("NO_STRUCTURED_CONTENT")
        score -= 1

    # 6. Does it link to other cards for deeper dive?
    wikilinks = re.findall(r"\[\[([^\]]+)\]\]", body)
    if len(wikilinks) < 2:
        issues.append("FEW_WIKILINKS")
        score -= 1
    elif len(wikilinks) >= 5:
        score += 1

    # Grade
    if score >= 10:
        grade = "A_USABLE"
    elif score >= 7:
        grade = "B_PARTIAL"
    elif score >= 4:
        grade = "C_NEEDS_WORK"
    else:
        grade = "D_BROKEN"

    return {
        "score": max(0, min(10, score)),
        "grade": grade,
        "issues": issues,
        "simulated_question": simulate_user_question(card),
        "actionable": has_action,
        "has_boundary": has_boundary,
        "wikilink_count": len(wikilinks),
    }


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--card", help="Test single card by ID")
    parser.add_argument("--domain", help="Test random cards in domain")
    parser.add_argument("--batch", type=int, default=0, help="Test N random enriched cards")
    parser.add_argument("--json", action="store_true")
    args = parser.parse_args()

    # Find cards to test
    candidates = []
    for f in WIKI.rglob("*.md"):
        if "raw" in f.parts or "_archive" in f.parts:
            continue
        if f.name in ("index.md", "log.md", "contradictions.md"):
            continue
        card = load_card(f)
        if not card:
            continue
        if args.card and card["id"] == args.card:
            candidates = [card]
            break
        if args.domain:
            domain_list = card.get("domain", [])
            if isinstance(domain_list, list) and args.domain in domain_list:
                candidates.append(card)
        elif card["status"] in ("enriched", "reviewed", "stable"):
            candidates.append(card)

    if not candidates:
        print("No cards found.")
        return 1

    if args.batch and args.batch > 0:
        candidates = random.sample(candidates, min(args.batch, len(candidates)))

    results = []
    for card in candidates:
        r = check_card_usability(card)
        r["id"] = card["id"]
        r["title"] = card["title"]
        r["type"] = card["type"]
        r["status"] = card["status"]
        results.append(r)

    if args.json:
        print(json.dumps(results, ensure_ascii=False, indent=2))
        return 0

    # Summary
    grades = defaultdict(int)
    for r in results:
        grades[r["grade"]] += 1
    print(f"Cards tested: {len(results)}")
    for g in ["A_USABLE", "B_PARTIAL", "C_NEEDS_WORK", "D_BROKEN"]:
        if g in grades:
            pct = grades[g] / len(results) * 100
            icon = {"A_USABLE": "✅", "B_PARTIAL": "⚠️", "C_NEEDS_WORK": "🔧", "D_BROKEN": "❌"}[g]
            print(f"  {icon} {g}: {grades[g]} ({pct:.1f}%)")

    # Show worst cards
    worst = [r for r in results if r["grade"] in ("C_NEEDS_WORK", "D_BROKEN")]
    if worst:
        print(f"\n## Needs work ({len(worst)} cards):")
        for r in sorted(worst, key=lambda x: x["score"]):
            print(f"  [{r['grade']}] {r['id']}: score={r['score']} issues={r['issues']}")
            print(f"       simulated Q: {r['simulated_question'][:80]}")

    # Write feedback
    FEEDBACK_DIR.mkdir(parents=True, exist_ok=True)
    from datetime import datetime
    ts = datetime.now().strftime("%Y%m%d_%H%M%S")
    report_path = FEEDBACK_DIR / f"simulated-feedback-{ts}.json"
    report_path.write_text(json.dumps(results, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"\nFeedback saved: {report_path.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
