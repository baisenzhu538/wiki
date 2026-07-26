"""KDO 知识库健康体检

四维指标：
  1. 覆盖 — 核心概念的可检索性
  2. 连通 — wikilink 双向完整性
  3. 鲜活 — 卡片更新时间分布
  4. 质量 — 门禁通过率

用法：
  python health_check.py                # 全量扫描
  python health_check.py --scope core   # 仅 reviewed + enriched（推荐）
  python health_check.py --scope reviewed  # 仅 reviewed

纯 Python 标准库，零外部依赖。
"""

import argparse
import json
import re
import os
from collections import defaultdict, Counter
from datetime import datetime, timedelta
from pathlib import Path
from typing import Any

WIKI_ROOT = Path(os.environ.get("WIKI_ROOT", r"C:\Users\Administrator\Desktop\wiki"))
CARD_DIRS = ["30_wiki/concepts", "30_wiki/frameworks", "30_wiki/tools", "30_wiki/cases"]


def parse_frontmatter(text: str) -> dict[str, Any]:
    """从 Markdown 文本中提取 YAML-like frontmatter。"""
    m = re.match(r"^---\s*\n(.*?)\n---", text, re.DOTALL)
    if not m:
        return {}
    fm = {}
    current_key = None
    current_list: list[str] = []
    for line in m.group(1).split("\n"):
        # 列表项
        if line.strip().startswith("- "):
            val = line.strip()[2:].strip()
            if current_key:
                current_list.append(val)
            continue
        # 新 key
        kv = re.match(r"^(\w+):\s*(.*)", line)
        if kv:
            if current_key and current_list:
                fm[current_key] = current_list
                current_list = []
            current_key = kv.group(1)
            val = kv.group(2).strip()
            if val:
                fm[current_key] = val
            else:
                current_list = []
    if current_key and current_list:
        fm[current_key] = current_list

    # 解析 list-like YAML strings (related / domain / source_refs)
    if "related" in fm and isinstance(fm["related"], str):
        fm["related"] = [r.strip().strip("[]'\"") for r in fm["related"].strip("[]").split(",") if r.strip()]
    return fm


def extract_wikilinks(text: str) -> set[str]:
    """提取 [[wikilink]] 目标 ID（去掉 alias 部分）。"""
    links = set()
    for m in re.finditer(r"\[\[([^\]|]+)(?:\|[^\]]+)?\]\]", text):
        target = m.group(1).strip()
        # 忽略外部 URL
        if "://" not in target and not target.startswith("<<"):
            links.add(target)
    return links


def gather_cards(scope: str = "all") -> list[dict]:
    """扫描 wiki 目录，返回所有卡片的 (id, path, frontmatter, body_wikilinks)。

    scope:
      - 'all': 全量扫描（默认）
      - 'core': 仅 status=reviewed 或 enriched
      - 'reviewed': 仅 status=reviewed
    """
    cards = []
    for d in CARD_DIRS:
        card_dir = WIKI_ROOT / d
        if not card_dir.is_dir():
            continue
        for f in sorted(card_dir.glob("*.md")):
            text = f.read_text(encoding="utf-8", errors="replace")
            fm = parse_frontmatter(text)
            card_id = fm.get("id", f.stem)
            out_links = extract_wikilinks(text)

            status = fm.get("status", "unknown")

            # scope filter
            if scope == "core" and status not in ("reviewed", "enriched"):
                continue
            if scope == "reviewed" and status != "reviewed":
                continue

            cards.append({
                "id": card_id,
                "path": str(f.relative_to(WIKI_ROOT)),
                "type": fm.get("type", "unknown"),
                "status": status,
                "updated_at": fm.get("updated_at", ""),
                "reviewed_by": fm.get("reviewed_by", ""),
                "related": [r.strip().strip("'\"[]") for r in fm.get("related", [])] if isinstance(fm.get("related"), list) else [],
                "out_links": out_links,
                "frontmatter": fm,
            })
    return cards


# ── 维度 1: 覆盖 ────────────────────────────────────────────

