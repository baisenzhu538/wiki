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


def _fm(tags=None, domain=None, sp=None, sc=None, aliases=None):
    fm = {}
    if tags is not None:
        fm["tags"] = tags
    if domain:
        fm["domain"] = domain
    if sp:
        fm["source_person"] = sp
    if sc:
        fm["source_context"] = sc
    if aliases is not None:
        fm["aliases"] = aliases
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


class TestSourceWordBlacklist(AuditBase):
    """#484 第5指标：来源形态词黑名单（独立出现拦/复合词白名单不拦/来源轴词不拦）。"""

    def test_independent_source_word_reported(self):
        self.write_card("a.md", _fm(tags=["科学决策", "逐字稿"], domain=["decision-making"]))
        r = ta.audit(ta.scan_cards())
        self.assertEqual(len(r["source_word_hits"]), 1)
        self.assertIn("逐字稿", r["source_word_hits"][0][1])

    def test_compound_word_not_reported(self):
        self.write_card("a.md", _fm(tags=["科学决策", "笔记法", "分享经济"], domain=["decision-making"]))
        r = ta.audit(ta.scan_cards())
        self.assertEqual(r["source_word_hits"], [])

    def test_source_axis_words_not_reported(self):
        # 来源轴受控词（拆书会/口述 在决策域来源轴 words 中）不被当污染
        self.write_card("a.md", _fm(tags=["科学决策", "拆书会", "口述"], domain=["decision-making"]))
        r = ta.audit(ta.scan_cards())
        # 拆书会/口述 在黑名单——但它们是来源轴受控词（任务书口径：来源轴词不报）
        # 实现上黑名单与来源轴词表重合时以来源轴为准——此处按任务书断言不报
        self.assertEqual(r["source_word_hits"], [])

    def test_pollution_rate_computed(self):
        self.write_card("a.md", _fm(tags=["逐字稿"], domain=["decision-making"]))
        self.write_card("b.md", _fm(tags=["科学决策"], domain=["decision-making"]))
        r = ta.audit(ta.scan_cards())
        self.assertEqual(r["source_word_rate"], 50.0)


class TestAliasPollution(AuditBase):
    """#494 第6指标：aliases 结构词/路径词污染（正反用例）。"""

    def test_struct_prefix_reported(self):
        self.write_card("a.md", _fm(tags=["科学决策"], domain=["decision-making"], aliases=["audience:executor", "好名"]))
        r = ta.audit(ta.scan_cards())
        hits = [h for h in r["alias_hits"] if "audience:executor" in h[1]]
        self.assertEqual(len(hits), 1)

    def test_path_word_reported(self):
        self.write_card("a.md", _fm(tags=["x"], aliases=["decisions.md", "正常别名"]))
        r = ta.audit(ta.scan_cards())
        self.assertEqual(len(r["alias_hits"]), 1)
        self.assertIn("路径词", r["alias_hits"][0][2])

    def test_clean_aliases_not_reported(self):
        self.write_card("a.md", _fm(tags=["x"], aliases=["科学决策", "拍板原则"]))
        r = ta.audit(ta.scan_cards())
        self.assertEqual(r["alias_hits"], [])

    def test_alias_rate_computed(self):
        self.write_card("a.md", _fm(tags=["x"], aliases=["decisions.md"]))
        self.write_card("b.md", _fm(tags=["x"], aliases=["好名"]))
        r = ta.audit(ta.scan_cards())
        self.assertEqual(r["alias_rate"], 50.0)


class TestTaskFreezeL10(unittest.TestCase):
    """#502 L10：任务单正文冻结检测（四类豁免 + 收严口径）。"""

    def test_exempt_ranges_frontmatter_and_sections(self):
        import importlib.util as _ilu
        _s = _ilu.spec_from_file_location("ffc", KDO_TOOLS / "file-flow-check.py")
        ffc = _ilu.module_from_spec(_s)
        _s.loader.exec_module(ffc)
        text = ("---\nid: 1\nstatus: queued\n---\n"
                "## 任务\n正文\n"
                "## 执行报告\n报告\n"
                "## 终审记录\n终审\n")
        # queued：frontmatter+执行报告+终审 豁免
        ranges = ffc._task_exempt_ranges(text, "queued")
        lines = text.splitlines()
        for ln, l in enumerate(lines, 1):
            if l.startswith("id:") or l.startswith("status:") or "正文" in l:
                continue
        # 行1-4 frontmatter 豁免；执行报告节=行7-8；终审节=行9-10
        self.assertTrue(any(s <= 2 <= e for s, e in ranges), "frontmatter 行应豁免")
        self.assertTrue(any(s <= 8 <= e for s, e in ranges), "执行报告节应豁免(queued)")
        # pending_review：执行报告不豁免
        ranges2 = ffc._task_exempt_ranges(text, "pending_review")
        self.assertFalse(any(s <= 8 <= e for s, e in ranges2), "提审后执行报告节不豁免")

    def test_in_exempt(self):
        import importlib.util as _ilu
        _s = _ilu.spec_from_file_location("ffc", KDO_TOOLS / "file-flow-check.py")
        ffc = _ilu.module_from_spec(_s)
        _s.loader.exec_module(ffc)
        self.assertTrue(ffc._in_exempt(2, [(1, 5)]))
        self.assertFalse(ffc._in_exempt(6, [(1, 5)]))
