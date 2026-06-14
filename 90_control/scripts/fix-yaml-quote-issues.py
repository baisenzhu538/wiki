#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
修复 30_wiki 中因中文双引号导致的 YAML frontmatter 解析错误
将包含中文引号的双引号字符串改为单引号字符串
"""

import re
import yaml
from pathlib import Path

WIKI_DIR = Path("C:/Users/Administrator/Desktop/wiki/30_wiki")

def has_chinese_quote(s):
    """检查字符串中是否包含中文双引号（左/右）"""
    return '"' in s or '"' in s


def fix_line(line):
    """修复单行 YAML 字符串中的引号问题"""
    # 匹配 key: "value" 形式，允许 key 前有空格或 - 
    pattern = re.compile(r'^(\s*-?\s*[\w_]+:\s*)"(.*)"\s*$')
    match = pattern.match(line)
    if not match:
        return line
    
    prefix = match.group(1)
    value = match.group(2)
    
    if not has_chinese_quote(value):
        return line
    
    # 改为单引号包裹，内部单引号转义
    if "'" in value:
        value = value.replace("'", "''")
    
    return f"{prefix}'{value}'\n"


def fix_file(file_path):
    """修复单个文件"""
    content = file_path.read_text(encoding="utf-8")
    if not content.startswith("---"):
        return False
    
    parts = content.split("---", 2)
    if len(parts) < 3:
        return False
    
    yaml_text = parts[1]
    body = parts[2]
    
    # 逐行修复
    lines = yaml_text.splitlines(keepends=True)
    fixed_lines = []
    for line in lines:
        fixed_lines.append(fix_line(line))
    
    new_yaml_text = "".join(fixed_lines)
    
    # 验证修复后是否可解析
    try:
        yaml.safe_load(new_yaml_text)
    except yaml.YAMLError as e:
        print(f"  修复后仍无法解析: {file_path}: {e}")
        return False
    
    # 写回
    new_content = f"---{new_yaml_text}---{body}"
    file_path.write_text(new_content, encoding="utf-8")
    return True


def main():
    fixed = 0
    still_error = 0
    
    for md_file in sorted(WIKI_DIR.rglob("*.md")):
        if md_file.name in ("index.md", "log.md", "contradictions.md", "concept-card-index-latest.md"):
            continue
        
        content = md_file.read_text(encoding="utf-8")
        if not content.startswith("---"):
            continue
        parts = content.split("---", 2)
        if len(parts) < 3:
            continue
        
        try:
            yaml.safe_load(parts[1])
            continue  # 无需修复
        except yaml.YAMLError:
            pass
        
        print(f"修复: {md_file.relative_to(WIKI_DIR)}")
        if fix_file(md_file):
            fixed += 1
        else:
            still_error += 1
    
    print(f"\n修复完成: {fixed} 个文件")
    if still_error > 0:
        print(f"仍有错误: {still_error} 个文件")


if __name__ == "__main__":
    main()
