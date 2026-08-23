"""Regression tests for queue_transition.py task file lookup."""
import sys
import tempfile
import unittest
from pathlib import Path

SCRIPT_DIR = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(SCRIPT_DIR))

import queue_transition as qt
from queue_transition import (
    find_task_file,
    find_task_file_by_frontmatter_id,
    _find_task_file_dual,
    ensure_task_workspace,
    TASK_DIR,
    BATCH_DIR,
)


class TestFindTaskFile(unittest.TestCase):

    def test_exact_filename_match_returns_correct_file(self):
        """When filename == task_id, exact match should return the file."""
        # Use a real task file from the wiki
        result = find_task_file("task_20260703_huangyaoshi-fix-queue-transition-review-lookup")
        self.assertIsNotNone(result)
        self.assertIn("task_20260703_huangyaoshi-fix-queue-transition-review-lookup", str(result))

    def test_missing_file_returns_none(self):
        """When no file matches, return None."""
        result = find_task_file("nonexistent_task_id_12345")
        self.assertIsNone(result)

    def test_frontmatter_id_match_finds_renamed_file(self):
        """When filename != task_id but frontmatter id matches, return the file."""
        # #55 scenario: queue id is laowantong-yitang-Y-model-os but
        # actual file is laowantong-agent-spec-yitang-Y-model-coach.md
        result = find_task_file_by_frontmatter_id(
            "task_20260703_laowantong-yitang-Y-model-os"
        )
        self.assertIsNotNone(result)
        self.assertIn("agent-spec-yitang-Y-model-coach", str(result))

    def test_dual_lookup_exact_preferred(self):
        """_find_task_file_dual should prefer exact filename match."""
        result = _find_task_file_dual(
            "task_20260703_huangyaoshi-fix-queue-transition-review-lookup"
        )
        self.assertIsNotNone(result)
        # exact match returns the file itself
        self.assertIn("fix-queue-transition-review-lookup", str(result))

    def test_dual_lookup_falls_back_to_frontmatter(self):
        """_find_task_file_dual should fall back to frontmatter when filename fails."""
        result = _find_task_file_dual(
            "task_20260703_laowantong-yitang-Y-model-os"
        )
        self.assertIsNotNone(result)
        self.assertIn("agent-spec-yitang-Y-model-coach", str(result))

    def test_dual_lookup_returns_none_when_both_fail(self):
        """When both filename and frontmatter fail, return None."""
        result = _find_task_file_dual("definitely_not_a_real_task_id_99999")
        self.assertIsNone(result)

    def test_no_prefix_side_effect(self):
        """Prefix of one task_id should NOT match a different task file."""
        # task_id[:40] = "task_20260703_laowantong-yitang-Y-model-"
        # This should NOT return foundation-production file as was the bug
        result = find_task_file("task_20260703_laowantong-yitang-Y-model-os")
        self.assertIsNone(result)  # filename exact match should fail
        # But frontmatter fallback should find the right one
        result2 = find_task_file_by_frontmatter_id("task_20260703_laowantong-yitang-Y-model-os")
        self.assertIsNotNone(result2)
        # And it should NOT be foundation-production
        self.assertNotIn("foundation-production", str(result2))


if __name__ == "__main__":
    unittest.main()


