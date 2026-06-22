"""修复调研域死链 —— 覆盖 YAML related 和正文 wikilinks。"""
import re
from pathlib import Path

REMAP = {
    "dk-yitang-research-novice-vs-veteran": "dk-yitang-research-starter-vs-veteran",
    "dk-yitang-research-survivorship-bias": "dk-yitang-survivor-bias-in-research",
    "dk-yitang-research-expert-trap": "dk-yitang-expert-interview-5-traps",
}

wiki = Path(r"C:\Users\Administrator\Desktop\wiki\30_wiki")

# Build all known IDs
known_ids = set()
for f in wiki.rglob("*.md"):
    if any(p in str(f) for p in ["_archive", "raw/", ".git"]):
        continue
    known_ids.add(f.stem)
    try:
        t = f.read_text(encoding="utf-8")[:1000]
        m = re.search(r'^id:\s*(.+)$', t, re.MULTILINE)
        if m:
            known_ids.add(m.group(1).strip())
    except:
        pass

# Scan for dead links
all_dead = set()
for f in wiki.rglob("*.md"):
    if any(p in str(f) for p in ["_archive", "raw/", ".git"]):
        continue
    text = f.read_text(encoding="utf-8")
    links = re.findall(r'\[\[([^\]|#]+)(?:\|[^\]]+)?\]\]', text)
    for link in links:
        stem = Path(link.strip()).stem
        if stem not in known_ids and not (wiki / link.strip()).with_suffix(".md").exists():
            all_dead.add(stem)

print(f"唯一死链 ID: {len(all_dead)}")

# Fix them
fixed = 0
removed = 0
files_touched = set()

for f in wiki.rglob("*.md"):
    if any(p in str(f) for p in ["_archive", "raw/", ".git"]):
        continue
    text = f.read_text(encoding="utf-8")
    modified = False
    for dead_id in sorted(all_dead, key=len, reverse=True):
        if dead_id not in text:
            continue
        if dead_id in REMAP:
            text = text.replace(f"[[{dead_id}]]", f"[[{REMAP[dead_id]}]]")
            text = text.replace(f"[[{dead_id}|", f"[[{REMAP[dead_id]}|")
            # In related: field
            text = re.sub(rf"^(\s*-?\s*'?)\[{dead_id}\]", rf"\1[{REMAP[dead_id]}]", text, flags=re.MULTILINE)
            fixed += text.count(f"[[{REMAP[dead_id]}]]") - (0 if dead_id not in text else 0)
        else:
            # Remove whole line if it's just a wikilink + metadata
            text = re.sub(rf"^- \[\[{re.escape(dead_id)}(?:\|[^\]]+)?\]\].*$\n", "", text, flags=re.MULTILINE)
            # Remove inline wikilinks (keep surrounding text)
            text = re.sub(rf"\[\[{re.escape(dead_id)}(?:\|[^\]]+)?\]\]", f"（{dead_id}，待补）", text)
            text = re.sub(rf"^(\s*-?\s*'?)\[{re.escape(dead_id)}(?:\|[^\]]+)?\]'?\s*\n", "", text, flags=re.MULTILINE)
        modified = True
    if modified:
        f.write_text(text, encoding="utf-8")
        files_touched.add(str(f.relative_to(wiki)))

removed = sum(1 for dead_id in all_dead if dead_id not in REMAP and any(
    dead_id in f.read_text(encoding="utf-8") for f in wiki.rglob("*.md")
))
print(f"修复文件: {len(files_touched)}")
print(f"  - 已重映射: {len(REMAP)} 个 ID")
print(f"  - 已移除/标记的剩余死链: {len(all_dead) - len(REMAP)} 个 ID")
