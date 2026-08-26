"""#547 回归：conveyor_probe 第九信号——基建运行态停拍报警。

用例：停拍告警触发 / 新鲜节拍不报警 / 幂等（持续停拍不重复报，恢复后再次停拍可重报）
/ l1-size.log 末行时间戳口径 / 文件不存在告警一次 / 读不出不误报（红线 4）。

运行：python -m pytest kdo-tools/tests/test_infra_liveness.py -q
"""
import importlib.util
import os
import time
from datetime import datetime, timedelta
from pathlib import Path

_SPEC = importlib.util.spec_from_file_location(
    "conveyor_probe", Path(__file__).resolve().parent.parent / "conveyor_probe.py"
)
probe = importlib.util.module_from_spec(_SPEC)
_SPEC.loader.exec_module(probe)


def _wire(tmp_path, monkeypatch):
    """把三个节拍文件指到 tmp。"""
    size_log = tmp_path / "l1-size.log"
    conv = tmp_path / "conveyor_state.json"
    inbox = tmp_path / "inbox_state.json"
    monkeypatch.setattr(probe, "INFRA_BEATS", [
        ("l1-capture", size_log, 60),
        ("conveyor-probe", conv, 20),
        ("inbox-watch", inbox, 20),
    ])
    return size_log, conv, inbox


def _fresh(path: Path, minutes: int = 0):
    path.write_text("{}", encoding="utf-8")
    ts = time.time() - minutes * 60
    os.utime(path, (ts, ts))


def test_fresh_beats_no_alert(tmp_path, monkeypatch):
    size_log, conv, inbox = _wire(tmp_path, monkeypatch)
    size_log.write_text(f"{datetime.now():%Y-%m-%d %H:%M:%S} | L1-full 320 MB\n", encoding="utf-8")
    _fresh(conv); _fresh(inbox)
    state = {}
    assert probe._scan_infra_liveness(state) == []
    assert state["infra_stale"] == []


def test_stale_beats_alert_once(tmp_path, monkeypatch):
    """停拍 >2×周期 → 报警一次；同状态再扫不重复（幂等跨越沿）。"""
    size_log, conv, inbox = _wire(tmp_path, monkeypatch)
    old = (datetime.now() - timedelta(minutes=90)).strftime("%Y-%m-%d %H:%M:%S")
    size_log.write_text(f"{old} | L1-full 320 MB\n", encoding="utf-8")
    _fresh(conv); _fresh(inbox, minutes=45)
    state = {}
    alerts = probe._scan_infra_liveness(state)
    assert len(alerts) == 2
    assert any("l1-capture" in a and "停拍" in a for a in alerts)
    assert any("inbox-watch" in a for a in alerts)
    # 幂等：同状态重扫 → 零新告警
    assert probe._scan_infra_liveness(state) == []
    # 恢复后再次停拍 → 可重报
    _fresh(inbox)
    probe._scan_infra_liveness(state)
    _fresh(inbox, minutes=45)
    alerts2 = probe._scan_infra_liveness(state)
    assert any("inbox-watch" in a for a in alerts2)


def test_missing_file_alerts(tmp_path, monkeypatch):
    _wire(tmp_path, monkeypatch)
    state = {}
    alerts = probe._scan_infra_liveness(state)
    assert len(alerts) == 3
    assert all("文件不存在" in a for a in alerts)
    assert probe._scan_infra_liveness(state) == []  # 幂等


def test_l1_size_log_uses_last_line_timestamp(tmp_path, monkeypatch):
    """l1-capture 口径：读末行时间戳而非 mtime（补采回填场景 mtime 会骗人）。"""
    size_log, conv, inbox = _wire(tmp_path, monkeypatch)
    _fresh(conv); _fresh(inbox)
    old = (datetime.now() - timedelta(minutes=120)).strftime("%Y-%m-%d %H:%M:%S")
    new = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    size_log.write_text(f"{old} | L1-full 100 MB\n{new} | L1-full 101 MB\n", encoding="utf-8")
    state = {}
    assert probe._scan_infra_liveness(state) == []  # 末拍新鲜 → 不报


def test_unreadable_file_no_false_alarm(tmp_path, monkeypatch):
    """读不出（如非法时间戳行）→ 不误报（红线 4）。"""
    size_log, conv, inbox = _wire(tmp_path, monkeypatch)
    size_log.write_text("不是时间戳格式\n", encoding="utf-8")
    _fresh(conv); _fresh(inbox)
    state = {}
    alerts = probe._scan_infra_liveness(state)
    assert all("l1-capture" not in a for a in alerts)
