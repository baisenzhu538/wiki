"""#670 回归：终审 PASS 后交付卡 status 自动翻转（draft→reviewed）。

实证：#666 终审 PASS A- 后框架批卡停留 draft（reviewed_by: 待审）→ 检索层带
【未审 draft】标（KDO CLI delivery.py `_label_unreviewed` #380）——此前靠欧阳锋
手工 review_mark 批收口（#656/#666 先例=人肉补丁）。修法：queue_transition review
verdict=pass 时按执行报告「交付物」节自动翻转（review_mark.mark_card 同一实现）。

用例：tier1 完整路径 / tier2 反引号裸 id / tier3 裸 id+声明目录（#666 写法）/
     tier3b type×N（#668 写法，含域中缀）/ 歧义标题不翻 / 非 draft 幂等护栏 /
     未识别降级提醒 / 翻转异常不阻断终审 / fail 分支不翻转 /
     mark_card only_flip_from 门控 + dry-run（手工 CLI 语义不回归）。

运行：python -m pytest 90_control/scripts/tests/test_review_card_flip_670.py -q
"""
import sys
import tempfile
import unittest
from pathlib import Path

SCRIPT_DIR = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(SCRIPT_DIR))

import queue_transition as qt
import review_mark

TODAY = review_mark.datetime.now(review_mark.CST).strftime("%Y-%m-%d")
OPINION = ("## 终审记录\n\n核对交付物清单与任务单规格逐项比对一致，三张卡均具 source_refs 与"
           "related 双向链接，回归用例佐证充分，队列流转链路完整，准许入库。\n")


def _mk_card(td, name, status="draft", reviewed_by="待审", subdir="frameworks"):
    d = Path(td) / "30_wiki" / subdir
    d.mkdir(parents=True, exist_ok=True)
    p = d / f"{name}.md"
    p.write_text(
        f"---\ntitle: {name}\ntype: concept\nstatus: {status}\n"
        f"author: laowantong\nreviewed_by: {reviewed_by}\nsource_refs:\n  - 10_raw/sources/x.md\n"
        f"---\n\n# {name}\n\n正文\n",
        encoding="utf-8",
    )
    return p


def _report(deliverable_line):
    return f"**交付物**：{deliverable_line}\n**完成内容**：略\n"


def _task_file(td, report, task_id="task_8888_flipcards"):
    tf = Path(td) / f"{task_id}.md"
    tf.write_text(
        f"---\nid: {task_id}\nstatus: pending_review\nassignee: laowantong\n---\n\n"
        f"# 任务\n\n## 执行报告\n\n{report}\n{OPINION}",
        encoding="utf-8",
    )
    return tf


class _SandboxMixin(unittest.TestCase):
    """`_WIKI_ROOT` 指向沙盒（tier1 路径解析/索引构建同锚），stem 索引缓存隔离。"""

    def setUp(self):
        self._old_root = qt._WIKI_ROOT
        self._old_stem_idx = qt._STEM_INDEX
        self._old_commit = qt._git_commit_card_flips

    def _sandbox(self, td):
        qt._WIKI_ROOT = Path(td)
        qt._STEM_INDEX = None  # 缓存隔离：沙盒各不相同
        qt._git_commit_card_flips = lambda *a, **k: None  # 沙盒无 .git，显式短路

    def tearDown(self):
        qt._WIKI_ROOT = self._old_root
        qt._STEM_INDEX = self._old_stem_idx
        qt._git_commit_card_flips = self._old_commit


