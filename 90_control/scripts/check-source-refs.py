#!/usr/bin/env python3
"""
source_refs 健康检查器
扫描 30_wiki 下所有卡片，验证每个 source_refs 指向的文件是否真实存在，
标记已知污染模式，生成可操作的清理报告。

用法：
    python 90_control/scripts/check-source-refs.py              # 扫描全库
    python 90_control/scripts/check-source-refs.py --domain yitang  # 仅扫描指定域
    python 90_control/scripts/check-source-refs.py --card yt-research-osl-framework  # 单卡
    python 90_control/scripts/check-source-refs.py --json         # JSON 输出（供 agent 消费）
    python 90_control/scripts/check-source-refs.py --fix-suggestions  # 额外输出修复建议
"""

import argparse
import json
import sys
from pathlib import Path
from collections import defaultdict

VAULT_ROOT = Path(__file__).resolve().parent.parent.parent
WIKI_DIR = VAULT_ROOT / "30_wiki"

# 已知污染/虚假 source 模式
CONTAMINATION_PATTERNS = [
    "src_20260503_52ae08ba-kdo_product_design_agent_final.md",
    "src_20260503_52ae08ba",
]

# source_refs 中可能以多种格式出现
# - "10_raw/sources/src_xxx/SKILL.md"  (文件路径)
# - "00_inbox/调研专题/一堂-xxx-口述.txt" (文件路径)
# - "src_20260503_52ae08ba" (src ID，非路径)
# - "[[some-card]]" (wikilink，不是文件 source)


def parse_frontmatter(text):
    """提取 YAML frontmatter。返回 (dict|None, error_msg|None)"""
    if not text.startswith("---\n"):
        return None, "missing frontmatter"
    end = text.find("\n---\n", 4)
    if end == -1:
        return None, "unclosed frontmatter"
    try:
        import yaml
        fm = yaml.safe_load(text[4:end])
        return (fm if isinstance(fm, dict) else {}), None
    except Exception as e:
        return None, f"YAML parse error: {e}"


def is_file_path(ref):
    """判断一个 source_ref 是否看起来像文件路径（而非纯 src ID 或 wikilink）"""
    s = str(ref).strip()
    if s.startswith("[[") or s.startswith("src_") and "/" not in s:
        return False
    return "/" in s or s.endswith(".md") or s.endswith(".txt") or s.endswith(".pdf")


def is_src_id(ref):
    """判断是否形如 src_YYYYMMDD_HHHHHHHH"""
    import re
    return bool(re.match(r"^src_\d{8}_[a-f0-9]{8}$", str(ref).strip()))


def resolve_path(ref, vault_root):
    """将 source_ref 解析为绝对路径。支持相对路径（从 vault 根）。"""
    s = str(ref).strip()
    candidate = vault_root / s
    return candidate


def check_card(file_path, vault_root):
    """检查单张卡片的 source_refs。返回 dict"""
    rel = file_path.relative_to(vault_root).as_posix()
    try:
        text = file_path.read_text(encoding="utf-8")
    except Exception as e:
        return {"file": rel, "card_id": file_path.stem, "error": f"read error: {e}", "sources": []}

    fm, err = parse_frontmatter(text)
    if err:
        return {"file": rel, "card_id": file_path.stem, "error": err, "sources": []}

    card_id = str(fm.get("id", file_path.stem)).strip()
    raw_refs = fm.get("source_refs", [])
    if not raw_refs:
        return {"file": rel, "card_id": card_id, "sources": [], "empty": True}
    if isinstance(raw_refs, str):
        raw_refs = [raw_refs]

    sources = []
    for ref in raw_refs:
        s = str(ref).strip()
        entry = {"raw": s}

        # 检查污染模式
        contaminated = False
        for pat in CONTAMINATION_PATTERNS:
            if pat in s:
                contaminated = True
                entry["contaminated_by"] = pat
                break
        entry["contaminated"] = contaminated

        # 检查路径是否存在
        if is_file_path(s):
            abs_path = resolve_path(s, vault_root)
            exists = abs_path.exists()
            entry["resolved_path"] = abs_path.as_posix()
            entry["exists"] = exists
            entry["kind"] = "file_path"
        elif is_src_id(s):
            entry["kind"] = "src_id"
            entry["exists"] = None  # src_id 需要查 registry，此处仅标记
        elif s.startswith("[["):
            entry["kind"] = "wikilink"
            entry["exists"] = None  # wikilink 不是文件 source
        else:
            entry["kind"] = "unknown"
            entry["exists"] = None

        sources.append(entry)

    return {
        "file": rel,
        "card_id": card_id,
        "domain": fm.get("domain", []),
        "status": fm.get("status", ""),
        "confidence": fm.get("confidence"),
        "sources": sources,
        "total": len(sources),
    }


