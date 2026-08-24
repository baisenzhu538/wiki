"""Regression tests for queue_transition.py task file lookup."""
import sys
import tempfile
import unittest
from pathlib import Path

SCRIPT_DIR = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(SCRIPT_DIR))

import queue_gate as qg  # #492：can_claim batch 豁免测试
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
            old_q = queue_transition.QUEUE_PATH
            queue_transition.QUEUE_PATH = qpath

            try:
                _review_board_update(register={
                    "seq": "411",
                    "task_id": "task_20260822_laowantong-related-asymmetry-backfill",
                    "assignee": "hermes",
                    "task_file": "f.md",
                })
            finally:
                queue_transition.QUEUE_PATH = old_q  # 恢复——否则污染后续测试（2026-08-23 #461 全量污染实证）
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
            orig_capsule = qt._capsule_event  # #511：测试隔离——台账测试不写真实胶囊事件库
            qt.FORCE_LEDGER = ledger
            qt._capsule_event = lambda *a: None
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
                qt._capsule_event = orig_capsule

    def test_role_of_instance_mapping(self):
        """#444 口径 + #503 修正：hermes→laowantong（专属实例）；kimi 多角色共用不再反推（回退同形）。"""
        self.assertEqual(qt._role_of("hermes"), "laowantong")
        self.assertEqual(qt._role_of("kimi"), "kimi")  # #503：kimi=王语嫣/欧阳锋/老顽童共用，不可反推
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


# ── #457 处置类门禁结构化回归（显式标记优先 + 关键词限定范围降级）──

class TestDisposalGateStructured(unittest.TestCase):
    """#457：disposal:true 硬门禁 + 关键词限定范围提示（#189/#454 误判根治）。"""

    def _task(self, tmp, body="", disposal=None, title="测试任务"):
        fm = f"---\nid: 9999\nassignee: huangyaoshi\nstatus: queued\ntitle: {title}\n"
        if disposal is not None:
            fm += f"disposal: {str(disposal).lower()}\n"
        fp = tmp / "task_9999_test.md"
        fp.write_text(fm + "---\n# 测试\n" + body, encoding="utf-8")
        return fp

    def test_189_misjudgment_pass(self):
        """#189 误判场景：处置词只出现在正文叙述（"术语清理"不在动作/目标节）→ 放行零提示。"""
        with tempfile.TemporaryDirectory() as d:
            fp = self._task(Path(d), body="## 动作\n按新口径重写卡片。\n## 任务目标\n完成重写。\n## 背景\n术语清理由旧口径迁移完成。")
            ok, msg = qt._check_disposal_gate(fp, {"title": "测试任务"}, "task_9999_test")
        self.assertTrue(ok)
        self.assertEqual(msg, "")  # "清理"在背景叙述 → 零提示

    def test_454_keyword_in_body_only_pass(self):
        """#454 同款：关键词只在独立背景节（"已废弃"），动作节干净 → 放行。"""
        with tempfile.TemporaryDirectory() as d:
            fp = self._task(Path(d), body="## 动作\n核对相关卡片并更新。\n## 背景\n旧方案已废弃。")
            ok, msg = qt._check_disposal_gate(fp, {"title": "测试"}, "task_9999_test")
        self.assertTrue(ok)
        self.assertEqual(msg, "")

    def test_marked_disposal_requires_judgement(self):
        """正测：disposal:true 无内容价值判断节 → 硬拦。"""
        with tempfile.TemporaryDirectory() as d:
            fp = self._task(Path(d), body="## 动作\n删除素材文件 A。", disposal=True)
            ok, msg = qt._check_disposal_gate(fp, {"title": "测试", "disposal": True}, "task_9999_test")
        self.assertFalse(ok)
        self.assertIn("内容价值判断", msg)

    def test_marked_disposal_with_judgement_pass(self):
        """正测：disposal:true + 内容价值判断节 → 通过 + 确认清单。"""
        with tempfile.TemporaryDirectory() as d:
            fp = self._task(Path(d), body="## 动作\n删除素材文件 A。\n## 内容价值判断\n已通读内容，删除逐件老朱亲批。")
            ok, msg = qt._check_disposal_gate(fp, {"title": "测试", "disposal": True}, "task_9999_test")
        self.assertTrue(ok)
        self.assertIn("已领取", msg)

    def test_unmarked_real_disposal_warns(self):
        """未标记真处置：动作节含处置词 → 提示不硬拦，引导补标记。"""
        with tempfile.TemporaryDirectory() as d:
            fp = self._task(Path(d), body="## 动作\n删除 3 个素材文件并归档。")
            ok, msg = qt._check_disposal_gate(fp, {"title": "测试"}, "task_9999_test")
        self.assertTrue(ok)  # 不硬拦
        self.assertIn("疑似处置未标记", msg)  # 提示引导补 disposal:true


