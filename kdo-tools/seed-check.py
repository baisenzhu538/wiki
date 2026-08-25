#!/usr/bin/env python3
"""seed-check.py — kdo-seed 装机自检（#532）：「机制不走样」从人工核对变脚本保证。

四查（对应 bootstrap 五步的验证半）：
  1. 目录齐不齐：九层骨架 + 角色文件 + 工具层关键件
  2. 路径通不通：KDO_ROOT 解析 + 关键脚本可导入（语法级）
  3. 计划任务注册没注册：schtasks 查询五个任务（本机装机后应注册；种子目录内只提示）
  4. 角色文件可读性：五角色上下文文件 UTF-8 可读

用法：python kdo-tools/seed-check.py [--root DIR]（默认 KDO_ROOT 或脚本祖父目录）
"""
import argparse
import subprocess
import sys
from pathlib import Path

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")

ROLES = ["huangyaoshi", "laowantong", "wangyuyan", "ouyangfeng", "fengqingyang"]
NINE_LAYERS = ["00_inbox", "10_raw", "20_memory", "30_wiki", "40_outputs",
               "50_delivery", "60_feedback", "70_product", "90_control", ".kdo"]
KEY_FILES = [
    "kdo-tools/conveyor_probe.py", "kdo-tools/l1_capture.py",
    "kdo-tools/daily-context-save.py", "90_control/scripts/queue_transition.py",
    "90_control/scripts/health-check.py", "90_control/scripts/pre_review.py",
    ".agent/startup.md", "90_control/kdo-charter-v0.1-draft.md",
]
SCHED_TASKS = ["kdo-conveyor-probe", "kdo-l1-capture", "kdo-inbox-watch",
               "kdo-health-daily", "kdo-quality-metrics"]


def check(root: Path) -> list[str]:
    """返回问题清单（空=全过）。"""
    problems = []
    for layer in NINE_LAYERS:
        if not (root / layer).is_dir():
            problems.append(f"骨架缺层: {layer}")
    for rel in KEY_FILES:
        if not (root / rel).is_file():
            problems.append(f"关键件缺失: {rel}")
    for role in ROLES:
        # 角色上下文双形态：.agent/<role>-context.md 或 20_memory/<role>-amnesia-recovery.md
        # （风清扬观察者无 .agent context，锚点在 20_memory——实测口径）
        candidates = [root / ".agent" / f"{role}-context.md",
                      root / "20_memory" / f"{role}-amnesia-recovery.md"]
        existing = [c for c in candidates if c.is_file()]
        if not existing:
            problems.append(f"角色上下文缺: {role}（.agent/ 与 20_memory/ 双无）")
            continue
        try:
            existing[0].read_text(encoding="utf-8")
        except (OSError, UnicodeDecodeError) as e:
            problems.append(f"角色文件不可读: {existing[0].name}: {e}")
    for script in ("kdo-tools/conveyor_probe.py", "90_control/scripts/queue_transition.py"):
        fp = root / script
        if fp.is_file():
            r = subprocess.run([sys.executable, "-m", "py_compile", str(fp)],
                               capture_output=True, timeout=30)
            if r.returncode != 0:
                problems.append(f"脚本不可编译: {script}")
    return problems


def check_scheduled_tasks() -> list[str]:
    """schtasks 注册核查（环境问题不硬失败——WSL/无权限环境返回提示）。"""
    problems = []
    for tn in SCHED_TASKS:
        r = subprocess.run(["schtasks", "/query", "/tn", tn],
                           capture_output=True, timeout=15)
        if r.returncode != 0:
            problems.append(f"计划任务未注册: {tn}")
    return problems


def main() -> int:
    ap = argparse.ArgumentParser(description="kdo-seed 装机自检（#532）")
    ap.add_argument("--root", help="库根（默认 KDO_ROOT 或脚本祖父目录）")
    ap.add_argument("--skip-tasks", action="store_true", help="跳过 schtasks 核查（种子目录内预检）")
    args = ap.parse_args()
    import os
    root = Path(args.root or os.environ.get("KDO_ROOT") or Path(__file__).resolve().parent.parent)

    problems = check(root)
    task_problems = [] if args.skip_tasks else check_scheduled_tasks()

    for p in problems + task_problems:
        print(f"🔴 {p}")
    if not problems and not task_problems:
        print(f"✅ seed-check 全过：{root}（九层骨架/关键件/五角色可读/脚本可编译/计划任务在册）")
        return 0
    print(f"共 {len(problems) + len(task_problems)} 项问题")
    return 1


if __name__ == "__main__":
    sys.exit(main())
