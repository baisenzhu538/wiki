"""Regression tests for audit_queue_integrity.py parse blind spot (#456).

- 表检测必须 robust（`|:---` 分隔行），旧 `| 队列序号` 表头检查整表静默失败
  → 审计假阴性（0 行解析）——#188 残留从未被抓的根因
- 单元格数异常（<5 列）的行禁止静默跳过 → 收集进 unresolved 并列入报告
"""
import sys
import tempfile
import unittest
from pathlib import Path

SCRIPT_DIR = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(SCRIPT_DIR))

import audit_queue_integrity as aqi

# daily-context-save.py 在 kdo-tools/，文件名含连字符 → importlib 加载
import importlib.util
KDO_TOOLS = Path(__file__).resolve().parent.parent.parent.parent / "kdo-tools"
_spec = importlib.util.spec_from_file_location(
    "daily_context_save", str(KDO_TOOLS / "daily-context-save.py"))
_dcs = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(_dcs)
_normalize_agent_id = _dcs._normalize_agent_id


QUEUE_SAMPLE = """# 生产队列
|:---:|:---|:---|:---:|:---:|---:|:---|:---|:---|
| 1 | `task_20260801_huangyaoshi-foo` | 正常行 | reviewed | huangyaoshi | x | `60_feedback/tasks/task_20260801_huangyaoshi-foo.md` | 备注 |
| 2 | `task_20260802_huangyaoshi-bar` | 缺列行 |
| 3 | `task_20260803_huangyaoshi-baz` | 超列行 | queued | huangyaoshi | x | `60_feedback/tasks/task_20260803_huangyaoshi-baz.md` | 备注 | 多出的列 |
"""


class TestParseQueue(unittest.TestCase):

    def setUp(self):
        self.tmp = tempfile.NamedTemporaryFile("w", encoding="utf-8", suffix=".md", delete=False)
        self.tmp.write(QUEUE_SAMPLE)
        self.tmp.close()
        self.path = Path(self.tmp.name)

    def tearDown(self):
        self.path.unlink(missing_ok=True)

    def test_parses_rows_with_ascii_separator_detection(self):
        """`|:---` 分隔行检测必须生效（旧 `| 队列序号` 表头检查整表假阴性）。"""
        rows, unresolved = aqi.parse_queue(self.path)
        self.assertEqual(len(rows), 2)  # 行 1、行 3（行 2 缺列进 unresolved）
        self.assertEqual(rows[0]["task_id"], "task_20260801_huangyaoshi-foo")
        self.assertEqual(rows[0]["status"], "reviewed")
        self.assertEqual(rows[1]["task_id"], "task_20260803_huangyaoshi-baz")

    def test_abnormal_rows_collected_not_skipped(self):
        """<5 列的行进 unresolved，不静默跳过（#456 盲区修复）。"""
        rows, unresolved = aqi.parse_queue(self.path)
        self.assertEqual(len(unresolved), 1)
        self.assertIn("task_20260802_huangyaoshi-bar", unresolved[0]["raw"])
        self.assertIn("line", unresolved[0])
        self.assertIn("cells", unresolved[0])

    def test_no_separator_row_yields_empty_rows(self):
        """无表格时返回空（不崩溃）。"""
        with tempfile.NamedTemporaryFile("w", encoding="utf-8", suffix=".md", delete=False) as f:
            f.write("# 只有标题\n")
            p = Path(f.name)
        try:
            rows, unresolved = aqi.parse_queue(p)
            self.assertEqual(rows, [])
            self.assertEqual(unresolved, [])
        finally:
            p.unlink(missing_ok=True)


class TestNormalizeAgentId(unittest.TestCase):
    """#456 agent_id 口径：中文映射拼音 / 测试残留拒绝 / 拼音透传。"""

    def test_cn_name_mapped_to_pinyin(self):
        self.assertEqual(_normalize_agent_id("老顽童"), "laowantong")
        self.assertEqual(_normalize_agent_id("欧阳锋"), "ouyangfeng")
        self.assertEqual(_normalize_agent_id("黄药师"), "huangyaoshi")

    def test_test_residual_rejected(self):
        self.assertIsNone(_normalize_agent_id("__test434__"))
        self.assertIsNone(_normalize_agent_id("__test464__"))

    def test_pinyin_passthrough(self):
        self.assertEqual(_normalize_agent_id("huangyaoshi"), "huangyaoshi")
        self.assertEqual(_normalize_agent_id("fengqingyang"), "fengqingyang")


if __name__ == "__main__":
    unittest.main()
