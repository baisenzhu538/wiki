"""#184: 全库 yaml.safe_load 体检"""
import yaml, re, sys
from pathlib import Path
from collections import Counter

VAULT = Path(__file__).resolve().parent.parent.parent
SCAN_DIRS = [(VAULT/"30_wiki", "30_wiki"), (VAULT/"10_raw/ocr-cards", "10_raw/ocr-cards")]

type1 = []  # parse error
type2 = []  # parse OK but structure anomaly
type3 = []  # no frontmatter
ok = 0

for base_dir, label in SCAN_DIRS:
    if not base_dir.is_dir(): continue
    for f in base_dir.rglob("*.md"):
        if any(x in str(f) for x in [".sandbox", ".tmp", "__pycache__"]): continue
        try:
            content = f.read_text(encoding="utf-8", errors="replace")
        except: continue

        fm_match = re.match(r"^---\s*\n(.*?)\n---", content, re.DOTALL)
        if not fm_match:
            type3.append(str(f.relative_to(VAULT)))
            continue

        fm_text = fm_match.group(1)
        try:
            fm = yaml.safe_load(fm_text)
        except Exception as e:
            type1.append((str(f.relative_to(VAULT)), str(e)[:80]))
            continue

        if not isinstance(fm, dict):
            type1.append((str(f.relative_to(VAULT)), "not a dict"))
            continue

        # Structure checks
        issues = []
        if "related" in fm and not isinstance(fm["related"], list):
            issues.append("related is not list")
        if "source_refs" in fm and not isinstance(fm["source_refs"], list):
            issues.append("source_refs is not list")
        if "id" not in fm or not fm["id"]:
            issues.append("missing id")

        if issues:
            type2.append((str(f.relative_to(VAULT)), issues))
        else:
            ok += 1

print(f"=== #184 YAML Audit ===")
print(f"OK:                 {ok}")
print(f"Type1 (parse fail): {len(type1)}")
print(f"Type2 (anomaly):    {len(type2)}")
print(f"Type3 (no fm):      {len(type3)}")

if type1:
    print(f"\n--- Type1: Parse Failures ---")
    for path, err in type1[:20]:
        print(f"  {path}: {err}")

if type2:
    print(f"\n--- Type2: Structure Anomalies ---")
    for path, issues in type2[:30]:
        print(f"  {path}: {issues}")

if type3:
    print(f"\n--- Type3: No Frontmatter ---")
    for path in type3[:20]:
        print(f"  {path}")
