"""Regression tests for queue_transition.py task file lookup."""
import sys
import tempfile
import unittest
from pathlib import Path

SCRIPT_DIR = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(SCRIPT_DIR))

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
