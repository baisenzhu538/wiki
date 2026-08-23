"""Regression tests for infra-status.py (#488：资产健康快照核心判定)."""
import importlib.util
import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

KDO_TOOLS = Path(__file__).resolve().parent.parent
_SPEC = importlib.util.spec_from_file_location("infra_status", KDO_TOOLS / "infra-status.py")
is_ = importlib.util.module_from_spec(_SPEC)
_SPEC.loader.exec_module(is_)


class TestFileOk(unittest.TestCase):
    def test_directory_counts_healthy(self):
        """目录 st_size 可能为 0——存在即健康（#488 首跑 L1-full 误判回归）。"""
        with tempfile.TemporaryDirectory() as d:
            p = Path(d)
            self.assertTrue(is_._file_ok(p))

    def test_missing_file_red(self):
        self.assertFalse(is_._file_ok(Path("C:/definitely-missing-xyz")))


class TestOptionalLedger(unittest.TestCase):
    def test_optional_always_green(self):
        """可选台账：不存在=无例外记录=健康（force-exceptions.log 无记录是好事）。"""
        name, kind, status = is_._check(("force-exceptions.log", "台账", "OPTIONAL:/nope.log"))
        self.assertEqual(status, "🟢")

    def test_real_optional_ledger_green(self):
        name, kind, status = is_._check(
            ("force-exceptions.log", "台账", "OPTIONAL:" + str(is_.WIKI / "90_control" / "force-exceptions.log")))
        self.assertEqual(status, "🟢")


class TestSnapshotRun(unittest.TestCase):
    def test_json_output_structure(self):
        """--json 输出含 assets/red/total 字段。"""
        r = subprocess.run([sys.executable, str(KDO_TOOLS / "infra-status.py"), "--json"],
                           capture_output=True, text=True, encoding="utf-8")
        data = json.loads(r.stdout)
        self.assertIn("assets", data)
        self.assertIn("red", data)
        self.assertIn("total", data)
        self.assertEqual(data["total"], len(data["assets"]))


if __name__ == "__main__":
    unittest.main()


class TestInventoryCoverage(unittest.TestCase):
    def test_core_assets_registered(self):
        """总表登记覆盖：核心资产名可被解析（含斜杠多名行）。"""
        known = is_._inventory_assets()
        for core in ("queue_transition", "conveyor_probe", "memory_capsule",
                     "web_search", "infra-status", "sync-hermes-mcp", "scan-ppt-gaps"):
            self.assertIn(core, known, f"{core} 应已登记入总表")

    def test_no_unregistered_core_assets(self):
        """对照检查：核心目录无未登记资产（登记纪律机械化为零缺口）。"""
        unreg = is_.check_inventory_coverage()
        self.assertEqual(unreg, [], f"未登记资产: {unreg}")

    def test_oneshot_patterns_skipped(self):
        """一次性批模式（fix-* 等）不报未登记（总表 §8 标记族）。"""
        known = is_._inventory_assets()
        # fix-yaml-errors-batch 类未在总表但模式匹配=跳过
        self.assertNotIn("fix-yaml-errors-batch", known)  # 不在总表
        unreg = is_.check_inventory_coverage()
        self.assertNotIn("fix-yaml-errors-batch", unreg)  # 也不报（一次性模式跳过）
