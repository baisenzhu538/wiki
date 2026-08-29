"""#574 R1 回归：check-review-sla 审查供给 SLA 分级推送（30min 提醒 / 2h 升级）。

运行：python -m pytest 90_control/scripts/tests/test_check_review_sla.py -q
沙盒：monkeypatch 注入临时 QUEUE_FILE，不碰真实看板；monkeypatch _push/_append_role_todo 隔离飞书/todos 副作用。
"""
import importlib.util
import sys
from datetime import datetime, timedelta
from pathlib import Path

SCRIPT_DIR = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(SCRIPT_DIR))

_SPEC = importlib.util.spec_from_file_location(
    "check_review_sla", SCRIPT_DIR / "check-review-sla.py"
)
crs = importlib.util.module_from_spec(_SPEC)
_SPEC.loader.exec_module(crs)

BEGIN = "<!-- REVIEW-PENDING-BEGIN -->"
END = "<!-- REVIEW-PENDING-END -->"


def _queue(tmp_path, monkeypatch, items):
    qf = tmp_path / "production-queue.md"
    qf.write_text(f"# 队列\n\n{BEGIN}\n\n" + "\n".join(items) + f"\n\n{END}\n", encoding="utf-8")
    monkeypatch.setattr(crs, "QUEUE_FILE", qf)


def _isolate(monkeypatch, sent):
    """隔离飞书 webhook 与 todos 落盘副作用，记录发送的 (role, text)。"""
    monkeypatch.setattr(crs, "_push", lambda role, text, dry_run: sent.append((role, text)) or True)
    monkeypatch.setattr(crs._cp, "_append_role_todo", lambda role, text: None)


def _fmt(dt):
    return dt.strftime("%m-%d %H:%M")


def test_fresh_pending_ok(tmp_path, monkeypatch):
    """10min 挂审：未超 30min 阈值 → 不推送，exit 0。"""
    fresh = _fmt(datetime.now() - timedelta(minutes=10))
    _queue(tmp_path, monkeypatch, [f"- #505 task_x｜huangyaoshi｜提审 {fresh}｜60_feedback/tasks/task_x.md"])
    sent = []
    _isolate(monkeypatch, sent)
    assert crs.main() == 0
    assert sent == []  # 未到提醒阈值，不推


def test_remind_over_30min(tmp_path, monkeypatch):
    """31min 挂审：软提醒推审查者（ouyangfeng），exit 0。"""
    age = _fmt(datetime.now() - timedelta(minutes=31))
    _queue(tmp_path, monkeypatch, [f"- #505 task_x｜huangyaoshi｜提审 {age}｜60_feedback/tasks/task_x.md"])
    sent = []
    _isolate(monkeypatch, sent)
    assert crs.main() == 0
    assert sent, "31min 应触发提醒推送"
    assert sent[0][0] == "ouyangfeng"
    assert "#505" in sent[0][1] and "60_feedback/tasks/task_x.md" in sent[0][1]


def test_escalate_over_2h(tmp_path, monkeypatch):
    """3h 挂审：硬升级 @ 负责人/老板，推审查者 + 王语嫣群，exit 1。"""
    age = _fmt(datetime.now() - timedelta(hours=3))
    _queue(tmp_path, monkeypatch, [f"- #505 task_x｜huangyaoshi｜提审 {age}｜60_feedback/tasks/task_x.md"])
    sent = []
    _isolate(monkeypatch, sent)
    assert crs.main() == 1
    roles = [r for r, _ in sent]
    assert roles == ["ouyangfeng", "wangyuyan"], f"升级应推两通道，实际 {roles}"
    assert "@" in sent[0][1], "升级消息应含 @ 标记"


def test_struck_lines_ignored(tmp_path, monkeypatch):
    """划销行跳过：不触发任何推送，exit 0。"""
    old = _fmt(datetime.now() - timedelta(hours=30))
    _queue(tmp_path, monkeypatch, [
        f"- ~~#500 task_y｜laowantong｜提审 {old}｜60_feedback/tasks/task_y.md~~ → 已终审 PASS A",
    ])
    sent = []
    _isolate(monkeypatch, sent)
    assert crs.main() == 0
    assert sent == []


def test_empty_section_ok(tmp_path, monkeypatch):
    _queue(tmp_path, monkeypatch, [])
    assert crs.main() == 0


def test_missing_markers_fail(tmp_path, monkeypatch):
    qf = tmp_path / "production-queue.md"
    qf.write_text("# 队列（无 REVIEW-PENDING 段）\n", encoding="utf-8")
    monkeypatch.setattr(crs, "QUEUE_FILE", qf)
    assert crs.main() == 1


def test_dry_run_no_side_effect(tmp_path, monkeypatch):
    """--dry-run：升级分支不真发 webhook、不落 todos。"""
    monkeypatch.setattr(sys, "argv", ["check-review-sla.py", "--dry-run"])
    age = _fmt(datetime.now() - timedelta(hours=3))
    _queue(tmp_path, monkeypatch, [f"- #505 task_x｜huangyaoshi｜提审 {age}｜60_feedback/tasks/task_x.md"])
    todos = []
    monkeypatch.setattr(crs._cp, "_append_role_todo", lambda role, text: todos.append((role, text)))
    # _push 走 dry_run 分支返回 False 不发送，无需额外 mock
    assert crs.main() == 1  # 升级仍破线 exit 1
    assert todos == [], "dry-run 不应落 todos"
