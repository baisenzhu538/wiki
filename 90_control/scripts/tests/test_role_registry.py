"""#552 回归：角色活性注册表 + 心跳写钩 + 活性判定 + 全死自报。

用例：心跳建档/续拍更新/双实例并存+active 切换/活性判定（>2×节奏疑似死亡）/
全死→gate-blocked 自报/未注册不误报。

运行：python -m pytest 90_control/scripts/tests/test_role_registry.py -q
"""
import json
import sys
import time
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

import role_registry as rr


def _wire(tmp_path, monkeypatch):
    reg = tmp_path / "role-registry.json"
    ledger = tmp_path / "gate-blocked.log"
    monkeypatch.setattr(rr, "REGISTRY", reg)
    monkeypatch.setattr(rr, "GATE_BLOCKED_LOG", ledger)
    monkeypatch.setattr(rr, "ALERT_STATE", tmp_path / "alert-state.json")
    return reg, ledger


def test_heartbeat_creates_and_updates(tmp_path, monkeypatch):
    """心跳建档：role/tool/kind/scope/channels 全字段；续拍只更新 heartbeat_ts。"""
    reg, _ = _wire(tmp_path, monkeypatch)
    rr.heartbeat("huangyaoshi", "kimi-cli", session_scope="C:/wiki", now=1000.0)
    rr.heartbeat("huangyaoshi", "kimi-cli", session_scope="C:/wiki", now=2000.0)
    e = json.loads(reg.read_text(encoding="utf-8"))["huangyaoshi"]
    assert len(e["instances"]) == 1
    assert e["instances"][0]["heartbeat_ts"] == 2000.0
    assert e["instances"][0]["session_scope"] == "C:/wiki"
    assert e["active"] == "kimi-cli"


def test_dual_instance_coexist_active_follows_latest(tmp_path, monkeypatch):
    """多实例并存：CLI+飞书双活共列；active 跟随最近心跳（单执行者防双写）。"""
    reg, _ = _wire(tmp_path, monkeypatch)
    rr.heartbeat("ouyangfeng", "kimi-cli", kind="cli", now=1000.0)
    rr.heartbeat("ouyangfeng", "hermes", kind="platform", profile="ouyangfeng", now=2000.0)
    e = json.loads(reg.read_text(encoding="utf-8"))["ouyangfeng"]
    assert len(e["instances"]) == 2  # 双活并存
    assert e["active"] == "hermes"   # 最近心跳=活跃


def test_liveness_stale_beyond_2x_pace(tmp_path, monkeypatch):
    """活性判定：huangyaoshi 节奏 15min → >30min 无心跳=疑似死亡。"""
    _wire(tmp_path, monkeypatch)
    rr.heartbeat("huangyaoshi", "cli", now=1000.0)
    lv = rr.liveness("huangyaoshi", now=1000.0 + 20 * 60)
    assert lv["alive"] and not lv["all_dead"]
    lv2 = rr.liveness("huangyaoshi", now=1000.0 + 40 * 60)
    assert lv2["all_dead"] and lv2["stale"]


def test_liveness_unregistered_not_dead(tmp_path, monkeypatch):
    """未注册角色不算「全死」（没上岗≠死亡）。"""
    _wire(tmp_path, monkeypatch)
    lv = rr.liveness("nobody", now=time.time())
    assert not lv["registered"] and not lv["all_dead"]


def test_check_liveness_reports_all_dead(tmp_path, monkeypatch):
    """全死 → gate-blocked.log 自报（#471 通道复用）；有活口不报。"""
    _, ledger = _wire(tmp_path, monkeypatch)
    rr.heartbeat("huangyaoshi", "cli", now=1000.0)          # 将死
    rr.heartbeat("wangyuyan", "cli", now=time.time())        # 活着
    alerts = rr.check_liveness(now=1000.0 + 60 * 60)
    assert alerts == ["huangyaoshi"]
    text = ledger.read_text(encoding="utf-8")
    assert "role-liveness" in text and "huangyaoshi" in text
    assert "wangyuyan" not in text


def test_check_liveness_cooldown_suppresses_repeat(tmp_path, monkeypatch):
    """#562：同角色 2h 冷却——连跑 3 拍仅首拍报警；恢复清零后再死重新报警。"""
    _, ledger = _wire(tmp_path, monkeypatch)
    t0 = 1000.0
    rr.heartbeat("huangyaoshi", "cli", now=t0)
    dead = t0 + 60 * 60
    a1 = rr.check_liveness(now=dead)                 # 首报
    a2 = rr.check_liveness(now=dead + 5 * 60)        # 5min 后：冷却抑制
    a3 = rr.check_liveness(now=dead + 30 * 60)       # 30min 后：仍抑制
    assert a1 == ["huangyaoshi"] and a2 == [] and a3 == []
    text = ledger.read_text(encoding="utf-8")
    assert text.count("role-liveness") == 1
    # 冷却期过后再报
    a4 = rr.check_liveness(now=dead + 3 * 3600)
    assert a4 == ["huangyaoshi"]
    assert ledger.read_text(encoding="utf-8").count("role-liveness") == 2
    # 恢复 → 清零重新武装：再死立即报不等冷却
    rr.heartbeat("huangyaoshi", "cli", now=dead + 4 * 3600)
    assert rr.check_liveness(now=dead + 4 * 3600) == []       # 活着不报
    a5 = rr.check_liveness(now=dead + 5 * 3600)               # 又死 → 立即报
    assert a5 == ["huangyaoshi"]
    assert ledger.read_text(encoding="utf-8").count("role-liveness") == 3
