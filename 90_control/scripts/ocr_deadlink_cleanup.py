#!/usr/bin/env python3
"""
#163 OCR 死链清理 — dry-run / apply 双模式
欧阳锋 6 条件全部内置。

用法:
  python ocr_deadlink_cleanup.py              # dry-run: 出 diff + manifest
  python ocr_deadlink_cleanup.py --apply      # 执行修复 + 归档
"""

import argparse, json, re, sys
from collections import defaultdict
from pathlib import Path

VAULT_ROOT = Path(__file__).resolve().parent.parent.parent
SANDBOX = VAULT_ROOT / "90_control" / ".sandbox"
MANIFEST_ARCHIVE = SANDBOX / "ocr_deadlink_manifest.json"

# ── 条件 2: 改项目标锁定（欧阳锋"读正文"二分裁定：仅正文实质引用保留为改，其余降级摘）──
REPLACEMENT_MAP = {
    # KEEP_改: yt-entrepreneur-unit-model body含"单元模型"+"单用户"≥2关键词
    "ocr-一堂-单元模型-单用户模型": "yt-entrepreneur-unit-model",
    # DOWNGRADE_摘 (正文无实质引用，仅主题相关):
    # ocr-一堂y模型steps策略集 — tool-yitang-Y-model-application body仅"应用"1词
    # ocr-泛产品设计-落地卡片-攻坚会 — yt-tool-business-formula-gongjianhui body仅"攻坚会"1词
    # ocr-一堂-人机协作-双三角模型 — concept-yihang-dual-triangle-core body仅"双三角"1词
    # ocr-一堂y模型-科学成事道理 — yt-decision-y-model body仅"Y模型"1词
}


def find_ocr_broken_links() -> list[dict]:
    """扫描全库 F2 BROKEN LINK 中 ocr-* 目标，返回 (from_card_path, ocr_target)。"""
    import subprocess
    r = subprocess.run(
        [sys.executable, str(VAULT_ROOT / "90_control" / "scripts" / "kdo_lint.py"),
         str(VAULT_ROOT / "30_wiki")],
        capture_output=True, text=True, timeout=120,
        cwd=str(VAULT_ROOT), encoding="utf-8", errors="replace",
    )
    results = []
    for line in (r.stdout + r.stderr).splitlines():
        m = re.search(r"F2 BROKEN LINK:\s*(\S+)\s*→\s*(ocr-\S+)", line)
        if m:
            from_id = m.group(1)
            ocr_target = m.group(2).rstrip(")")
            # Clean ocr target name
            ocr_target = re.sub(r"\s*\(.*$", "", ocr_target)
            results.append({"from_id": from_id, "ocr_target": ocr_target})
    return results


def find_card_file(card_id: str) -> Path | None:
    """Locate a card's .md file by frontmatter id or filename stem."""
    for d in ["concepts", "frameworks", "tools", "cases", "methods", "systems",
              "operations", "dark-knowledges"]:
        dpath = VAULT_ROOT / "30_wiki" / d
        if not dpath.is_dir():
            continue
        for f in dpath.rglob("*.md"):
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


def process_card(filepath: Path, ocr_target: str, action: str, replacement: str = "") -> dict | None:
    """Process a single card: remove/ocr-* reference from related, strip body wikilinks.
    Returns change record or None if no change needed."""
    try:
        content = filepath.read_text(encoding="utf-8")
    except Exception:
        return None

    original = content
    changes = []

    # ── Condition 5: Strip body inline [[ocr-*]] → keep text ──
    body_pattern = re.compile(r"\[\[(" + re.escape(ocr_target) + r")(?:\|[^\]]+)?\]\]")
    body_matches = body_pattern.findall(content)
    if body_matches:
        content = body_pattern.sub(r"\1", content)
        changes.append(f"body: stripped [[{ocr_target}]] brackets ({len(body_matches)} occurrences)")

    # ── Fix related list: replace or remove ocr-* reference ──
    fm_match = re.match(r"^(---\s*\n.*?\n---)", content, re.DOTALL)
    if fm_match:
        fm_block = fm_match.group(1)
        rest = content[len(fm_block):]

        if action == "改" and replacement:
            # Replace ocr_target with replacement in related
            new_fm = fm_block.replace(f"[[{ocr_target}]]", f"[[{replacement}]]")
            if new_fm != fm_block:
                changes.append(f"related: {ocr_target} → {replacement}")
                content = new_fm + rest
        elif action == "摘":
            # Remove related line containing ocr_target
            lines = fm_block.splitlines()
            new_lines = []
            removed = 0
            for line in lines:
                if ocr_target in line and line.strip().startswith("-"):
                    removed += 1
                    continue
                new_lines.append(line)
            if removed > 0:
                new_fm = "\n".join(new_lines)
                content = new_fm + rest
                changes.append(f"related: removed {removed} line(s) referencing [[{ocr_target}]]")

    if content == original:
        return None

    return {
        "file": str(filepath.relative_to(VAULT_ROOT)),
        "ocr_target": ocr_target,
        "action": action,
        "replacement": replacement if action == "改" else None,
        "changes": changes,
        "diff": _compute_diff(original, content),
        "new_content": content,
    }


