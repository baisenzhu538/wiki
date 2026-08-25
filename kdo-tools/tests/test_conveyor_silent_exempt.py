"""#520 R1 回归：conveyor_probe 夜间静默分级（终审类信号豁免，其余待补发）。

运行：python -m pytest kdo-tools/tests/test_conveyor_silent_exempt.py -q
"""
import importlib.util
from pathlib import Path

_SPEC = importlib.util.spec_from_file_location(
    "conveyor_probe", Path(__file__).resolve().parent.parent / "conveyor_probe.py"
)
probe = importlib.util.module_from_spec(_SPEC)
_SPEC.loader.exec_module(probe)


def test_exempt_role_goes_through():
    defer, exempt = probe._split_silent_exempt({"ouyangfeng": "🔔 新提审"}, {"ouyangfeng"})
    assert defer == {}
    assert exempt == {"ouyangfeng": "🔔 新提审"}


def test_non_exempt_role_deferred():
    defer, exempt = probe._split_silent_exempt({"laowantong": "📥 可领取"}, {"ouyangfeng"})
    assert defer == {"laowantong": "📥 可领取"}
    assert exempt == {}


def test_mixed_split():
    to_send = {"ouyangfeng": "🔔 新提审", "wangyuyan": "📬 新建议书"}
    defer, exempt = probe._split_silent_exempt(to_send, {"ouyangfeng"})
    assert exempt == {"ouyangfeng": "🔔 新提审"}
    assert defer == {"wangyuyan": "📬 新建议书"}


def test_empty_exempt_set_defers_all():
    defer, exempt = probe._split_silent_exempt({"ouyangfeng": "x"}, set())
    assert defer == {"ouyangfeng": "x"}
    assert exempt == {}
