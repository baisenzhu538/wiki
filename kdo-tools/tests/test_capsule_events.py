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
    """失败可见不静默：DB 不可写 → 返回 False + 不抛异常（不阻断主流程）。"""
    db = tmp_path / "activity_log.db"
    monkeypatch.setattr(mc, "A_DIR", tmp_path)
    monkeypatch.setattr(mc, "A_DB", db)
    mc.cmd_init()
    db.chmod(0o444)  # 只读 → INSERT 失败
    try:
        ok = mc.log_event_safe("huangyaoshi", "error", "x")
    finally:
        db.chmod(0o644)
    assert ok is False


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
