#!/usr/bin/env python3
"""
source_refs 虚假引用清理器（行级精确替换）
仅移除包含 src_20260503_52ae08ba 的 source_refs 条目。
自动修复缩进错误：被错误嵌套在虚假 source 下的真实 source 提升为顶级条目。

用法：
    python 90_control/scripts/purge-dead-source-refs.py --dry-run
    python 90_control/scripts/purge-dead-source-refs.py
"""

import argparse
import sys
from pathlib import Path

VAULT_ROOT = Path(__file__).resolve().parent.parent.parent
WIKI_DIR = VAULT_ROOT / "30_wiki"
DEAD_MARKER = "52ae08ba"


def clean_card(file_path, dry_run=True):
    """
    行级清理。核心逻辑：
    1. 扫描 frontmatter 行
    2. 标记包含 DEAD_MARKER 的 source 行及其子行（缩进更多的行）
    3. 移除标记行
    4. 被移除行的直接子行去缩进（提升为顶级 source 条目）
    """
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
    lines = yaml_text.split("\n")

    # 找 source_refs 块
    src_start = None
    for i, line in enumerate(lines):
        if line.strip().startswith("source_refs:"):
            src_start = i
            break

    if src_start is None:
        return False, 0, []

    # 找块结束
    src_end = len(lines)
    for i in range(src_start + 1, len(lines)):
        line = lines[i]
        if line and not line[0].isspace() and ":" in line:
            src_end = i
            break

    # 分析 source_refs 块内的缩进层级
    # source_refs: 的下一行通常缩进 2 空格
    base_indent = None
    for i in range(src_start + 1, src_end):
        line = lines[i]
        if line.strip() and line.strip().startswith("-"):
            base_indent = len(line) - len(line.lstrip())
            break

    if base_indent is None:
        # 可能是 source_refs: [] 或其他格式，没有列表条目
        return False, 0, []

    # 逐行处理：标记要删除的行 + 要提升缩进的行
    to_remove = set()
    indent_fix = {}  # line_idx -> new_indent_level
    dead_removed = []

    i = src_start + 1
    while i < src_end:
        line = lines[i]
        stripped = line.strip()
        current_indent = len(line) - len(line.lstrip())

        if not stripped:
            i += 1
            continue

        # 检查是否以 - 开头（列表条目）
        if stripped.startswith("-"):
            val = stripped[1:].strip().strip('"').strip("'")
            if DEAD_MARKER in val:
                to_remove.add(i)
                dead_removed.append(val[:100])
                # 检查后续行是否有更深缩进（子条目，需要提升）
                child_indent = current_indent + 2
                j = i + 1
                while j < src_end:
                    next_line = lines[j]
                    if not next_line.strip():
                        j += 1
                        continue
                    next_indent = len(next_line) - len(next_line.lstrip())
                    if next_indent >= child_indent:
                        # 子条目 → 提升到 base_indent
                        new_line = " " * base_indent + next_line.lstrip()
                        lines[j] = new_line
                        j += 1
                    else:
                        break
                i = j
                continue

        i += 1

    if not to_remove:
        return False, 0, []

    if dry_run:
        return True, len(dead_removed), dead_removed

    # 重构 YAML：保留未标记的行
    new_yaml_lines = []
    for i, line in enumerate(lines):
        if i in to_remove:
            continue
        new_yaml_lines.append(line)

    # 如果 source_refs 后面没有条目了，补空列表
    if src_start < len(new_yaml_lines):
        # 检查 source_refs: 后是否还有条目
        has_entries = False
        for i in range(src_start + 1, len(new_yaml_lines)):
            l = new_yaml_lines[i]
            if l.strip().startswith("-"):
                has_entries = True
                break
            if l and not l[0].isspace():
                break
        if not has_entries:
            new_yaml_lines[src_start] = "source_refs: []"

    new_yaml = "\n".join(new_yaml_lines)
    new_content = "---\n" + new_yaml + "\n---" + body
    file_path.write_text(new_content, encoding="utf-8")
    return True, len(dead_removed), dead_removed


def main():
    parser = argparse.ArgumentParser(description="source_refs 虚假引用清理（行级精确替换）")
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
            changes.append((rel, fp.stem, count))

    mode = "[DRY RUN] " if args.dry_run else ""
    print(f"# {mode}source_refs 虚假引用清理报告")
    print(f"**扫描文件**：{len(md_files)}")
    print(f"**受影响**：{total_changed} 张卡片")
    print(f"**移除**：{total_removed} 条引用")
    print(f"**匹配**：`{DEAD_MARKER}`")
    print()

    if changes:
        print("| 卡片 ID | 文件 | 移除 |")
        print("|---|---|---|")
        for rel, card_id, count in changes:
            print(f"| `{card_id}` | `{rel}` | {count} |")

    if args.dry_run and total_changed > 0:
        print()
        print("> 执行清理：`python 90_control/scripts/purge-dead-source-refs.py`")


if __name__ == "__main__":
    main()
