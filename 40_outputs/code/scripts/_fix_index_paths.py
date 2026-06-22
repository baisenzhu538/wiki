"""修复 index.md 中 1846 个路径错误的 wikilinks。"""
import re
from pathlib import Path

wiki = Path(r"C:\Users\Administrator\Desktop\wiki\30_wiki")
index = wiki / "index.md"
text = index.read_text(encoding="utf-8")

# Build: filename stem → correct relative path from 30_wiki/
stem_to_path = {}
for f in wiki.rglob("*.md"):
    if any(p in str(f) for p in ["_archive", "raw/", ".git"]):
        continue
    rel = str(f.relative_to(wiki)).replace("\\", "/")
    stem_to_path[f.stem] = rel

def fix_link(m):
    full = m.group(0)
    inner = m.group(1)
    display = m.group(2) if m.lastindex >= 2 else ""
    target_path = inner.strip()

    # Check by full path first
    direct = wiki / target_path
    if direct.exists():
        return full  # already correct

    # Check by stem
    stem = Path(target_path).stem
    if stem in stem_to_path:
        correct = stem_to_path[stem]
        if display:
            return f"[[{correct}|{display}]]"
        else:
            return f"[[{correct}]]"

    return full  # can't fix, leave as-is

# Match [[path|display]] or [[path]]
pattern = re.compile(r'\[\[([a-zA-Z0-9_\-/].+?\.md)(?:\|([^\]]+))?\]\]')
fixed_count = 0
unfixed = []

def replace_one(m):
    global fixed_count
    full = m.group(0)
    result = fix_link(m)
    if result != full:
        fixed_count += 1
    else:
        stem = Path(m.group(1).strip()).stem
        if stem not in stem_to_path:
            unfixed.append((m.group(1).strip(), stem))
    return result

new_text = pattern.sub(replace_one, text)

index.write_text(new_text, encoding="utf-8")
print(f"修复: {fixed_count} 个路径")
print(f"无法修复: {len(unfixed)} 个")
for path, stem in unfixed[:10]:
    print(f"  {path} -> stem={stem}")
