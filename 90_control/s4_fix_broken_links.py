"""S4-1: Batch fix broken wikilinks via close-match replacement."""
import json
import re
from pathlib import Path
from difflib import get_close_matches
from collections import Counter

VAULT = Path(r"C:\Users\Administrator\Desktop\wiki")

# Load broken links
with open(VAULT / "90_control" / "s4-broken-links.json", "r", encoding="utf-8") as f:
    data = json.load(f)

# Index all existing .md stems (case-insensitive)
all_stems = {}
for f in VAULT.rglob("*.md"):
    if f.is_file():
        all_stems[f.stem.lower()] = f.stem

# Build fix mapping: broken_target -> correct_stem
target_counts = Counter(b["target"] for b in data["broken_links"])
fix_map = {}
unfixable = []

for target in sorted(set(b["target"] for b in data["broken_links"])):
    stem = Path(target.replace("\\", "/")).stem
    all_stem_names = list(all_stems.values())
    matches = get_close_matches(stem, all_stem_names, n=1, cutoff=0.75)
    if matches and matches[0] != stem:
        fix_map[target] = matches[0]
    else:
        unfixable.append(target)

print(f"Fixable unique targets: {len(fix_map)}")
print(f"Total broken link occurrences to fix: {sum(target_counts[t] for t in fix_map)}")
print(f"Unfixable targets: {len(unfixable)}")
print()

# Show the fix mapping
for old, new in sorted(fix_map.items(), key=lambda x: -target_counts[x[0]]):
    print(f"  {target_counts[old]:3d}x  [[{old}]]  ->  [[{new}]]")
print()

# Group by source file
fixes_by_file = {}
for b in data["broken_links"]:
    if b["target"] in fix_map:
        fixes_by_file.setdefault(b["source"], []).append((b["target"], fix_map[b["target"]]))

# Pilot cards already done
already_fixed = {
    '30_wiki/concepts/yt-unit-model-ai-assisted.md',
    '30_wiki/concepts/yt-decision-consensus-iceberg.md',
    '30_wiki/concepts/yt-decision-habit-shift.md',
}

# Apply fixes
fixed_files = 0
fixed_links = 0
dry_run = False

for rel_path, replacements in sorted(fixes_by_file.items()):
    if rel_path in already_fixed:
        print(f"SKIP (pilot): {rel_path}")
        continue

    fpath = VAULT / rel_path
    if not fpath.exists():
        print(f"MISSING: {rel_path}")
        continue

    content = fpath.read_text(encoding="utf-8")
    original = content
    file_fixes = 0

    for old_target, new_target in set(replacements):
        # Match [[old_target]] or [[old_target|...]] or [[old_target#...]]
        pattern = re.compile(
            r'\[\[\s*' + re.escape(old_target) + r'\s*(?:[#|]\s*[^\]]+)?\s*\]\]'
        )
        count_before = len(pattern.findall(content))
        content = pattern.sub('[[' + new_target + ']]', content)
        file_fixes += count_before

    if content != original:
        if not dry_run:
            fpath.write_text(content, encoding="utf-8")
        fixed_files += 1
        fixed_links += file_fixes
        print(f"FIXED: {rel_path} ({file_fixes} link(s))")

print(f"\nDone. Files: {fixed_files}, Links: {fixed_links}")
