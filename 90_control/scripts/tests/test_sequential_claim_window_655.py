"""#655 回归：claim --sequence 同执行者显式多单连发窗口。

场景（friction 三连 09-06 03:48/04:33/04:47）：编排者一条指令派多单，complete 前单
→ claim 下一单撞 #504「同执行者 pending_review 占位」，只能 --force+reason。

- own pending_review 阻塞 + --sequence → 放行（sequential 注记）
- own pending_review 阻塞 无 --sequence → 照旧拦（#504 不弱化），报错指路 --sequence
- --sequence 不越界：FIFO 他单 pending / #503 claimed 锁仍拦
- --sequence 放行不走 force 台账（非例外，是预期流）

运行：python -m pytest 90_control/scripts/tests/test_sequential_claim_window_655.py -q
沙盒：queue_gate.can_claim 纯函数面 + queue_transition.action_claim monkeypatch 隔离
（沿 test_queue_transition.py TestForceClaimLedger 同款），不碰真实队列。
"""
import tempfile
import unittest
from pathlib import Path

import sys

SCRIPT_DIR = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(SCRIPT_DIR))

import queue_gate as qg
import queue_transition as qt


def _row(seq: int, task_id: str, status: str, assignee: str = "huangyaoshi") -> dict:
    return {"seq": seq, "task_id": task_id, "status": status, "assignee": assignee,
            "name": task_id, "raw": ""}


class TestSequenceGatePure(unittest.TestCase):
    """can_claim 纯函数面：sequence 只放宽 own pending 一支。"""

    def test_655_sequence_passes_own_pending(self):
        """场景复现：前单 pending_review，claim 下一单 --sequence → 放行+注记。"""
        rows = [
            _row(652, "task_a_constitution", "pending_review"),
            _row(653, "task_b_crossrepo", "queued"),
        ]
        ok, reason = qg.can_claim("task_b_crossrepo", rows, "huangyaoshi", sequence=True)
        self.assertTrue(ok, f"--sequence 未放行连发: {reason}")
        self.assertIn("sequential", reason)
        self.assertIn("#655", reason)

    def test_504_still_blocks_without_sequence(self):
        """护栏：不带 --sequence 时 #504 照旧拦（门禁不弱化），并指路 --sequence。"""
        rows = [
            _row(652, "task_a_constitution", "pending_review"),
            _row(653, "task_b_crossrepo", "queued"),
        ]
        ok, reason = qg.can_claim("task_b_crossrepo", rows, "huangyaoshi")
        self.assertFalse(ok)
        self.assertIn("#504", reason)
        self.assertIn("--sequence", reason)

    def test_655_sequence_does_not_bypass_fifo_others_pending(self):
        """越界护栏①：队列前方是他单 pending_review → --sequence 不得放行（FIFO 照旧）。"""
        rows = [
            _row(650, "task_other_role", "pending_review", assignee="laowantong"),
            _row(652, "task_a_constitution", "pending_review"),
            _row(653, "task_b_crossrepo", "queued"),
        ]
        ok, reason = qg.can_claim("task_b_crossrepo", rows, "huangyaoshi", sequence=True)
        self.assertFalse(ok, f"--sequence 越过他单 FIFO 阻塞: {reason}")

    def test_655_sequence_does_not_bypass_claimed_lock(self):
        """越界护栏②：名下还有 claimed 在途单 → --sequence 不得放行（#503 锁照旧）。"""
        rows = [
            _row(652, "task_a_constitution", "pending_review"),
            _row(653, "task_b_crossrepo", "claimed-huangyaoshi"),
            _row(655, "task_c_window", "queued"),
        ]
        ok, reason = qg.can_claim("task_c_window", rows, "huangyaoshi", sequence=True)
        self.assertFalse(ok, f"--sequence 越过 #503 claimed 锁: {reason}")
        self.assertIn("claimed", reason)


class TestSequenceClaimEndToEnd(unittest.TestCase):
    """action_claim 面：--sequence 放行 + 不写 force 台账（沿 TestForceClaimLedger 沙盒）。"""

    def _setup(self, rows):
        self._tmpdir = Path(tempfile.mkdtemp())
        self._task_fp = self._tmpdir / "task_9999_655test.md"
        self._task_fp.write_text(
            "---\nid: 9999\nassignee: huangyaoshi\nstatus: queued\n---\n# t\n",
            encoding="utf-8")
        self._queue_fp = self._tmpdir / "production-queue.md"
        self._queue_fp.write_text("# 队列\n", encoding="utf-8")
        self._ledger = self._tmpdir / "force-exceptions.log"
        self._olds = (qt.parse_queue, qt.find_task, qt._find_task_file_dual,
                      qt.update_queue_status, qt.QUEUE_PATH, qt.FORCE_LEDGER)
        qt.parse_queue = lambda: rows
        qt.find_task = lambda tid, rows=None: next(
            (r for r in rows if r["task_id"] == tid), None)
        qt._find_task_file_dual = lambda tid: self._task_fp
        qt.update_queue_status = lambda tid, st: None
        qt.QUEUE_PATH = self._queue_fp
        qt.FORCE_LEDGER = self._ledger

    def _teardown(self):
        (qt.parse_queue, qt.find_task, qt._find_task_file_dual,
         qt.QUEUE_PATH, qt.update_queue_status, qt.FORCE_LEDGER) = self._olds

    def test_sequence_claim_passes_without_force_entry(self):
        """两单连发模拟：前单 pending_review，claim 下一单 --sequence → 放行 + 台账零新增。"""
        rows = [
            _row(652, "task_9999_prev", "pending_review"),
            _row(655, "task_9999_655test", "queued"),
        ]
        self._setup(rows)
        try:
            ok, msg = qt.action_claim("task_9999_655test", "huangyaoshi", sequence=True)
        finally:
            self._teardown()
        self.assertTrue(ok, msg)
        self.assertIn("sequential", msg)
        self.assertFalse(self._ledger.exists(), "--sequence 不得写 force 台账")

    def test_plain_claim_still_blocked(self):
        """同场景不带 --sequence → 照旧拦（#504 语义不回归）。"""
        rows = [
            _row(652, "task_9999_prev", "pending_review"),
            _row(655, "task_9999_655test", "queued"),
        ]
        self._setup(rows)
        try:
            ok, msg = qt.action_claim("task_9999_655test", "huangyaoshi")
        finally:
            self._teardown()
        self.assertFalse(ok)
        self.assertIn("#504", msg)


if __name__ == "__main__":
    unittest.main()