# ── #461 cancel 命令回归（queued 单取消/被取代终态）──

class TestCancelCommand(unittest.TestCase):
    """#461：queued 可 cancel / reason 必填 / cancelled 后 claim 拒 / 非 queued 拒。
    函数级 mock（parse_queue 默认参数在 queue_gate 定义时绑定，改模块属性无效——#444 同坑）。"""

    def _mock(self, status):
        self._tmpdir = Path(tempfile.mkdtemp())
        self._task_fp = self._tmpdir / "task_cancel_test.md"
        self._task_fp.write_text("---\nid: 9999\nassignee: huangyaoshi\nstatus: queued\n---\n# t\n", encoding="utf-8")
        # apply_updates 里 backup(QUEUE_PATH) 读队列文件——mock 一个真实存在的临时队列
        self._queue_fp = self._tmpdir / "production-queue.md"
        self._queue_fp.write_text("# 队列\n", encoding="utf-8")
        self._rows = [{
            "seq": "9999", "task_id": "task_cancel_test", "name": "测试",
            "status": status, "assignee": "huangyaoshi", "raw": "",
        }]
        self._olds = (qt.parse_queue, qt.find_task, qt._find_task_file_dual, qt.update_queue_status, qt.QUEUE_PATH)
        qt.parse_queue = lambda: self._rows
        qt.find_task = lambda tid, rows=None: (self._rows[0] if tid == "task_cancel_test" else None)
        qt._find_task_file_dual = lambda tid: self._task_fp
        qt.update_queue_status = lambda tid, st: None  # 不写真实队列文件（隔离）
        qt.QUEUE_PATH = self._queue_fp

    def _restore(self):
        qt.parse_queue, qt.find_task, qt._find_task_file_dual, qt.update_queue_status, qt.QUEUE_PATH = self._olds

    def test_reason_required(self):
        self._mock("queued")
        try:
            ok, msg = qt.action_cancel("task_cancel_test", "huangyaoshi", None)
        finally:
            self._restore()
        self.assertFalse(ok)
        self.assertIn("--reason", msg)

    def test_queued_cancel_success(self):
        self._mock("queued")
        try:
            ok, msg = qt.action_cancel("task_cancel_test", "huangyaoshi", "被 #999 取代")
        finally:
            self._restore()
        self.assertTrue(ok)
        self.assertIn("cancelled", msg)

    def test_non_queued_rejected(self):
        self._mock("pending_review")
        try:
            ok, msg = qt.action_cancel("task_cancel_test", "huangyaoshi", "test")
        finally:
            self._restore()
        self.assertFalse(ok)
        self.assertIn("仅 queued", msg)

    def test_cancelled_not_claimable(self):
        """cancelled 后 claim → 报「已取消」非「不存在」（can_claim 显式传 rows）。"""
        self._mock("cancelled")
        try:
            from queue_gate import can_claim
            ok, msg = can_claim("task_cancel_test", self._rows, "huangyaoshi")
        finally:
            self._restore()
        self.assertFalse(ok)
        self.assertIn("已取消", msg)


