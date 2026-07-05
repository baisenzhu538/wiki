#!/usr/bin/env python3
"""
扫描口述稿中的 Truman 操作演示段落。

Truman 说以下信号词时，通常是在摊开自己的操作过程——最高优先级标注：
  "我给你演示一下" "举个例子" "这是我真实的" "我给你们看一个"
  "你们感受一下" "准备好，惊喜来了" "来，我现场给你"
  "我给你看一个" "试一下啊" "你们试试"
  "这个建议是最近我用的特别开心的" "注意，所有你们未来"

Usage:
  python kdo-tools/scan-demo-sections.py <口述稿路径>
  python kdo-tools/scan-demo-sections.py --all   # 扫描 inbox 所有口述稿
"""

import argparse
import re
import sys
from pathlib import Path

WIKI = Path(__file__).resolve().parent.parent

SIGNAL_WORDS = [
    "我给你演示一下", "举个例子", "这是我真实的", "我给你们看一个",
    "你们感受一下", "准备好，惊喜来了", "来，我现场给你",
    "我给你看一个", "试一下啊", "你们试试",
    "这个建议是最近我用的特别开心的", "注意，所有你们未来",
    "我稍微解释一下", "我先不说过程", "直接说结果",
    "这个时候", "后来一次意外", "转折出现了",
]

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")


def scan_file(path: Path, full_context: bool = True) -> list[dict]:
    """Scan a transcript for demo paragraphs. Returns list of {line, context, signal, category}."""
    text = path.read_text(encoding="utf-8", errors="ignore")
    lines = text.split("\n")
    results = []

    for i, line in enumerate(lines):
        for signal in SIGNAL_WORDS:
            if signal in line:
                # Extract surrounding context (20 lines before, 10 after for full, or 5/3 for summary)
                if full_context:
                    start = max(0, i - 20)
                    end = min(len(lines), i + 11)
                else:
                    start = max(0, i - 5)
                    end = min(len(lines), i + 4)
                context = "\n".join(lines[start:end])
                # Categorize the signal
                if signal in ("转折出现了", "后来一次意外"):
                    category = "转折/突破"
                elif signal in ("这个时候", "我先不说过程"):
                    category = "叙事结构"
                elif signal in ("举个例子", "我给你们看一个", "我给你看一个"):
                    category = "案例演示"
                elif signal in ("这是我真实的", "这个建议是最近我用的特别开心的"):
                    category = "操作心法"
                elif signal in ("试一下啊", "你们试试", "注意，所有你们未来"):
                    category = "可执行提示"
                elif signal in ("你们感受一下", "准备好，惊喜来了"):
                    category = "高潮/总结"
                else:
                    category = "其他"

                results.append({
                    "line": i + 1,
                    "signal": signal,
                    "category": category,
                    "trigger": line.strip()[:200],
                    "context": context[:2000],
                })
                break

    return results


