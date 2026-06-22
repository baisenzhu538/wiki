"""扫描所有域，输出卡片数排行。"""
import re
from collections import defaultdict
from pathlib import Path

wiki = Path(r"C:\Users\Administrator\Desktop\wiki\30_wiki")
domains = defaultdict(lambda: defaultdict(list))

for f in wiki.rglob("*.md"):
    if any(p in str(f) for p in ["_archive", "raw/", ".git", "index.md", "log.md"]):
        continue
    try:
        text = f.read_text(encoding="utf-8")[:2000]
    except:
        continue
    m = re.search(r'^id:\s*(.+)$', text, re.MULTILINE)
    if not m:
        continue
    cid = m.group(1).strip()
    m2 = re.search(r'^domain:\s*\[(.*?)\]', text, re.MULTILINE)
    if not m2:
        m2 = re.search(r'^domain:\s*(.+)$', text, re.MULTILINE)
    doms = []
    if m2:
        for d in m2.group(1).strip().split(","):
            d = d.strip().strip('"').strip("'").strip("[").strip("]").strip()
            if d and not d.startswith("- "):
                doms.append(d)
    m3 = re.search(r'^type:\s*(.+)$', text, re.MULTILINE)
    ctype = m3.group(1).strip() if m3 else "?"
    for d in doms:
        domains[d][ctype].append(cid)

# 排序输出
sorted_domains = sorted(domains.items(), key=lambda x: sum(len(v) for v in x[1].values()), reverse=True)
for d, types in sorted_domains:
    total = sum(len(v) for v in types.values())
    if total < 10:
        continue
    type_summary = " + ".join(f"{t}={len(v)}" for t, v in sorted(types.items(), key=lambda x: -len(x[1])))
    print(f"{d:30s} {total:4d} 卡  ({type_summary})")
