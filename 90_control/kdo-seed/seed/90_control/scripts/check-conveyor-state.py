#!/usr/bin/env python3
"""check-conveyor-state.py — conveyor_probe 空转报警（#519）。

探针每 10 分钟应落一次 state（.kdo/conveyor_state.json last_run_ts）。
state 年龄 > 2×周期（20 分钟）= 连续空转疑似（崩溃/计划任务失效）→ exit 1。

为什么需要它：#519 实证——探针静默 noop 15 小时无人察觉（#501 的「故障窗口
补偿提示」在崩溃路径打不出来，循环依赖）。本检查由 health-check 每日 02:07
带动，不依赖「下一次成功的运行」来报告「之前的运行崩了」。

用法：python 90_control/scripts/check-conveyor-state.py
"""
import json
import sys
import time
from pathlib import Path

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")

VAULT_ROOT = Path(__file__).resolve().parent.parent.parent
STATE_FILE = VAULT_ROOT / ".kdo" / "conveyor_state.json"
PROBE_PERIOD_MIN = 10          # kdo-conveyor-probe 计划任务周期
THRESHOLD_MIN = PROBE_PERIOD_MIN * 2  # 2×周期=20 分钟无落盘即报警


def main() -> int:
    if not STATE_FILE.exists():
        print(f"FAIL: conveyor state 不存在（{STATE_FILE}）——探针从未成功落盘")
        return 1
    try:
        state = json.loads(STATE_FILE.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as e:
        print(f"FAIL: conveyor state 不可读: {e}")
        return 1
    ts = state.get("last_run_ts")
    if not ts:
        print("FAIL: conveyor state 无 last_run_ts 字段")
        return 1
    age_min = (time.time() - float(ts)) / 60
    if age_min > THRESHOLD_MIN:
        print(f"FAIL: conveyor_probe 疑似空转——state {age_min:.0f} 分钟未更新"
              f"（阈值 {THRESHOLD_MIN} 分钟=2×周期）；查 logs/conveyor-probe.log 与计划任务 kdo-conveyor-probe")
        return 1
    print(f"conveyor_probe state 正常（{age_min:.1f} 分钟前落盘，阈值 {THRESHOLD_MIN} 分钟）")
    return 0


if __name__ == "__main__":
    sys.exit(main())
