#!/usr/bin/env python3
"""agent-activity-check.py — 停滞诊断三问一脚本（E035 工具化，#374）。

输入 agent 名，输出三段证据：
1. 进程态：该 agent 相关进程（gateway/CLI/MCP server）CPU 时间增量（5s 采样两次）
2. 文件活动：全工作面（wiki 全库含 .kdo/.agent + agent复盘）最近 N 分钟文件 mtime 清单（按目录分组）
3. 队列态：claimed 任务 + claim 时长（对比任务类型参考基线）

用法：
    python kdo-tools/agent-activity-check.py <agent> [--minutes 30] [--json]

只读诊断，不动任何状态。判定建议（活跃/疑似停滞/停滞）仅供参考，人下结论。
"""

import argparse
import json
import subprocess
import sys
import time
from datetime import datetime, timezone
from pathlib import Path

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")

WIKI = Path(r"C:\Users\Administrator\Desktop\wiki")
REVIEW_DIR = WIKI.parent / "agent复盘"
PROFILES_DIR = Path(r"C:\Users\Administrator\AppData\Local\hermes\profiles")


def _now_epoch() -> float:
    return time.time()


def _ps(cmd: list[str]) -> str:
    try:
        return subprocess.run(cmd, capture_output=True, text=True, timeout=30).stdout
    except Exception:
        return ""


def query_processes(agent: str) -> list[dict]:
    """Windows: 匹配 agent 相关进程（profile 目录名或 gateway 服务名）。"""
    out = _ps(["powershell", "-NoProfile", "-Command",
               "Get-CimInstance Win32_Process | Where-Object { $_.Name -match 'python|node' } | "
               "ForEach-Object { $_.ProcessId.ToString() + '|' + $_.CreationDate.ToString('yyyy-MM-dd HH:mm:ss') + '|' + ($_.CommandLine -replace '\\|',' ' -replace \"`n\",' ') }"])
    procs = []
    self_pid = str(0)
    for line in out.splitlines():
        parts = line.strip().split("|", 2)
        if len(parts) != 3:
            continue
        pid, created, cmdline = parts
        if "agent-activity-check" in cmdline:
            continue  # 排除本脚本自身
        low = cmdline.lower()
        if (f"hermes-gateway-{agent}" in low or f"-p {agent}" in low
                or f"--profile {agent}" in low or f"profiles\\{agent}" in low
                or f"profiles/{agent}" in low):
            procs.append({"pid": pid, "created": created, "cmd": cmdline[:100]})
    return procs


def cpu_delta(pid: str, interval: float = 5.0) -> float | None:
    """两次采样 CPU 时间增量（秒）。"""
    try:
        t1 = float(_ps(["powershell", "-NoProfile", "-Command",
                        f"(Get-Process -Id {pid} -ErrorAction SilentlyContinue).CPU"]).strip() or 0)
        time.sleep(interval)
        t2 = float(_ps(["powershell", "-NoProfile", "-Command",
                        f"(Get-Process -Id {pid} -ErrorAction SilentlyContinue).CPU"]).strip() or 0)
        return t2 - t1
    except Exception:
        return None


def file_activity(agent: str, minutes: int) -> dict[str, list[str]]:
    """全工作面最近 N 分钟 mtime 文件，按目录分组。"""
    cutoff = _now_epoch() - minutes * 60
    roots = [WIKI, REVIEW_DIR / agent]
    groups: dict[str, list[str]] = {}
    for root in roots:
        if not root.exists():
            continue
        for p in root.rglob("*"):
            if p.is_file():
                try:
                    if ".git" in p.parts:
                        continue  # git 内部噪声排除
                    if p.stat().st_mtime >= cutoff:
                        rel = str(p.relative_to(root))
                        dirname = str(p.parent.relative_to(root)) or "."
                        groups.setdefault(dirname, []).append(p.name)
                except (OSError, ValueError):
                    continue
    return groups


