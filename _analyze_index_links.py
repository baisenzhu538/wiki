"""Analyze link formats in index.md and find broken links."""
import re
from pathlib import Path
from collections import Counter

root = Path(r"C:\Users\Administrator\Desktop\wiki")
index_path = root / "30_wiki/index.md"
text = index_path.read_text(encoding="utf-8", errors="replace")
links = re.findall(r"\[\[([^\]]+)\]\]", text)
print(f"Total links in index.md: {len(links)}")

# Build vault name index
vault_stems = set()
for md in root.rglob("*.md"):
    if ".trash" in md.parts or ".obsidian" in md.parts or ".git" in md.parts:
        continue
    vault_stems.add(md.stem)
    vault_stems.add(md.name)

formats = Counter()
broken = []
backslash_links = []
forward_path_links = []

for raw in links:
    target = raw.split("|")[0].strip()
    # Detect backslash
    if "\\" in target:
        formats["backslash_path"] += 1
        backslash_links.append(target)
    elif "/" in target:
        formats["forward_slash_path"] += 1
        forward_path_links.append(target)
    elif target.endswith(".md"):
        formats["with_md_suffix"] += 1
    else:
        formats["bare_card_id"] += 1

    # Check if broken
    if target in vault_stems:
        continue
    if (root / target).exists():
        continue
    stem = target.rsplit("\\", 1)[-1].rsplit("/", 1)[-1].rsplit(".", 1)[0]
    if stem in vault_stems:
        continue
    broken.append(target)

for fmt, count in formats.most_common():
    print(f"  {fmt}: {count}")

print(f"\nBroken links: {len(broken)}")
print(f"Backslash links: {len(backslash_links)}")
print(f"Forward-slash path links: {len(forward_path_links)}")

if backslash_links:
    print("\nSample backslash links:")
    for t in backslash_links[:5]:
        print(f"  [[{t}]]")

if forward_path_links:
    print("\nSample forward-slash path links:")
    for t in forward_path_links[:5]:
        print(f"  [[{t}]]")

if broken:
    print("\nSample broken links:")
    for t in broken[:10]:
        print(f"  [[{t}]]")
