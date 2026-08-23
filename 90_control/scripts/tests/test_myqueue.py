"""Regression tests for queue_transition.myqueue (#472：角色任务路由只读视图)."""
import io
import sys
import unittest
from contextlib import redirect_stdout
from pathlib import Path

SCRIPT_DIR = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(SCRIPT_DIR))

import queue_transition as qt


def _row(seq, task_id, status, assignee, name="任务", raw=""):
    return {"seq": str(seq), "task_id": task_id, "name": name, "status": status,
            "assignee": assignee, "raw": raw or f"| {seq} | `{task_id}` | {name} | {status} | {assignee} |"}


class MyqueueBase(unittest.TestCase):
    def setUp(self):
        self.rows = []
        self._orig_parse = qt.parse_queue
        self._orig_depends = qt._task_depends_on
        self._orig_active = qt._is_active_task
        qt.parse_queue = lambda: self.rows
        qt._task_depends_on = lambda task_id: self.depends.get(task_id, [])
        qt._is_active_task = lambda tid, rows: tid in self.active
        self.depends = {}
        self.active = set()

    def tearDown(self):
        qt.parse_queue = self._orig_parse
        qt._task_depends_on = self._orig_depends
        qt._is_active_task = self._orig_active

    def run_myqueue(self, role):
        buf = io.StringIO()
        with redirect_stdout(buf):
            rc = qt.action_myqueue(role)
        return rc, buf.getvalue()


class TestMyqueueViews(MyqueueBase):
    def test_claimable_queued_no_dep(self):
        self.rows = [_row(1, "task_a", "queued", "huangyaoshi")]
        rc, out = self.run_myqueue("huangyaoshi")
        self.assertEqual(rc, 0)
        self.assertIn("✅ 可领 1", out)
        self.assertIn("task_a", out)
        self.assertIn("🧊 冻结 0", out)

    def test_frozen_by_queue_annotation(self):
        # 队列行标注冻结留档/勿领 → 冻结（#459 被取代挂账同款）
        self.rows = [
            _row(2, "task_b", "queued", "huangyaoshi",
                 raw="| 2 | `task_b` | x | queued | huangyaoshi | 冻结留档勿领取 |"),
        ]
        rc, out = self.run_myqueue("huangyaoshi")
        self.assertIn("🧊 冻结 1", out)
        self.assertIn("task_b", out)
        self.assertIn("✅ 可领 0", out)  # 冻结任务不进可领

    def test_waiting_on_active_dependency(self):
        self.rows = [
            _row(3, "task_c", "queued", "huangyaoshi"),
            _row(4, "task_dep", "pending_review", "laowantong"),
        ]
        self.depends["task_c"] = ["task_dep"]
        self.active = {"task_dep"}  # 依赖仍在流转
        rc, out = self.run_myqueue("huangyaoshi")
        self.assertIn("⏸ 等依赖 1", out)
        self.assertIn("task_c", out)
        self.assertIn("task_dep", out)

    def test_dep_satisfied_claimable(self):
        self.rows = [_row(5, "task_e", "queued", "huangyaoshi")]
        self.depends["task_e"] = ["task_done"]
        self.active = set()  # 依赖无活跃行=已结束=满足
        rc, out = self.run_myqueue("huangyaoshi")
        self.assertIn("✅ 可领 1", out)
        self.assertIn("task_e", out)

    def test_doing_and_reviewing(self):
        self.rows = [
            _row(6, "task_f", "claimed-huangyaoshi", "huangyaoshi"),
            _row(7, "task_g", "pending_review", "huangyaoshi"),
        ]
        rc, out = self.run_myqueue("huangyaoshi")
        self.assertIn("🚧 进行中 1", out)
        self.assertIn("task_f", out)
        self.assertIn("⏳ 待终审 1", out)
        self.assertIn("task_g", out)

    def test_other_role_not_shown(self):
        self.rows = [
            _row(8, "task_h", "queued", "laowantong"),
            _row(9, "task_i", "queued", "huangyaoshi"),
        ]
        rc, out = self.run_myqueue("huangyaoshi")
        self.assertIn("task_i", out)
        self.assertNotIn("task_h", out)


class TestTaskDependsOn(unittest.TestCase):
    def test_real_task_file_returns_list(self):
        # 真实任务书（存量无 depends_on → 空列表=可领；不崩）
        deps = qt._task_depends_on("task_20260823_huangyaoshi-file-flow-lint")
        self.assertIsInstance(deps, list)

    def test_missing_task_returns_empty(self):
        self.assertEqual(qt._task_depends_on("task_9999_nonexistent"), [])


if __name__ == "__main__":
    unittest.main()
