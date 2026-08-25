"""#533 回归：技术域适配包——三 schema 可解析+示例卡过校验+盘点三堆分类。

运行：python -m pytest kdo-tools/tests/test_tech_adaptation.py -q
"""
import importlib.util
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parent.parent.parent
SCHEMAS = ROOT / "90_control" / "schemas"

_SPEC = importlib.util.spec_from_file_location(
    "tech_inventory", ROOT / "kdo-tools" / "tech_inventory.py"
)
ti = importlib.util.module_from_spec(_SPEC)
_SPEC.loader.exec_module(ti)


def test_schemas_parse_and_required():
    """三 schema YAML 可解析且必填字段声明在位。"""
    import jsonschema
    for name, req in [("spec.yaml", ["spec_version", "artifact_path"]),
                      ("module.yaml", ["responsibility", "interface_contract"]),
                      ("fault-case.yaml", ["symptom", "root_cause", "fix"])]:
        schema = yaml.safe_load((SCHEMAS / name).read_text(encoding="utf-8"))
        jsonschema.Draft7Validator.check_schema(schema)  # schema 自身合法
        for r in req:
            assert r in schema["required"], f"{name} 缺必填 {r}"


def test_example_cards_validate():
    """三张示例卡 frontmatter 过各自 schema（jsonschema 真校验）。"""
    import jsonschema
    for schema_name, card_name in [("spec.yaml", "spec-example.md"),
                                   ("module.yaml", "module-example.md"),
                                   ("fault-case.yaml", "fault-case-example.md")]:
        schema = yaml.safe_load((SCHEMAS / schema_name).read_text(encoding="utf-8"))
        text = (SCHEMAS / "examples" / card_name).read_text(encoding="utf-8")
        fm = yaml.safe_load(text.split("---\n", 2)[1])
        jsonschema.validate(fm, schema)  # 不抛即过


def _mk(tmp_path, name, content):
    p = tmp_path / name
    p.write_text(content, encoding="utf-8")
    return p


GOOD = "---\ntitle: t\ntype: module\ncreated_at: 2026-08-26\nstatus: draft\nsource_refs: [src_x]\n---\n\n实质正文。\n"


def test_inventory_three_piles(tmp_path):
    """三堆分类：可审/返工（缺源）/废弃（空壳）各归各位。"""
    _mk(tmp_path, "good.md", GOOD)
    _mk(tmp_path, "nosource.md", GOOD.replace("[src_x]", "[src_unknown]"))
    _mk(tmp_path, "shell.md", "# 只有标题\n")
    _mk(tmp_path, "nofm.md", "没有卡头但正文很长" + "字" * 200)
    piles = ti.inventory(tmp_path)
    assert [i["path"] for i in piles["可审"]] == ["good.md"]
    assert {i["path"] for i in piles["返工"]} == {"nosource.md", "nofm.md"}
    assert [i["path"] for i in piles["废弃"]] == ["shell.md"]


def test_inventory_missing_fm_fields(tmp_path):
    _mk(tmp_path, "half.md", "---\ntitle: t\ntype: module\n---\n\n正文。\n")
    piles = ti.inventory(tmp_path)
    assert piles["返工"][0]["path"] == "half.md"
    assert "缺字段" in piles["返工"][0]["reason"]
