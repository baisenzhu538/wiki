"""#168A A-2: ai-saas复合domain拆分 dry-run/apply"""
import re, sys
from pathlib import Path

VAULT = Path(__file__).resolve().parent.parent.parent
DRY = "--apply" not in sys.argv

REPLACEMENTS = {
    "yitang- ai-saas": ["yitang", "ai-saas"],
    "ai-saas- yitang": ["ai-saas", "yitang"],
    "learning-methodology- ai-saas": ["learning-methodology", "ai-saas"],
    "ai-saas- ai": ["ai-saas", "ai"],
}

fixed = 0
for d in ["concepts","frameworks","tools","cases","systems","methods","dark-knowledges","dk","domains","decisions","skills"]:
    dpath = VAULT / "30_wiki" / d
    if not dpath.is_dir(): continue
    for f in dpath.rglob("*.md"):
        try: c = f.read_text(encoding="utf-8", errors="replace")
        except: continue
        original = c
        for old, new_list in REPLACEMENTS.items():
            if old in c:
                new_items = "\n".join(f"  - {x}" for x in new_list)
                c = c.replace(f"  - {old}", new_items)
        if c == original: continue
        if not DRY: f.write_text(c, encoding="utf-8")
        fixed += 1
        if DRY or fixed <= 5:
            print(f"  {f.relative_to(VAULT)}: domain split")

mode = "DRY-RUN" if DRY else "APPLY"
print(f"\n{mode}: {fixed} cards fixed")
if not DRY: print("Done.")