class TestGateBlockedNoiseFilter(unittest.TestCase):
    """#483：gate-blocked.log 测试噪声分流——task_9999_* 走独立 test log，
    真实拦截不受影响（防第五探针误报王语嫣）。"""

    def setUp(self):
        import tempfile
        self.tmp = Path(tempfile.mkdtemp())
        self._orig = (qt.GATE_BLOCKED_LOG, qt.GATE_BLOCKED_TEST_LOG)
        qt.GATE_BLOCKED_LOG = self.tmp / "gate-blocked.log"
        qt.GATE_BLOCKED_TEST_LOG = self.tmp / "gate-blocked-test.log"

    def tearDown(self):
        import shutil
        qt.GATE_BLOCKED_LOG, qt.GATE_BLOCKED_TEST_LOG = self._orig
        shutil.rmtree(self.tmp, ignore_errors=True)

    def test_test_task_goes_to_test_log(self):
        qt._log_gate_blocked("task_9999_force-test", "F-034-force无理由", "无 reason")
        self.assertFalse(qt.GATE_BLOCKED_LOG.exists())  # 真实日志零污染
        self.assertTrue(qt.GATE_BLOCKED_TEST_LOG.exists())
        self.assertIn("task_9999_force-test", qt.GATE_BLOCKED_TEST_LOG.read_text(encoding="utf-8"))

    def test_real_task_stays_in_real_log(self):
        qt._log_gate_blocked("task_20260823_huangyaoshi-x", "F-034-五字段", "缺字段", "huangyaoshi")
        self.assertTrue(qt.GATE_BLOCKED_LOG.exists())
        self.assertIn("task_20260823_huangyaoshi-x", qt.GATE_BLOCKED_LOG.read_text(encoding="utf-8"))
        self.assertFalse(qt.GATE_BLOCKED_TEST_LOG.exists())

    def test_test_record_preserved_not_dropped(self):
        """边界：测试件记录保留（E028 测试覆盖历史），只是换文件不丢弃。"""
        qt._log_gate_blocked("task_9999_test", "处置-硬门禁", "缺内容价值判断节")
        self.assertIn("task_9999_test", qt.GATE_BLOCKED_TEST_LOG.read_text(encoding="utf-8"))


class TestBatchBlockingExemption(unittest.TestCase):
    """#492（F-050 方案一）：batch:true 任务 pending_review 不阻塞前方；非 batch 仍阻塞。"""

    def _rows(self, statuses):
        """构造队列行：[(seq, task_id, status, assignee)]。"""
        return [{"seq": str(seq), "task_id": tid, "name": n, "status": s,
                 "assignee": a, "raw": f"| {seq} | `{tid}` | {n} | {s} | {a} |"}
                for seq, (tid, n, s, a) in enumerate(statuses)]

    def test_batch_pending_not_blocking(self):
        # 前方 #426(batch:true, pending_review) + 后方任务 queued → 可领
        rows = self._rows([
            ("task_20260822_laowantong-tags-judgment-batch", "批次", "pending_review", "laowantong"),
            ("task_20260824_laowantong-oral-spray", "主线", "queued", "laowantong"),
        ])
        ok, _ = qg.can_claim("task_20260824_laowantong-oral-spray", rows, "laowantong")
        self.assertTrue(ok)

    def test_normal_pending_still_blocking(self):
        # 前方非 batch pending_review → 仍阻塞
        rows = self._rows([
            ("task_normal_pending", "整单", "pending_review", "laowantong"),
            ("task_behind", "主线", "queued", "laowantong"),
        ])
        ok, _ = qg.can_claim("task_behind", rows, "laowantong")
        self.assertFalse(ok)

    def test_real_426_is_batch(self):
        # #426 已加 batch:true（实证）
        self.assertTrue(qg._is_batch_task("task_20260822_laowantong-tags-judgment-batch"))

    def test_normal_task_not_batch(self):
        self.assertFalse(qg._is_batch_task("task_20260823_huangyaoshi-role-routes"))


