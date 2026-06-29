import re, yaml
from pathlib import Path
from collections import Counter

# Collect ALL valid IDs in the vault
all_ids = set()
for d in ["30_wiki", "10_raw", "20_memory", "40_outputs", "50_delivery", "60_feedback", "70_product", "90_control", "00_inbox"]:
    dp = Path(d)
    if dp.exists():
        for p in dp.rglob("*.md"):
            all_ids.add(p.stem)
            # also handle paths like concepts/card-name
            rel = str(p.relative_to(dp).with_suffix(""))
            all_ids.add(rel)

print(f"Total valid IDs: {len(all_ids)}")

# Scan ALL files for broken wikilinks
broken = Counter()
files_with_broken = set()
total = 0

for d in ["30_wiki", "20_memory", "40_outputs", "70_product", "90_control"]:
    dp = Path(d)
    if not dp.exists():
        continue
    for p in dp.rglob("*.md"):
        if "_archive" in str(p):
            continue
        try:
            text = p.read_text(encoding="utf-8", errors="ignore")
        except:
            continue
        # Skip frontmatter
        body_start = 0
        if text.startswith("---"):
            end = text.find("---", 3)
            body_start = end + 3 if end > 0 else 0
        body = text[body_start:]
        
        links = re.findall(r'\[\[([^\]|#]+)(?:[|#][^\]]+)?\]\]', body)
        has_broken = False
        for link in links:
            total += 1
            link_id = link.split("/")[-1].strip()
            if link_id not in all_ids and link not in all_ids:
                broken[link] += 1
                has_broken = True
        if has_broken:
            files_with_broken.add(str(p.relative_to(Path("."))))

print(f"Total wikilinks scanned: {total}")
print(f"Unique broken targets: {len(broken)}")
print(f"Files with >=1 broken link: {len(files_with_broken)}")
print()
print("All broken targets:")
for link, count in broken.most_common():
    # Show the file too
    sources = [f for f in files_with_broken if link in open(f, encoding="utf-8", errors="ignore").read()]
    print(f"  {count}x [[{link[:100]}]]")