def scan(vault_root, domain_filter=None, card_filter=None):
    """扫描全库"""
    files = [
        f for f in WIKI_DIR.rglob("*.md")
        if "_archive" not in f.parts and "raw" not in f.parts
    ]
    results = []
    for fp in sorted(files):
        r = check_card(fp, vault_root)
        if card_filter and r["card_id"] != card_filter:
            continue
        if domain_filter:
            domains = r.get("domain", [])
            if isinstance(domains, str):
                domains = [domains]
            if domain_filter not in domains:
                continue
        results.append(r)
    return results


def summarize(results):
    """生成汇总统计"""
    total_cards = len(results)
    cards_with_sources = sum(1 for r in results if r.get("total", 0) > 0)
    cards_empty = sum(1 for r in results if r.get("empty"))
    cards_with_errors = sum(1 for r in results if "error" in r)

    total_refs = sum(r.get("total", 0) for r in results)
    refs_missing = 0
    refs_contaminated = 0
    refs_file_path = 0
    refs_ok = 0

    contaminated_cards = []
    missing_source_cards = []

    for r in results:
        card_contaminated = False
        card_missing = []
        for s in r.get("sources", []):
            if s.get("contaminated"):
                refs_contaminated += 1
                card_contaminated = True
            if s.get("kind") == "file_path":
                refs_file_path += 1
                if s.get("exists") is True:
                    refs_ok += 1
                elif s.get("exists") is False:
                    refs_missing += 1
                    card_missing.append(s["raw"])
        if card_contaminated:
            contaminated_cards.append(r)
        if card_missing:
            missing_source_cards.append((r, card_missing))

    return {
        "total_cards": total_cards,
        "cards_with_sources": cards_with_sources,
        "cards_empty": cards_empty,
        "cards_with_errors": cards_with_errors,
        "total_refs": total_refs,
        "refs_file_path": refs_file_path,
        "refs_ok": refs_ok,
        "refs_missing": refs_missing,
        "refs_contaminated": refs_contaminated,
        "contaminated_cards": contaminated_cards,
        "missing_source_cards": missing_source_cards,
    }


