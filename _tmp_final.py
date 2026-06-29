import yaml, re
from pathlib import Path
from collections import Counter

wiki = Path("30_wiki")
total = 0
has_related_field = 0
related_is_list = 0
related_is_empty_list = 0
related_has_wikilinks = 0
body_has_wikilinks = 0
body_wikilink_count = Counter()
total_body_wikilinks = 0

for p in wiki.rglob("*.md"):
    if "_archive" in str(p) or "raw/ocr" in str(p):
        continue
    total += 1
    try:
        text = p.read_text(encoding="utf-8", errors="ignore")
    except:
        continue
    
    # Check body wikilinks
    body_start = text.find("---", 3) + 3 if text.startswith("---") else 0
    body = text[body_start:]
    wiki_links = re.findall(r'\[\[([^\]|#]+)(?:[|#][^\]]+)?\]\]', body)
    if wiki_links:
        body_has_wikilinks += 1
    total_body_wikilinks += len(wiki_links)
    for link in wiki_links:
        body_wikilink_count[link] += 1
    
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
    
    if "related" in fm:
        has_related_field += 1
        related = fm["related"]
        if isinstance(related, list):
            related_is_list += 1
            if not related:
                related_is_empty_list += 1
            for r in related:
                if isinstance(r, str) and r.startswith("[["):
                    related_has_wikilinks += 1
                    break

print(f"Total cards (excl raw/ocr, _archive): {total}")
print(f"Has 'related' field: {has_related_field}")
print(f"  related is list: {related_is_list}")
print(f"  related is empty []: {related_is_empty_list}")
print(f"  related has wikilinks: {related_has_wikilinks}")
print(f"Cards with body wikilinks: {body_has_wikilinks}")
print(f"Total body wikilinks: {total_body_wikilinks}")
print()
print("Top 20 body wikilink targets:")
for link, count in body_wikilink_count.most_common(20):
    print(f"  {count}x [[{link}]]")
