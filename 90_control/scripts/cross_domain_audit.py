#!/usr/bin/env python3
"""
跨域 related 链接审计脚本。

独立运行:  python 90_control/scripts/cross_domain_audit.py
指定路径:  python 90_control/scripts/cross_domain_audit.py --vault C:/path/to/vault
指定白名单: python 90_control/scripts/cross_domain_audit.py --whitelist 90_control/cross-domain-whitelist.json
"""

import re, json, sys
from collections import defaultdict
from datetime import datetime
from pathlib import Path


# ── Frontmatter 解析（与 vault-snapshot.py 共享逻辑）──

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
            key, val = key.strip(), val.strip().strip('"').strip("'")
            if val.startswith("[") and val.endswith("]"):
                items = [it.strip().strip('"').strip("'") for it in val[1:-1].split(",")]
                result[key] = [it for it in items if it]
            elif val == "":
                result[key] = []
            else:
                result[key] = val
    list_keys = ["domain", "related", "source_refs", "tags"]
    for lk in list_keys:
        if lk in result and result[lk] == []:
            pat = re.compile(rf"^{lk}:\n((?:\s*-+.+\n?)*)", re.MULTILINE)
            m = pat.search(text[3:end])
            if m:
                items = re.findall(r"^\s*-+\s*(.+)$", m.group(1), re.MULTILINE)
                result[lk] = [it.strip().strip('"').strip("'") for it in items]
    return result


# ── 域判定 ──

# 前缀 → 域映射（启发式回退）
PREFIX_DOMAIN = {
    "framework-strategy": "strategy",
    "tool-strategy": "strategy",
    "case-strategy": "strategy",
    "dk-strategy": "strategy",
    "concept-strategy": "strategy",
    "framework-lean": "lean-startup",
    "tool-lean": "lean-startup",
    "case-lean": "lean-startup",
    "dk-lean": "lean-startup",
    "framework-five-step": "five-step",
    "yt-five-step": "five-step",
    "yt-entrepreneur": "entrepreneurship",
    "yt-decision": "decision",
    "yt-demand": "demand-analysis",
    "yt-barrier": "barrier",
    "yt-growth": "growth",
    "yt-business-model": "business-model",
    "yt-product": "product",
    "yt-model": "modeling",
    "yt-research": "research",
    "yt-foresight": "foresight",
    "tool-agent": "ai-collaboration",
    "tool-demand": "demand-analysis",
    "framework-demand": "demand-analysis",
    "framework-ai": "ai-collaboration",
    "framework-yitang": "yitang",
    "tool-yitang": "yitang",
    "case-yitang": "yitang",
    "dk-yitang": "yitang",
    "concept-yitang": "yitang",
    "concept-harness": "ai-collaboration",
    "concept-candy": "content-production",
    "framework-multi-agent": "ai-collaboration",
    "ai-short-drama": "ai-saas",
    "concept-mckinsey": "management",
    "framework-candy": "content-production",
    "framework-doris": "research",
    "concept-toyota": "management",
    "concept-maister": "management",
    "concept-minto": "management",
    "framework-course": "yitang",
    "framework-ci": "yitang",
    "business-formula": "yitang",
    "beverage-foodservice": "yitang",
    "ai-native": "ai-saas",
    "ai-complex": "ai-saas",
    "framework-harness": "ai-collaboration",
    "framework-learning": "learning-methodology",
    "concept-harness": "ai-collaboration",
}


def id_to_domain(card_id: str) -> str:
    """前缀启发式推断域。"""
    for prefix, domain in PREFIX_DOMAIN.items():
        if card_id.startswith(prefix):
            return domain
    return "unknown"


# ── Bridge 卡定义 ──

BRIDGE_CARDS = {
    "framework-strategy-lean-validation": {"strategy", "lean-startup"},
    "framework-five-step-lean-interface": {"five-step", "lean-startup"},
    "framework-lean-pivot-decision": {"lean-startup", "decision"},
    "framework-ai-accelerated-strategy-cycle": {"strategy", "lean-startup", "ai-collaboration"},
    "framework-demand-lean-bridge": {"demand-analysis", "lean-startup"},
}