class TestEnsureTaskWorkspace(unittest.TestCase):
    """#402: claim 长程任务自动建 workspace（最小三件套）。"""

    def _task_file(self, tmp, long_running=True):
        fp = tmp / "task_9999_test-long-running.md"
        flag = "long_running: true\n" if long_running else ""
        fp.write_text(f"---\nid: 9999\nstatus: queued\n{flag}---\n# t\n", encoding="utf-8")
        return fp

    def test_long_running_creates_workspace(self):
        with tempfile.TemporaryDirectory() as d:
            tmp = Path(d)
            task_file = self._task_file(tmp)
            note = ensure_task_workspace("task_9999_test-long-running", task_file)
            ws = tmp / "task_9999_test-long-running-workspace"
            self.assertIsNotNone(note)
            self.assertTrue((ws / "in-progress").is_dir())
            self.assertTrue((ws / "excluded").is_dir())
            self.assertTrue((ws / "next-pointer.md").is_file())
            self.assertIn("workspace 已创建", note)

    def test_non_long_running_skips(self):
        with tempfile.TemporaryDirectory() as d:
            tmp = Path(d)
            task_file = self._task_file(tmp, long_running=False)
            note = ensure_task_workspace("task_9999_test-long-running", task_file)
            self.assertIsNone(note)
            self.assertFalse((tmp / "task_9999_test-long-running-workspace").exists())

    def test_existing_workspace_idempotent(self):
        with tempfile.TemporaryDirectory() as d:
            tmp = Path(d)
            task_file = self._task_file(tmp)
            ensure_task_workspace("task_9999_test-long-running", task_file)
            note2 = ensure_task_workspace("task_9999_test-long-running", task_file)
            self.assertIn("已存在", note2)
            # 不覆盖已有指针
            (tmp / "task_9999_test-long-running-workspace" / "next-pointer.md").write_text(
                "# 已有人写的内容\n", encoding="utf-8")
            ensure_task_workspace("task_9999_test-long-running", task_file)
            self.assertEqual(
                (tmp / "task_9999_test-long-running-workspace" / "next-pointer.md").read_text(encoding="utf-8"),
                "# 已有人写的内容\n",
            )


class TestReviewBoardBatchReregister(unittest.TestCase):
    """O-3 分批提审回归（#413 R3）：分批任务二次 complete 必须重新登记 REVIEW-PENDING

    幂等判断此前把"已划掉的行"也算已登记——分批任务第二次提审时段内已有划掉行
    （含 task_id）→ 不再登记 → 提审无声（#411 三批实证）。
    """

    def test_batch_reregister_after_strike(self):
        import tempfile
        from pathlib import Path
        from queue_transition import _review_board_update

        with tempfile.TemporaryDirectory() as d:
            tmp = Path(d)
            qpath = tmp / "production-queue.md"
            qpath.write_text(
                "---\nid: production-queue\ntype: queue\n---\n\n"
                "<!-- REVIEW-PENDING-BEGIN（queue_transition 自动维护，勿手改） -->\n\n"
                "## ⚖️ 待终审\n\n"
                "- ~~#411 task_20260822_laowantong-related-asymmetry-backfill｜hermes｜提审 08-22 11:38｜f.md~~ → 已终审 PASS A-\n\n"
                "<!-- REVIEW-PENDING-END -->\n",
                encoding="utf-8",
            )
            import queue_transition
            queue_transition.QUEUE_PATH = qpath

            _review_board_update(register={
                "seq": "411",
                "task_id": "task_20260822_laowantong-related-asymmetry-backfill",
                "assignee": "hermes",
                "task_file": "f.md",
            })
            text = qpath.read_text(encoding="utf-8")
            # 修复后：已划掉行不算已登记 → 应追加第二行未划掉的登记
            lines = [l for l in text.splitlines() if l.startswith("- ") and "task_20260822" in l]
            active = [l for l in lines if not l.startswith("- ~~")]
            self.assertEqual(len(active), 1, f"应重新登记一行未划掉的提审行，实际:\n{lines}")
            self.assertIn("提审", active[0])


# ── #429 流转留痕三件套门禁回归（F-034 交付五字段 / F-035 审查意见落盘 / F-029 waiting-external）──

