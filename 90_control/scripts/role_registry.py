#!/usr/bin/env python3
"""role_registry.py — 角色活性注册表（#552，#525 四拆之一）。

设计稿=90_control/role-clock-architecture.md §1（严格按稿施工，不扩设计）。
- 注册表：90_control/role-registry.json（轻 JSON 单文件，不落数据库）
- 写侧：heartbeat（CLI 启动/时钟蹭拍/手工 register）；单角色单实例写自己键，无锁竞争
- 读侧：liveness（heartbeat 年龄 >2×该角色节奏=疑似死亡）；全死 → gate-blocked.log 自报
- 多实例并存：同角色双活=唤醒双发（消费幂等各自去重）；active=最近心跳实例（单执行者防双写）

用法：
  python 90_control/scripts/role_registry.py heartbeat huangyaoshi --tool kimi-cli
  python 90_control/scripts/role_registry.py status            # 全角色活性一览
  python 90_control/scripts/role_registry.py check-liveness    # 全死角色 → gate-blocked 自报
"""
import argparse
import json
import sys
import time
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent.parent
REGISTRY = ROOT / "90_control" / "role-registry.json"
GATE_BLOCKED_LOG = ROOT / "90_control" / "gate-blocked.log"

# 角色唤醒节奏（分钟）——活性判定基准（>2×节奏=疑似死亡）。
# 来源 #555 编排：老顽童 15 / 王语嫣 30 / 黄药师 15 / 风清扬 720（日 2 拍）/ 欧阳锋事件驱动=30 兜底
ROLE_PACE_MIN = {
    "laowantong": 15, "huangyaoshi": 15, "wangyuyan": 30,
    "ouyangfeng": 30, "fengqingyang": 720,
}
DEFAULT_PACE_MIN = 30

# #562 止血：报警冷却——同角色 2h 内不重复自报；恢复（有活口）后清零重新武装。
# 只压频不删报：首次必报、恢复后再死必报。
ALERT_COOLDOWN_SEC = 2 * 3600
ALERT_STATE = ROOT / ".kdo" / "role-liveness-alert-state.json"


def _load_alert_state() -> dict:
    try:
        data = json.loads(ALERT_STATE.read_text(encoding="utf-8"))
        return data if isinstance(data, dict) else {}
    except Exception:
        return {}


def _save_alert_state(state: dict) -> None:
    ALERT_STATE.parent.mkdir(parents=True, exist_ok=True)
    tmp = ALERT_STATE.with_suffix(".tmp")
    tmp.write_text(json.dumps(state, ensure_ascii=False, indent=2), encoding="utf-8")
    tmp.replace(ALERT_STATE)


def _load() -> dict:
    try:
        data = json.loads(REGISTRY.read_text(encoding="utf-8"))
        return data if isinstance(data, dict) else {}
    except Exception:
        return {}


def _save(reg: dict) -> None:
    REGISTRY.parent.mkdir(parents=True, exist_ok=True)
    tmp = REGISTRY.with_suffix(".tmp")
    tmp.write_text(json.dumps(reg, ensure_ascii=False, indent=2), encoding="utf-8")
    tmp.replace(REGISTRY)  # 原子替换防半写


def heartbeat(role: str, tool: str, kind: str = "cli",
              session_scope: str | None = None, profile: str | None = None,
              channels: list[str] | None = None, now: float | None = None) -> dict:
    """写心跳：upsert instances[tool]，active=本实例（最近心跳=当前活跃）。
    返回更新后的角色条目。"""
    now = now or time.time()
    reg = _load()
    entry = reg.setdefault(role, {"instances": [], "active": tool})
    entry["active"] = tool
    inst = None
    for i in entry["instances"]:
        if i.get("tool") == tool:
            inst = i
            break
    if inst is None:
        inst = {"tool": tool, "kind": kind, "channels": channels or ["todos"]}
        entry["instances"].append(inst)
    inst["heartbeat_ts"] = now
    if session_scope:
        inst["session_scope"] = session_scope
    if profile:
        inst["profile"] = profile
    _save(reg)
    return entry


