import yaml
from pathlib import Path
from collections import Counter

wiki = Path("30_wiki")
tag_samples = []
tag_counts = Counter()
cards_with_tags = 0
cards_without_tags = 0

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
    tags = fm.get("tags", [])
    if not tags or not isinstance(tags, list) or not tags:
        cards_without_tags += 1
    else:
        cards_with_tags += 1
        for t in tags[:3]:
            if isinstance(t, str):
                tag_counts[t] += 1

print(f"Cards with tags: {cards_with_tags}")
print(f"Cards without tags: {cards_without_tags}")
print(f"Unique tag values (top 15):")
for t, c in tag_counts.most_common(15):
    print(f"  {c:4d}x {t}")
