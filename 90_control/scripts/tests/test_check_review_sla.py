"""#520 R3 回归：check-review-sla 审查供给 SLA 观测（pending_review 最大年龄 >2h → exit 1）。

运行：python -m pytest 90_control/scripts/tests/test_check_review_sla.py -q
沙盒：monkeypatch 注入临时 QUEUE_FILE，不碰真实看板。
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


def _fmt(dt):
    return dt.strftime("%m-%d %H:%M")


def test_fresh_pending_ok(tmp_path, monkeypatch):
    fresh = _fmt(datetime.now() - timedelta(minutes=30))
    _queue(tmp_path, monkeypatch, [f"- #505 task_x｜huangyaoshi｜提审 {fresh}｜60_feedback/tasks/task_x.md"])
    assert crs.main() == 0


def test_old_pending_alerts(tmp_path, monkeypatch):
    old = _fmt(datetime.now() - timedelta(hours=3))
    _queue(tmp_path, monkeypatch, [f"- #505 task_x｜huangyaoshi｜提审 {old}｜60_feedback/tasks/task_x.md"])
    assert crs.main() == 1


def test_struck_lines_ignored(tmp_path, monkeypatch):
    old = _fmt(datetime.now() - timedelta(hours=30))
    _queue(tmp_path, monkeypatch, [
        f"- ~~#500 task_y｜laowantong｜提审 {old}｜60_feedback/tasks/task_y.md~~ → 已终审 PASS A",
    ])
    assert crs.main() == 0


def test_empty_section_ok(tmp_path, monkeypatch):
    _queue(tmp_path, monkeypatch, [])
    assert crs.main() == 0


def test_missing_markers_fail(tmp_path, monkeypatch):
    qf = tmp_path / "production-queue.md"
    qf.write_text("# 队列（无 REVIEW-PENDING 段）\n", encoding="utf-8")
    monkeypatch.setattr(crs, "QUEUE_FILE", qf)
    assert crs.main() == 1
