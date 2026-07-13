"""#185 v2: Fix ALL template placeholder wikilinks"""
from pathlib import Path
import re

VAULT = Path(__file__).resolve().parent.parent.parent

# Broader patterns — catch all [[keyword]] that are NOT real card references
patterns = [
    "[[xxx]]", "[[...]]", "[[wikilink]]", "[[case-xxx]]", "[[card-id]]",
    "[[id]]", "[[src_unknown]]", "[[A]]", "[[B]]", "[[concept-id]]",
    "[[framework-id]]", "[[tool-id]]", "[[case-id]]", "[[concept-xxx]]",
    "[[your-card-name]]", "[[your-id]]"
]

fixed = 0
scan_dirs = [".agent", "70_product", "kdo-tools", "30_wiki", "40_outputs", "90_control", "20_memory", "60_feedback"]

for sd in scan_dirs:
    dp = VAULT / sd
    if not dp.is_dir(): continue
    for f in dp.rglob("*"):
        if f.is_dir(): continue
        if any(x in str(f) for x in [".sandbox", ".tmp", "__pycache__", ".git", "raw/ocr", ".bak"]): continue
        # Accept all text files — broader than just .md/.yaml
        try:
            c = f.read_text(encoding="utf-8", errors="replace")
        except: continue

        # Skip if no [[ in file at all
        if "[[" not in c: continue

        orig = c
        for p in patterns:
            if p in c:
                # Only wrap if not already in backticks
                c = re.sub(r"(?<!`)" + re.escape(p) + r"(?!`)", "`" + p + "`", c)

        if c != orig:
            f.write_text(c, encoding="utf-8")
            fixed += 1
            print("  %s" % f.relative_to(VAULT))

print("\nFixed: %d files" % fixed)
# Quick verify
remaining = 0
for sd in scan_dirs:
    dp = VAULT / sd
    if not dp.is_dir(): continue
    for f in dp.rglob("*"):
        if f.is_dir(): continue
        if any(x in str(f) for x in [".sandbox", ".tmp", "__pycache__", ".git", "raw/ocr", ".bak"]): continue
        try: c = f.read_text(encoding="utf-8", errors="replace")
        except: continue
        for p in patterns:
            if p in c and "`" + p + "`" not in c:
                remaining += 1
                break
print("Remaining (unfixed): %d files" % remaining)
