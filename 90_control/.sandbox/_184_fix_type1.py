"""#184: Fix Type1 YAML parse errors. Dry-run first."""
import yaml, re, sys
from pathlib import Path

VAULT = Path(__file__).resolve().parent.parent.parent
DRY = "--apply" not in sys.argv

def fix_frontmatter(fm_text):
    """Try to fix common YAML issues. Returns (fixed_text, None) or (None, error)."""
    lines = fm_text.splitlines()
    fixed_lines = []
    in_related = False
    base_indent = None

    for i, line in enumerate(lines):
        stripped = line.lstrip()
        # Detect related list
        if re.match(r'^related:\s*$', stripped):
            in_related = True
            fixed_lines.append(line)
            continue
        if in_related and stripped and not stripped.startswith('-') and ':' in stripped:
            in_related = False

        if in_related and stripped.startswith('-'):
            # Find the current indent
            indent = len(line) - len(line.lstrip())
            if base_indent is None:
                base_indent = indent
            # Normalize to base_indent
            if indent != base_indent:
                line = " " * base_indent + stripped
        fixed_lines.append(line)

    new_fm = "\n".join(fixed_lines)
    try:
        yaml.safe_load(new_fm)
        return new_fm, None
    except Exception as e:
        return None, str(e)[:80]

fixed = 0
still_broken = 0
for base_dir in ["30_wiki", "10_raw/ocr-cards"]:
    bp = VAULT / base_dir
    if not bp.is_dir(): continue
    for f in bp.rglob("*.md"):
        if any(x in str(f) for x in [".sandbox", ".tmp", "__pycache__", "raw/ocr"]): continue
        try:
            content = f.read_text(encoding="utf-8", errors="replace")
        except: continue

        fm_match = re.match(r"^---\s*\n(.*?)\n---", content, re.DOTALL)
        if not fm_match: continue
        fm_text = fm_match.group(1)

        # Skip if already valid
        try:
            yaml.safe_load(fm_text)
            continue
        except: pass

        new_fm, err = fix_frontmatter(fm_text)
        if new_fm is None:
            still_broken += 1
            continue

        rest = content[len(fm_match.group(0)):]
        new_content = "---\n" + new_fm + "\n---" + rest
        if not DRY:
            f.write_text(new_content, encoding="utf-8")
        fixed += 1

mode = "DRY-RUN" if DRY else "APPLY"
print(f"{mode}: {fixed} fixed, {still_broken} still broken")
