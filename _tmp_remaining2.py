import yaml
from pathlib import Path

wiki = Path("30_wiki")
for p in wiki.rglob("*.md"):
    if "_archive" in str(p):
        continue
    try:
        text = p.read_text(encoding="utf-8", errors="ignore")
    except:
        continue
    if not text.startswith("---"):
        continue
    parts = text.split("---", 2)
    if len(parts) < 3:
        continue
    try:
        yaml.safe_load(parts[1])
    except Exception as e:
        rel = str(p.relative_to(wiki))
        print(f"STILL BROKEN: {rel}")
        print(f"  Error: {e}")
        # Show the frontmatter
        fm_lines = parts[1].split("\n")
        # Find problematic area
        for i, line in enumerate(fm_lines):
            if i < 3 or line.strip().startswith("source_refs") or line.strip().startswith("related") or line.strip().startswith("domain"):
                print(f"  L{i+1}: {line}")
        print()
