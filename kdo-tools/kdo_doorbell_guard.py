#!/usr/bin/env python3
"""kdo_doorbell_guard.py — #565：OS 门铃守卫。会话活着则跳过本次唤醒（防平行工班）。

exit 0 = 放行（该角色本地会话心跳不新鲜，门铃该拍）
exit 1 = 跳过（心跳新鲜=会话活着自己在跑，OS 门铃不抢活）

判定源=90_control/role-registry.json（#552 注册表；#562 起心跳写面=消费回执+
SessionHeartbeat 钩，活跃会话心跳分钟级新鲜）。注册表缺失/解析失败=放行（fail-open
叫不醒比叫重更糟——08-28 五小时聋哑实证）。

用法：kdo-doorbell.cmd 里 `python kdo-tools/kdo_doorbell_guard.py huangyaoshi || exit /b 0`
"""
import json
import sys
import time
from pathlib import Path

REGISTRY = Path(__file__).resolve().parent.parent / "90_control" / "role-registry.json"
FRESH_SEC = 10 * 60  # 心跳 <10min = 会话活着（消费回执/SessionHeartbeat 拍点都远密于此）


def session_alive(role: str, now: float | None = None) -> bool:
    now = now or time.time()
    try:
        reg = json.loads(REGISTRY.read_text(encoding="utf-8"))
    except Exception:
        return False  # fail-open：读不出=当死，放行门铃
    entry = reg.get(role) or {}
    for inst in entry.get("instances", []):
        if inst.get("kind") != "cli":
            continue  # 平台实例（hermes）的活性不能证明本地 CLI 会话活着
        try:
            if now - float(inst.get("heartbeat_ts", 0)) < FRESH_SEC:
                return True
        except (TypeError, ValueError):
            continue
    return False


def main() -> int:
    role = sys.argv[1] if len(sys.argv) > 1 else "huangyaoshi"
    alive = session_alive(role)
    print(f"[doorbell-guard] {role} cli-session {'alive -> skip' if alive else 'stale/dead -> fire'}")
    return 1 if alive else 0


if __name__ == "__main__":
    sys.exit(main())
