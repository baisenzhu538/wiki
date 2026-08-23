"""Regression tests for queue_batch_accept.py (#479：四步一体 + 禁静默 + 对账)."""
import importlib.util
import shutil
import sys
import tempfile
import unittest
from pathlib import Path

KDO_TOOLS = Path(__file__).resolve().parent.parent
_SPEC = importlib.util.spec_from_file_location("queue_batch_accept", KDO_TOOLS / "queue_batch_accept.py")
qba = importlib.util.module_from_spec(_SPEC)
_SPEC.loader.exec_module(qba)

QUEUE_TMPL = """# 队列
|:---:|:---|:---|:---:|:---:|---:|
| 1 | `task_test-batch` | 批次任务 | pending_review | laowantong | 验收 |
<!-- REVIEW-PENDING-BEGIN（queue_transition 自动维护，勿手改） -->
- #1 task_test-batch｜laowantong｜提审 08-23 10:00｜60_feedback/tasks/task_test-batch.md
<!-- REVIEW-PENDING-END -->
"""

TASK_TMPL = """---
id: 1
assignee: laowantong
status: pending_review
---
# task_test-batch

## 批次验收记录

- 欧阳锋：PASS A-（2026-08-23）
"""


class Base(unittest.TestCase):
    def setUp(self):
        self.tmp = Path(tempfile.mkdtemp())
        self.tasks = self.tmp / "tasks"
        self.tasks.mkdir()
        self.queue = self.tmp / "production-queue.md"
        (self.tasks / "task_test-batch.md").write_text(TASK_TMPL, encoding="utf-8")
        self.queue.write_text(QUEUE_TMPL, encoding="utf-8")
        self._orig = (qba.QUEUE_FILE, qba.TASK_DIR)
        qba.QUEUE_FILE, qba.TASK_DIR = self.queue, self.tasks
        # 拦截 git commit（测试环境无 git 场景）
        self._orig_git = qba._git_commit
        qba._git_commit = lambda *a, **k: None

    def tearDown(self):
        qba.QUEUE_FILE, qba.TASK_DIR = self._orig
        qba._git_commit = self._orig_git
        shutil.rmtree(self.tmp, ignore_errors=True)


class TestAccept(Base):
    def test_four_steps_all_applied(self):
        rc = qba.action_accept("task_test-batch", "A-")
        self.assertEqual(rc, 0)
        # 步2：REVIEW-PENDING 划线
        q = self.queue.read_text(encoding="utf-8")
        self.assertIn("~~#1 task_test-batch", q)
        self.assertIn("批次验收（A-）", q)
        # 步3：队列行 queued
        rows = qba.parse_queue(self.queue)
        target = next(r for r in rows if r["task_id"] == "task_test-batch")
        self.assertEqual(target["status"], "queued")
        # 步4：frontmatter queued
        self.assertIn("status: queued", (self.tasks / "task_test-batch.md").read_text(encoding="utf-8"))

    def test_missing_accept_section_rejected(self):
        (self.tasks / "task_test-batch.md").write_text(
            TASK_TMPL.replace("## 批次验收记录", "## 别的节"), encoding="utf-8")
        rc = qba.action_accept("task_test-batch", "A-")
        self.assertEqual(rc, 1)
        # 未落盘
        self.assertIn("pending_review", self.queue.read_text(encoding="utf-8"))

    def test_not_pending_review_rejected(self):
        self.queue.write_text(QUEUE_TMPL.replace("pending_review", "queued"), encoding="utf-8")
        rc = qba.action_accept("task_test-batch", "A-")
        self.assertEqual(rc, 1)

    def test_silent_failure_asserted(self):
        """静默失败根治：替换计数≠1 必须抛错中止（#426 教训）。"""
        # 前置通过（状态解析 pending_review），但步 3 正则不匹配（状态列双空格）
        self.queue.write_text(QUEUE_TMPL.replace("| pending_review |", "| pending_review  |"), encoding="utf-8")
        with self.assertRaises(RuntimeError):
            qba.action_accept("task_test-batch", "A-")

    def test_dry_run_no_write(self):
        rc = qba.action_accept("task_test-batch", "A-", dry_run=True)
        self.assertEqual(rc, 0)
        self.assertIn("pending_review", self.queue.read_text(encoding="utf-8"))
        self.assertIn("status: pending_review", (self.tasks / "task_test-batch.md").read_text(encoding="utf-8"))


if __name__ == "__main__":
    unittest.main()
