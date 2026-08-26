"""#524 回归：kdo_search 消费端契约——status/confidence 标注 + ⚠️ 前缀 + 来源层标注 + 排序加权。

混合语料（reviewed/draft/pending_review/无 status 非卡）验证标注与排序；
降权不剔除（红线 4）。纯函数级测试，不起 MCP server、不碰检索引擎。

运行：python -m pytest kdo-tools/tests/test_mcp_server.py -q
"""
import importlib.util
from pathlib import Path

_SPEC = importlib.util.spec_from_file_location(
    "kdo_mcp_tools", Path(__file__).resolve().parent.parent / "mcp" / "tools.py"
)
tools = importlib.util.module_from_spec(_SPEC)
_SPEC.loader.exec_module(tools)


def _card(tmp_path: Path, rel: str, status: str | None, confidence: str = "") -> Path:
    p = tmp_path / rel
    p.parent.mkdir(parents=True, exist_ok=True)
    fm = ["---", "title: 测试卡", "type: concept"]
    if status is not None:
        fm.append(f"status: {status}")
    if confidence:
        fm.append(f"confidence: {confidence}")
    fm.append("---")
    p.write_text("\n".join(fm) + "\n\n正文\n", encoding="utf-8")
    return p


# ── 标题前缀（任务第 1 条）──

def test_draft_gets_warn_prefix():
    assert tools._display_title("卡A", "draft") == "⚠️ 卡A"


def test_pending_review_gets_warn_prefix():
    assert tools._display_title("卡A", "pending_review") == "⚠️ 卡A"


def test_reviewed_no_prefix():
    assert tools._display_title("卡A", "reviewed") == "卡A"


# ── 来源层标注（任务第 2 条）──

def test_raw_source_layer_labeled():
    assert tools._source_layer_label("10_raw/sources/x.md", "") == "[raw]"


def test_skills_source_layer_labeled():
    assert tools._source_layer_label("40_outputs/skills/foo/SKILL.md", "") == "[skills]"


def test_wiki_card_no_layer_label():
    assert tools._source_layer_label("30_wiki/concepts/x.md", "") == ""


def test_status_present_no_layer_label():
    assert tools._source_layer_label("10_raw/sources/x.md", "draft") == ""


# ── 排序加权（任务第 3 条：降权不剔除）──

def test_status_weights_mixed_corpus(tmp_path):
    """等分混合语料：reviewed 前移、draft 降权、无 status 保持——全部保留不剔除。"""
    rev = _card(tmp_path, "30_wiki/concepts/a.md", "reviewed")
    raw = _card(tmp_path, "10_raw/sources/b.md", None)
    drf = _card(tmp_path, "30_wiki/concepts/c.md", "draft")
    fused = [(1.0, str(rev), "s"), (1.0, str(raw), "s"), (1.0, str(drf), "s")]
    weighted = tools._apply_status_weights(fused)
    scores = {Path(p).stem: s for s, p, _ in weighted}
    assert scores["a"] > scores["b"] > scores["c"]
    assert len(weighted) == 3  # 降权不剔除


def test_pending_review_weight_between():
    assert tools._STATUS_WEIGHT["pending_review"] < 1.0
    assert tools._STATUS_WEIGHT["pending_review"] > tools._STATUS_WEIGHT["draft"]


def test_missing_file_weight_neutral(tmp_path):
    """文件不可读 → 权重 1.0（fail-open 不误伤）。"""
    fused = [(1.0, str(tmp_path / "ghost.md"), "s")]
    weighted = tools._apply_status_weights(fused)
    assert weighted[0][0] == 1.0


# ── #541：trust_level 加权 + 低置信标记 + conflict_with 警告 ──

def _card_v2(tmp_path: Path, rel: str, status: str | None, trust: str = "",
             conflict: list | None = None) -> Path:
    p = tmp_path / rel
    p.parent.mkdir(parents=True, exist_ok=True)
    fm = ["---", "title: 测试卡", "type: concept"]
    if status is not None:
        fm.append(f"status: {status}")
    if trust:
        fm.append(f"trust_level: {trust}")
    if conflict:
        fm.append("conflict_with:")
        fm.extend(f"- '{c}'" for c in conflict)
    fm.append("---")
    p.write_text("\n".join(fm) + "\n\n正文\n", encoding="utf-8")
    return p


