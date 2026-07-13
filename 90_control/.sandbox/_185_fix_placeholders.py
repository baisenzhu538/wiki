"""#185: Fix template placeholder wikilinks"""
from pathlib import Path
import re

VAULT = Path(__file__).resolve().parent.parent.parent
patterns = ["[[xxx]]", "[[...]]", "[[wikilink]]", "[[case-xxx]]", "[[card-id]]", "[[A]]", "[[src_unknown]]"]
fixed = 0

scan_dirs = [".agent", "70_product", "kdo-tools", "30_wiki", "40_outputs", "90_control"]
for sd in scan_dirs:
    dp = VAULT / sd
    if not dp.is_dir(): continue
    for f in dp.rglob("*"):
        if f.is_dir(): continue
        if f.suffix not in [".md", ".yaml"]: continue
        if any(x in str(f) for x in [".sandbox", ".tmp", "__pycache__", ".git", "raw/ocr"]): continue
        try:
            c = f.read_text(encoding="utf-8", errors="replace")
        except: continue
        orig = c
        for p in patterns:
            if p in c:
                c = re.sub(r"(?<!`)" + re.escape(p) + r"(?!`)", "`" + p + "`", c)
        if c != orig:
            f.write_text(c, encoding="utf-8")
            fixed += 1
            print("  %s" % f.relative_to(VAULT))

print("\nFixed: %d files" % fixed)
