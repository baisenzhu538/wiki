import yaml
from pathlib import Path
from collections import Counter

wiki = Path("30_wiki")
nested_list_cards = []
empty_related = []
no_related = []
normal_related = []

for p in wiki.rglob("*.md"):
    if "_archive" in str(p) or "raw/ocr" in str(p):
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
    
    related = fm.get("related")
    if related is None:
        no_related.append(p.stem)
    elif not isinstance(related, list):
        continue  # skip unusual types
    elif not related:
        empty_related.append(p.stem)
    else:
        # Check if entries are nested lists
        first = related[0]
        if isinstance(first, list):
            nested_list_cards.append(str(p.relative_to(wiki)))
        else:
            normal_related.append(str(p.relative_to(wiki)))

print(f"Nested list related (CORRUPTED): {len(nested_list_cards)}")
print(f"Empty related []: {len(empty_related)}")
print(f"No related field: {len(no_related)}")
print(f"Normal related (strings): {len(normal_related)}")
print()
print("Sample corrupted cards:")
for c in nested_list_cards[:10]:
    print(f"  {c}")
print()
print("Sample normal cards:")
for c in normal_related[:10]:
    print(f"  {c}")
