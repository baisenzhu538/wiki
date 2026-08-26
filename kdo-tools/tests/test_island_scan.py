"""#528 回归：孤岛卡扫描（双无检测+豁免+清单）。

三类用例（任务书第 4 条）：孤岛/非孤岛/豁免。

运行：python -m pytest kdo-tools/tests/test_island_scan.py -q
"""
import importlib.util
from pathlib import Path

_SPEC = importlib.util.spec_from_file_location(
    "island_scan", Path(__file__).resolve().parent.parent / "island_scan.py"
)
isl = importlib.util.module_from_spec(_SPEC)
_SPEC.loader.exec_module(isl)


def _card(root: Path, rel: str, ctype: str = "concept", related: str = ""):
    p = root / rel
    p.parent.mkdir(parents=True, exist_ok=True)
    rel_line = f"related: [{related}]" if related else "related: []"
    p.write_text(f"---\ntitle: t\ntype: {ctype}\n{rel_line}\n---\n\n正文\n", encoding="utf-8")
    return p


def test_island_detected(tmp_path):
    """无出链+无入链=孤岛入清单。"""
    _card(tmp_path, "concepts/lonely.md")
    _card(tmp_path, "concepts/hub.md", related="lonely-x")
    result = isl.scan(tmp_path)
    # 精确断言：hub 有出链但无入链 → 非孤岛（有出链）；lonely 双无 → 孤岛
    paths = {i["path"] for i in result["islands"]}
    assert "concepts/lonely.md" in paths
    assert "concepts/hub.md" not in paths  # hub 有出链（指向 lonely-x）


def test_inlinked_not_island(tmp_path):
    """无出链但有入链 → 非孤岛。"""
    _card(tmp_path, "concepts/a.md", related="b")
    _card(tmp_path, "concepts/b.md")  # 无出链但被 a 引用
    result = isl.scan(tmp_path)
    paths = {i["path"] for i in result["islands"]}
    assert "concepts/b.md" not in paths
    assert "concepts/a.md" not in paths


def test_agent_spec_exempt(tmp_path):
    """agent-spec 类（type 或目录）双无也豁免。"""
    _card(tmp_path, "agent-specs/agent-spec-x.md", ctype="tool-agent-spec")
    _card(tmp_path, "tools/agent-spec-y.md")  # 目录名 agent-specs 才豁免，tools/ 不豁免但 type 普通→看双无
    result = isl.scan(tmp_path)
    paths = {i["path"] for i in result["islands"]}
    assert "agent-specs/agent-spec-x.md" not in paths  # type 豁免
    assert "tools/agent-spec-y.md" in paths  # 无豁免+双无 → 孤岛


def test_non_card_excluded(tmp_path):
    """无 frontmatter type 的文件不进扫描面。"""
    p = tmp_path / "README.md"
    p.write_text("# 说明\n", encoding="utf-8")
    result = isl.scan(tmp_path)
    assert result["total_cards"] == 0 and result["islands"] == []
