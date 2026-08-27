#!/usr/bin/env python3
"""kdo_session_heartbeat_hook.py — #562 任务2：kimi-cli SessionHeartbeat 钩（会话活跃=心跳补面）。

挂法（~/.kimi-code/config.toml）：
    [[hooks]]
    event = "SessionHeartbeat"
    command = "python C:/Users/Administrator/Desktop/wiki/kdo-tools/kdo_session_heartbeat_hook.py"

语义：CLI 会话活着（SessionHeartbeat 每 60s 一拍）→ 按 session_id 解析角色 →
role_registry.heartbeat(role, tool="kimi-cli")。补上「人在会话里回话但没跑 kdo 命令」
的活性盲区（08-27 王语嫣误报实证：active 回话中却被判全实例死亡）。

角色解析：payload.session_id → 缓存（90_control/session-roles.json）→
会话目录 state.json 的 title（首条用户消息自动生成，含「你是<角色>」），匹配五角色
中/拼音名。解析不出=不写心跳（fail-open，绝不误写别的角色）。

纪律：永远 exit 0、静默（stdout 会进上下文）；任何异常吞掉。
"""
import json
import re
import sys
from pathlib import Path

WIKI_ROOT = Path(__file__).resolve().parent.parent
SESSIONS_ROOT = Path.home() / ".kimi-code" / "sessions"
CACHE = WIKI_ROOT / "90_control" / "session-roles.json"

ROLE_ALIASES = {
    "huangyaoshi": "huangyaoshi", "黄药师": "huangyaoshi",
    "laowantong": "laowantong", "老顽童": "laowantong",
    "wangyuyan": "wangyuyan", "王语嫣": "wangyuyan",
    "ouyangfeng": "ouyangfeng", "欧阳锋": "ouyangfeng",
    "fengqingyang": "fengqingyang", "风清扬": "fengqingyang",
}


def _load_cache() -> dict:
    try:
        data = json.loads(CACHE.read_text(encoding="utf-8"))
        return data if isinstance(data, dict) else {}
    except Exception:
        return {}


def _save_cache(cache: dict) -> None:
    try:
        tmp = CACHE.with_suffix(".tmp")
        tmp.write_text(json.dumps(cache, ensure_ascii=False, indent=1), encoding="utf-8")
        tmp.replace(CACHE)
    except Exception:
        pass


def resolve_role(session_id: str, sessions_root: Path = SESSIONS_ROOT) -> str | None:
    """session_id → 拼音角色名；解析不出返回 None。"""
    cache = _load_cache()
    if session_id in cache:
        return cache[session_id]
    for state_file in sessions_root.glob(f"*/{session_id}/state.json"):
        try:
            title = json.loads(state_file.read_text(encoding="utf-8")).get("title", "")
        except Exception:
            continue
        for alias, role in ROLE_ALIASES.items():
            if alias in title:
                cache[session_id] = role
                _save_cache(cache)
                return role
    return None


def main() -> int:
    try:
        payload = json.load(sys.stdin)
        sid = payload.get("session_id", "")
        if sid:
            role = resolve_role(sid)
            if role:
                sys.path.insert(0, str(WIKI_ROOT / "90_control" / "scripts"))
                import role_registry
                role_registry.heartbeat(role, tool="kimi-cli", kind="cli",
                                        session_scope=payload.get("cwd"))
    except Exception:
        pass
    return 0


if __name__ == "__main__":
    sys.exit(main())
