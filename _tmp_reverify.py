import yaml
from pathlib import Path

wiki = Path("30_wiki")
total = 0
empty_related = 0
has_real_links = 0
only_unknown = 0

for p in wiki.rglob("*.md"):
    if "_archive" in str(p) or "raw/ocr" in str(p):
        continue
    total += 1
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
    if not related or not isinstance(related, list) or not related:
        empty_related += 1
        continue
    has_real = any(isinstance(r, str) and not "unknown" in r.lower() for r in related)
    if has_real:
        has_real_links += 1
    else:
        only_unknown += 1

print(f"Total cards (excl _archive, raw/ocr): {total}")
print(f"Empty/null related: {empty_related}")
print(f"Has real wikilinks in related: {has_real_links}")
print(f"Only src_unknown/pending_unknown: {only_unknown}")
print(f"Cards with ZERO real outbound links: {empty_related + only_unknown}")
