"""#184: Fix Type1 YAML parse errors — related list indentation + bare wikilinks"""
import yaml, re, sys
from pathlib import Path

VAULT = Path(__file__).resolve().parent.parent.parent
DRY = "--apply" not in sys.argv

fixed = 0
for base_dir in ["30_wiki", "10_raw/ocr-cards"]:
    bp = VAULT / base_dir
    if not bp.is_dir(): continue
    for f in bp.rglob("*.md"):
        if any(x in str(f) for x in [".sandbox", ".tmp", "__pycache__"]): continue
        try:
            content = f.read_text(encoding="utf-8", errors="replace")
        except: continue

        fm_match = re.match(r"^---\s*\n(.*?)\n---", content, re.DOTALL)
        if not fm_match: continue
        fm_text = fm_match.group(1)
        rest = content[len(fm_match.group(0)):]

        # Try parsing — if OK, skip
        try:
            yaml.safe_load(fm_text)
            continue
        except: pass

        # Fix: normalize related list indentation (4 spaces → 2 spaces)
        lines = fm_text.splitlines()
        new_lines = []
        for line in lines:
            # Fix: 4-space indented related entries → 2-space
            if line.startswith("    -") and ("[[" in line):
                line = "  " + line[4:]
            # Fix: bare wikilinks in related → add quotes
            if re.match(r"^\s+-\s+\[\[", line) and "'" not in line and '"' not in line:
                # Check if it has spaces (needs quoting)
                entry = line.split("-", 1)[1].strip()
                if " " in entry and not (entry.startswith("'") or entry.startswith('"')):
                    line = line.replace(entry, "'" + entry + "'")
            new_lines.append(line)

        new_fm = "\n".join(new_lines)
        new_content = new_fm + rest

        # Verify fix
        try:
            yaml.safe_load(new_fm)
        except:
            continue  # Still broken, skip

        if not DRY:
            f.write_text(new_content, encoding="utf-8")
        fixed += 1

mode = "DRY-RUN" if DRY else "APPLY"
print(f"{mode}: {fixed} files fixed")
