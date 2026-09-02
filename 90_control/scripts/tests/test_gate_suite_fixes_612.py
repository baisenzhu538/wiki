"""#612 回归：门禁顺手套件双修。

任务1：F-036 落点门禁否定句 emoji 误伤豁免（queue_gate.check_issue_disposition）
  - 否定前挂词（不落/不构成/无……）紧邻 emoji → 不计入问题条目，放行
  - 真问题条目（emoji 非否定语境）且无落点词 → 仍拦截（防豁免开口子）
任务2：review pass 交付卡 review_mark 转正提醒（queue_transition._review_card_mark_reminder）
  - 交付物节含 30_wiki 卡片路径 → 输出「N 张交付卡待 review_mark 转正」
  - 无 30_wiki 路径 / 无执行报告 → 空串不打扰

运行：python -m pytest 90_control/scripts/tests/test_gate_suite_fixes_612.py -q
"""
import sys
import tempfile
import unittest
from pathlib import Path

SCRIPT_DIR = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(SCRIPT_DIR))

import queue_gate as qg
import queue_transition as qt


class TestF036NegationExemption(unittest.TestCase):
    """否定声明句放行 + 真问题条目仍拦截。"""

    def test_negation_buluo_passes(self):
        """#608 被拦原句型：「不落 🟠/🟡」→ 放行。"""
        ok, msg = qg.check_issue_disposition("发现的问题均不落 🟠/🟡 级，无需落点。")
        self.assertTrue(ok, msg)

    def test_negation_bugoucheng_passes(self):
        ok, msg = qg.check_issue_disposition("以上差异不构成 🟡 级问题。")
        self.assertTrue(ok, msg)

    def test_negation_wu_passes(self):
        ok, msg = qg.check_issue_disposition("本次审查无 🟠/🟡 级问题。")
        self.assertTrue(ok, msg)

    def test_real_issue_without_disposition_blocked(self):
        """真问题条目 + 无落点词 → 仍拦截（豁免不能开成口子）。"""
        ok, msg = qg.check_issue_disposition("发现问题：\n- 🟠 交付物未入仓\n- 🟡 文档过期")
        self.assertFalse(ok)
        self.assertIn("F-036", msg)
        self.assertIn("否定", msg)  # 报错文案含否定句提示（欧阳锋口径）

    def test_real_issue_with_disposition_passes(self):
        """真问题条目 + 落点词 → 放行（原有行为不回归）。"""
        ok, msg = qg.check_issue_disposition("- 🟠 交付物未入仓 → 落点：另立项 #999")
        self.assertTrue(ok, msg)

    def test_negation_word_not_adjacent_still_blocked(self):
        """否定词不紧邻 emoji（「暂无落点：🟠」）→ 不误豁免，仍拦截。"""
        ok, msg = qg.check_issue_disposition("- 🟠 问题甲，暂无落点：🟡 问题乙")
        self.assertFalse(ok)


class TestReviewCardMarkReminder(unittest.TestCase):
    """review pass 交付卡转正提醒（纯函数级，不走状态机）。"""

    def _mk_task(self, td: str, body: str) -> Path:
        tf = Path(td) / "task_9999_612test.md"
        tf.write_text(body, encoding="utf-8")
        return tf

    def test_wiki_card_in_deliverables_reminds(self):
        body = (
            "# 任务\n\n## 执行报告\n"
            "**交付物**：`30_wiki/concepts/foo.md`、`30_wiki/frameworks/bar.md` 已入库\n"
            "**完成内容**：建卡两张\n"
            "**验证**：kdo lint 通过\n"
            "**边界**：无\n"
            "**需要谁动作**：欧阳锋终审\n"
        )
        with tempfile.TemporaryDirectory() as td:
            tf = self._mk_task(td, body)
            remind = qt._review_card_mark_reminder(tf)
        self.assertIn("2 张交付卡待 review_mark 转正", remind)
        self.assertIn("30_wiki/concepts/foo.md", remind)

    def test_no_wiki_card_no_reminder(self):
        body = (
            "# 任务\n\n## 执行报告\n"
            "**交付物**：`90_control/scripts/queue_gate.py` 已入库\n"
            "**完成内容**：改门禁\n"
        )
        with tempfile.TemporaryDirectory() as td:
            tf = self._mk_task(td, body)
            remind = qt._review_card_mark_reminder(tf)
        self.assertEqual(remind, "")

    def test_no_exec_report_no_reminder(self):
        with tempfile.TemporaryDirectory() as td:
            tf = self._mk_task(td, "# 任务\n（无执行报告节）\n")
            remind = qt._review_card_mark_reminder(tf)
        self.assertEqual(remind, "")


if __name__ == "__main__":
    unittest.main()