class TestDeliveryFieldsGate(unittest.TestCase):
    """F-034：交付五字段机读检查。"""

    def _report(self, fields: set[str]) -> str:
        parts = ["## 执行报告\n"]
        if "清单" in fields:
            parts.append("**交付物**：a.py\n")
        if "内容" in fields:
            parts.append("**完成内容**：一句话\n")
        if "验证" in fields:
            parts.append("**验证**：pytest -q → 5 passed\n")
        if "边界" in fields:
            parts.append("**边界**：未动其它文件\n")
        if "动作" in fields:
            parts.append("**需要谁动作**：王语嫣复核\n")
        return "".join(parts)

    def test_full_fields_pass(self):
        fp = Path(__file__).parent / "_tmp_429_test.md"
        fp.write_text(self._report({"清单", "内容", "验证", "边界", "动作"}), encoding="utf-8")
        try:
            ok, msg = qt._check_delivery_fields(fp, None)
            self.assertTrue(ok, msg)
        finally:
            fp.unlink(missing_ok=True)

    def test_missing_field_blocked(self):
        fp = Path(__file__).parent / "_tmp_429_test.md"
        fp.write_text(self._report({"清单", "内容", "验证"}), encoding="utf-8")
        try:
            ok, msg = qt._check_delivery_fields(fp, None)
            self.assertFalse(ok)
            self.assertIn("未做项/边界", msg)
            self.assertIn("需要谁动作", msg)
        finally:
            fp.unlink(missing_ok=True)

    def test_no_exec_report_blocked(self):
        fp = Path(__file__).parent / "_tmp_429_test.md"
        fp.write_text("没有执行报告节\n", encoding="utf-8")
        try:
            ok, _ = qt._check_delivery_fields(fp, None)
            self.assertFalse(ok)
        finally:
            fp.unlink(missing_ok=True)


class TestReviewRecordGate(unittest.TestCase):
    """F-035：审查意见书强制落盘。"""

    def test_missing_review_section_blocked(self):
        fp = Path(__file__).parent / "_tmp_429_review.md"
        fp.write_text("## 概要\n无终审记录\n", encoding="utf-8")
        try:
            ok, msg = qt._check_review_record(fp, None)
            self.assertFalse(ok)
            self.assertIn("终审记录", msg)
        finally:
            fp.unlink(missing_ok=True)

    def test_review_section_present_pass(self):
        fp = Path(__file__).parent / "_tmp_429_review.md"
        fp.write_text("## 终审记录\n\n**结论**：PASS / A。O0 溯源逐条验证。验收标准逐条核对，魔鬼代言人无阻断项，残余风险已注明。\n", encoding="utf-8")
        try:
            ok, _ = qt._check_review_record(fp, None)
            self.assertTrue(ok)
        finally:
            fp.unlink(missing_ok=True)

    def test_review_file_alternative_pass(self):
        rf = Path(__file__).parent / "_tmp_429_reviewfile.md"
        rf.write_text("审查意见书：verdict PASS，grade A，溯源验证若干。\n" * 5, encoding="utf-8")
        fp = Path(__file__).parent / "_tmp_429_review.md"
        fp.write_text("无终审记录\n", encoding="utf-8")
        try:
            ok, _ = qt._check_review_record(fp, str(rf))
            self.assertTrue(ok)
        finally:
            rf.unlink(missing_ok=True)
            fp.unlink(missing_ok=True)


class TestWaitingExternal(unittest.TestCase):
    """F-029：waiting-external 状态机转移。"""

    def test_transitions_registered(self):
        self.assertEqual(qt.TRANSITIONS[("pending_review", "mark_waiting")], "waiting-external")
        self.assertEqual(qt.TRANSITIONS[("waiting-external", "resume")], "pending_review")


# ── #433 负向判词证据层门禁回归（风清扬建议书采纳，三复现用例）──

class TestNegativeClaimGate(unittest.TestCase):
    """#433：意见书负向断言词必须带 `**存在性核查**` 锚点。"""

    # 复现用例 1：#430 坚果云——"无远程备份"（未查云同步形态）
    def test_430_nutcloud_repro_blocked(self):
        text = "**结论**：PASS / A-。发现：无远程备份（本地单点容灾缺口）。"
        ok, msg = qt._check_negative_claims(text)
        self.assertFalse(ok)
        self.assertIn("存在性核查", msg)

    # 复现用例 2：FQ-E04——"卡住"（未标注证据层）
    def test_fqe04_blocked(self):
        text = "**结论**：欧阳锋卡住。"
        ok, _ = qt._check_negative_claims(text)
        self.assertFalse(ok)

    # 复现用例 3：FQ-E01——"待终审"（状态未拉最新=相邻型，非负向断言，门禁不误拦）
    def test_fqe01_not_blocked(self):
        text = "**结论**：#427 待终审。"
        ok, msg = qt._check_negative_claims(text)
        self.assertTrue(ok)
        self.assertEqual(msg, "")  # 相邻型不在负向门禁范围——证明不误拦

    def test_anchor_present_pass(self):
        text = ("**结论**：PASS / A-。无远程备份。\n\n**存在性核查**：\n"
                "- 查过形态：本地 git/坚果云/进程/配置——坚果云已同步（进程+配置+用户确认）\n"
                "- 结论等级：未发现（默认）")
        ok, _ = qt._check_negative_claims(text)
        self.assertTrue(ok)

    def test_common_phrase_no_block(self):
        """合法常见短语（无阻断项）不触发强词硬拦，仅宽词提示。"""
        text = "**结论**：PASS / A。无阻断项。"
        ok, msg = qt._check_negative_claims(text)
        self.assertTrue(ok)