class TestIssueDispositionGate(unittest.TestCase):
    """F-036 问题落点门禁（用户拍板方案 C）：审查发现问题必须给落点。"""

    def test_orange_without_disposition_blocked(self):
        opinion = "**发现问题**：\n- 🟠 全库数字两次运行微差——需确认扫描器判定\n"
        ok, msg = qt._check_issue_disposition(opinion)
        self.assertFalse(ok)
        self.assertIn("F-036", msg)

    def test_orange_with_disposition_passed(self):
        opinion = "**发现问题**：\n- 🟠 微差待校准——另立项（#474 校准响应）\n"
        ok, _ = qt._check_issue_disposition(opinion)
        self.assertTrue(ok)

    def test_blue_only_passed(self):
        opinion = "**发现问题**：🔵 无实质缺陷——观察项\n"
        ok, _ = qt._check_issue_disposition(opinion)
        self.assertTrue(ok)

    def test_yellow_with_f_parking_passed(self):
        opinion = "**发现问题**：\n- 🟡 观察项——登记停车场 F-048\n"
        ok, _ = qt._check_issue_disposition(opinion)
        self.assertTrue(ok)

    def test_no_issue_section_passed(self):
        ok, _ = qt._check_issue_disposition("**结论**：PASS / A-\n")
        self.assertTrue(ok)


# ── #503 claim 口径族根治回归（claim 保持 assignee 原值 + claimed 锁匹配洞A）──

class TestClaimAssigneePreserved(unittest.TestCase):
    """#503：claim 不按 instance 反推覆盖 assignee——只写 status + instance。"""

    def _setup(self, assignee):
        self._tmpdir = Path(tempfile.mkdtemp())
        self._task_fp = self._tmpdir / "task_9999_503test.md"
        self._task_fp.write_text(
            f"---\nid: 9999\nassignee: {assignee}\nstatus: queued\n---\n# t\n",
            encoding="utf-8")
        self._queue_fp = self._tmpdir / "production-queue.md"
        self._queue_fp.write_text("# 队列\n", encoding="utf-8")
        self._rows = [{
            "seq": "9999", "task_id": "task_9999_503test", "name": "测试",
            "status": "queued", "assignee": assignee, "raw": "",
        }]
        self._olds = (qt.parse_queue, qt.find_task, qt._find_task_file_dual,
                      qt.update_queue_status, qt.QUEUE_PATH)
        qt.parse_queue = lambda: self._rows
        qt.find_task = lambda tid, rows=None: (
            self._rows[0] if tid == "task_9999_503test" else None)
        qt._find_task_file_dual = lambda tid: self._task_fp
        qt.update_queue_status = lambda tid, st: None
        qt.QUEUE_PATH = self._queue_fp

    def _teardown(self):
        (qt.parse_queue, qt.find_task, qt._find_task_file_dual,
         qt.update_queue_status, qt.QUEUE_PATH) = self._olds

    def _fm(self):
        fm, _ = qt.parse_frontmatter(self._task_fp)
        return fm.get("assignee"), fm.get("instance"), fm.get("status")

    def test_kimi_claim_keeps_wangyuyan(self):
        """#497 实证场景：王语嫣(kimi) claim 王语嫣单 → assignee 保持 wangyuyan，instance 记 kimi。"""
        self._setup("wangyuyan")
        try:
            ok, msg = qt.action_claim("task_9999_503test", "kimi")
        finally:
            self._teardown()
        self.assertTrue(ok, msg)
        assignee, instance, status = self._fm()
        self.assertEqual(assignee, "wangyuyan")
        self.assertEqual(instance, "kimi")
        self.assertEqual(status, "in_progress")

    def test_hermes_claim_keeps_laowantong(self):
        """老顽童(hermes) claim 老顽童单 → assignee 保持 laowantong，instance 记 hermes。"""
        self._setup("laowantong")
        try:
            ok, msg = qt.action_claim("task_9999_503test", "hermes")
        finally:
            self._teardown()
        self.assertTrue(ok, msg)
        assignee, instance, status = self._fm()
        self.assertEqual(assignee, "laowantong")
        self.assertEqual(instance, "hermes")

    def test_cross_role_claim_keeps_original_assignee(self):
        """跨角色 claim：assignee 保持任务单原值（不被执行实例反推覆盖）。"""
        self._setup("wangyuyan")
        try:
            ok, msg = qt.action_claim("task_9999_503test", "huangyaoshi")
        finally:
            self._teardown()
        self.assertTrue(ok, msg)
        assignee, instance, _ = self._fm()
        self.assertEqual(assignee, "wangyuyan")
        self.assertEqual(instance, "huangyaoshi")


