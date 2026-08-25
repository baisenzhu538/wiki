"""#516 回归：wechat_promote 去重键补 _processed 隔离区（含 .regen-* 变体）。

背景：E037 门禁判定把卡隔离到 pending-cards/_processed/ 后，管线去重只查
PENDING/CASES/RERUN 三处不查 _processed → 已判定卡当夜再生循环。
修复：promote_case 去重补查 _processed（原名 + stem.regen-* 后缀变体）。

运行：python -m pytest kdo-tools/tests/test_wechat_promote.py -q
沙盒：模块属性注入临时目录（PENDING_DIR/CASES_DIR/RERUN_DIR），不碰真实 vault。
"""
import importlib.util
from pathlib import Path

_SPEC = importlib.util.spec_from_file_location(
    "wechat_promote", Path(__file__).resolve().parent.parent / "wechat_promote.py"
)
wp = importlib.util.module_from_spec(_SPEC)
_SPEC.loader.exec_module(wp)

CARD_NAME = "case-wechat-2404c1658025473c.md"
VALID_CARD = """---
title: 测试卡
type: case
domain: test
source_refs: [src_x]
created_at: 2026-08-25
---

""" + "正文" * 120 + "\n"


def _sandbox(tmp_path, monkeypatch):
    """注入沙盒路径。返回 (pending, cases, rerun)。"""
    pending = tmp_path / "pending-cards"
    cases = tmp_path / "cases"
    rerun = tmp_path / "_needs_rerun"
    for d in (pending, cases, rerun):
        d.mkdir(parents=True)
    monkeypatch.setattr(wp, "PENDING_DIR", pending)
    monkeypatch.setattr(wp, "CASES_DIR", cases)
    monkeypatch.setattr(wp, "RERUN_DIR", rerun)
    return pending, cases, rerun


def _card(tmp_path, name=CARD_NAME, content=VALID_CARD):
    f = tmp_path / name
    f.write_text(content, encoding="utf-8")
    return f


def test_processed_same_name_skip(tmp_path, monkeypatch):
    """_processed 有同名卡 → skip 不再生（#516 主场景）。"""
    pending, _, _ = _sandbox(tmp_path, monkeypatch)
    (pending / "_processed").mkdir()
    (pending / "_processed" / CARD_NAME).write_text(VALID_CARD, encoding="utf-8")
    assert wp.promote_case(_card(tmp_path), dry_run=False) == "skip"
    assert not (pending / CARD_NAME).exists()


def test_processed_regen_variant_skip(tmp_path, monkeypatch):
    """_processed 只有 .regen-* 变体（原名被再生后隔离）→ 仍 skip。"""
    pending, _, _ = _sandbox(tmp_path, monkeypatch)
    (pending / "_processed").mkdir()
    (pending / "_processed" / "case-wechat-2404c1658025473c.regen-20260825.md").write_text(
        VALID_CARD, encoding="utf-8")
    assert wp.promote_case(_card(tmp_path), dry_run=False) == "skip"
    assert not (pending / CARD_NAME).exists()


def test_processed_unrelated_not_skip(tmp_path, monkeypatch):
    """_processed 只有无关卡 → 不误伤，正常落待编排区。"""
    pending, _, _ = _sandbox(tmp_path, monkeypatch)
    (pending / "_processed").mkdir()
    (pending / "_processed" / "case-wechat-aaaaaaaaaaaaaaaa.md").write_text(VALID_CARD, encoding="utf-8")
    assert wp.promote_case(_card(tmp_path), dry_run=False) == "pending"
    assert (pending / CARD_NAME).exists()


def test_existing_three_dirs_still_skip(tmp_path, monkeypatch):
    """原有三处去重不回归：PENDING/CASES/RERUN 有同名卡仍 skip。"""
    pending, cases, rerun = _sandbox(tmp_path, monkeypatch)
    for d in (pending, cases, rerun):
        d.joinpath(CARD_NAME).write_text(VALID_CARD, encoding="utf-8")
        assert wp.promote_case(_card(tmp_path), dry_run=False) == "skip"
        d.joinpath(CARD_NAME).unlink()
