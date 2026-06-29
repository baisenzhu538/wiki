import yaml
from pathlib import Path
from collections import Counter

wiki = Path("30_wiki")
error_types = Counter()
fixable = []
unfixable = []

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
    except Exception as e:
        err_str = str(e)
        rel = str(p.relative_to(wiki))
        # Classify error
        if "expected <block end>, but found '-'" in err_str:
            error_types["source_refs indent issue"] += 1
            fixable.append(rel)
        elif "expected <block end>, but found" in err_str:
            error_types[f"other block mapping: {err_str[err_str.find('found')+6:err_str.find('found')+60]}"] += 1
            unfixable.append(rel)
        elif "mapping values are not allowed" in err_str:
            error_types["mapping values not allowed"] += 1
            fixable.append(rel)
        else:
            error_types[f"other: {err_str[:80]}"] += 1
            unfixable.append(rel)

print(f"Total YAML errors: {len(fixable) + len(unfixable)}")
print(f"Fixable (known pattern): {len(fixable)}")
print(f"Need investigation: {len(unfixable)}")
print()
print("Error type distribution:")
for t, c in error_types.most_common():
    print(f"  {c:3d}: {t}")
print()
print("Sample fixable files:")
for f in fixable[:15]:
    print(f"  {f}")
