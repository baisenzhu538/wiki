"""Taxonomy migration — optimized single-pass.
Step 1: dark-knowledge/dark_knowledge -> dk
Step 2: concepts/tool-*.md -> tools/ + wikilink update (single pass)
"""
import re, sys
from pathlib import Path

ROOT = Path(r"C:\Users\Administrator\Desktop\wiki")
WIKI = ROOT / "30_wiki"
APPLY = "--apply" in sys.argv
STEP = "step2" if "--step2" in sys.argv else "step1" if "--step1" in sys.argv else "all"


def step1():
    """dark-knowledge / dark_knowledge -> dk"""
    n = 0
    for md in WIKI.rglob("*.md"):
        if ".trash" in md.parts: continue
        raw = md.read_text(encoding="utf-8", errors="replace")
        text = raw.replace("\r\n", "\n")
        if not text.startswith("---\n"): continue
        end = text.find("\n---\n", 4)
        if end == -1: continue
        fm = text[4:end]
        if "type: dark-knowledge" not in fm and "type: dark_knowledge" not in fm:
            continue
        new_fm = re.sub(r"^type: dark[_\-]knowledge$", "type: dk", fm, flags=re.MULTILINE)
        if new_fm == fm: continue
        if APPLY:
            md.write_text("---\n" + new_fm + "\n---" + text[end+5:], encoding="utf-8")
        n += 1
    return n


def step2():
    """Move concepts/tool-*.md -> tools/, update wikilinks."""
    concepts = WIKI / "concepts"
    tools = WIKI / "tools"
    tools.mkdir(parents=True, exist_ok=True)

    tool_files = sorted(concepts.glob("tool-*.md"), key=lambda p: -len(p.stem))

    # Build stem->path map, sorted by key length descending
    stem_to_filename = {p.stem: p.name for p in tool_files}

    # Build replacement: old_text -> new_text (for in-wikilink replacement)
    replace = {}
    for p in tool_files:
        s, fn = p.stem, p.name
        for old in [f"concepts/{fn}", f"30_wiki/concepts/{fn}",
                     f"concepts/{s}", f"30_wiki/concepts/{s}", s]:
            replace[old] = s
            replace[old.replace("/", "\\")] = s

    def _sub_link(m):
        target = m.group(1)
        pipe = m.group(2) or ""
        clean = target.replace("\\", "/")
        if clean in replace:
            return f"[[{replace[clean]}{pipe}]]"
        return m.group(0)

    link_re = re.compile(r"\[\[([^\]|]+)(\|[^\]]+)?\]\]")

    # Move files
    moved = 0
    for p in tool_files:
        dst = tools / p.name
        if dst.exists():
            print(f"  SKIP (exists): {p.name}")
            continue
        if APPLY:
            p.rename(dst)
        moved += 1

    # Update wikilinks — iterate ALL vault files
    updated_files = 0
    if APPLY:
        for md in ROOT.rglob("*.md"):
            if ".trash" in md.parts or ".obsidian" in md.parts or ".git" in md.parts:
                continue
            raw = md.read_text(encoding="utf-8", errors="replace")
            new_raw = link_re.sub(_sub_link, raw)
            if new_raw != raw:
                md.write_text(new_raw, encoding="utf-8")
                updated_files += 1

    return moved, updated_files


m = "APPLY" if APPLY else "DRY RUN"

if STEP in ("step1", "all"):
    n = step1()
    print(f"Step 1 [{m}]: {n} cards type-unified (dark-knowledge/dark_knowledge -> dk)")
    if not APPLY: print("  (dry run — no changes)")

if STEP in ("step2", "all"):
    moved, updated = step2()
    print(f"Step 2 [{m}]: {moved} files moved, {updated} files wikilink-updated")
    if not APPLY: print("  (dry run — no changes)")

if not APPLY:
    print("\n  To apply: python _taxonomy_migrate.py --apply")
