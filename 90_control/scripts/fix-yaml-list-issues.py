#!/usr/bin/env python3
"""
修复 frontmatter 中列表字段的格式问题：
1. domain 被错误保存为 "['xxx']" 字符串 → 恢复为列表
2. tags/pipeline/related 中包含 None 值 → 清理
"""

import re
import sys
if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")
if hasattr(sys.stderr, "reconfigure"):
    sys.stderr.reconfigure(encoding="utf-8", errors="replace")
import yaml
from pathlib import Path

WIKI_DIR = Path("C:/Users/Administrator/Desktop/wiki/30_wiki")


def parse_frontmatter(text):
    if not text.startswith("---\n"):
        return None, text, None
    end_idx = text.find("\n---\n", 4)
    if end_idx == -1:
        return None, text, None
    fm_text = text[4:end_idx]
    try:
        fm = yaml.safe_load(fm_text)
        if not isinstance(fm, dict):
            fm = {}
        return fm, text[end_idx + 5 :], fm_text
    except Exception:
        return None, text, None


def clean_list_value(value):
    """清理列表字段中的 None 和字符串化列表"""
    if value is None:
        return None
    if isinstance(value, str):
        # 处理 "['x', 'y']" 格式
        s = value.strip()
        if s.startswith("[") and s.endswith("]"):
            inner = s[1:-1]
            items = []
            for part in re.split(r",\s*", inner):
                part = part.strip()
                if part.startswith("'") and part.endswith("'"):
                    part = part[1:-1]
                elif part.startswith('"') and part.endswith('"'):
                    part = part[1:-1]
                if part and part != "None":
                    items.append(part)
            return items if items else None
        return [s] if s else None
    if isinstance(value, list):
        cleaned = []
        for item in value:
            if item is None or str(item).strip() == "None":
                continue
            cleaned.append(item)
        return cleaned if cleaned else None
    return value


def format_yaml_value(key, val):
    """格式化 YAML 值"""
    if val is None:
        return None
    if isinstance(val, list):
        if not val:
            return f"{key}: []"
        lines = [f"{key}:"]
        for item in val:
            lines.append(f"  - {format_scalar(item)}")
        return "\n".join(lines)
    if isinstance(val, dict):
        lines = [f"{key}:"]
        for k, v in val.items():
            lines.append(f"  {k}: {format_scalar(v)}")
        return "\n".join(lines)
    return f"{key}: {format_scalar(val)}"


def format_scalar(val):
    if isinstance(val, str):
        # 如果包含中文或特殊字符，加双引号
        if re.search(r'[\u4e00-\u9fff\s\[\]:,]', val) or val in ("true", "false", "null", "yes", "no", "on", "off"):
            escaped = val.replace('\\', '\\\\').replace('"', '\\"')
            return f'"{escaped}"'
        return val
    return str(val)


def main():
    files = list(WIKI_DIR.rglob("*.md"))
    changes = []
    skipped = 0

    for file_path in files:
        text = file_path.read_text(encoding="utf-8")
        result = parse_frontmatter(text)
        if result[0] is None:
            skipped += 1
            continue
        
        fm, body, fm_text = result
        modified = False
        
        # 清理 domain
        if "domain" in fm:
            cleaned = clean_list_value(fm["domain"])
            if cleaned != fm["domain"]:
                fm["domain"] = cleaned
                modified = True
        
        # 清理 tags
        if "tags" in fm:
            cleaned = clean_list_value(fm["tags"])
            if cleaned != fm["tags"]:
                fm["tags"] = cleaned
                modified = True
        
        # 清理 pipeline
        if "pipeline" in fm:
            cleaned = clean_list_value(fm["pipeline"])
            if cleaned != fm["pipeline"]:
                fm["pipeline"] = cleaned
                modified = True
        
        # 清理 related
        if "related" in fm:
            cleaned = clean_list_value(fm["related"])
            if cleaned != fm["related"]:
                fm["related"] = cleaned
                modified = True
        
        if modified:
            # 重新生成 frontmatter，保持原始键顺序
            yaml_lines = []
            for key, val in fm.items():
                if val is None:
                    continue
                formatted = format_yaml_value(key, val)
                if formatted is None:
                    continue
                yaml_lines.append(formatted)
            
            new_text = f"---\n" + "\n".join(yaml_lines) + f"\n---\n{body}"
            file_path.write_text(new_text, encoding="utf-8")
            changes.append(str(file_path))

    print(f"修复文件数：{len(changes)}")
    print(f"跳过文件数：{skipped}")
    
    report_path = Path("C:/Users/Administrator/Desktop/wiki/60_feedback/audit/kcard-yaml-list-fix-report-2026-06-15.md")
    lines = [
        "# YAML 列表字段修复报告",
        "",
        f"**修复时间**：2026-06-15  ",
        f"**修复文件数**：{len(changes)}  ",
        f"**跳过文件数**：{skipped}  ",
        "",
        "## 修复内容",
        "- domain 字段中被错误保存为 `\"['xxx']\"` 的字符串化列表",
        "- tags/pipeline/related 中的 `None` 值",
        "",
        "## 修复文件清单",
        "",
    ]
    for f in changes:
        lines.append(f"- `{f}`")
    report_path.write_text("\n".join(lines), encoding="utf-8")
    print(f"报告：{report_path}")


if __name__ == "__main__":
    main()
