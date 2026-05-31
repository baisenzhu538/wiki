"""Scan all concept cards for frontmatter corruption after Data Curator Clean."""
import yaml
from pathlib import Path

CONCEPTS_DIR = Path(r"C:\Users\Administrator\Desktop\wiki\30_wiki\concepts")

def check_frontmatter_integrity(filepath: Path) -> list[str]:
    text = filepath.read_text(encoding="utf-8", errors="replace")
    if not text.startswith("---\n"):
        return []
    end = text.find("\n---\n", 4)
    if end == -1:
        return []
    raw_fm = text[4:end]
    issues = []
    try:
        metadata = yaml.safe_load(raw_fm)
    except yaml.YAMLError as e:
        issues.append(f"YAML parse error: {e}")
        return issues
    if not isinstance(metadata, dict):
        issues.append("Frontmatter is not a dict after parse")
        return issues
    # Check for known-bug patterns: dict keys starting with "- " (flattened list-as-dict)
    for key, value in metadata.items():
        if isinstance(value, dict):
            dash_keys = [k for k in value if str(k).startswith("-")]
            if len(dash_keys) > 1:
                issues.append(f"Field '{key}' appears to be flattened list-as-dict ({len(dash_keys)} dash-keys)")
        elif isinstance(value, list):
            str_colons = [i for i in value if isinstance(i, str) and ":" in i]
            if len(str_colons) >= 3 and len(str_colons) == len(value):
                issues.append(f"Field '{key}' has {len(str_colons)} string items with ':' — may be flattened structured data")
    return issues

affected = []
total = 0
for f in sorted(CONCEPTS_DIR.glob("*.md")):
    total += 1
    issues = check_frontmatter_integrity(f)
    if issues:
        affected.append((f, issues))
        print(f"  BUG {f.stem}")
        for issue in issues:
            print(f"    {issue}")

print(f"\nScanned {total} cards.")
print(f"Potentially corrupted: {len(affected)}")
if not affected:
    print("No corruption detected beyond the 2 already rolled back.")
