"""Regression tests for file-flow-check.py (#450：规范 §8 L1-L9 + 向前生效 §9)."""
import json
import sys
import tempfile
import unittest
from pathlib import Path

KDO_TOOLS = Path(__file__).resolve().parent.parent

import importlib.util
_SPEC = importlib.util.spec_from_file_location(
    "file_flow_check", KDO_TOOLS / "file-flow-check.py")
ffc = importlib.util.module_from_spec(_SPEC)
_SPEC.loader.exec_module(ffc)


def write(path: Path, content: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content, encoding="utf-8")


DIAG_FM = """---
doc_id: D-20260823-001
version: v1.0
created_at: '2026-08-23T10:00:00+08:00'
updated_at: '2026-08-23T10:00:00+08:00'
audience: 王语嫣
status: pending_orchestration
---
正文
"""


class BaseTestCase(unittest.TestCase):
    def setUp(self):
        self.tmp = Path(tempfile.mkdtemp())
        self.diag = self.tmp / "diagnosis"
        self.tasks = self.tmp / "tasks"
        self.queue = self.tmp / "production-queue.md"
        self._orig = (ffc.DIAG_DIR, ffc.TASK_DIR, ffc.QUEUE_FILE, ffc.WIKI_CARDS)
        ffc.DIAG_DIR, ffc.TASK_DIR, ffc.QUEUE_FILE = (
            self.diag, self.tasks, self.queue)
        # wiki 卡扫描隔离：临时空目录（测试聚焦本用例，避免真实 30_wiki 干扰）
        self.wiki = self.tmp / "wiki"
        self.wiki.mkdir()
        ffc.WIKI_CARDS = self.wiki
        # 冻结段（模拟探针登记）
        write(self.queue, f"""# 队列
<!-- PROPOSAL-PENDING-BEGIN（自动登记：conveyor_probe.py；勿手改——王语嫣复核后划掉） -->
- diag_20260823_huangyaoshi-frozen.md｜08-23 10:00｜待王语嫣复核裁定
<!-- PROPOSAL-PENDING-END -->
""")

    def tearDown(self):
        ffc.DIAG_DIR, ffc.TASK_DIR, ffc.QUEUE_FILE, ffc.WIKI_CARDS = self._orig
        import shutil
        shutil.rmtree(self.tmp, ignore_errors=True)

    def scan(self):
        return ffc.scan_diag_files()


class TestL1DocIdDuplicate(BaseTestCase):
    def test_duplicate_doc_id_reported(self):
        write(self.diag / "diag_20260823_a-foo.md", DIAG_FM.replace("D-20260823-001", "D-20260823-099"))
        write(self.diag / "diag_20260823_b-bar.md", DIAG_FM.replace("D-20260823-001", "D-20260823-099"))
        out = ffc.check_doc_id_duplicates(self.scan())
        self.assertEqual(len(out), 1)
        self.assertEqual(out[0][0], "error")
        self.assertIn("D-20260823-099", out[0][2])

    def test_unique_doc_id_no_report(self):
        write(self.diag / "diag_20260823_a-foo.md", DIAG_FM)
        self.assertEqual(ffc.check_doc_id_duplicates(self.scan()), [])


class TestL2DocIdFormat(BaseTestCase):
    def test_bad_format_reported(self):
        bad = DIAG_FM.replace("doc_id: D-20260823-001", "doc_id: D-20260823-01")  # 两位序号
        write(self.diag / "diag_20260823_a-foo.md", bad)
        out = ffc.check_doc_id_format(self.scan())
        self.assertEqual(len(out), 1)
        self.assertEqual(out[0][0], "error")


class TestL3Version(BaseTestCase):
    def test_effective_new_file_missing_version(self):
        no_ver = DIAG_FM.replace("version: v1.0\n", "")
        write(self.diag / "diag_20260823_a-foo.md", no_ver)
        out = ffc.check_version(self.scan())
        self.assertEqual(len(out), 1)
        self.assertEqual(out[0][0], "warning")

    def test_legacy_file_missing_version_not_reported(self):
        legacy = DIAG_FM.replace("version: v1.0\n", "").replace("2026-08-23", "2026-06-12")
        write(self.diag / "diag_20260612_a-foo.md", legacy)
        self.assertEqual(ffc.check_version(self.scan()), [])


class TestL4Timestamps(BaseTestCase):
    def test_missing_updated_at_reported(self):
        no_upd = DIAG_FM.replace("updated_at: '2026-08-23T10:00:00+08:00'\n", "")
        write(self.diag / "diag_20260823_a-foo.md", no_upd)
        out = ffc.check_timestamps(self.scan())
        self.assertEqual(len(out), 1)
        self.assertIn("updated_at", out[0][2])


class TestL5Naming(BaseTestCase):
    def test_bad_name_new_file_warning(self):
        write(self.diag / "weird-name.md", DIAG_FM)
        out = ffc.check_naming(self.scan())
        self.assertEqual(len(out), 1)
        self.assertEqual(out[0][0], "warning")

    def test_bad_name_legacy_info_only(self):
        legacy = DIAG_FM.replace("2026-08-23", "2026-06-12")
        write(self.diag / "weird-name.md", legacy)
        out = ffc.check_naming(self.scan())
        self.assertEqual(out[0][0], "info")


