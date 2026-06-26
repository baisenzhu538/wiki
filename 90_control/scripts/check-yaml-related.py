"""
Batch check YAML frontmatter and related links across all wiki cards.

Usage:
    python check-yaml-related.py                  # Full report
    python check-yaml-related.py --domain <name>  # Single domain
    python check-yaml-related.py --broken-only    # Only show broken links
    python check-yaml-related.py --json           # JSON output
"""
import argparse, json, re, sys
from pathlib import Path
from collections import Counter, defaultdict

WIKI = Path(r"C:\Users\Administrator\Desktop\wiki\30_wiki")
IGNORE = ["_archive", "index.md", "log.md"]

def safe_read(f):
    for enc in ['utf-8', 'gbk', 'latin-1']:
        try: return f.read_text(encoding=enc)
        except: pass
    return None

def parse_frontmatter(text):
    if not text.startswith("---"): return {}, text
    end = text.find("---", 3)
    if end == -1: return {}, text
    fm, body = {}, text[3:end]
    for line in body.split("\n"):
        if ":" in line:
            k, _, v = line.partition(":")
            k, v = k.strip(), v.strip().strip('"').strip("'")
            if v.startswith("[") and v.endswith("]"):
                fm[k] = [it.strip().strip('"').strip("'") for it in v[1:-1].split(",") if it.strip()]
            else:
                fm[k] = v
    for lk in ["related", "domain", "source_refs", "tags"]:
        if lk in fm and (fm[lk] == [] or fm[lk] == ""):
            pat = re.compile(rf"^{lk}:\n((?:\s+-.+\n?)*)", re.MULTILINE)
            m = pat.search(body)
            if m:
                items = re.findall(r"^\s*-\s+(.+)$", m.group(1), re.MULTILINE)
                fm[lk] = [it.strip().strip('"').strip("'") for it in items]
    return fm, text[end+3:]

def get_related_ids(fm):
    rel = fm.get("related", [])
    if isinstance(rel, str): rel = [rel] if rel else []
    ids = set()
    for r in rel:
        r = r.strip()
        if not r: continue
        m = re.search(r'\[\[([^\]|]+)', r)
        ids.add(m.group(1).strip() if m else r)
    return ids

def main():
    p = argparse.ArgumentParser()
    p.add_argument("--domain")
    p.add_argument("--broken-only", action="store_true")
    p.add_argument("--json", action="store_true")
    args = p.parse_args()

    # Build ID -> path index
    all_ids = {}
    all_cards = []
    for f in sorted(WIKI.rglob("*.md")):
        if any(p in str(f) for p in IGNORE): continue
        text = safe_read(f)
        if not text: continue
        fm, _ = parse_frontmatter(text)
        if "id" not in fm: continue
        all_ids[fm["id"]] = str(f.relative_to(WIKI))
        all_cards.append({"id": fm["id"], "path": str(f.relative_to(WIKI)), "fm": fm, "file": f})

    if args.domain:
        all_cards = [c for c in all_cards
                     if args.domain in str(c.get("fm", {}).get("domain", ""))]

    # Check each card
    yaml_errors = []
    broken_links = []
    low_related = []
    missing_fields = defaultdict(list)

    for card in all_cards:
        cid = card["id"]
        fm = card["fm"]

        # YAML parse check (if we got here, it parsed)
        # Required fields
        for field in ["title", "type", "status", "author"]:
            if field not in fm or not fm[field]:
                missing_fields[field].append(cid)

        # Related count
        rel_count = len(get_related_ids(fm))
        if rel_count < 3:
            low_related.append((cid, rel_count, card["path"]))

        # Broken related links
        for rid in get_related_ids(fm):
            if rid not in all_ids:
                broken_links.append((cid, rid, card["path"]))

    # Output
    if args.json:
        result = {
            "total": len(all_cards),
            "yaml_errors": len(yaml_errors),
            "broken_links": len(broken_links),
            "low_related": len(low_related),
            "missing_fields": {k: len(v) for k, v in missing_fields.items()},
            "broken_link_detail": [{"card": c, "broken_id": b, "path": p} for c, b, p in broken_links[:50]],
        }
        print(json.dumps(result, ensure_ascii=False, indent=2))
        return

    print(f"Cards checked: {len(all_cards)}")

    if missing_fields:
        print(f"\n--- Missing Fields ---")
        for field, cards in sorted(missing_fields.items()):
            print(f"  {field}: {len(cards)} cards")
            if not args.broken_only:
                for c in cards[:5]:
                    print(f"    - {c}")
                if len(cards) > 5: print(f"    ... and {len(cards)-5} more")

    if low_related and not args.broken_only:
        print(f"\n--- Low Related (<3) ---")
        for cid, cnt, path in sorted(low_related, key=lambda x: x[1])[:20]:
            print(f"  [{cnt}] {cid}  ({path})")

    if broken_links:
        print(f"\n--- Broken Related Links ({len(broken_links)}) ---")
        for cid, bid, path in broken_links[:30]:
            print(f"  {cid} -> [[{bid}]]  (target not found)")
        if len(broken_links) > 30:
            print(f"  ... and {len(broken_links)-30} more")

    print(f"\nSummary: {len(all_cards)} cards, "
          f"{len(broken_links)} broken links, "
          f"{len(low_related)} low-related, "
          f"{sum(len(v) for v in missing_fields.values())} missing fields")

if __name__ == "__main__":
    main()
