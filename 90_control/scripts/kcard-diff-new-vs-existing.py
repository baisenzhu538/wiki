#!/usr/bin/env python3
"""New card vs existing cards — automated contradiction detection.

Usage:
  python kcard-diff-new-vs-existing.py --new <card_id>          Compare one new card
  python kcard-diff-new-vs-existing.py --domain <domain> --recent 7  All new cards in domain

Finds: overlapping claims, conflicting definitions, boundary extensions, deepening insights.
"""

import argparse, json, re, sys
import sys
if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")
if hasattr(sys.stderr, "reconfigure"):
    sys.stderr.reconfigure(encoding="utf-8", errors="replace")
from pathlib import Path
from collections import defaultdict

ROOT = Path(__file__).resolve().parent.parent.parent
WIKI = ROOT / "30_wiki"
FEEDBACK = ROOT / "60_feedback" / "contradictions"

def load_card(path: Path) -> dict | None:
    try: content = path.read_text(encoding="utf-8")
    except: return None
    if not content.startswith("---"): return None
    end = content.find("---", 3)
    if end == -1: return None
    import yaml
    try: fm = yaml.safe_load(content[3:end])
    except: return None
    if not fm or not isinstance(fm, dict): return None
    body = content[end+3:]
    # Extract claims
    claims = re.findall(r'(?:claim|Claim|C\d+).*?(?:conf[=:]\s*([\d.]+))?[:\s]*(.*?)(?:\n|$)', body, re.IGNORECASE)
    return {
        "id": str(fm.get("id", path.stem)),
        "title": str(fm.get("title", "")),
        "type": str(fm.get("type", "")),
        "domain": fm.get("domain", []),
        "status": str(fm.get("status", "")),
        "confidence": fm.get("confidence"),
        "claims": [{"text": c[1].strip()[:120], "conf": float(c[0]) if c[0] else None} for c in claims[:10]],
        "key_terms": set(re.findall(r'(?:模型|框架|方法|原则|步骤|阶段|层|要素|维度|核心|关键)', body)) if any(kw in body for kw in ['模型','框架','方法']) else set(),
        "mtime": path.stat().st_mtime,
        "path": str(path.relative_to(WIKI)),
    }

def check_contradictions(new_card: dict, existing: list[dict]) -> list[dict]:
    """Compare new card claims against existing cards for conflicts."""
    findings = []
    new_claims = new_card.get("claims", [])
    if not new_claims:
        return [{"type": "NO_CLAIMS", "severity": "info", "detail": "新卡没有提取到可验证的 claims"}]

    new_domain = set(new_card.get("domain", []))
    new_terms = new_card.get("key_terms", set())
    new_title_words = set(new_card.get("title", "").lower().split())

    for old in existing:
        if old["id"] == new_card["id"]:
            continue
        old_domain = set(old.get("domain", []))
        old_title_words = set(old.get("title", "").lower().split())

        # Must share domain or title keyword overlap to be relevant
        domain_overlap = new_domain & old_domain if new_domain and old_domain else False
        title_overlap = len(new_title_words & old_title_words) >= 3
        if not domain_overlap and not title_overlap:
            continue

        # Compare claims
        for nc in new_claims:
            for oc in old.get("claims", []):
                n_text = nc.get("text", "")
                o_text = oc.get("text", "")
                if not n_text or not o_text:
                    continue

                # Simple overlap check
                n_words = set(n_text)
                o_words = set(o_text)
                overlap = len(n_words & o_words) / max(len(n_words | o_words), 1)

                if overlap > 0.6:
                    n_conf = nc.get("conf") or 0
                    o_conf = oc.get("conf") or 0

                    # Classify the conflict
                    if n_conf > o_conf + 0.2:
                        ctype = "深化型"
                        detail = f"新卡({n_conf})比旧卡({o_conf})置信度更高——可能是方法论更新"
                    elif o_conf > n_conf + 0.2:
                        ctype = "待验证"
                        detail = f"旧卡({o_conf})置信度高于新卡({n_conf})——需要交叉验证"
                    else:
                        ctype = "重叠型"
                        detail = f"两条 claims 置信度接近({n_conf} vs {o_conf})——可能存在冗余"

                    findings.append({
                        "type": ctype,
                        "severity": "warn" if ctype == "待验证" else "info",
                        "new_card": new_card["id"],
                        "new_claim": n_text[:80],
                        "old_card": old["id"],
                        "old_claim": o_text[:80],
                        "old_status": old["status"],
                        "overlap": round(overlap, 2),
                        "detail": detail,
                    })

    return findings


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--new", help="New card ID to check")
    parser.add_argument("--domain", help="Domain to scan for new cards")
    parser.add_argument("--recent", type=int, default=7, help="Days to look back for new cards")
    parser.add_argument("--json", action="store_true")
    args = parser.parse_args()

    # Load all existing cards
    all_cards = {}
    for f in WIKI.rglob("*.md"):
        if "raw" in f.parts or "_archive" in f.parts: continue
        if f.name in ("index.md","log.md"): continue
        card = load_card(f)
        if card: all_cards[card["id"]] = card

    if args.new:
        new_id = args.new
        if new_id not in all_cards:
            print(f"Card '{new_id}' not found.")
            return 1
        new_card = all_cards[new_id]
        existing = [c for cid, c in all_cards.items() if cid != new_id]
        findings = check_contradictions(new_card, existing)

        if args.json:
            print(json.dumps(findings, ensure_ascii=False, indent=2))
            return 0

        print(f"## 新卡: {new_card['title']} ({new_card['id']})")
        print(f"   Claims: {len(new_card['claims'])} | Domain: {new_card['domain']}")
        if not findings:
            print("   ✅ 未检测到与现有卡片的冲突")
        else:
            for f in findings:
                icon = {"深化型":"📈","待验证":"⚠️","重叠型":"🔄"}.get(f["type"],"❓")
                print(f"   {icon} [{f['type']}] {f['detail']}")
                print(f"      新: {f['new_claim']}")
                print(f"      旧: {f['old_claim']} (卡: {f['old_card']}, status: {f['old_status']})")

        # Write report
        FEEDBACK.mkdir(parents=True, exist_ok=True)
        from datetime import datetime
        ts = datetime.now().strftime("%Y%m%d_%H%M%S")
        out = FEEDBACK / f"new-card-check-{new_id}-{ts}.json"
        out.write_text(json.dumps(findings, ensure_ascii=False, indent=2), encoding="utf-8")

    else:
        print("Usage: --new <card_id> | --domain <domain> --recent N")
        return 1

    return 0

if __name__ == "__main__":
    main()
