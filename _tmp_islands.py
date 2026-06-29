import re
from pathlib import Path
from collections import Counter

wiki = Path("30_wiki")
# Cards that have NO body wikilinks at all - these are pure islands
total = 0
no_links = 0
has_links = 0
link_counts = Counter()

for p in wiki.rglob("*.md"):
    if "_archive" in str(p):
        continue
    total += 1
    try:
        text = p.read_text(encoding="utf-8", errors="ignore")
    except:
        continue
    body_start = text.find("---", 3) + 3 if text.startswith("---") else 0
    body = text[body_start:]
    wiki_links = re.findall(r'\[\[([^\]|#]+)(?:[|#][^\]]+)?\]\]', body)
    if not wiki_links:
        no_links += 1
    else:
        has_links += 1
    link_counts[len(wiki_links)] += 1

print(f"Total cards: {total}")
print(f"Cards WITH body wikilinks: {has_links}")
print(f"Cards WITHOUT body wikilinks (ISLANDS): {no_links}")
print(f"Pct islands: {no_links/total*100:.1f}%")
print()
print("Body wikilink count distribution:")
for count, num_cards in sorted(link_counts.items(), key=lambda x: -x[1])[:25]:
    print(f"  {count} links: {num_cards} cards")
