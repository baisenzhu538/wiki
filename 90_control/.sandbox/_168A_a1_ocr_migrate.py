"""#168A A-1: OCR物理迁移 dry-run/apply"""
import re, sys, shutil, os
from pathlib import Path

VAULT = Path(__file__).resolve().parent.parent.parent
DRY = "--apply" not in sys.argv
MODE = "DRY-RUN" if DRY else "APPLY"

SRC = VAULT / "30_wiki/raw/ocr"
DST = VAULT / "10_raw/ocr-cards"
CARDS = sorted(SRC.glob("*.md"))

# ── 1. 物理迁移 ──
print(f"[1/6] Physical migration ({MODE})")
print(f"  {len(CARDS)} cards: {SRC} -> {DST}")
if not DRY:
    DST.mkdir(parents=True, exist_ok=True)
    for card in CARDS:
        shutil.move(str(card), str(DST / card.name))
    # Remove empty source dir
    try:
        SRC.rmdir()
    except OSError:
        pass
    print(f"  Moved {len(CARDS)} cards")

# ── 2. 机器边清空 ──
print(f"\n[2/6] Machine edge cleanup ({MODE})")
cleared = 0
edge_count = 0
for card in sorted(DST.glob("*.md")) if not DRY else CARDS:
    try:
        c = card.read_text(encoding="utf-8", errors="replace")
    except: continue
    fm_match = re.match(r"^(---\s*\n.*?\n---)", c, re.DOTALL)
    if not fm_match: continue
    fm = fm_match.group(1)
    rest = c[len(fm):]
    # Count related entries
    related_count = len([l for l in fm.splitlines() if l.strip().startswith("-") and "[[" in l])
    if related_count == 0: continue
    edge_count += related_count
    # Remove all related entries
    lines = fm.splitlines()
    new_lines = []
    for l in lines:
        if re.match(r'^\s+-\s+', l) and ('[[' in l or '[[' in l):
            continue
        new_lines.append(l)
    new_fm = "\n".join(new_lines)
    new_content = new_fm + rest
    if not DRY:
        card.write_text(new_content, encoding="utf-8")
    cleared += 1

if DRY:
    print(f"  Would clear {edge_count} related entries from {cleared} cards")
else:
    print(f"  Cleared {edge_count} related entries from {cleared} cards")

# ── 3. 引用链修复：正式卡 source_refs ──
print(f"\n[3/6] Source refs fixup ({MODE})")
refs_fixed = 0
for d in ["concepts","frameworks","tools","cases","systems","methods","dark-knowledges","dk","domains","decisions","skills"]:
    dpath = VAULT / "30_wiki" / d
    if not dpath.is_dir(): continue
    for f in dpath.rglob("*.md"):
        try:
            c = f.read_text(encoding="utf-8", errors="replace")
        except: continue
        if "30_wiki/raw/ocr" not in c: continue
        new_c = c.replace("30_wiki/raw/ocr", "10_raw/ocr-cards")
        if new_c == c: continue
        rel = str(f.relative_to(VAULT))
        if not DRY:
            f.write_text(new_c, encoding="utf-8")
        refs_fixed += 1
        print(f"  {rel}")

print(f"  Fixed {refs_fixed} source_refs")

# ── 4. 硬编码路径更新 ──
print(f"\n[4/6] Hardcoded path updates ({MODE})")
hardcoded = [
    ("90_control/ingestion-pipeline.md", [(124, "30_wiki/raw/ocr", "10_raw/ocr-cards"),
                                           (133, "30_wiki/raw/ocr", "10_raw/ocr-cards"),
                                           (140, "30_wiki/raw/ocr", "10_raw/ocr-cards")]),
    ("90_control/scripts/fix_cb_ew.py", [(182, "30_wiki/raw/ocr", "10_raw/ocr-cards")]),
    ("90_control/scripts/label-quality-migrate.py", [(71, "30_wiki/raw/ocr", "10_raw/ocr-cards")]),
    ("90_control/.sandbox/_ocr_final_cleanup.py", [(67, "30_wiki/raw/ocr", "10_raw/ocr-cards"),
                                                     (68, "30_wiki/raw/ocr", "10_raw/ocr-cards")]),
    (".agent/context.md", [(98, "30_wiki/raw/ocr", "10_raw/ocr-cards")]),
]

updated = 0
for path, changes in hardcoded:
    f = VAULT / path
    if not f.exists():
        print(f"  SKIP {path} (not found)")
        continue
    c = f.read_text(encoding="utf-8", errors="replace")
    new_c = c
    for line_no, old, new in changes:
        if old in new_c:
            new_c = new_c.replace(old, new)
    if new_c == c: continue
    if not DRY:
        f.write_text(new_c, encoding="utf-8")
    updated += 1
    print(f"  {path}")

print(f"  Updated {updated} files")

# ── 5. needs-review 伪域清洗 ──
print(f"\n[5/6] needs-review domain cleanup ({MODE})")
domain_fixed = 0
for card in sorted(DST.glob("*.md")) if not DRY else sorted(SRC.glob("*.md")):
    try:
        c = card.read_text(encoding="utf-8", errors="replace")
    except: continue
    fm_match = re.match(r"^(---\s*\n.*?\n---)", c, re.DOTALL)
    if not fm_match: continue
    fm = fm_match.group(1)
    rest = c[len(fm):]
    if "needs-review" not in fm: continue
    # Check if needs-review is in domain field context
    if "domain:" in fm:
        domain_section_start = fm.find("domain:")
        domain_section_end = fm.find("\n", fm.find("\n", domain_section_start + 1) + 1)
        if "needs-review" in fm[domain_section_start:domain_section_end]:
            new_fm = fm.replace("- needs-review\n", "").replace("  - needs-review\n", "")
            if new_fm != fm:
                domain_fixed += 1
                if not DRY:
                    card.write_text(new_fm + rest, encoding="utf-8")

print(f"  Fixed {domain_fixed} needs-review domain entries")

# ── 6. 复扫验证 ──
print(f"\n[6/6] Residual scan")
import subprocess
r = subprocess.run(["rg", "-l", "30_wiki/raw/ocr", "30_wiki/", "90_control/", ".agent/"],
    capture_output=True, text=True, cwd=str(VAULT))
remaining = [l for l in r.stdout.strip().split("\n") if l and ".sandbox/" not in l and "tasks/" not in l and "memory/" not in l and "corrections/" not in l]
if remaining:
    print(f"  WARNING: {len(remaining)} active references remain:")
    for l in remaining[:10]:
        print(f"    {l}")
else:
    print(f"  No active references to 30_wiki/raw/ocr/ found")

print(f"\n{MODE} complete.")