class TestResolveDeliveredCards(_SandboxMixin):
    def test_tier1_full_path(self):
        with tempfile.TemporaryDirectory() as td:
            self._sandbox(td)
            _mk_card(td, "framework-demo-a")
            cards, unres = qt._resolve_delivered_cards(
                _report("新卡 `30_wiki/frameworks/framework-demo-a.md`。"), "t.md")
            self.assertEqual([c.stem for c in cards], ["framework-demo-a"])
            self.assertEqual(unres, [])

    def test_tier2_backticked_bare_id(self):
        with tempfile.TemporaryDirectory() as td:
            self._sandbox(td)
            _mk_card(td, "dk-demo-b", subdir="dark-knowledges")
            cards, unres = qt._resolve_delivered_cards(
                _report("A 组新卡（`30_wiki/dark-knowledges/`：`dk-demo-b` M-07）。"), "t.md")
            self.assertEqual([c.stem for c in cards], ["dk-demo-b"])
            self.assertEqual(unres, [])

    def test_tier3_bare_ids_declared_dir_666_style(self):
        """#666 实报写法：`30_wiki/frameworks/`：framework-x(199 行)/framework-y(195)。"""
        with tempfile.TemporaryDirectory() as td:
            self._sandbox(td)
            _mk_card(td, "framework-demo-x")
            _mk_card(td, "framework-demo-y")
            cards, unres = qt._resolve_delivered_cards(
                _report("批 1 框架 2 件已入库 `30_wiki/frameworks/`（对齐）："
                        "framework-demo-x(199 行)/framework-demo-y(195)；"
                        "pre-submit 存档 `logs/pre.log`。"), "t.md")
            self.assertEqual(sorted(c.stem for c in cards),
                             ["framework-demo-x", "framework-demo-y"])
            self.assertEqual(unres, [])

    def test_tier3b_type_by_count_titles_668_style(self):
        """#668 实报写法：framework×7（知识卡片公式/…）——文件名带域中缀也命中。"""
        with tempfile.TemporaryDirectory() as td:
            self._sandbox(td)
            _mk_card(td, "framework-AI知识库-知识卡片公式")
            cards, unres = qt._resolve_delivered_cards(
                _report("framework×1（知识卡片公式）+ 自攻击报告 `60_feedback/atk.md`。"), "t.md")
            self.assertEqual([c.stem for c in cards], ["framework-AI知识库-知识卡片公式"])
            self.assertEqual(unres, [])

    def test_ambiguous_title_defers_to_human(self):
        """同前缀后缀匹配歧义（>1 候选）→ 不翻，进 unresolved（宁漏勿错翻）。"""
        with tempfile.TemporaryDirectory() as td:
            self._sandbox(td)
            _mk_card(td, "framework-域A-知识卡片公式")
            _mk_card(td, "framework-域B-知识卡片公式")
            cards, unres = qt._resolve_delivered_cards(
                _report("framework×1（知识卡片公式）。"), "t.md")
            self.assertEqual(cards, [])
            self.assertEqual(len(unres), 1)

    def test_unknown_id_reported_not_resolved(self):
        with tempfile.TemporaryDirectory() as td:
            self._sandbox(td)
            cards, unres = qt._resolve_delivered_cards(
                _report("`framework-not-in-vault` 一张。"), "t.md")
            self.assertEqual(cards, [])
            self.assertEqual(unres, ["framework-not-in-vault"])

    def test_exempt_marker_skips_resolution(self):
        with tempfile.TemporaryDirectory() as td:
            self._sandbox(td)
            cards, unres = qt._resolve_delivered_cards(
                _report("纯任务单修改，无卡片交付。"), "t.md")
            self.assertEqual((cards, unres), ([], []))

    def test_missing_tier1_file_goes_unresolved(self):
        with tempfile.TemporaryDirectory() as td:
            self._sandbox(td)
            cards, unres = qt._resolve_delivered_cards(
                _report("新卡 `30_wiki/frameworks/framework-ghost.md`。"), "t.md")
            self.assertEqual(cards, [])
            self.assertEqual(unres, ["30_wiki/frameworks/framework-ghost.md"])


