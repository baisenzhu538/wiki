"""Fix #168A 3 residuals"""
import re
from pathlib import Path
VAULT = Path(__file__).resolve().parent.parent.parent

# 1. A-1: one OCR card still has needs-review
f1 = VAULT / "10_raw/ocr-cards/ocr-微信图片_20260507004802_38_32.md"
c = f1.read_text(encoding="utf-8", errors="replace")
c = c.replace("- needs-review\n", "")
f1.write_text(c, encoding="utf-8")
print("1. needs-review cleaned: ocr-微信图片_20260507004802_38_32.md")

# 2. A-2: 17 cards with composite domain, broader match
REPL = {
    "yitang- ai-saas": ["yitang", "ai-saas"],
    "learning-methodology- ai-saas": ["learning-methodology", "ai-saas"],
}
fixed = 0
for d in ["concepts","frameworks","tools","cases","methods","systems","dark-knowledges","dk","domains","decisions","skills"]:
    dp = VAULT / "30_wiki" / d
    if not dp.is_dir(): continue
    for f in dp.rglob("*.md"):
        try: c = f.read_text(encoding="utf-8", errors="replace")
        except: continue
        orig = c
        for old, new_list in REPL.items():
            if old in c:
                new_items = "\n".join(f"  - {x}" for x in new_list)
                c = c.replace(f"  - {old}", new_items)
        if c != orig:
            f.write_text(c, encoding="utf-8")
            fixed += 1
print(f"2. A-2 residual: {fixed} cards fixed")

# 3. A-3: 紫鲸ai pending_unknown
f3 = VAULT / "30_wiki/concepts/紫鲸ai智能体工作流平台.md"
c3 = f3.read_text(encoding="utf-8", errors="replace")
count = c3.count("[[pending_unknown]]")
c3 = re.sub(r'\s*-\s*"[\[\[].*?pending_unknown.*?[\]\]"]"\s*\n', '\n', c3)
c3 = re.sub(r'\s*-\s*\[\[pending_unknown\]\]\s*\n', '\n', c3)
c3 = re.sub(r'\s*-\s*[\x27\"][\[\[].*?pending_unknown.*?[\]\]][\x27\"]\s*\n', '\n', c3)
f3.write_text(c3, encoding="utf-8")
print(f"3. A-3 residual: {count} pending_unknown removed from 紫鲸ai")

# Verify
print("\nVerification:")
# Check A-1
c1_check = f1.read_text(encoding="utf-8", errors="replace")
print(f"  A-1 needs-review in ocr card: {'needs-review' in c1_check}")

# Check A-2: domain grep
import subprocess
r = subprocess.run(["rg", "-c", "yitang- ai-saas|learning-methodology- ai-saas", "30_wiki/tools/"],
    capture_output=True, text=True, cwd=str(VAULT), encoding="utf-8", errors="replace")
remaining = sum(int(l.split(":")[1]) for l in r.stdout.strip().split("\n") if ":" in l and l.split(":")[1].isdigit())
print(f"  A-2 composite domain remaining: {remaining}")

# Check A-3
c3_check = f3.read_text(encoding="utf-8", errors="replace")
print(f"  A-3 pending_unknown in 紫鲸: {'pending_unknown' in c3_check}")
