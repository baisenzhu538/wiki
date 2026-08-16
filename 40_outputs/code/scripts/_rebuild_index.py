"""将 index.md 从 1846 链超级枢纽重建成域级 MOC。"""
from pathlib import Path
import sys
if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")
if hasattr(sys.stderr, "reconfigure"):
    sys.stderr.reconfigure(encoding="utf-8", errors="replace")
import re
from datetime import datetime, timezone

wiki = Path(r"C:\Users\Administrator\Desktop\wiki\30_wiki")
index = wiki / "index.md"
text = index.read_text(encoding="utf-8")

# Keep frontmatter
end_fm = text.find("---", 3)
fm = text[:end_fm + 3]

# Discover all domain digests
digests = {}
for f in sorted(wiki.rglob("*-domain-digest.md")):
    dname = f.stem.replace("-domain-digest", "").replace("-", " ").title()
    rel = str(f.relative_to(wiki)).replace("\\", "/")
    digests[rel] = dname

# Group by domain
from collections import defaultdict
domains = defaultdict(list)
for f in wiki.rglob("*.md"):
    if any(p in str(f) for p in ["_archive", "raw/", ".git"]):
        continue
    rel = str(f.relative_to(wiki)).replace("\\", "/")
    if "index" in rel.lower() or "log" in rel.lower():
        continue
    try:
        t = f.read_text(encoding="utf-8")[:1000]
    except:
        continue
    m = re.search(r'^domain:\s*\[(.*?)\]', t, re.MULTILINE)
    if not m:
        m = re.search(r'^domain:\s*(.+)$', t, re.MULTILINE)
    if m:
        dom_value = m.group(1).strip()
        for d in dom_value.split(","):
            d = d.strip().strip('"').strip("'").strip("[").strip("]")
            if d:
                domains[d].append(rel)

# Build new body
now = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%S+00:00")
L = []  # lines

L.append("\n# Wiki Index\n")
L.append(f"_Last updated: {now}_\n")

# Domain digests first
L.append("## 域入口（Domain Digests）\n")
L.append("| 域 | 入口卡 |\n")
L.append("|---|---|\n")
for rel, name in sorted(digests.items()):
    stem = Path(rel).stem
    L.append(f"| {name} | [[{stem}]] |\n")

# Domain-level statistics
L.append("\n## 域统计\n")
L.append("| 域 | 卡片数 | 入口 |\n")
L.append("|---|---|---|\n")
for d, cards in sorted(domains.items(), key=lambda x: -len(x[1])):
    if d in ("", "[]", "master", "system"):
        continue
    if len(cards) < 5:
        continue
    digest_stem = f"{d}-domain-digest"
    digest_rel = f"domains/{digest_stem}.md"
    has_digest = digest_rel in digests
    if has_digest:
        L.append(f"| {d} | {len(cards)} | [[{digest_stem}]] |\n")
    else:
        L.append(f"| {d} | {len(cards)} | — |\n")

# Key control files
L.append("\n## 控制面板\n")
L.append("- [[concept-card-index-latest]] — 卡片全量表（自动生成）\n")
L.append("- [[links/index|links/index]] — 反向链接索引\n")
L.append("\n> 详细卡片列表见各域入口卡。域入口卡是 Obsidian 图谱中的枢纽节点。\n")

new_content = fm + "".join(L)
index.write_text(new_content, encoding="utf-8")
print(f"重建完成: 从 394KB 缩减为 {len(new_content.encode('utf-8'))/1024:.1f}KB")
print(f"链接自 1846 个 → {len(digests)} 个域入口")
