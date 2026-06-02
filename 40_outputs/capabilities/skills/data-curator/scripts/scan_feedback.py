#!/usr/bin/env python3
"""Sprint 6: Auto-scan all article Feedback sections, extract and categorize issues.
Usage: python scan_feedback.py [--json] [--save]
"""
import json, re, sys
from pathlib import Path
from collections import Counter

VAULT = Path(r"C:\Users\Administrator\Desktop\wiki")
ARTICLES_DIR = VAULT / "40_outputs" / "content" / "articles"

def scan_all():
    articles = sorted(ARTICLES_DIR.glob("*.md"))
    all_feedback = []

    for art in articles:
        text = art.read_text(encoding="utf-8", errors="replace")
        fb_section = re.search(r"## Feedback\s*\n(.*?)(?=\n##\s|\n---\s*$|\Z)", text, re.DOTALL)
        if not fb_section:
            continue
        fb_text = fb_section.group(1).strip()
        items = re.findall(
            r"(?:^|\n)\s*(?:\d+\.|\-|\*)\s+\*?\*?(.+?)\*?\*?(?=\n\s*(?:\d+\.|\-|\*|\Z))",
            fb_text, re.DOTALL
        )
        if not items:
            items = [p.strip() for p in fb_text.split("\n\n") if p.strip() and len(p.strip()) > 20]

        for item in items:
            item = item.strip().replace("\n", " ")
            cat = categorize(item)
            all_feedback.append({
                "article": art.name,
                "category": cat,
                "text": item[:200],
            })

    return all_feedback, len(articles)


def categorize(text):
    t = text.lower()
    if any(kw in t for kw in ["命令", "cli", "终", "查询", "stats", "count", "search", "status", "--"]):
        return "缺CLI命令"
    if any(kw in t for kw in ["自动化", "自动", "机制", "提取", "汇聚", "收集", "跟踪", "分析器"]):
        return "缺自动化机制"
    if any(kw in t for kw in ["角色", "汇聚者", "管理者", "不确定.*谁", "负责"]):
        return "缺角色/流程"
    if any(kw in t for kw in ["数据", "评测", "benchmark", "白皮书", "测量", "统计", "定量"]):
        return "缺数据/评测"
    if any(kw in t for kw in ["feedback", "回音", "没人看", "消费", "习惯解", "技术解"]):
        return "Feedback本身"
    return "其他"


def main():
    feedback, total = scan_all()
    cats = Counter(f["category"] for f in feedback)

    print(f"Scanned {total} articles, found {len(feedback)} feedback items.\n")
    for cat, count in cats.most_common():
        print(f"  {cat}: {count}")
    print()

    for cat in sorted(cats.keys()):
        items = [f for f in feedback if f["category"] == cat]
        print(f"--- {cat} ({len(items)} 条) ---")
        for i, f in enumerate(items, 1):
            print(f"  {i}. [{f['article'][:40]}] {f['text'][:120]}")
        print()

    # Save report
    if "--save" in sys.argv:
        out = VAULT / "70_product" / "tasks" / "feedback-scan-auto.md"
        out.parent.mkdir(parents=True, exist_ok=True)
        lines = [
            "---",
            f"title: \"Feedback 自动扫描 — {len(feedback)} 条\"",
            "type: task",
            f"created_at: 2026-06-03",
            "status: pending",
            "---",
            "",
            f"扫描 {total} 篇文章，提取 {len(feedback)} 条 Feedback。",
            "",
        ]
        for cat in sorted(cats.keys()):
            items = [f for f in feedback if f["category"] == cat]
            lines.append(f"## {cat} ({len(items)} 条)")
            lines.append("")
            for i, f in enumerate(items, 1):
                lines.append(f"{i}. [{f['article'][:50]}] {f['text'][:150]}")
            lines.append("")
        out.write_text("\n".join(lines), encoding="utf-8")
        print(f"Saved: {out}")

    if "--json" in sys.argv:
        print(json.dumps(feedback, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
