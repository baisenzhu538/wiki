#!/usr/bin/env python3
"""域解压审计——检查每个域的 framework 卡是否有足够的解压资产配套。

解压比 = framework 卡数 : (tool + skill + workflow + case + agent-spec) 卡数
底线: 1 framework → ≥3 解压资产。低于此比例的域标记为「压缩过度」。

用法:
    python 90_control/scripts/domain-decompression-audit.py           # 全库审计
    python 90_control/scripts/domain-decompression-audit.py --domain C域  # 单域审计
    python 90_control/scripts/domain-decompression-audit.py --json    # JSON 输出
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from collections import defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent.parent
WIKI_DIR = ROOT / "30_wiki"

# Card types: compression (上游/抽象) vs decompression (下游/操作)
COMPRESSION_TYPES = {"framework"}
DECOMPRESSION_TYPES = {"tool", "skill", "workflow", "case", "agent-spec"}
ALL_TYPES = COMPRESSION_TYPES | DECOMPRESSION_TYPES | {"concept", "dk", "method", "bridge", "index"}


def parse_frontmatter(path: Path) -> dict:
    """Extract YAML frontmatter from a markdown card."""
    text = path.read_text(encoding="utf-8", errors="ignore")
    if not text.startswith("---"):
        return {}
    match = re.match(r"^---\r?\n(.*?)\r?\n---", text, re.DOTALL)
    if not match:
        return {}
    try:
        import yaml
        return yaml.safe_load(match.group(1)) or {}
    except Exception:
        return {}


def card_type(fm: dict) -> str:
    """Determine card type from frontmatter — type field or filename prefix."""
    t = fm.get("type", "")
    if isinstance(t, str) and t.strip():
        return t.strip().lower()
    return "unknown"


def card_domain(fm: dict) -> str:
    """Extract primary domain from frontmatter."""
    d = fm.get("domain", "")
    if isinstance(d, list):
        return d[0] if d else "unknown"
    if isinstance(d, str):
        return d.strip() or "unknown"
    return "unknown"


def scan_wiki(wiki_dir: Path = WIKI_DIR) -> dict[str, dict]:
    """Scan all cards in wiki and group by domain.

    Returns: {domain: {type: count, cards: [path, ...]}}
    """
    domains: dict[str, dict] = defaultdict(lambda: defaultdict(lambda: {"count": 0, "cards": []}))

    for path in wiki_dir.rglob("*.md"):
        fm = parse_frontmatter(path)
        t = card_type(fm)
        if t == "unknown":
            continue
        domain = card_domain(fm)
        domains[domain][t]["count"] += 1
        domains[domain][t]["cards"].append(str(path.relative_to(ROOT)))

    return {k: dict(v) for k, v in domains.items()}


def audit_domain(name: str, data: dict) -> dict:
    """Audit a single domain's decompression ratio."""
    frameworks = data.get("framework", {}).get("count", 0)
    decomp_count = sum(data.get(t, {}).get("count", 0) for t in DECOMPRESSION_TYPES)
    total = sum(data.get(t, {}).get("count", 0) for t in ALL_TYPES)

    if frameworks == 0:
        ratio = None
        status = "no_frameworks"
    else:
        ratio = decomp_count / frameworks
        if ratio < 1.0:
            status = "critical"
        elif ratio < 3.0:
            status = "compression_heavy"
        elif ratio <= 10.0:
            status = "healthy"
        else:
            status = "tool_heavy"

    return {
        "domain": name,
        "total_cards": total,
        "frameworks": frameworks,
        "decompression_assets": decomp_count,
        "ratio": round(ratio, 1) if ratio is not None else None,
        "status": status,
        "detail": {t: data.get(t, {}).get("count", 0) for t in ALL_TYPES},
    }


def render_report(results: list[dict], json_output: bool = False) -> str:
    """Render audit results."""
    if json_output:
        return json.dumps(results, ensure_ascii=False, indent=2)

    lines = []
    lines.append("=" * 70)
    lines.append("  KDO 域解压审计报告")
    lines.append("  解压比 = (tool + skill + workflow + case + agent-spec) / framework")
    lines.append("  底线：≥ 3.0 = healthy, < 3.0 = compression_heavy, < 1.0 = critical")
    lines.append("=" * 70)
    lines.append("")

    # Sort by status severity then by ratio
    severity = {"critical": 0, "compression_heavy": 1, "no_frameworks": 2, "healthy": 3, "tool_heavy": 4}
    results.sort(key=lambda r: (severity.get(r["status"], 99), r["ratio"] or 999))

    status_icon = {
        "critical": "🔴",
        "compression_heavy": "🟡",
        "no_frameworks": "⚪",
        "healthy": "🟢",
        "tool_heavy": "🔵",
    }

    critical = [r for r in results if r["status"] == "critical"]
    heavy = [r for r in results if r["status"] == "compression_heavy"]
    healthy = [r for r in results if r["status"] == "healthy"]

    lines.append(f"  总域数: {len(results)}")
    lines.append(f"  🔴 critical (<1.0): {len(critical)}")
    lines.append(f"  🟡 compression_heavy (<3.0): {len(heavy)}")
    lines.append(f"  🟢 healthy (≥3.0): {len(healthy)}")
    lines.append("")

    for r in results:
        icon = status_icon.get(r["status"], "  ")
        ratio_str = f"{r['ratio']:.1f}" if r["ratio"] is not None else "N/A"
        lines.append(f"  {icon} {r['domain']}")
        lines.append(f"     frameworks={r['frameworks']}  decomp={r['decompression_assets']}  ratio={ratio_str}  total={r['total_cards']}")
        detail_parts = []
        for t in ["framework", "concept", "method", "tool", "skill", "workflow", "case", "agent-spec", "dk", "bridge"]:
            c = r["detail"].get(t, 0)
            if c > 0:
                detail_parts.append(f"{t}={c}")
        lines.append(f"     明细: {', '.join(detail_parts)}")
        lines.append("")

    # Recommendations
    if critical or heavy:
        lines.append("---")
        lines.append("  建议优先修复的域 (compression_heavy + critical):")
        for r in [*critical, *heavy]:
            needed = max(0, (r["frameworks"] * 3) - r["decompression_assets"])
            lines.append(f"    {r['domain']}: 需补 ≥{needed} 张解压资产 (tool/skill/case/agent-spec)")
        lines.append("")

    return "\n".join(lines)


def main():
    parser = argparse.ArgumentParser(description="KDO 域解压审计")
    parser.add_argument("--domain", help="只审计指定域")
    parser.add_argument("--json", action="store_true", help="JSON 输出")
    parser.add_argument("--min-cards", type=int, default=5, help="最小卡片数阈值，低于此数的域不审计 (default: 5)")
    args = parser.parse_args()

    domains = scan_wiki(WIKI_DIR)

    if args.domain:
        target = args.domain
        if target not in domains:
            print(f"域 '{target}' 未找到。可用域: {', '.join(sorted(domains.keys()))}", file=sys.stderr)
            sys.exit(1)
        domains = {target: domains[target]}

    results = []
    for name, data in sorted(domains.items()):
        total = sum(data.get(t, {}).get("count", 0) for t in ALL_TYPES)
        if total < args.min_cards:
            continue
        results.append(audit_domain(name, data))

    output = render_report(results, json_output=args.json)
    print(output)


if __name__ == "__main__":
    main()
