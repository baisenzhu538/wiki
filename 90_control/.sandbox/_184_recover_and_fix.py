"""#184: Recover corrupted frontmatter (missing --- markers) + fix YAML"""
import yaml, re, sys
from pathlib import Path

VAULT = Path(__file__).resolve().parent.parent.parent

# Scan for corrupted files — frontmatter text without --- markers
corrupted = 0
recovered = 0
for base_dir in ["30_wiki", "10_raw/ocr-cards"]:
    bp = VAULT / base_dir
    if not bp.is_dir(): continue
    for f in bp.rglob("*.md"):
        if any(x in str(f) for x in [".sandbox", ".tmp", "__pycache__"]): continue
        try:
            content = f.read_text(encoding="utf-8", errors="replace")
        except: continue

        # Check if frontmatter is intact
        fm_match = re.match(r"^---\s*\n(.*?)\n---", content, re.DOTALL)
        if fm_match: continue  # OK

        # Detect corrupted: starts with frontmatter fields but no --- markers
        # Check if first line looks like a YAML key (contains "id:" or "title:")
        first_line = content.split("\n")[0] if content else ""
        if not re.match(r'^\w+:\s', first_line): continue  # Not a corrupted card

        # Find body start (title line starting with #)
        body_start = re.search(r"\n#[^#]", content)
        if not body_start: continue

        fm_text = content[:body_start.start()].strip()
        body = content[body_start.start():]

        # Fix YAML indentation before wrapping
        lines = fm_text.splitlines()
        fixed_lines = []
        for line in lines:
            stripped = line.lstrip()
            if stripped.startswith("-") and line.startswith("    "):
                line = "  " + stripped
            fixed_lines.append(line)
        fm_text = "\n".join(fixed_lines)

        # Verify YAML
        try:
            yaml.safe_load(fm_text)
        except:
            continue  # Still broken, skip

        recovered_content = "---\n" + fm_text + "\n---\n" + body
        f.write_text(recovered_content, encoding="utf-8")
        recovered += 1

        if recovered <= 5:
            print(f"  Recovered: {f.relative_to(VAULT)}")

print(f"Recovered: {recovered} files")

# Re-verify
ok = fail = 0
for base_dir in ["30_wiki", "10_raw/ocr-cards"]:
    bp = VAULT / base_dir
    if not bp.is_dir(): continue
    for f in bp.rglob("*.md"):
        if any(x in str(f) for x in [".sandbox", ".tmp", "__pycache__"]): continue
        try:
            content = f.read_text(encoding="utf-8", errors="replace")
        except: continue
        fm_match = re.match(r"^---\s*\n(.*?)\n---", content, re.DOTALL)
        if not fm_match:
            fail += 1
            continue
        try:
            yaml.safe_load(fm_match.group(1))
            ok += 1
        except:
            fail += 1

print(f"Post-recovery: OK={ok}, Fail={fail}")
