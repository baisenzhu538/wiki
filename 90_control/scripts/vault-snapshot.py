#!/usr/bin/env python3
"""
生成 KDO vault 一页纸状态快照，供欧阳锋等非 CLI 角色使用。

输出: 90_control/vault-status.md
用法: python 90_control/scripts/vault-snapshot.py [--days 2]
"""

import json
import re
import sys
from collections import defaultdict
from datetime import datetime, timedelta, timezone
from pathlib import Path

WIKI_DIR = Path("30_wiki")
OUTPUT_PATH = Path("90_control/vault-status.md")
DOMAIN_ORDER = ["strategy", "yitang", "decision", "research", "demand", "growth",
                "barrier", "business-model", "product", "human-ai", "design",
                "embedded", "personal-growth", "content"]


def parse_frontmatter(text: str) -> dict | None:
    if not text.startswith("---"):
        return None
    end = text.find("---", 3)
    if end == -1:
        return None
    fm_text = text[3:end].strip()
    result = {}
    for line in fm_text.split("\n"):
        if ":" in line:
            key, _, val = line.partition(":")
            key = key.strip()
            val = val.strip().strip('"').strip("'")
            # Inline YAML list: [a, b, c]
            if val.startswith("[") and val.endswith("]"):
                items = [it.strip().strip('"').strip("'") for it in val[1:-1].split(",")]
                result[key] = [it for it in items if it]
            elif val == "":
                result[key] = []  # multi-line list, scanned below
            else:
                result[key] = val
    # Crude YAML list support: scan for indented "- " lines after key with empty value
    list_keys = ["domain", "source_refs", "tags", "related"]
    for lk in list_keys:
        if lk in result and result[lk] == []:
            pat = re.compile(rf"^{lk}:\n((?:\s+-.+\n?)*)", re.MULTILINE)
            m = pat.search(text[3:end])
            if m:
                items = re.findall(r"^\s*-\s+(.+)$", m.group(1), re.MULTILINE)
                result[lk] = [it.strip().strip('"').strip("'") for it in items]
    # Also: single-item inline list like [strategy] gets split to just "strategy"
    for lk in list_keys:
        if lk in result and isinstance(result[lk], str) and result[lk].startswith("["):
            items = [it.strip().strip('"').strip("'") for it in result[lk][1:-1].split(",")]
            result[lk] = [it for it in items if it]
    return result


def scan_cards(root: Path) -> list[dict]:
    cards = []
    for f in sorted(root.rglob("*.md")):
        # Skip index/log/archive/raw
        rp = str(f.relative_to(root))
        if any(p in rp for p in ["index.md", "log.md", "_archive", "raw/"]):
            continue
        try:
            text = f.read_text(encoding="utf-8")
        except Exception:
            continue
        fm = parse_frontmatter(text)
        if not fm or "id" not in fm:
            continue
        fm["_path"] = rp
        fm["_size"] = len(text)
        # Parse date
        for dk in ["created_at", "updated_at"]:
            if dk in fm:
                try:
                    fm[dk] = datetime.fromisoformat(fm[dk].replace("Z", "+00:00"))
                except (ValueError, TypeError):
                    pass
        cards.append(fm)
    return cards


