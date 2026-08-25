"""#536 回归：near-miss 超期升级推送（≥3 轮推王语嫣/修正消项/静默 defer/幂等）。

运行：python -m pytest kdo-tools/tests/test_near_miss_escalation.py -q
"""
import importlib.util
from pathlib import Path

_SPEC = importlib.util.spec_from_file_location(
    "conveyor_probe", Path(__file__).resolve().parent.parent / "conveyor_probe.py"
)
probe = importlib.util.module_from_spec(_SPEC)
_SPEC.loader.exec_module(probe)

MISS = ["diag_20260826_bad.md｜三元组缺 audience"]


def _todos(tmp_path, monkeypatch):
    monkeypatch.setattr(probe, "TODOS_DIR", tmp_path)
    return tmp_path / "wangyuyan.md"


def test_escalates_at_third_round(tmp_path, monkeypatch):
    fp = _todos(tmp_path, monkeypatch)
    state = {}
    probe._escalate_near_miss(state, MISS, dry_run=False, silent=False)
    probe._escalate_near_miss(state, MISS, dry_run=False, silent=False)
    assert not fp.exists() or "超期升级" not in fp.read_text(encoding="utf-8")  # 1-2 轮不推
    probe._escalate_near_miss(state, MISS, dry_run=False, silent=False)
    text = fp.read_text(encoding="utf-8")
    assert "超期升级" in text and "diag_20260826_bad.md" in text and "3 轮未修正" in text
    assert "首检出" in text  # 首次检出时间戳入推送


def test_fixed_item_clears_and_no_repush(tmp_path, monkeypatch):
    """修正消项：违例消失→出账；再出现（同理由）不重复推（escalated 幂等）。"""
    fp = _todos(tmp_path, monkeypatch)
    state = {}
    for _ in range(3):
        probe._escalate_near_miss(state, MISS, dry_run=False, silent=False)
    probe._escalate_near_miss(state, [], dry_run=False, silent=False)  # 修正
    assert state["near_miss_rounds"] == {}  # 出账
    for _ in range(3):  # 同理由再犯——escalated 幂等不重复推
        probe._escalate_near_miss(state, MISS, dry_run=False, silent=False)
    assert fp.read_text(encoding="utf-8").count("超期升级") == 1


def test_silent_defers_then_fires(tmp_path, monkeypatch):
    """夜间静默 defer：轮数照计不推送；首个非静默拍补发。"""
    fp = _todos(tmp_path, monkeypatch)
    state = {}
    for _ in range(3):
        probe._escalate_near_miss(state, MISS, dry_run=False, silent=True)
    assert not fp.exists()  # 静默期不推
    probe._escalate_near_miss(state, MISS, dry_run=False, silent=False)
    assert "超期升级" in fp.read_text(encoding="utf-8")  # 天亮补发


def test_dry_run_no_write(tmp_path, monkeypatch):
    fp = _todos(tmp_path, monkeypatch)
    state = {}
    for _ in range(3):
        probe._escalate_near_miss(state, MISS, dry_run=True, silent=False)
    assert not fp.exists()
