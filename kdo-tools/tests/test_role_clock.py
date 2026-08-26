"""#553 回归：role_clock 调度器——到点/事件驱动/三适配器/降级路径。

运行：python -m pytest kdo-tools/tests/test_role_clock.py -q
"""
import importlib.util
import json
import time
from pathlib import Path

_SPEC = importlib.util.spec_from_file_location(
    "role_clock", Path(__file__).resolve().parent.parent / "role_clock.py"
)
rc = importlib.util.module_from_spec(_SPEC)
_SPEC.loader.exec_module(rc)


def _wire(tmp_path, monkeypatch, registry: dict):
    reg = tmp_path / "role-registry.json"
    reg.write_text(json.dumps(registry), encoding="utf-8")
    monkeypatch.setattr(rc, "REGISTRY", reg)
    monkeypatch.setattr(rc, "STATE_FILE", tmp_path / "state.json")
    monkeypatch.setattr(rc, "WAKE_LOG", tmp_path / "wake.log")
    monkeypatch.setattr(rc, "TODOS_DIR", tmp_path / "todos")
    return reg


_REG = {"huangyaoshi": {"active": "cli", "instances": [{"tool": "cli", "channels": ["todos"]}]},
        "ouyangfeng": {"active": "cli", "instances": [{"tool": "cli", "channels": ["todos"]}]}}


def test_pace_due_and_not_due(tmp_path, monkeypatch):
    """到点判定：huangyaoshi 节奏 15min——超期到期、期内不到期。"""
    _wire(tmp_path, monkeypatch, _REG)
    now = time.time()
    due = rc.due_roles(now=now, state={"last_wake": {"huangyaoshi": now - 20 * 60}})
    assert any(r == "huangyaoshi" for r, _ in due)
    due2 = rc.due_roles(now=now, state={"last_wake": {"huangyaoshi": now - 5 * 60}})
    assert not any(r == "huangyaoshi" and "到点" in why for r, why in due2)


def test_event_driven_ouyangfeng(tmp_path, monkeypatch):
    """欧阳锋事件驱动：有待终审 → 即醒（防抖最小间隔 10min）；无待终审不到点（30min 期内）。"""
    _wire(tmp_path, monkeypatch, _REG)
    now = time.time()
    monkeypatch.setattr(rc, "_pending_review_exists", lambda: True)
    due = rc.due_roles(now=now, state={"last_wake": {"ouyangfeng": now - 11 * 60,
                                                     "huangyaoshi": now}})
    assert ("ouyangfeng", "事件驱动：有待终审") in due
    # 防抖：10min 内刚醒过 → 不再醒
    due2 = rc.due_roles(now=now, state={"last_wake": {"ouyangfeng": now - 5 * 60,
                                                      "huangyaoshi": now}})
    assert not any(r == "ouyangfeng" for r, _ in due2)
    # 无待终审 → 事件驱动不触发
    monkeypatch.setattr(rc, "_pending_review_exists", lambda: False)
    due3 = rc.due_roles(now=now, state={"last_wake": {"ouyangfeng": now - 11 * 60,
                                                      "huangyaoshi": now}})
    assert not any(r == "ouyangfeng" for r, _ in due3)


def test_wake_writes_todos_and_log(tmp_path, monkeypatch):
    """适配器：todos 恒落盘 + 唤醒日志留痕（统一 payload 文案）。"""
    _wire(tmp_path, monkeypatch, _REG)
    touched = rc.wake("laowantong", "到点（节奏 15min）",
                      {"active": "cli", "instances": [{"tool": "cli", "channels": ["todos"]}]})
    assert touched == ["todos"]
    text = (tmp_path / "todos" / "laowantong.md").read_text(encoding="utf-8")
    assert "【叫醒】laowantong" in text and "读 todos/laowantong.md 未读段" in text
    log = (tmp_path / "wake.log").read_text(encoding="utf-8")
    assert "laowantong" in log and "到点" in log


def test_run_full_cycle(tmp_path, monkeypatch):
    """调度单拍：到期角色唤醒 + state 写回；第二拍不到期不重复唤醒。"""
    _wire(tmp_path, monkeypatch, _REG)
    monkeypatch.setattr(rc, "_pending_review_exists", lambda: False)
    now = time.time()
    rc.run(now=now)
    state = json.loads((tmp_path / "state.json").read_text(encoding="utf-8"))
    assert "huangyaoshi" in state["last_wake"]  # 首拍全到期
    todos = tmp_path / "todos" / "huangyaoshi.md"
    assert todos.exists()
    # 第二拍：无到期 → 不动
    rc.run(now=now + 60)
    assert todos.read_text(encoding="utf-8").count("【叫醒】") == 1


def test_all_dead_still_wakes_and_reports(tmp_path, monkeypatch):
    """红线：active 实例全死 → 照常唤醒（误发>漏发）+ 降级报警走 role_registry 自报（不切执行权）。"""
    _wire(tmp_path, monkeypatch, _REG)
    called = {"n": 0}
    import role_registry as rr
    monkeypatch.setattr(rr, "check_liveness", lambda now=None: called.__setitem__("n", called["n"] + 1) or ["huangyaoshi"])
    monkeypatch.setattr(rr, "liveness", lambda role, now=None, reg=None: {
        "role": role, "alive": [], "stale": [("cli", 999)], "all_dead": True, "registered": True})
    monkeypatch.setattr(rc, "_pending_review_exists", lambda: False)
    rc.run(now=time.time())
    assert called["n"] >= 1  # 降级报警触发
    assert (tmp_path / "todos" / "huangyaoshi.md").exists()  # 唤醒照发
