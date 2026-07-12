"""Add yt-entrepreneur-unit-model backlinks to 6 same-family cards"""
from pathlib import Path
VAULT = Path(__file__).resolve().parent.parent.parent

targets = [
    ("30_wiki/concepts/concept-最简单元模型.md", "concept-最简单元模型"),
    ("30_wiki/frameworks/yt-tob-unit-model.md", "yt-tob-unit-model"),
    ("30_wiki/tools/tool-单元模型-单商圈.md", "tool-单元模型-单商圈"),
    ("30_wiki/tools/tool-单元模型-单城市.md", "tool-单元模型-单城市"),
    ("30_wiki/tools/tool-单元模型-壁垒预判.md", "tool-单元模型-壁垒预判"),
    ("30_wiki/tools/tool-单元模型-象限分析法.md", "tool-单元模型-象限分析法"),
]

for path, name in targets:
    f = VAULT / path
    c = f.read_text(encoding="utf-8")

    # Check if backlink already exists
    if "yt-entrepreneur-unit-model" in c.split("---", 2)[1]:
        print(f"{name}: already has backlink, skip")
        continue

    lines = c.splitlines()
    # Find last related line in frontmatter
    fm_end = 0
    for i, l in enumerate(lines):
        if l.strip() == "---" and i > 0:
            fm_end = i
            break

    last_related = -1
    for i in range(fm_end):
        l = lines[i].strip()
        if l.startswith("-") and ("[[" in l):
            last_related = i

    if last_related < 0:
        print(f"{name}: no related list found, skip")
        continue

    # Match quote style
    if "'" in lines[last_related]:
        new_entry = f"  - '[[yt-entrepreneur-unit-model]]'"
    else:
        new_entry = f'  - "[[yt-entrepreneur-unit-model]]"'

    lines.insert(last_related + 1, new_entry)
    f.write_text("\n".join(lines), encoding="utf-8")
    print(f"{name}: added backlink")

print("Done")
