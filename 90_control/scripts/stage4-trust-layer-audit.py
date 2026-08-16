#!/usr/bin/env python3
"""
阶段 4：按可信度分层审查
扫描 30_wiki 卡片，识别并批量修正 confidence/trust_level/reviewed_by 等元数据问题。
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
from datetime import datetime

WIKI_DIR = Path("C:/Users/Administrator/Desktop/wiki/30_wiki")
OUTPUT_DIR = Path("C:/Users/Administrator/Desktop/wiki/60_feedback/audit")
OUTPUT_REPORT = OUTPUT_DIR / "kcard-stage4-trust-layer-report-2026-06-15.md"

APPROVAL_KEYWORDS = ["批准", "采纳", "回应", "审查", "同意", "通过", "确认"]
APPROVAL_REVIEWERS = ["欧阳锋", "黄药师", "老顽童", "王语嫣", "洪七公", "孔阳"]


def parse_frontmatter(text):
    if not text.startswith("---\n"):
        return None, text
    # 找到 frontmatter 结束位置（第二个 ---）
    end_idx = text.find("\n---\n", 4)
    if end_idx == -1:
        return None, text
    fm_text = text[4:end_idx]
    body = text[end_idx + 5 :]
    try:
        fm = yaml.safe_load(fm_text)
        return fm if isinstance(fm, dict) else {}, body
    except Exception:
        return None, text


def count_source_refs(fm):
    refs = fm.get("source_refs")
    if not refs:
        return 0
    if isinstance(refs, str):
        return 1 if refs.strip() else 0
    if isinstance(refs, list):
        return len([r for r in refs if str(r).strip()])
    return 0


def detect_approval_in_body(body, fm):
    """检测正文是否包含批准/采纳等字样及可能的 reviewer"""
    approved_by = None
    for reviewer in APPROVAL_REVIEWERS:
        if reviewer not in body:
            continue
        # 找到 reviewer 所在位置，检查周围是否有批准关键词
        for m in re.finditer(re.escape(reviewer), body):
            start = max(0, m.start() - 80)
            end = min(len(body), m.end() + 80)
            context = body[start:end]
            if any(kw in context for kw in APPROVAL_KEYWORDS):
                approved_by = reviewer
                break
        if approved_by:
            break
    return approved_by


def main():
    issues = {
        "approved_but_pending": [],
        "high_conf_low_sources": [],
        "missing_confidence": [],
        "missing_trust": [],
        "high_conf_low_trust": [],
        "date_inconsistency": [],
        "auto_fixable": [],
    }

    files = list(WIKI_DIR.rglob("*.md"))

    for file_path in files:
        text = file_path.read_text(encoding="utf-8")
        fm, body = parse_frontmatter(text)
        if fm is None:
            continue

        status = str(fm.get("status", "")).strip().lower()
        reviewed_by = str(fm.get("reviewed_by", "") or "").strip()
        confidence_raw = fm.get("confidence")
        trust_level = str(fm.get("trust_level", "") or "").strip().lower()
        source_count = count_source_refs(fm)

        try:
            confidence = float(confidence_raw) if confidence_raw is not None else None
        except (ValueError, TypeError):
            confidence = None

        # 1. 已批准但 reviewed_by pending
        if reviewed_by == "pending":
            approved_by = detect_approval_in_body(body, fm)
            if approved_by:
                issues["approved_but_pending"].append({
                    "file": str(file_path),
                    "approved_by": approved_by,
                    "status": status,
                })

        # 2. 高置信低来源
        if confidence is not None and confidence >= 0.90 and source_count < 2:
            issues["high_conf_low_sources"].append({
                "file": str(file_path),
                "confidence": confidence,
                "source_count": source_count,
                "status": status,
            })

        # 3. 缺失 confidence
        if confidence is None:
            issues["missing_confidence"].append({
                "file": str(file_path),
                "status": status,
                "source_count": source_count,
                "trust_level": trust_level,
            })

        # 4. 缺失 trust_level
        if not trust_level:
            issues["missing_trust"].append({
                "file": str(file_path),
                "status": status,
                "source_count": source_count,
                "confidence": confidence,
            })

        # 5. 高置信低信任
        if confidence is not None and confidence >= 0.85 and trust_level in ("low", "medium-low"):
            issues["high_conf_low_trust"].append({
                "file": str(file_path),
                "confidence": confidence,
                "trust_level": trust_level,
            })

        # 6. 日期字段不一致（简单检查）
        date_fields = {}
        for field in ["date", "created_at", "updated_at", "review_date"]:
            val = fm.get(field)
            if val:
                date_fields[field] = str(val)
        if date_fields:
            dates = list(date_fields.values())
            if len(set(dates)) > 1 and len(dates) >= 2:
                # 仅标记明显异常（如 date 与 created_at 不同且不是同一日）
                issues["date_inconsistency"].append({
                    "file": str(file_path),
                    "fields": date_fields,
                })

    # 生成报告
    lines = [
        "# 30_wiki 阶段 4 可信度分层审查报告",
        "",
        f"**报告日期**：2026-06-15  ",
        f"**审查角色**：王语嫣  ",
        f"**覆盖范围**：30_wiki 全库 {len(files)} 张卡片  ",
        "**本阶段目标**：识别 confidence/trust_level/reviewed_by 等可信度元数据问题，批量修正可规则化的问题。",
        "",
        "---",
        "",
        "## 一、问题统计",
        "",
    ]

    lines.append("| 问题类型 | 数量 | 是否可批量自动处理 |")
    lines.append("|---|---|---|")
    for key, label, auto in [
        ("approved_but_pending", "正文已批准但 reviewed_by 仍为 pending", "部分可（需确认 reviewer）"),
        ("high_conf_low_sources", "confidence ≥ 0.90 但 source < 2", "可"),
        ("missing_confidence", "缺失 confidence", "可（按 status/source 填充默认值）"),
        ("missing_trust", "缺失 trust_level", "可（按 status/source 填充默认值）"),
        ("high_conf_low_trust", "confidence ≥ 0.85 但 trust_level 为 low/medium-low", "可"),
        ("date_inconsistency", "日期字段不一致", "需人工复核"),
    ]:
        lines.append(f"| {label} | {len(issues[key])} | {auto} |")

    lines.extend(["", "---", "", "## 二、正文已批准但 reviewed_by 仍为 pending", ""])
    if issues["approved_but_pending"]:
        lines.append("| 文件 | 检测到的批准人 | 当前 status | 建议操作 |")
        lines.append("|---|---|---|---|")
        for item in issues["approved_but_pending"]:
            lines.append(f"| `{item['file']}` | {item['approved_by']} | {item['status']} | 更新 reviewed_by 为 {item['approved_by']}，status 视情况改为 approved/reviewed |")
    else:
        lines.append("未发现此类问题。")

    lines.extend(["", "---", "", "## 三、高置信低来源卡片", ""])
    if issues["high_conf_low_sources"]:
        lines.append("| 文件 | confidence | source 数量 | status | 建议操作 |")
        lines.append("|---|---|---|---|---|")
        for item in issues["high_conf_low_sources"]:
            new_conf = 0.85 if item["confidence"] >= 0.95 else 0.80
            lines.append(f"| `{item['file']}` | {item['confidence']} | {item['source_count']} | {item['status']} | 下调 confidence 至 {new_conf} |")
    else:
        lines.append("未发现此类问题。")

    lines.extend(["", "---", "", "## 四、缺失 confidence 的卡片", ""])
    if issues["missing_confidence"]:
        lines.append("| 文件 | status | source 数量 | 当前 trust_level | 建议 confidence |")
        lines.append("|---|---|---|---|---|")
        for item in issues["missing_confidence"]:
            suggested = suggest_confidence(item["status"], item["source_count"])
            lines.append(f"| `{item['file']}` | {item['status']} | {item['source_count']} | {item['trust_level'] or '(empty)'} | {suggested} |")
    else:
        lines.append("未发现此类问题。")

    lines.extend(["", "---", "", "## 五、缺失 trust_level 的卡片", ""])
    if issues["missing_trust"]:
        lines.append("| 文件 | status | source 数量 | 当前 confidence | 建议 trust_level |")
        lines.append("|---|---|---|---|---|")
        for item in issues["missing_trust"]:
            suggested = suggest_trust(item["status"], item["source_count"], item["confidence"])
            lines.append(f"| `{item['file']}` | {item['status']} | {item['source_count']} | {item['confidence'] if item['confidence'] is not None else '(empty)'} | {suggested} |")
    else:
        lines.append("未发现此类问题。")

    lines.extend(["", "---", "", "## 六、高置信低信任卡片", ""])
    if issues["high_conf_low_trust"]:
        lines.append("| 文件 | confidence | trust_level | 建议操作 |")
        lines.append("|---|---|---|---|")
        for item in issues["high_conf_low_trust"]:
            lines.append(f"| `{item['file']}` | {item['confidence']} | {item['trust_level']} | 下调 confidence 至 0.80 或提升 trust_level |")
    else:
        lines.append("未发现此类问题。")

    lines.extend(["", "---", "", "## 七、日期字段不一致卡片", ""])
    if issues["date_inconsistency"]:
        lines.append("| 文件 | 日期字段 | 建议操作 |")
        lines.append("|---|---|---|")
        for item in issues["date_inconsistency"]:
            fields_str = ", ".join(f"{k}={v}" for k, v in item["fields"].items())
            lines.append(f"| `{item['file']}` | {fields_str} | 人工复核 |")
    else:
        lines.append("未发现此类问题。")

    lines.extend([
        "",
        "---",
        "",
        "## 八、批量处理规则",
        "",
        "### 8.1 自动下调规则",
        "- confidence ≥ 0.95 且 source < 2 → 0.85",
        "- confidence 0.90–0.94 且 source < 2 → 0.80",
        "- confidence ≥ 0.85 且 trust_level 为 low/medium-low → 0.80",
        "",
        "### 8.2 默认值填充规则",
        "| status | source 数量 | confidence | trust_level |",
        "|---|---|---|---|",
        "| draft | 0 | 0.60 | low |",
        "| draft | ≥1 | 0.70 | medium-low |",
        "| proposed | 任意 | 0.65 | low |",
        "| enriched | 0 | 0.75 | medium-low |",
        "| enriched | 1 | 0.80 | medium |",
        "| enriched | ≥2 | 0.85 | medium-high |",
        "| reviewed | 任意 | 0.85 | high |",
        "| stable | 任意 | 0.90 | high |",
        "| needs-review | 任意 | 0.70 | medium-low |",
        "",
        "### 8.3 已批准卡片更新规则",
        "- 正文检测到 reviewer + 批准关键词，且当前 reviewed_by=pending → 更新 reviewed_by 为检测到的 reviewer",
        "- 若 status 为 draft/proposed → 同时更新为 reviewed（最终是否 approved 需人工确认）",
    ])

    OUTPUT_REPORT.write_text("\n".join(lines), encoding="utf-8")
    print(f"报告已生成：{OUTPUT_REPORT}")
    print(f"问题统计：")
    for key in issues:
        print(f"  {key}: {len(issues[key])}")


def suggest_confidence(status, source_count):
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
    return 0.75


def suggest_trust(status, source_count, confidence):
    if status in ("draft", "proposed"):
        return "low"
    if status == "needs-review":
        return "medium-low"
    if status == "enriched":
        if source_count >= 2:
            return "medium-high"
        return "medium" if source_count >= 1 else "medium-low"
    if status in ("reviewed", "active"):
        return "high"
    if status == "stable":
        return "high"
    return "medium"


if __name__ == "__main__":
    main()
