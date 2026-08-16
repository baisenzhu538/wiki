#!/usr/bin/env python3
"""
MCP 可发现性自查 — 新卡提交前验证外部 Agent 能否搜到。

用法:
  python kdo-tools/mcp-reachability-check.py <card_path> --keywords "创新者的窘境,Christensen,破坏性创新"
  python kdo-tools/mcp-reachability-check.py 30_wiki/frameworks/framework-xxx.md --keywords "关键词1,关键词2"

输出:
  [PASS] 命中 → 关键词在搜索结果中且该卡排在前5
  [WARN] 弱命中 → 关键词有结果但该卡不在前5
  ❌ 未命中 → 关键词搜不到该卡 → 建议补全 aliases/title/tags
"""
import argparse
import sys
if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")
if hasattr(sys.stderr, "reconfigure"):
    sys.stderr.reconfigure(encoding="utf-8", errors="replace")
import importlib.util
import re
import sys
from pathlib import Path

SCRIPT_DIR = Path(__file__).resolve().parent
VAULT_ROOT = SCRIPT_DIR.parent


def _load_search():
    """Absolute-path import — avoids site-packages mcp SDK hijack."""
    tools_path = SCRIPT_DIR / "mcp" / "tools.py"
    spec = importlib.util.spec_from_file_location("kdo_mcp_tools", tools_path)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod.search


search = _load_search()


def main():
    parser = argparse.ArgumentParser(description="MCP reachability self-check")
    parser.add_argument("card", help="Path to card file (relative to vault root)")
    parser.add_argument("--keywords", required=True, help="Comma-separated test keywords")
    args = parser.parse_args()

    card_path = Path(args.card)
    if not card_path.is_absolute():
        card_path = VAULT_ROOT / card_path
    if not card_path.exists():
        print(f"ERROR: card not found: {card_path}")
        sys.exit(1)

    card_id = card_path.stem
    keywords = [k.strip() for k in args.keywords.split(",") if k.strip()]

    print(f"[MCP] MCP 可发现性自查")
    print(f"   卡片: {card_id}")
    print(f"   路径: {card_path.relative_to(VAULT_ROOT).as_posix()}")
    print()

    hit_count = 0
    miss_keywords = []
    suggestions = []

    for kw in keywords:
        result = search(kw, limit=10)
        results = result.get("results", [])
        found = False
        position = 0
        for i, r in enumerate(results):
            if r.get("id") == card_id:
                found = True
                position = i + 1
                break

        if found and position <= 5:
            print(f"   [PASS] '{kw}' → 命中 (排名 #{position}, score {results[position-1].get('score', 0):.1f})")
            hit_count += 1
        elif found:
            print(f"   [WARN]  '{kw}' → 弱命中 (排名 #{position}, 不在前5)")
            hit_count += 1
        else:
            print(f"   ❌ '{kw}' → 未命中")
            miss_keywords.append(kw)

    print()
    score = hit_count / len(keywords) * 100 if keywords else 0

    if hit_count == len(keywords):
        print(f"[PASS] 可发现性 {score:.0f}/100 — 全部命中，可以提交。")
    else:
        print(f"[WARN]  可发现性 {score:.0f}/100 — {hit_count}/{len(keywords)} 命中")

        if miss_keywords:
            print()
            print("   建议补全以下 frontmatter 字段：")
            print(f"     aliases: [{', '.join(repr(k) for k in miss_keywords)}]")
            card_text = card_path.read_text(encoding="utf-8", errors="replace")
            has_title = bool(re.search(r"^title:\s*\S", card_text, re.MULTILINE))
            if not has_title:
                print(f"     title: （当前为空——外部 Agent 永远搜不到这张卡）")

    sys.exit(0 if hit_count == len(keywords) else 1)


if __name__ == "__main__":
    main()
