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
    """将 source_ref 解析为绝对路径。支持相对路径（从 vault 根）。
    #543：先剥 `:NN` 行号锚后缀（`path:2245` → `path`）——行号是定位信息，
    不参与存在性判定；带锚引用此前全被误判缺失（1024 条死引数字被污染的根因之一）。"""
    s = str(ref).strip()
    s = strip_line_anchor(s)
    candidate = vault_root / s
    return candidate


import re as _re

_LINE_ANCHOR_RE = _re.compile(r"^(.*?):\d+(?:-\d+)?$")


def strip_line_anchor(ref):
    """剥除 `path:NN` / `path:NN-MM` 行号锚后缀，返回 (纯路径)。
    只剥数字锚（`x.md:2245`）；Windows 盘符 `C:/...` 不误伤（盘符后非数字）。
    无锚 → 原样返回。"""
    m = _LINE_ANCHOR_RE.match(ref)
    if m and m.group(1):
        return m.group(1)
    return ref


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

        # 检查路径是否存在（#543：剥行号锚后判定，锚本身记录供误报挤占量统计）
        if is_file_path(s):
            stripped = strip_line_anchor(s)
            entry["had_line_anchor"] = stripped != s
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
    """扫描指定 vault 的 30_wiki（#543：原实现忽略 vault_root 参数用模块级 WIKI_DIR，
    测试/多库场景下扫错库——改为参数驱动）。"""
    wiki_dir = Path(vault_root) / "30_wiki"
    files = [
        f for f in wiki_dir.rglob("*.md")
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
    refs_line_anchor = 0          # #543：带行号锚的引用总数
    refs_line_anchor_alive = 0    # #543：剥锚后文件存在（此前被误判缺失）的数量

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
                if s.get("had_line_anchor"):
                    refs_line_anchor += 1
                if s.get("exists") is True:
                    refs_ok += 1
                    if s.get("had_line_anchor"):
                        refs_line_anchor_alive += 1
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
        "refs_line_anchor": refs_line_anchor,
        "refs_line_anchor_alive": refs_line_anchor_alive,
        "contaminated_cards": contaminated_cards,
        "missing_source_cards": missing_source_cards,
    }