def check_coverage(cards: list[dict]) -> dict:
    """检查哪些核心概念可能无法通过检索命中。"""
    issues = []

    for c in cards:
        if c["status"] in ("draft", "stale", "needs-review"):
            issues.append({
                "card": c["id"],
                "path": c["path"],
                "issue": f"status={c['status']} — 检索可能返回过时或未审内容",
            })

    # 无 source_refs 的卡 = 不可溯源
    for c in cards:
        fm = c["frontmatter"]
        if not fm.get("source_refs"):
            issues.append({
                "card": c["id"],
                "path": c["path"],
                "issue": "无 source_refs — 不可溯源，置信度不可验证",
            })

    # 无 related 的孤立卡
    orphans = [c for c in cards if not c.get("related")]
    for c in orphans:
        issues.append({
            "card": c["id"],
            "path": c["path"],
            "issue": "无 related — 孤立卡，图检索无法到达",
        })

    total = len(cards)
    bad_card_ids = set(i.get("card", "") for i in issues)
    bad_card_ids.discard("")
    ok = total - len(bad_card_ids)
    return {
        "total": total,
        "pass": ok,
        "fail": len(bad_card_ids),
        "rate": f"{ok / total * 100:.1f}%" if total else "N/A",
        "issues": issues,
    }


# ── 维度 2: 连通 ────────────────────────────────────────────

def check_connectivity(cards: list[dict]) -> dict:
    """检查 wikilink 双向完整性 — 欧阳锋 F2 规则。"""
    id_set = {c["id"] for c in cards}
    broken = []

    for c in cards:
        for target in c.get("out_links", set()):
            # 跨域引用可能指向不存在的卡
            if target not in id_set:
                # 检查是否为已知的外部引用格式（如 yt- 前缀的旧卡）
                broken.append({
                    "from": c["id"],
                    "from_path": c["path"],
                    "to": target,
                })

    # 反向检查：A 的 related 引了 B，B 的 related 有没有回链 A
    missing_backlinks = []
    for c in cards:
        for target in c.get("related", []):
            target = target.strip().strip("'\"")
            if not target or target.startswith("<<"):
                continue
            target_card = next((x for x in cards if x["id"] == target), None)
            if target_card:
                target_related = target_card.get("related", [])
                if c["id"] not in [r.strip().strip("'\"") for r in target_related]:
                    missing_backlinks.append({
                        "from": c["id"],
                        "to": target,
                        "to_has_no_backlink": True,
                    })

    total_links = sum(len(c.get("out_links", set())) for c in cards)
    return {
        "total_wikilinks": total_links,
        "broken_links": len(broken),
        "broken_details": broken[:20],  # top 20
        "missing_backlinks": len(missing_backlinks),
        "missing_backlink_details": missing_backlinks[:20],
        "verdict": "🟢 全通" if not broken and not missing_backlinks else
                   f"🟡 {len(broken)} 断链 + {len(missing_backlinks)} 缺回链"
                   if len(broken) + len(missing_backlinks) < 20 else
                   f"🔴 {len(broken)} 断链 + {len(missing_backlinks)} 缺回链",
    }


# ── 维度 3: 鲜活 ────────────────────────────────────────────

def check_freshness(cards: list[dict]) -> dict:
    """检查卡片更新时间分布。"""
    now = datetime.now()
    ages = []
    stale = []
    no_date = []

    for c in cards:
        ua = c.get("updated_at", "").strip().strip("'\"")
        if not ua:
            no_date.append(c["id"])
            continue
        try:
            dt = datetime.strptime(ua[:10], "%Y-%m-%d")
            age_days = (now - dt).days
            ages.append(age_days)
            if age_days > 90:
                stale.append({"card": c["id"], "path": c["path"], "age_days": age_days})
        except ValueError:
            no_date.append(c["id"])

    if ages:
        buckets = Counter()
        for d in ages:
            if d <= 7: buckets["≤7d"] += 1
            elif d <= 30: buckets["8-30d"] += 1
            elif d <= 90: buckets["31-90d"] += 1
            else: buckets[">90d"] += 1
    else:
        buckets = {}

    return {
        "with_date": len(ages),
        "no_date": len(no_date),
        "no_date_cards": no_date[:10],
        "age_distribution": dict(buckets),
        "stale_count": len(stale),
        "stale_cards": stale[:10],
        "verdict": "🟢 全部新鲜" if len(stale) == 0 and len(no_date) == 0 else
                   f"🟡 {len(stale)} 张超90天 + {len(no_date)} 张无日期"
                   if len(stale) + len(no_date) <= 5 else
                   f"🔴 {len(stale)} 张超90天 + {len(no_date)} 张无日期",
    }


# ── 维度 4: 质量 ────────────────────────────────────────────

