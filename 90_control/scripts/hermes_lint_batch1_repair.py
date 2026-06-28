#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Hermes lint Batch 1 frontmatter mechanical repair helper.

Usage:
    python 90_control/scripts/hermes_lint_batch1_repair.py --dry-run
    python 90_control/scripts/hermes_lint_batch1_repair.py --apply

This script fixes the five safe frontmatter error patterns identified in
60_feedback/tasks/task_20260628_hermes-lint-baseline-cleanup-batch1.md.

Rules enforced:
  1. Only frontmatter is modified; body content is never deleted.
  2. src_unknown placeholders are NOT replaced with real content.
  3. Body text that leaked into frontmatter is moved back to the body.
  4. Missing frontmatter closing separators are inserted.
  5. Colon-in-scalar list items are converted to proper YAML objects.

After running with --apply, verify with:
    python 90_control/scripts/hermes_lint_batch1_repair.py --verify
"""

import argparse
import json
import os
import re
import sys
from collections import Counter
from pathlib import Path

import yaml

VAULT = Path(__file__).resolve().parents[2]
SAFE_BATCH = VAULT / "90_control/.tmp/hermes_lint_safe_batch.json"
UNSAFE_BATCH = VAULT / "90_control/.tmp/hermes_lint_unsafe_batch.json"


def load_batch(path: Path) -> list[dict]:
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)


def split_frontmatter(text: str) -> tuple[str | None, str, str]:
    """Split a markdown file into (frontmatter_raw, separator, body).
    Returns (None, '', text) if no frontmatter is detected.
    """
    if not text.startswith("---"):
        return None, "", text
    parts = text.split("---", 2)
    if len(parts) < 3:
        return parts[1] if len(parts) > 1 else None, "", text
    return parts[1], "---", parts[2]


def fix_no_closing_separator(text: str, path: str) -> str | None:
    """Insert missing closing --- before the first body heading."""
    fm, sep, body = split_frontmatter(text)
    if fm is None or sep:
        return None
    # Find first body marker: # heading, or a line with # glued to frontmatter text.
    lines = text.splitlines()
    insert_idx = None
    split_offset = 0
    split_new_line = None
    for i, line in enumerate(lines):
        if i == 0 and line.strip() == "---":
            continue
        if line.startswith("#"):
            insert_idx = i
            break
        # Body heading glued to frontmatter line (e.g. "key: value# Title").
        m = re.search(r"(?<=.)(#\s+)", line)
        if m:
            insert_idx = i
            split_offset = m.start()
            split_new_line = line[m.end():].lstrip()
            break
    if insert_idx is None:
        return None
    if split_offset:
        lines[insert_idx] = lines[insert_idx][:split_offset].rstrip()
        lines.insert(insert_idx + 1, "# " + split_new_line)
        insert_idx += 1
    new_lines = lines[:insert_idx] + ["---", ""] + lines[insert_idx:]
    return "\n".join(new_lines)


def fix_body_leak(text: str, path: str) -> str | None:
    """Move body markdown that leaked into frontmatter back to the body."""
    fm, sep, body = split_frontmatter(text)
    if fm is None or not sep:
        return None
    lines = fm.splitlines()

    # Case A: Body marker starts its own line inside frontmatter.
    cut_idx = None
    for i, line in enumerate(lines):
        stripped = line.lstrip()
        if (
            stripped.startswith("#")
            or stripped.startswith(">")
            or stripped.startswith("|")
            or re.match(r"\*\*[^*]+\*\*\s*[：:]", stripped)
        ):
            cut_idx = i
            break

    # Case B: Body marker is glued to the last frontmatter line (no newline before # or >).
    if cut_idx is None and lines:
        last = lines[-1]
        # Find first body marker inside the last line.
        m = re.search(r"(?=\s|^)(#\s+|>\s+)", last)
        if m:
            cut_idx = len(lines) - 1
            prefix = last[: m.start()].rstrip()
            suffix = last[m.start():].lstrip()
            lines[-1] = prefix
            lines.append(suffix)

    if cut_idx is None:
        return None

    clean_fm = "\n".join(lines[:cut_idx]).rstrip()
    leaked = "\n".join(lines[cut_idx:]).lstrip()
    new_body = leaked + "\n" + body if body else leaked
    return f"---\n{clean_fm}\n---\n{new_body}"


def fix_expected_colon(text: str, path: str) -> str | None:
    """Attempt to repair 'expected colon' by closing frontmatter or fixing list items."""
    # Most expected_colon cases are actually body leaks or missing separators.
    candidate = fix_body_leak(text, path)
    if candidate:
        return candidate
    candidate = fix_no_closing_separator(text, path)
    if candidate:
        return candidate
    fm, sep, body = split_frontmatter(text)
    if fm is None:
        return None
    # If frontmatter ends with a bare list item, try converting to body or closing.
    lines = fm.splitlines()
    if lines and re.match(r"^-\s+", lines[-1]):
        return f"---\n" + "\n".join(lines[:-1]) + "\n---\n" + lines[-1] + "\n" + body
    return None


def fix_colon_in_scalar_list_item(text: str, path: str) -> str | None:
    """Convert list items followed by indented keys into proper YAML objects."""
    fm, sep, body = split_frontmatter(text)
    if fm is None or not sep:
        return None
    lines = fm.splitlines()
    new_lines = []
    i = 0
    changed = False
    while i < len(lines):
        line = lines[i]
        list_match = re.match(r"^(\s*)-\s+(.+)$", line)
        if list_match and i + 1 < len(lines):
            indent = list_match.group(1)
            item = list_match.group(2)
            next_line = lines[i + 1]
            next_key_match = re.match(r"^(\s+)(\w+):\s*(.*)$", next_line)
            # The next key must be indented more than the list dash.
            if next_key_match and len(next_key_match.group(1)) > len(indent):
                # item is a scalar like "src_unknown" that should not be there.
                key = next_key_match.group(2)
                key_indent = next_key_match.group(1)
                # If item is src_unknown, drop it and use the key line directly.
                if item.strip() == "src_unknown":
                    new_lines.append(f"{indent}- {key}: {next_key_match.group(3)}".rstrip())
                    i += 2
                    changed = True
                    continue
                # Otherwise, convert item to an object key if possible.
                # Heuristic: if item looks like a simple id/name, keep it as key.
                if re.match(r"^[A-Za-z0-9_\-]+$", item.strip()):
                    new_lines.append(f"{indent}- {item.strip()}:")
                    new_lines.append(f"{key_indent}{key}: {next_key_match.group(3)}")
                    i += 2
                    changed = True
                    continue
        new_lines.append(line)
        i += 1
    if not changed:
        return None
    return f"---\n" + "\n".join(new_lines) + "\n---" + body


def fix_indent_or_list_error(text: str, path: str) -> str | None:
    """Repair minor indent/list errors, typically missing separator."""
    return fix_body_leak(text, path) or fix_no_closing_separator(text, path)


REPAIR_FUNCS = {
    "colon_in_scalar_list_item": fix_colon_in_scalar_list_item,
    "body_leak_into_frontmatter": fix_body_leak,
    "expected_colon": fix_expected_colon,
    "no_closing_separator": fix_no_closing_separator,
    "indent_or_list_error": fix_indent_or_list_error,
}


def repair_file(path: str, issue: str, dry_run: bool = True) -> tuple[bool, str | None]:
    p = VAULT / path
    try:
        text = p.read_text(encoding="utf-8")
    except Exception as e:
        return False, f"read error: {e}"
    func = REPAIR_FUNCS.get(issue)
    if not func:
        return False, f"no repair function for {issue}"
    new_text = func(text, path)
    if new_text is None:
        return False, "no fix applied (pattern not matched)"
    if new_text == text:
        return False, "no change"
    # Validate frontmatter parses.
    if not new_text.startswith("---"):
        return False, "repair removed frontmatter start"
    parts = new_text.split("---", 2)
    if len(parts) < 3:
        return False, "repair left frontmatter unclosed"
    try:
        yaml.safe_load(parts[1])
    except yaml.YAMLError as e:
        return False, f"repair produced invalid yaml: {e}"
    if not dry_run:
        p.write_text(new_text, encoding="utf-8")
    return True, None


def main():
    parser = argparse.ArgumentParser(description="Hermes lint Batch 1 repair helper")
    parser.add_argument("--dry-run", action="store_true", help="Show what would be changed")
    parser.add_argument("--apply", action="store_true", help="Apply fixes")
    parser.add_argument("--verify", action="store_true", help="Verify current files parse")
    parser.add_argument("--max", type=int, default=0, help="Max files to process (0=all)")
    args = parser.parse_args()

    if not SAFE_BATCH.exists():
        print(f"Batch file not found: {SAFE_BATCH}", file=sys.stderr)
        sys.exit(1)

    safe = load_batch(SAFE_BATCH)

    if args.verify:
        ok = bad = 0
        for it in safe:
            p = VAULT / it["path"]
            try:
                text = p.read_text(encoding="utf-8")
                parts = text.split("---", 2)
                if len(parts) < 3:
                    bad += 1
                    continue
                yaml.safe_load(parts[1])
                ok += 1
            except Exception:
                bad += 1
        print(f"verify: {ok} ok, {bad} still bad out of {len(safe)}")
        return

    if not (args.dry_run or args.apply):
        parser.print_help()
        return

    counts = Counter()
    failed = []
    limit = args.max if args.max > 0 else len(safe)
    for it in safe[:limit]:
        success, err = repair_file(it["path"], it["issue"], dry_run=not args.apply)
        if success:
            counts[it["issue"]] += 1
            print(f"{'[DRY-RUN] ' if args.dry_run else ''}fixed {it['path']} ({it['issue']})")
        else:
            failed.append((it["path"], it["issue"], err))
            print(f"{'[DRY-RUN] ' if args.dry_run else ''}SKIP {it['path']} ({it['issue']}): {err}")

    print("\nSummary:")
    for issue, n in counts.most_common():
        print(f"  {n:4d} {issue}")
    print(f"  {len(failed):4d} failed/skipped")
    if failed:
        print("\nFailed/skipped files:")
        for path, issue, err in failed[:20]:
            print(f"  {path} | {issue} | {err}")


if __name__ == "__main__":
    main()
