import re
from pathlib import Path

root = Path(r"C:\Users\Administrator\Desktop\wiki")

moves = [
    ("30_wiki/dk/dk-yitang-channel-exploration-traps.md",
     "30_wiki/dark-knowledges/dk-yitang-channel-exploration-traps.md"),
    ("30_wiki/frameworks/concept-yitang-channel-lean-validation-bridge.md",
     "30_wiki/concepts/concept-yitang-channel-lean-validation-bridge.md"),
]

replace = {}
for src_rel, dst_rel in moves:
    src_stem = Path(src_rel).stem
    dst_stem = Path(dst_rel).stem
    for old in [src_rel, src_rel.replace("/", "\\"), src_stem]:
        replace[old] = dst_stem

for src_rel, dst_rel in moves:
    src = root / src_rel
    dst = root / dst_rel
    dst.parent.mkdir(parents=True, exist_ok=True)
    src.rename(dst)
    print(f"Moved: {src_rel} -> {dst_rel}")

n = 0
for md in root.rglob("*.md"):
    if ".trash" in md.parts or ".obsidian" in md.parts or ".git" in md.parts:
        continue
    raw = md.read_text(encoding="utf-8", errors="replace")
    orig = raw
    for old, new in replace.items():
        if old in raw:
            raw = raw.replace(old, new)
    if raw != orig:
        md.write_text(raw, encoding="utf-8")
        n += 1
print(f"Wikilinks updated in {n} files")
