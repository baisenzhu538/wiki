import yaml
from pathlib import Path
from collections import Counter

wiki = Path("30_wiki")
related_types = Counter()
empty_count = 0
has_real_links = 0
only_unknown = 0

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
        empty_count += 1
        continue
    if not isinstance(related, list):
        continue
    
    has_real = False
    has_unknown = False
    for r in related:
        if not isinstance(r, str):
            continue
        if "pending_unknown" in r:
            related_types["pending_unknown"] += 1
            has_unknown = True
        elif "src_unknown" in r:
            related_types["src_unknown"] += 1
            has_unknown = True
        elif r.startswith("[["):
            related_types["wikilink"] += 1
            has_real = True
        else:
            related_types[f"other: {r[:50]}"] += 1
            has_real = True
    
    if has_real:
        has_real_links += 1
    elif has_unknown:
        only_unknown += 1

print(f"Empty related: {empty_count}")
print(f"Only src_unknown/pending_unknown: {only_unknown}")
print(f"Has at least 1 real link: {has_real_links}")
print()
print("Related entry types:")
for t, c in related_types.most_common(20):
    print(f"  {c}: {t}")