# ── #435 词表扩展回归（数据异常类：为空/空值强词 + 截断/损坏正则 + 正向声明不误伤）──

class TestNegativeGateVocabData(unittest.TestCase):
    """#435：数据异常类词表扩展。"""

    def test_empty_value_blocked(self):
        """正测：'grade 为空'（#442 后走断言句式正则）→ 被拦。"""
        ok, msg = qt._check_negative_claims("**结论**：grade 为空。")
        self.assertFalse(ok)
        self.assertIn("为空", msg)

    def test_value_empty_blocked(self):
        """正测：'值为空'（无空格紧邻）→ 被拦。"""
        ok, msg = qt._check_negative_claims("**结论**：值为空。")
        self.assertFalse(ok)

    def test_not_empty_not_blocked(self):
        """#442 否定式反例：'字段不为空'正向声明 → 不误伤（STRONG 已删子串；正则主语不匹配）。"""
        ok, msg = qt._check_negative_claims("**结论**：字段不为空。")
        self.assertTrue(ok)
        self.assertEqual(msg, "")

    def test_non_empty_value_not_blocked(self):
        """#442 否定式反例：'非空值' → 不误伤。"""
        ok, msg = qt._check_negative_claims("**结论**：非空值已确认。")
        self.assertTrue(ok)
        self.assertEqual(msg, "")

    def test_data_damaged_pattern_blocked(self):
        """正测：'数据已损坏'（断言句式正则）→ 被拦。"""
        ok, msg = qt._check_negative_claims("**结论**：数据已损坏。")
        self.assertFalse(ok)
        self.assertIn("数据已损坏", msg)

    def test_positive_no_truncation_not_blocked(self):
        """反测：'无截断'正向声明 → 不硬拦（宽词仅提示）。"""
        ok, _ = qt._check_negative_claims("**结论**：全程无截断，完整读取。")
        self.assertTrue(ok)

    def test_positive_no_damage_not_blocked(self):
        """反测：'确认无损坏' → 正则不命中（无主语），仅宽词提示。"""
        ok, msg = qt._check_negative_claims("**结论**：确认无损坏。")
        self.assertTrue(ok)
        self.assertIn("需人工", msg)

    def test_with_anchor_pass(self):
        """反测：数据异常断言 + 核查锚点（含完整读取证据）→ 通过。"""
        text = ("**结论**：grade 为空。\n\n**存在性核查**：\n"
                "- 查过形态：完整读取 SQLite（非截断视图），grade 列确为空\n"
                "- 结论等级：确认缺失（全查过）")
        ok, _ = qt._check_negative_claims(text)
        self.assertTrue(ok)


