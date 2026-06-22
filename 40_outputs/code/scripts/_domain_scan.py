"""扫描所有域（含合并子域计数）。"""
import re
from collections import defaultdict
from pathlib import Path

wiki = Path(r"C:\Users\Administrator\Desktop\wiki\30_wiki")
domains = defaultdict(list)

for f in wiki.rglob("*.md"):
    if any(p in str(f) for p in ["_archive", "raw/", ".git", "index.md", "log.md"]):
        continue
    try:
        text = f.read_text(encoding="utf-8")[:2000]
    except:
        continue
    m = re.search(r'^id:\s*(.+)$', text, re.MULTILINE)
    if not m: continue
    cid = m.group(1).strip()
    m2 = re.search(r'^domain:\s*\[(.*?)\]', text, re.MULTILINE)
    if not m2:
        m2 = re.search(r'^domain:\s*(.+)$', text, re.MULTILINE)
    if not m2: continue
    for d in m2.group(1).strip().split(","):
        d = d.strip().strip('"').strip("'").strip("[") .strip("]").strip()
        if d and not d.startswith("-"):
            domains[d].append(cid)

for d, cards in sorted(domains.items(), key=lambda x: -len(x[1])):
    if len(cards) >= 5:
        print(f"{d:35s} {len(cards):4d}")
