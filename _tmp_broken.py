import re
from pathlib import Path
from collections import Counter

wiki = Path("30_wiki")
# Collect all valid card IDs
all_ids = set()
for p in wiki.rglob("*.md"):
    if "_archive" in str(p):
        continue
    all_ids.add(p.stem)

# Also collect from 10_raw, 20_memory, 40_outputs, etc.
for d in ["10_raw", "20_memory", "40_outputs", "50_delivery", "60_feedback", "70_product", "90_control", "00_inbox"]:
    dp = Path(d)
    if dp.exists():
        for p in dp.rglob("*.md"):
            all_ids.add(p.stem)

print(f"Total valid IDs in vault: {len(all_ids)}")

# Check body wikilinks for broken targets
broken_body_links = Counter()
total_body_links = 0
cards_with_broken_body = 0

for p in wiki.rglob("*.md"):
    if "_archive" in str(p) or "raw/ocr" in str(p):
        continue
    try:
        text = p.read_text(encoding="utf-8", errors="ignore")
    except:
        continue
    body_start = text.find("---", 3) + 3 if text.startswith("---") else 0
    body = text[body_start:]
    wiki_links = re.findall(r'\[\[([^\]|#]+)(?:[|#][^\]]+)?\]\]', body)
    has_broken = False
    for link in wiki_links:
        total_body_links += 1
        link_id = link.split("/")[-1].strip()  # handle paths like concepts/yt-model
        if link_id not in all_ids and link not in all_ids:
            broken_body_links[link] += 1
            has_broken = True
    if has_broken:
        cards_with_broken_body += 1

print(f"Total body wikilinks: {total_body_links}")
print(f"Broken body link targets: {len(broken_body_links)}")
print(f"Cards with broken body links: {cards_with_broken_body}")
print()
print("Top 40 broken body link targets:")
for link, count in broken_body_links.most_common(40):
    print(f"  {count}x [[{link[:80]}]]")