# ── 审计逻辑 ──

def load_cards(vault: Path) -> dict[str, dict]:
    """加载 30_wiki/ 所有卡片，返回 id → frontmatter 映射。"""
    cards = {}
    wiki = vault / "30_wiki"
    for f in wiki.rglob("*.md"):
        if any(p in str(f) for p in ["_archive", "raw/", ".git"]):
            continue
        try:
            text = f.read_text(encoding="utf-8")
        except Exception:
            continue
        fm = parse_frontmatter(text)
        if not fm or "id" not in fm:
            continue
        fm["_path"] = str(f.relative_to(vault)).replace("\\", "/")
        cards[fm["id"]] = fm
    return cards


def domain_of(card_id: str, cards: dict) -> str | None:
    """获取卡片的域：优先 frontmatter domain 字段，回退前缀启发式。"""
    if card_id not in cards:
        return id_to_domain(card_id)
    fm = cards[card_id]
    domains = fm.get("domain", [])
    if isinstance(domains, str):
        domains = [domains]
    if domains:
        # 过滤掉内部标签域
        real = [d for d in domains if d not in ("master", "system", "", "[]")]
        if real:
            return real[0]
    return id_to_domain(card_id)


def extract_related_ids(fm: dict) -> list[str]:
    """从 frontmatter 的 related 字段提取纯 ID 列表。"""
    rel = fm.get("related", [])
    if isinstance(rel, str):
        rel = [rel]
    ids = []
    for r in rel:
        m = re.search(r'\[\[([^\]|]+)', r)
        if m:
            ids.append(m.group(1).strip())
        else:
            ids.append(r.strip())
    return ids


def run_audit(vault: Path, whitelist: set) -> dict:
    cards = load_cards(vault)
    issues = {"rule1": [], "rule2": [], "rule3": []}

    for cid, fm in cards.items():
        ctype = fm.get("type", "?")
        related_ids = extract_related_ids(fm)
        related_domains = {domain_of(rid, cards) for rid in related_ids if rid}
        related_domains.discard(None)
        related_domains.discard("unknown")

        # 规则 1：framework/tool 卡必须跨域 ≥2
        if ctype in ("framework", "tool") and cid not in whitelist:
            if len(related_domains) < 2:
                my_domain = domain_of(cid, cards) or "unknown"
                issues["rule1"].append({
                    "id": cid,
                    "type": ctype,
                    "title": fm.get("title", cid),
                    "own_domain": my_domain,
                    "related_domains": sorted(related_domains),
                })

        # 规则 2：bridge 卡目标域覆盖
        if cid in BRIDGE_CARDS:
            target = BRIDGE_CARDS[cid]
            covered = related_domains & target
            missing = target - covered
            if len(covered) < 2:
                issues["rule2"].append({
                    "id": cid,
                    "target_domains": sorted(target),
                    "covered": sorted(covered),
                    "missing": sorted(missing),
                })

        # 规则 3：domain digest 必须链接 ≥2 个其他 digest
        if fm.get("type") == "index" and cid.endswith("-domain-digest") and cid not in whitelist:
            linked_digests = [r for r in related_ids if r.endswith("-domain-digest") and r != cid]
            if len(linked_digests) < 2:
                issues["rule3"].append({
                    "id": cid,
                    "linked_digests": linked_digests,
                })

    return {"cards": cards, "issues": issues}


