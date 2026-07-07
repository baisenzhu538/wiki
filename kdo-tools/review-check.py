#!/usr/bin/env python3
"""Agent 复盘检查 v2 — 格式统一 + 内容深度验证 + 审计日报。

Usage:
  python kdo-tools/review-check.py          # 全量检查，输出审计日报
  python kdo-tools/review-check.py --json   # JSON 输出，供脚本消费
  python kdo-tools/review-check.py --agent huangyaoshi  # 单 Agent 检查
"""

import json
import sys
from datetime import datetime, timezone
from pathlib import Path

REVIEW_DIR = Path.home() / "Desktop" / "agent复盘"

# Agent ID 映射：程序ID → (中文名, 是否活跃)
AGENTS = {
    "huangyaoshi":              ("黄药师", True),
    "wangyuyan":                ("王语嫣", True),
    "laowantong":               ("老顽童", True),
    "ouyangfeng":               ("欧阳锋", True),
    "hongqigong":               ("洪七公", True),
    "duanwangye":               ("段王爷", True),
    "sales-dialogue-assistant": ("销售对话参谋", True),
}

# Truman 10章必须标题（用于格式完整性检查）
TEN_CHAPTERS = [
    "概要",
    "关键决策",
    "思维盲点",
    "顿悟",
    "过程资产",
    "元反思",
    "逐轮映射",
    "飞轮效应",
    "对照实验",
    "下次改进",
]

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")


RETRIEVAL_SIGNALS = [
    "kdo query", "kdo-tools", "wiki", "检索", "知识库检索",
    "cross-domain-patterns", "Read 30_wiki", "Read .agent",
    "查了知识库", "查了wiki", "搜了wiki",
]
RETRIEVAL_DISCOVERY = [
    "发现", "找到", "纠正", "之前不知道", "才知道",
    "漏了", "没找到", "没有覆盖", "不存在",
]


def check_retrieval(content: str) -> dict:
    """检查复盘中是否包含 wiki 检索行为（§10.4.1 要求）。"""
    has_mention = any(sig.lower() in content.lower() for sig in RETRIEVAL_SIGNALS)
    has_discovery = any(sig in content for sig in RETRIEVAL_DISCOVERY)
    return {
        "has_retrieval": has_mention,
        "has_discovery": has_mention and has_discovery,
    }


def check_content_depth(content: str, size: int) -> dict:
    """检查复盘内容深度，返回等级和详情。"""
    chapters_found = [ch for ch in TEN_CHAPTERS if ch in content]
    chapter_count = len(chapters_found)
    missing = [ch for ch in TEN_CHAPTERS if ch not in content]

    # 检查盲点是否追问了"为什么"
    blindspot_has_why = False
    blindspot_count = 0
    if "思维盲点" in content:
        bs_start = content.find("思维盲点")
        bs_end = content.find("##", bs_start + 1) if content.find("##", bs_start + 1) > 0 else len(content)
        blindspot_section = content[bs_start:bs_end]
        blindspot_count = blindspot_section.count("\n") // 2  # rough estimate
        blindspot_has_why = any(kw in blindspot_section for kw in ["为什么漏", "为什么没", "根因", "原因"])

    retrieval = check_retrieval(content)

    # A 级：≥3000B + 10章 + 盲点≥2且有追问 + 检索有发现（§10.4.1 A级要求）
    if (size >= 3000 and chapter_count == 10
            and blindspot_count >= 2 and blindspot_has_why
            and retrieval["has_discovery"]):
        grade = "A"
        emoji = "🟢"
    # B 级：≥1500B + 8章以上 + 盲点≥1 + 至少提及检索（§10.4.1 B级要求）
    elif size >= 1500 and chapter_count >= 8 and retrieval["has_retrieval"]:
        grade = "B"
        emoji = "🟡"
    else:
        grade = "C"
        emoji = "🔴"

    return {
        "grade": grade,
        "emoji": emoji,
        "size": size,
        "chapter_count": chapter_count,
        "missing": missing,
        "blindspot_count": blindspot_count,
        "blindspot_has_why": blindspot_has_why,
        "retrieval": retrieval,
    }


