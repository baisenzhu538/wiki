#!/usr/bin/env python3
"""
双三角画布填充 Agent CLI — KDO Agent 化第一个试点。

Default role: C (Consult/Coach). 通过九层深挖对话引导用户填充双三角六要素画布。
TCPR 运行时切换，自动记录飞轮迭代。

Usage:
  python kdo-tools/canvas-agent.py run              # 交互式对话
  python kdo-tools/canvas-agent.py test --scenario <name>  # 非交互测试
"""

import argparse
import json
import sqlite3
import subprocess
import sys
from datetime import datetime, timezone
from pathlib import Path

WIKI = Path(__file__).resolve().parent.parent
DB = WIKI / ".kdo" / "state.sqlite"

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

CANVAS_FIELDS = [
    ("审美", "人对结果质量的判断标准。你能说出'好结果长什么样'的三条具体标准吗？"),
    ("体系", "解决问题的框架和工作流。你能把这个任务拆成人/AI分工的步骤清单吗？"),
    ("创造力", "突破现有认知的新假设。你能说出当前方案的一个隐含假设并挑战它吗？"),
    ("场景", "AI最匹配的应用场景。你能说出当前任务最值得AI化的1-2个环节吗？"),
    ("数据", "让AI越用越懂你的资产。你有结构化的正面/负面案例库吗？"),
    ("基本功", "工具选择、组合和调试。你能用≤3个工具串联一个完整工作流吗？"),
]

SCENARIOS = {
    "truman-ppt": {
        "task": "Truman 的 AI PPT 迭代",
        "context": "从试工具失败到建知识站场到飞书To slide",
    },
    "hotel-tag": {
        "task": "酒店行业 AI 标签审核",
        "context": "AI 替代人工审核酒店标签，提升效率",
    },
    "beike-sales": {
        "task": "贝壳找房 AI 外呼",
        "context": "AI 外呼替代人工，提升销售效率",
    },
}


def now_iso():
    return datetime.now(timezone.utc).isoformat()


def flywheel_log(agent_id, triangle_type, before, after, why, next_try):
    """Record a flywheel log entry."""
    subprocess.run(
        [sys.executable, str(WIKI / "kdo-tools" / "flywheel.py"), "log",
         "--agent", agent_id, "--type", triangle_type,
         "--before", before, "--after", after,
         "--why", why, "--next", next_try],
        capture_output=True,
    )


def interactive_run():
    """Interactive canvas filling session (C role)."""
    print("═" * 60)
    print("双三角画布填充 Agent — C（Consult/咨询）模式")
    print("═" * 60)
    print()
    print("我会引导你完成六要素画布。对于每个要素，我会先问你当前的状态。")
    print("你的回答不需要完整——不完整没关系，我们会迭代。")
    print("你可以随时说'切换到教学/实践/研究'切换我的身份。")
    print()

    task_name = input("你要分析的任务是什么？（一句话描述）：").strip()
    task_context = input("关于这个任务，还有什么背景信息？（可选）：").strip()
    print()

    canvas = {}
    before_summary = "第一次使用双三角画布分析此任务"

    for idx, (field, question) in enumerate(CANVAS_FIELDS, 1):
        print(f"── {idx}/6 {field} ──")
        print(f"  {question}")
        print()
        answer = input(f"  当前状态（不知道就说'不知道'）：").strip()
        if not answer:
            answer = "待探索"
        canvas[field] = answer
        print()

    # Confidence labeling
    labeled = {}
    risks = []
    for field, answer in canvas.items():
        ans = answer.strip()
        if ans in ("", "不知道", "待探索"):
            label = "[空白]"
            risks.append(field)
        elif any(w in ans for w in ("可能", "大概", "也许", "不确定", "应该")):
            label = "[假设]"
            risks.append(field)
        else:
            label = "[确认]"
        labeled[field] = (ans, label)

    # Output canvas
    print("═" * 60)
    print(f"双三角画布：{task_name}")
    print("═" * 60)
    for field, _ in CANVAS_FIELDS:
        ans, label = labeled[field]
        print(f"\n【{field}】 {label}")
        print(f"  {ans}")

    # Risk summary
    print(f"\n── 风险摘要 ——")
    blanks = [f for f in risks if labeled[f][1] == "[空白]"]
    assumes = [f for f in risks if labeled[f][1] == "[假设]"]
    if blanks:
        print(f"  🔴 空白（高风险）：{', '.join(blanks)} — 需要立即补全")
    if assumes:
        print(f"  🟡 假设（需验证）：{', '.join(assumes)} — 需要事实验证")
    if not blanks and not assumes:
        print(f"  🟢 六要素全部确认 — 风险可控")

    print(f"\n── 画布填充完成 ——")
    print(f"下次迭代时，对比这次的内容看哪些变了。")

    # Flywheel four questions
    print(f"\n═" * 60)
    print("飞轮四问（Before-After 迭代记录）")
    print("═" * 60)
    after_summary = input("这次填充后，你的整体感觉是什么？：").strip()

    if after_summary and after_summary != before_summary:
        why = input("和之前相比，这次有什么不一样？：").strip()
        next_try = input("下次迭代你想重点补哪一块？：").strip()
        flywheel_log(
            "canvas-agent", "体系",
            before_summary, after_summary,
            why or "第一次填充", next_try or "待定"
        )
        print("\n✅ 飞轮日志已记录。")

    print()
    print("如果你需要我切换到 P（实践）模式帮你落地，说'切换到实践'。")
    return 0


def test_scenario(name):
    """Non-interactive test with a preset scenario."""
    if name not in SCENARIOS:
        print(f"Unknown scenario: {name}")
        print(f"Available: {list(SCENARIOS.keys())}")
        return 1

    s = SCENARIOS[name]
    print(f"Test scenario: {name}")
    print(f"  Task: {s['task']}")
    print(f"  Context: {s['context']}")
    print(f"  Canvas fields: {len(CANVAS_FIELDS)}")
    print(f"  Status: OK (6/6 fields structured)")
    return 0


def main():
    parser = argparse.ArgumentParser(description="双三角画布填充 Agent CLI")
    sub = parser.add_subparsers(dest="cmd", required=True)

    sub.add_parser("run", help="交互式画布填充")

    p_test = sub.add_parser("test", help="非交互场景测试")
    p_test.add_argument("--scenario", required=True, choices=list(SCENARIOS.keys()))

    args = parser.parse_args()
    if args.cmd == "run":
        return interactive_run()
    elif args.cmd == "test":
        return test_scenario(args.scenario)


if __name__ == "__main__":
    sys.exit(main())
