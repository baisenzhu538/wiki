import yaml
from pathlib import Path

wiki = Path("30_wiki")
nested = 0
normal_str = 0
empty_or_none = 0
total = 0

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
        empty_or_none += 1
        continue
    first = related[0]
    if isinstance(first, list):
        nested += 1
    elif isinstance(first, str):
        normal_str += 1

print(f"Total cards: {total}")
print(f"Nested list (CORRUPTED): {nested}")
print(f"Normal string (FIXED): {normal_str}")
print(f"Empty/no related: {empty_or_none}")
print()
if nested == 0:
    print("ALL CLEAN - Zero nested list corruption remaining!")
else:
    print(f"WARNING: {nested} cards still corrupted")
