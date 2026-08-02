#!/usr/bin/env python3
"""
#227 紧急修复 — 全库 aliases 块合并 + 孤儿行清理 + yaml 验证

破坏: 批量操作注入多个 aliases 块 + 孤儿 src_unknown/标签行 → YAML 全坏
"""
import argparse, re, sys
from pathlib import Path

VAULT_ROOT = Path(__file__).resolve().parent.parent.parent
WIKI_DIR = VAULT_ROOT / "30_wiki"

ORPHAN_PATTERNS = [
    r'^  - src_unknown\s*$',
    r'^  - audience:\w+\s*$',
    r'^  - scene:\w+\s*$',
    r'^  - skill-level:\w+\s*$',
    r'^  - method:\S+\s*$',
    r'^  - source-person:\S+\s*$',
    r'^  - industry:\S+\s*$',
    r'^  - value-tier:\S+\s*$',
    r'^  - prerequisite-knowledge:\S+\s*$',
]


def repair(text: str) -> tuple[str, int, int]:
    """Fix one card. Returns (new_text, old_blocks, merged_items)."""
    # Count ALL aliases blocks (any indentation)
    blocks = list(re.finditer(r'^  aliases:\s*\n((?:    - .+\n)*)', text, re.MULTILINE))
    blocks += list(re.finditer(r'^aliases:\s*\n((?:  - .+\n)*)', text, re.MULTILINE))
    if len(blocks) < 2:
        return text, 0, 0

    # Collect all items from all aliases blocks
    all_items = set()
    for b in blocks:
        for item in re.findall(r'^\s*-\s+(.+)$', b.group(1), re.MULTILINE):
            c = item.strip().strip('"').strip("'")
            if c and c != 'src_unknown':
                all_items.add(c)

    # Remove injected aliases after diagnostic_signals:
    text = re.sub(
        r'(^diagnostic_signals:\s*\n)  aliases:\s*\n(?:    - .+\n)*',
        r'\1',
        text, flags=re.MULTILINE,
    )
    text = re.sub(
        r'(^diagnostic_signals:\s*\n)aliases:\s*\n(?:  - .+\n)*',
        r'\1',
        text, flags=re.MULTILINE,
    )

    # Remove ALL aliases blocks (both indented and root-level)
    text = re.sub(r'^  aliases:\s*\n(?:    - .+\n)*', '', text, flags=re.MULTILINE)
    text = re.sub(r'^aliases:\s*\n(?:  - .+\n)*', '', text, flags=re.MULTILINE)

    # Remove orphan debris lines (src_unknown, audience/scene/skill-level at root)
    for pattern in ORPHAN_PATTERNS:
        text = re.sub(pattern, '', text, flags=re.MULTILINE)

    # Clean up triple+ blank lines
    text = re.sub(r'\n\n\n+', '\n\n', text)

    # Insert single merged block before source_refs:
    sorted_a = sorted(all_items)
    new_block = 'aliases:\n' + '\n'.join(f'  - {a}' for a in sorted_a) + '\n'
    if re.search(r'^source_refs:', text, re.MULTILINE):
        text = re.sub(r'^(source_refs:)', new_block + r'\1', text, count=1, flags=re.MULTILINE)
    elif re.search(r'^related:', text, re.MULTILINE):
        text = re.sub(r'^(related:)', new_block + r'\1', text, count=1, flags=re.MULTILINE)
    else:
        text = re.sub(r'^(---\s*\n)', r'\1' + new_block, text, count=1)

    # Validate YAML
    m = re.match(r'^---\s*\n(.*?)\n---\s*\n', text, re.DOTALL)
    if m:
        try:
            import yaml
            yaml.safe_load(m.group(1))
        except Exception:
            return text, len(blocks), 0

    return text, len(blocks), len(all_items)


def scan_and_fix(target_dir: Path, dry_run: bool) -> dict:
    stats = {"total": 0, "fixed": 0, "failed": [], "remaining": 0}
    for fp in sorted(target_dir.rglob("*.md")):
        if "_archive" in str(fp) or "raw" in str(fp):
            continue
        stats["total"] += 1
        old = fp.read_text(encoding="utf-8", errors="replace")
        new, blocks, items = repair(old)
        if blocks < 2:
            continue
        if items == 0:
            stats["failed"].append((fp.name, "yaml broken"))
            continue
        if not dry_run:
            fp.write_text(new, encoding="utf-8")
        stats["fixed"] += 1

    for fp in target_dir.rglob("*.md"):
        if "_archive" in str(fp) or "raw" in str(fp):
            continue
        if len(re.findall(r'^aliases:\s*$', fp.read_text(encoding="utf-8", errors="replace"), re.MULTILINE)) > 1:
            stats["remaining"] += 1
    return stats


def main():
    p = argparse.ArgumentParser(description="#227 repair")
    p.add_argument("--dry-run", action="store_true")
    p.add_argument("--dir")
    args = p.parse_args()
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")

    dirs = [args.dir] if args.dir else [
        "frameworks", "tools", "concepts", "dk", "dark-knowledges",
        "cases", "bridges", "methods", "systems", "skills", "domains",
        "decisions", "entities", "projects", "personal-os", "principles",
        "operations", "workflows", "knowledges", "prompt-methodology",
        "cross-domain-patterns",
    ]

    grand = {"total": 0, "fixed": 0, "failed": [], "remaining": 0}
    for d in dirs:
        t = WIKI_DIR / d
        if not t.exists():
            continue
        s = scan_and_fix(t, args.dry_run)
        if s["fixed"] > 0 or s["remaining"] > 0:
            label = "DRY" if args.dry_run else "FIX"
            print(f"[{label}] {d}/: {s['total']} files, {s['fixed']} fixed, {s['remaining']} remaining double")
        for name, e in s["failed"]:
            print(f"  FAIL: {name}: {e}")
        grand["total"] += s["total"]
        grand["fixed"] += s["fixed"]
        grand["failed"].extend(s["failed"])
        grand["remaining"] += s["remaining"]

    print(f"\nTotal: {grand['total']} | Fixed: {grand['fixed']} | Failed: {len(grand['failed'])} | Double remaining: {grand['remaining']}")
    print(f"Status: {'PASS' if not grand['remaining'] and not grand['failed'] else 'FAIL'}")
    sys.exit(1 if (grand["remaining"] or grand["failed"]) else 0)


if __name__ == "__main__":
    main()
