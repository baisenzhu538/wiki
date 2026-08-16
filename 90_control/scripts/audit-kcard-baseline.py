#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
30_wiki 知识卡基线扫描脚本
生成全库卡片清单 CSV 和基线问题报告 Markdown
"""

import os
import sys
if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")
if hasattr(sys.stderr, "reconfigure"):
    sys.stderr.reconfigure(encoding="utf-8", errors="replace")
import re
import csv
import yaml
from pathlib import Path
from collections import Counter, defaultdict
from datetime import datetime

WIKI_DIR = Path("C:/Users/Administrator/Desktop/wiki/30_wiki")
OUTPUT_DIR = Path("C:/Users/Administrator/Desktop/wiki/60_feedback/audit")
OUTPUT_CSV = OUTPUT_DIR / "kcard-inventory-2026-06-14.csv"
OUTPUT_REPORT = OUTPUT_DIR / "kcard-baseline-report-2026-06-14.md"


def normalize_string(value):
    """统一字符串格式，去除引号和首尾空格"""
    if value is None:
        return ""
    if isinstance(value, str):
        return value.strip().strip('"').strip("'")
    return str(value)


def parse_frontmatter(file_path):
    """解析 Markdown 文件的 YAML frontmatter"""
    content = file_path.read_text(encoding="utf-8")
    if not content.startswith("---"):
        return None, content
    
    parts = content.split("---", 2)
    if len(parts) < 3:
        return None, content
    
    yaml_text = parts[1].strip()
    try:
        fm = yaml.safe_load(yaml_text) or {}
    except yaml.YAMLError as e:
        print(f"YAML parse error in {file_path}: {e}")
        return None, content
    
    return fm, parts[2]


def extract_fields(fm, file_path, body):
    """提取并规范化字段"""
    fields = {
        "file_path": str(file_path.relative_to(WIKI_DIR.parent)).replace("\\", "/"),
        "dir": file_path.parent.name,
        "file_size": len(body.encode("utf-8")),
        "id": normalize_string(fm.get("id", "")),
        "title": normalize_string(fm.get("title", "")),
        "type": normalize_string(fm.get("type", "")),
        "status": normalize_string(fm.get("status", "")),
        "author": normalize_string(fm.get("author", "")),
        "reviewed_by": normalize_string(fm.get("reviewed_by", "")),
        "confidence": "",
        "trust_level": normalize_string(fm.get("trust_level", "")),
        "source_refs_count": 0,
        "source_refs_has_theme": False,
        "domain_list": "",
        "tags_count": 0,
        "related_count": 0,
        "created_at": normalize_string(fm.get("created_at", "")),
        "updated_at": normalize_string(fm.get("updated_at", "")),
    }
    
    # confidence 处理：可能是数值、字符串、或带注释
    conf = fm.get("confidence")
    if conf is not None:
        if isinstance(conf, (int, float)):
            fields["confidence"] = float(conf)
        elif isinstance(conf, str):
            # 尝试提取数值，如 "0.8 # 全局置信度"
            m = re.search(r"(\d+\.?\d*)", conf)
            if m:
                try:
                    fields["confidence"] = float(m.group(1))
                except ValueError:
                    fields["confidence"] = conf
            else:
                fields["confidence"] = conf
    
    # source_refs
    source_refs = fm.get("source_refs", [])
    if isinstance(source_refs, list):
        fields["source_refs_count"] = len(source_refs)
        fields["source_refs_has_theme"] = any(
            isinstance(s, str) and s.startswith("theme-") for s in source_refs
        )
    elif isinstance(source_refs, str):
        fields["source_refs_count"] = 1
        fields["source_refs_has_theme"] = source_refs.startswith("theme-")
    
    # domain
    domain = fm.get("domain", [])
    if isinstance(domain, list):
        fields["domain_list"] = ", ".join(normalize_string(d) for d in domain)
    elif isinstance(domain, str):
        fields["domain_list"] = normalize_string(domain)
    
    # tags
    tags = fm.get("tags", [])
    if isinstance(tags, list):
        fields["tags_count"] = len(tags)
    elif isinstance(tags, str):
        fields["tags_count"] = 1
    
    # related
    related = fm.get("related", [])
    if isinstance(related, list):
        fields["related_count"] = len(related)
    elif isinstance(related, str):
        fields["related_count"] = 1
    
    return fields


def flag_issues(fields):
    """标记问题标签"""
    issues = []
    
    if not fields["id"]:
        issues.append("no-id")
    if not fields["title"]:
        issues.append("no-title")
    if not fields["type"]:
        issues.append("no-type")
    if not fields["status"]:
        issues.append("no-status")
    if fields["status"].lower() == "draft":
        issues.append("draft")
    if not fields["author"]:
        issues.append("no-author")
    if not fields["reviewed_by"]:
        issues.append("no-reviewer")
    if fields["source_refs_count"] == 0:
        issues.append("no-source")
    if fields["source_refs_has_theme"]:
        issues.append("theme-source")
    if fields["file_size"] < 500:
        issues.append("empty-or-tiny")
    
    # confidence / trust_level 异常
    conf = fields["confidence"]
    trust = fields["trust_level"].lower()
    if conf == "":
        issues.append("no-confidence")
    else:
        try:
            conf_val = float(conf)
            if conf_val >= 0.85 and trust in ("", "medium", "medium-high"):
                issues.append("high-conf-low-trust")
            if conf_val >= 0.80 and trust == "":
                issues.append("high-conf-no-trust")
            if conf_val < 0.60:
                issues.append("low-confidence")
        except (ValueError, TypeError):
            issues.append("invalid-confidence")
    
    if not trust:
        issues.append("no-trust-level")
    
    # 格式问题：status/trust_level 是否带引号
    # 这里我们已经在 normalize_string 中去除引号，所以格式问题需要通过原始 YAML 判断
    # 简化处理：如果原始 frontmatter 中字段值被引号包围，视为 format-issue
    # 这个在后续元数据治理阶段再处理
    
    return ";".join(issues)


def collect_all_domains(rows):
    """统计 domain 分布"""
    domain_counter = Counter()
    for row in rows:
        if row["domain_list"]:
            for d in row["domain_list"].split(","):
                d = d.strip()
                if d:
                    domain_counter[d] += 1
    return domain_counter


def collect_all_authors(rows):
    """统计 author 分布"""
    author_counter = Counter()
    for row in rows:
        if row["author"]:
            author_counter[row["author"]] += 1
        else:
            author_counter["(no author)"] += 1
    return author_counter


def collect_all_reviewers(rows):
    """统计 reviewed_by 分布"""
    reviewer_counter = Counter()
    for row in rows:
        if row["reviewed_by"]:
            reviewer_counter[row["reviewed_by"]] += 1
        else:
            reviewer_counter["(no reviewer)"] += 1
    return reviewer_counter


def collect_issue_counts(rows):
    """统计问题标签分布"""
    issue_counter = Counter()
    issue_by_dir = defaultdict(Counter)
    for row in rows:
        issues = row["issues"].split(";") if row["issues"] else []
        for issue in issues:
            if issue:
                issue_counter[issue] += 1
                issue_by_dir[row["dir"]][issue] += 1
    return issue_counter, issue_by_dir


def generate_report(rows, issue_counter, issue_by_dir, domain_counter, author_counter, reviewer_counter):
    """生成 Markdown 基线报告"""
    total = len(rows)
    draft_count = sum(1 for r in rows if r["status"].lower() == "draft")
    enriched_count = sum(1 for r in rows if r["status"].lower() == "enriched")
    stable_count = sum(1 for r in rows if r["status"].lower() == "stable")
    no_source_count = sum(1 for r in rows if "no-source" in r["issues"])
    no_author_count = sum(1 for r in rows if "no-author" in r["issues"])
    no_reviewer_count = sum(1 for r in rows if "no-reviewer" in r["issues"])
    empty_count = sum(1 for r in rows if "empty-or-tiny" in r["issues"])
    high_conf_low_trust_count = sum(1 for r in rows if "high-conf-low-trust" in r["issues"])
    
    lines = [
        "# 30_wiki 知识卡基线扫描报告",
        "",
        f"> 生成时间：{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}",
        f"> 扫描范围：`30_wiki/` 下所有 `.md` 文件",
        f"> 总卡片数：{total}",
        "",
        "## 一、整体概况",
        "",
        "| 指标 | 数量 | 占比 |",
        "|---|---|---|",
        f"| 总卡片数 | {total} | 100% |",
        f"| draft 状态 | {draft_count} | {draft_count/total*100:.1f}% |",
        f"| enriched 状态 | {enriched_count} | {enriched_count/total*100:.1f}% |",
        f"| stable 状态 | {stable_count} | {stable_count/total*100:.1f}% |",
        f"| 无 source_refs | {no_source_count} | {no_source_count/total*100:.1f}% |",
        f"| 无 author | {no_author_count} | {no_author_count/total*100:.1f}% |",
        f"| 无 reviewed_by | {no_reviewer_count} | {no_reviewer_count/total*100:.1f}% |",
        f"| 空壳/微小文件 | {empty_count} | {empty_count/total*100:.1f}% |",
        f"| 高置信低信任 | {high_conf_low_trust_count} | {high_conf_low_trust_count/total*100:.1f}% |",
        "",
        "## 二、问题标签分布",
        "",
        "| 问题标签 | 数量 | 占比 |",
        "|---|---|---|",
    ]
    
    for issue, count in issue_counter.most_common():
        lines.append(f"| {issue} | {count} | {count/total*100:.1f}% |")
    
    lines.extend([
        "",
        "## 三、按目录问题分布",
        "",
        "| 目录 | draft | no-source | no-author | no-reviewer | empty-or-tiny | high-conf-low-trust |",
        "|---|---|---|---|---|---|---|",
    ])
    
    for dir_name in sorted(issue_by_dir.keys()):
        counter = issue_by_dir[dir_name]
        lines.append(
            f"| {dir_name} | "
            f"{counter.get('draft', 0)} | "
            f"{counter.get('no-source', 0)} | "
            f"{counter.get('no-author', 0)} | "
            f"{counter.get('no-reviewer', 0)} | "
            f"{counter.get('empty-or-tiny', 0)} | "
            f"{counter.get('high-conf-low-trust', 0)} |"
        )
    
    lines.extend([
        "",
        "## 四、Author 分布（前 30）",
        "",
        "| Author | 数量 |",
        "|---|---|",
    ])
    for author, count in author_counter.most_common(30):
        lines.append(f"| {author} | {count} |")
    
    lines.extend([
        "",
        "## 五、Reviewer 分布（前 30）",
        "",
        "| Reviewer | 数量 |",
        "|---|---|",
    ])
    for reviewer, count in reviewer_counter.most_common(30):
        lines.append(f"| {reviewer} | {count} |")
    
    lines.extend([
        "",
        "## 六、Domain 分布（前 50）",
        "",
        "| Domain | 数量 |",
        "|---|---|",
    ])
    for domain, count in domain_counter.most_common(50):
        lines.append(f"| {domain} | {count} |")
    
    lines.extend([
        "",
        "## 七、高危卡片清单（示例）",
        "",
        "以下卡片同时存在多个高危问题标签，需优先处理：",
        "",
        "| 文件路径 | 状态 | Author | Reviewer | Source数 | Confidence | Trust | 问题标签 |",
        "|---|---|---|---|---|---|---|---|",
    ])
    
    # 高危：no-source + no-author + no-reviewer，或 empty-or-tiny，或 high-conf-low-trust
    high_risk_rows = []
    for row in rows:
        issues = set(row["issues"].split(";")) if row["issues"] else set()
        risk_score = 0
        if "no-source" in issues:
            risk_score += 1
        if "no-author" in issues:
            risk_score += 1
        if "no-reviewer" in issues:
            risk_score += 1
        if "empty-or-tiny" in issues:
            risk_score += 3
        if "high-conf-low-trust" in issues:
            risk_score += 2
        if "no-confidence" in issues:
            risk_score += 1
        if risk_score >= 3:
            high_risk_rows.append((risk_score, row))
    
    high_risk_rows.sort(key=lambda x: (-x[0], x[1]["file_path"]))
    
    for risk_score, row in high_risk_rows[:100]:
        lines.append(
            f"| {row['file_path']} | {row['status']} | {row['author'] or '(空)'} | "
            f"{row['reviewed_by'] or '(空)'} | {row['source_refs_count']} | "
            f"{row['confidence'] if row['confidence'] != '' else '(空)'} | "
            f"{row['trust_level'] or '(空)'} | {row['issues']} |"
        )
    
    lines.extend([
        "",
        f"> 注：完整清单见 `{OUTPUT_CSV.name}`，共 {len(high_risk_rows)} 张高危卡片。",
        "",
        "## 八、下一步建议",
        "",
        "1. **阶段 1 元数据治理**：先为无 author/reviewer/id 的卡片补全基础字段；",
        "2. **阶段 2 高危清理**：优先处理 `empty-or-tiny`、`no-source` + `no-author` + `no-reviewer` 的卡片；",
        "3. **阶段 3 作者审查**：从老顽童、黄药师等关键作者开始；",
        "4. **阶段 4/5 分层与 domain 审查**：按可信度和业务域抽样深入。",
        "",
    ])
    
    return "\n".join(lines)


def main():
    rows = []
    parse_errors = []
    
    for md_file in sorted(WIKI_DIR.rglob("*.md")):
        # 跳过 index.md、log.md 等非知识卡文件
        if md_file.name in ("index.md", "log.md", "contradictions.md", "concept-card-index-latest.md"):
            continue
        
        fm, body = parse_frontmatter(md_file)
        if fm is None:
            parse_errors.append(str(md_file.relative_to(WIKI_DIR)))
            continue
        
        fields = extract_fields(fm, md_file, body)
        fields["issues"] = flag_issues(fields)
        rows.append(fields)
    
    # 确保输出目录存在
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    
    # 写入 CSV
    csv_columns = [
        "file_path", "dir", "file_size", "id", "title", "type", "status",
        "author", "reviewed_by", "confidence", "trust_level", "source_refs_count",
        "source_refs_has_theme", "domain_list", "tags_count", "related_count",
        "created_at", "updated_at", "issues"
    ]
    with open(OUTPUT_CSV, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=csv_columns)
        writer.writeheader()
        writer.writerows(rows)
    
    # 统计分析
    issue_counter, issue_by_dir = collect_issue_counts(rows)
    domain_counter = collect_all_domains(rows)
    author_counter = collect_all_authors(rows)
    reviewer_counter = collect_all_reviewers(rows)
    
    # 写入报告
    report = generate_report(rows, issue_counter, issue_by_dir, domain_counter, author_counter, reviewer_counter)
    OUTPUT_REPORT.write_text(report, encoding="utf-8")
    
    print(f"扫描完成：{len(rows)} 张卡片")
    print(f"CSV 输出：{OUTPUT_CSV}")
    print(f"报告输出：{OUTPUT_REPORT}")
    if parse_errors:
        print(f"解析错误：{len(parse_errors)} 个文件")
        for err in parse_errors[:10]:
            print(f"  - {err}")


if __name__ == "__main__":
    main()
