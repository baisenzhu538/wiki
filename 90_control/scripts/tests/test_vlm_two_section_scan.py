"""#540 回归（wiki 仓）：VLM/OCR 两段式存量扫描。

运行：python -m pytest 90_control/scripts/tests/test_vlm_two_section_scan.py -q
"""
import importlib.util
import sys
from pathlib import Path

SCRIPT_DIR = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(SCRIPT_DIR))

_SPEC = importlib.util.spec_from_file_location(
    "check_vlm_two_section", SCRIPT_DIR / "check-vlm-two-section.py"
)
vs = importlib.util.module_from_spec(_SPEC)
_SPEC.loader.exec_module(vs)


def _mk(root: Path, rel: str, author: str, body: str):
    p = root / "30_wiki" / rel
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text(f"---\ntitle: t\ntype: case\nauthor: {author}\n---\n\n{body}\n", encoding="utf-8")


def test_scan_classifies(tmp_path):
    _mk(tmp_path, "cases/bad.md", "洪七公（VLM提取）", "## VLM 解析\n\n推断。\n")
    _mk(tmp_path, "cases/good.md", "洪七公（VLM提取）", f"> {vs.VLM_WARN_LINE}\n\n推断。\n")
    _mk(tmp_path, "cases/human.md", "老顽童", "正文。\n")
    r = vs.scan(tmp_path)
    assert r["total_vlm"] == 2 and r["compliant"] == 1
    assert [v["path"] for v in r["violations"]] == ["30_wiki/cases/bad.md"]


def test_body_mention_only_not_vlm(tmp_path):
    """正文提到 VLM 但 author 不含 → 不算 VLM 卡（不误伤）。"""
    _mk(tmp_path, "cases/x.md", "老顽童", "本文讨论 VLM 提取的质量问题。\n")
    assert vs.scan(tmp_path)["total_vlm"] == 0
