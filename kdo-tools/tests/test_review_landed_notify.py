"""#535 回归：终审落点通知（PASS 简报+FAIL 置顶）+ myqueue 最近终审栏。

运行：python -m pytest kdo-tools/tests/test_review_landed_notify.py -q
"""
import importlib.util
from pathlib import Path

_SPEC = importlib.util.spec_from_file_location(
    "conveyor_probe", Path(__file__).resolve().parent.parent / "conveyor_probe.py"
)
probe = importlib.util.module_from_spec(_SPEC)
_SPEC.loader.exec_module(probe)


def _task_with_review(tmp_path, task_id, review_section):
    td = tmp_path / "tasks"
    td.mkdir(exist_ok=True)
    fp = td / f"{task_id}.md"
    fp.write_text(f"# 任务\n\n## 执行报告\n\nx\n\n{review_section}\n", encoding="utf-8")
    return td


def test_brief_pass_with_grade(tmp_path, monkeypatch):
    td = _task_with_review(tmp_path, "task_a", "## 终审记录\n\n- **终审**：欧阳锋 08-26 **PASS A**\n")
    monkeypatch.setattr(probe, "TASK_DIR", td)
    assert probe._review_brief("task_a") == "PASS A"


def test_brief_fail_with_rework_and_o2(tmp_path, monkeypatch):
    td = _task_with_review(tmp_path, "task_b",
                           "## 终审记录\n\n- **终审**：欧阳锋 08-26 **FAIL**\n- O2 指令：返工\n- 返工项 2 条\n")
    monkeypatch.setattr(probe, "TASK_DIR", td)
    brief = probe._review_brief("task_b")
    assert brief.startswith("FAIL") and "O2" in brief and "有返工项" in brief


def test_brief_missing_file_empty(tmp_path, monkeypatch):
    monkeypatch.setattr(probe, "TASK_DIR", tmp_path / "nope")
    assert probe._review_brief("ghost") == ""


def test_prepend_puts_fail_on_top(tmp_path, monkeypatch):
    monkeypatch.setattr(probe, "TODOS_DIR", tmp_path)
    fp = tmp_path / "laowantong.md"
    fp.write_text("# laowantong 待办\n\n- [旧] 既有待办\n", encoding="utf-8")
    probe._prepend_role_todo("laowantong", "🔴 KDO 退回 1 单（返工优先）：#531")
    body = fp.read_text(encoding="utf-8")
    lines = body.splitlines()
    fail_idx = next(i for i, ln in enumerate(lines) if "退回 1 单" in ln)
    old_idx = next(i for i, ln in enumerate(lines) if "既有待办" in ln)
    assert fail_idx < old_idx  # FAIL 在既有条目之上（置顶）


def test_prepend_creates_file(tmp_path, monkeypatch):
    monkeypatch.setattr(probe, "TODOS_DIR", tmp_path)
    probe._prepend_role_todo("huangyaoshi", "🔴 退回测试")
    assert "退回测试" in (tmp_path / "huangyaoshi.md").read_text(encoding="utf-8")
