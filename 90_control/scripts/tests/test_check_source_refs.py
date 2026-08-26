"""#543 回归：check-source-refs 行号锚剥除 + json 宿主兼容 + 阈值退出码 + 治理聚类。

运行：python -m pytest 90_control/scripts/tests/test_check_source_refs.py -q
"""
import importlib.util
import io
import json
import sys
from pathlib import Path

_SPEC = importlib.util.spec_from_file_location(
    "check_source_refs", Path(__file__).resolve().parent.parent / "check-source-refs.py"
)
csr = importlib.util.module_from_spec(_SPEC)
_SPEC.loader.exec_module(csr)


def _mkvault(tmp_path: Path) -> Path:
    """最小 vault：1 真实素材 + 3 卡（锚定存在/锚定缺失/裸缺失）。"""
    (tmp_path / "10_raw" / "sources").mkdir(parents=True)
    (tmp_path / "10_raw" / "sources" / "real.md").write_text("x", encoding="utf-8")
    wiki = tmp_path / "30_wiki" / "concepts"
    wiki.mkdir(parents=True)

    def card(name, refs):
        fm = ["---", f"id: {name}", "type: concept", "status: draft", "source_refs:"]
        fm += [f"- '{r}'" for r in refs]
        fm.append("---")
        (wiki / f"{name}.md").write_text("\n".join(fm) + "\n\n正文\n", encoding="utf-8")

    card("anchored-alive", ["10_raw/sources/real.md:2245"])
    card("anchored-dead", ["10_raw/sources/ghost.md:12"])
    card("plain-dead", ["10_raw/sources/ghost2.md"])
    return tmp_path


def _scan_tmp(tmp_path):
    results = [csr.check_card(fp, tmp_path) for fp in (tmp_path / "30_wiki").rglob("*.md")]
    return {r["card_id"]: r for r in results}


def test_anchor_stripped_existing_file_found(tmp_path):
    """带行号锚 + 文件存在 → exists=True（修复前误判缺失）。"""
    cards = _scan_tmp(_mkvault(tmp_path))
    s = cards["anchored-alive"]["sources"][0]
    assert s["exists"] is True
    assert s["had_line_anchor"] is True


def test_anchor_stripped_missing_still_reported(tmp_path):
    """带行号锚 + 文件不存在 → 仍报缺失（剥锚不误伤真死引）。"""
    cards = _scan_tmp(_mkvault(tmp_path))
    s = cards["anchored-dead"]["sources"][0]
    assert s["exists"] is False
    assert s["had_line_anchor"] is True


def test_plain_missing_still_reported(tmp_path):
    cards = _scan_tmp(_mkvault(tmp_path))
    s = cards["plain-dead"]["sources"][0]
    assert s["exists"] is False
    assert s["had_line_anchor"] is False


def test_strip_line_anchor_pure():
    assert csr.strip_line_anchor("a/b.md:2245") == "a/b.md"
    assert csr.strip_line_anchor("a/b.md:10-20") == "a/b.md"
    assert csr.strip_line_anchor("a/b.md") == "a/b.md"
    assert csr.strip_line_anchor("C:/foo/bar.md") == "C:/foo/bar.md"  # 盘符不误伤
    assert csr.strip_line_anchor("src_20260531_x") == "src_20260531_x"


def test_anchor_stats_in_summary(tmp_path):
    """挤占量统计：锚引用总数 + 剥锚后存活数进入 stats。"""
    results = list(_scan_tmp(_mkvault(tmp_path)).values())
    stats = csr.summarize(results)
    assert stats["refs_line_anchor"] == 2
    assert stats["refs_line_anchor_alive"] == 1
    assert stats["refs_missing"] == 2  # anchored-dead + plain-dead


def _run_scan_json(tmp_path, monkeypatch):
    """以无 .buffer 的 StringIO 为 stdout 跑 cmd_scan（模拟 agent 宿主），返回 (exit|None, json)。"""
    vault = _mkvault(tmp_path)
    out = io.StringIO()
    monkeypatch.setattr(sys, "stdout", out)
    args = argparse_ns(json=True, report_dir=None, max_missing=None, max_contaminated=None,
                       domain=None, card=None)
    code = None
    try:
        csr.cmd_scan(args, vault)
    except SystemExit as e:
        code = e.code
    return code, json.loads(out.getvalue())


class argparse_ns:
    def __init__(self, **kw):
        self.__dict__.update(kw)


def test_json_survives_bufferless_stdout(tmp_path, monkeypatch):
    """#543 json bug：stdout 无 .buffer（agent 宿主）不再 AttributeError 崩溃。"""
    code, data = _run_scan_json(tmp_path, monkeypatch)
    assert code == 1  # 有缺失 → exit 1（默认旧行为）
    assert data["stats"]["refs_missing"] == 2


def test_max_missing_threshold(tmp_path, monkeypatch):
    """阈值制：缺失≤阈值 exit 0（存量不扰），超阈值 exit 1（增量报警）。"""
    vault = _mkvault(tmp_path)
    for expected_code, threshold in ((0, 2), (0, 5), (1, 1)):
        out = io.StringIO()
        monkeypatch.setattr(sys, "stdout", out)
        args = argparse_ns(json=False, report_dir=None, max_missing=threshold, max_contaminated=None,
                           domain=None, card=None)
        code = None
        try:
            csr.cmd_scan(args, vault)
        except SystemExit as e:
            code = e.code
        got = code if code is not None else 0  # 不超阈值不 SystemExit = 0
        assert got == expected_code, f"threshold={threshold} expect {expected_code} got {got}"


def test_report_dir_writes_md_and_json_with_clusters(tmp_path, monkeypatch):
    vault = _mkvault(tmp_path)
    report_dir = tmp_path / "analysis"
    out = io.StringIO()
    monkeypatch.setattr(sys, "stdout", out)
    args = argparse_ns(json=False, report_dir=str(report_dir), max_missing=None, max_contaminated=None,
                       domain=None, card=None)
    try:
        csr.cmd_scan(args, vault)
    except SystemExit:
        pass
    md = (report_dir / "source-refs-health-latest.md").read_text(encoding="utf-8")
    js = json.loads((report_dir / "source-refs-health-latest.json").read_text(encoding="utf-8"))
    assert "死引治理聚类" in md
    assert js["clusters"]["by_domain_status"]
    assert js["clusters"]["by_domain_status"][0]["missing"] == 2
