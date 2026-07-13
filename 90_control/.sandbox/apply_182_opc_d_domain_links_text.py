#!/usr/bin/env python3
"""
#182 OPC 销售域 × D 域回链批量落地脚本（文本版，保留 frontmatter 缩进）
- 正向：22 张 30_wiki 正式卡 → D 域目标卡
- 反向：D 域目标卡 → OPC 销售域卡（保证 related 双向闭合）
- 不碰 .agent/prompts/
"""

from pathlib import Path
from collections import defaultdict
import re

VAULT = Path("C:/Users/Administrator/Desktop/wiki")

FORWARD = {
    "personal-os/opc-ai-sales-agent-architecture.md": [
        "framework-一堂-转化率黑客-总纲",
        "conversion-rate-domain-digest",
    ],
    "tools/tool-opc-sales-dialogue-assistant.md": [
        "framework-一堂-转化率黑客-总纲",
        "conversion-rate-domain-digest",
    ],
    "tools/tool-agent-spec-yitang-opening-3min.md": [
        "framework-一堂-十指模型",
        "framework-一堂-触点本质论",
    ],
    "tools/tool-agent-spec-yitang-objection-handler.md": [
        "framework-一堂-阻力方法论骨架",
        "framework-一堂-12种阻力总表",
        "tool-一堂-阻力消除12策小抄",
    ],
    "tools/tool-agent-spec-yitang-customer-segmentation.md": [
        "tool-一堂-五种挖触点",
        "framework-一堂-12触点SABC分级",
    ],
    "tools/tool-agent-spec-yitang-value-proposition.md": [
        "framework-一堂-动力三曲线",
        "tool-一堂-FAB说服法",
        "framework-一堂-十指模型",
    ],
    "tools/tool-agent-spec-yitang-sales-process-tracker.md": [
        "framework-一堂-转化率提升六步法",
        "framework-一堂-12种阻力总表",
    ],
    "tools/tool-agent-spec-yitang-sales-performance-monitor.md": [
        "framework-一堂-动力三曲线",
        "framework-一堂-转化率提升六步法",
    ],
    "tools/tool-agent-spec-yitang-self-motivation.md": [
        "framework-一堂-动力三曲线",
        "tool-一堂-心理激励优先机制",
    ],
    "frameworks/framework-yitang-sales-incentive-6d.md": [
        "framework-一堂-动力三曲线",
    ],
    "tools/tool-yitang-sales-process-decomposition.md": [
        "framework-一堂-转化率提升六步法",
    ],
    "tools/tool-yitang-value-proposition-4step.md": [
        "framework-一堂-动力三曲线",
        "tool-一堂-FAB说服法",
    ],
    "tools/tool-yitang-sales-performance-management.md": [
        "framework-一堂-转化率提升六步法",
        "framework-一堂-动力三曲线",
    ],
    "tools/tool-yitang-payment-collection-playbook.md": [
        "framework-一堂-12种阻力总表",
        "tool-一堂-阻力消除12策小抄",
        # 以下 6 条为既有 related 的去 BOM 显影，需补双向闭合
        "tool-yitang-sales-process-decomposition",
        "framework-yitang-scientific-sales-five-step",
        "dk-yitang-sales-common-pitfalls",
        "tool-yitang-sales-performance-management",
        "framework-yitang-sales-incentive-6d",
        "tool-opc-sales-dialogue-assistant",
    ],
    "cases/case-yitang-sales-transformation-jubensha-saas.md": [
        "case-一堂-阻力篇案例库",
        "case-一堂-触点篇案例库",
    ],
    "cases/case-yitang-sales-transformation-tuliaogongsi.md": [
        "case-一堂-触点篇案例库",
        "case-一堂-组合篇案例库",
    ],
    "cases/case-yitang-sales-transformation-meirongyuan.md": [
        "case-一堂-触点篇案例库",
        "case-一堂-动力篇案例库",
    ],
    "dark-knowledges/dk-yitang-sales-common-pitfalls.md": [
        "framework-一堂-12种阻力总表",
        "framework-一堂-转化率提升六步法",
    ],
}


def target_path(tid: str) -> Path:
    if tid.endswith("-domain-digest"):
        return VAULT / "30_wiki" / "domains" / f"{tid}.md"
    prefix = tid.split("-")[0]
    if prefix == "case":
        return VAULT / "30_wiki" / "cases" / f"{tid}.md"
    if prefix == "dk":
        return VAULT / "30_wiki" / "dark-knowledges" / f"{tid}.md"
    if prefix == "framework":
        return VAULT / "30_wiki" / "frameworks" / f"{tid}.md"
    if prefix == "tool":
        return VAULT / "30_wiki" / "tools" / f"{tid}.md"
    raise ValueError(f"无法定位 target: {tid}")


def id_from_path(path: Path) -> str:
    return path.relative_to(VAULT / "30_wiki").stem


def extract_frontmatter(text: str):
    if not text.startswith("---"):
        return None, text
    parts = text.split("---", 2)
    if len(parts) < 3:
        return None, text
    return parts[1], parts[2]