def check_agent(agent_id: str, today: str) -> list[dict]:
    """检查单个 Agent 的复盘状态。返回列表——每个实例一条记录。"""
    cn_name, active = AGENTS.get(agent_id, (agent_id, True))

    if not active:
        return [{"agent": agent_id, "cn_name": cn_name, "status": "inactive", "grade": None}]

    agent_dir = REVIEW_DIR / agent_id / "daily-context"
    if not agent_dir.exists():
        return [{"agent": agent_id, "cn_name": cn_name, "status": "missing", "grade": None, "emoji": "❌", "size": 0}]

    # 扫描当天所有文件：YYYY-MM-DD.md + YYYY-MM-DD-<instance>.md
    candidates = sorted(agent_dir.glob(f"{today}*.md"))
    if not candidates:
        return [{"agent": agent_id, "cn_name": cn_name, "status": "missing", "grade": None, "emoji": "❌", "size": 0}]

    results = []
    for f in candidates:
        instance = ""
        stem = f.stem  # e.g. "2026-07-08" or "2026-07-08-hermes"
        if stem != today:
            instance = stem[len(today) + 1:]  # extract "hermes" from "2026-07-08-hermes"

        try:
            content = f.read_text(encoding="utf-8", errors="ignore")
            size = f.stat().st_size
        except Exception:
            results.append({"agent": agent_id, "cn_name": cn_name, "status": "error", "grade": None, "emoji": "❌", "size": 0, "instance": instance})
            continue

        depth = check_content_depth(content, size)
        results.append({
            "agent": agent_id,
            "cn_name": cn_name,
            "status": "ok",
            "instance": instance,
            **depth,
        })

    return results


def print_report(results: list, today: str):
    """输出审计日报（人读格式）。"""
    ok = [r for r in results if r["status"] == "ok"]
    missing = [r for r in results if r["status"] == "missing"]
    inactive = [r for r in results if r["status"] == "inactive"]

    a_count = sum(1 for r in ok if r["grade"] == "A")
    b_count = sum(1 for r in ok if r["grade"] == "B")
    c_count = sum(1 for r in ok if r["grade"] == "C")
    total_active = len(results) - len(inactive)

    print(f"Agent 复盘审计 — {today}\n")

    for r in results:
        label = r['agent'] + (f"/{r['instance']}" if r.get('instance') else "")
        if r["status"] == "missing":
            print(f"  {label:<32} ❌ 未复盘")
        elif r["status"] == "error":
            print(f"  {label:<32} ❌ 读取失败")
        elif r["status"] == "inactive":
            print(f"  {label:<32} ⏸️ 非活跃")
        elif r["grade"] == "A":
            retrieval_note = " 📚检索有发现" if r.get("retrieval", {}).get("has_discovery") else ""
            print(f"  {label:<32} 🟢 A级 ({r['size']}B) — {r['chapter_count']}/10章，盲点≥2且有追问{retrieval_note}")
        elif r["grade"] == "B":
            missing_str = f"，缺{'、'.join(r['missing'][:3])}" if r['missing'] else ""
            retrieval_note = " ✅已检索" if r.get("retrieval", {}).get("has_retrieval") else ""
            print(f"  {label:<32} 🟡 B级 ({r['size']}B) — {r['chapter_count']}/10章{missing_str}{retrieval_note}")
        else:
            reasons = []
            if r.get('size', 0) < 1500:
                reasons.append(f"仅{r['size']}B")
            if r.get('chapter_count', 0) < 8:
                reasons.append(f"仅{r.get('chapter_count', 0)}/10章")
            if r.get('blindspot_count', 0) > 0 and not r.get('blindspot_has_why'):
                reasons.append("盲点未追问")
            if not r.get("retrieval", {}).get("has_retrieval"):
                reasons.append("未检索wiki")
            why = "、".join(reasons) if reasons else f"仅{r['size']}B"
            print(f"  {label:<32} 🔴 C级 ({r['size']}B) — {why}")

    print(f"  {'─' * 60}")
    print(f"  覆盖率：{len(ok)}/{total_active}   A级率：{a_count}/{total_active}   B级以上：{a_count + b_count}/{total_active}")

    # 连续达标追踪
    if len(missing) == 0 and c_count == 0:
        print(f"  🏆 全 Agent 复盘达标（B 级以上）")
    else:
        if missing:
            names = ", ".join(r["cn_name"] for r in missing)
            print(f"  ⚠️ 未复盘：{names}")
        if c_count > 0:
            names = ", ".join(r["cn_name"] for r in ok if r["grade"] == "C")
            print(f"  ⚠️ 形式主义：{names}")

    return 0 if len(missing) == 0 and c_count == 0 else 1


def main():
    today = datetime.now().strftime("%Y-%m-%d")
    use_json = "--json" in sys.argv
    single_agent = None

    for i, arg in enumerate(sys.argv):
        if arg == "--agent" and i + 1 < len(sys.argv):
            single_agent = sys.argv[i + 1]

    agents_to_check = [single_agent] if single_agent else list(AGENTS.keys())
    results = []
    for a in agents_to_check:
        results.extend(check_agent(a, today))

    if use_json:
        print(json.dumps({"date": today, "results": results}, ensure_ascii=False, indent=2))
    else:
        rc = print_report(results, today)
        sys.exit(rc)


if __name__ == "__main__":
    main()
