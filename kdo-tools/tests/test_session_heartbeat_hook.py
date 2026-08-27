"""#562：kimi-cli SessionHeartbeat 钩的角色解析回归。"""
import importlib.util
import json
import sys
from pathlib import Path

HOOK_PATH = Path(__file__).resolve().parent.parent / "kdo_session_heartbeat_hook.py"
spec = importlib.util.spec_from_file_location("kdo_session_heartbeat_hook", HOOK_PATH)
hook = importlib.util.module_from_spec(spec)
spec.loader.exec_module(hook)


def _mk_session(sessions_root, sid, title):
    d = sessions_root / "wd_wiki_x" / sid
    d.mkdir(parents=True)
    (d / "state.json").write_text(json.dumps({"id": sid, "title": title}), encoding="utf-8")


def test_resolve_role_from_title(tmp_path, monkeypatch):
    monkeypatch.setattr(hook, "CACHE", tmp_path / "session-roles.json")
    _mk_session(tmp_path, "session_aaa", "你是黄药师，继续")
    _mk_session(tmp_path, "session_bbb", "领取任务")
    assert hook.resolve_role("session_aaa", tmp_path) == "huangyaoshi"
    assert hook.resolve_role("session_bbb", tmp_path) is None


def test_resolve_role_cache_hit(tmp_path, monkeypatch):
    cache = tmp_path / "session-roles.json"
    cache.write_text(json.dumps({"session_ccc": "wangyuyan"}), encoding="utf-8")
    monkeypatch.setattr(hook, "CACHE", cache)
    assert hook.resolve_role("session_ccc", tmp_path) == "wangyuyan"  # 无会话目录也命中缓存


def test_resolve_role_pinyin_alias(tmp_path, monkeypatch):
    monkeypatch.setattr(hook, "CACHE", tmp_path / "session-roles.json")
    _mk_session(tmp_path, "session_ddd", "ouyangfeng 终审")
    assert hook.resolve_role("session_ddd", tmp_path) == "ouyangfeng"