def test_trust_weights_layered_order(tmp_path):
    """#541 混合语料：reviewed+high > 无标注非卡 > draft+medium——全部保留不剔除。"""
    hi = _card_v2(tmp_path, "30_wiki/frameworks/a.md", "reviewed", "high")
    raw = _card_v2(tmp_path, "10_raw/sources/b.md", None)
    lo = _card_v2(tmp_path, "30_wiki/cases/c.md", "draft", "medium")
    fused = [(1.0, str(hi), "s"), (1.0, str(raw), "s"), (1.0, str(lo), "s")]
    weighted = tools._apply_status_weights(fused)
    scores = {Path(p).stem: s for s, p, _ in weighted}
    assert scores["a"] > scores["b"] > scores["c"]
    assert len(weighted) == 3  # 降权不剔除


def test_trust_weight_ordering():
    assert tools._TRUST_WEIGHT["high"] > tools._TRUST_WEIGHT["medium"] > tools._TRUST_WEIGHT["low"]


def test_draft_high_beats_nothing_but_loses_to_reviewed_high(tmp_path):
    """同 status 下 trust 分层：reviewed+low 仍低于 reviewed+high。"""
    hi = _card_v2(tmp_path, "30_wiki/concepts/a.md", "reviewed", "high")
    lo = _card_v2(tmp_path, "30_wiki/concepts/b.md", "reviewed", "low")
    fused = [(1.0, str(hi), "s"), (1.0, str(lo), "s")]
    weighted = tools._apply_status_weights(fused)
    scores = {Path(p).stem: s for s, p, _ in weighted}
    assert scores["a"] > scores["b"]


def test_confidence_flag_rules():
    assert tools._confidence_flag("draft", "high") == "低置信度"          # 未终审必标
    assert tools._confidence_flag("pending_review", "medium") == "低置信度"
    assert tools._confidence_flag("reviewed", "low") == "低置信度"        # 低 trust 必标
    assert tools._confidence_flag("reviewed", "medium-low") == "低置信度"
    assert tools._confidence_flag("", "medium") == "低置信度"             # 未终审 medium
    assert tools._confidence_flag("reviewed", "high") == ""
    assert tools._confidence_flag("reviewed", "medium") == ""
    assert tools._confidence_flag("reviewed", "") == ""                   # fail-open 不误标


def test_display_title_low_confidence_suffix():
    assert tools._display_title("卡A", "draft", True) == "⚠️ 卡A（低置信度）"
    assert tools._display_title("卡A", "reviewed", True) == "卡A（低置信度）"
    assert tools._display_title("卡A", "reviewed", False) == "卡A"


def test_conflict_warning_from_frontmatter(tmp_path):
    """#541 + #539 用例：conflict_with 列表 → 附冲突警告指向权威卡。"""
    p = _card_v2(tmp_path, "30_wiki/cases/c.md", "draft", "medium",
                 conflict=["[[concept-yihang-dual-triangle-core]]"])
    fm = tools._parse_frontmatter(p.read_text(encoding="utf-8"))
    links, warning = tools._conflict_warning(fm)
    assert links == ["[[concept-yihang-dual-triangle-core]]"]
    assert "冲突" in warning and "以权威卡为准" in warning
    assert "concept-yihang-dual-triangle-core" in warning


def test_conflict_warning_empty():
    assert tools._conflict_warning({}) == ([], "")
    assert tools._conflict_warning({"conflict_with": []}) == ([], "")
    assert tools._conflict_warning({"conflict_with": None}) == ([], "")


def test_conflict_warning_string_form():
    links, warning = tools._conflict_warning({"conflict_with": "[[card-x]]"})
    assert links == ["[[card-x]]"]
    assert warning.startswith("⚠️")