def check_quality(cards: list[dict]) -> dict:
    """检查门禁通过率。"""
    statuses = Counter(c["status"] for c in cards)
    reviewed_by_ouyang = [c for c in cards if "欧阳锋" in str(c.get("reviewed_by", ""))]
    has_source = [c for c in cards if c["frontmatter"].get("source_refs")]
    has_updated = [c for c in cards if c.get("updated_at", "").strip().strip("'\"")]

    issues = []
    for c in cards:
        card_issues = []
        if not c.get("updated_at", "").strip().strip("'\""):
            card_issues.append("缺 updated_at（欧阳锋 F1 扣分项）")
        if not c["frontmatter"].get("source_refs"):
            card_issues.append("缺 source_refs")
        if c["status"] == "draft" and "reviewed_by" not in c.get("frontmatter", {}):
            card_issues.append("draft 卡未指定 reviewer")
        if card_issues:
            issues.append({"card": c["id"], "path": c["path"], "issues": card_issues})

    return {
        "total": len(cards),
        "status_distribution": dict(statuses),
        "reviewed_by_欧阳锋": len(reviewed_by_ouyang),
        "has_source_refs": len(has_source),
        "has_updated_at": len(has_updated),
        "f1_violations": len(cards) - len(has_updated),
        "quality_issues": issues[:20],
        "verdict": "🟢 门禁全过" if not issues else
                   f"🟡 {len(issues)} 张卡有质量问题" if len(issues) <= 5 else
                   f"🔴 {len(issues)} 张卡有质量问题",
    }


# ── 主报告 ────────────────────────────────────────────────────

def run(scope: str = "all") -> str:
    cards = gather_cards(scope=scope)

    cov = check_coverage(cards)
    con = check_connectivity(cards)
    fresh = check_freshness(cards)
    qual = check_quality(cards)

    lines = []
    lines.append("=" * 60)
    lines.append(f"  KDO 知识库健康体检 — {datetime.now().strftime('%Y-%m-%d %H:%M')}")
    lines.append(f"  范围：{scope}  |  扫描卡片：{len(cards)} 张")
    lines.append("=" * 60)

    lines.append(f"\n📊 覆盖（可检索性）")
    lines.append(f"  通过：{cov['pass']}/{cov['total']} ({cov['rate']})")
    if cov["issues"]:
        lines.append(f"  ⚠️  {len(cov['issues'])} 个问题：")
        for i in cov["issues"][:8]:
            lines.append(f"     [{i['card']}] {i['issue']}")

    lines.append(f"\n🔗 连通（wikilink 双向完整性）")
    lines.append(f"  wikilink 总数：{con['total_wikilinks']}")
    lines.append(f"  {con['verdict']}")
    if con["broken_details"]:
        for b in con["broken_details"][:5]:
            lines.append(f"     断链：{b['from']} → {b['to']}（目标不存在）")
    if con["missing_backlink_details"]:
        for m in con["missing_backlink_details"][:5]:
            lines.append(f"     缺回链：{m['from']} → {m['to']}")

    lines.append(f"\n📅 鲜活（更新时间）")
    lines.append(f"  {fresh['verdict']}")
    if fresh["age_distribution"]:
        lines.append(f"  分布：{dict(fresh['age_distribution'])}")
    if fresh["stale_cards"]:
        for s in fresh["stale_cards"][:5]:
            lines.append(f"     {s['card']} — {s['age_days']} 天未更新")

    lines.append(f"\n✅ 质量（门禁通过率）")
    lines.append(f"  {qual['verdict']}")
    lines.append(f"  审核：{qual['reviewed_by_欧阳锋']}/{qual['total']} 欧阳锋终审")
    lines.append(f"  F1（缺 updated_at）：{qual['f1_violations']} 张")
    lines.append(f"  状态分布：{qual['status_distribution']}")
    if qual["quality_issues"]:
        for q in qual["quality_issues"][:5]:
            lines.append(f"     [{q['card']}] {', '.join(q['issues'])}")

    lines.append(f"\n{'=' * 60}")
    lines.append("体检完成。")

    report = "\n".join(lines)
    return report


if __name__ == "__main__":
    import sys
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")

    parser = argparse.ArgumentParser(description="KDO 知识库健康体检")
    parser.add_argument("--scope", choices=["all", "core", "reviewed"], default="all",
                        help="扫描范围: all=全量, core=reviewed+enriched, reviewed=仅reviewed")
    args = parser.parse_args()
    print(run(scope=args.scope))
