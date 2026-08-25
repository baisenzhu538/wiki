"""#527 回归：check-depended-draft 被依赖卡 draft 门禁。

两类核心用例（任务书第 3 条）：被引用 draft→报警 / 无引用 draft→不报警；
baseline 机制：存量 WARNING / 新引用 ERROR（只向前生效）。

运行：python -m pytest 90_control/scripts/tests/test_check_depended_draft.py -q
沙盒：monkeypatch 注入临时 vault 根，不碰真实库。
"""
import importlib.util
import json
import sys
from pathlib import Path

SCRIPT_DIR = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(SCRIPT_DIR))

_SPEC = importlib.util.spec_from_file_location(
    "check_depended_draft", SCRIPT_DIR / "check-depended-draft.py"
)
cdd = importlib.util.module_from_spec(_SPEC)
_SPEC.loader.exec_module(cdd)


def _vault(tmp_path: Path):
    """迷你 vault：1 draft 卡+1 reviewed 卡+1 无引用 draft 卡。"""
    wiki = tmp_path / "30_wiki" / "concepts"
    wiki.mkdir(parents=True)
    (wiki / "card-draft-depended.md").write_text(
        "---\ntitle: 被依赖草稿\ntype: concept\nstatus: draft\n---\n正文\n", encoding="utf-8")
    (wiki / "card-draft-lonely.md").write_text(
        "---\ntitle: 孤立草稿\ntype: concept\nstatus: draft\n---\n正文\n", encoding="utf-8")
    (wiki / "card-reviewed.md").write_text(
        "---\ntitle: 已审卡\ntype: concept\nstatus: reviewed\n---\n正文\n", encoding="utf-8")
    return tmp_path


def _spec_referencing(tmp_path: Path, target: str):
    adir = tmp_path / "agents" / "some-agent"
    adir.mkdir(parents=True)
    (adir / "CLAUDE.md").write_text(f"# 配置\n数据链: {target}\n", encoding="utf-8")


def test_depended_draft_flagged(tmp_path, monkeypatch):
    _vault(tmp_path)
    _spec_referencing(tmp_path, "30_wiki/concepts/card-draft-depended.md")
    monkeypatch.setattr(cdd, "VAULT_ROOT", tmp_path)
    v = cdd.find_violations(tmp_path)
    assert v == [("agents/some-agent/CLAUDE.md", "30_wiki/concepts/card-draft-depended.md")]


def test_lonely_draft_not_flagged(tmp_path, monkeypatch):
    """draft 本身无罪——无引用的 draft 不报警。"""
    _vault(tmp_path)  # 无引用源文件
    monkeypatch.setattr(cdd, "VAULT_ROOT", tmp_path)
    assert cdd.find_violations(tmp_path) == []


def test_reviewed_card_not_flagged(tmp_path):
    _vault(tmp_path)
    _spec_referencing(tmp_path, "30_wiki/concepts/card-reviewed.md")
    assert cdd.find_violations(tmp_path) == []


def test_bare_stem_reference_flagged(tmp_path):
    """词边界裸 stem 引用（工具配置硬引用形态）也算。"""
    _vault(tmp_path)
    _spec_referencing(tmp_path, "card-draft-depended")  # 无路径无扩展名
    v = cdd.find_violations(tmp_path)
    assert ("agents/some-agent/CLAUDE.md", "30_wiki/concepts/card-draft-depended.md") in v


def test_new_violation_error_known_warning(tmp_path, monkeypatch):
    """baseline 机制：存量 WARNING exit 0；新增引用 ERROR exit 1。"""
    _vault(tmp_path)
    _spec_referencing(tmp_path, "30_wiki/concepts/card-draft-depended.md")
    monkeypatch.setattr(cdd, "VAULT_ROOT", tmp_path)
    monkeypatch.setattr(cdd, "BASELINE", tmp_path / "baseline.json")
    monkeypatch.setattr(cdd, "INV_DIR", tmp_path / "inv")

    # 登记 baseline 后：存量 → exit 0
    import sys as _sys
    _sys.argv = ["x", "--update-baseline"]
    assert cdd.main() == 0
    _sys.argv = ["x"]
    assert cdd.main() == 0  # 存量在册 → WARNING 不拦

    # 新增一张 draft 卡+新引用源 → 新违例 ERROR
    wiki2 = tmp_path / "30_wiki" / "concepts" / "card-draft-new.md"
    wiki2.write_text("---\ntitle: 新草稿\ntype: concept\nstatus: draft\n---\n", encoding="utf-8")
    spec2 = tmp_path / "agents" / "other-agent"
    spec2.mkdir(parents=True)
    (spec2 / "CLAUDE.md").write_text("数据源: card-draft-new\n", encoding="utf-8")
    assert cdd.main() == 1  # 新引用违例 → ERROR


def test_inventory_output(tmp_path, monkeypatch, capsys):
    _vault(tmp_path)
    _spec_referencing(tmp_path, "30_wiki/concepts/card-draft-depended.md")
    monkeypatch.setattr(cdd, "VAULT_ROOT", tmp_path)
    monkeypatch.setattr(cdd, "INV_DIR", tmp_path / "inv")
    import sys as _sys
    _sys.argv = ["x", "--inventory"]
    assert cdd.main() == 0
    data = json.loads((tmp_path / "inv" / "inventory.json").read_text(encoding="utf-8"))
    assert data == [{"source": "agents/some-agent/CLAUDE.md",
                     "card": "30_wiki/concepts/card-draft-depended.md"}]
    assert "card-draft-depended" in (tmp_path / "inv" / "inventory.md").read_text(encoding="utf-8")


def test_glob_reference_flagged(tmp_path):
    """glob 数据链引用（30_wiki/frameworks/framework-truman-feature-*.md 形态）算引用——
    #527 触发案例（layered-system 经 basic-skills-coach CLAUDE.md glob 引用）实测形态。"""
    _vault(tmp_path)
    _spec_referencing(tmp_path, "框架卡: 30_wiki/concepts/card-draft-*.md")
    v = cdd.find_violations(tmp_path)
    assert ("agents/some-agent/CLAUDE.md", "30_wiki/concepts/card-draft-depended.md") in v


def test_index_type_not_flagged(tmp_path):
    """type: index/log 的非卡资产（log.md/cases-index）被引用不报警——写入路径≠消费依赖。"""
    wiki = tmp_path / "30_wiki"
    wiki.mkdir(parents=True)
    (wiki / "log.md").write_text(
        "---\ntype: index\nstatus: draft\ntitle: log\n---\n", encoding="utf-8")
    _spec_referencing(tmp_path, "30_wiki/log.md")
    assert cdd.find_violations(tmp_path) == []
