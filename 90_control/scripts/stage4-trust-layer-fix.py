#!/usr/bin/env python3
"""
阶段 4：按可信度分层审查 - 批量修正脚本
自动处理：
1. 缺失 confidence 的卡片（按 status/source 填充默认值）
2. 缺失 trust_level 的卡片（按 status/source/confidence 填充默认值）
3. 高置信低来源的卡片（下调 confidence）

不处理：
- approved_but_pending（需人工确认）
- date_inconsistency（需人工复核）
"""

import re
import sys
if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")
if hasattr(sys.stderr, "reconfigure"):
    sys.stderr.reconfigure(encoding="utf-8", errors="replace")
import yaml
from pathlib import Path
from collections import defaultdict

WIKI_DIR = Path("C:/Users/Administrator/Desktop/wiki/30_wiki")
OUTPUT_DIR = Path("C:/Users/Administrator/Desktop/wiki/60_feedback/audit")
OUTPUT_LOG = OUTPUT_DIR / "kcard-stage4-fix-log-2026-06-15.md"


def parse_frontmatter(text):
    if not text.startswith("---\n"):
        return None, text, None
    end_idx = text.find("\n---\n", 4)
    if end_idx == -1:
        return None, text, None
    fm_text = text[4:end_idx]
    body = text[end_idx + 5 :]
    try:
        fm = yaml.safe_load(fm_text)
        if not isinstance(fm, dict):
            fm = {}
        return fm, body, fm_text
    except Exception:
        return None, text, None


def count_source_refs(fm):
    refs = fm.get("source_refs")
    if not refs:
        return 0
    if isinstance(refs, str):
        return 1 if refs.strip() else 0
    if isinstance(refs, list):
        return len([r for r in refs if str(r).strip()])
    return 0


def suggest_confidence(status, source_count):
    status = str(status).strip().lower().strip('"')
    if status == "draft":
        return 0.70 if source_count >= 1 else 0.60
    if status == "proposed":
        return 0.65
    if status == "enriched":
        if source_count >= 2:
            return 0.85
        return 0.80 if source_count >= 1 else 0.75
    if status in ("reviewed", "active"):
        return 0.85
    if status == "stable":
        return 0.90
    if status == "needs-review":
        return 0.70
    if status in ("deprecated", "superseded"):
        return 0.75
    return 0.75


def suggest_trust(status, source_count, confidence):
    status = str(status).strip().lower().strip('"')
    if status in ("draft", "proposed"):
        return "low"
    if status == "needs-review":
        return "medium-low"
    if status == "enriched":
        if source_count >= 2 or (confidence is not None and confidence >= 0.85):
            return "medium-high"
        return "medium" if source_count >= 1 else "medium-low"
    if status in ("reviewed", "active"):
        return "high"
    if status == "stable":
        return "high"
    if status in ("deprecated", "superseded"):
        return "medium-low"
    return "medium"


def update_frontmatter_text(fm_text, fm, changes):
    """在原始 frontmatter 文本中更新指定字段，保留格式"""
    lines = fm_text.split("\n")
    updated_keys = set()
    new_lines = []
    
    for line in lines:
        # 检查是否是要修改的键
        matched = False
        for key in changes:
            # 匹配 key: ... 或 key: 开头（考虑列表）
            if re.match(rf"^{re.escape(key)}\s*:", line.strip()):
                # 如果值在下一行缩进（列表或对象），这里简化处理：只替换当前行的标量值
                if line.strip().endswith(":"):
                    # 可能是多行结构，不在这里替换
                    pass
                else:
                    # 保留缩进
                    indent = line[: len(line) - len(line.lstrip())]
                    new_lines.append(f"{indent}{key}: {changes[key]}")
                    updated_keys.add(key)
                    matched = True
                    break
        if not matched:
            new_lines.append(line)
    
    # 对未更新的键，在合适位置插入
    for key in changes:
        if key not in updated_keys:
            # 简单插入到末尾
            new_lines.append(f"{key}: {changes[key]}")
    
    return "\n".join(new_lines)


def format_yaml_value(value):
    """格式化 YAML 值，字符串加引号避免中文问题"""
    if isinstance(value, str):
        return f'"{value}"'
    return str(value)


