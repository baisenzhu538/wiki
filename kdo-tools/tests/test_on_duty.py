"""#550 回归：on_duty 在岗判定（时段静默 → 在岗判定，老朱直令）。

验收三用例：有事件流=激活 / 无事件流=静默 / 探针自身事件不计入。
外加：L1 新文件=激活 / 双信号不可得=默认激活 / probe 静默分支统一 defer（不分级）。

运行：python -m pytest kdo-tools/tests/test_on_duty.py -q
"""
import importlib.util
import json
import sqlite3
import time
from datetime import datetime, timedelta, timezone
from pathlib import Path

_SPEC = importlib.util.spec_from_file_location(
    "on_duty", Path(__file__).resolve().parent.parent / "on_duty.py"
)
od = importlib.util.module_from_spec(_SPEC)
_SPEC.loader.exec_module(od)


def _mk_db(tmp_path: Path, events: list[tuple[str, str]]) -> Path:
    """events: [(ts_iso_utc, event_type)]"""
    db = tmp_path / "activity_log.db"
    conn = sqlite3.connect(str(db))
    conn.execute("CREATE TABLE activity_log (id INTEGER PRIMARY KEY AUTOINCREMENT, agent_id TEXT,"
                 " session_id TEXT, ts TEXT, event_type TEXT, payload_summary TEXT, payload_hash TEXT)")
    for ts, et in events:
        conn.execute("INSERT INTO activity_log (agent_id, ts, event_type) VALUES ('a', ?, ?)", (ts, et))
    conn.commit(); conn.close()
    return db


def _iso(dt: datetime) -> str:
    return dt.astimezone(timezone.utc).isoformat()


def test_active_when_recent_events(tmp_path):
    """有事件流=激活：近窗口有真实事件（queue_transition）。"""
    db = _mk_db(tmp_path, [(_iso(datetime.now() - timedelta(minutes=5)), "queue_transition")])
    on, reason = od.any_agent_on_duty(event_db=db, l1_root=tmp_path / "no-l1")
    assert on and "事件库" in reason


def test_silent_when_no_activity(tmp_path):
    """无事件流=静默：事件全在窗口外 + L1 当日目录无新文件。"""
    db = _mk_db(tmp_path, [(_iso(datetime.now() - timedelta(hours=2)), "queue_transition")])
    l1 = tmp_path / "L1"
    day = l1 / datetime.now().strftime("%Y-%m-%d")
    day.mkdir(parents=True)
    old_file = day / "old.jsonl"
    old_file.write_text("x", encoding="utf-8")
    old_ts = time.time() - 3600
    import os
    os.utime(old_file, (old_ts, old_ts))
    on, reason = od.any_agent_on_duty(event_db=db, l1_root=l1)
    assert not on


def test_probe_own_events_not_counted(tmp_path):
    """探针自身事件不计入：近窗口只有 friction（探针镜像写入）→ 仍静默。"""
    db = _mk_db(tmp_path, [(_iso(datetime.now() - timedelta(minutes=2)), "friction")])
    on, _ = od.any_agent_on_duty(event_db=db, l1_root=tmp_path / "no-l1")
    assert not on


def test_l1_fresh_file_marks_active(tmp_path):
    """事件库无新事件但 L1 当日目录有新文件 → 在岗。"""
    db = _mk_db(tmp_path, [])
    l1 = tmp_path / "L1"
    day = l1 / datetime.now().strftime("%Y-%m-%d")
    day.mkdir(parents=True)
    (day / "fresh.jsonl").write_text("x", encoding="utf-8")
    on, reason = od.any_agent_on_duty(event_db=db, l1_root=l1)
    assert on and "L1" in reason


def test_default_active_when_signals_unreadable(tmp_path):
    """双信号不可得（库不存在+L1 不存在）→ 默认激活（静默是例外不是默认）。"""
    on, reason = od.any_agent_on_duty(event_db=tmp_path / "no.db", l1_root=tmp_path / "no-l1")
    assert on and "默认激活" in reason


# ── probe 侧：静默分支统一 defer（豁免分级已废）──

def test_probe_silent_branch_defers_all_uniformly(tmp_path, monkeypatch):
    """无在岗时所有角色消息全 defer——不再有 exempt 分级（#550 任务 3）。"""
    import io
    spec = importlib.util.spec_from_file_location(
        "conveyor_probe", Path(__file__).resolve().parent.parent / "conveyor_probe.py"
    )
    probe = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(probe)
    # 静默分支不再读任何 exempt 集合：直接静态断言源码无残留
    src = (Path(__file__).resolve().parent.parent / "conveyor_probe.py").read_text(encoding="utf-8")
    assert "_split_silent_exempt" not in src
    assert "exempt_roles" not in src
