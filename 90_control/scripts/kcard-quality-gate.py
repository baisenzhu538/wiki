#!/usr/bin/env python3
"""
KDO 卡片质量门禁脚本
扫描 30_wiki 下所有卡片，按 90_control/quality-gates/kcard.md 规则检查 P0/P1 问题。

用法：
    python kcard-quality-gate.py [--fix-p0]

--fix-p0：尝试自动修复部分 P0 问题（谨慎使用，修复前建议先打 git tag）
"""

import argparse
import json
import re
import yaml
from pathlib import Path
from collections import defaultdict

WIKI_DIR = Path("C:/Users/Administrator/Desktop/wiki/30_wiki")
REPORT_DIR = Path("C:/Users/Administrator/Desktop/wiki/60_feedback/audit")

VALID_TYPES = {
    "concept", "skill", "case", "framework", "dark-knowledge", "tool",
    "decision", "proposal", "improvement-plan", "entity", "analysis",
    "system", "requirement", "report", "index", "dk"
}

VALID_STATUSES = {"draft", "enriched", "reviewed", "stable", "proposed", "needs-review", "deprecated", "superseded", "active", "redirect", "pending", "revised"}

VALID_TRUST_LEVELS = {"low", "medium-low", "medium", "medium-high", "high"}


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
    except Exception as e:
        return None, text, str(e)


def count_source_refs(fm):
    refs = fm.get("source_refs")
    if not refs:
        return 0
    if isinstance(refs, str):
        return 1 if str(refs).strip() and str(refs).strip() != "None" else 0
    if isinstance(refs, list):
        return len([r for r in refs if str(r).strip() and str(r).strip() != "None"])
    return 0


def extract_wikilinks(text):
    """提取 [[...]] 链接"""
    return re.findall(r"\[\[([^\]]+)\]\]", text)


