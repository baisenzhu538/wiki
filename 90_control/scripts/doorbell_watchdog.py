#!/usr/bin/env python3
"""门铃看门狗（系统级，老朱 2026-09-10 拍板「不信纪律信门禁」+ 同意门铃转系统级）。

逻辑：王语嫣交互会话的门铃 cron 是会话级的——会话死则门铃死（E 族教训）。
本看门狗挂系统计划任务，每 10 分钟检查 todos/wangyuyan.md 最后一拍值守拍时间：
- <45min：会话活着，零动作
- ≥45min：门铃死了 → 拉起 headless 王语嫣执行值守序列（拉起器通道预检自带 fallback）
- 拉起后 45min 内不重复拉（防抖）；连续拉起 3 次无新值守拍 → 停拉并 gate-blocked 报警（可能任务/通道有真问题）
"""
import json
import re
import subprocess
import sys
from datetime import datetime, timezone, timedelta
from pathlib import Path

WIKI = Path(r"C:\Users\Administrator\Desktop\wiki")
TODOS = WIKI / "90_control" / "todos" / "wangyuyan.md"
LOG = WIKI / "logs" / "doorbell-watchdog.log"
STATE = WIKI / "90_control" / ".doorbell-watchdog-state.json"
STALE_MIN = 45
MAX_CONSECUTIVE_LAUNCHES = 3

def last_beat_time():
    """todos 里最后一个 🕐 值守拍的时间戳（本地时间）。"""
    if not TODOS.exists():
        return None
    last = None
    for line in TODOS.read_text(encoding="utf-8", errors="replace").splitlines():
        if "🕐 值守拍" in line:
            m = re.search(r"\[(\d{4}-\d{2}-\d{2}) (\d{2}):(\d{2})\]", line)
            if m:
                last = datetime.strptime(f"{m.group(1)} {m.group(2)}:{m.group(3)}", "%Y-%m-%d %H:%M")
    return last

def main():
    now = datetime.now()
    state = json.loads(STATE.read_text(encoding="utf-8")) if STATE.exists() else {"launches": [], "blocked": False}
    ts = last_beat_time()
    if ts is None:
        verdict, stale = "no-beat-found", True
    else:
        stale = (now - ts) > timedelta(minutes=STALE_MIN)
        verdict = f"last={ts:%H:%M} stale={stale}"

    if state.get("blocked"):
        print(f"blocked（连续拉起无新拍，待王语嫣裁定） {verdict}")
        return

    if not stale:
        print(f"ok {verdict}")
        return

    # 防抖：45min 内不重复拉起
    launches = [t for t in state["launches"] if (now - datetime.fromisoformat(t)) < timedelta(minutes=STALE_MIN)]
    if launches:
        print(f"debounce（45min 内已拉过） {verdict}")
        state["launches"] = launches
        STATE.write_text(json.dumps(state, ensure_ascii=False), encoding="utf-8")
        return

    # 连续拉起上限
    recent = [t for t in state["launches"] if (now - datetime.fromisoformat(t)) < timedelta(hours=3)]
    if len(recent) >= MAX_CONSECUTIVE_LAUNCHES:
        state["blocked"] = True
        state["launches"] = recent
        STATE.write_text(json.dumps(state, ensure_ascii=False), encoding="utf-8")
        with open(WIKI / "90_control" / "gate-blocked.log", "a", encoding="utf-8") as f:
            f.write(f"{now:%Y-%m-%d %H:%M:%S}｜doorbell-watchdog｜门铃连续 {MAX_CONSECUTIVE_LAUNCHES} 次拉起无新值守拍，停拉待裁定（{verdict}）｜doorbell_watchdog\n")
        print(f"BLOCKED+报警 {verdict}")
        return

    # 拉起 headless 王语嫣补位
    prompt = ("【系统级门铃兜底】交互会话的门铃疑似死亡（45min 无值守拍）。你执行值守序列："
              "①读 90_control/todos/wangyuyan.md 未读段 ②三扫描面（diagnosis 新建议书/pending-cards/00_inbox 根目录新件）"
              "③queue_transition.py status——pending_review 拉欧阳锋终审，claimed 超 45min 无产出补拉对应角色 "
              "④在 todos/wangyuyan.md 追加一行值守拍（🕐 值守拍HH:MM：系统级兜底拉起+状态一句话）。")
    r = subprocess.run(
        [sys.executable, str(WIKI / "90_control" / "scripts" / "kimi-headless-launch.py"), "wangyuyan", prompt],
        capture_output=True, text=True, timeout=120, cwd=str(WIKI),
    )
    launches.append(now.isoformat())
    state["launches"] = launches
    STATE.write_text(json.dumps(state, ensure_ascii=False), encoding="utf-8")
    with open(LOG, "a", encoding="utf-8") as f:
        f.write(f"{now:%Y-%m-%d %H:%M:%S} stale={verdict} → 拉起 rc={r.returncode} tail={(r.stdout or r.stderr).strip()[-120:]}\n")
    print(f"launched {verdict}")

if __name__ == "__main__":
    main()
