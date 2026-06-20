#!/usr/bin/env python3
"""
source_refs 污染批量清理器
仅移除指向 src_20260503_52ae08ba 的虚假引用，不动其他 source。
使用 yaml.safe_load 解析 → 过滤 → 精准行级替换，不破坏 YAML 结构。

用法：
    python 90_control/scripts/purge-dead-source-refs.py --dry-run
    python 90_control/scripts/purge-dead-source-refs.py
"""

import argparse
import re
import sys
from pathlib import Path

VAULT_ROOT = Path(__file__).resolve().parent.parent.parent
WIKI_DIR = VAULT_ROOT / "30_wiki"

# 唯一要清理的污染模式
DEAD_PATTERN = "src_20260503_52ae08ba"


def clean_card(file_path, dry_run=True):
    """清理单张卡片。返回 (changed, removed_count, removed_values)"""
    try:
        original = file_path.read_text(encoding="utf-8")
    except Exception as e:
        return False, 0, [f"read error: {e}"]

    if not original.startswith("---\n"):
        return False, 0, []

    end = original.find("\n---\n", 4)
    if end == -1:
        return False, 0, []

    yaml_text = original[4:end]
    body = original[end + 5:]

    # 用 yaml.safe_load 解析
    try:
        import yaml
        fm = yaml.safe_load(yaml_text)
    except Exception:
        return False, 0, []

    if not isinstance(fm, dict):
        return False, 0, []

    raw_refs = fm.get("source_refs", [])
    if not raw_refs:
        return False, 0, []
    if isinstance(raw_refs, str):
        raw_refs = [raw_refs]

    # 找出要移除的
    dead_indices = []
    for i, ref in enumerate(raw_refs):
        s = str(ref).strip()
        if DEAD_PATTERN in s:
            dead_indices.append(i)

    if not dead_indices:
        return False, 0, []

    # 重建 source_refs 列表（只保留非污染的）
    clean_refs = [ref for i, ref in enumerate(raw_refs) if i not in dead_indices]
    removed_refs = [str(raw_refs[i]) for i in dead_indices]

    if dry_run:
        return True, len(dead_indices), removed_refs

    # === 执行替换 ===
    yaml_lines = yaml_text.split("\n")

    # 找到 source_refs: 行
    src_line_idx = None
    for i, line in enumerate(yaml_lines):
        if line.strip().startswith("source_refs:"):
            src_line_idx = i
            break

    if src_line_idx is None:
        return False, 0, []

    # 找到 source_refs 块结束位置（下一个顶层 key）
    block_end = len(yaml_lines)
    for i in range(src_line_idx + 1, len(yaml_lines)):
        line = yaml_lines[i]
        if line and not line[0].isspace() and ":" in line and not line.strip().startswith("-"):
            block_end = i
            break

    # 重建 source_refs 块
    if clean_refs:
        new_block = ["source_refs:"]
        for ref in clean_refs:
            s = str(ref).strip()
            new_block.append(f"  - {s}")
    else:
        new_block = ["source_refs: []"]

    # 拼接新 YAML
    new_yaml_lines = yaml_lines[:src_line_idx] + new_block + yaml_lines[block_end:]
    new_yaml = "\n".join(new_yaml_lines)

    new_content = "---\n" + new_yaml + "\n---" + body
    file_path.write_text(new_content, encoding="utf-8")
    return True, len(dead_indices), removed_refs


def main():
    parser = argparse.ArgumentParser(description="source_refs 虚假引用批量清理")
    parser.add_argument("--dry-run", action="store_true", help="预览模式")
    args = parser.parse_args()

    md_files = [
        f for f in WIKI_DIR.rglob("*.md")
        if "_archive" not in f.parts and "raw" not in f.parts
    ]

    total_changed = 0
    total_removed = 0
    changes = []

    for fp in sorted(md_files):
        changed, count, detail = clean_card(fp, dry_run=args.dry_run)
        if changed:
            total_changed += 1
            total_removed += count
            rel = fp.relative_to(VAULT_ROOT).as_posix()
            changes.append((rel, fp.stem, count, detail))

    mode = "[DRY RUN] " if args.dry_run else ""
    print(f"# {mode}source_refs 虚假引用清理报告")
    print(f"**扫描文件**：{len(md_files)}")
    print(f"**受影响卡片**：{total_changed}")
    print(f"**移除虚假引用**：{total_removed} 条")
    print(f"**匹配模式**：`{DEAD_PATTERN}`")
    print()

    if changes:
        # 按文件路径分组显示
        print("| 卡片 ID | 文件 | 移除 |")
        print("|---|---|---|")
        for rel, card_id, count, detail in changes:
            print(f"| `{card_id}` | `{rel}` | {count} |")

    if args.dry_run and total_changed > 0:
        print()
        print("> 这是预览。执行清理：")
        print("> `python 90_control/scripts/purge-dead-source-refs.py`")


if __name__ == "__main__":
    main()
