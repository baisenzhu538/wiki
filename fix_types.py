"""Add missing type field to wiki cards based on filename prefix inference."""
import re
from pathlib import Path
from collections import Counter

VAULT = Path(r"C:\Users\Administrator\Desktop\wiki\30_wiki\concepts")

PREFIX_MAP = {
    "yt": "concept", "master": "framework", "case": "case",
    "dk": "dark-knowledge", "skill": "skill", "anthropic": "concept",
    "concept": "concept", "aima": "concept", "kimi": "concept",
    "deepseek": "concept", "ocr": "concept",
}

def add_type(filepath):
    text = filepath.read_text(encoding="utf-8")
    lines = text.split("\n")
    in_fm = False
    has_type = False
    id_idx = None
    fm_start = None
    for i, line in enumerate(lines):
        if line.strip() == "---":
            if not in_fm:
                in_fm = True
                fm_start = i
            elif fm_start is not None:
                break
        elif in_fm:
            if re.match(r'^type:\s*\S', line):
                has_type = True
            if id_idx is None and re.match(r'^id:\s*\S', line):
                id_idx = i
    if has_type:
        return None
    stem = filepath.stem
    prefix = stem.split("-", 1)[0] if "-" in stem else stem
    typ = PREFIX_MAP.get(prefix, "concept")
    type_line = f'type: "{typ}"'
    if id_idx is not None:
        lines.insert(id_idx + 1, type_line)
    elif fm_start is not None:
        lines.insert(fm_start + 1, type_line)
    else:
        return None
    filepath.write_text("\n".join(lines), encoding="utf-8")
    return typ

if __name__ == "__main__":
    fixed = []
    skipped = []
    for md in sorted(VAULT.glob("*.md")):
        r = add_type(md)
        if r:
            fixed.append((md.stem, r))
        else:
            skipped.append(md.stem)

    print(f"Fixed: {len(fixed)}")
    for stem, typ in fixed[:20]:
        print(f"  {stem} -> {typ}")
    if len(fixed) > 20:
        print(f"  ... and {len(fixed) - 20} more")
    print(f"Already had type: {len(skipped)}")

    counts = Counter(t for _, t in fixed)
    print("\nBy type:")
    for t, c in counts.most_common():
        print(f"  {t}: {c}")
