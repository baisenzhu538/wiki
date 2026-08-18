"""KDO Time Capsule Sync - Regenerate CAPSULE_STARTUP.md from database.

v2 兼容（#366）：目标文件若为 v2 启动指针（含 "启动指针" 与 "version: 2.0"），
保留 §0 版本校验 / §1 启动流程 / §2 角色路由（静态约定，由 agent 维护），
仅从 time-capsule.db 再生 §3 角色身份卡与 §4 Shared State。
文件缺失或为 v1 时维持旧行为（全量 v1 再生）。
"""
import sqlite3, os

DB = os.path.join(os.path.dirname(os.path.abspath(__file__)), "time-capsule.db")
db = sqlite3.connect(DB)
db.row_factory = sqlite3.Row


def build_roles_block() -> list[str]:
    lines = ["## 3 · 角色身份卡", ""]
    for agent in db.execute("SELECT * FROM agents ORDER BY role_type, name"):
        aid = agent["id"]
        lines.append("### " + agent["name"] + " (" + agent["role_name"] + ")")
        lines.append("- id: " + aid + "  |  type: " + (agent["role_type"] or "") + "  |  interface: " + (agent["interface"] or ""))
        identity = db.execute("SELECT value FROM memories WHERE agent_id=? AND key='identity'", (aid,)).fetchone()
        if identity:
            lines.append("- identity: " + identity["value"])
        for m in db.execute("SELECT key, value FROM memories WHERE agent_id=? AND key!='identity' ORDER BY key", (aid,)):
            lines.append("- " + m["key"] + ": " + m["value"])
        cards = db.execute("SELECT * FROM behavior_cards WHERE agent_id=? ORDER BY card_id", (aid,)).fetchall()
        if cards:
            lines.append("- cards: " + " | ".join([c["card_id"] + "=" + c["action"] for c in cards]))
        lines.append("")
    return lines


def build_shared_block() -> list[str]:
    lines = ["## 4 · Shared State"]
    for s in db.execute("SELECT * FROM shared_state ORDER BY key"):
        lines.append("- " + s["key"] + ": " + s["value"])
    return lines


def build_legacy_v1() -> str:
    lines = ["# KDO Time Capsule - Agent Startup Recovery", ""]
    for agent in db.execute("SELECT * FROM agents ORDER BY role_type, name"):
        aid = agent["id"]
        lines.append("## " + agent["name"] + " (" + agent["role_name"] + ")")
        lines.append("- id: " + aid + "  |  type: " + (agent["role_type"] or "") + "  |  interface: " + (agent["interface"] or ""))
        identity = db.execute("SELECT value FROM memories WHERE agent_id=? AND key='identity'", (aid,)).fetchone()
        if identity:
            lines.append("- identity: " + identity["value"])
        for m in db.execute("SELECT key, value FROM memories WHERE agent_id=? AND key!='identity' ORDER BY key", (aid,)):
            lines.append("- " + m["key"] + ": " + m["value"])
        cards = db.execute("SELECT * FROM behavior_cards WHERE agent_id=? ORDER BY card_id", (aid,)).fetchall()
        if cards:
            lines.append("- cards: " + " | ".join([c["card_id"] + "=" + c["action"] for c in cards]))
        lines.append("")
    lines.append("## Shared State")
    for s in db.execute("SELECT * FROM shared_state ORDER BY key"):
        lines.append("- " + s["key"] + ": " + s["value"])
    db.close()
    return "\n".join(lines)


out_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "CAPSULE_STARTUP.md")
existing = ""
if os.path.exists(out_path):
    with open(out_path, "r", encoding="utf-8", errors="replace") as f:
        existing = f.read()

if "启动指针" in existing and "version: 2.0" in existing:
    # v2 模式：保留 §0/§1/§2（静态约定），再生 §3 + §4
    prefix = existing.split("## 3 · 角色身份卡")[0].rstrip()
    content = (
        prefix
        + "\n\n"
        + "\n".join(build_roles_block())
        + "\n\n"
        + "\n".join(build_shared_block())
        + "\n"
    )
else:
    content = build_legacy_v1()

with open(out_path, "w", encoding="utf-8") as f:
    f.write(content)
print("capsule synced: " + out_path)
