import yaml, re
from pathlib import Path
from collections import Counter

wiki = Path("30_wiki")
# Find cards with related field but no wikilinks - what ARE they?
related_content_types = Counter()
samples = []

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
        continue
    if not isinstance(related, list):
        related_content_types[f"non-list: {type(related).__name__}"] += 1
        continue
    if not related:
        related_content_types["empty []"] += 1
        continue
    
    # Classify the content
    has_wikilink = False
    has_bare_id = False
    has_unknown = False
    has_other = False
    
    for r in related:
        if not isinstance(r, str):
            related_content_types[f"non-str item: {type(r).__name__}"] += 1
            continue
        if r.startswith("[["):
            has_wikilink = True
        elif "unknown" in r.lower():
            has_unknown = True
        elif re.match(r'^[\w-]+$', r):  # bare id like 'yt-something'
            has_bare_id = True
        else:
            has_other = True
            if len(samples) < 10:
                samples.append((p.stem, r))
    
    if has_wikilink:
        related_content_types["has [[wikilinks]]"] += 1
    elif has_unknown and not has_bare_id:
        related_content_types["only src/pending_unknown"] += 1
    elif has_bare_id and not has_unknown:
        related_content_types["only bare IDs (no brackets)"] += 1
    elif has_bare_id and has_unknown:
        related_content_types["mix bare IDs + unknown"] += 1
    elif has_other:
        related_content_types["other content"] += 1
    else:
        related_content_types["UNCLASSIFIED"] += 1

print("=== related field content classification ===")
for t, c in related_content_types.most_common():
    print(f"  {c:5d}: {t}")

print(f"\n=== Sample 'other' related entries ===")
for name, val in samples:
    print(f"  {name}: '{val[:100]}'")
