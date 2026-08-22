"""#421 传送带探针测试：三元组检出 / PROPOSAL-PENDING 登记幂等 / 历史行保留 / 边界（无流转能力）/ 通知 dry-run。

运行：python -m pytest kdo-tools/tests/test_conveyor_probe.py -q
"""
import importlib.util
import sys
from pathlib import Path

_SPEC = importlib.util.spec_from_file_location(
    "conveyor_probe", Path(__file__).resolve().parent.parent / "conveyor_probe.py"
)
probe = importlib.util.module_from_spec(_SPEC)
_SPEC.loader.exec_module(probe)

TRIPLET = """---
id: diag_test-1
title: 测试建议书
type: proposal
status: pending_orchestration
audience: 王语嫣
---

测试。
"""


def _write_triplet(dir_: Path, name: str) -> Path:
    fp = dir_ / name
    fp.write_text(TRIPLET, encoding="utf-8")
    return fp


def test_scan_proposals_detects_triplet(tmp_path, monkeypatch):
    monkeypatch.setattr(probe, "DIAG_DIR", tmp_path)
    _write_triplet(tmp_path, "diag_20260822_test-a.md")
    (tmp_path / "diag_20260822_not-proposal.md").write_text(
        "---\nid: x\ntitle: y\nstatus: reviewed\n---\n", encoding="utf-8"
    )
    hits = probe._scan_proposals()
    assert hits == ["diag_20260822_test-a.md"]


def test_update_board_idempotent(tmp_path, monkeypatch):
    queue = tmp_path / "production-queue.md"
    queue.write_text(f"# 队列\n\n{probe.PROPOSAL_BEGIN}\n{probe.PROPOSAL_END}\n", encoding="utf-8")
    monkeypatch.setattr(probe, "QUEUE_FILE", queue)
    first = probe._update_proposal_board(["diag_20260822_test-a.md"])
    second = probe._update_proposal_board(["diag_20260822_test-a.md"])
    assert first == ["diag_20260822_test-a.md"]
    assert second == []  # 幂等：重跑不重复登记
    assert queue.read_text(encoding="utf-8").count("diag_20260822_test-a.md") == 1


def test_update_board_keeps_historical_rows(tmp_path, monkeypatch):
    """同一文件的多条历史裁定记录不得被重写删除（2026-08-22 误删实证）。"""
    queue = tmp_path / "production-queue.md"
    history = (
        f"{probe.PROPOSAL_BEGIN}\n"
        "- ~~60_feedback/diagnosis/diag_x.md｜裁定一｜风清扬 08-22~~ → 已复核\n"
        "- ~~60_feedback/diagnosis/diag_x.md｜裁定二｜风清扬 08-22~~ → 已复核\n"
        f"{probe.PROPOSAL_END}\n"
    )
    queue.write_text(history, encoding="utf-8")
    monkeypatch.setattr(probe, "QUEUE_FILE", queue)
    probe._update_proposal_board(["diag_x.md"])
    text = queue.read_text(encoding="utf-8")
    assert text.count("裁定一") == 1
    assert text.count("裁定二") == 1  # 历史行保留


def test_no_transition_capability():
    """边界硬编码：探针无领取/裁决/流转能力——不 import queue_transition，无 claim/complete/review 函数。"""
    src = Path(__file__).resolve().parent.parent.joinpath("conveyor_probe.py").read_text(encoding="utf-8")
    assert "import queue_transition" not in src
    assert "from queue_transition" not in src
    for fn in ("claim", "complete", "review", "release"):
        assert f"def {fn}" not in src
    import pytest
    with pytest.raises(AttributeError):
        probe.claim("x")  # 模块无此能力 = 试图领取被拒


def test_notify_dry_run_no_send(tmp_path, monkeypatch, capsys):
    monkeypatch.setattr(probe, "HOOKS_FILE", tmp_path / "none.json")  # 无配置 → dry-run 路径
    probe._notify({"ouyangfeng": "🔔 测试"}, dry_run=False, silent=False)
    out = capsys.readouterr().out
    assert "dry-run 不发送" in out  # 无 webhook 配置 → 不静默失败，显式打印
