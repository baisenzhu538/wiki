"""Analyze broken links for auto-fixable close matches."""
import json
from pathlib import Path
from difflib import get_close_matches

VAULT = Path(r"C:\Users\Administrator\Desktop\wiki")

with open(VAULT / "90_control" / "s4-broken-links.json", "r", encoding="utf-8") as f:
    data = json.load(f)

# Get all existing page stems
all_stems = set()
for f in VAULT.rglob("*.md"):
    if f.is_file():
        all_stems.add(f.stem)

# For each unique broken target, find close matches
unique_targets = set(b["target"] for b in data["broken_links"])

from collections import Counter
target_counts = Counter(b["target"] for b in data["broken_links"])

fixable = {}
not_fixable = []

for target in sorted(unique_targets):
    # Extract stem from path-like or plain target
    t = target.replace("\\", "/")
    stem = Path(t).stem
    matches = get_close_matches(stem, all_stems, n=3, cutoff=0.75)
    if matches:
        fixable[target] = matches
    else:
        not_fixable.append(target)

print(f"Unique broken targets: {len(unique_targets)}")
print(f"Has close match (>=75%): {len(fixable)}")
print(f"No close match: {len(not_fixable)}")
print()

# How many total broken links would be fixable?
fixable_count = sum(target_counts[t] for t in fixable)
not_fixable_count = sum(target_counts[t] for t in not_fixable)
print(f"Fixable links: {fixable_count}")
print(f"Not fixable links (genuinely missing): {not_fixable_count}")
print()

print("Top fixable targets:")
for target, matches in sorted(fixable.items(), key=lambda x: -target_counts[x[0]])[:30]:
    count = target_counts[target]
    print(f"  {count:3d}x [[{target[:90]}]]")
    for m in matches:
        print(f"         -> {m}")

print()
print("Top NOT fixable (genuinely missing):")
for target in sorted(not_fixable, key=lambda x: -target_counts[x])[:20]:
    count = target_counts[target]
    if count >= 2:
        print(f"  {count:3d}x [[{target[:90]}]]")
