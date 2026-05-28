"""Select pilot cards for S4-1 broken link fixing."""
import json
from pathlib import Path
from difflib import get_close_matches
from collections import defaultdict

VAULT = Path(r"C:\Users\Administrator\Desktop\wiki")

with open(VAULT / "90_control" / "s4-broken-links.json", "r", encoding="utf-8") as f:
    data = json.load(f)

all_stems = set()
for f in VAULT.rglob("*.md"):
    if f.is_file():
        all_stems.add(f.stem)

unique_targets = set(b["target"] for b in data["broken_links"])
fixable_map = {}
for target in unique_targets:
    stem = Path(target.replace("\\", "/")).stem
    matches = get_close_matches(stem, all_stems, n=1, cutoff=0.75)
    if matches:
        fixable_map[target] = matches[0]

# Group fixable links by source file
by_source = defaultdict(list)
for bl in data["broken_links"]:
    if bl["target"] in fixable_map:
        by_source[bl["source"]].append(bl)

# Select pilot: pick cards in 30_wiki/concepts/ with 1-2 fixable links (safe, not too many)
# Exclude OCR files
candidates = []
for src, links in by_source.items():
    if "ocr-" in src.lower() or "ocr_" in src.lower():
        continue
    if len(links) <= 3:
        candidates.append((src, links))

candidates.sort(key=lambda x: -len(x[1]))

print("=== Pilot candidates (non-OCR, 1-3 fixable links each) ===")
for src, links in candidates[:15]:
    print(f"\n{src} ({len(links)} links):")
    for l in links:
        replacement = fixable_map[l["target"]]
        print(f"  L{l['line']:4d}: [[{l['target']}]] -> [[{replacement}]]")

print(f"\nTotal fixable across all files: {sum(len(v) for v in by_source.values())}")
print(f"Total files with fixable links: {len(by_source)}")
