"""Final fix: wrap YAML values containing unescaped double-quotes in single quotes."""
import yaml
from pathlib import Path

CONCEPTS = Path(r"C:\Users\Administrator\Desktop\wiki\30_wiki\concepts")

def fix_double_quotes_in_values(raw_fm):
    """Wrap values containing bare double-quotes in single quotes for YAML safety."""
    lines = raw_fm.split("\n")
    result = []
    for line in lines:
        stripped = line.strip()
        # Only process indented list items (dimensions items)
        if stripped.startswith("- ") and ":" in stripped:
            key_part, _, val_part = stripped.partition(": ")
            key_part = key_part[2:]  # Remove "- " prefix
            # If value contains bare " that could be interpreted as YAML string delimiter
            if '"' in val_part:
                # Count quotes - if odd, it's a problem
                quote_count = val_part.count('"')
                if quote_count > 0 and '=' in val_part:
                    # Wrap entire value in single quotes
                    indent = len(line) - len(line.lstrip())
                    result.append(" " * indent + f"- {key_part}: '{val_part}'")
                    continue
            # Also check for "pattern"=pattern which confuses YAML
            if val_part.strip().startswith('"') and '=' in val_part:
                indent = len(line) - len(line.lstrip())
                result.append(" " * indent + f"- {key_part}: '{val_part}'")
                continue
        result.append(line)
    return "\n".join(result)


# Fix all 3 broken cards
for filename in ["yt-decision-y-model.md", "yt-decision-width-method.md", "yt-model-aesthetic-progression.md"]:
    path = CONCEPTS / filename
    text = path.read_text(encoding="utf-8", errors="replace")
    if not text.startswith("---\n"):
        continue
    end = text.find("\n---\n", 4)
    if end == -1:
        continue
    raw_fm = text[4:end]
    body = text[end+5:]

    fixed_fm = fix_double_quotes_in_values(raw_fm)
    try:
        yaml.safe_load(fixed_fm)
        new_text = "---\n" + fixed_fm + "\n---\n" + body
        path.write_text(new_text, encoding="utf-8")
        print(f"FIXED: {filename}")
    except yaml.YAMLError as e:
        print(f"STILL BROKEN: {filename} — {e}")

# Final verification
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

print(f"\nAll cards YAML-valid: {424 - len(remaining)}/{424}")
if remaining:
    print(f"Still broken: {remaining}")
