"""#538 回归：review --override 改判通道（reviewed→queued 机器流转）。

四类用例（任务书第 4 条）：正常改判/缺 --reason 拒绝/非 reviewed 拒绝/台账留痕。

运行：python -m pytest 90_control/scripts/tests/test_review_override.py -q
沙盒：monkeypatch parse_queue/find_task/QUEUE_PATH/FORCE_LEDGER；task_9999_ 前缀不写胶囊事件。
"""
import sys
import tempfile
import unittest
from pathlib import Path

SCRIPT_DIR = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(SCRIPT_DIR))

import queue_transition as qt


class TestReviewOverride(unittest.TestCase):
    def _setup(self, rows, task_fp):
        self._olds = (qt.parse_queue, qt.find_task, qt._find_task_file_dual,
                      qt.QUEUE_PATH, qt.FORCE_LEDGER)
        self._rows = rows
        self._task_fp = task_fp
        qt.parse_queue = lambda: self._rows
        qt.find_task = lambda tid, rows=None: next((r for r in self._rows if r["task_id"] == tid), None)
        qt._find_task_file_dual = lambda tid: self._task_fp
        qt.apply_updates = lambda *a, **k: None  # 状态机写入点 stub（本批只验门禁/台账/追记）
        qt.QueueLock = _NullLock
        # #546：终审权校验另测（test_instance_registry.py），本批聚焦改判通道——stub 放行
        self._old_auth = qt._check_review_authority
        qt._check_review_authority = lambda *a, **k: (True, "")

    def _teardown(self):
        (qt.parse_queue, qt.find_task, qt._find_task_file_dual,
         qt.QUEUE_PATH, qt.FORCE_LEDGER) = self._olds
        qt.apply_updates = self._orig_apply
        qt.QueueLock = _OrigLock
        qt._check_review_authority = self._old_auth

    def _mk(self, td, status="reviewed"):
        qf = Path(td) / "queue.md"
        qf.write_text("# q\n", encoding="utf-8")
        tf = Path(td) / "task_9999_538test.md"
        tf.write_text("---\nid: 538\ngrade: A\nstatus: reviewed\n---\n\n# 任务\n", encoding="utf-8")
        ledger = Path(td) / "force-exceptions.log"
        rows = [{"seq": "538", "task_id": "task_9999_538test", "name": "n",
                 "status": status, "assignee": "huangyaoshi", "raw": "| 538 |"}]
        self._orig_apply = qt.apply_updates
        self._setup(rows, tf)
        qt.QUEUE_PATH = qf
        qt.FORCE_LEDGER = ledger
        return tf, ledger

    def test_normal_override(self):
        """reviewed + fail + override + reason → 改判成功+追记+台账。"""
        with tempfile.TemporaryDirectory() as td:
            tf, ledger = self._mk(td)
            try:
                ok, msg = qt.action_review("task_9999_538test", "fail", "欧阳锋",
                                           override=True, reason="实跑发现双 bug")
            finally:
                self._teardown()
            self.assertTrue(ok, msg)
            self.assertIn("改判", msg)
            body = tf.read_text(encoding="utf-8")
            self.assertIn("## 改判记录", body)
            self.assertIn("PASS A → FAIL", body)
            self.assertIn("实跑发现双 bug", body)
            self.assertIn("task_9999_538test", ledger.read_text(encoding="utf-8"))

    def test_override_without_reason_rejected(self):
        with tempfile.TemporaryDirectory() as td:
            tf, ledger = self._mk(td)
            try:
                ok, msg = qt.action_review("task_9999_538test", "fail", "欧阳锋", override=True)
            finally:
                self._teardown()
            self.assertFalse(ok)
            self.assertIn("--reason", msg)
            self.assertFalse(ledger.exists())  # 拒绝不留痕

    def test_override_non_reviewed_rejected(self):
        with tempfile.TemporaryDirectory() as td:
            tf, _ = self._mk(td, status="pending_review")
            try:
                ok, msg = qt.action_review("task_9999_538test", "fail", "欧阳锋",
                                           override=True, reason="x")
            finally:
                self._teardown()
            self.assertFalse(ok)

    def test_override_wrong_reviewer_rejected(self):
        """改判权=终审者专用。"""
        with tempfile.TemporaryDirectory() as td:
            tf, _ = self._mk(td)
            try:
                ok, msg = qt.action_review("task_9999_538test", "fail", "王语嫣",
                                           override=True, reason="x")
            finally:
                self._teardown()
            self.assertFalse(ok)
            self.assertIn("欧阳锋", msg)


class _NullLock:
    def __init__(self, *a): pass
    def __enter__(self): return self
    def __exit__(self, *a): return False


_OrigLock = qt.QueueLock

if __name__ == "__main__":
    unittest.main()