class TestClaimedLockMatching(unittest.TestCase):
    """#503 洞A：同一执行者（同实例或同角色）已有 claimed → 阻塞；不同角色不阻塞。"""

    def _rows(self, entries):
        return [{"seq": str(i), "task_id": tid, "name": "n", "status": s,
                 "assignee": a, "raw": f"| {i} | `{tid}` | n | {s} | {a} |"}
                for i, (tid, s, a) in enumerate(entries)]

    def test_same_role_blocks_multi_instance(self):
        """洞A 实证场景：kimi 已 claim 老顽童单 → hermes 再 claim 另一张老顽童单被拒。"""
        rows = self._rows([
            ("task_a", "claimed-kimi", "laowantong"),
            ("task_b", "queued", "laowantong"),
        ])
        ok, msg = qg.can_claim("task_b", rows, "hermes")
        self.assertFalse(ok)
        self.assertIn("task_a", msg)

    def test_same_instance_blocks(self):
        """同实例：claimed-hermes 在前 → hermes 再 claim 被拒（旧子串匹配失效点）。"""
        rows = self._rows([
            ("task_a", "claimed-hermes", "laowantong"),
            ("task_b", "queued", "laowantong"),
        ])
        ok, msg = qg.can_claim("task_b", rows, "hermes")
        self.assertFalse(ok)
        self.assertIn("task_a", msg)

    def test_different_role_not_blocked(self):
        """不同角色的 claimed 不阻塞：王语嫣单 claimed-kimi → 黄药师 claim 黄药师单放行。"""
        rows = self._rows([
            ("task_a", "claimed-kimi", "wangyuyan"),
            ("task_b", "queued", "huangyaoshi"),
        ])
        ok, msg = qg.can_claim("task_b", rows, "huangyaoshi")
        self.assertTrue(ok, msg)

    def test_legacy_instance_name_assignee_still_blocks(self):
        """存量兼容：claimed 行 assignee 是旧实例名（未回改）→ status 前缀维度仍拦住同实例。"""
        rows = self._rows([
            ("task_a", "claimed-hermes", "hermes"),
            ("task_b", "queued", "laowantong"),
        ])
        ok, msg = qg.can_claim("task_b", rows, "hermes")
        self.assertFalse(ok)
        self.assertIn("task_a", msg)


# ── #504 审查等待期占位阻塞回归（pending_review 占执行者位 + force 留痕）──

class TestReviewWaitBlock(unittest.TestCase):
    """#504：同执行者已有 pending_review（不论队列前后）→ 阻塞 claim 新任务；
    batch:true 豁免（#492 语义不变）；--force 放行但留痕（例外不得无痕）。"""

    def _rows(self, entries):
        return [{"seq": str(i), "task_id": tid, "name": "n", "status": s,
                 "assignee": a, "raw": f"| {i} | `{tid}` | n | {s} | {a} |"}
                for i, (tid, s, a) in enumerate(entries)]

    def test_own_pending_review_blocks_claim(self):
        """场景①：自己已有 pending_review（队列后方）→ claim 前方新单被拒，提示等欧阳锋终审。"""
        rows = self._rows([
            ("task_new_front", "queued", "huangyaoshi"),
            ("task_own_pending", "pending_review", "huangyaoshi"),
        ])
        ok, msg = qg.can_claim("task_new_front", rows, "huangyaoshi")
        self.assertFalse(ok)
        self.assertIn("待欧阳锋终审", msg)
        self.assertIn("task_own_pending", msg)

    def test_other_role_pending_keeps_generic_message(self):
        """他人 pending_review 仍按原口径阻塞（队列整体等待终审），消息不冒充"自己"。"""
        rows = self._rows([
            ("task_other_pending", "pending_review", "laowantong"),
            ("task_mine", "queued", "huangyaoshi"),
        ])
        ok, msg = qg.can_claim("task_mine", rows, "huangyaoshi")
        self.assertFalse(ok)
        self.assertIn("pending_review", msg)
        self.assertNotIn("待欧阳锋终审：", msg.replace("任务待欧阳锋终审", ""))

    def test_batch_pending_exempt_even_same_role(self):
        """场景②：batch:true 任务（#426 真实单）pending_review → 同角色也不阻塞（#492 语义不变）。"""
        rows = self._rows([
            ("task_20260822_laowantong-tags-judgment-batch", "pending_review", "laowantong"),
            ("task_main", "queued", "laowantong"),
        ])
        ok, msg = qg.can_claim("task_main", rows, "hermes")
        self.assertTrue(ok, msg)


