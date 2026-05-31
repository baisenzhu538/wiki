"""Fix YAML frontmatter: remove blank lines from block collections that break yaml.safe_load."""
import yaml
from pathlib import Path

CONCEPTS = Path(r"C:\Users\Administrator\Desktop\wiki\30_wiki\concepts")

def normalize_frontmatter_blank_lines(text):
    """Remove blank lines inside YAML frontmatter that break block collection parsing."""
    if not text.startswith("---\n"):
        return text
    end = text.find("\n---\n", 4)
    if end == -1:
        return text
    raw_fm = text[4:end]
    body = text[end+5:]
    lines = raw_fm.split("\n")
    result = []
    in_block = False
    for line in lines:
        stripped = line.strip()
        if stripped.startswith("- ") or stripped.startswith("  ") or stripped.startswith("\t"):
            in_block = True
        elif stripped and ":" in stripped and not stripped.startswith("-"):
            in_block = False
        # Remove blank lines in block collections
        if in_block and not stripped:
            continue
        result.append(line)
    new_fm = "\n".join(result)
    # Verify valid YAML
    try:
        yaml.safe_load(new_fm)
    except yaml.YAMLError as e:
        print(f"  STILL INVALID after normalization: {e}")
        return text  # Don't write if still broken
    return "---\n" + new_fm + "\n---\n" + body

# Find all cards with YAML parse errors
broken = []
for f in sorted(CONCEPTS.glob("*.md")):
    text = f.read_text(encoding="utf-8", errors="replace")
    if not text.startswith("---\n"):
        continue
    end = text.find("\n---\n", 4)
    if end == -1:
        continue
    raw = text[4:end]
    try:
        yaml.safe_load(raw)
    except yaml.YAMLError:
        broken.append(f)

print(f"Found {len(broken)} cards with YAML parse errors.\n")

for f in broken:
    text = f.read_text(encoding="utf-8", errors="replace")
    new_text = normalize_frontmatter_blank_lines(text)
    if new_text != text:
        f.write_text(new_text, encoding="utf-8")
        # Verify after write
        verify = f.read_text(encoding="utf-8", errors="replace")
        e = verify.find("\n---\n", 4)
        if e > 0:
            try:
                yaml.safe_load(verify[4:e])
                print(f"  FIXED: {f.stem}")
            except yaml.YAMLError as err:
                print(f"  STILL BROKEN: {f.stem} — {err}")
    else:
        print(f"  UNFIXABLE: {f.stem}")

# Final scan
broken2 = []
for f in sorted(CONCEPTS.glob("*.md")):
    text = f.read_text(encoding="utf-8", errors="replace")
    if not text.startswith("---\n"):
        continue
    end = text.find("\n---\n", 4)
    if end == -1:
        continue
    try:
        yaml.safe_load(text[4:end])
    except yaml.YAMLError:
        broken2.append(f)

print(f"\nFinal: {len(broken2)} remaining YAML parse errors")
if broken2:
    for b in broken2:
        print(f"  ❌ {b.stem}")