class TestFlipDeliveredCards(_SandboxMixin):
    def test_flip_draft_card_on_disk(self):
        with tempfile.TemporaryDirectory() as td:
            self._sandbox(td)
            p = _mk_card(td, "framework-demo-a")
            msg = qt._flip_delivered_cards(
                _task_file(td, _report("新卡 `30_wiki/frameworks/framework-demo-a.md`。")),
                "欧阳锋")
            text = p.read_text(encoding="utf-8")
            self.assertIn("status: reviewed", text)
            self.assertIn("reviewed_by: 欧阳锋", text)
            self.assertIn(f"review_date: {TODAY}", text)
            self.assertNotIn("reviewed_by: 待审", text)
            self.assertIn("自动翻转 1 张", msg)

    def test_non_draft_untouched_idempotent_guard(self):
        with tempfile.TemporaryDirectory() as td:
            self._sandbox(td)
            p = _mk_card(td, "framework-demo-a", status="reviewed", reviewed_by="欧阳锋")
            msg = qt._flip_delivered_cards(
                _task_file(td, _report("新卡 `30_wiki/frameworks/framework-demo-a.md`。")),
                "欧阳锋")
            self.assertIn("status: reviewed", p.read_text(encoding="utf-8"))
            self.assertIn("未动", msg)
            self.assertNotIn("自动翻转", msg)

    def test_mixed_batch_flips_only_drafts(self):
        """同批 draft 翻、已 reviewed 跳过——#668 批场景（部分卡此前已手工收口）。"""
        with tempfile.TemporaryDirectory() as td:
            self._sandbox(td)
            p_draft = _mk_card(td, "framework-demo-a")
            p_done = _mk_card(td, "framework-demo-b", status="reviewed")
            msg = qt._flip_delivered_cards(
                _task_file(td, _report("两件 `30_wiki/frameworks/framework-demo-a.md`、"
                                       "`30_wiki/frameworks/framework-demo-b.md`。")),
                "欧阳锋")
            self.assertIn("status: reviewed", p_draft.read_text(encoding="utf-8"))
            self.assertIn("自动翻转 1 张", msg)
            self.assertIn("未动", msg)
            self.assertNotIn("review_date", p_done.read_text(encoding="utf-8").split("---")[1])

    def test_unresolved_degrades_to_reminder_not_write(self):
        with tempfile.TemporaryDirectory() as td:
            self._sandbox(td)
            msg = qt._flip_delivered_cards(
                _task_file(td, _report("`framework-not-in-vault` 一张。")), "欧阳锋")
            self.assertIn("未能自动翻转", msg)
            self.assertIn("framework-not-in-vault", msg)

    def test_flip_exception_does_not_raise(self):
        """翻转环节异常绝不阻断终审主流程——降级为报告条目。"""
        with tempfile.TemporaryDirectory() as td:
            self._sandbox(td)
            _mk_card(td, "framework-demo-a")
            orig = review_mark.mark_card
            qt.review_mark.mark_card = lambda *a, **k: (_ for _ in ()).throw(RuntimeError("boom"))
            try:
                msg = qt._flip_delivered_cards(
                    _task_file(td, _report("新卡 `30_wiki/frameworks/framework-demo-a.md`。")),
                    "欧阳锋")
            finally:
                qt.review_mark.mark_card = orig
            self.assertIn("boom", msg)

    def test_no_wiki_deliverable_returns_empty(self):
        with tempfile.TemporaryDirectory() as td:
            self._sandbox(td)
            msg = qt._flip_delivered_cards(
                _task_file(td, _report("脚本 `90_control/scripts/x.py` 与 log `logs/x.log`。")),
                "欧阳锋")
            self.assertEqual(msg, "")

    def test_exempt_section_returns_empty(self):
        with tempfile.TemporaryDirectory() as td:
            self._sandbox(td)
            _mk_card(td, "framework-demo-a")
            msg = qt._flip_delivered_cards(
                _task_file(td, _report("纯任务单修改（见任务单 diff）。")), "欧阳锋")
            self.assertEqual(msg, "")


