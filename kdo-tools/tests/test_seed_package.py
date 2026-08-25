"""#532 回归：build_seed 种子构建 + seed-check 自检 + 路径参数化回退。

运行：python -m pytest kdo-tools/tests/test_seed_package.py -q
沙盒：种子构建到 tmp，不碰真实 90_control/kdo-seed。
"""
import importlib.util
from pathlib import Path

_TOOLS_DIR = Path(__file__).resolve().parent.parent


def _load(name, file):
    spec = importlib.util.spec_from_file_location(name, _TOOLS_DIR / file)
    m = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(m)
    return m


bs = _load("build_seed", "build_seed.py")
sc = _load("seed_check", "seed-check.py")


def test_seed_build_complete(tmp_path):
    """种子构建：关键件+九层骨架+五角色骨架齐。"""
    stats = bs.build(tmp_path / "seed-out")
    seed = tmp_path / "seed-out" / "seed"
    assert stats["files"] > 50  # 机制文件全集非空壳
    for layer in bs.NINE_LAYERS:
        assert (seed / layer / ".gitkeep").exists(), layer
    for role in bs.ROLES:
        assert (seed / "agent复盘" / role / "daily-context").is_dir(), role
    assert (seed / "kdo-tools" / "conveyor_probe.py").exists()
    assert (seed / "90_control" / "scripts" / "queue_transition.py").exists()
    assert (seed / ".agent" / "startup.md").exists()


def test_seed_check_passes_on_real_vault():
    """seed-check 对真实库（本机）目录/文件/角色/编译四查全过（不查 schtasks）。"""
    root = _TOOLS_DIR.parent
    problems = sc.check(root)
    assert problems == [], problems


def test_seed_check_catches_missing_layer(tmp_path):
    """缺层必报（负向用例）。"""
    (tmp_path / "00_inbox").mkdir()
    problems = sc.check(tmp_path)
    assert any("骨架缺层" in p for p in problems)
    assert any("关键件缺失" in p for p in problems)


def test_cmd_wrappers_parameterized():
    """六个 .cmd 全部 KDO_ROOT 优先+%~dp0.. 回退，无硬编码绝对路径。"""
    for name in ["kdo-conveyor-probe.cmd", "kdo-l1-capture.cmd", "kdo-quality-metrics.cmd",
                 "run-daily-audit-digest.cmd", "run-kdo-health.cmd", "run-l1-archive.cmd"]:
        text = (_TOOLS_DIR / name).read_text(encoding="utf-8")
        assert "%KDO_ROOT%" in text and "%~dp0.." in text, name
        assert "cd /d C:\\" not in text, name


def test_py_scripts_kdo_root_fallback():
    """参数化 py 脚本：无 KDO_ROOT 环境变量时回退值=真实库根（本机零行为变化）。"""
    import os
    os.environ.pop("KDO_ROOT", None)
    m = _load("agent_activity_check", "agent-activity-check.py")
    assert Path(m.WIKI) == _TOOLS_DIR.parent
