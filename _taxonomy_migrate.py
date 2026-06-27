"""Taxonomy migration: Step 1 (type unification) + Step 2 (directory migration).

Step 1: dark-knowledge / dark_knowledge -> dk  (frontmatter only, no path change)
Step 2: concepts/tool-*.md -> tools/           (path change + wikilink update)
"""

import re
import sys
from pathlib import Path

ROOT = Path(r"C:\Users\Administrator\Desktop\wiki")
WIKI = ROOT / "30_wiki"
DRY_RUN = "--apply" not in sys.argv

INTERNAL_LINK_RE = re.compile(r"\[\[([^\]]+)\]\]")


def step1_unify_types():
    """Unify dark-knowledge / dark_knowledge -> dk in frontmatter type field."""
    count = 0
    for md in WIKI.rglob("*.md"):
        if ".trash" in md.parts:
            continue
        raw = md.read_text(encoding="utf-8", errors="replace")
        raw_unix = raw.replace("\r\n", "\n")
        if not raw_unix.startswith("---\n"):
            continue
        end = raw_unix.find("\n---\n", 4)
        if end == -1:
            continue
        fm_text = raw_unix[4:end]
        body = raw_unix[end + 5:]

        # Check if type field needs unification
        new_fm_lines = []
        changed = False
        for line in fm_text.split("\n"):
            stripped = line.strip()
            if stripped in ("type: dark-knowledge", "type: dark_knowledge"):
                new_fm_lines.append("type: dk")
                changed = True
            else:
                new_fm_lines.append(line)

        if not changed:
            continue

        new_content = "---\n" + "\n".join(new_fm_lines) + "\n---" + body
        if not DRY_RUN:
            md.write_text(new_content, encoding="utf-8")
        count += 1

    return count


def step2_migrate_files():
    """Move concepts/tool-*.md -> tools/ and update all wikilinks."""
    concepts_dir = WIKI / "concepts"
    tools_dir = WIKI / "tools"
    tools_dir.mkdir(parents=True, exist_ok=True)

    # Collect files to move, sorted by id length descending for safe replacement
    moves = []
    for md in concepts_dir.glob("tool-*.md"):
        moves.append((md.name, md.stem, md))

    # Sort by stem length descending to prevent partial match
    moves.sort(key=lambda x: -len(x[1]))

    # Build replacement map: old_target -> new_target
    # old_target can be: concepts/tool-xxx.md, 30_wiki/concepts/tool-xxx.md, tool-xxx
    replacements = {}
    for filename, stem, _ in moves:
        old_patterns = [
            f"concepts/{filename}",
            f"30_wiki/concepts/{filename}",
            f"concepts/{stem}",
            f"30_wiki/concepts/{stem}",
            f"{stem}",  # bare id
        ]
        for old in old_patterns:
            replacements[old] = stem  # new target = bare id
        # Also handle backslash variants
        for old in list(replacements.keys()):
            replacements[old.replace("/", "\\")] = stem

    # Move files first
    moved = 0
    for filename, stem, md in moves:
        dst = tools_dir / filename
        if dst.exists():
            print(f"  CONFLICT: {md.name} already exists in tools/ — skipping")
            continue
        if not DRY_RUN:
            md.rename(dst)
        moved += 1

    # Update wikilinks in all remaining files
    updated_files = 0
    updated_refs = 0
    for md in ROOT.rglob("*.md"):
        if ".trash" in md.parts or ".obsidian" in md.parts or ".git" in md.parts:
            continue
        raw = md.read_text(encoding="utf-8", errors="replace")
        original = raw

        for old_target, new_target in replacements.items():
            # Match [[old_target]] or [[old_target|alias]]
            pattern = re.escape(old_target)
            raw = re.sub(
                rf"\[\[{pattern}(\|.*?)?\]\]",
                lambda m, nt=new_target: f"[[{nt}{m.group(1) or ''}]]",
                raw,
            )

        if raw != original:
            updated_files += 1
            updated_refs += len(re.findall(r"\[\[([^\]]+)\]\]", original)) - len(
                re.findall(r"\[\[([^\]]+)\]\]", raw)
            )
            updated_refs = abs(updated_refs)  # avoid negative
            if not DRY_RUN:
                md.write_text(raw, encoding="utf-8")

    return moved, updated_files


def main():
    step = sys.argv[1] if len(sys.argv) > 1 else "all"
    mode = "DRY RUN" if DRY_RUN else "APPLY"

    if step in ("step1", "all"):
        print(f"\n{'='*60}")
        print(f"  STEP 1: Type unification (dark-knowledge/dark_knowledge -> dk)")
        print(f"  Mode: {mode}")
        print(f"{'='*60}")
        n = step1_unify_types()
        print(f"  Cards modified: {n}")
        if DRY_RUN:
            print(f"  (dry run — no changes written)")

    if step in ("step2", "all"):
        print(f"\n{'='*60}")
        print(f"  STEP 2: Directory migration (concepts/tool-*.md -> tools/)")
        print(f"  Mode: {mode}")
        print(f"{'='*60}")
        moved, updated = step2_migrate_files()
        print(f"  Files moved: {moved}")
        print(f"  Files with updated wikilinks: {updated}")
        if DRY_RUN:
            print(f"  (dry run — no changes written)")

    if DRY_RUN:
        print(f"\n  To apply: python _taxonomy_migrate.py --apply")


if __name__ == "__main__":
    main()
