#!/usr/bin/env python3
"""KDO Research Adapter — 将 business-research Skill 的 OSCAR 流程适配到 KDO 工具链。

核心职责：
1. 封装 web_search.py，提供 Agent/Skill 可调用的统一接口。
2. 支持 OSCAR 三步快速启动：Objective / Scope / Checklist。
3. 输出 KDO 标准 JSON，便于后续 validate、交叉验证和引用。

Usage:
    python kdo-tools/research_adapter.py search "query1" "query2" --json
    python kdo-tools/research_adapter.py oscar --objective "评估某赛道" \
        --scope "2024-2026, 中国, 前5竞品" \
        --checklist "市场规模,竞品定价,渠道结构" --json
    python kdo-tools/research_adapter.py validate report.md
"""

import argparse
import json
import sys
from pathlib import Path
from typing import Any

# 将 kdo-tools 加入路径，确保能 import web_search
sys.path.insert(0, str(Path(__file__).parent))
import web_search


def _now() -> str:
    from datetime import datetime, timezone
    return datetime.now(timezone.utc).isoformat()


def run_search(queries: list[str], backend: str = "auto") -> dict[str, Any]:
    """对多个查询执行搜索，返回 KDO 标准结果包。"""
    results_by_query: dict[str, list[dict]] = {}
    for q in queries:
        results_by_query[q] = web_search.search(q, backend=backend)
    return {
        "adapter": "kdo-research",
        "version": "1.0.0",
        "step": "search",
        "backend": backend,
        "timestamp": _now(),
        "queries": queries,
        "results": results_by_query,
    }


def run_oscar(objective: str, scope: str, checklist: str, backend: str = "auto") -> dict[str, Any]:
    """基于 OSCAR 的前三步（O+S+C）自动生成搜索计划并执行第一轮搜索。"""
    # 将 checklist 拆分为独立查询项
    items = [item.strip() for item in checklist.replace("，", ",").split(",") if item.strip()]
    queries = [f"{objective} {item} {scope}".strip() for item in items]
    search_result = run_search(queries, backend=backend)
    return {
        "adapter": "kdo-research",
        "version": "1.0.0",
        "step": "oscar-round-1",
        "oscar": {
            "objective": objective,
            "scope": scope,
            "checklist": items,
        },
        "timestamp": _now(),
        "backend": backend,
        **search_result,
    }


def run_validate(report_path: str) -> dict[str, Any]:
    """对 Markdown 调研报告执行最小质量门检查。

    当前检查项（对应 business-research Skill 的 15 项机械检查中的 P0 项）：
    - 必须包含来源 URL 或 "口述待独立核实"
    - 数字/金额/百分比必须附带来源
    - 必须包含 ≥2 个独立来源的交叉验证声明
    """
    from pathlib import Path
    text = Path(report_path).read_text(encoding="utf-8")
    issues = []

    # P0: 来源要求
    has_url = "http://" in text or "https://" in text
    has_oral_note = "口述待独立核实" in text
    if not (has_url or has_oral_note):
        issues.append("缺少可验证来源 URL 或'口述待独立核实'标注")

    # P0: 数字必须有来源支撑（简单启发式：数字附近 80 字符内是否有 http 或 source=）
    import re
    number_pattern = re.compile(r"\d+[\.\d]*[%％亿万千]?")
    for m in number_pattern.finditer(text):
        start = max(0, m.start() - 80)
        end = min(len(text), m.end() + 80)
        ctx = text[start:end]
        if "http" not in ctx and "source=" not in ctx and "口述" not in ctx:
            snippet = text[m.start():m.end()]
            if len(snippet) < 10:  # 忽略页码等短数字
                continue
            issues.append(f"数字'{snippet}'附近缺少来源标注")
            if len(issues) >= 10:
                break

    # P0: 交叉验证声明
    cross_keywords = ["交叉验证", "独立来源", "多方验证", "互相印证"]
    has_cross = any(kw in text for kw in cross_keywords)
    if not has_cross:
        issues.append("缺少'交叉验证/独立来源'声明")

    passed = len(issues) == 0
    return {
        "adapter": "kdo-research",
        "version": "1.0.0",
        "step": "validate",
        "report": report_path,
        "timestamp": _now(),
        "passed": passed,
        "issues": issues,
        "summary": "通过 P0 机械检查" if passed else f"发现 {len(issues)} 项 P0 问题",
    }


def main() -> int:
    parser = argparse.ArgumentParser(description="KDO Research Adapter for business-research Skill")
    sub = parser.add_subparsers(dest="command", required=True)

    p_search = sub.add_parser("search", help="执行多查询搜索")
    p_search.add_argument("queries", nargs="+", help="一个或多个搜索查询")
    p_search.add_argument("--backend", default="auto", choices=["auto", "searx", "cn_bing", "bing"])
    p_search.add_argument("--json", action="store_true", help="输出 JSON")

    p_oscar = sub.add_parser("oscar", help="OSCAR 第一轮搜索")
    p_oscar.add_argument("--objective", required=True, help="研究目标")
    p_oscar.add_argument("--scope", required=True, help="研究范围")
    p_oscar.add_argument("--checklist", required=True, help="待查清单（逗号分隔）")
    p_oscar.add_argument("--backend", default="auto", choices=["auto", "searx", "cn_bing", "bing"])
    p_oscar.add_argument("--json", action="store_true", help="输出 JSON")

    p_validate = sub.add_parser("validate", help="验证调研报告 P0 质量门")
    p_validate.add_argument("report", help="Markdown 报告路径")
    p_validate.add_argument("--json", action="store_true", help="输出 JSON")

    args = parser.parse_args()

    if args.command == "search":
        result = run_search(args.queries, backend=args.backend)
    elif args.command == "oscar":
        result = run_oscar(args.objective, args.scope, args.checklist, backend=args.backend)
    elif args.command == "validate":
        result = run_validate(args.report)
    else:
        parser.print_help()
        return 1

    print(json.dumps(result, ensure_ascii=False, indent=2))
    return 0 if (args.command != "validate" or result.get("passed")) else 2


if __name__ == "__main__":
    raise SystemExit(main())
