#!/usr/bin/env python3
"""
口述稿全文索引——王语嫣的超长文解析辅助工具。

把口述稿按段落分块，建立关键词→段落的快速索引。
不用全读——搜主题词，直接跳到相关段落精读。

Usage:
  python kdo-tools/transcript-index.py build <口述稿路径>
  python kdo-tools/transcript-index.py search <口述稿路径> <关键词>
"""

import argparse
import json
import re
import sys
from collections import defaultdict
from pathlib import Path

WIKI = Path(__file__).resolve().parent.parent

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")


def split_paragraphs(text: str) -> list[dict]:
    """Split transcript into paragraphs with line numbers."""
    lines = text.split("\n")
    paragraphs = []
    current = []
    start = 0
    for i, line in enumerate(lines):
        stripped = line.strip()
        if stripped:
            if not current:
                start = i + 1
            current.append(stripped)
        else:
            if current and len(" ".join(current)) > 20:
                paragraphs.append({
                    "start": start,
                    "end": i,
                    "text": " ".join(current),
                    "length": len(" ".join(current)),
                })
            current = []
    if current and len(" ".join(current)) > 20:
        paragraphs.append({"start": start, "end": len(lines), "text": " ".join(current), "length": len(" ".join(current))})
    return paragraphs


def build_index(transcript_path: Path) -> Path:
    """Build a keyword→paragraph index from a transcript."""
    text = transcript_path.read_text(encoding="utf-8", errors="ignore")
    paragraphs = split_paragraphs(text)

    # Build inverted index: keyword → list of paragraph indices
    index = defaultdict(list)
    for idx, para in enumerate(paragraphs):
        # Extract meaningful words (Chinese: 2+ chars, English: 3+ chars)
        words = set()
        # Chinese words
        for match in re.finditer(r'[一-鿿]{2,}', para["text"]):
            words.add(match.group())
        # Key phrases we care about
        for phrase in ["双三角", "Y模型", "实事求是", "解放思想", "创造力", "审美", "体系", "场景", "数据",
                        "基本功", "人在环", "飞轮", "AI原生", "PPT", "复盘", "X光", "口喷", "武器库",
                        "龙虾", "刻意练习", "段位", "螺旋上升", "入门", "进阶", "高阶", "自我修养",
                        "提示词", "partner", "YAI", "上下文", "知识库", "资产包", "SVN", "代码库",
                        "画布", "备忘录", "里程碑", "保底策略", "交叉比对", "实证", "真机"]:
            if phrase in para["text"]:
                words.add(phrase)

        for w in words:
            index[w].append(idx)

    # Write index file
    out_dir = transcript_path.parent / "_processed"
    out_dir.mkdir(parents=True, exist_ok=True)
    out_path = out_dir / f"{transcript_path.stem}_索引.json"

    data = {
        "source": str(transcript_path.relative_to(WIKI)),
        "total_paragraphs": len(paragraphs),
        "keywords": len(index),
        "index": {k: v for k, v in sorted(index.items())},
        "paragraphs": paragraphs,
    }
    out_path.write_text(json.dumps(data, ensure_ascii=False, indent=2), encoding="utf-8")

    # Also generate a human-readable summary
    summary_path = out_dir / f"{transcript_path.stem}_主题索引.md"
    lines = [f"# 主题索引：{transcript_path.stem}", f"", f"共 {len(paragraphs)} 段，{len(index)} 个关键词", f""]
    for keyword, para_indices in sorted(index.items(), key=lambda x: -len(x[1])):
        lines.append(f"## {keyword}（{len(para_indices)} 段）")
        for pi in para_indices[:5]:
            p = paragraphs[pi]
            lines.append(f"- L{p['start']}-{p['end']}（{p['length']}字）: {p['text'][:100]}...")
        if len(para_indices) > 5:
            lines.append(f"- ...还有 {len(para_indices) - 5} 段")
        lines.append("")
    summary_path.write_text("\n".join(lines), encoding="utf-8")

    print(f"索引已生成：{out_path.relative_to(WIKI)}")
    print(f"主题索引：{summary_path.relative_to(WIKI)}")
    print(f"  {len(paragraphs)} 段，{len(index)} 个关键词")
    return out_path


def search_index(transcript_path: Path, keyword: str) -> int:
    """Search the index for a keyword and print matching paragraphs."""
    out_dir = transcript_path.parent / "_processed"
    index_path = out_dir / f"{transcript_path.stem}_索引.json"

    if not index_path.exists():
        print("索引不存在。先跑 build。", file=sys.stderr)
        return 1

    data = json.loads(index_path.read_text(encoding="utf-8"))
    index = data["index"]
    paragraphs = data["paragraphs"]

    if keyword not in index:
        # Fuzzy: try partial match
        matches = [k for k in index if keyword in k]
        if matches:
            print(f"精确匹配无。包含'{keyword}'的关键词: {matches}")
            for m in matches:
                print(f"\n--- {m}（{len(index[m])} 段）---")
                for pi in index[m][:3]:
                    p = paragraphs[pi]
                    print(f"\nL{p['start']}-{p['end']}（{p['length']}字）:")
                    print(f"  {p['text'][:300]}")
        else:
            print(f"未找到: {keyword}")
        return 0

    print(f"## {keyword}（{len(index[keyword])} 段）\n")
    for pi in index[keyword]:
        p = paragraphs[pi]
        # Highlight the keyword
        text = p["text"].replace(keyword, f"**{keyword}**")
        print(f"### L{p['start']}-{p['end']}（{p['length']}字）")
        print(f"{text[:400]}")
        print()

    return 0


def main():
    parser = argparse.ArgumentParser(description="口述稿全文索引")
    sub = parser.add_subparsers(dest="cmd", required=True)

    p_build = sub.add_parser("build", help="建立索引")
    p_build.add_argument("path", help="口述稿路径")

    p_search = sub.add_parser("search", help="搜索关键词")
    p_search.add_argument("path", help="口述稿路径")
    p_search.add_argument("keyword", help="关键词")

    args = parser.parse_args()
    p = Path(args.path).resolve()
    if not p.exists():
        print(f"File not found: {p}", file=sys.stderr)
        return 1

    if args.cmd == "build":
        build_index(p)
    elif args.cmd == "search":
        return search_index(p, args.keyword)

    return 0


if __name__ == "__main__":
    sys.exit(main())
