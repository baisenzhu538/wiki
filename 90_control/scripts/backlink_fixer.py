#!/usr/bin/env python3
"""
F2 auto-backlink --fix — 自动补全缺失的双向回链。

用法:
  python backlink_fixer.py                    # dry-run: 扫描 F2 缺回链，出 diff 不落盘
  python backlink_fixer.py --apply            # 执行修复 + 输出 touched-files manifest
  python backlink_fixer.py --files f1.md f2.md  # 只修复指定文件的缺回链

欧阳锋四条前置条件（全满足）：
  ① 默认 dry-run 出 diff，--apply 才落笔
  ② 只动 related 行，不碰正文
  ③ 遵守 .lint_exceptions.json 例外清单
  ④ --apply 模式输出 touched-files manifest
"""

import argparse
import json
import re
import subprocess
import sys
from collections import defaultdict
from pathlib import Path

VAULT_ROOT = Path(__file__).resolve().parent.parent.parent
LINT_SCRIPT = Path(__file__).resolve().parent / "kdo_lint.py"
EXCEPTIONS_FILE = VAULT_ROOT / "90_control" / ".lint_exceptions.json"
MANIFEST_FILE = VAULT_ROOT / "90_control" / ".backlink_fixer_manifest.txt"


def load_exceptions() -> dict:
    if not EXCEPTIONS_FILE.exists():
        return {}
    try:
        return json.loads(EXCEPTIONS_FILE.read_text(encoding="utf-8"))
    except Exception:
        return {}


def match_glob(pattern: str, value: str) -> bool:
    import fnmatch
    if not pattern or pattern == "*":
        return True
    return fnmatch.fnmatch(value, pattern)


def is_exempted(from_card: str, to_card: str, exceptions: dict) -> bool:
    for rule in exceptions.get("f2_missing", []):
        if match_glob(rule.get("from", "*"), from_card) and match_glob(rule.get("to", "*"), to_card):
            return True
    return False


def get_f2_missing_backlinks() -> list[tuple[str, str]]:
    """Run lint --incremental, extract F2 MISSING BACKLINK pairs."""
    try:
        result = subprocess.run(
            [sys.executable, str(LINT_SCRIPT), "--incremental", "--json"] if False else
            [sys.executable, str(LINT_SCRIPT), "--incremental"],
            capture_output=True, text=True, timeout=120,
            cwd=str(VAULT_ROOT), encoding="utf-8", errors="replace",
        )
        output = result.stdout + result.stderr
    except Exception as e:
        print(f"ERROR: lint failed: {e}", file=sys.stderr)
        sys.exit(1)

    pairs = []
    for line in output.splitlines():
        # "F2 MISSING BACKLINK: A → B (target has no backlink to A)"
        m = re.search(r"F2 MISSING BACKLINK:\s*(\S+)\s*→\s*(\S+)", line)
        if m:
            pairs.append((m.group(1), m.group(2)))
    return pairs


def find_card_file(card_id: str) -> Path | None:
    """Given a card id, find its .md file in 30_wiki/."""
    search_dirs = ["concepts", "frameworks", "tools", "cases", "methods", "systems", "operations", "dark-knowledges"]
    for d in search_dirs:
        for f in (VAULT_ROOT / "30_wiki" / d).rglob("*.md"):
            # match by filename stem or frontmatter id
            if f.stem == card_id:
                return f
            try:
                content = f.read_text(encoding="utf-8", errors="replace")
                m = re.match(r"^---\s*\n.*?\nid:\s*(\S+).*?\n---", content, re.DOTALL)
                if m and m.group(1).strip().strip("'\"") == card_id:
                    return f
            except Exception:
                continue
    return None


def add_backlink_to_file(filepath: Path, backlink_id: str) -> bool:
    """Add [[backlink_id]] to the card's related list in frontmatter. Returns True if changed."""
    try:
        content = filepath.read_text(encoding="utf-8")
    except Exception:
        return False

    # Find frontmatter
    fm_match = re.match(r"^(---\s*\n.*?\n---)", content, re.DOTALL)
    if not fm_match:
        return False
    fm_block = fm_match.group(1)
    rest = content[len(fm_block):]

    # Check if backlink already exists
    if backlink_id in fm_block:
        return False

    # Format the new entry — match existing quote style
    if "'[[" in fm_block:
        new_entry = f"  - '[[{backlink_id}]]'"
    elif '"' in fm_block and '[[' in fm_block:
        new_entry = f'  - "[[{backlink_id}]]"'
    else:
        new_entry = f"  - '[[{backlink_id}]]'"

    # Insert after the last line of the related list
    # Find `related:` and all subsequent list items
    lines = fm_block.splitlines()
    related_idx = None
    for i, line in enumerate(lines):
        if re.match(r"^related:\s*", line):
            related_idx = i
            break

    if related_idx is None:
        # No related field — add one before closing ---
        insert_at = len(lines) - 1  # before closing ---
        lines.insert(insert_at, "related:")
        lines.insert(insert_at + 1, new_entry)
    else:
        # Find the last related list item
        last_related = related_idx
        for i in range(related_idx + 1, len(lines)):
            if re.match(r"^\s+-\s+", lines[i]):
                last_related = i
            elif lines[i].strip() and not lines[i].startswith(" "):
                break
        lines.insert(last_related + 1, new_entry)

    new_fm = "\n".join(lines)
    new_content = new_fm + rest

    try:
        filepath.write_text(new_content, encoding="utf-8")
        return True
    except Exception:
        return False


