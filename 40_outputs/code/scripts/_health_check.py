"""Obsidian vault 健康度综合评估"""
import re, json
import sys
if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")
if hasattr(sys.stderr, "reconfigure"):
    sys.stderr.reconfigure(encoding="utf-8", errors="replace")
from collections import defaultdict
from pathlib import Path

wiki = Path(r"C:\Users\Administrator\Desktop\wiki\30_wiki")

# 1. 扫描所有卡片
cards = []
orphans = []
for f in wiki.rglob("*.md"):
    if any(p in str(f) for p in ["_archive", "raw/", ".git", "index.md", "log.md"]):
        continue
    try:
        text = f.read_text(encoding="utf-8")
    except:
        continue
    fm = {}
    if text.startswith("---"):
        end = text.find("---", 3)
        if end != -1:
            for line in text[3:end].split("\n"):
                if ":" in line:
                    k, _, v = line.partition(":")
                    v = v.strip().strip('"').strip("'")
                    fm[k.strip()] = v
    if "id" not in fm:
        continue
    fm["_path"] = str(f.relative_to(wiki)).replace("\\", "/")
    cards.append(fm)

# 2. 构建网络
all_ids = {c["id"] for c in cards}
all_paths = {c["_path"]: c["id"] for c in cards}
stem_to_ids = {}
for c in cards:
    stem_to_ids[Path(c["_path"]).stem] = c["id"]

incoming = defaultdict(int)
outgoing = defaultdict(int)
dead_links = 0
total_links = 0

for f in wiki.rglob("*.md"):
    if any(p in str(f) for p in ["_archive", "raw/", ".git"]):
        continue
    text = f.read_text(encoding="utf-8")
    rel = str(f.relative_to(wiki)).replace("\\", "/")
    source_id = None
    for c in cards:
        if c["_path"] == rel:
            source_id = c["id"]
            break
    links = re.findall(r'\[\[([^\]|#]+)(?:\|[^\]]+)?\]\]', text)
    for link in links:
        target = link.strip()
        stem = Path(target).stem
        total_links += 1
        if stem in stem_to_ids:
            target_id = stem_to_ids[stem]
            outgoing[source_id or rel] += 1
            incoming[target_id] += 1
        else:
            dead_links += 1

# 3. 统计
total = len(cards)
no_incoming = [c for c in cards if incoming[c["id"]] == 0]
no_outgoing = [c for c in cards if outgoing.get(c["id"], 0) == 0]
isolated = [c for c in cards if incoming[c["id"]] == 0 and outgoing.get(c["id"], 0) == 0]

by_type = defaultdict(int)
by_domain = defaultdict(int)
by_status = defaultdict(int)
no_domain = 0
for c in cards:
    by_type[c.get("type", "?")] += 1
    d = c.get("domain", "")
    if not d or d == "[]":
        no_domain += 1
    else:
        for dd in d.strip("[]").split(","):
            by_domain[dd.strip().strip('"').strip("'")] += 1
    by_status[c.get("status", "?")] += 1

# 4. 域间连通性（跨域桥接数）
cross_domain_edges = 0
# Simplified: count related links between different domains
domain_of = {c["id"]: c.get("domain", "") for c in cards}

print("=" * 50)
print("KDO Vault 健康度报告")
print("=" * 50)
print(f"\n## 基础数据")
print(f"卡片总数: {total}")
print(f"总链接数: {total_links}")
print(f"死链数: {dead_links} ({dead_links/max(total_links,1)*100:.1f}%)")
print(f"孤立卡（无入无出）: {len(isolated)}")
print(f"无入链卡: {len(no_incoming)}")
print(f"无出链卡: {len(no_outgoing)}")

print(f"\n## 类型分布")
for t, n in sorted(by_type.items(), key=lambda x: -x[1]):
    print(f"  {t}: {n}")

print(f"\n## 状态分布")
for s, n in sorted(by_status.items(), key=lambda x: -x[1]):
    print(f"  {s}: {n}")

print(f"\n## 域 Top 15")
for d, n in sorted(by_domain.items(), key=lambda x: -x[1])[:15]:
    cards_in_domain = sum(1 for c in cards if d in c.get("domain", ""))
    print(f"  {d}: {n}")

print(f"\n## 质量指标")
draft_pct = by_status.get("draft", 0) / total * 100
print(f"draft 率: {draft_pct:.1f}%")
print(f"死链率: {dead_links/max(total_links,1)*100:.1f}%")
print(f"孤立率: {len(isolated)/total*100:.1f}%")
print(f"缺域率: {no_domain/total*100:.1f}%")

# 健康度评分
score = 100
if dead_links > total_links * 0.05: score -= 20
elif dead_links > total_links * 0.01: score -= 10
if len(isolated) > total * 0.10: score -= 15
elif len(isolated) > total * 0.05: score -= 8
if draft_pct > 50: score -= 10
elif draft_pct > 30: score -= 5
if no_domain / total > 0.10: score -= 10
print(f"\n## 综合健康度: {score}/100")
if score >= 90: print("🟢 健康")
elif score >= 75: print("🟡 亚健康")
elif score >= 60: print("🟠 需关注")
else: print("🔴 需干预")
