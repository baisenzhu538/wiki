"""#580（F-064）回归：终审 FAIL 打回自动 rework 标记 + 返工重提绕过 #504 拦截。

场景（任务单 60_feedback/tasks/task_20260830_huangyaoshi-rework-reclaim-bypass-504.md 验证节）：
  1. assignee 名下有 pending_review + rework:true 单 → 可直接 claim（无 force）
  2. assignee 名下有 pending_review + 普通新单 → 仍被 #504 拦截
  3. FAIL 打回（review fail / #538 override）→ 任务单自动打 rework: true
  4. 边界不放宽：他人前方 pending FIFO 阻塞照旧 / #503 claimed 锁照旧 / PASS 不打标

运行：python -m pytest 90_control/scripts/tests/test_rework_reclaim.py -q
沙盒：can_claim 侧注入 qg.TASKS_DIR；action_review 侧 monkeypatch
parse_queue/find_task/_find_task_file_dual/QUEUE_PATH/FORCE_LEDGER/_check_review_authority，
apply_updates 用真身（临时队列文件带合法表格行 + 临时任务单）——验证 rework:true 真落 frontmatter。
task_9999_ 前缀不写胶囊事件（#483 噪声分流纪律）。
"""
import sys
import tempfile
import unittest
from pathlib import Path

SCRIPT_DIR = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(SCRIPT_DIR))

import queue_gate as qg
import queue_transition as qt


def _mk_queue_file(path: Path, rows: list[tuple[str, str, str, str]]) -> None:
    """写一个 parse_queue/update_queue_status 都认的临时队列文件。

    rows: [(task_id, name, status, assignee)]
    """
    lines = [
        "| # | 任务 | 名称 | 状态 | 承担 |",
        "|:---:|:---:|:---:|:---:|:---:|",
    ]
    for i, (tid, name, status, assignee) in enumerate(rows, 1):
        lines.append(f"| {i} | `{tid}` | {name} | {status} | {assignee} |")
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")


class TestReworkReclaimGate(unittest.TestCase):
    """can_claim：rework:true 豁免 #504 own-pending，其余阻塞语义不动。"""

    def setUp(self):
        self._old_tasks_dir = qg.TASKS_DIR
        self._tmp = tempfile.TemporaryDirectory()
        qg.TASKS_DIR = Path(self._tmp.name)

    def tearDown(self):
        qg.TASKS_DIR = self._old_tasks_dir
        self._tmp.cleanup()

    def _mk_task_sheet(self, task_id: str, rework: bool) -> None:
        flag = "rework: true\n" if rework else ""
        (qg.TASKS_DIR / f"{task_id}.md").write_text(
            f"---\nid: 9999\n{flag}status: queued\n---\n# t\n", encoding="utf-8")

    def _rows(self, statuses):
        """构造队列行：[(task_id, status, assignee)]，按队列顺序。"""
        return [{"seq": str(i), "task_id": tid, "name": "n", "status": s,
                 "assignee": a, "raw": f"| {i} | `{tid}` | n | {s} | {a} |"}
                for i, (tid, s, a) in enumerate(statuses)]

    def test_rework_claim_bypasses_own_pending(self):
        """场景1：own pending 在前（#575→#578 FIFO 陷阱）+ rework:true → 无 force 可领。"""
        tid = "task_9999_rework_reclaim"
        self._mk_task_sheet(tid, rework=True)
        rows = self._rows([
            ("task_9999_own_pending", "pending_review", "laowantong"),
            (tid, "queued", "laowantong"),
        ])
        ok, reason = qg.can_claim(tid, rows, "laowantong")
        self.assertTrue(ok, reason)

    def test_normal_new_task_still_blocked(self):
        """场景2：own pending + 普通新单（无 rework 标）→ #504 照拦。"""
        tid = "task_9999_new_work"
        self._mk_task_sheet(tid, rework=False)
        rows = self._rows([
            ("task_9999_own_pending", "pending_review", "laowantong"),
            (tid, "queued", "laowantong"),
        ])
        ok, reason = qg.can_claim(tid, rows, "laowantong")
        self.assertFalse(ok)
        self.assertIn("#504", reason)
        self.assertIn("task_9999_own_pending", reason)

    def test_rework_foreign_pending_still_blocks(self):
        """边界：rework 单前方有他人 pending → FIFO 阻塞不豁免。"""
        tid = "task_9999_rework_foreign"
        self._mk_task_sheet(tid, rework=True)
        rows = self._rows([
            ("task_9999_foreign_pending", "pending_review", "wangyuyan"),
            ("task_9999_own_pending", "pending_review", "laowantong"),
            (tid, "queued", "laowantong"),
        ])
        ok, reason = qg.can_claim(tid, rows, "laowantong")
        self.assertFalse(ok, reason)
        self.assertIn("队列前方", reason)
        self.assertIn("task_9999_foreign_pending", reason)
        self.assertNotIn("task_9999_own_pending", reason.split("：")[1] if "：" in reason else reason)

    def test_rework_claimed_lock_unchanged(self):
        """边界：#503 同执行者 claimed 锁——rework 不豁免（同时最多一个 in_progress）。"""
        tid = "task_9999_rework_claimed"
        self._mk_task_sheet(tid, rework=True)
        rows = self._rows([
            (tid, "queued", "laowantong"),
            ("task_9999_in_progress", "claimed-laowantong", "laowantong"),
        ])
        ok, reason = qg.can_claim(tid, rows, "laowantong")
        self.assertFalse(ok)
        self.assertIn("claimed 任务未释放", reason)

    def test_rework_no_own_pending_claimable(self):
        """rework 标在无 own pending 时不改变结果（可领照旧可领）。"""
        tid = "task_9999_rework_clean"
        self._mk_task_sheet(tid, rework=True)
        rows = self._rows([(tid, "queued", "laowantong")])
        ok, reason = qg.can_claim(tid, rows, "laowantong")
        self.assertTrue(ok, reason)

    def test_is_rework_task_variants(self):
        """_is_rework_task：true/false/缺文件/大小写。"""
        self._mk_task_sheet("task_9999_rw_yes", rework=True)
        self._mk_task_sheet("task_9999_rw_no", rework=False)
        self.assertTrue(qg._is_rework_task("task_9999_rw_yes"))
        self.assertFalse(qg._is_rework_task("task_9999_rw_no"))
        self.assertFalse(qg._is_rework_task("task_9999_rw_missing"))
        (qg.TASKS_DIR / "task_9999_rw_upper.md").write_text(
            "---\nrework: True\n---\n", encoding="utf-8")
        self.assertTrue(qg._is_rework_task("task_9999_rw_upper"))