def liveness(role: str, now: float | None = None, reg: dict | None = None) -> dict:
    """单角色活性：{role, alive[], stale[], all_dead}。疑似死亡=heartbeat 年龄 >2×节奏。"""
    now = now or time.time()
    reg = reg if reg is not None else _load()
    entry = reg.get(role)
    if not entry or not entry.get("instances"):
        return {"role": role, "alive": [], "stale": [], "all_dead": False, "registered": False}
    pace = ROLE_PACE_MIN.get(role, DEFAULT_PACE_MIN)
    alive, stale = [], []
    for i in entry["instances"]:
        age_min = (now - float(i.get("heartbeat_ts", 0))) / 60
        (alive if age_min <= 2 * pace else stale).append((i["tool"], round(age_min, 1)))
    return {"role": role, "alive": alive, "stale": stale,
            "all_dead": not alive, "registered": True, "pace_min": pace}


def check_liveness(now: float | None = None) -> list[str]:
    """全角色扫描：已注册但全死 → gate-blocked.log 自报（#471 通道复用，不新造报警器）。
    #562：同角色 2h 冷却（ALERT_STATE 记 last_alert_ts），恢复后清零重新武装。
    返回本次实际新报警的角色列表（冷却抑制的不在内）。"""
    now = now or time.time()
    reg = _load()
    state = _load_alert_state()
    alerts = []
    suppressed = []
    lines = []
    for role in reg:
        lv = liveness(role, now=now, reg=reg)
        if not lv["registered"]:
            continue
        if not lv["all_dead"]:
            state.pop(role, None)  # 恢复 → 清零重新武装
            continue
        if role in state and now - float(state[role]) < ALERT_COOLDOWN_SEC:
            suppressed.append(role)
            continue
        state[role] = now
        line = f"role-liveness｜{role} 全实例疑似死亡（stale: {lv['stale']}）"
        alerts.append(role)
        lines.append(line)
    _save_alert_state(state)
    if lines:
        ts = time.strftime("%Y-%m-%d %H:%M:%S")
        try:
            with GATE_BLOCKED_LOG.open("a", encoding="utf-8") as f:
                for ln in lines:
                    f.write(f"{ts}｜{ln}｜role_registry check-liveness｜role_registry\n")
        except OSError as e:
            print(f"[warn] gate-blocked 台账写入失败: {e}", file=sys.stderr)
    if suppressed:
        print(f"[info] 冷却抑制 {len(suppressed)} 角色（2h 内已报过）: {suppressed}")
    return alerts


def main() -> int:
    p = argparse.ArgumentParser(description="角色活性注册表（#552）")
    sub = p.add_subparsers(dest="cmd", required=True)
    hb = sub.add_parser("heartbeat", help="写心跳（CLI 启动/时钟蹭拍）")
    hb.add_argument("role")
    hb.add_argument("--tool", required=True)
    hb.add_argument("--kind", default="cli")
    hb.add_argument("--session-scope", default=None)
    hb.add_argument("--profile", default=None)
    hb.add_argument("--channels", default=None, help="逗号分隔，默认 todos")
    sub.add_parser("status", help="全角色活性一览")
    sub.add_parser("check-liveness", help="全死角色 → gate-blocked 自报")
    args = p.parse_args()

    if args.cmd == "heartbeat":
        channels = args.channels.split(",") if args.channels else None
        e = heartbeat(args.role, args.tool, args.kind, args.session_scope, args.profile, channels)
        print(f"[ok] 心跳已写: {args.role}/{args.tool}（active={e['active']}，实例 {len(e['instances'])} 个）")
        return 0
    if args.cmd == "status":
        reg = _load()
        if not reg:
            print("注册表为空")
            return 0
        for role in sorted(reg):
            lv = liveness(role, reg=reg)
            print(f"{role}: active={reg[role].get('active')} alive={lv['alive']} stale={lv['stale']}")
        return 0
    if args.cmd == "check-liveness":
        alerts = check_liveness()
        print(f"全死角色 {len(alerts)} 个{f'：{alerts}' if alerts else ''}")
        return 1 if alerts else 0
    return 1


if __name__ == "__main__":
    sys.exit(main())
