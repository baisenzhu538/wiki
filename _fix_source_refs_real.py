"""Fix all broken source_refs — exact string replacement, git-diff verifiable."""
import yaml
from pathlib import Path

root = Path(r"C:\Users\Administrator\Desktop\wiki")
wiki = root / "30_wiki"

# Build fast filename index
src_filenames = set()
for f in (root / "10_raw/sources").glob("*"):
    if f.is_file(): src_filenames.add(f.name)
for f in (root / "00_inbox").rglob("*"):
    if f.is_file(): src_filenames.add(f.name)

fixes = {}
for md in wiki.rglob("*.md"):
    if ".trash" in md.parts:
        continue
    text = md.read_text(encoding="utf-8", errors="replace")
    text_u = text.replace("\r\n", "\n")
    end = text_u.find("\n---\n", 4)
    if end == -1: continue
    try: fm = yaml.safe_load(text_u[4:end])
    except: continue
    if not isinstance(fm, dict): continue
    refs = fm.get("source_refs", [])
    if not isinstance(refs, list): continue
    for ref in refs:
        if isinstance(ref, dict): continue
        rs = str(ref).strip()
        if not rs: continue
        if rs.startswith(("http", "pending_archive:", "src_unknown")): continue
        norm = rs.replace("\\", "/")
        if (root / norm).exists(): continue
        if Path(rs).name in src_filenames: continue
        fixes[str(md)] = fixes.get(str(md), []) + [rs]

n = 0
for path, refs in fixes.items():
    md = root / path
    raw = md.read_text(encoding="utf-8")
    for rs in refs:
        for old in [f"  - {rs}", f"- {rs}"]:
            if old in raw:
                raw = raw.replace(old, f"  - pending_archive:{rs}")
                n += 1
                break
    md.write_text(raw, encoding="utf-8")

print(f"Fixed {len(fixes)} files, {n} refs -> pending_archive")
