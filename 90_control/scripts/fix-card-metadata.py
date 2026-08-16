#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
30_wiki 知识卡元数据治理脚本
- 废弃 0 字节占位文件
- 补全 id / author / reviewed_by / created_at
- 统一 status / trust_level / confidence 格式
"""

import re
import sys
if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")
if hasattr(sys.stderr, "reconfigure"):
    sys.stderr.reconfigure(encoding="utf-8", errors="replace")
import os
import shutil
import yaml
from pathlib import Path
from datetime import datetime

WIKI_DIR = Path("C:/Users/Administrator/Desktop/wiki/30_wiki")
AUDIT_DIR = Path("C:/Users/Administrator/Desktop/wiki/60_feedback/audit")
DEPRECATED_DIR = AUDIT_DIR / "deprecated"
LOG_FILE = AUDIT_DIR / "metadata-cleanup-log-2026-06-15.md"

TODAY = datetime.now().strftime("%Y-%m-%d")


def generate_id(file_path):
    """基于文件名生成 id"""
    return file_path.stem


def normalize_status_value(value):
    """统一 status/trust_level 值格式：去除引号"""
    if value is None:
        return None
    value = str(value).strip()
    # 去除首尾引号
    if (value.startswith('"') and value.endswith('"')) or \
       (value.startswith("'") and value.endswith("'")):
        value = value[1:-1]
    return value


def has_field(frontmatter_text, key):
    """检查 frontmatter 中是否已有某字段"""
    pattern = re.compile(rf'^{re.escape(key)}:\s*', re.MULTILINE)
    return bool(pattern.search(frontmatter_text))


def add_field(frontmatter_text, key, value):
    """在 frontmatter 末尾添加字段"""
    return frontmatter_text.rstrip() + f"\n{key}: {value}\n"


def update_field_format(frontmatter_text, key, transform_func):
    """更新某字段的值格式"""
    pattern = re.compile(rf'^{re.escape(key)}:\s*(.*?)$', re.MULTILINE)
    
    def repl(match):
        old_value = match.group(1)
        new_value = transform_func(old_value.strip())
        if new_value != old_value.strip():
            return f"{key}: {new_value}"
        return match.group(0)
    
    return pattern.sub(repl, frontmatter_text)


def process_file(file_path, changes):
    """处理单个文件，返回变更记录"""
    content = file_path.read_text(encoding="utf-8")
    
    if not content.startswith("---"):
        changes.append({
            "file": str(file_path.relative_to(WIKI_DIR.parent)),
            "action": "skipped",
            "reason": "no frontmatter"
        })
        return
    
    parts = content.split("---", 2)
    if len(parts) < 3:
        changes.append({
            "file": str(file_path.relative_to(WIKI_DIR.parent)),
            "action": "skipped",
            "reason": "invalid frontmatter"
        })
        return
    
    fm_text = parts[1]
    body = parts[2]
    file_changes = []
    
    # 1. 补全 id
    if not has_field(fm_text, "id"):
        new_id = generate_id(file_path)
        fm_text = add_field(fm_text, "id", f'"{new_id}"')
        file_changes.append(f"add id: {new_id}")
    
    # 2. 补全 author
    if not has_field(fm_text, "author"):
        fm_text = add_field(fm_text, "author", "legacy")
        file_changes.append("add author: legacy")
    
    # 3. 补全 reviewed_by
    if not has_field(fm_text, "reviewed_by"):
        fm_text = add_field(fm_text, "reviewed_by", "pending")
        file_changes.append("add reviewed_by: pending")
    
    # 4. 补全 created_at
    if not has_field(fm_text, "created_at"):
        fm_text = add_field(fm_text, "created_at", f'"{TODAY}"')
        file_changes.append(f"add created_at: {TODAY}")
    
    # 5. 统一 status 格式
    def normalize_status(v):
        nv = normalize_status_value(v)
        return nv if nv else v
    fm_text = update_field_format(fm_text, "status", normalize_status)
    
    # 6. 统一 trust_level 格式
    fm_text = update_field_format(fm_text, "trust_level", normalize_status)
    
    # 7. 统一 confidence 格式：去除注释，保留数值
    def normalize_confidence(v):
        m = re.search(r'(\d+\.?\d*)', v)
        if m:
            return m.group(1)
        return v
    fm_text = update_field_format(fm_text, "confidence", normalize_confidence)
    
    # 验证修复后的 YAML
    try:
        yaml.safe_load(fm_text)
    except yaml.YAMLError as e:
        changes.append({
            "file": str(file_path.relative_to(WIKI_DIR.parent)),
            "action": "error",
            "reason": f"YAML parse error after modification: {e}"
        })
        return
    
    if file_changes:
        new_content = f"---{fm_text}---{body}"
        file_path.write_text(new_content, encoding="utf-8")
        changes.append({
            "file": str(file_path.relative_to(WIKI_DIR.parent)),
            "action": "modified",
            "changes": "; ".join(file_changes)
        })
    else:
        changes.append({
            "file": str(file_path.relative_to(WIKI_DIR.parent)),
            "action": "no-change",
            "reason": "all required fields present"
        })


def deprecate_empty_files(changes):
    """废弃 0 字节或内容极少的占位文件"""
    DEPRECATED_DIR.mkdir(parents=True, exist_ok=True)
    
    for md_file in sorted(WIKI_DIR.rglob("*.md")):
        if md_file.name in ("index.md", "log.md", "contradictions.md", "concept-card-index-latest.md"):
            continue
        
        content = md_file.read_text(encoding="utf-8")
        if len(content.strip()) == 0:
            # 0 字节文件，废弃
            deprecated_name = md_file.stem + "-deprecated.md"
            deprecated_path = DEPRECATED_DIR / deprecated_name
            shutil.move(str(md_file), str(deprecated_path))
            changes.append({
                "file": str(md_file.relative_to(WIKI_DIR.parent)),
                "action": "deprecated",
                "reason": "empty file (0 bytes)",
                "moved_to": str(deprecated_path.relative_to(WIKI_DIR.parent.parent))
            })


def generate_log(changes):
    """生成变更日志"""
    modified = [c for c in changes if c["action"] == "modified"]
    deprecated = [c for c in changes if c["action"] == "deprecated"]
    skipped = [c for c in changes if c["action"] in ("skipped", "no-change")]
    errors = [c for c in changes if c["action"] == "error"]
    
    lines = [
        "# 30_wiki 元数据治理变更日志",
        "",
        f"> 执行时间：{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}",
        f"> 总处理文件数：{len(changes)}",
        f"> 修改文件数：{len(modified)}",
        f"> 废弃文件数：{len(deprecated)}",
        f"> 跳过/无需修改：{len(skipped)}",
        f"> 错误数：{len(errors)}",
        "",
        "## 一、废弃文件",
        "",
        "| 原路径 | 原因 | 移动至 |",
        "|---|---|---|",
    ]
    for c in deprecated:
        lines.append(f"| {c['file']} | {c['reason']} | {c.get('moved_to', '')} |")
    
    lines.extend([
        "",
        "## 二、修改文件（前 200 条）",
        "",
        "| 文件路径 | 变更内容 |",
        "|---|---|",
    ])
    for c in modified[:200]:
        lines.append(f"| {c['file']} | {c['changes']} |")
    
    if len(modified) > 200:
        lines.append(f"| ... | 共 {len(modified)} 条修改，超出部分省略 |")
    
    if errors:
        lines.extend([
            "",
            "## 三、错误文件",
            "",
            "| 文件路径 | 错误原因 |",
            "|---|---|",
        ])
        for c in errors:
            lines.append(f"| {c['file']} | {c['reason']} |")
    
    lines.append("")
    LOG_FILE.write_text("\n".join(lines), encoding="utf-8")


def main():
    changes = []
    
    # 第一步：废弃空文件
    print("Step 1: 废弃空文件...")
    deprecate_empty_files(changes)
    
    # 第二步：处理所有文件的元数据
    print("Step 2: 治理元数据...")
    for md_file in sorted(WIKI_DIR.rglob("*.md")):
        if md_file.name in ("index.md", "log.md", "contradictions.md", "concept-card-index-latest.md"):
            continue
        process_file(md_file, changes)
    
    # 第三步：生成日志
    print("Step 3: 生成变更日志...")
    generate_log(changes)
    
    print(f"\n完成：")
    print(f"- 修改：{len([c for c in changes if c['action'] == 'modified'])} 个文件")
    print(f"- 废弃：{len([c for c in changes if c['action'] == 'deprecated'])} 个文件")
    print(f"- 错误：{len([c for c in changes if c['action'] == 'error'])} 个文件")
    print(f"- 日志：{LOG_FILE}")


if __name__ == "__main__":
    main()
