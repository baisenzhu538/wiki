"""Regression tests for l1_capture.py volume red-line (#471：体积记录 + 超限机器自报)."""
import importlib.util
import sys
import tempfile
import unittest
from pathlib import Path

KDO_TOOLS = Path(__file__).resolve().parent.parent
_SPEC = importlib.util.spec_from_file_location(
    "l1_capture", KDO_TOOLS / "l1_capture.py")
lc = importlib.util.module_from_spec(_SPEC)
_SPEC.loader.exec_module(lc)


class BaseVolumeTest(unittest.TestCase):
    def setUp(self):
        self.tmp = Path(tempfile.mkdtemp())
        self.root = self.tmp / "L1-full"
        self.size_log = self.tmp / "l1-size.log"
        self.gate_log = self.tmp / "gate-blocked.log"
        self._orig = (lc.L1_ROOT, lc.SIZE_LOG, lc.GATE_BLOCKED_LOG, lc.SIZE_REDLINE_MB)
        lc.L1_ROOT, lc.SIZE_LOG, lc.GATE_BLOCKED_LOG = self.root, self.size_log, self.gate_log
        # 默认红线抬高：单测场景不想误触发
        lc.SIZE_REDLINE_MB = 10_000_000

    def tearDown(self):
        lc.L1_ROOT, lc.SIZE_LOG, lc.GATE_BLOCKED_LOG, lc.SIZE_REDLINE_MB = self._orig
        import shutil
        shutil.rmtree(self.tmp, ignore_errors=True)


class TestDirSizeMb(BaseVolumeTest):
    def test_computes_mb_correctly(self):
        (self.root / "a").mkdir(parents=True)
        (self.root / "a" / "f1").write_bytes(b"x" * (1024 * 1024))  # 1 MiB
        (self.root / "f2").write_bytes(b"y" * (512 * 1024))         # 0.5 MiB
        size = lc._dir_size_mb(self.root)
        self.assertAlmostEqual(size, 1.5, places=1)

    def test_missing_dir_returns_zero(self):
        self.assertEqual(lc._dir_size_mb(self.tmp / "nope"), 0.0)


class TestLogSizeAndAlert(BaseVolumeTest):
    def test_under_redline_writes_size_only(self):
        (self.root).mkdir(parents=True)
        (self.root / "f1").write_bytes(b"x" * 1024)
        lc._log_size_and_alert()
        self.assertTrue(self.size_log.exists())
        self.assertIn("L1-full", self.size_log.read_text(encoding="utf-8"))
        self.assertFalse(self.gate_log.exists())  # 未超限不告警

    def test_over_redline_reports_to_gate_blocked(self):
        (self.root).mkdir(parents=True)
        (self.root / "f1").write_bytes(b"x" * (2 * 1024 * 1024))
        lc.SIZE_REDLINE_MB = 1  # 2MB > 1MB 红线
        lc._log_size_and_alert()
        self.assertTrue(self.gate_log.exists())
        text = self.gate_log.read_text(encoding="utf-8")
        self.assertIn("l1-capture", text)
        self.assertIn("L1-体积超限", text)

    def test_size_log_appends_history(self):
        (self.root).mkdir(parents=True)
        (self.root / "f1").write_bytes(b"x" * 1024)
        lc._log_size_and_alert()
        lc._log_size_and_alert()
        lines = self.size_log.read_text(encoding="utf-8").splitlines()
        self.assertEqual(len(lines), 2)  # 追加不覆盖


if __name__ == "__main__":
    unittest.main()
