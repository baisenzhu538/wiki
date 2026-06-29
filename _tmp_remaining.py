import yaml
from pathlib import Path
from collections import Counter

wiki = Path("30_wiki")
remaining = []
entry_patterns = Counter()

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
    related = fm.get("related", [])
    if not isinstance(related, list) or not related:
        continue
    first = related[0]
    if isinstance(first, list):
        remaining.append(str(p.relative_to(wiki)))
        # Classify the pattern
        for i, item in enumerate(related):
            if isinstance(item, list):
                if len(item) == 2 and isinstance(item[0], str) and isinstance(item[1], str):
                    entry_patterns["[card, alias] pair"] += 1
                elif len(item) == 1 and isinstance(item[0], str):
                    entry_patterns["[card] single"] += 1
                else:
                    entry_patterns[f"list len={len(item)}: {type(item[0]).__name__}"] += 1

print(f"Remaining nested-list cards: {len(remaining)}")
print()
print("Entry patterns in remaining cards:")
for pat, count in entry_patterns.most_common():
    print(f"  {count}: {pat}")
print()
print("Sample remaining cards:")
for c in remaining[:10]:
    print(f"  {c}")
