"""扫描五步法子域卡片。"""
import re
from collections import defaultdict
from pathlib import Path

wiki = Path(r"C:\Users\Administrator\Desktop\wiki\30_wiki")
SUBDOMAINS = {
    "demand-analysis": [],
    "product": [],
    "business-model": [],
    "growth": [],
    "barrier": [],
}

for f in wiki.rglob("*.md"):
    if any(p in str(f) for p in ["_archive", "raw/", ".git"]): continue
    try: t = f.read_text(encoding="utf-8")[:2000]
    except: continue
    m = re.search(r'^id:\s*(.+)$', t, re.MULTILINE)
    if not m: continue
    cid = m.group(1)
    m2 = re.search(r'^domain:\s*\[(.*?)\]', t, re.MULTILINE)
    if not m2: m2 = re.search(r'^domain:\s*(.+)$', t, re.MULTILINE)
    doms = [d.strip().strip('"').strip("'") for d in m2.group(1).split(",")] if m2 else []
    m3 = re.search(r'^title:\s*(.+)$', t, re.MULTILINE)
    title = m3.group(1).strip().strip('"').strip("'")[:60] if m3 else ""
    m4 = re.search(r'^type:\s*(.+)$', t, re.MULTILINE)
    ctype = m4.group(1)[:15] if m4 else "?"

    for sd in SUBDOMAINS:
        if sd in doms:
            SUBDOMAINS[sd].append((cid, ctype, title))

for sd, cards in SUBDOMAINS.items():
    print(f"\n=== {sd}: {len(cards)} 张 ===")
    for cid, ctype, title in sorted(cards)[:30]:
        print(f"  [{ctype:12s}] {cid:50s} {title}")
