import yaml, re, os
from pathlib import Path
from collections import Counter

wiki = Path("30_wiki")
all_ids = set()
broken_links = Counter()
total_links = 0
cards_with_broken = 0
cards_no_related = 0
cards_src_unknown_related = 0

# First pass: collect all valid card IDs and their actual file paths
for p in wiki.rglob("*.md"):
    if "_archive" in str(p):
        continue
    all_ids.add(p.stem)

# Second pass: check every card's wikilinks
for p in wiki.rglob("*.md"):
    if "_archive" in str(p):
        continue
    try:
        text = p.read_text(encoding="utf-8", errors="ignore")
    except:
        continue
    # Check related field in frontmatter
    has_broken_in_card = False
    if text.startswith("---"):
        parts = text.split("---", 2)
        if len(parts) >= 3:
            try:
                fm = yaml.safe_load(parts[1])
                if fm and isinstance(fm, dict):
                    related = fm.get("related", [])
                    if not related:
                        cards_no_related += 1
                    elif isinstance(related, list):
                        # Check for src_unknown / pending_unknown
                        if any("unknown" in str(r).lower() for r in related):
                            cards_src_unknown_related += 1
                    # Check wikilinks
                    wikilinks = re.findall(r'\[\[([^\]|#]+)', parts[2]) if len(parts) >= 3 else []
                    for link in wikilinks:
                        total_links += 1
                        link_id = link.split("|")[0].strip()
                        if link_id not in all_ids:
                            broken_links[link_id] += 1
                            has_broken_in_card = True
            except:
                pass
    if has_broken_in_card:
        cards_with_broken += 1

print(f"Total unique card IDs: {len(all_ids)}")
print(f"Total wikilinks found: {total_links}")
print(f"Unique broken link targets: {len(broken_links)}")
print(f"Cards with >=1 broken link: {cards_with_broken}")
print(f"Cards with empty related: {cards_no_related}")
print(f"Cards with src_unknown in related: {cards_src_unknown_related}")
print()
print("Top 30 broken link targets:")
for link, count in broken_links.most_common(30):
    print(f"  {count}x [[{link}]]")