def check_card(file_path, all_ids):
    text = file_path.read_text(encoding="utf-8")
    result = parse_frontmatter(text)
    issues = {"p0": [], "p1": []}
    fm = None

    if result[0] is None:
        issues["p0"].append(f"YAML 解析错误: {result[2]}")
        return issues, fm

    fm, body, _ = result

    # P0 检查
    # 1. id
    card_id = str(fm.get("id", "")).strip().strip('"')
    if not card_id:
        issues["p0"].append("缺少 id")
    elif card_id != file_path.stem:
        issues["p0"].append(f"id ({card_id}) 与文件名 ({file_path.stem}) 不一致")

    # 2. title
    title = fm.get("title")
    if not title or str(title).strip() in ("", "None"):
        issues["p0"].append("缺少 title")

    # 3. type
    card_type = str(fm.get("type", "")).strip().strip('"').lower()
    if not card_type:
        issues["p0"].append("缺少 type")
    elif card_type not in VALID_TYPES:
        issues["p1"].append(f"type 值异常: {card_type}")

    # 4. status（先提取，后续多处使用）
    status = str(fm.get("status", "") or "").strip().strip('"').lower()

    # 5. source_refs
    source_count = count_source_refs(fm)
    if source_count == 0:
        if status in ("enriched", "reviewed", "stable", "active"):
            issues["p0"].append("source_refs 为空")
        else:
            issues["p1"].append("source_refs 为空")

    # 6. author
    author = str(fm.get("author", "") or "").strip().strip('"')
    if not author:
        issues["p0"].append("author 为空")
    elif author == "legacy":
        if status in ("enriched", "reviewed", "stable", "active"):
            issues["p0"].append("author=legacy 但 status 非 draft")
        else:
            issues["p1"].append("author=legacy，建议替换为真实作者")

    # 7. reviewed_by
    reviewed_by = str(fm.get("reviewed_by", "") or "").strip().strip('"')
    if reviewed_by == "pending" and status in ("enriched", "reviewed", "stable"):
        issues["p0"].append(f"status={status} 但 reviewed_by=pending")

    # 7. status
    if status and status not in VALID_STATUSES:
        issues["p1"].append(f"status 值异常: {status}")

    # 8. confidence
    confidence_raw = fm.get("confidence")
    confidence = None
    if confidence_raw is None:
        issues["p0"].append("缺少 confidence")
    else:
        try:
            confidence = float(confidence_raw)
            if not (0.0 <= confidence <= 1.0):
                issues["p0"].append(f"confidence 越界: {confidence}")
        except (ValueError, TypeError):
            issues["p0"].append(f"confidence 非数字: {confidence_raw}")

    # 9. trust_level
    trust_level = str(fm.get("trust_level", "") or "").strip().strip('"').lower()
    if not trust_level:
        issues["p0"].append("缺少 trust_level")
    elif trust_level not in VALID_TRUST_LEVELS:
        issues["p1"].append(f"trust_level 值异常: {trust_level}")

    # 10. domain
    domain = fm.get("domain")
    if not domain:
        issues["p0"].append("缺少 domain")
    elif isinstance(domain, list):
        if len(domain) == 0:
            issues["p0"].append("domain 为空列表")
        elif any(str(d).startswith("[") for d in domain):
            issues["p0"].append("domain 包含字符串化列表残留")
    elif isinstance(domain, str):
        if domain.strip() == "" or domain.strip() == "None":
            issues["p0"].append("domain 为空字符串")
        elif domain.startswith("["):
            issues["p0"].append("domain 为字符串化列表")

    # 11. dangling links
    related = fm.get("related") or []
    if isinstance(related, str):
        related = [related]
    related_links_raw = [str(r).strip().strip('"') for r in related if r is not None and str(r).strip()]
    body_links_raw = extract_wikilinks(body)
    all_links_raw = set(related_links_raw + body_links_raw)
    dangling = []
    for link in all_links_raw:
        # Normalize: strip multiple bracket layers + quotes
        link_id = link.strip()
        while link_id.startswith("[[") and link_id.endswith("]]"):
            link_id = link_id[2:-2]
        link_id = link_id.strip().strip("'\"").strip()
        link_id = link_id.split("#")[0].strip()
        if link_id and link_id not in all_ids:
            dangling.append(link_id)
    if dangling:
        issues["p1"].append(f"dangling 链接: {', '.join(dangling[:5])}")

    # P1 检查
    # 1. confidence/trust 一致性
    if confidence is not None:
        if confidence >= 0.90 and source_count < 2:
            issues["p1"].append(f"confidence={confidence} 但 source 仅 {source_count} 个")
        if status == "draft" and confidence >= 0.85:
            issues["p1"].append(f"status=draft 但 confidence={confidence}")
        if trust_level in ("low", "medium-low") and confidence >= 0.85:
            issues["p1"].append(f"trust_level={trust_level} 但 confidence={confidence}")
        if trust_level == "high" and source_count < 2:
            issues["p1"].append(f"trust_level=high 但 source 仅 {source_count} 个")

    # 2. OCR 卡默认低信任
    if card_id.startswith("ocr-"):
        if trust_level not in ("low", "medium-low"):
            issues["p1"].append(f"OCR 卡 trust_level={trust_level}，建议 low 或 medium-low")
        if confidence is not None and confidence > 0.60:
            issues["p1"].append(f"OCR 卡 confidence={confidence}，建议 ≤0.60")

    # 3. status 与 reviewed_by 一致性（更严格）
    if status == "reviewed" and (not reviewed_by or reviewed_by == "pending"):
        issues["p1"].append("status=reviewed 但 reviewed_by 无效")

    # 4. source_refs 中的 src_ID 是否在 source 注册表中存在
    try:
        sid_map = json.loads((Path(WIKI_DIR).parent / ".kdo" / "source_id_map.json").read_text(encoding="utf-8"))
    except Exception:
        sid_map = {}
    refs = fm.get("source_refs", []) or []
    if isinstance(refs, str): refs = [refs]
    if not isinstance(refs, list): refs = []
    missing_srcs = []
    for r in refs:
        r_str = str(r).strip()
        m = re.match(r'(src_\d+_\w{8})', r_str)
        if m and m.group(1) not in sid_map:
            missing_srcs.append(m.group(1))
    if missing_srcs:
        issues["p1"].append(f"source_refs 中的 src ID 未注册: {', '.join(missing_srcs[:3])}")

    # 5. contradicts 字段残留检测（应改用 related）
    if fm.get("contradicts"):
        issues["p1"].append("frontmatter 含 contradicts 字段，应改为 related（语义修正 2026-06-15）")

    # 6. reviewed_by 与 author 相同且非"黄药师/欧阳锋"（自审）
    if reviewed_by and author and reviewed_by == author and author not in ("黄药师", "欧阳锋"):
        issues["p1"].append(f"自审: author={author}, reviewed_by={reviewed_by} 相同")

    return issues, fm


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--fix-p0", action="store_true", help="尝试自动修复部分 P0 问题")
    args = parser.parse_args()

    files = [f for f in WIKI_DIR.rglob("*.md") if "_archive" not in f.parts and "raw" not in f.parts]
    all_ids = {f.stem for f in files}

    stats = {"total": len(files), "p0": 0, "p1": 0, "clean": 0, "yaml_error": 0}
    p0_issues = defaultdict(list)
    p1_issues = defaultdict(list)

    for file_path in files:
        issues, fm = check_card(file_path, all_ids)
        rel_path = file_path.relative_to(WIKI_DIR)
        if issues["p0"]:
            stats["p0"] += 1
            p0_issues[str(rel_path)] = issues["p0"]
        if issues["p1"]:
            stats["p1"] += 1
            p1_issues[str(rel_path)] = issues["p1"]
        if not issues["p0"] and not issues["p1"]:
            stats["clean"] += 1
        if fm is None:
            stats["yaml_error"] += 1

    # 生成报告
    lines = [
        "# KDO 卡片质量门禁报告",
        "",
        f"**扫描时间**：2026-06-15  ",
        f"**扫描范围**：30_wiki 全库 {stats['total']} 张卡片  ",
        f"**P0 阻塞问题卡片**：{stats['p0']} 张  ",
        f"**P1 修复问题卡片**：{stats['p1']} 张  ",
        f"**完全干净卡片**：{stats['clean']} 张  ",
        f"**YAML 解析错误**：{stats['yaml_error']} 张  ",
        "",
        "---",
        "",
        "## P0 阻塞问题清单",
        "",
    ]

    if p0_issues:
        lines.append("| 文件 | P0 问题 |")
        lines.append("|---|---|")
        for file, issues in sorted(p0_issues.items()):
            lines.append(f"| `{file}` | {'; '.join(issues)} |")
    else:
        lines.append("无 P0 阻塞问题。")

    lines.extend(["", "---", "", "## P1 修复问题清单", ""])

    if p1_issues:
        lines.append("| 文件 | P1 问题 |")
        lines.append("|---|---|")
        for file, issues in sorted(p1_issues.items()):
            lines.append(f"| `{file}` | {'; '.join(issues)} |")
    else:
        lines.append("无 P1 修复问题。")

    lines.extend([
        "",
        "---",
        "",
        "## 使用说明",
        "",
        "运行门禁脚本：",
        "```bash",
        "python 90_control/scripts/kcard-quality-gate.py",
        "```",
        "",
        "P0 问题必须在卡片进入 enriched/reviewed/stable 前修复。",
        "P1 问题应在发布前修复。",
    ])

    report_path = REPORT_DIR / "kcard-quality-gate-report-2026-06-15.md"
    report_path.parent.mkdir(parents=True, exist_ok=True)
    report_path.write_text("\n".join(lines), encoding="utf-8")

    print(f"报告已生成：{report_path}")
    print(f"统计：{stats}")


if __name__ == "__main__":
    main()