class TestForceClaimLedger(unittest.TestCase):
    """#504 场景③：claim --force 放行保留，但绕过阻塞必须写 force-exceptions.log 台账。"""

    def _setup(self, rows):
        self._tmpdir = Path(tempfile.mkdtemp())
        self._task_fp = self._tmpdir / "task_9999_504test.md"
        self._task_fp.write_text(
            "---\nid: 9999\nassignee: huangyaoshi\nstatus: queued\n---\n# t\n",
            encoding="utf-8")
        self._queue_fp = self._tmpdir / "production-queue.md"
        self._queue_fp.write_text("# 队列\n", encoding="utf-8")
        self._ledger = self._tmpdir / "force-exceptions.log"
        self._rows = rows
        self._olds = (qt.parse_queue, qt.find_task, qt._find_task_file_dual,
                      qt.update_queue_status, qt.QUEUE_PATH, qt.FORCE_LEDGER)
        qt.parse_queue = lambda: self._rows
        qt.find_task = lambda tid, rows=None: (
            next((r for r in self._rows if r["task_id"] == tid), None))
        qt._find_task_file_dual = lambda tid: self._task_fp
        qt.update_queue_status = lambda tid, st: None
        qt.QUEUE_PATH = self._queue_fp
        qt.FORCE_LEDGER = self._ledger

    def _teardown(self):
        (qt.parse_queue, qt.find_task, qt._find_task_file_dual,
         qt.update_queue_status, qt.QUEUE_PATH, qt.FORCE_LEDGER) = self._olds

    def _mkrows(self, entries):
        return [{"seq": str(i), "task_id": tid, "name": "n", "status": s,
                 "assignee": a, "raw": f"| {i} | `{tid}` | n | {s} | {a} |"}
                for i, (tid, s, a) in enumerate(entries)]

    def test_force_bypass_logged(self):
        """force 绕过 pending_review 阻塞 → 放行 + 台账留痕（绕过原因写入）。"""
        rows = self._mkrows([
            ("task_9999_504test", "queued", "huangyaoshi"),
            ("task_pending", "pending_review", "huangyaoshi"),
        ])
        self._setup(rows)
        try:
            ok, msg = qt.action_claim("task_9999_504test", "huangyaoshi", force=True)
        finally:
            self._teardown()
        self.assertTrue(ok, msg)
        self.assertIn("留痕", msg)
        line = self._ledger.read_text(encoding="utf-8")
        self.assertIn("task_9999_504test", line)
        self.assertIn("pending_review 阻塞", line)
        self.assertIn("huangyaoshi", line)

    def test_force_without_blocker_not_logged(self):
        """无可绕过的阻塞时 force 不留痕（台账不制造噪声）。"""
        rows = self._mkrows([
            ("task_9999_504test", "queued", "huangyaoshi"),
        ])
        self._setup(rows)
        try:
            ok, msg = qt.action_claim("task_9999_504test", "huangyaoshi", force=True)
        finally:
            self._teardown()
        self.assertTrue(ok, msg)
        self.assertFalse(self._ledger.exists())
