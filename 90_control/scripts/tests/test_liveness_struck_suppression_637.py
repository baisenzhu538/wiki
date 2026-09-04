"""#637 回归之二：check_liveness「已登记且已划销 → 不再重复自报」。

背景：#635 F-074（有单才报）+#562（2h 冷却）落地后，持续死亡的角色每 2h 冷却到期
仍重复自报，王语嫣划销处置过的事件照发不误（09-04 全天 20 条实证）。修法：
告警前查板面——该角色 liveness 死况已有划销行（处置过）且持续未恢复 → 抑制；
恢复后 state 清零重新武装，再死必报（防过度收敛）。

运行：python -m pytest 90_control/scripts/tests/test_liveness_struck_suppression_637.py -q
"""
import sys
import time
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
sys.path.insert(0, str(Path(__file__).resolve().parent.parent.parent.parent / "kdo-tools"))

import conveyor_probe as cp
import role_registry as rr


def _wire(tmp_path, monkeypatch, queue_text: str):
    reg = tmp_path / "role-registry.json"
    monkeypatch.setattr(rr, "REGISTRY", reg)
    monkeypatch.setattr(rr, "GATE_BLOCKED_LOG", tmp_path / "gate-blocked.log")
    monkeypatch.setattr(rr, "ALERT_STATE", tmp_path / "alert-state.json")
    queue = tmp_path / "production-queue.md"
    queue.write_text(queue_text, encoding="utf-8")
    monkeypatch.setattr(rr, "QUEUE_FILE", queue)
    return reg


def _queue_text(busy_role="ouyangfeng", struck_role=None):
    lines = ["|:---:|:---|:---|:---:|:---|",
             f"| 1 | task_test_1 | 测试 | queued | {busy_role} |",
             "", cp.PROPOSAL_BEGIN]
    if struck_role:
        lines.append(f"- ~~[gate-blocked] role-liveness｜09-04 10:00｜待王语嫣复核处置｜"
                     f"2026-09-04 09:00:00｜role-liveness｜{struck_role} 全实例疑似死亡"
                     f"（stale: x）｜role_registry check-liveness｜role_registry~~ → 划销（王语嫣）")
    lines.append(cp.PROPOSAL_END)
    return "\n".join(lines) + "\n"


def test_first_death_alerts(tmp_path, monkeypatch):
    """有单角色全死、从未报过 → 必报（防过度收敛：首报不压）。"""
    reg = _wire(tmp_path, monkeypatch, _queue_text())
    rr.heartbeat("ouyangfeng", "kimi-cli", now=1000.0)  # 久远心跳=全死
    alerts = rr.check_liveness(now=1000.0 + 3 * 3600)
    assert "ouyangfeng" in alerts


def test_struck_after_alert_suppressed(tmp_path, monkeypatch):
    """已报过（state 在）+ 板面已划销 + 冷却已过 → 抑制（处置过不重复打扰）。"""
    reg = _wire(tmp_path, monkeypatch, _queue_text(struck_role="ouyangfeng"))
    rr.heartbeat("ouyangfeng", "kimi-cli", now=1000.0)
    t1 = 1000.0 + 3 * 3600
    assert "ouyangfeng" in rr.check_liveness(now=t1)  # 首报
    # 冷却过后（2h+）仍死、但已划销 → 抑制
    assert rr.check_liveness(now=t1 + 3 * 3600) == []


def test_not_struck_cooldown_realerts(tmp_path, monkeypatch):
    """已报过但未划销（未处置）→ 冷却到期照报（#562 压频不删报语义保留）。"""
    reg = _wire(tmp_path, monkeypatch, _queue_text())  # 板面无划销行
    rr.heartbeat("ouyangfeng", "kimi-cli", now=1000.0)
    t1 = 1000.0 + 3 * 3600
    assert "ouyangfeng" in rr.check_liveness(now=t1)
    assert "ouyangfeng" in rr.check_liveness(now=t1 + 3 * 3600)  # 冷却到期重报


def test_recovery_rearms_then_redeath_alerts(tmp_path, monkeypatch):
    """恢复 → state 清零重新武装 → 再死必报（划销历史不误压新死况）。"""
    reg = _wire(tmp_path, monkeypatch, _queue_text(struck_role="ouyangfeng"))
    rr.heartbeat("ouyangfeng", "kimi-cli", now=1000.0)
    t1 = 1000.0 + 3 * 3600
    rr.check_liveness(now=t1)  # 首报
    rr.heartbeat("ouyangfeng", "kimi-cli", now=t1 + 100)  # 恢复
    rr.check_liveness(now=t1 + 200)  # 有活口 → state 清零
    # 再死（心跳又过期），历史划销行仍在板面 —— 但 state 已清零 = 新死况 → 必报
    alerts = rr.check_liveness(now=t1 + 100 + 3 * 3600)
    assert "ouyangfeng" in alerts


def test_not_busy_silence_intact(tmp_path, monkeypatch):
    """F-074 语义不回归：无单角色全死 → 静默（不写 gate-blocked）。"""
    _wire(tmp_path, monkeypatch, _queue_text(busy_role="laowantong"))  # ouyangfeng 无单
    rr.heartbeat("ouyangfeng", "kimi-cli", now=1000.0)
    alerts = rr.check_liveness(now=1000.0 + 3 * 3600)
    assert "ouyangfeng" not in alerts