def build_snapshot(cards: list[dict], days: int = 2) -> str:
    now = datetime.now()
    cutoff = now - timedelta(days=days)
    cutoff_utc = datetime.now(timezone.utc) - timedelta(days=days)

    # --- Domain × Type matrix ---
    domain_types = defaultdict(lambda: defaultdict(int))
    domain_conf = defaultdict(list)
    all_domains = set()
    for c in cards:
        domains = c.get("domain", [])
        if isinstance(domains, str):
            domains = [domains]
        ctype = c.get("type", "unknown")
        conf = c.get("confidence", 0)
        try:
            conf = float(conf)
        except (TypeError, ValueError):
            conf = 0
        for d in domains:
            domain_types[d][ctype] += 1
            domain_conf[d].append(conf)
            all_domains.add(d)

    # --- Recent changes ---
    recent = []
    for c in cards:
        created = c.get("created_at")
        updated = c.get("updated_at")
        # Normalize to naive for comparison
        if created and created.tzinfo:
            created = created.replace(tzinfo=None)
        if updated and updated.tzinfo:
            updated = updated.replace(tzinfo=None)
        if (created and created >= cutoff) or (updated and updated >= cutoff):
            recent.append(c)

    # --- Quality ---
    total = len(cards)
    draft = sum(1 for c in cards if c.get("status") == "draft")
    needs_review = sum(1 for c in cards if c.get("status") == "needs-review")
    low_conf = 0
    for c in cards:
        conf = c.get("confidence", 0)
        try:
            conf = float(conf)
        except (TypeError, ValueError):
            conf = 1.0
        if conf < 0.7:
            low_conf += 1
    no_source = sum(1 for c in cards if not c.get("source_refs") or c["source_refs"] == [])

    # --- Build output ---
    lines = []
    lines.append(f"# KDO Vault 状态快照\n")
    lines.append(f"> 自动生成：{now.strftime('%Y-%m-%d %H:%M')} UTC")
    lines.append(f"> 卡片总数：**{total}** | draft: {draft} | needs-review: {needs_review} | 低置信度(<0.7): {low_conf} | 缺 source: {no_source}\n")

    # Domain table
    lines.append("## 域 × 类型 矩阵\n")
    all_types = sorted(set(t for dt in domain_types.values() for t in dt))
    header = ["域", "总计", "avg conf"] + all_types
    lines.append("| " + " | ".join(header) + " |")
    lines.append("|" + "---|" * len(header) + "")
    ordered_domains = [d for d in DOMAIN_ORDER if d in all_domains] + sorted(all_domains - set(DOMAIN_ORDER))
    for d in ordered_domains:
        dt = domain_types[d]
        row_total = sum(dt.values())
        avg_c = sum(domain_conf[d]) / len(domain_conf[d]) if domain_conf[d] else 0
        cells = [d, str(row_total), f"{avg_c:.2f}"]
        for t in all_types:
            cells.append(str(dt.get(t, 0)))
        lines.append("| " + " | ".join(cells) + " |")

    # Recent changes
    lines.append(f"\n## 最近 {days} 天变更（{len(recent)} 张）\n")
    if recent:
        # Group by date
        by_date = defaultdict(list)
        for c in recent:
            d = c.get("created_at") or c.get("updated_at")
            if d:
                by_date[d.strftime("%m-%d")].append(c)
        for day in sorted(by_date, reverse=True):
            lines.append(f"### {day}\n")
            for c in sorted(by_date[day], key=lambda x: x.get("id", "")):
                ctype = c.get("type", "?")
                cid = c.get("id", "?")
                title = c.get("title", cid)
                domains = c.get("domain", [])
                if isinstance(domains, str):
                    domains = [domains]
                conf = c.get("confidence", "?")
                lines.append(f"- `{cid}` [{ctype}] {title}  (conf={conf}, domain={','.join(domains)})")
            lines.append("")

    # Quality alerts
    lines.append("## 质量提示\n")
    lines.append(f"- draft 卡: {draft} 张")
    lines.append(f"- needs-review: {needs_review} 张")
    lines.append(f"- 低置信度(<0.7): {low_conf} 张")
    lines.append(f"- 缺 source_refs: {no_source} 张")

    # Top heavy domains
    lines.append("\n### 最重的域\n")
    sorted_domains = sorted(domain_types.items(), key=lambda x: sum(x[1].values()), reverse=True)
    for d, types in sorted_domains[:8]:
        total_d = sum(types.values())
        avg_c = sum(domain_conf[d]) / len(domain_conf[d]) if domain_conf[d] else 0
        type_summary = " + ".join(f"{t}={c}" for t, c in sorted(types.items()) if c > 0)
        lines.append(f"- **{d}**: {total_d} 张 (conf={avg_c:.2f}) — {type_summary}")

    lines.append(f"\n---\n*快照脚本: `90_control/scripts/vault-snapshot.py`*")
    return "\n".join(lines)


def main(days: int = 2):
    root = Path(__file__).resolve().parent.parent.parent  # vault root
    wiki = root / WIKI_DIR
    if not wiki.is_dir():
        print(f"错误：找不到 {wiki}", file=sys.stderr)
        sys.exit(1)

    cards = scan_cards(wiki)
    snapshot = build_snapshot(cards, days=days)

    out = root / OUTPUT_PATH
    out.write_text(snapshot, encoding="utf-8")
    print(f"已写入: {out}")
    dc = set()
    for c in cards:
        d = c.get("domain", [])
        if isinstance(d, str):
            dc.add(d)
        elif isinstance(d, list):
            dc.update(d)
    print(f"卡片: {len(cards)} | 域: {len(dc)}")


if __name__ == "__main__":
    import argparse
    p = argparse.ArgumentParser(description="生成 vault 状态快照")
    p.add_argument("--days", type=int, default=2, help="最近 N 天的变更窗口（默认 2）")
    args = p.parse_args()
    main(days=args.days)
