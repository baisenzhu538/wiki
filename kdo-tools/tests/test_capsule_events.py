"""#511 回归：胶囊事件层 4 类事件（queue_transition/decision/friction/error）。

运行：python -m pytest kdo-tools/tests/test_capsule_events.py -q
隔离：memory_capsule.A_DB 注入临时库，不碰真实事件库。
"""
import importlib.util
import sqlite3
import sys
from pathlib import Path

KDO_TOOLS = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(KDO_TOOLS))
sys.path.insert(0, str(KDO_TOOLS.parent / "90_control" / "scripts"))

import memory_capsule as mc


def _tmp_db(tmp_path, monkeypatch):
    db = tmp_path / "activity_log.db"
    monkeypatch.setattr(mc, "A_DIR", tmp_path)
    monkeypatch.setattr(mc, "A_DB", db)
    mc.cmd_init()
    return db


def _events(db):
    con = sqlite3.connect(str(db))
    rows = con.execute("SELECT agent_id, event_type, payload_summary FROM activity_log").fetchall()
    con.close()
    return rows


def test_log_event_safe_writes_row(tmp_path, monkeypatch):
    """成功路径：事件落库，返回 True。"""
    db = _tmp_db(tmp_path, monkeypatch)
    assert mc.log_event_safe("huangyaoshi", "decision", "task=#1;verdict=pass")
    rows = _events(db)
    assert rows == [("huangyaoshi", "decision", "task=#1;verdict=pass")]


def test_log_event_safe_failure_visible_not_silent(tmp_path, monkeypatch):
    """失败可见不静默：写入面永久故障（非属性可自愈）→ 返回 False + 不抛异常（不阻断主流程）。
    #545：只读属性场景已升级为自愈（见下一条）；本例用 monkeypatch 模拟持续失败。"""
    db = _tmp_db(tmp_path, monkeypatch)
    def _always_fail(*a, **kw):
        raise sqlite3.OperationalError("attempt to write a readonly database")
    monkeypatch.setattr(mc, "_insert_event", _always_fail)
    monkeypatch.setattr(mc.time, "sleep", lambda *_: None)  # 测试不等退避
    monkeypatch.setattr(mc, "_pending_log", lambda *_: None)  # 不污染真实待收口日志
    ok = mc.log_event_safe("huangyaoshi", "error", "x")
    assert ok is False


def test_log_event_safe_readonly_attr_self_heals(tmp_path, monkeypatch):
    """#545 主回归：db 文件被置只读属性 → 自动清属性 + 重试写入成功（08-26 14 次复发的场景）。"""
    db = _tmp_db(tmp_path, monkeypatch)
    db.chmod(0o444)  # 外部因素置只读（复现 "attempt to write a readonly database"）
    monkeypatch.setattr(mc.time, "sleep", lambda *_: None)
    monkeypatch.setattr(mc, "_pending_log", lambda *_: None)  # 不污染真实待收口日志
    try:
        ok = mc.log_event_safe("huangyaoshi", "error", "gate-blocked;task=t1")
    finally:
        db.chmod(0o644)  # 清理，防 tmp 目录删除失败
    assert ok is True
    rows = _events(db)
    assert rows == [("huangyaoshi", "error", "gate-blocked;task=t1")]
    assert db.stat().st_mode & 0o200  # 只读属性已被清除


def test_log_event_safe_transient_lock_retry(tmp_path, monkeypatch):
    """#545：瞬时失败（锁/占用）→ 退避重试一次后成功。"""
    db = _tmp_db(tmp_path, monkeypatch)
    calls = {"n": 0}
    real_insert = mc._insert_event
    def _flaky(*a, **kw):
        calls["n"] += 1
        if calls["n"] == 1:
            raise sqlite3.OperationalError("database is locked")
        return real_insert(*a, **kw)
    monkeypatch.setattr(mc, "_insert_event", _flaky)
    monkeypatch.setattr(mc.time, "sleep", lambda *_: None)
    ok = mc.log_event_safe("huangyaoshi", "friction", "f1")
    assert ok is True and calls["n"] == 2


def test_transition_hook_writes_queue_and_decision_events(tmp_path, monkeypatch):
    """queue_transition 主钩：claim/complete → queue_transition 事件；review → +decision 事件。"""
    import queue_transition as qt
    db = _tmp_db(tmp_path, monkeypatch)
    # 直接调 _capsule_event 等价路径（钩子在 main()，此处验证写入面行为）
    qt._capsule_event("huangyaoshi", "queue_transition", "task=t1;action=claim;actor=huangyaoshi")
    qt._capsule_event("ouyangfeng", "decision", "task=t1;verdict=pass;grade=A;reviewer=ouyangfeng")
    rows = _events(db)
    types = [r[1] for r in rows]
    assert "queue_transition" in types and "decision" in types


def test_gate_blocked_writes_error_event(tmp_path, monkeypatch):
    """error 事件：真实任务 gate-blocked → 写胶囊；task_9999_ 测试件 → 不写（#483 分流纪律）。"""
    import queue_transition as qt
    db = _tmp_db(tmp_path, monkeypatch)
    monkeypatch.setattr(qt, "GATE_BLOCKED_LOG", tmp_path / "gb.log")
    monkeypatch.setattr(qt, "GATE_BLOCKED_TEST_LOG", tmp_path / "gbt.log")
    qt._log_gate_blocked("task_20260825_real-x", "F-034-五字段", "缺字段", "huangyaoshi")
    qt._log_gate_blocked("task_9999_test", "F-034-五字段", "缺字段")
    rows = _events(db)
    assert len(rows) == 1
    assert rows[0][1] == "error" and "task_20260825_real-x" in rows[0][2]


def test_force_exception_writes_error_event(tmp_path, monkeypatch):
    """error 事件：force 例外台账 → 写胶囊；测试件不写。"""
    import queue_transition as qt
    db = _tmp_db(tmp_path, monkeypatch)
    monkeypatch.setattr(qt, "FORCE_LEDGER", tmp_path / "force.log")
    qt._log_force_exception("task_20260825_real-y", "huangyaoshi", "并行审批", bypass="test")
    qt._log_force_exception("task_9999_force", "huangyaoshi", "x", bypass="test")
    rows = _events(db)
    assert len(rows) == 1 and rows[0][1] == "error" and "force-exception" in rows[0][2]


def test_friction_scan_writes_friction_events(tmp_path, monkeypatch):
    """friction 事件：探针扫描到新 friction 行 → 逐条写胶囊（agent 取行首 [角色]）。"""
    _SPEC = importlib.util.spec_from_file_location("conveyor_probe", KDO_TOOLS / "conveyor_probe.py")
    probe = importlib.util.module_from_spec(_SPEC)
    _SPEC.loader.exec_module(probe)
    db = _tmp_db(tmp_path, monkeypatch)
    monkeypatch.setattr(probe.mc, "A_DIR", tmp_path)
    monkeypatch.setattr(probe.mc, "A_DB", db)
    # 直接验证写入面：friction 行 → log_event_safe（主流程调用点与 #458 同钩）
    ln = "[huangyaoshi] 2026-08-25｜场景｜摩擦内容"
    import re as _re
    m = _re.match(r"^\[([^\]]+)\]", ln)
    assert probe.mc.log_event_safe(m.group(1), "friction", ln[:300])
    rows = _events(db)
    assert rows == [("huangyaoshi", "friction", ln[:300])]
