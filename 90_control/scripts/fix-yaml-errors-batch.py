#!/usr/bin/env python3
"""
批量修复 YAML 解析错误（阶段 6 批量修复任务 1）
处理模式：
1. 列表项中包含未转义中文双引号 → 用单引号包裹
2. entity/project/system 卡的 id 字段被 source 污染 → 分离 id 和 source_refs
3. log.md 等非卡片文件 → 特殊处理或跳过
"""

import re
from pathlib import Path

WIKI_DIR = Path("C:/Users/Administrator/Desktop/wiki/30_wiki")
REPORT_DIR = Path("C:/Users/Administrator/Desktop/wiki/60_feedback/audit")


def read_file(file_path):
    return file_path.read_text(encoding="utf-8")


def write_file(file_path, text):
    file_path.write_text(text, encoding="utf-8")


def has_chinese_quote(s):
    return '"' in s or '"' in s


def fix_list_item_quotes(fm_text):
    """修复列表项中的中文双引号问题"""
    lines = fm_text.split("\n")
    new_lines = []
    for line in lines:
        # 匹配列表项：  - "..."
        match = re.match(r'^(\s+-\s+)"(.*)"\s*$', line)
        if match:
            prefix, value = match.groups()
            if has_chinese_quote(value):
                # 用单引号包裹，内部单引号转义
                if "'" in value:
                    value = value.replace("'", "''")
                new_lines.append(f"{prefix}'{value}'")
                continue
        new_lines.append(line)
    return "\n".join(new_lines)


def fix_id_with_sources(fm_text, title, file_stem):
    """修复 id 字段被 source 污染的问题"""
    # 匹配 id: "xxx - "src_..." - "src_..."" 或 id: "xxx - "src_...""
    pattern = re.compile(r'^(id:\s*)"([^"]+?\s+-\s+)(src_\d{8}_[0-9a-f]+(?:\s+-\s+src_\d{8}_[0-9a-f]+)*)"\s*$', re.MULTILINE)
    
    def replacer(m):
        prefix = m.group(1)
        id_part = m.group(2).strip().rstrip(" -")
        sources_str = m.group(3)
        sources = re.findall(r'src_\d{8}_[0-9a-f]+', sources_str)
        
        # 如果 id_part 为空或与 title 不一致，使用 title 或 file_stem
        clean_id = id_part.strip() or title.strip() or file_stem
        result = f'{prefix}"{clean_id}"'
        if sources:
            source_lines = "\nsource_refs:\n" + "\n".join(f'  - "{s}"' for s in sources)
            result += source_lines
        return result
    
    return pattern.sub(replacer, fm_text)


def fix_polluted_type(fm_text, file_stem):
    """修复 type 字段被 source 污染的问题（如 graph-rag-retrieval-layer）"""
    # 匹配 type: "concept - "LightRAG..." - ".kdo/...""
    pattern = re.compile(r'^(type:\s*)"([^"]+?)\s+-\s+"([^"]+)"(?:\s+-\s+"([^"]+)")?"\s*$', re.MULTILINE)
    
    def replacer(m):
        prefix = m.group(1)
        type_part = m.group(2).strip()
        source1 = m.group(3).strip() if m.group(3) else None
        source2 = m.group(4).strip() if m.group(4) else None
        
        result = f'{prefix}"{type_part}"'
        sources = [s for s in [source1, source2] if s]
        if sources:
            result += "\nsource_refs:\n" + "\n".join(f'  - "{s}"' for s in sources)
        return result
    
    return pattern.sub(replacer, fm_text)


def extract_title_from_fm(fm_text):
    """从 frontmatter 文本中提取 title"""
    match = re.search(r'^title:\s*"([^"]*)"', fm_text, re.MULTILINE)
    if match:
        return match.group(1)
    match = re.search(r'^title:\s*([^\n]+)', fm_text, re.MULTILINE)
    if match:
        return match.group(1).strip()
    return ""


def main():
    files = list(WIKI_DIR.rglob("*.md"))
    fixed = []
    skipped = []
    
    for file_path in files:
        text = read_file(file_path)
        if not text.startswith("---\n"):
            continue
        
        end_idx = text.find("\n---\n", 4)
        if end_idx == -1:
            # 无结束标记，特殊处理 log.md
            if file_path.name == "log.md":
                # 重新生成简洁 frontmatter
                body = text[text.find("#"):]
                new_text = "---\nid: \"log\"\ntype: \"concept\"\nstatus: \"draft\"\ntitle: \"Wiki Log\"\ndomain: []\n---\n\n" + body
                write_file(file_path, new_text)
                fixed.append((str(file_path.relative_to(WIKI_DIR)), "log.md 重新生成 frontmatter"))
            elif file_path.name == "contradictions.md":
                # 跳过非卡片文件
                skipped.append((str(file_path.relative_to(WIKI_DIR)), "无 frontmatter 结束标记，非知识卡"))
            else:
                skipped.append((str(file_path.relative_to(WIKI_DIR)), "无 frontmatter 结束标记"))
            continue
        
        fm_text = text[4:end_idx]
        body = text[end_idx + 5:]
        original_fm = fm_text
        title = extract_title_from_fm(fm_text)
        file_stem = file_path.stem
        
        # 应用修复
        fm_text = fix_list_item_quotes(fm_text)
        fm_text = fix_id_with_sources(fm_text, title, file_stem)
        fm_text = fix_polluted_type(fm_text, file_stem)
        
        if fm_text != original_fm:
            new_text = f"---\n{fm_text}\n---\n{body}"
            write_file(file_path, new_text)
            fixed.append((str(file_path.relative_to(WIKI_DIR)), "修复 YAML 格式问题"))
    
    # 生成报告
    lines = [
        "# YAML 错误批量修复报告",
        "",
        f"**修复时间**：2026-06-15  ",
        f"**修复文件数**：{len(fixed)}  ",
        f"**跳过文件数**：{len(skipped)}  ",
        "",
        "## 修复文件清单",
        "",
    ]
    for f, reason in fixed:
        lines.append(f"- `{f}`：{reason}")
    
    lines.extend(["", "## 跳过文件清单", ""])
    for f, reason in skipped:
        lines.append(f"- `{f}`：{reason}")
    
    report_path = REPORT_DIR / "kcard-yaml-errors-fix-report-2026-06-15.md"
    report_path.write_text("\n".join(lines), encoding="utf-8")
    
    print(f"修复：{len(fixed)}，跳过：{len(skipped)}")
    print(f"报告：{report_path}")


if __name__ == "__main__":
    main()
