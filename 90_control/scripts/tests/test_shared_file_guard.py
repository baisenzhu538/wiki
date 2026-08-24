"""#505 回归：shared_file_guard stale 检测 + conveyor_probe 队列写点 QueueLock 兜底。

模拟并发写场景：snapshot 后文件被他人改动 / HEAD 移动 → verify 必须报警（exit 1 语义）。
"""
import sys
import tempfile
import unittest
from pathlib import Path

SCRIPT_DIR = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(SCRIPT_DIR))

import shared_file_guard as sfg


class TestSharedFileGuard(unittest.TestCase):
    """#505 L1：并发 add 同文件场景——检测/报警生效。"""

    def setUp(self):
        self._tmp = Path(tempfile.mkdtemp())
        self._fp = self._tmp / "production-queue.md"
        self._fp.write_text("# 队列\n| 1 | `task_a` | 甲 | queued | huangyaoshi |\n",
                            encoding="utf-8")
        self._orig_head = sfg._git_head
        sfg._git_head = lambda: "aaaa1111bbbb2222"  # 隔离真实 git 状态
        self.addCleanup(self._restore)

    def _restore(self):
        sfg._git_head = self._orig_head

    def test_fresh_when_nothing_changed(self):
        """基线后零变更 → FRESH。"""
        base = sfg.snapshot(self._fp)
        fresh, msg = sfg.verify(self._fp, base)
        self.assertTrue(fresh, msg)
        self.assertEqual(msg, "FRESH")

    def test_stale_when_file_changed_concurrently(self):
        """并发写实证场景：snapshot 后另一实例改了同文件 → STALE 报警。"""
        base = sfg.snapshot(self._fp)
        # 模拟并发写：另一实例在窗口内追加了一行（#488 行错位事故的温床）
        self._fp.write_text(self._fp.read_text(encoding="utf-8")
                            + "| 2 | `task_b` | 乙 | queued | laowantong |\n",
                            encoding="utf-8")
        fresh, msg = sfg.verify(self._fp, base)
        self.assertFalse(fresh)
        self.assertIn("STALE", msg)
        self.assertIn("已变化", msg)

    def test_stale_when_head_moved(self):
        """git HEAD 移动（他人 commit 入仓）→ STALE，提示重读最新态。"""
        base = sfg.snapshot(self._fp)
        sfg._git_head = lambda: "cccc3333dddd4444"
        fresh, msg = sfg.verify(self._fp, base)
        self.assertFalse(fresh)
        self.assertIn("HEAD 已移动", msg)

    def test_unknown_head_fail_open(self):
        """git 不可用（unknown）→ 不阻断，仅靠文件 hash 判定。"""
        sfg._git_head = lambda: "unknown"
        base = sfg.snapshot(self._fp)
        fresh, msg = sfg.verify(self._fp, base)
        self.assertTrue(fresh, msg)

    def test_bad_baseline_rejected(self):
        """基线格式错 → 拒绝（防调用方传错参数静默通过）。"""
        fresh, msg = sfg.verify(self._fp, "not-a-baseline")
        self.assertFalse(fresh)
        self.assertIn("格式错误", msg)

    def test_missing_file_stale(self):
        """文件在基线后被删 → STALE（现场与基线根本不符）。"""
        base = sfg.snapshot(self._fp)
        self._fp.unlink()
        fresh, msg = sfg.verify(self._fp, base)
        self.assertFalse(fresh)
        self.assertIn("STALE", msg)


class TestConveyorProbeQueueLock(unittest.TestCase):
    """#505：conveyor_probe 队列文件 3 个写函数已套 QueueLock（装饰器注入）。"""

    def test_write_functions_wrapped(self):
        """行为级验证：mock QueueLock，调用 3 个写函数 → 每次必经 enter/exit（锁名 production-queue）。"""
        sys.path.insert(0, str(SCRIPT_DIR.parent.parent / "kdo-tools"))
        import conveyor_probe as cp

        calls = []

        class FakeLock:
            def __init__(self, name):
                calls.append(("init", name))

            def __enter__(self):
                calls.append(("enter", None))
                return self

            def __exit__(self, *a):
                calls.append(("exit", None))
                return False

        orig = cp.QueueLock
        cp.QueueLock = FakeLock
        try:
            cp._update_proposal_board([])
            cp._update_proposal_board_friction([])
            cp._update_proposal_board_gate([])
        finally:
            cp.QueueLock = orig
        enters = [c for c in calls if c[0] == "enter"]
        exits = [c for c in calls if c[0] == "exit"]
        self.assertEqual(len(enters), 3, f"3 个写函数都应经过锁 enter，实际: {calls}")
        self.assertEqual(len(exits), 3)
        names = {c[1] for c in calls if c[0] == "init"}
        self.assertEqual(names, {"production-queue"})


if __name__ == "__main__":
    unittest.main()