class TestL6Slug(BaseTestCase):
    def test_slug_with_path_word_reported(self):
        write(self.diag / "diag_20260823_a-bad slug.md", DIAG_FM)
        out = ffc.check_slug(self.scan())
        self.assertEqual(len(out), 1)
        self.assertIn("bad slug", out[0][2])


class TestL7Frozen(BaseTestCase):
    """#473 项2 无状态方案：冻结清单动态生成 + git HEAD 锚点（monkeypatch 注入）。"""

    def _patch_git(self, modified: bool = False, tracked: bool = True):
        import unittest.mock as mock
        self._git = mock.patch.object(ffc, "_git_diff_quiet", return_value=modified)
        self._track = mock.patch.object(ffc, "_is_tracked_by_git", return_value=tracked)
        self._git.start()
        self._track.start()

    def tearDown(self):
        super().tearDown()
        if hasattr(self, "_git"):
            self._git.stop()
            self._track.stop()

    def test_frozen_file_modified_reported(self):
        write(self.diag / "diag_20260823_huangyaoshi-frozen.md", DIAG_FM)
        self._patch_git(modified=True)
        out = ffc.check_frozen(self.scan())
        self.assertEqual(len(out), 1)
        self.assertEqual(out[0][0], "error")
        self.assertIn("冻结", out[0][2])

    def test_frozen_file_untouched_clean(self):
        write(self.diag / "diag_20260823_huangyaoshi-frozen.md", DIAG_FM)
        self._patch_git(modified=False)
        self.assertEqual(ffc.check_frozen(self.scan()), [])

    def test_frozen_file_untracked_warns(self):
        write(self.diag / "diag_20260823_huangyaoshi-frozen.md", DIAG_FM)
        self._patch_git(modified=False, tracked=False)
        out = ffc.check_frozen(self.scan())
        self.assertEqual(out[0][0], "warning")
        self.assertIn("未被 git 跟踪", out[0][2])


class TestL8Amends(BaseTestCase):
    def test_dangling_amends_reported(self):
        amends = DIAG_FM.replace(
            "updated_at: '2026-08-23T10:00:00+08:00'",
            "updated_at: '2026-08-23T10:00:00+08:00'\namends: D-20260823-999")
        write(self.diag / "diag_20260823_a-foo.md", amends)
        out = ffc.check_amends(self.scan())
        self.assertEqual(len(out), 1)
        self.assertIn("D-20260823-999", out[0][2])

    def test_amends_with_comment_resolves(self):
        # 被引用件存在
        write(self.diag / "diag_20260823_a-base.md", DIAG_FM)
        # 订正件 amends 带注释 → 取 D-编号前缀比对
        amends = DIAG_FM.replace(
            "doc_id: D-20260823-001", "doc_id: D-20260823-002").replace(
            "updated_at: '2026-08-23T10:00:00+08:00'",
            "updated_at: '2026-08-23T10:00:00+08:00'\namends: D-20260823-001（补充说明）")
        write(self.diag / "diag_20260823_b-amend-v1.1.md", amends)
        self.assertEqual(ffc.check_amends(self.scan()), [])


class TestL9Namespace(BaseTestCase):
    def test_task_file_with_doc_id_reported(self):
        write(self.tasks / "task_20260823_huangyaoshi-foo.md",
              "---\nid: 470\nstatus: queued\ndoc_id: D-20260823-100\n---\n# x\n")
        out = ffc.check_id_namespace(self.scan())
        self.assertEqual(len(out), 1)
        self.assertIn("doc_id", out[0][2])


class TestEffectiveFrom(BaseTestCase):
    def test_is_effective_by_created_at(self):
        fm = {"created_at": "2026-08-23T09:00:00+08:00"}
        self.assertTrue(ffc.is_effective(Path("diag_20260823_a-foo.md"), fm))
        fm_old = {"created_at": "2026-06-12T09:00:00+08:00"}
        self.assertFalse(ffc.is_effective(Path("diag_20260612_a-foo.md"), fm_old))

    def test_is_effective_by_filename_when_no_created_at(self):
        self.assertTrue(ffc.is_effective(Path("diag_20260823_a-foo.md"), {}))
        self.assertFalse(ffc.is_effective(Path("diag_20260612_a-foo.md"), {}))


class TestFindDuplicateDocIds(BaseTestCase):
    def test_returns_duplicate_map(self):
        write(self.diag / "diag_20260823_a-foo.md", DIAG_FM.replace("D-20260823-001", "D-20260823-007"))
        write(self.diag / "diag_20260823_b-bar.md", DIAG_FM.replace("D-20260823-001", "D-20260823-007"))
        dup = ffc.find_duplicate_doc_ids()
        self.assertEqual(list(dup.keys()), ["D-20260823-007"])
        self.assertEqual(len(dup["D-20260823-007"]), 2)


if __name__ == "__main__":
    unittest.main()