class _NullLock:
    def __init__(self, *a): pass
    def __enter__(self): return self
    def __exit__(self, *a): return False


class TestReworkFlagOnFail(unittest.TestCase):
    """FAIL 打回自动打标：review fail / #538 override → frontmatter rework: true。"""

    REVIEW_SECTION = (
        "\n## 终审记录\n\n"
        "结论：交付物未达验收标准，核心逻辑存在缺陷，**存在性核查**已附证据清单，"
        "退回返工。以上意见超过五十字，构成有效审查意见书。\n")

    def setUp(self):
        self._olds = (qt.parse_queue, qt.find_task, qt._find_task_file_dual,
                      qt.QUEUE_PATH, qt.FORCE_LEDGER, qt._check_review_authority,
                      qt.QueueLock)
        self._old_tasks_dir = qg.TASKS_DIR
        self._tmp = tempfile.TemporaryDirectory()
        td = Path(self._tmp.name)
        self.td = td
        qg.TASKS_DIR = td  # can_claim 侧 _is_rework_task 读同一临时目录（端到端用例）
        self.qf = td / "queue.md"
        self.tf = td / "task_9999_rw_fail.md"
        self.ledger = td / "force-exceptions.log"
        qt.QUEUE_PATH = self.qf
        qt.FORCE_LEDGER = self.ledger
        qt._check_review_authority = lambda *a, **k: (True, "")
        qt.QueueLock = _NullLock

    def tearDown(self):
        (qt.parse_queue, qt.find_task, qt._find_task_file_dual,
         qt.QUEUE_PATH, qt.FORCE_LEDGER, qt._check_review_authority,
         qt.QueueLock) = self._olds
        qg.TASKS_DIR = self._old_tasks_dir
        self._tmp.cleanup()

    def _setup_pending_review(self):
        """pending_review 任务 + 真身 apply_updates 可写的临时队列表格。"""
        _mk_queue_file(self.qf, [("task_9999_rw_fail", "n", "pending_review", "laowantong")])
        self.tf.write_text(
            "---\nid: 9999\nassignee: laowantong\nstatus: pending_review\n---\n"
            "# t\n" + self.REVIEW_SECTION, encoding="utf-8")
        rows = qg.parse_queue(self.qf)
        qt.parse_queue = lambda: rows
        qt.find_task = lambda tid, r=None: next(
            (x for x in rows if x["task_id"] == tid), None)
        qt._find_task_file_dual = lambda tid: self.tf

    def test_review_fail_sets_rework_flag(self):
        """verdict=fail → 状态回 queued + frontmatter rework: true。"""
        self._setup_pending_review()
        try:
            ok, msg = qt.action_review("task_9999_rw_fail", "fail", "欧阳锋")
        finally:
            pass
        self._restore_rows_after_fail()
        self.assertTrue(ok, msg)
        self.assertIn("已自动标 rework:true", msg)
        fm, _ = qt.parse_frontmatter(self.tf)
        self.assertTrue(fm.get("rework") is True)
        self.assertEqual(fm.get("status"), "queued")

    def _restore_rows_after_fail(self):
        """FAIL 后队列行状态已被真身 apply_updates 改写，重读保持沙盒一致。"""
        rows = qg.parse_queue(self.qf)
        qt.parse_queue = lambda: rows
        qt.find_task = lambda tid, r=None: next(
            (x for x in rows if x["task_id"] == tid), None)

    def test_review_fail_then_claim_free(self):
        """端到端：FAIL 打回打标 → can_claim 豁免 own-pending（#580 主场景闭环）。"""
        self._setup_pending_review()
        ok, msg = qt.action_review("task_9999_rw_fail", "fail", "欧阳锋")
        self.assertTrue(ok, msg)
        # 打回后任务回 queued（真身写入队列文件）
        rows = qg.parse_queue(self.qf)
        self.assertEqual(rows[0]["status"], "queued")
        # 模拟 own pending 复活（另一单提审）后返工重提——rework 豁免生效
        self._mk_task_sheet_write_rework()
        gate_rows = self._gate_rows()
        ok2, reason2 = qg.can_claim("task_9999_rw_fail", gate_rows, "laowantong",
                                    )
        self.assertTrue(ok2, reason2)

    def _mk_task_sheet_write_rework(self):
        """端到端场景的第二张 own pending 单（pending_review）。"""
        other = self.td / "task_9999_rw_other.md"
        other.write_text("---\nid: 9998\nstatus: queued\n---\n# t\n", encoding="utf-8")

    def _gate_rows(self):
        return [
            {"seq": "1", "task_id": "task_9999_rw_other", "name": "n",
             "status": "pending_review", "assignee": "laowantong",
             "raw": "| 1 | `task_9999_rw_other` | n | pending_review | laowantong |"},
            {"seq": "2", "task_id": "task_9999_rw_fail", "name": "n",
             "status": "queued", "assignee": "laowantong",
             "raw": "| 2 | `task_9999_rw_fail` | n | queued | laowantong |"},
        ]

    def test_review_pass_no_rework_flag(self):
        """PASS → reviewed，不打 rework 标（标记只属 FAIL 打回）。"""
        self._setup_pending_review()
        ok, msg = qt.action_review("task_9999_rw_fail", "pass", "欧阳锋", grade="A")
        self.assertTrue(ok, msg)
        fm, _ = qt.parse_frontmatter(self.tf)
        self.assertNotIn("rework", fm)
        self.assertEqual(fm.get("status"), "reviewed")

    def test_override_sets_rework_flag(self):
        """#538 改判（reviewed→queued）→ 同样打 rework:true。"""
        _mk_queue_file(self.qf, [("task_9999_rw_fail", "n", "reviewed", "laowantong")])
        self.tf.write_text(
            "---\nid: 9999\nassignee: laowantong\nstatus: reviewed\ngrade: A\n---\n# t\n",
            encoding="utf-8")
        rows = qg.parse_queue(self.qf)
        qt.parse_queue = lambda: rows
        qt.find_task = lambda tid, r=None: next(
            (x for x in rows if x["task_id"] == tid), None)
        qt._find_task_file_dual = lambda tid: self.tf
        ok, msg = qt.action_review("task_9999_rw_fail", "fail", "欧阳锋",
                                   override=True, reason="实跑发现返工漏洞")
        self.assertTrue(ok, msg)
        fm, body = qt.parse_frontmatter(self.tf)
        self.assertTrue(fm.get("rework") is True)
        self.assertEqual(fm.get("status"), "queued")
        self.assertIn("## 改判记录", body)


if __name__ == "__main__":
    unittest.main()
