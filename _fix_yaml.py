"""Minimal YAML fix: remove blank lines within block sequences and fix orphaned lines."""
import yaml
from pathlib import Path

CONCEPTS = Path(r"C:\Users\Administrator\Desktop\wiki\30_wiki\concepts")

def fix_frontmatter_whitespace(text):
    """Remove blank lines within block collections (sequences/mappings) in YAML frontmatter.
    Blank lines between top-level keys are preserved.
    """
    if not text.startswith("---\n"):
        return text
    end = text.find("\n---\n", 4)
    if end == -1:
        return text
    raw_fm = text[4:end]
    body = text[end+5:]

    lines = raw_fm.split("\n")
    result = []
    # Track whether we're inside a block (list or nested mapping)
    depth = 0  # >0 means we're inside a block collection

    for line in lines:
        stripped = line.strip()

        # Detect depth by leading whitespace
        indent = len(line) - len(line.lstrip())

        # Top-level keys reset depth tracking
        if indent == 0 and stripped and not stripped.startswith("-") and not stripped.startswith("#"):
            depth = 0
            if stripped and not stripped.startswith("#"):
                # Check if this key opens a block
                if stripped.endswith(":") and not stripped.startswith("-"):
                    pass  # Could open a block
            result.append(line)
            continue

        # Indented lines or list items
        if indent > 0 or stripped.startswith("- "):
            if depth == 0:
                depth = 1

            # Skip blank lines inside blocks
            if not stripped and depth > 0:
                continue

            # Skip blank lines
            if not stripped:
                continue

            result.append(line)
            continue

        # Blank lines between top-level keys
        result.append(line)

    new_fm = "\n".join(result)
    try:
        yaml.safe_load(new_fm)
        return "---\n" + new_fm + "\n---\n" + body
    except yaml.YAMLError:
        return text  # Don't change if still invalid


# Find and fix
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
        new_text = fix_frontmatter_whitespace(text)
        if new_text != text:
            # Verify
            e = new_text.find("\n---\n", 4)
            try:
                yaml.safe_load(new_text[4:e])
                f.write_text(new_text, encoding="utf-8")
                print(f"  FIXED: {f.stem}")
            except yaml.YAMLError as err:
                print(f"  PARTIAL: {f.stem} — {err}")
                f.write_text(new_text, encoding="utf-8")
        else:
            print(f"  UNFIXABLE: {f.stem} — whitespace removal didn't help")

# Final scan
remaining = []
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
        remaining.append(f.stem)

print(f"\nYAML-valid: {424 - len(remaining)}/{424}")
if remaining:
    print(f"Still broken ({len(remaining)}): {remaining}")
