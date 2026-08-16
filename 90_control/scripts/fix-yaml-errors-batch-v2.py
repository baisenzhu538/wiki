#!/usr/bin/env python3
"""
批量修复 YAML 解析错误 V2
"""

import re
import sys
if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")
if hasattr(sys.stderr, "reconfigure"):
    sys.stderr.reconfigure(encoding="utf-8", errors="replace")
from pathlib import Path

WIKI_DIR = Path("C:/Users/Administrator/Desktop/wiki/30_wiki")
REPORT_DIR = Path("C:/Users/Administrator/Desktop/wiki/60_feedback/audit")


def read_file(file_path):
    return file_path.read_text(encoding="utf-8")


def write_file(file_path, text):
    file_path.write_text(text, encoding="utf-8")


def extract_frontmatter(text):
    """更鲁棒地提取 frontmatter"""
    if not text.startswith("---\n"):
        return None, text
    # 尝试找到第二个 ---
    end_idx = text.find("\n---\n", 4)
    if end_idx != -1:
        return text[4:end_idx], text[end_idx + 5:]
    # 处理 domain: []--- 这种没有换行的情况
    end_idx = text.find("---\n", 4)
    if end_idx != -1:
        return text[4:end_idx].rstrip(), text[end_idx + 4:]
    return None, text


def fix_title_quotes(fm_text):
    """修复 title 中的中文双引号"""
    # 匹配 title: "..." 且内部有中文双引号
    pattern = re.compile(r'^(title:\s*)"((?:[^"\n]|"")*)"$', re.MULTILINE)
    
    def replacer(m):
        prefix = m.group(1)
        value = m.group(2)
        if '"' in value or '"' in value:
            # 用单引号包裹
            value = value.replace("'", "''")
            return f"{prefix}'{value}'"
        return m.group(0)
    
    return pattern.sub(replacer, fm_text)


def fix_id_with_sources(fm_text):
    """修复 id 字段被 source 污染"""
    # 匹配 id: "xxx - "src_..." ..."
    pattern = re.compile(
        r'^(id:\s*)"([^"]*?)\s+-\s+((?:src_\d{8}_[0-9a-f]+(?:\s+-\s+)?)+)"$',
        re.MULTILINE
    )
    
    def replacer(m):
        prefix = m.group(1)
        id_part = m.group(2).strip()
        sources_str = m.group(3)
        sources = re.findall(r'src_\d{8}_[0-9a-f]+', sources_str)
        
        result = f'{prefix}"{id_part}"'
        if sources:
            result += "\nsource_refs:\n" + "\n".join(f'  - "{s}"' for s in sources)
        return result
    
    return pattern.sub(replacer, fm_text)


def fix_general_quotes_in_values(fm_text):
    """修复任意标量值中的中文双引号"""
    # 匹配 key: "..." 且值内部有中文双引号
    pattern = re.compile(r'^([\w_\u4e00-\u9fff]+:\s*)"((?:[^"\n]|"")*)"$', re.MULTILINE)
    
    def replacer(m):
        prefix = m.group(1)
        value = m.group(2)
        if '"' in value or '"' in value:
            value = value.replace("'", "''")
            return f"{prefix}'{value}'"
        return m.group(0)
    
    return pattern.sub(replacer, fm_text)


def fix_list_item_quotes(fm_text):
    """修复列表项中的中文双引号"""
    lines = fm_text.split("\n")
    new_lines = []
    for line in lines:
        match = re.match(r'^(\s+-\s+)"(.*)"\s*$', line)
        if match:
            prefix, value = match.groups()
            if '"' in value or '"' in value:
                value = value.replace("'", "''")
                new_lines.append(f"{prefix}'{value}'")
                continue
        new_lines.append(line)
    return "\n".join(new_lines)


def rebuild_frontmatter(fm_dict, original_keys):
    """从字典重新生成 frontmatter"""
    lines = []
    for key in original_keys:
        if key not in fm_dict:
            continue
        val = fm_dict[key]
        if val is None:
            continue
        if isinstance(val, list):
            lines.append(f"{key}:")
            for item in val:
                if item is None or str(item).strip() == "None":
                    continue
                lines.append(f"  - {format_scalar(item)}")
        elif isinstance(val, dict):
            lines.append(f"{key}:")
            for k, v in val.items():
                lines.append(f"  {k}: {format_scalar(v)}")
        else:
            lines.append(f"{key}: {format_scalar(val)}")
    return "\n".join(lines)


def format_scalar(val):
    if isinstance(val, str):
        if re.search(r'[\u4e00-\u9fff\s\[\]:,]', val) or val in ("true", "false", "null", "yes", "no", "on", "off"):
            escaped = val.replace('\\', '\\\\').replace('"', '\\"')
            return f'"{escaped}"'
        return val
    return str(val)


def main():
    files = list(WIKI_DIR.rglob("*.md"))
    fixed = []
    skipped = []
    
    for file_path in files:
        text = read_file(file_path)
        fm_text, body = extract_frontmatter(text)
        
        if fm_text is None:
            skipped.append((str(file_path.relative_to(WIKI_DIR)), "无 frontmatter"))
            continue
        
        original_fm = fm_text
        
        # 应用修复
        fm_text = fix_title_quotes(fm_text)
        fm_text = fix_id_with_sources(fm_text)
        fm_text = fix_general_quotes_in_values(fm_text)
        fm_text = fix_list_item_quotes(fm_text)
        
        if fm_text != original_fm:
            new_text = f"---\n{fm_text}\n---\n{body}"
            write_file(file_path, new_text)
            fixed.append((str(file_path.relative_to(WIKI_DIR)), "修复 YAML 格式问题"))
    
    # 特殊处理 log.md 和 contradictions.md
    for name in ["log.md", "contradictions.md"]:
        p = WIKI_DIR / name
        if p.exists():
            text = read_file(p)
            # 找到 # 标题位置
            hash_idx = text.find("# ")
            if hash_idx != -1:
                body = text[hash_idx:]
                title = body.split("\n")[0].replace("# ", "").strip()
                type_val = "concept"
                new_text = f'---\nid: "{p.stem}"\ntype: "{type_val}"\nstatus: "draft"\ntitle: "{title}"\ndomain: []\n---\n\n{body}'
                write_file(p, new_text)
                fixed.append((name, "重新生成 frontmatter"))
    
    # 生成报告
    lines = [
        "# YAML 错误批量修复报告 V2",
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
    
    report_path = REPORT_DIR / "kcard-yaml-errors-fix-v2-report-2026-06-15.md"
    report_path.write_text("\n".join(lines), encoding="utf-8")
    
    print(f"修复：{len(fixed)}，跳过：{len(skipped)}")
    print(f"报告：{report_path}")


if __name__ == "__main__":
    main()
