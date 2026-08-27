"""#556 daily-audit-digest ⑤「待你拍板」栏测试：读 conveyor state 在列集合（只消费不检出）。

运行：python -m pytest kdo-tools/tests/test_daily_audit_digest.py -q
"""
import importlib.util
import json
from pathlib import Path

_SPEC = importlib.util.spec_from_file_location(
    "daily_audit_digest", Path(__file__).resolve().parent.parent / "daily-audit-digest.py"
)
digest = importlib.util.module_from_spec(_SPEC)
_SPEC.loader.exec_module(digest)


def test_pending_decisions_lists_items(tmp_path, monkeypatch):
    st = tmp_path / "conveyor_state.json"
    st.write_text(json.dumps({"pending_decisions": {
        "task_20260827_a-decide": {"seq": "556", "source": "终审记录节", "since": "2026-08-27 10:00"},
    }}, ensure_ascii=False), encoding="utf-8")
    monkeypatch.setattr(digest, "CONVEYOR_STATE", st)
    lines = digest._pending_decisions()
    assert len(lines) == 1
    assert "#556" in lines[0] and "task_20260827_a-decide" in lines[0] and "终审记录节" in lines[0]


def test_pending_decisions_empty_when_none(tmp_path, monkeypatch):
    st = tmp_path / "conveyor_state.json"
    st.write_text(json.dumps({"pending_decisions": {}}), encoding="utf-8")
    monkeypatch.setattr(digest, "CONVEYOR_STATE", st)
    assert digest._pending_decisions() == []


def test_pending_decisions_state_missing_visible(tmp_path, monkeypatch):
    """state 文件缺失不静默——可见提示行（失败可见纪律）。"""
    monkeypatch.setattr(digest, "CONVEYOR_STATE", tmp_path / "none.json")
    lines = digest._pending_decisions()
    assert len(lines) == 1 and "不存在" in lines[0]
