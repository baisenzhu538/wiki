#!/usr/bin/env python3
"""
source_refs 污染批量清理器
移除全库卡片中指向不存在文件的 source_refs，重点清理 src_20260503_52ae08ba 污染。

用法：
    python 90_control/scripts/purge-dead-source-refs.py --dry-run     # 预览变更
    python 90_control/scripts/purge-dead-source-refs.py                # 执行清理
    python 90_control/scripts/purge-dead-source-refs.py --card <id>    # 单卡清理
"""

import argparse
import re
import sys
from pathlib import Path
from collections import defaultdict

VAULT_ROOT = Path(__file__).resolve().parent.parent.parent
WIKI_DIR = VAULT_ROOT / "30_wiki"

# 已知不存在的文件/污染模式 -> 直接移除
DEAD_PATTERNS = [
    "src_20260503_52ae08ba-kdo_product_design_agent_final.md",
    "src_20260503_52ae08ba",
]

# source_refs 中常见但指向不存在文件的路径片段
# 这些在 check-source-refs.py 中已被验证为缺失
DEAD_PATH_FRAGMENTS = [
    "kdo_product_design_agent_final",
]


def parse_frontmatter_block(text):
    """返回 (before_yaml, yaml_str, after_yaml) """
    if not text.startswith("---\n"):
        return None, None, None
    end = text.find("\n---\n", 4)
    if end == -1:
        return None, None, None
    return "", text[4:end], text[end + 5:]


def extract_source_refs(yaml_str):
    """从 YAML 字符串中提取 source_refs 列表"""
    # 匹配 source_refs: 块
    lines = yaml_str.split("\n")
    in_source_refs = False
    source_lines = []
    source_start = None
    source_end = None

    for i, line in enumerate(lines):
        stripped = line.strip()
        if stripped.startswith("source_refs:"):
            in_source_refs = True
            source_start = i
            # 检查是否在同一行有值 (source_refs: [])
            if "[" in stripped and "]" in stripped:
                source_end = i + 1
                in_source_refs = False
            continue
        if in_source_refs:
            if stripped.startswith("-") or stripped.startswith("#") or stripped == "":
                source_lines.append((i, line))
                continue
            elif ":" in stripped and not stripped.startswith("-"):
                # 下一个 field 开始了
                source_end = i
                in_source_refs = False
            elif stripped == "":
                continue
            else:
                # 可能是没有 - 前缀的值行
                source_lines.append((i, line))

    if in_source_refs and source_start is not None:
        source_end = len(lines)

    return source_start, source_end, source_lines, lines


def is_dead_source(ref):
    """判断一个 source_ref 是否应被移除"""
    s = str(ref).strip().strip('"').strip("'")
    if not s or s == "None":
        return True
    for pat in DEAD_PATTERNS:
        if pat in s:
            return True
    for frag in DEAD_PATH_FRAGMENTS:
        if frag in s:
            return True
    return False


def check_file_exists(ref, vault_root):
    """检查文件路径是否存在"""
    s = str(ref).strip().strip('"').strip("'")
    # 只检查看起来像文件路径的
    if "/" not in s:
        return None  # 不是文件路径，不判断
    candidate = vault_root / s
    return candidate.exists()


def clean_card(file_path, dry_run=True):
    """清理单张卡片。返回 (changed, dead_removed, details)"""
    try:
        text = file_path.read_text(encoding="utf-8")
    except Exception as e:
        return False, 0, f"read error: {e}"

    if not text.startswith("---\n"):
        return False, 0, "no frontmatter"

    end = text.find("\n---\n", 4)
    if end == -1:
        return False, 0, "unclosed frontmatter"

    yaml_str = text[4:end]
    body = text[end + 5:]

    source_start, source_end, source_lines_info, lines = extract_source_refs(yaml_str)
    if source_start is None:
        return False, 0, "no source_refs field"  # 没有 source_refs，跳过

    # 重建 clean source_refs
    clean_sources = []
    dead_removed = []
    for line_idx, line in source_lines_info:
        stripped = line.strip()
        if stripped.startswith("#"):
            clean_sources.append((line_idx, line))
            continue
        if not stripped:
            clean_sources.append((line_idx, line))
            continue
        # 提取 - 后面的值
        if stripped.startswith("-"):
            val = stripped[1:].strip()
            if is_dead_source(val):
                dead_removed.append(val)
                continue
            # 也检查文件是否存在
            exists = check_file_exists(val, VAULT_ROOT)
            if exists is False:
                dead_removed.append(val)
                continue
        clean_sources.append((line_idx, line))

    if not dead_removed:
        return False, 0, "no dead sources"

    if dry_run:
        return True, len(dead_removed), dead_removed

    # 重建 source_refs 块
    new_lines = lines[:source_start + 1]  # 保留到 source_refs: 行

    if clean_sources:
        for line_idx, line in clean_sources:
            new_lines.append(line)
    else:
        # 全部移除了，保留空列表
        new_lines[source_start] = "source_refs: []"

    # 保留 source_refs 之后的行
    if source_end and source_end < len(lines):
        new_lines.extend(lines[source_end:])

    new_yaml = "\n".join(new_lines)
    # 清理多余空行
    new_yaml = re.sub(r"\n{3,}", "\n\n", new_yaml)

    new_content = "---\n" + new_yaml + "\n---" + body
    file_path.write_text(new_content, encoding="utf-8")
    return True, len(dead_removed), dead_removed


def main():
    parser = argparse.ArgumentParser(description="source_refs 污染批量清理器")
    parser.add_argument("--dry-run", action="store_true", help="预览模式，不实际修改文件")
    parser.add_argument("--card", help="仅清理指定卡片 ID")
    args = parser.parse_args()

    md_files = [
        f for f in WIKI_DIR.rglob("*.md")
        if "_archive" not in f.parts and "raw" not in f.parts
    ]

    if args.card:
        md_files = [f for f in md_files if f.stem == args.card]
        if not md_files:
            print(f"错误：未找到卡片 {args.card}", file=sys.stderr)
            sys.exit(2)

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
    print(f"# {mode}source_refs 污染清理报告")
    print(f"**扫描**：{len(md_files)} 个文件")
    print(f"**需清理**：{total_changed} 张卡片")
    print(f"**移除条目**：{total_removed} 条")
    print()

    if changes:
        print("| 卡片 ID | 文件 | 移除数 | 移除的 source |")
        print("|---|---|---|---|")
        for rel, card_id, count, detail in changes:
            removed_preview = ", ".join(str(d)[:60] for d in detail[:3])
            if len(detail) > 3:
                removed_preview += f" ... (+{len(detail)-3})"
            print(f"| `{card_id}` | `{rel}` | {count} | {removed_preview} |")

    if args.dry_run and total_changed > 0:
        print()
        print("> 这是预览。去掉 --dry-run 执行实际清理。")
        print(f"> 命令：python 90_control/scripts/purge-dead-source-refs.py")

    sys.exit(0 if total_changed == 0 else 0)


if __name__ == "__main__":
    main()