def cluster_missing(stats):
    """#543 死引治理聚类：域 × status 透视 + 指向 00_inbox 的最低成本修复簇。
    返回 {by_domain_status, inbox_pointing, top_cards}（只统计文件缺失类）。"""
    by_domain_status = defaultdict(int)
    inbox_pointing = []
    card_missing_counts = []
    for r, missing in stats["missing_source_cards"]:
        domains = r.get("domain") or ["<none>"]
        if isinstance(domains, str):
            domains = [domains]
        status = r.get("status") or "<none>"
        for d in domains:
            by_domain_status[(str(d), status)] += len(missing)
        for m in missing:
            if "00_inbox" in m.replace("\\", "/"):
                inbox_pointing.append({"card_id": r["card_id"], "status": status, "missing": m})
        card_missing_counts.append((r["card_id"], status, domains, len(missing)))
    card_missing_counts.sort(key=lambda x: -x[3])
    return {
        "by_domain_status": [
            {"domain": d, "status": s, "missing": n}
            for (d, s), n in sorted(by_domain_status.items(), key=lambda kv: -kv[1])
        ],
        "inbox_pointing": inbox_pointing,
        "top_cards": [
            {"card_id": c, "status": s, "domain": d, "missing": n}
            for c, s, d, n in card_missing_counts[:50]
        ],
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
        f"**🔗 行号锚引用**：{stats['refs_line_anchor']} 条（剥锚后存在 {stats['refs_line_anchor_alive']} 条——剥锚修复前全被误判缺失，#543）",
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


def generate_cluster_section(stats):
    """#543：死引治理聚类段（域×status 透视 + inbox 指向簇 + Top 缺引卡）。"""
    cl = cluster_missing(stats)
    lines = [
        "## 死引治理聚类（#543：分批方案输入）",
        "",
        "### 域 × status 透视（reviewed 卡带死引=终审漏项，优先治理）",
        "",
        "| 域 | status | 缺失条数 |",
        "|---|---|---|",
    ]
    for row in cl["by_domain_status"]:
        lines.append(f"| {row['domain']} | {row['status']} | {row['missing']} |")
    lines.append("")
    lines.append(f"### 指向 00_inbox 的死引（{len(cl['inbox_pointing'])} 条——修复成本最低：归档即可）")
    lines.append("")
    lines.append("| 卡片 ID | status | 缺失路径 |")
    lines.append("|---|---|---|")
    for it in cl["inbox_pointing"][:100]:
        lines.append(f"| `{it['card_id']}` | {it['status']} | `{it['missing']}` |")
    if len(cl["inbox_pointing"]) > 100:
        lines.append(f"| ... | 省略 {len(cl['inbox_pointing']) - 100} 条，见 JSON | |")
    lines.append("")
    lines.append("### 缺引最多卡片 Top 50")
    lines.append("")
    lines.append("| 卡片 ID | status | 缺失条数 |")
    lines.append("|---|---|---|")
    for it in cl["top_cards"]:
        lines.append(f"| `{it['card_id']}` | {it['status']} | {it['missing']} |")
    lines.append("")
    return lines, cl


def cmd_scan(args, vault_root):
    results = scan(vault_root, args.domain, args.card)
    stats = summarize(results)

    # Windows PowerShell GBK 编码兼容（#543：无 .buffer/reconfigure 的 agent 宿主 stdout
    # 不崩——此前 io.TextIOWrapper(sys.stdout.buffer) 直接 AttributeError，JSON 零输出=消费面断）
    try:
        sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    except Exception:
        pass

    clusters = None
    if args.report_dir:
        cluster_lines, clusters = generate_cluster_section(stats)
        out_dir = Path(args.report_dir)
        out_dir.mkdir(parents=True, exist_ok=True)
        md = generate_report(results, stats, vault_root)
        # 聚类段插在「修复优先级」之前
        marker = "## 修复优先级"
        if marker in md:
            md = md.replace(marker, "\n".join(cluster_lines) + "\n---\n\n" + marker, 1)
        (out_dir / "source-refs-health-latest.md").write_text(md, encoding="utf-8")

    if args.json or args.report_dir:
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
            "clusters": clusters if clusters is not None else cluster_missing(stats),
        }
        if args.report_dir:
            (Path(args.report_dir) / "source-refs-health-latest.json").write_text(
                json.dumps(output, ensure_ascii=False, indent=2), encoding="utf-8")
        if args.json:
            print(json.dumps(output, ensure_ascii=False, indent=2))
    else:
        report = generate_report(results, stats, vault_root)
        print(report)

    # 退出码：缺失/污染超阈值才报警（#543：阈值=治理基线，防增量不扰存量；
    # 默认 None=有任何缺失/污染即 exit 1，旧行为）
    if args.max_missing is not None or args.max_contaminated is not None:
        miss_over = stats["refs_missing"] > (args.max_missing if args.max_missing is not None else 0)
        cont_over = stats["refs_contaminated"] > (args.max_contaminated if args.max_contaminated is not None else 0)
        if miss_over or cont_over:
            sys.exit(1)
    elif stats["refs_missing"] > 0 or stats["refs_contaminated"] > 0:
        sys.exit(1)


def main():
    parser = argparse.ArgumentParser(description="source_refs 健康检查器")
    parser.add_argument("--domain", help="仅扫描指定 domain（如 yitang）")
    parser.add_argument("--card", help="仅检查指定卡片 ID")
    parser.add_argument("--json", action="store_true", help="JSON 输出")
    parser.add_argument("--report-dir", help="#543：报告落盘目录（写 source-refs-health-latest.{md,json}，含治理聚类）")
    parser.add_argument("--max-missing", type=int, default=None,
                        help="#543：缺失数阈值——超过才 exit 1（默认 None=有任何缺失即 exit 1，旧行为）")
    parser.add_argument("--max-contaminated", type=int, default=None,
                        help="#543：污染数阈值——超过才 exit 1（默认 None=有任何污染即 exit 1，旧行为）")
    args = parser.parse_args()
    cmd_scan(args, VAULT_ROOT)


if __name__ == "__main__":
    main()
