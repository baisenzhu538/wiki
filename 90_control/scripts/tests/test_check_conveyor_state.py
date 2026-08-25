"""#519 回归：check-conveyor-state 空转报警（state 年龄 > 2×周期 → exit 1）。

运行：python -m pytest 90_control/scripts/tests/test_check_conveyor_state.py -q
沙盒：monkeypatch 注入临时 STATE_FILE，不碰真实 .kdo/conveyor_state.json。
"""
import importlib.util
import json
import sys
import time
from pathlib import Path

SCRIPT_DIR = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(SCRIPT_DIR))

_SPEC = importlib.util.spec_from_file_location(
    "check_conveyor_state", SCRIPT_DIR / "check-conveyor-state.py"
)
ccs = importlib.util.module_from_spec(_SPEC)
_SPEC.loader.exec_module(ccs)


def _write_state(tmp_path, monkeypatch, last_run_ts):
    sf = tmp_path / "conveyor_state.json"
    sf.write_text(json.dumps({"last_run_ts": last_run_ts}), encoding="utf-8")
    monkeypatch.setattr(ccs, "STATE_FILE", sf)
    return sf


def test_fresh_state_ok(tmp_path, monkeypatch):
    _write_state(tmp_path, monkeypatch, time.time() - 60)  # 1 分钟前
    assert ccs.main() == 0


def test_stale_state_alerts(tmp_path, monkeypatch):
    _write_state(tmp_path, monkeypatch, time.time() - 21 * 60)  # 21 分钟前 > 20 阈值
    assert ccs.main() == 1


def test_missing_state_file_alerts(tmp_path, monkeypatch):
    monkeypatch.setattr(ccs, "STATE_FILE", tmp_path / "nope.json")
    assert ccs.main() == 1


def test_missing_timestamp_field_alerts(tmp_path, monkeypatch):
    sf = tmp_path / "conveyor_state.json"
    sf.write_text(json.dumps({"other": 1}), encoding="utf-8")
    monkeypatch.setattr(ccs, "STATE_FILE", sf)
    assert ccs.main() == 1


def test_corrupt_state_alerts(tmp_path, monkeypatch):
    sf = tmp_path / "conveyor_state.json"
    sf.write_text("{not json", encoding="utf-8")
    monkeypatch.setattr(ccs, "STATE_FILE", sf)
    assert ccs.main() == 1