def queue_claimed(agent: str) -> list[dict]:
    """队列中该 agent 的 claimed 任务 + claim 时长（分钟）。"""
    import yaml
    queue = WIKI / "70_product" / "tasks" / "production-queue.md"
    rows = []
    in_table = False
    for line in queue.read_text(encoding="utf-8", errors="replace").splitlines():
        if line.strip().startswith("|:---"):
            in_table = True
            continue
        if not in_table or not line.startswith("|"):
            if in_table and not line.startswith("|"):
                break
            continue
        cells = [c.strip().strip("`").strip() for c in line.strip("|").split("|")]
        if len(cells) < 6:
            continue
        rows.append(cells)

    result = []
    for cells in rows:
        status = cells[3]
        if status.startswith(f"claimed-{agent}"):
            task_id = cells[1]
            tf = WIKI / "60_feedback" / "tasks" / f"{task_id}.md"
            claimed_since = None
            if tf.exists():
                txt = tf.read_text(encoding="utf-8", errors="replace")
                fm = txt[txt.find("---") + 3: txt.find("---", 4)]
                try:
                    fm_d = yaml.safe_load(fm) or {}
                    claimed_since = fm_d.get("updated_at") or fm_d.get("claimed_at")
                except Exception:
                    pass
            age_min = None
            if claimed_since:
                try:
                    t = datetime.fromisoformat(str(claimed_since).replace("Z", "+00:00"))
                    age_min = round((datetime.now(timezone.utc) - t).total_seconds() / 60)
                except Exception:
                    pass
            result.append({"task": task_id, "status": status, "claimed_min": age_min})
    return result


def main():
    parser = argparse.ArgumentParser(description="agent 停滞诊断三问（E035 工具化）")
    parser.add_argument("agent", help="agent 名（如 huangyaoshi）")
    parser.add_argument("--minutes", type=int, default=30, help="文件活动窗口（默认 30）")
    parser.add_argument("--json", action="store_true")
    args = parser.parse_args()
    agent = args.agent.lower()

    # 1. 进程态
    procs = query_processes(agent)
    proc_rows = []
    for p in procs:
        delta = cpu_delta(p["pid"])
        proc_rows.append({"pid": p["pid"], "created": p["created"], "cpu_delta_5s": delta, "cmd": p["cmd"]})

    # 2. 文件活动
    activity = file_activity(agent, args.minutes)
    total_files = sum(len(v) for v in activity.values())

    # 3. 队列态
    claimed = queue_claimed(agent)

    # 判定建议
    hints = []
    if proc_rows:
        busy = any((r["cpu_delta_5s"] or 0) > 0.01 for r in proc_rows)
        hints.append("进程 CPU 增量" + ("活跃" if busy else "疑似无 CPU 活动"))
    if total_files > 0:
        hints.append(f"最近 {args.minutes} 分钟 {total_files} 个文件变更（活跃）")
    else:
        hints.append(f"最近 {args.minutes} 分钟无文件变更")
    if claimed:
        for c in claimed:
            if c["claimed_min"] and c["claimed_min"] > 30:
                hints.append(f"{c['task']} claim {c['claimed_min']} 分钟——基建类 30min 内静默正常，超时需人工判断")
    if total_files == 0 and not any((r["cpu_delta_5s"] or 0) > 0.01 for r in proc_rows):
        verdict = "疑似停滞"
    elif total_files > 0:
        verdict = "活跃"
    else:
        verdict = "无法判定（无进程匹配时需人工查证）"

    report = {"agent": agent, "processes": proc_rows, "file_activity": activity,
              "file_count": total_files, "claimed": claimed, "verdict": verdict, "hints": hints}

    if args.json:
        print(json.dumps(report, ensure_ascii=False, indent=1))
    else:
        print(f"=== agent: {agent} ===")
        print("[1] 进程态:")
        for r in proc_rows:
            d = r["cpu_delta_5s"]
            d_str = f"{d:.3f}s" if d is not None else "n/a"
            print(f"  PID {r['pid']} (since {r['created']}) cpu/5s={d_str}  {r['cmd'][:60]}")
        if not proc_rows:
            print("  无匹配进程（agent 可能未运行或 profile 名不同）")
        print("[2] 文件活动 (最近 %d 分钟):" % args.minutes)
        for d, files in sorted(activity.items()):
            print(f"  {d or '.'}: {', '.join(files[:8])}{' …' if len(files) > 8 else ''}")
        print(f"  共 {total_files} 个文件")
        print("[3] 队列态:")
        for c in claimed:
            age = f"{c['claimed_min']} 分钟" if c["claimed_min"] is not None else "未知"
            print(f"  {c['task']} [{c['status']}] claim {age}")
        if not claimed:
            print("  无 claimed 任务")
        print(f"判定建议: {verdict}")
        for h in hints:
            print(f"  - {h}")


if __name__ == "__main__":
    main()
