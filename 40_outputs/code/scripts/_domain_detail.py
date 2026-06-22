"""某域的卡片详情（前 30 张）。"""
import re, sys
from pathlib import Path

domain = sys.argv[1] if len(sys.argv) > 1 else "ai-collaboration"
wiki = Path(r"C:\Users\Administrator\Desktop\wiki\30_wiki")

for f in wiki.rglob("*.md"):
    if any(p in str(f) for p in ["_archive", "raw/", ".git"]):
        continue
    try: text = f.read_text(encoding="utf-8")[:2000]
    except: continue
    m = re.search(r'^id:\s*(.+)$', text, re.MULTILINE)
    if not m: continue
    cid = m.group(1).strip()
    m2 = re.search(r'^domain:\s*\[(.*?)\]', text, re.MULTILINE)
    if not m2:
        m2 = re.search(r'^domain:\s*(.+)$', text, re.MULTILINE)
    doms = [d.strip().strip('"').strip("'") for d in m2.group(1).split(",")] if m2 else []
    if domain not in doms: continue
    m3 = re.search(r'^title:\s*(.+)$', text, re.MULTILINE)
    title = m3.group(1).strip().strip('"').strip("'") if m3 else ""
    m4 = re.search(r'^type:\s*(.+)$', text, re.MULTILINE)
    ctype = m4.group(1).strip() if m4 else "?"
    conf = ""
    m5 = re.search(r'^confidence:\s*(.+)$', text, re.MULTILINE)
    if m5: conf = f"conf={m5.group(1).strip()}"
    print(f"[{ctype:12s}] {cid:50s} {title[:60]:60s} {conf}")
