"""Regression tests for tags-audit / check-tags-health (#474：四指标计算 + 边界)."""
import importlib.util
import io
import sys
import tempfile
import unittest
from contextlib import redirect_stdout
from pathlib import Path

KDO_TOOLS = Path(__file__).resolve().parent.parent.parent.parent / "kdo-tools"
_SPEC = importlib.util.spec_from_file_location("tags_audit", KDO_TOOLS / "tags-audit.py")
ta = importlib.util.module_from_spec(_SPEC)
_SPEC.loader.exec_module(ta)

SCRIPTS = Path(__file__).resolve().parent.parent
_SPEC2 = importlib.util.spec_from_file_location("check_tags_health", SCRIPTS / "check-tags-health.py")
cth = importlib.util.module_from_spec(_SPEC2)
_SPEC2.loader.exec_module(cth)


def _fm(tags=None, domain=None, sp=None, sc=None):
    fm = {}
    if tags is not None:
        fm["tags"] = tags
    if domain:
        fm["domain"] = domain
    if sp:
        fm["source_person"] = sp
    if sc:
        fm["source_context"] = sc
    return fm


class AuditBase(unittest.TestCase):
    def setUp(self):
        self.tmp = Path(tempfile.mkdtemp())
        self._orig = ta.CARDS_DIR
        ta.CARDS_DIR = self.tmp

    def tearDown(self):
        ta.CARDS_DIR = self._orig
        import shutil
        shutil.rmtree(self.tmp, ignore_errors=True)

    def write_card(self, name, fm):
        body = "---\n" + "\n".join(f"{k}: {v}" if not isinstance(v, list) else f"{k}: {v}"
                                   for k, v in fm.items()) + "\n---\n# 正文\n"
        (self.tmp / name).write_text(body, encoding="utf-8")


class TestDirtyDetection(AuditBase):
    def test_course_name_dirty(self):
        self.write_card("a.md", _fm(tags=["机会预判课"], domain=["decision-making"]))
        self.write_card("b.md", _fm(tags=["科学决策"], domain=["decision-making"]))
        r = ta.audit(ta.scan_cards())
        self.assertEqual(len(r["dirty_course"]), 1)
        self.assertIn("机会预判课", r["dirty_course"][0][1])

    def test_x_zhi_prefix_dirty(self):
        self.write_card("a.md", _fm(tags=["五步法之需求分析"], domain=["decision-making"]))
        r = ta.audit(ta.scan_cards())
        self.assertEqual(len(r["dirty_course"]), 1)
        self.assertIn("五步法之需求分析", r["dirty_course"][0][1])

    def test_source_mixed_dirty(self):
        self.write_card("a.md", _fm(tags=["时代判断力口述"], domain=["decision-making"]))
        r = ta.audit(ta.scan_cards())
        self.assertEqual(len(r["dirty_course"]), 1)
        self.assertIn("来源词混入", r["dirty_course"][0][2])

    def test_negative_strong_dirty(self):
        self.write_card("a.md", _fm(tags=["为空"], domain=["decision-making"]))
        r = ta.audit(ta.scan_cards())
        self.assertEqual(len(r["dirty"]), 1)
        self.assertEqual(r["dirty"][0][2], "STRONG")

    def test_clean_tags_no_dirty(self):
        self.write_card("a.md", _fm(tags=["科学决策", "拍板原则"], domain=["decision-making"]))
        r = ta.audit(ta.scan_cards())
        self.assertEqual(r["dirty"], [])
        self.assertEqual(r["dirty_course"], [])


class TestSourceAxis(AuditBase):
    def test_missing_when_source_field_without_source_tag(self):
        self.write_card("a.md", _fm(tags=["科学决策"], domain=["decision-making"],
                                    sp="半肥猫", sc="开放麦口述"))
        r = ta.audit(ta.scan_cards())
        self.assertEqual(len(r["source_missing"]), 1)

    def test_ok_when_source_tag_present(self):
        self.write_card("a.md", _fm(tags=["科学决策", "口述"], domain=["decision-making"],
                                    sp="半肥猫"))
        r = ta.audit(ta.scan_cards())
        self.assertEqual(r["source_missing"], [])


class TestEmptyAndFormat(AuditBase):
    def test_missing_null_empty_list(self):
        self.write_card("a.md", _fm(domain=["decision-making"]))           # 缺失
        self.write_card("b.md", _fm(tags=[], domain=["decision-making"]))   # 空列表
        r = ta.audit(ta.scan_cards())
        self.assertEqual(len(r["empty_bad"]), 2)

    def test_comma_string_format(self):
        self.write_card("a.md", _fm(tags="科学决策, 拍板", domain=["decision-making"]))
        r = ta.audit(ta.scan_cards())
        self.assertEqual(len(r["empty_bad"]), 1)
        self.assertIn("逗号", r["empty_bad"][0][1])


class TestDomainAxis(AuditBase):
    def test_axis_domain_counted(self):
        self.write_card("a.md", _fm(tags=["科学决策"], domain=["decision-making"]))
        self.write_card("b.md", _fm(tags=["x"], domain=["strategy"]))
        r = ta.audit(ta.scan_cards())
        self.assertEqual(r["domain_counts"]["decision-making"], 1)
        self.assertEqual(r["domain_counts"]["strategy"], 1)


class TestHealthCheck(unittest.TestCase):
    def test_load_paths_valid(self):
        """check-tags-health 的依赖路径正确（tags-audit 可加载）。"""
        self.assertTrue(cth.KDO_TOOLS.exists())
        self.assertTrue((cth.KDO_TOOLS / "tags-audit.py").exists())
        self.assertEqual(cth.LINES["dirty_rate"], 5.0)
        self.assertEqual(cth.LINES["source_coverage"], 90.0)


if __name__ == "__main__":
    unittest.main()
