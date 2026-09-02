"""#616 任务3 回归：reviewer 翻转通道（王语嫣限 assignee=ouyangfeng 编排骨架单）。

实证：review 硬编码「只有欧阳锋可 review」，欧阳锋自己的单无人可翻转
（#544 手工翻转先例 + 09-02 #614 第二例）。修法：--reviewer 王语嫣 限编排骨架单放行，
F-035/F-036/台账留痕不变；终审权校验（#546）对王语嫣要求 cwd 有 wangyuyan 登记实例。

用例：编排骨架单王语嫣可审 / 非编排骨架单拒 / 其他 reviewer 拒 /
      authority 校验认 wangyuyan 登记 / 无 wangyuyan 登记拒。

运行：python -m pytest 90_control/scripts/tests/test_reviewer_flip_616.py -q
"""
import json
import os
import sys
import tempfile
import unittest
from pathlib import Path

SCRIPT_DIR = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(SCRIPT_DIR))

import queue_transition as qt

OPINION = ("## 终审记录\n\n核对完毕：交付物清单与任务单规格逐项一致，三处修改均有回归用例佐证，"
           "队列流转、台账、看板登记链路完整，准许入库。（编排骨架单翻转通道）\n")


class TestReviewerFlip(unittest.TestCase):
    def setUp(self):
        self._real_auth = qt._check_review_authority  # authority 用例要用真身
        self._saved = (
            qt.parse_queue, qt.find_task, qt._find_task_file_dual,
            qt.apply_updates, qt.QueueLock, qt._check_review_authority,
            qt._check_issue_disposition, qt.QUEUE_PATH,
        )
        qt.QueueLock = _NullLock
        qt.apply_updates = lambda *a, **k: None
        qt._check_review_authority = lambda *a, **k: (True, "")
        qt._check_issue_disposition = lambda *a, **k: (True, "")

    def tearDown(self):
        (qt.parse_queue, qt.find_task, qt._find_task_file_dual,
         qt.apply_updates, qt.QueueLock, qt._check_review_authority,
         qt._check_issue_disposition, qt.QUEUE_PATH) = self._saved

    def _mk(self, td, assignee):
        qf = Path(td) / "queue.md"
        qf.write_text("# q\n", encoding="utf-8")
        qt.QUEUE_PATH = qf
        tf = Path(td) / "task_9999_flip.md"
        tf.write_text(
            f"---\nid: task_9999_flip\nstatus: pending_review\nassignee: {assignee}\n---\n\n# 任务\n\n{OPINION}",
            encoding="utf-8",
        )
        rows = [{"seq": "9999", "task_id": "task_9999_flip", "name": "n",
                 "status": "pending_review", "assignee": assignee, "raw": "| 9999 |"}]
        qt.parse_queue = lambda: rows
        qt.find_task = lambda tid, rows_=None: next((r for r in rows if r["task_id"] == tid), None)
        qt._find_task_file_dual = lambda tid: tf
        return tf

    def test_wangyuyan_flip_skeleton_task_allowed(self):
        """assignee=ouyangfeng 的编排骨架单 + reviewer=王语嫣 → 放行。"""
        with tempfile.TemporaryDirectory() as td:
            self._mk(td, "ouyangfeng")
            ok, msg = qt.action_review("task_9999_flip", "pass", "王语嫣", "A-")
        self.assertTrue(ok, msg)
        self.assertIn("终审通过", msg)

    def test_wangyuyan_flip_non_skeleton_rejected(self):
        """assignee≠ouyangfeng（如 laowantong 生产单）→ 王语嫣仍不可审。"""
        with tempfile.TemporaryDirectory() as td:
            self._mk(td, "laowantong")
            ok, msg = qt.action_review("task_9999_flip", "pass", "王语嫣", "A-")
        self.assertFalse(ok)
        self.assertIn("翻转通道仅限", msg)

    def test_other_reviewer_rejected(self):
        with tempfile.TemporaryDirectory() as td:
            self._mk(td, "ouyangfeng")
            ok, msg = qt.action_review("task_9999_flip", "pass", "老顽童")
        self.assertFalse(ok)
        self.assertIn("只有欧阳锋", msg)

    def test_authority_accepts_wangyuyan_registration(self):
        """翻转通道终审权校验：cwd 有 wangyuyan 登记实例 → 放行。"""
        with tempfile.TemporaryDirectory() as td:
            reg = {"instances": {"wangyuyan": {
                "role": "wangyuyan", "cwd": os.getcwd(),
                "tool": "", "session": "", "ts": "2026-09-02T00:00:00"}}}
            rf = Path(td) / "active-instances.json"
            rf.write_text(json.dumps(reg, ensure_ascii=False), encoding="utf-8")
            old = qt.INSTANCE_REGISTRY
            qt.INSTANCE_REGISTRY = rf
            try:
                ok, msg = self._real_auth("task_9999_flip", "王语嫣")
            finally:
                qt.INSTANCE_REGISTRY = old
        self.assertTrue(ok, msg)

    def test_authority_accepts_legacy_suffixed_wangyuyan(self):
        """#620 裸名口径：在册旧身份 wangyuyan-kimi-0902 按同角色登记计 → 放行。"""
        with tempfile.TemporaryDirectory() as td:
            reg = {"instances": {"wangyuyan-kimi-0902": {
                "role": "wangyuyan-kimi-0902", "cwd": os.getcwd(),
                "tool": "", "session": "", "ts": "2026-09-02T01:30:57"}}}
            rf = Path(td) / "active-instances.json"
            rf.write_text(json.dumps(reg, ensure_ascii=False), encoding="utf-8")
            old = qt.INSTANCE_REGISTRY
            qt.INSTANCE_REGISTRY = rf
            try:
                ok, msg = self._real_auth("task_9999_flip", "王语嫣")
            finally:
                qt.INSTANCE_REGISTRY = old
        self.assertTrue(ok, msg)

    def test_authority_rejects_without_wangyuyan_registration(self):
        """只有 ouyangfeng 登记 ≠ 王语嫣可审（一具两职防控对称适用）。"""
        with tempfile.TemporaryDirectory() as td:
            reg = {"instances": {"ouyangfeng": {
                "role": "ouyangfeng", "cwd": os.getcwd(),
                "tool": "", "session": "", "ts": "2026-09-02T00:00:00"}}}
            rf = Path(td) / "active-instances.json"
            rf.write_text(json.dumps(reg, ensure_ascii=False), encoding="utf-8")
            old = qt.INSTANCE_REGISTRY
            qt.INSTANCE_REGISTRY = rf
            try:
                ok, msg = self._real_auth("task_9999_flip", "王语嫣")
            finally:
                qt.INSTANCE_REGISTRY = old
        self.assertFalse(ok)
        self.assertIn("register wangyuyan", msg)


class _NullLock:
    def __init__(self, *a): pass
    def __enter__(self): return self
    def __exit__(self, *a): return False


if __name__ == "__main__":
    unittest.main()
