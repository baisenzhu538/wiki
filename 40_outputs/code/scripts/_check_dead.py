import re
from pathlib import Path

wiki = Path(r"C:\Users\Administrator\Desktop\wiki\30_wiki")
index = wiki / "index.md"
text = index.read_text(encoding="utf-8")

# Extract all wikilinks: [[path|display]] or [[id]] or [text](path)
wikilinks = re.findall(r'\[\[([^\]|]+)(?:\|[^\]]+)?\]\]', text)
mdlinks = re.findall(r'\[([^\]]+)\]\(([^)]+)\)', text)

dead = 0
alive = 0
for link in wikilinks:
    target = link.strip()
    # Try as direct path, or search by stem
    direct = wiki / target
    if direct.with_suffix(".md").exists() or direct.exists():
        alive += 1
        continue
    # Try just the filename
    stem = Path(target).stem
    matches = list(wiki.rglob(f"{stem}.md"))
    if matches:
        alive += 1
        continue
    dead += 1

for _, path in mdlinks:
    target = wiki / path
    if target.exists():
        alive += 1
    else:
        dead += 1

print(f"index.md 链接: alive={alive}, dead={dead}")
print(f"死链率: {dead}/{alive+dead} = {dead/(alive+dead)*100:.0f}%")
