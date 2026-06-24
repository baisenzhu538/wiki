"""Scan all business-model-related cards in vault."""
import re
from pathlib import Path

wiki = Path(r"C:\Users\Administrator\Desktop\wiki\30_wiki")

BUSINESS_MODEL_KEYWORDS = [
    "unit.model", "unit-economics", "单元模型", "unit.economic",
    "business.model", "商业模型", "商业模式",
    "profit.model", "盈利模式", "profit-model",
    "pricing", "定价",
    "revenue.model", "收入模型",
    "channel.economics", "渠道经济",
    "scalability", "规模经济",
    "business.formula", "业务公式",
]

def is_bm_card(cid, title, ctype, doms_str, fpath):
    """Heuristic: does this card belong to business-model domain?"""
    # Check ID prefix
    if any(kw in cid.lower() for kw in ["unit-model", "business-model", "profit-model", "pricing",
                                           "unit.model", "unit.economic", "channel.economic"]):
        return True
    # Check title
    for kw in BUSINESS_MODEL_KEYWORDS:
        if kw in title:
            return True
    # Check file path
    if "unit-model" in fpath or "business-model" in fpath:
        return True
    return False

cards = []
for f in wiki.rglob("*.md"):
    if any(p in str(f) for p in ["_archive", "raw/", ".git", "index.md", "log.md"]):
        continue
    try: t = f.read_text(encoding="utf-8")[:2000]
    except: continue
    m = re.search(r'^id:\s*(.+)$', t, re.MULTILINE)
    if not m: continue
    cid = m.group(1).strip()
    m2 = re.search(r'^title:\s*(.+)$', t, re.MULTILINE)
    title = m2.group(1).strip().strip('"').strip("'")[:80] if m2 else ""
    m3 = re.search(r'^type:\s*(.+)$', t, re.MULTILINE)
    ctype = m3.group(1).strip() if m3 else "?"
    m4 = re.search(r'^domain:\s*\[(.*?)\]', t, re.MULTILINE)
    if not m4: m4 = re.search(r'^domain:\s*(.+)$', t, re.MULTILINE)
    doms = m4.group(1).strip() if m4 else ""
    fpath = str(f.relative_to(wiki)).replace("\\", "/")
    if is_bm_card(cid, title, ctype, doms, fpath):
        cards.append((cid, ctype, title[:60], doms[:40], fpath))

print(f"Total BM-related cards: {len(cards)}\n")
by_type = {}
for cid, ctype, title, doms, fpath in sorted(cards):
    by_type.setdefault(ctype, []).append((cid, title, doms, fpath))
for ctype, items in sorted(by_type.items()):
    print(f"## {ctype} ({len(items)})")
    for cid, title, doms, fpath in items:
        print(f"  [{doms:30s}] {cid:55s} {title}")
