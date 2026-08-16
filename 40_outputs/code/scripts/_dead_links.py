import re
import sys
if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")
if hasattr(sys.stderr, "reconfigure"):
    sys.stderr.reconfigure(encoding="utf-8", errors="replace")
from collections import defaultdict
from pathlib import Path

wiki = Path(r"C:\Users\Administrator\Desktop\wiki\30_wiki")

# Build set of all card IDs and file paths
all_ids = set()
all_paths = {}  # stem -> first full path
for f in wiki.rglob("*.md"):
    if any(p in str(f) for p in ["_archive", "raw/", ".git"]):
        continue
    all_paths[f.stem] = f
    # Also check frontmatter for id field
    try:
        t = f.read_text(encoding="utf-8")[:2000]
        m = re.search(r'^id:\s*(.+)$', t, re.MULTILINE)
        if m:
            all_ids.add(m.group(1).strip())
    except:
        pass
    all_ids.add(f.stem)

dead_by_file = defaultdict(list)

for f in wiki.rglob("*.md"):
    if any(p in str(f) for p in ["_archive", "raw/", ".git"]):
        continue
    try:
        text = f.read_text(encoding="utf-8")
    except:
        continue
    # Extract [[target|...]] or [[target]]
    links = re.findall(r'\[\[([^\]|#]+)(?:\|[^\]]+)?(?:\#[^\]]+)?\]\]', text)
    # Also [text](path.md)
    mdlinks = re.findall(r'\[[^\]]*\]\(([^)#]+\.md[^)]*)\)', text)

    for link in links:
        target = link.strip()
        stem = Path(target).stem
        # Check by stem
        if stem in all_paths or stem in all_ids:
            continue
        # Check direct path
        direct = wiki / target
        if direct.with_suffix(".md").exists() or direct.exists():
            continue
        dead_by_file[f.relative_to(wiki)].append(target)

    for link in mdlinks:
        target = link.strip()
        resolved = (wiki / target).resolve()
        if resolved.exists():
            continue
        dead_by_file[f.relative_to(wiki)].append(target)

total_dead = sum(len(v) for v in dead_by_file.values())
print(f"死链总数: {total_dead} 分布在 {len(dead_by_file)} 个文件中")

# Show files with the most dead links
for relpath, links in sorted(dead_by_file.items(), key=lambda x: -len(x[1]))[:10]:
    print(f"\n{relpath} ({len(links)} dead):")
    for l in links[:5]:
        print(f"  [[{l}]]")
    if len(links) > 5:
        print(f"  ... +{len(links)-5} more")
