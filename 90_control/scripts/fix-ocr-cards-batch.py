#!/usr/bin/env python3
"""
批量降级 OCR 卡片：
- trust_level 设为 low
- confidence 设为 0.6（如果当前 > 0.6）
- status 如为 enriched/reviewed/stable，降级为 draft
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
REPORT_DIR = Path("C:/Users/Administrator/Desktop/wiki/60_feedback/audit")


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
        return fm, text[end_idx + 5:], fm_text
    except Exception as e:
        return None, text, str(e)


def format_scalar(val):
    if isinstance(val, str):
        if re.search(r'[\u4e00-\u9fff\s\[\]:,]', val) or val in ("true", "false", "null", "yes", "no", "on", "off"):
            escaped = val.replace('\\', '\\\\').replace('"', '\\"')
            return f'"{escaped}"'
        return val
    return str(val)


def rebuild_frontmatter(fm, original_keys):
    lines = []
    for key in original_keys:
        if key not in fm:
            continue
        val = fm[key]
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


def main():
    files = list(WIKI_DIR.rglob("*.md"))
    fixed = []
    stats = defaultdict(int)
    
    for file_path in files:
        text = file_path.read_text(encoding="utf-8")
        result = parse_frontmatter(text)
        if result[0] is None:
            continue
        
        fm, body, fm_text = result
        card_id = str(fm.get("id", "") or "").strip().strip('"')
        
        if not card_id.startswith("ocr-"):
            continue
        
        modified = False
        actions = []
        
        # 1. trust_level 设为 low
        current_trust = str(fm.get("trust_level", "") or "").strip().strip('"').lower()
        if current_trust != "low":
            fm["trust_level"] = "low"
            actions.append(f"trust_level: {current_trust or '(empty)'} → low")
            modified = True
            stats["trust_downgraded"] += 1
        
        # 2. confidence 设为 0.6（如果当前 > 0.6）
        confidence_raw = fm.get("confidence")
        try:
            confidence = float(confidence_raw) if confidence_raw is not None else None
        except (ValueError, TypeError):
            confidence = None
        
        if confidence is None or confidence > 0.6:
            old_conf = confidence if confidence is not None else "(empty)"
            fm["confidence"] = 0.6
            actions.append(f"confidence: {old_conf} → 0.6")
            modified = True
            stats["confidence_downgraded"] += 1
        
        # 3. status 降级
        status = str(fm.get("status", "") or "").strip().strip('"').lower()
        if status in ("enriched", "reviewed", "stable"):
            fm["status"] = "draft"
            actions.append(f"status: {status} → draft")
            modified = True
            stats["status_downgraded"] += 1
        
        # 4. reviewed_by 设为 pending（如果之前不是 pending）
        reviewed_by = str(fm.get("reviewed_by", "") or "").strip().strip('"')
        if reviewed_by != "pending":
            fm["reviewed_by"] = "pending"
            actions.append(f"reviewed_by: {reviewed_by or '(empty)'} → pending")
            modified = True
            stats["reviewer_reset"] += 1
        
        if modified:
            original_keys = list(fm.keys())
            new_fm_text = rebuild_frontmatter(fm, original_keys)
            new_text = f"---\n{new_fm_text}\n---\n{body}"
            file_path.write_text(new_text, encoding="utf-8")
            fixed.append({
                "file": str(file_path.relative_to(WIKI_DIR)),
                "actions": actions,
            })
    
    # 生成报告
    lines = [
        "# OCR 卡片批量降级报告",
        "",
        f"**修复时间**：2026-06-15  ",
        f"**修复 OCR 卡片数**：{len(fixed)}  ",
        "",
        "## 降级统计",
        "",
    ]
    for key, count in sorted(stats.items(), key=lambda x: -x[1]):
        label = {
            "trust_downgraded": "trust_level 降级为 low",
            "confidence_downgraded": "confidence 降级为 0.6",
            "status_downgraded": "status 降级为 draft",
            "reviewer_reset": "reviewed_by 重置为 pending",
        }.get(key, key)
        lines.append(f"- {label}: {count} 张")
    
    lines.extend(["", "## 修复文件清单", ""])
    for item in fixed:
        lines.append(f"### `{item['file']}`")
        for action in item["actions"]:
            lines.append(f"- {action}")
        lines.append("")
    
    report_path = REPORT_DIR / "kcard-ocr-cards-downgrade-report-2026-06-15.md"
    report_path.write_text("\n".join(lines), encoding="utf-8")
    
    print(f"修复 OCR 卡片数：{len(fixed)}")
    print(f"统计：{dict(stats)}")
    print(f"报告：{report_path}")


if __name__ == "__main__":
    main()