def generate_report(results, stats, vault_root):
    """生成 Markdown 报告"""
    lines = [
        "# source_refs 健康检查报告",
        "",
        f"**扫描范围**：{stats['total_cards']} 张卡片",
        f"**有 source 的卡片**：{stats['cards_with_sources']} 张",
        f"**空 source 卡片**：{stats['cards_empty']} 张",
        f"**source_refs 总数**：{stats['total_refs']} 条",
        f"**文件路径类 source**：{stats['refs_file_path']} 条",
        f"**✅ 文件存在**：{stats['refs_ok']} 条",
        f"**❌ 文件缺失**：{stats['refs_missing']} 条",
        f"**⚠️ 污染引用**：{stats['refs_contaminated']} 条",
        "",
        "---",
        "",
    ]

    # 污染卡片
    if stats["contaminated_cards"]:
        lines.append("## ⚠️ 污染引用（已知虚假 source）")
        lines.append("")
        lines.append("| 卡片 ID | 污染 source | 当前 status |")
        lines.append("|---|---|---|")
        for r in stats["contaminated_cards"]:
            for s in r["sources"]:
                if s.get("contaminated"):
                    lines.append(
                        f"| `{r['card_id']}` "
                        f"| `{s.get('contaminated_by', s['raw'])}` "
                        f"| {r.get('status', '?')} |"
                    )
        lines.append("")

    # 缺失 source
    if stats["missing_source_cards"]:
        lines.append("## ❌ 文件缺失（source_refs 指向不存在的文件）")
        lines.append("")
        lines.append("| 卡片 ID | 缺失路径 |")
        lines.append("|---|---|")
        seen = set()
        for r, missing in stats["missing_source_cards"]:
            for m in missing:
                key = (r["card_id"], m)
                if key not in seen:
                    seen.add(key)
                    lines.append(f"| `{r['card_id']}` | `{m}` |")
        lines.append("")

    # 按卡片明细
    lines.append("## 逐卡明细")
    lines.append("")
    lines.append("| 卡片 ID | source 总数 | ✅ | ❌ | ⚠️ | status |")
    lines.append("|---|---|---|---|---|---|")
    for r in results:
        if "error" in r:
            lines.append(f"| `{r['card_id']}` | - | - | - | - | ERROR: {r['error']} |")
            continue
        ok = sum(1 for s in r["sources"] if s.get("exists") is True)
        bad = sum(1 for s in r["sources"] if s.get("exists") is False)
        contaminated = sum(1 for s in r["sources"] if s.get("contaminated"))
        if ok == 0 and bad == 0 and contaminated == 0:
            continue  # 跳过全空/无文件路径 source 的卡片
        lines.append(
            f"| `{r['card_id']}` "
            f"| {r.get('total', 0)} "
            f"| {ok} "
            f"| {bad} "
            f"| {contaminated} "
            f"| {r.get('status', '?')} |"
        )
    lines.append("")

    # 修复建议
    lines.extend([
        "---",
        "",
        "## 修复优先级",
        "",
        "1. **先修污染引用**：将污染 source 替换为 `10_raw/sources/src_20260620_business-research-skill-v2.1.0/` 或 `00_inbox/调研专题/` 下对应真实文件",
        "2. **再补缺失文件**：确认文件是否被移动/重命名，或补入缺失的素材",
        "3. **最后验 src_id**：对 `src_*` ID 类 source，需查 `.kdo/source_id_map.json` 确认是否已注册",
        "",
        f"*生成：check-source-refs.py · {Path(__file__).name}*",
    ])

    return "\n".join(lines)


def cmd_scan(args, vault_root):
    results = scan(vault_root, args.domain, args.card)
    stats = summarize(results)

    # Windows PowerShell GBK 编码兼容
    import io
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

    if args.json:
        output = {
            "stats": {k: v for k, v in stats.items() if k not in ("contaminated_cards", "missing_source_cards")},
            "contaminated_cards": [
                {"card_id": r["card_id"], "file": r["file"], "status": r.get("status"),
                 "contaminated_sources": [s["raw"] for s in r["sources"] if s.get("contaminated")]}
                for r in stats["contaminated_cards"]
            ],
            "missing_source_cards": [
                {"card_id": r["card_id"], "file": r["file"],
                 "missing": [s["raw"] for s in r["sources"] if s.get("exists") is False]}
                for r, missing in stats["missing_source_cards"]
            ],
        }
        print(json.dumps(output, ensure_ascii=False, indent=2))
    else:
        report = generate_report(results, stats, vault_root)
        print(report)

    # 退出码：有问题则非零
    if stats["refs_missing"] > 0 or stats["refs_contaminated"] > 0:
        sys.exit(1)


def main():
    parser = argparse.ArgumentParser(description="source_refs 健康检查器")
    parser.add_argument("--domain", help="仅扫描指定 domain（如 yitang）")
    parser.add_argument("--card", help="仅检查指定卡片 ID")
    parser.add_argument("--json", action="store_true", help="JSON 输出")
    args = parser.parse_args()
    cmd_scan(args, VAULT_ROOT)


if __name__ == "__main__":
    main()