def compute_diff(filepath: Path, backlink_id: str) -> str:
    """Preview what would change — returns human-readable diff string."""
    try:
        content = filepath.read_text(encoding="utf-8")
    except Exception:
        return f"  (cannot read {filepath})"

    fm_match = re.match(r"^(---\s*\n.*?\n---)", content, re.DOTALL)
    if not fm_match:
        return f"  (no frontmatter in {filepath})"
    fm_block = fm_match.group(1)

    if backlink_id in fm_block:
        return f"  (already has backlink to {backlink_id})"

    # Show the last line of related list and the new line
    lines = fm_block.splitlines()
    last_related_line = ""
    for i, line in enumerate(lines):
        if re.match(r"^\s+-\s+", line):
            last_related_line = line

    if "'[[" in fm_block:
        new_line = f"  - '[[{backlink_id}]]'"
    else:
        new_line = f"  - '[[{backlink_id}]]'"

    return f"  + {new_line}\n    (after: {last_related_line.strip()[:60]})"


def main():
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")

    parser = argparse.ArgumentParser(description="F2 auto-backlink --fix")
    parser.add_argument("--apply", action="store_true", help="执行修复（默认 dry-run）")
    parser.add_argument("--files", nargs="*", help="只修复指定文件的缺回链")
    args = parser.parse_args()

    exceptions = load_exceptions()
    all_pairs = get_f2_missing_backlinks()

    # Filter: exempted pairs
    pairs = [(frm, to) for frm, to in all_pairs if not is_exempted(frm, to, exceptions)]

    if args.files:
        file_set = {f.replace("\\", "/").rstrip("/") for f in args.files}
        pairs = [(frm, to) for frm, to in pairs
                 if any(f in frm or f in to for f in file_set)]

    if not pairs:
        print("No F2 missing backlinks to fix.")
        sys.exit(0)

    # Group by target card (the one that needs the backlink added)
    by_target: dict[str, list[str]] = defaultdict(list)
    for frm, to in pairs:
        by_target[to].append(frm)

    print("=" * 55)
    mode = "DRY-RUN" if not args.apply else "APPLY"
    print(f"F2 Auto-Backlink Fixer — {mode}")
    print("=" * 55)
    print(f"  Missing backlinks: {len(pairs)}")
    print(f"  Target cards:      {len(by_target)}")
    print(f"  Exempted:          {len(all_pairs) - len(pairs)}")
    print()

    touched = []
    errors = []

    for target_id, from_ids in sorted(by_target.items()):
        card_file = find_card_file(target_id)
        if not card_file:
            errors.append(f"Cannot find card file for: {target_id} (referenced by {', '.join(from_ids)})")
            continue

        for from_id in from_ids:
            if args.apply:
                changed = add_backlink_to_file(card_file, from_id)
                if changed:
                    rel = card_file.relative_to(VAULT_ROOT).as_posix()
                    touched.append(rel)
                    print(f"  ✅ {target_id} ← {from_id}  ({rel})")
            else:
                diff = compute_diff(card_file, from_id)
                print(f"  📝 {target_id} ← {from_id}")
                print(f"{diff}")

    print()

    if errors:
        print(f"⚠️  {len(errors)} error(s):")
        for e in errors:
            print(f"  {e}")
        print()

    if args.apply:
        # Write manifest
        unique_touched = sorted(set(touched))
        MANIFEST_FILE.write_text(
            "# backlink_fixer touched-files manifest\n" +
            "# Append this list to your submission manifest.\n" +
            "\n".join(unique_touched) + "\n",
            encoding="utf-8",
        )
        print(f"📋 Touched-files manifest → {MANIFEST_FILE}")
        print(f"   {len(unique_touched)} files modified")
        print()
        print("Append this manifest to your submission manifest.")
    else:
        print("DRY-RUN complete. Use --apply to execute.")
        print(f"  {len(pairs)} backlinks pending, {len(errors)} errors")


if __name__ == "__main__":
    main()
