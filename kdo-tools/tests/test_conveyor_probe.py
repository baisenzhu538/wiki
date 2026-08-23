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
    monkeypatch.setattr(probe, "HOOKS_FILE", tmp_path / "none.json")  # 无配置 → 显式打印不静默失败
    probe._notify({"ouyangfeng": "🔔 测试"}, dry_run=False, silent=False)
    out = capsys.readouterr().out
    assert "不发送" in out


# ── #421 终审 P1 修复回归（静默/dry-run 不消耗幂等配额 + pending 补发）──

def test_notify_silent_returns_empty():
    """静默 = 不发送且不消耗配额（返回空列表，调用方据此把消息留 pending）。"""
    sent = probe._notify({"ouyangfeng": "🔔 测试"}, dry_run=False, silent=True)
    assert sent == []


def test_notify_dryrun_returns_empty():
    """dry-run = 不发送不消耗配额。"""
    sent = probe._notify({"ouyangfeng": "🔔 测试"}, dry_run=True, silent=False)
    assert sent == []


def test_notify_success_returns_sent_roles(tmp_path, monkeypatch):
    import json as _json
    hooks = tmp_path / "hooks.json"
    hooks.write_text(_json.dumps({"ouyangfeng": {"url": "https://example.com/hook", "key": "k"}}), encoding="utf-8")
    monkeypatch.setattr(probe, "HOOKS_FILE", hooks)
    monkeypatch.setattr(probe, "_send_hook", lambda url, text, key=None: True)
    sent = probe._notify({"ouyangfeng": "🔔 测试"}, dry_run=False, silent=False)
    assert sent == ["ouyangfeng"]


def test_msg_key_stable():
    k1 = probe._msg_key("ouyangfeng", "🔔 KDO 新提审 3 单：#421，请终审")
    k2 = probe._msg_key("ouyangfeng", "🔔 KDO 新提审 3 单：#421，请终审")
    assert k1 == k2
    assert k1.startswith("ouyangfeng:")


# ── #443 可领取通知按 assignee 路由回归 ──

def test_route_huangyaoshi_task():
    rows = [("task_443_x", "443", "huangyaoshi"), ("task_426_y", "426", "laowantong")]
    buckets = probe._route_queued(rows)
    assert "huangyaoshi" in buckets and [t for t, _ in buckets["huangyaoshi"]] == ["task_443_x"]
    assert "laowantong" in buckets and [t for t, _ in buckets["laowantong"]] == ["task_426_y"]


def test_route_instance_aliases():
    """hermes/kimi 实例 → laowantong 通道（E020 实例口径）。"""
    rows = [("task_a", "1", "hermes"), ("task_b", "2", "kimi")]
    buckets = probe._route_queued(rows)
    assert buckets["laowantong"] == [("task_a", "1"), ("task_b", "2")]


def test_route_unknown_falls_back():
    """未知/缺省 assignee → 回落 laowantong，不静默丢。"""
    rows = [("task_x", "9", ""), ("task_y", "10", "some-new-instance")]
    buckets = probe._route_queued(rows)
    assert len(buckets.get("laowantong", [])) == 2


def test_route_split_buckets():
    """同批多 assignee → 拆分投递（一角色一桶）。"""
    rows = [("task_1", "1", "huangyaoshi"), ("task_2", "2", "wangyuyan"), ("task_3", "3", "laowantong")]
    buckets = probe._route_queued(rows)
    assert set(buckets.keys()) == {"huangyaoshi", "wangyuyan", "laowantong"}


# ── #458 第四探针（friction 增量扫描）回归 ──

def test_friction_scan_detects_new_lines(tmp_path, monkeypatch):
    """friction 增量检测：新行被检出，重复行幂等。"""
    f = tmp_path / "friction-log.md"
    f.write_text("# friction\n\n| 时间 | 场景 | 问题 |\n|:--|:--|:--|\n\n2026-08-23 10:00｜门禁误判｜测试问题一｜建议收窄\n", encoding="utf-8")
    monkeypatch.setattr(probe, "RETRO_ROOT", tmp_path.parent)
    monkeypatch.setattr(probe, "FRICTION_ROLES", [tmp_path.name])
    monkeypatch.setattr(probe, "SHARED_FRICTION", tmp_path / "none.md")

    state = {}
    first = probe._scan_friction(state)
    assert len(first) == 1
    assert "测试问题一" in first[0]

    second = probe._scan_friction(state)
    assert second == []  # 幂等：重复扫描零新增

    # 追加新行 → 只检出新的
    f.write_text(f.read_text(encoding="utf-8") + "2026-08-23 11:00｜工具卡顿｜测试问题二\n", encoding="utf-8")
    third = probe._scan_friction(state)
    assert len(third) == 1
    assert "测试问题二" in third[0]


def test_friction_registration_marks_clue(tmp_path, monkeypatch):
    """friction 线索登记 PROPOSAL-PENDING：[friction] 标记 + 幂等。"""
    queue = tmp_path / "production-queue.md"
    queue.write_text(f"# 队列\n\n{probe.PROPOSAL_BEGIN}\n{probe.PROPOSAL_END}\n", encoding="utf-8")
    monkeypatch.setattr(probe, "QUEUE_FILE", queue)
    probe._update_proposal_board_friction(["[huangyaoshi] 2026-08-23 10:00｜门禁误判｜测试问题"])
    text = queue.read_text(encoding="utf-8")
    assert "[friction] [huangyaoshi] 2026-08-23 10:00" in text
    probe._update_proposal_board_friction(["[huangyaoshi] 2026-08-23 10:00｜门禁误判｜测试问题"])
    assert text.count("[friction]") == 1  # 幂等
