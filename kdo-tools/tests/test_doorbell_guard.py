"""#565：OS 门铃守卫（活着跳过）+ SessionStart 门铃自检钩回归。"""
import importlib.util
import json
import time
from pathlib import Path

def _load(name):
    p = Path(__file__).resolve().parent.parent / f"{name}.py"
    spec = importlib.util.spec_from_file_location(name, p)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod

guard = _load("kdo_doorbell_guard")
boot = _load("kdo_session_boot_hook")


def _reg(tmp_path, ts):
    f = tmp_path / "role-registry.json"
    f.write_text(json.dumps({"huangyaoshi": {"instances": [
        {"tool": "kimi-cli", "kind": "cli", "heartbeat_ts": ts}]}}), encoding="utf-8")
    return f


def test_guard_skips_when_alive(tmp_path, monkeypatch):
    monkeypatch.setattr(guard, "REGISTRY", _reg(tmp_path, time.time() - 60))
    assert guard.session_alive("huangyaoshi") is True


def test_guard_fires_when_stale_or_missing(tmp_path, monkeypatch):
    monkeypatch.setattr(guard, "REGISTRY", _reg(tmp_path, time.time() - 3600))
    assert guard.session_alive("huangyaoshi") is False
    monkeypatch.setattr(guard, "REGISTRY", tmp_path / "missing.json")
    assert guard.session_alive("huangyaoshi") is False  # fail-open 放行


def test_guard_ignores_platform_instances(tmp_path, monkeypatch):
    f = tmp_path / "role-registry.json"
    f.write_text(json.dumps({"huangyaoshi": {"instances": [
        {"tool": "hermes", "kind": "platform", "heartbeat_ts": time.time()}]}}), encoding="utf-8")
    monkeypatch.setattr(guard, "REGISTRY", f)
    assert guard.session_alive("huangyaoshi") is False  # hermes 活≠本地 CLI 活


def test_boot_hook_injects_only_in_wiki(tmp_path, monkeypatch, capsys):
    import io, contextlib
    payload = json.dumps({"hook_event_name": "SessionStart", "cwd": str(boot.WIKI_ROOT)})
    monkeypatch.setattr("sys.stdin", io.StringIO(payload))
    assert boot.main() == 0
    assert "门铃自检" in capsys.readouterr().out

    payload = json.dumps({"hook_event_name": "SessionStart", "cwd": "C:/other/place"})
    monkeypatch.setattr("sys.stdin", io.StringIO(payload))
    assert boot.main() == 0
    assert capsys.readouterr().out == ""  # 非 wiki 仓不注入
