#!/usr/bin/env python3
"""Post-process kdo index --rebuild output to fix wikilink format.

Fixes:
- 30_wiki/index.md           : strip `.md` suffix / `30_wiki/` prefix / backslashes
- 30_wiki/links/index.md     : strip `.md` suffix / `30_wiki/` prefix / backslashes

Target format:
- [[path/file]] or [[path/file|alias]]
- forward slashes only
- no leading `30_wiki/`
- no trailing `.md` (preserves `#heading` / `^block` anchors)

UTF-8 is used for all reads/writes to protect CJK filenames.
"""
from __future__ import annotations

import re
import sys
from pathlib import Path

WIKI_DIR = "30_wiki"
INDEX_FILE = Path(WIKI_DIR) / "index.md"
LINKS_FILE = Path(WIKI_DIR) / "links" / "index.md"

WIKILINK_RE = re.compile(r"\[\[([^\]]+)\]\]")
PREFIX_RE = re.compile(r"^30_wiki[/\\]", re.IGNORECASE)


def split_target_anchor(target: str) -> tuple[str, str]:
    """Split `path/file.md#heading` into (`path/file.md`, `#heading`)."""
    anchor_match = re.search(r"[#^].*", target)
    if anchor_match:
        return target[: anchor_match.start()], anchor_match.group(0)
    return target, ""


def normalize_target(raw_target: str) -> str:
    t = raw_target.replace("\\", "/").strip()
    # Remove leading /, ./, and 30_wiki/ (case-insensitive)
    t = re.sub(r"^(?:\.?/)+", "", t)
    t = PREFIX_RE.sub("", t)

    base, anchor = split_target_anchor(t)
    # Remove trailing .md from the file part only
    if base.lower().endswith(".md"):
        base = base[:-3]

    return base + anchor


def fix_one_link(match: re.Match) -> str:
    inner = match.group(1)
    if "|" in inner:
        target, alias = inner.split("|", 1)
        target = target.strip()
        alias = alias.strip()
        new_target = normalize_target(target)
        if new_target != target:
            return f"[[{new_target}|{alias}]]"
        return match.group(0)
    else:
        target = inner.strip()
        new_target = normalize_target(target)
        if new_target != target:
            return f"[[{new_target}]]"
        return match.group(0)


def fix_file(path: Path) -> tuple[int, list[tuple[str, str]]]:
    text = path.read_text(encoding="utf-8")
    changed: list[tuple[str, str]] = []

    def repl(m: re.Match) -> str:
        original = m.group(0)
        fixed = fix_one_link(m)
        if fixed != original:
            changed.append((original, fixed))
        return fixed

    new_text = WIKILINK_RE.sub(repl, text)
    if new_text != text:
        path.write_text(new_text, encoding="utf-8")
    return len(changed), changed


def main() -> int:
    root = Path.cwd()
    index_path = root / INDEX_FILE
    links_path = root / LINKS_FILE

    if not index_path.exists():
        print(f"ERROR: {index_path} not found", file=sys.stderr)
        return 1
    if not links_path.exists():
        print(f"ERROR: {links_path} not found", file=sys.stderr)
        return 1

    idx_count, idx_changes = fix_file(index_path)
    links_count, links_changes = fix_file(links_path)

    print(f"Fixed {idx_count} wikilink(s) in {index_path}")
    for old, new in idx_changes[:5]:
        print(f"  {old} -> {new}")

    print(f"Fixed {links_count} wikilink(s) in {links_path}")
    for old, new in links_changes[:5]:
        print(f"  {old} -> {new}")

    return 0


if __name__ == "__main__":
    sys.exit(main())