def generate_report(vault: Path, whitelist: set, output: Path) -> str:
    result = run_audit(vault, whitelist)
    cards = result["cards"]
    issues = result["issues"]

    total_issues = len(issues["rule1"]) + len(issues["rule2"]) + len(issues["rule3"])
    now = datetime.now().strftime("%Y-%m-%d %H:%M")

    lines = []
    lines.append(f"# 跨域链接审计报告\n")
    lines.append(f"**执行时间**：{now}")
    lines.append(f"**总检查卡数**：{len(cards)}")
    lines.append(f"**异常卡数**：{total_issues}\n")

    # Rule 1
    lines.append(f"## 1. framework/tool 卡未跨域（{len(issues['rule1'])} 张）\n")
    if issues["rule1"]:
        lines.append("| 卡 ID | 类型 | 自身域 | 当前跨域 |")
        lines.append("|:--|:--|:--|:--|")
        for i in sorted(issues["rule1"], key=lambda x: x["id"]):
            cross = ", ".join(i["related_domains"]) if i["related_domains"] else "无"
            lines.append(f"| `{i['id']}` | {i['type']} | {i['own_domain']} | {cross} |")
    else:
        lines.append("✅ 全部通过\n")

    # Rule 2
    lines.append(f"\n## 2. bridge 卡目标域覆盖（{len(issues['rule2'])} 张不足）\n")
    if issues["rule2"]:
        lines.append("| 卡 ID | 目标域 | 已覆盖 | 缺失 |")
        lines.append("|:--|:--|:--|:--|")
        for i in sorted(issues["rule2"], key=lambda x: x["id"]):
            lines.append(f"| `{i['id']}` | {', '.join(i['target_domains'])} | {', '.join(i['covered']) or '无'} | {', '.join(i['missing'])} |")
    else:
        lines.append("✅ 全部 bridge 卡目标域覆盖 ≥2\n")

    # Rule 3
    lines.append(f"\n## 3. domain digest 链接不足（{len(issues['rule3'])} 个）\n")
    if issues["rule3"]:
        lines.append("| digest ID | 当前 linked digests | 建议 |")
        lines.append("|:--|:--|:--|")
        for i in sorted(issues["rule3"], key=lambda x: x["id"]):
            lines.append(f"| `{i['id']}` | {', '.join(i['linked_digests']) or '无'} | 补充 2+ 个相关域 digest |")
    else:
        lines.append("✅ 全部 digest 链接 ≥2\n")

    # Whitelist
    lines.append(f"\n## 4. 白名单（{len(whitelist)} 项）\n")
    for w in sorted(whitelist):
        lines.append(f"- `{w}`")

    lines.append(f"\n---\n*审计脚本: `90_control/scripts/cross_domain_audit.py`*")

    report = "\n".join(lines)
    if output:
        output.write_text(report, encoding="utf-8")
    return report


def load_whitelist(path: Path) -> set:
    if not path.exists():
        # 默认白名单
        return {
            "tool-agent-crawl4ai",
            "tool-agent-firecrawl",
            "tool-strategy-gap-analysis",
        }
    data = json.loads(path.read_text(encoding="utf-8"))
    return set(data)


if __name__ == "__main__":
    import argparse
    p = argparse.ArgumentParser(description="跨域 related 链接审计")
    p.add_argument("--vault", default=r"C:\Users\Administrator\Desktop\wiki",
                   help="Vault 根目录")
    p.add_argument("--report", default=r"C:\Users\Administrator\Desktop\wiki\60_feedback\audit\cross-domain-link-report.md",
                   help="报告输出路径")
    p.add_argument("--whitelist", default=r"C:\Users\Administrator\Desktop\wiki\90_control\cross-domain-audit-whitelist.json",
                   help="白名单 JSON 文件路径")
    p.add_argument("--stdout", action="store_true", help="同时输出到 stdout")
    args = p.parse_args()

    vault = Path(args.vault)
    report_path = Path(args.report)
    report_path.parent.mkdir(parents=True, exist_ok=True)
    whitelist = load_whitelist(Path(args.whitelist))

    report = generate_report(vault, whitelist, report_path)
    if args.stdout:
        print(report)
    else:
        # 只打印摘要
        result = run_audit(vault, whitelist)
        total = len(result["issues"]["rule1"]) + len(result["issues"]["rule2"]) + len(result["issues"]["rule3"])
        print(f"审计完成: {len(result['cards'])} 张卡, {total} 个异常")
        print(f"  规则1 (未跨域):  {len(result['issues']['rule1'])}")
        print(f"  规则2 (bridge):  {len(result['issues']['rule2'])}")
        print(f"  规则3 (digest):  {len(result['issues']['rule3'])}")
        print(f"  报告: {report_path}")
