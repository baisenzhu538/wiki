"""#520 R2 回归：generate-dashboard 阻塞链标记（pending_review 后方有同角色 queued → 🔴阻塞链）。

运行：python -m pytest kdo-tools/tests/test_dashboard_blocking.py -q
"""
import importlib.util
from pathlib import Path

_SPEC = importlib.util.spec_from_file_location(
    "generate_dashboard", Path(__file__).resolve().parent.parent / "generate-dashboard.py"
)
gd = importlib.util.module_from_spec(_SPEC)
_SPEC.loader.exec_module(gd)


def _task(seq, status, assignee):
    return {"seq": seq, "id": f"t{seq}", "name": f"任务{seq}", "status": status,
            "assignee": assignee, "cards": "", "deps": "", "source": "",
            "notes": "", "priority": "P1", "grade": "", "conditional": False}


def test_pending_review_with_queued_behind_marked():
    tasks = [_task(505, "pending_review", "huangyaoshi"),
             _task(506, "queued", "huangyaoshi")]
    gd._mark_blocking_chains(tasks)
    assert tasks[0]["blocking"] is True
    assert tasks[1]["blocking"] is False


def test_pending_review_without_queued_behind_not_marked():
    tasks = [_task(505, "pending_review", "huangyaoshi"),
             _task(490, "queued", "huangyaoshi")]  # 前方 queued 不算阻塞链
    gd._mark_blocking_chains(tasks)
    assert tasks[0]["blocking"] is False


def test_other_assignee_queued_not_marked():
    tasks = [_task(505, "pending_review", "huangyaoshi"),
             _task(506, "queued", "laowantong")]
    gd._mark_blocking_chains(tasks)
    assert tasks[0]["blocking"] is False


def test_queued_task_never_marked():
    tasks = [_task(505, "queued", "huangyaoshi"),
             _task(506, "queued", "huangyaoshi")]
    gd._mark_blocking_chains(tasks)
    assert all(not t["blocking"] for t in tasks)


def test_blocking_badge_in_card_html():
    t = _task(505, "pending_review", "huangyaoshi")
    t["blocking"] = True
    html = gd._task_card_html(t, "pending")
    assert "🔴阻塞链" in html