def _compute_diff(original: str, modified: str) -> str:
    """Minimal diff showing changed lines."""
    orig_lines = original.splitlines()
    mod_lines = modified.splitlines()
    diff_lines = []
    for i, (o, m) in enumerate(zip(orig_lines, mod_lines)):
        if o != m:
            diff_lines.append(f"  L{i+1}: -{o[:80]}")
            diff_lines.append(f"  L{i+1}: +{m[:80]}")
    if len(mod_lines) > len(orig_lines):
        for i in range(len(orig_lines), len(mod_lines)):
            diff_lines.append(f"  L{i+1}: +{mod_lines[i][:80]}")
    elif len(orig_lines) > len(mod_lines):
        for i in range(len(mod_lines), len(orig_lines)):
            diff_lines.append(f"  L{i+1}: -{orig_lines[i][:80]}")
    return "\n".join(diff_lines)


def main():
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")

    parser = argparse.ArgumentParser(description="#163 OCR deadlink cleanup")
    parser.add_argument("--apply", action="store_true", help="执行修复")
    args = parser.parse_args()

    broken = find_ocr_broken_links()
    print(f"Found {len(broken)} ocr-* BROKEN LINK references")

    # Group by ocr_target
    by_target: dict[str, list[str]] = defaultdict(list)
    for b in broken:
        by_target[b["ocr_target"]].append(b["from_id"])

    print(f"Unique ocr targets: {len(by_target)}")

    # Determine action for each target
    actions = {}
    for ocr in by_target:
        if ocr in REPLACEMENT_MAP:
            actions[ocr] = ("改", REPLACEMENT_MAP[ocr])
        else:
            actions[ocr] = ("摘", "")

    # Process
    manifest: list[dict] = []
    all_changes: list[dict] = []
    touched_files: set[str] = set()

    for ocr_target, from_ids in sorted(by_target.items()):
        action, replacement = actions[ocr_target]

        for from_id in from_ids:
            card_file = find_card_file(from_id)
            if not card_file:
                print(f"  SKIP: cannot find card file for {from_id}")
                continue

            record = process_card(card_file, ocr_target, action, replacement)
            if record:
                manifest.append({"from": from_id, "to": ocr_target, "action": action})
                all_changes.append(record)
                touched_files.add(record["file"])

    # ── Condition 1: Archive manifest ──
    SANDBOX.mkdir(parents=True, exist_ok=True)
    MANIFEST_ARCHIVE.write_text(
        json.dumps({
            "description": "#163 OCR deadlink cleanup — from×target full mapping",
            "total_pairs": len(manifest),
            "pairs": manifest,
        }, ensure_ascii=False, indent=2),
        encoding="utf-8",
    )

    # ── Output ──
    print()
    print("=" * 55)
    mode = "APPLY" if args.apply else "DRY-RUN"
    print(f"#163 OCR Deadlink Cleanup — {mode}")
    print("=" * 55)
    print(f"  Pairs:    {len(manifest)}")
    print(f"  Files:    {len(touched_files)}")
    print(f"  改 (replace): {sum(1 for m in manifest if m['action'] == '改')}")
    print(f"  摘 (remove):  {sum(1 for m in manifest if m['action'] == '摘')}")
    print(f"  Manifest: {MANIFEST_ARCHIVE}")
    print()

    # Show 改 items for 欧阳锋 review
    gai_items = [c for c in all_changes if c["action"] == "改"]
    if gai_items:
        print("── 改 (replace) items ──")
        for c in gai_items:
            print(f"  {c['file']}: {c['ocr_target']} → {c['replacement']}")
        print()

    # Show diff sample
    sample = all_changes[:5] + all_changes[-5:] if len(all_changes) > 10 else all_changes
    print(f"── Diff sample ({len(sample)} of {len(all_changes)}) ──")
    for c in sample:
        print(f"\n  [{c['file']}] {c['action']}: {c['ocr_target']}")
        for ch in c["changes"]:
            print(f"    {ch}")
        if c["diff"]:
            for dline in c["diff"].splitlines()[:6]:
                print(f"    {dline}")

    if args.apply:
        # Write changes
        written = 0
        for c in all_changes:
            filepath = VAULT_ROOT / c["file"]
            try:
                filepath.write_text(c["new_content"], encoding="utf-8")
                written += 1
            except Exception as e:
                print(f"  ERROR writing {c['file']}: {e}")

        print(f"\n✅ Applied: {written}/{len(all_changes)} files written")
        print(f"📋 Manifest: {MANIFEST_ARCHIVE}")
        print("Run: python 90_control/scripts/kdo_lint.py --baseline  to rebuild baseline")
    else:
        print(f"\nDRY-RUN complete. {len(all_changes)} changes pending.")
        print("Use --apply to execute.")


if __name__ == "__main__":
    main()
