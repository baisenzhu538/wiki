"""Check 老顽童 recent production — count cards by domain created/updated recently."""
import re
from pathlib import Path
from datetime import datetime, timedelta

wiki = Path(r"C:\Users\Administrator\Desktop\wiki\30_wiki")
cutoff = datetime(2026, 6, 23)

for domain_prefix in ["lean", "strategy", "cross"]:
    cards = []
    for f in wiki.rglob("*.md"):
        if any(p in str(f) for p in ["_archive", "raw/", ".git"]): continue
        try: t = f.read_text(encoding="utf-8")[:500]
        except: continue
        m = re.search(r'^id:\s*(.+)$', t, re.MULTILINE)
        if not m: continue
        cid = m.group(1).strip()
        if domain_prefix == "cross" and not cid.startswith("case-cross"): continue
        if domain_prefix == "lean" and not ("lean" in cid): continue
        if domain_prefix == "strategy" and not cid.startswith(("framework-strategy", "tool-strategy", "case-strategy", "dk-strategy", "concept-strategy")): continue
        m2 = re.search(r'^created_at:\s*"?(.+?)"?\s*$', t, re.MULTILINE)
        date_str = (m2.group(1) if m2 else "").strip().strip('"')
        m3 = re.search(r'^title:\s*(.+)$', t, re.MULTILINE)
        title = m3.group(1).strip().strip('"').strip("'")[:60] if m3 else ""
        m4 = re.search(r'^type:\s*(.+)$', t, re.MULTILINE)
        ctype = m4.group(1).strip() if m4 else "?"
        cards.append((cid, ctype, title, date_str))
    print(f"\n=== {domain_prefix}: {len(cards)} 张 ===")
    for cid, ctype, title, date in sorted(cards, key=lambda x: x[3] or "", reverse=True)[:30]:
        print(f"  [{ctype:12s}] [{date or '??':10s}] {cid:55s} {title}")