class TestForceLedgerAndEvidenceGate(unittest.TestCase):
    """#444：--force 例外台账 + evidence 侧门封堵 + assignee 角色名口径。"""

    def _make_task_file(self, with_report: bool) -> Path:
        """构造临时任务单（含/不含五字段执行报告）。"""
        report = ("\n## 执行报告\n\n**完成内容**：测试交付。\n**交付物**：tmp 文件。\n"
                  "**验证**：pytest。\n**边界**：无。\n**需要谁动作**：欧阳锋终审。\n"
                  ) if with_report else ""
        content = ("---\nid: 444-test\nassignee: huangyaoshi\nstatus: in_progress\n---\n"
                   "# 测试任务单\n" + report)
        fd, name = tempfile.mkstemp(suffix=".md")
        import os as _os
        _os.close(fd)
        f = Path(name)
        f.write_text(content, encoding="utf-8")
        self.addCleanup(_os.unlink, name)
        return f

    def test_evidence_side_door_sealed(self):
        """#444 侧门封堵：任务单无执行报告时，evidence 指向含五字段锚点的外部文件也 FAIL。"""
        task = self._make_task_file(with_report=False)
        fd, evname = tempfile.mkstemp(suffix=".md")
        import os as _os
        _os.close(fd)
        ev = Path(evname)
        ev.write_text("**完成内容**：外部文件含全部锚点。**交付物**：x。**验证**：x。"
                      "**边界**：x。**需要谁动作**：x。", encoding="utf-8")
        self.addCleanup(_os.unlink, evname)
        ok, msg = qt._check_delivery_fields(task, str(ev))
        self.assertFalse(ok)
        self.assertIn("执行报告", msg)

    def test_exec_report_passes_without_evidence(self):
        """正测：任务单执行报告五字段齐全 → PASS（evidence 非必需）。"""
        task = self._make_task_file(with_report=True)
        ok, msg = qt._check_delivery_fields(task, None)
        self.assertTrue(ok)
        self.assertEqual(msg, "")

    def test_force_exception_ledger_written(self):
        """#444 台账：force 例外写入 force-exceptions.log（谁/何时/绕过哪条/为何）。"""
        with tempfile.TemporaryDirectory() as td:
            ledger = Path(td) / "force-exceptions.log"
            orig = qt.FORCE_LEDGER
            qt.FORCE_LEDGER = ledger
            try:
                path = qt._log_force_exception("task_test_444", "wangyuyan", "生产已完成未走领取")
                self.assertTrue(ledger.exists())
                line = ledger.read_text(encoding="utf-8")
                self.assertIn("task_test_444", line)
                self.assertIn("wangyuyan", line)
                self.assertIn("F-034", line)
                self.assertIn("生产已完成未走领取", line)
                self.assertEqual(path, str(ledger))
            finally:
                qt.FORCE_LEDGER = orig

    def test_role_of_instance_mapping(self):
        """#444 口径：instance→角色名映射（hermes/kimi→laowantong；其余同形）。"""
        self.assertEqual(qt._role_of("hermes"), "laowantong")
        self.assertEqual(qt._role_of("kimi"), "laowantong")
        self.assertEqual(qt._role_of("huangyaoshi"), "huangyaoshi")
        self.assertEqual(qt._role_of("wangyuyan"), "wangyuyan")
        self.assertEqual(qt._role_of("ouyangfeng"), "ouyangfeng")

    def test_force_complete_without_reason_rejected(self):
        """#444 核心用例：force complete 无 --reason → 拒绝（#441 后门根治）。
        FAIL 退回修复（欧阳锋）：monkeypatch 函数级隔离——构造 claimed 状态 rows + 临时任务单，
        不碰真实队列（状态漂移断言脆弱根治）。"""
        import os as _os
        with tempfile.TemporaryDirectory() as d:
            tmp = Path(d)
            task_file = tmp / "task_9999_force-test.md"
            task_file.write_text(
                "---\nid: 9999\nassignee: wangyuyan\nstatus: claimed\n---\n# 测试任务单\n",
                encoding="utf-8")
            fake_rows = [{
                "seq": "9999", "task_id": "task_9999_force-test", "name": "测试",
                "status": "claimed-wangyuyan", "assignee": "wangyuyan", "raw": "",
            }]
            old_pq, old_ft, old_fd = qt.parse_queue, qt.find_task, qt._find_task_file_dual
            try:
                qt.parse_queue = lambda: fake_rows
                qt.find_task = lambda tid, rows=None: (
                    fake_rows[0] if tid == "task_9999_force-test" else None)
                qt._find_task_file_dual = lambda tid: task_file
                ok, msg = qt.action_complete(
                    "task_9999_force-test", "wangyuyan", None, force=True, reason=None)
            finally:
                qt.parse_queue, qt.find_task, qt._find_task_file_dual = old_pq, old_ft, old_fd
        self.assertFalse(ok)
        self.assertIn("--reason", msg)
