"""#425 --health 指标集测试：纯函数（fixture 卡）+ 集成冒烟（真实库）。

运行：python -m pytest 90_control/scripts/tests/test_health_metrics.py -q
"""
import importlib.util
import subprocess
import sys
from pathlib import Path

# 文件名带连字符无法 import，用 spec 加载（不触发 main：有 __main__ guard）
_SPEC = importlib.util.spec_from_file_location(
    "full_library_rescan", Path(__file__).resolve().parent.parent / "full-library-rescan.py"
)
flr = importlib.util.module_from_spec(_SPEC)
_SPEC.loader.exec_module(flr)


def _card(id_, rel, fm):
    return {"rel": rel, "id": id_, "fm": fm, "err": None, "body": "", "body_start": 1}


def test_draft_ratio_counts_draft_only():
    cards = [
        _card("a", "30_wiki/concepts/a.md", {"status": "draft"}),
        _card("b", "30_wiki/concepts/b.md", {"status": "reviewed"}),
        _card("c", "30_wiki/concepts/c.md", {"status": "draft"}),
        _card("d", "30_wiki/concepts/d.md", {"status": "enriched"}),
    ]
    r = flr.m_draft_ratio(cards)
    assert r["value"] == 2
    assert r["total"] >= 2865  # 真实库全量 md 数，只增不减


def test_empty_shell_counts_src_unknown():
    cards = [
        _card("a", "30_wiki/concepts/a.md", {"source_refs": ["src_unknown"]}),
        _card("b", "30_wiki/concepts/b.md", {"source_refs": ["10_raw/sources/x.md"]}),
        _card("c", "30_wiki/concepts/c.md", {"source_refs": ["path/to/y.md - src_unknown"]}),
        _card("d", "30_wiki/concepts/d.md", {"status": "reviewed"}),
    ]
    r = flr.m_empty_shell(cards)
    assert r["value"] == 2  # a 独立占位 + c 定位后缀占位
    assert r["total"] == 4


def test_graph_orphan_counts_zero_inlink():
    cards = [
        _card("a", "30_wiki/concepts/a.md", {"related": ["b"]}),
        _card("b", "30_wiki/concepts/b.md", {"related": []}),
        _card("c", "30_wiki/concepts/c.md", {"related": ["a"]}),
    ]
    r = flr.m_graph_orphan(cards)
    assert r["value"] == 1  # c 无入链
    assert r["total"] == 3


def test_trend_tolerance():
    # 0.5 个百分点内 = 持平（798/2865=0.2785 vs 基线 0.279 不应误报）
    assert flr._health_trend(0.2785, 0.279) == "="
    assert flr._health_trend(0.279, 0.279) == "="
    assert flr._health_trend(0.2, 0.279) == "↓ 改善"
    assert flr._health_trend(0.31, 0.279) == "↑ 恶化"
    assert flr._health_trend(0.31, 0.3, lower_better=False) == "↑ 改善"
    assert flr._health_trend(None, 0.3) == "?"


def test_health_cli_smoke():
    r = subprocess.run(
        [sys.executable, str(Path(__file__).resolve().parent.parent / "full-library-rescan.py"), "--health"],
        capture_output=True, text=True, encoding="utf-8", errors="replace", timeout=300,
    )
    assert r.returncode == 0, r.stderr[-500:]
    for needle in ("draft 占比", "parse-error", "related-asymmetry", "复盘 A 级覆盖率", "交接留痕完整度", "待定义"):
        assert needle in r.stdout, f"缺指标行: {needle}"