class TestActionReviewEndToEnd(_SandboxMixin):
    """终审 PASS → 交付卡自动翻转，全链路（真实写盘，队列层 monkeypatch）。"""

    _QT_ATTRS = ("parse_queue", "find_task", "_find_task_file_dual", "QueueLock",
                 "apply_updates", "_check_review_authority", "_check_issue_disposition",
                 "_review_board_update", "QUEUE_PATH")

    def setUp(self):
        super().setUp()
        self._saved_queue = {a: getattr(qt, a) for a in self._QT_ATTRS}

    def tearDown(self):
        for a, v in self._saved_queue.items():
            setattr(qt, a, v)  # monkeypatch 全量回收——泄漏会毒化后续测试文件（本单实证）
        super().tearDown()

    def _wire(self, td, card_status="draft"):
        self._sandbox(td)
        qf = Path(td) / "queue.md"
        qf.write_text("# q\n", encoding="utf-8")
        qt.QUEUE_PATH = qf
        tf = _task_file(td, _report("新卡 `30_wiki/frameworks/framework-e2e.md`。"))
        p = _mk_card(td, "framework-e2e", status=card_status)
        rows = [{"seq": "8888", "task_id": "task_8888_flipcards", "name": "n",
                 "status": "pending_review", "assignee": "laowantong", "raw": "| 8888 |"}]
        qt.parse_queue = lambda: rows
        qt.find_task = lambda tid, rows_=None: next(
            (r for r in rows if r["task_id"] == tid), None)
        qt._find_task_file_dual = lambda tid: tf
        qt.QueueLock = _NullLock
        qt.apply_updates = lambda *a, **k: None
        qt._check_review_authority = lambda *a, **k: (True, "")
        qt._check_issue_disposition = lambda *a, **k: (True, "")
        qt._review_board_update = lambda *a, **k: None
        return p

    def test_pass_flips_card_end_to_end(self):
        with tempfile.TemporaryDirectory() as td:
            p = self._wire(td)
            ok, msg = qt.action_review("task_8888_flipcards", "pass", "欧阳锋", "A-")
            self.assertTrue(ok, msg)
            self.assertIn("终审通过", msg)
            self.assertIn("自动翻转 1 张", msg)
            text = p.read_text(encoding="utf-8")
            self.assertIn("status: reviewed", text)
            self.assertIn("reviewed_by: 欧阳锋", text)
            self.assertIn(f"review_date: {TODAY}", text)

    def test_pass_already_reviewed_card_no_double_write(self):
        with tempfile.TemporaryDirectory() as td:
            p = self._wire(td, card_status="reviewed")
            ok, msg = qt.action_review("task_8888_flipcards", "pass", "欧阳锋", "A-")
            self.assertTrue(ok, msg)
            self.assertIn("未动", msg)
            self.assertNotIn("review_date",
                             p.read_text(encoding="utf-8").split("---")[1])

    def test_fail_does_not_flip(self):
        with tempfile.TemporaryDirectory() as td:
            p = self._wire(td)
            ok, msg = qt.action_review("task_8888_flipcards", "fail", "欧阳锋")
            self.assertTrue(ok, msg)
            self.assertIn("status: draft", p.read_text(encoding="utf-8"))

    def test_unresolvable_path_reported_in_review_message(self):
        """识别不出（文件不存在）→ 终审照常通过，报告项列明请人工 review_mark 收口。"""
        with tempfile.TemporaryDirectory() as td:
            self._sandbox(td)
            qf = Path(td) / "queue.md"
            qf.write_text("# q\n", encoding="utf-8")
            qt.QUEUE_PATH = qf
            tf = _task_file(td, _report("交付卡 `30_wiki/frameworks/framework-ghost.md`"
                                        "（盘上无此文件）。"))
            rows = [{"seq": "8888", "task_id": "task_8888_flipcards", "name": "n",
                     "status": "pending_review", "assignee": "laowantong", "raw": "| 8888 |"}]
            qt.parse_queue = lambda: rows
            qt.find_task = lambda tid, rows_=None: next(
                (r for r in rows if r["task_id"] == tid), None)
            qt._find_task_file_dual = lambda tid: tf
            qt.QueueLock = _NullLock
            qt.apply_updates = lambda *a, **k: None
            qt._check_review_authority = lambda *a, **k: (True, "")
            qt._check_issue_disposition = lambda *a, **k: (True, "")
            qt._review_board_update = lambda *a, **k: None
            ok, msg = qt.action_review("task_8888_flipcards", "pass", "欧阳锋", "A-")
            self.assertTrue(ok, msg)
            self.assertIn("终审通过", msg)
            self.assertIn("framework-ghost", msg)


class TestMarkCardGate(unittest.TestCase):
    """review_mark.mark_card only_flip_from 门控 + dry-run（手工 CLI 语义不回归）。"""

    def test_only_flip_from_blocks_reviewed_card(self):
        with tempfile.TemporaryDirectory() as td:
            p = _mk_card(td, "c1", status="reviewed", reviewed_by="欧阳锋")
            ok, msg = review_mark.mark_card(p, reviewer="欧阳锋", only_flip_from=("draft",))
            self.assertFalse(ok)
            self.assertTrue(msg.startswith("skip: status=reviewed"))
            self.assertNotIn(f"review_date: {TODAY}", p.read_text(encoding="utf-8"))

    def test_manual_cli_semantics_preserved_without_gate(self):
        """不带 only_flip_from（手工 CLI 路径）→ stable 卡也翻（欧阳锋裁量权不变）。"""
        with tempfile.TemporaryDirectory() as td:
            p = _mk_card(td, "c2", status="stable", reviewed_by="")
            ok, msg = review_mark.mark_card(p, reviewer="欧阳锋")
            self.assertTrue(ok, msg)
            self.assertIn("status: reviewed", p.read_text(encoding="utf-8"))

    def test_dry_run_no_write(self):
        with tempfile.TemporaryDirectory() as td:
            p = _mk_card(td, "c3")
            before = p.read_text(encoding="utf-8")
            ok, msg = review_mark.mark_card(p, reviewer="欧阳锋", dry_run=True)
            self.assertTrue(ok, msg)
            self.assertIn("[DRY RUN]", msg)
            self.assertEqual(before, p.read_text(encoding="utf-8"))

    def test_frontmatter_other_fields_preserved(self):
        with tempfile.TemporaryDirectory() as td:
            p = _mk_card(td, "c4")
            ok, _ = review_mark.mark_card(p, reviewer="欧阳锋")
            self.assertTrue(ok)
            text = p.read_text(encoding="utf-8")
            for frag in ("title: c4", "author: laowantong", "source_refs:",
                         "10_raw/sources/x.md"):
                self.assertIn(frag, text)


class _NullLock:
    def __init__(self, *a): pass
    def __enter__(self): return self
    def __exit__(self, *a): return False


if __name__ == "__main__":
    unittest.main()