def find_related_range(fm_text: str):
    """
    返回 related 列表在 frontmatter 字符串中的范围 (start, end, next_field_start, item_indent)。
    start = related: 行之后的位置；
    end   = 列表最后一个项结束的位置；
    next_field_start = related 列表后下一个同级/外层 key 开始的位置（无则为 len(fm_text)）；
    item_indent = 列表项前面的空格（含 related 本身的缩进）。
    """
    m = re.search(r"^(\s*)related:\s*$", fm_text, re.MULTILINE)
    if not m:
        return None, None, None, None
    related_indent = m.group(1)
    related_indent_len = len(related_indent)
    start = m.end()
    rest = fm_text[start:]
    lines = rest.splitlines(keepends=True)
    end = start
    next_field_start = None
    item_indent = None
    cumulative_len = 0
    for line in lines:
        stripped = line.lstrip()
        line_indent_len = len(line) - len(stripped)
        # 结束：遇到 frontmatter 结尾或同级/外层 key
        if stripped.startswith("---"):
            if next_field_start is None:
                next_field_start = start + cumulative_len
            break
        if re.match(r"[a-zA-Z0-9_\-]+:\s", stripped) and line_indent_len <= related_indent_len:
            if next_field_start is None:
                next_field_start = start + cumulative_len
            break
        # 列表项：缩进 >= related（允许同列），且以 - 开头
        if re.match(r"-\s", stripped) and line_indent_len >= related_indent_len:
            item_indent = line[:line_indent_len]
            end = start + cumulative_len + len(line)
        cumulative_len += len(line)
    if next_field_start is None:
        next_field_start = start + cumulative_len
    return start, end, next_field_start, item_indent or ""


def parse_related_items(fm_text: str, start: int, end: int):
    items = set()
    section = fm_text[start:end]
    for line in section.splitlines():
        m = re.search(r"-\s+(?:'|\"|\[\[)?([^\]'\"\n\r]+)(?:'|\"|\]\])?", line)
        if m:
            raw = m.group(1).strip()
            items.add(raw.strip("[]"))
    return items


def format_related_item(tid: str, style: str, item_indent: str) -> str:
    if style == "double-quote":
        return f'{item_indent}- "[[{tid}]]"'
    if style == "single-quote":
        return f"{item_indent}- '[[{tid}]]'"
    if style == "bracket":
        return f"{item_indent}- [[{tid}]]"
    return f"{item_indent}- {tid}"


def detect_item_style(section: str) -> str:
    """返回 related 列表中占多数的格式。"""
    counts = {"double-quote": 0, "single-quote": 0, "bracket": 0, "plain": 0}
    for line in section.splitlines():
        stripped = line.lstrip()
        if re.match(r"-\s+'\[\[", stripped):
            counts["single-quote"] += 1
        elif re.match(r'-\s+"\[\[', stripped):
            counts["double-quote"] += 1
        elif re.match(r"-\s+\[\[", stripped):
            counts["bracket"] += 1
        elif re.match(r"-\s+\S", stripped):
            counts["plain"] += 1
    # 返回非零中数量最多的风格；全空则默认 bracket
    return max(counts, key=lambda k: counts[k]) if any(counts.values()) else "bracket"


def add_links(path: Path, new_ids: list[str], reverse_map: dict):
    text = path.read_text(encoding="utf-8-sig")
    fm_text, body = extract_frontmatter(text)
    if fm_text is None:
        print(f"SKIP no frontmatter: {path}")
        return
    start, end, next_field_start, item_indent = find_related_range(fm_text)
    if start is None:
        style = "bracket"
        insert_pos = len(fm_text.rstrip())
        new_section = f"\nrelated:\n" + "\n".join(format_related_item(tid, style, "") for tid in new_ids)
        new_fm = fm_text[:insert_pos] + new_section + "\n"
    else:
        existing = parse_related_items(fm_text, start, end)
        style = detect_item_style(fm_text[start:end]) if end > start else "bracket"
        to_add = [tid for tid in new_ids if tid not in existing]
        if not to_add:
            return
        new_lines = "\n".join(format_related_item(tid, style, item_indent) for tid in to_add)
        # 在 related 最后一个项之后、下一个字段之前插入；保留字段前空行结构
        tail = fm_text[end:next_field_start]
        if not tail.endswith("\n"):
            tail += "\n"
        suffix = fm_text[next_field_start:]
        new_fm = fm_text[:end] + tail + new_lines + "\n" + suffix
    path.write_text(f"---{new_fm}---{body}", encoding="utf-8")
    src_id = id_from_path(path)
    for tid in new_ids:
        reverse_map[target_path(tid)].add(src_id)
    print(f"FWD {path.relative_to(VAULT/'30_wiki')}: +{len(to_add)}")


def main():
    reverse_map = defaultdict(set)
    for src_rel, targets in FORWARD.items():
        add_links(VAULT / "30_wiki" / src_rel, targets, reverse_map)

    for tgt_path, src_ids in reverse_map.items():
        text = tgt_path.read_text(encoding="utf-8-sig")
        fm_text, body = extract_frontmatter(text)
        if fm_text is None:
            print(f"SKIP reverse no frontmatter: {tgt_path}")
            continue
        start, end, next_field_start, item_indent = find_related_range(fm_text)
        style = detect_item_style(fm_text[start:end]) if start is not None and end > start else "bracket"
        to_add = []
        existing = parse_related_items(fm_text, start, end) if start is not None else set()
        for sid in sorted(src_ids):
            if sid not in existing:
                to_add.append(sid)
        if not to_add:
            continue
        if start is None:
            insert_pos = len(fm_text.rstrip())
            new_section = f"\nrelated:\n" + "\n".join(format_related_item(sid, style, "") for sid in to_add)
            new_fm = fm_text[:insert_pos] + new_section + "\n"
        else:
            new_lines = "\n".join(format_related_item(sid, style, item_indent) for sid in to_add)
            tail = fm_text[end:next_field_start]
            if not tail.endswith("\n"):
                tail += "\n"
            suffix = fm_text[next_field_start:]
            new_fm = fm_text[:end] + tail + new_lines + "\n" + suffix
        tgt_path.write_text(f"---{new_fm}---{body}", encoding="utf-8")
        print(f"REV {tgt_path.relative_to(VAULT/'30_wiki')}: +{len(to_add)}")


if __name__ == "__main__":
    main()
