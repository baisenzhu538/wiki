import yaml
from pathlib import Path
from collections import Counter

wiki = Path("30_wiki")
empty_related = []
src_unknown_related = []
pending_unknown_related = []
real_related_count = Counter()

for p in wiki.rglob("*.md"):
    if "_archive" in str(p):
        continue
    try:
        text = p.read_text(encoding="utf-8", errors="ignore")
    except:
        continue
    if not text.startswith("---"):
        continue
    parts = text.split("---", 2)
    if len(parts) < 3:
        continue
    try:
        fm = yaml.safe_load(parts[1])
    except:
        continue
    if not fm or not isinstance(fm, dict):
        continue
    related = fm.get("related", [])
    if not related:
        empty_related.append(p.stem)
    elif isinstance(related, list):
        real = [r for r in related if isinstance(r, str) and "unknown" not in r.lower()]
        if not real:
            src_unknown_related.append(p.stem)
        real_related_count[len(real)] += 1

print(f"Cards with EMPTY related: {len(empty_related)}")
print(f"Cards with ONLY src_unknown/pending_unknown in related: {len(src_unknown_related)}")
print(f"Total cards with no real related links: {len(empty_related) + len(src_unknown_related)}")
print()
print("Real related link count distribution:")
for count, num_cards in sorted(real_related_count.items()):
    print(f"  {count} real links: {num_cards} cards")
print()
print("Sample empty related cards (first 20):")
for c in empty_related[:20]:
    print(f"  {c}")