def main():
    files = list(WIKI_DIR.rglob("*.md"))
    log_entries = []
    
    stats = {
        "filled_confidence": 0,
        "filled_trust": 0,
        "lowered_confidence": 0,
        "skipped_yaml_error": 0,
        "skipped_no_frontmatter": 0,
    }

    for file_path in files:
        text = file_path.read_text(encoding="utf-8")
        result = parse_frontmatter(text)
        if result[0] is None:
            if result[2] is None:
                stats["skipped_no_frontmatter"] += 1
            else:
                stats["skipped_yaml_error"] += 1
            continue
        
        fm, body, fm_text = result
        original_fm_text = fm_text
        
        status = str(fm.get("status", "") or "").strip().lower().strip('"')
        reviewed_by = str(fm.get("reviewed_by", "") or "").strip()
        confidence_raw = fm.get("confidence")
        trust_level = str(fm.get("trust_level", "") or "").strip().lower()
        source_count = count_source_refs(fm)
        
        try:
            confidence = float(confidence_raw) if confidence_raw is not None else None
        except (ValueError, TypeError):
            confidence = None
        
        changes = {}
        log_entry = {"file": str(file_path), "actions": []}
        
        # 1. 缺失 confidence
        if confidence is None:
            new_conf = suggest_confidence(status, source_count)
            changes["confidence"] = new_conf
            confidence = new_conf
            log_entry["actions"].append(f"补充 confidence: {new_conf}")
            stats["filled_confidence"] += 1
        
        # 2. 缺失 trust_level
        if not trust_level:
            new_trust = suggest_trust(status, source_count, confidence)
            changes["trust_level"] = new_trust
            log_entry["actions"].append(f"补充 trust_level: {new_trust}")
            stats["filled_trust"] += 1
        
        # 3. 高置信低来源
        if confidence is not None and confidence >= 0.90 and source_count < 2:
            if confidence >= 0.95:
                new_conf = 0.85
            else:
                new_conf = 0.80
            changes["confidence"] = new_conf
            log_entry["actions"].append(f"confidence 从 {confidence} 下调至 {new_conf}（source 仅 {source_count} 个）")
            stats["lowered_confidence"] += 1
            confidence = new_conf
        
        if changes:
            # 更新 frontmatter 文本
            # 使用 yaml dump 重新生成，保留键顺序
            new_fm = dict(fm)
            for key, val in changes.items():
                new_fm[key] = val
            
            # 重新生成 frontmatter，保持原始顺序
            ordered_fm = {}
            for key in fm.keys():
                ordered_fm[key] = new_fm.get(key)
            for key in changes:
                if key not in ordered_fm:
                    ordered_fm[key] = changes[key]
            
            # 手动生成 YAML，避免中文引号问题
            yaml_lines = []
            for key, val in ordered_fm.items():
                if val is None:
                    continue
                if isinstance(val, list):
                    yaml_lines.append(f"{key}:")
                    for item in val:
                        yaml_lines.append(f"  - {format_yaml_value(item)}")
                elif isinstance(val, dict):
                    yaml_lines.append(f"{key}:")
                    for k, v in val.items():
                        yaml_lines.append(f"  {k}: {format_yaml_value(v)}")
                else:
                    yaml_lines.append(f"{key}: {format_yaml_value(val)}")
            
            new_fm_text = "\n".join(yaml_lines)
            new_text = f"---\n{new_fm_text}\n---\n{body}"
            file_path.write_text(new_text, encoding="utf-8")
            log_entries.append(log_entry)

    # 生成日志报告
    lines = [
        "# 阶段 4 可信度分层批量修正日志",
        "",
        f"**处理时间**：2026-06-15  ",
        f"**处理范围**：30_wiki 全库 {len(files)} 张卡片  ",
        "**处理规则**：",
        "- 缺失 confidence：按 status/source 填充默认值",
        "- 缺失 trust_level：按 status/source/confidence 填充默认值",
        "- 高置信低来源：confidence ≥ 0.95 → 0.85；0.90–0.94 → 0.80",
        "",
        "## 统计",
        "",
        f"- 补充 confidence：{stats['filled_confidence']} 张",
        f"- 补充 trust_level：{stats['filled_trust']} 张",
        f"- 下调 confidence：{stats['lowered_confidence']} 张",
        f"- 跳过（无 frontmatter）：{stats['skipped_no_frontmatter']} 张",
        f"- 跳过（YAML 解析错误）：{stats['skipped_yaml_error']} 张",
        "",
        "## 详细变更清单",
        "",
    ]
    
    for entry in log_entries:
        rel_path = Path(entry["file"]).relative_to(Path("C:/Users/Administrator/Desktop"))
        lines.append(f"### `{rel_path}`")
        for action in entry["actions"]:
            lines.append(f"- {action}")
        lines.append("")
    
    OUTPUT_LOG.write_text("\n".join(lines), encoding="utf-8")
    print(f"批量修正完成：{OUTPUT_LOG}")
    print(f"统计：{stats}")


if __name__ == "__main__":
    main()
