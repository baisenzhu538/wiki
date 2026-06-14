#!/usr/bin/env python3
"""
批量修复 YAML 解析错误 V3
按行处理 frontmatter，修复引号嵌套和 id 污染
"""

import re
from pathlib import Path

WIKI_DIR = Path("C:/Users/Administrator/Desktop/wiki/30_wiki")
REPORT_DIR = Path("C:/Users/Administrator/Desktop/wiki/60_feedback/audit")


def read_file(file_path):
    return file_path.read_text(encoding="utf-8")


def write_file(file_path, text):
    file_path.write_text(text, encoding="utf-8")


def extract_frontmatter(text):
    if not text.startswith("---\n"):
        return None, text
    end_idx = text.find("\n---\n", 4)
    if end_idx != -1:
        return text[4:end_idx], text[end_idx + 5:]
    end_idx = text.find("---\n", 4)
    if end_idx != -1:
        return text[4:end_idx].rstrip(), text[end_idx + 4:]
    return None, text


def fix_scalar_line(line):
    """修复标量行中的双引号嵌套"""
    # 匹配 key: "value"
    match = re.match(r'^(\s*[\w_\u4e00-\u9fff]+:\s*)"(.*)"\s*$', line)
    if not match:
        return line, False
    prefix, value = match.groups()
    # 如果值内部包含双引号（超过 2 个表示有嵌套），用单引号包裹
    if value.count('"') > 2 or value.count('"') >= 1:
        value = value.replace("'", "''")
        return f"{prefix}'{value}'", True
    return line, False


def fix_id_line(line):
    """修复 id 字段被 source 污染"""
    match = re.match(r'^(id:\s*)"([^"]*?)\s+-\s+((?:src_\d{8}_[0-9a-f]+(?:\s+-\s+)?)+)"\s*$', line)
    if not match:
        return line, False
    prefix, id_part, sources_str = match.groups()
    sources = re.findall(r'src_\d{8}_[0-9a-f]+', sources_str)
    result = f'{prefix}"{id_part.strip()}"'
    if sources:
        result += "\nsource_refs:\n" + "\n".join(f'  - "{s}"' for s in sources)
    return result, True


def fix_list_item_line(line):
    """修复列表项中的双引号嵌套"""
    match = re.match(r'^(\s+-\s+)"(.*)"\s*$', line)
    if not match:
        return line, False
    prefix, value = match.groups()
    if value.count('"') > 0:
        value = value.replace("'", "''")
        return f"{prefix}'{value}'", True
    return line, False


def main():
    files = list(WIKI_DIR.rglob("*.md"))
    fixed = []
    
    for file_path in files:
        text = read_file(file_path)
        fm_text, body = extract_frontmatter(text)
        if fm_text is None:
            continue
        
        original_fm = fm_text
        new_lines = []
        modified = False
        
        for line in fm_text.split("\n"):
            # 先尝试修复 id 污染
            new_line, changed = fix_id_line(line)
            if changed:
                new_lines.append(new_line)
                modified = True
                continue
            
            # 修复列表项
            new_line, changed = fix_list_item_line(line)
            if changed:
                new_lines.append(new_line)
                modified = True
                continue
            
            # 修复标量行
            new_line, changed = fix_scalar_line(line)
            if changed:
                new_lines.append(new_line)
                modified = True
                continue
            
            new_lines.append(line)
        
        if modified:
            new_fm_text = "\n".join(new_lines)
            new_text = f"---\n{new_fm_text}\n---\n{body}"
            write_file(file_path, new_text)
            fixed.append(str(file_path.relative_to(WIKI_DIR)))
    
    # 特殊处理 log.md 和 contradictions.md
    for name in ["log.md", "contradictions.md"]:
        p = WIKI_DIR / name
        if p.exists():
            text = read_file(p)
            hash_idx = text.find("# ")
            if hash_idx != -1:
                body = text[hash_idx:]
                title = body.split("\n")[0].replace("# ", "").strip()
                new_text = f'---\nid: "{p.stem}"\ntype: "concept"\nstatus: "draft"\ntitle: "{title}"\ndomain: []\n---\n\n{body}'
                write_file(p, new_text)
                fixed.append(name)
    
    # 生成报告
    lines = [
        "# YAML 错误批量修复报告 V3",
        "",
        f"**修复时间**：2026-06-15  ",
        f"**修复文件数**：{len(fixed)}  ",
        "",
        "## 修复文件清单",
        "",
    ]
    for f in fixed:
        lines.append(f"- `{f}`")
    
    report_path = REPORT_DIR / "kcard-yaml-errors-fix-v3-report-2026-06-15.md"
    report_path.write_text("\n".join(lines), encoding="utf-8")
    
    print(f"修复：{len(fixed)}")
    print(f"报告：{report_path}")


if __name__ == "__main__":
    main()
