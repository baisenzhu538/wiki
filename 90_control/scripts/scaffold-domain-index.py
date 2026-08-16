#!/usr/bin/env python3
"""
域索引入口卡骨架生成器
扫描指定域的所有卡片，按类型分组（framework/tool/case/dk/concept），
生成四段式索引入口卡 Markdown 骨架。

用法：
    python 90_control/scripts/scaffold-domain-index.py --domain yitang --topic 调研    # 扫描 yitang 域
    python 90_control/scripts/scaffold-domain-index.py --prefix framework-yitang        # 按 ID 前缀扫描
    python 90_control/scripts/scaffold-domain-index.py --domain yitang --dry-run        # 预览
"""

import argparse
import sys
if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")
if hasattr(sys.stderr, "reconfigure"):
    sys.stderr.reconfigure(encoding="utf-8", errors="replace")
import sys
from pathlib import Path
from collections import defaultdict

VAULT_ROOT = Path(__file__).resolve().parent.parent.parent
WIKI_DIR = VAULT_ROOT / "30_wiki"


def parse_frontmatter(text):
    if not text.startswith("---\n"):
        return {}
    end = text.find("\n---\n", 4)
    if end == -1:
        return {}
    try:
        import yaml
        fm = yaml.safe_load(text[4:end])
        return fm if isinstance(fm, dict) else {}
    except Exception:
        return {}


def scan_cards(domain=None, prefix=None):
    """扫描指定域/前缀的卡片"""
    cards = defaultdict(list)
    for fp in sorted(WIKI_DIR.rglob("*.md")):
        if "_archive" in fp.parts or "raw" in fp.parts:
            continue
        try:
            text = fp.read_text(encoding="utf-8")
        except Exception:
            continue

        fm = parse_frontmatter(text)
        if not fm:
            continue

        card_id = fm.get("id", fp.stem)
        domains = fm.get("domain", [])
        if isinstance(domains, str):
            domains = [domains]

        # 过滤
        if domain and domain not in domains:
            continue
        if prefix and not card_id.startswith(prefix):
            continue

        card_type = fm.get("type", "concept")
        title = fm.get("title", card_id)
        cards[card_type].append((card_id, title))

    return cards


def generate_skeleton(cards, domain_name):
    """生成四段式索引入口卡"""
    lines = [
        "---",
        f"id: {domain_name}-domain-digest",
        f"title: 域摘要：{domain_name}",
        "type: index",
        "status: draft",
        "domain:",
        f"  - yitang",
        "source_context: 由 scaffold-domain-index.py 自动生成骨架",
        f"created_at: '2026-06-21'",
        "author: 老顽童",
        "reviewed_by: 王语嫣",
        "---",
        "",
        f"# 域摘要：{domain_name}",
        "",
    ]

    total = sum(len(v) for v in cards.values())
    lines.append(f"> {total} 张卡 · 自动生成骨架 · 待老顽童填写描述")

    # 核心框架
    frameworks = cards.get("framework", [])
    if frameworks:
        lines.extend(["", "## 核心框架（先读）", "",
                       "| 卡 | 做什么 |", "|:--|:--|"])
        for cid, title in frameworks:
            lines.append(f"| `{cid}` | TODO |")

    # 工具卡
    tools = cards.get("tool", [])
    if tools:
        lines.extend(["", "## 工具索引", "",
                       "| 卡 | 场景 |", "|:--|:--|"])
        for cid, title in tools:
            lines.append(f"| `{cid}` | TODO |")

    # 案例
    cases = cards.get("case", [])
    if cases:
        lines.extend(["", "## 关键案例", "",
                       "| 卡 | 行业/场景 | 核心教训 |", "|:--|:--|:--|"])
        for cid, title in cases:
            lines.append(f"| `{cid}` | TODO | TODO |")

    # 暗知识
    dks = cards.get("dark_knowledge", cards.get("dark-knowledge", cards.get("dk", [])))
    if dks:
        lines.extend(["", "## 暗知识（不要踩的坑）", "",
                       "| 卡 | 一句话 |", "|:--|:--|"])
        for cid, title in dks:
            lines.append(f"| `{cid}` | TODO |")

    # 概念
    concepts = cards.get("concept", [])
    if concepts:
        lines.extend(["", "## 概念与原则", "",
                       "| 卡 | 一句话 |", "|:--|:--|"])
        for cid, title in concepts:
            lines.append(f"| `{cid}` | TODO |")

    lines.extend(["", "---", "",
                   "*骨架由 scaffold-domain-index.py 生成，TODO 行需人工填写*"])

    return "\n".join(lines)


def main():
    parser = argparse.ArgumentParser(description="域索引入口卡骨架生成器")
    parser.add_argument("--domain", help="按 domain 过滤（如 yitang）")
    parser.add_argument("--prefix", help="按 ID 前缀过滤（如 framework-yitang-research）")
    parser.add_argument("--topic", default="new-domain", help="域名称（用于生成文件名和标题）")
    parser.add_argument("--dry-run", action="store_true", help="仅预览，不写入文件")
    args = parser.parse_args()

    if not args.domain and not args.prefix:
        print("错误：至少指定 --domain 或 --prefix", file=sys.stderr)
        sys.exit(2)

    cards = scan_cards(domain=args.domain, prefix=args.prefix)
    total = sum(len(v) for v in cards.values())

    if total == 0:
        print(f"未找到匹配的卡片（domain={args.domain}, prefix={args.prefix}）")
        sys.exit(1)

    skeleton = generate_skeleton(cards, args.topic)
    print(f"# 域索引入口卡骨架")
    print(f"**域**: {args.topic} | **卡片数**: {total}")
    for t, cs in sorted(cards.items()):
        print(f"  {t}: {len(cs)} 张")
    print()

    if args.dry_run:
        print(skeleton[:2000])
        print("...")
    else:
        out_path = VAULT_ROOT / "30_wiki" / "domains" / f"{args.topic}-domain-digest.md"
        out_path.parent.mkdir(parents=True, exist_ok=True)
        out_path.write_text(skeleton, encoding="utf-8")
        print(f"已写入: {out_path.relative_to(VAULT_ROOT).as_posix()}")
        print("TODO 行需老顽童人工填写描述。")


if __name__ == "__main__":
    main()