def generate_compilation(path: Path) -> Path:
    """Generate a structured 高价值段落汇编 from a transcript.
    Returns the path to the compiled markdown file.
    This is what 王语嫣 reads instead of the full transcript.
    """
    text = path.read_text(encoding="utf-8", errors="ignore")
    transcript_lines = text.split("\n")
    results = scan_file(path, full_context=True)
    if not results:
        return None

    # Group by category
    from collections import defaultdict
    by_category = defaultdict(list)
    for r in results:
        by_category[r["category"]].append(r)

    # Generate compilation
    lines = []
    lines.append(f"# 高价值段落汇编：{path.stem}")
    lines.append(f"> 自动生成。共 {len(results)} 处标记。王语嫣：读完这份汇编再写诊断报告。")
    try:
        rel = path.resolve().relative_to(WIKI.resolve())
    except ValueError:
        rel = path
    lines.append(f"> 原文路径：{rel}")
    lines.append("")
    # Signal density map
    density_buckets = defaultdict(int)
    for r in results:
        bucket = (r["line"] // 500) * 500
        density_buckets[bucket] += 1

    lines.append("## 信号密度地图（优先读密集区）")
    lines.append("")
    for start, count in sorted(density_buckets.items()):
        bar = "█" * min(count, 20)
        lines.append(f"- L{start}-{start+500}: {count}处 {bar}")
    lines.append("")

    lines.append("## 建议阅读顺序")
    lines.append("")
    priority_order = ["案例演示", "操作心法", "转折/突破", "可执行提示", "高潮/总结", "叙事结构", "其他"]
    for cat in priority_order:
        if cat in by_category:
            lines.append(f"- **{cat}**：{len(by_category[cat])} 处 → 优先精读")
    lines.append("")
    lines.append("---")
    lines.append("")

    for cat in priority_order:
        if cat not in by_category:
            continue
        lines.append(f"## {cat}（{len(by_category[cat])} 处）")
        lines.append("")
        for idx, r in enumerate(by_category[cat], 1):
            lines.append(f"### {idx}. L{r['line']} 🔴 {r['signal']}")
            lines.append(f"> 触发句：{r['trigger'][:150]}")
            lines.append("")
            lines.append("```")
            lines.append(r["context"][:1500])
            lines.append("```")
            lines.append("")
            lines.append("**诊断提示**：读完这段后，回答——")
            lines.append("- Before: Truman 以前的旧做法是什么？")
            lines.append("- After: 现在的新做法是什么？")
            lines.append("- Why: 为什么更好（双三角哪个要素被补上了）？")
            lines.append("- 通用: 这段能不能变成可复用的模板/skill/workflow？")
            lines.append("")

    # ── Suspicious zone scan: do BEFORE writing the file ──
    # Oral transcripts have very short lines (one sentence per line).
    # Instead of single-line length, look for 5+ consecutive non-empty lines
    # without any signal words — these are "quietly delivered" narrative passages.
    suspicious_runs = []
    current_run = []
    current_start = 0
    for i, line in enumerate(transcript_lines):
        has_signal = any(s in line for s in SIGNAL_WORDS)
        has_content = len(line.strip()) > 10  # skip blank/short lines
        if has_content and not has_signal:
            if not current_run:
                current_start = i + 1
            current_run.append(line)
        else:
            if len(current_run) >= 5:  # 5+ consecutive lines without signals
                suspicious_runs.append({
                    "start": current_start,
                    "lines": len(current_run),
                    "text": " ".join(current_run)[:200],
                })
            current_run = []
    # Check final run
    if len(current_run) >= 5:
        suspicious_runs.append({
            "start": current_start,
            "lines": len(current_run),
            "text": " ".join(current_run)[:200],
        })

    if suspicious_runs:
        lines.append("---")
        lines.append("## ⚠️ 怀疑区：连续5行以上无信号词的叙事段落")
        lines.append(f"> 共 {len(suspicious_runs)} 处。这些区域可能包含'安静地'讲的重要内容，建议抽查。")
        lines.append("")
        for s in suspicious_runs[:15]:
            lines.append(f"- L{s['start']}（{s['lines']}行）: {s['text'][:150]}")
        if len(suspicious_runs) > 15:
            lines.append(f"- ...还有 {len(suspicious_runs) - 15} 处")

    # Write to _processed/
    out_dir = path.parent / "_processed"
    out_dir.mkdir(parents=True, exist_ok=True)
    out_path = out_dir / f"{path.stem}_高价值段落汇编.md"
    out_path.write_text("\n".join(lines), encoding="utf-8")

    print(f"  汇编已生成：{out_path.relative_to(WIKI)}")
    print(f"    {len(results)} 处标记，按 {len(by_category)} 个分类组织")
    if suspicious_runs:
        print(f"    ⚠️  {len(suspicious_runs)} 处怀疑区（无信号词叙事段落）——建议抽查")
    return out_path


def scan_all():
    """Scan all oral transcripts in inbox."""
    inbox = WIKI / "00_inbox"
    total = 0
    for pattern in ["*口述*.txt", "*口述*.md", "*逐字稿*"]:
        for f in inbox.rglob(pattern):
            results = scan_file(f)
            if results:
                print(f"\n{'='*60}")
                print(f"📄 {f.relative_to(WIKI)} — {len(results)} 处操作演示")
                print(f"{'='*60}")
                for r in results:
                    print(f"\n  L{r['line']} 🔴 {r['signal']}")
                    print(f"  {r['trigger']}")
                total += len(results)

    print(f"\n{'='*60}")
    print(f"总计: {total} 处操作演示段落")
    return total


def main():
    parser = argparse.ArgumentParser(description="扫描口述稿中的 Truman 操作演示段落")
    parser.add_argument("path", nargs="?", help="口述稿路径")
    parser.add_argument("--all", action="store_true", help="扫描 inbox 所有口述稿")
    parser.add_argument("--compile", action="store_true", help="生成高价值段落汇编（推荐）")
    args = parser.parse_args()

    if args.all:
        scan_all()
    elif args.path:
        p = Path(args.path).resolve()
        if not p.exists():
            print(f"File not found: {p}", file=sys.stderr)
            return 1
        if args.compile:
            generate_compilation(p)
        else:
            results = scan_file(p, full_context=False)
            print(f"{p}: {len(results)} 处操作演示段落")
            for r in results:
                print(f"\n  L{r['line']} 🔴 {r['signal']} [{r['category']}]")
                print(f"  {r['trigger']}")
    else:
        parser.print_help()

    return 0


if __name__ == "__main__":
    sys.exit(main())
