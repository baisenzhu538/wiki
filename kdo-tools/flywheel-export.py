#!/usr/bin/env python3
"""Export flywheel log as human-readable markdown to desktop."""
import sqlite3, sys
from datetime import datetime
from pathlib import Path

WIKI = Path(__file__).resolve().parent.parent
DB = WIKI / ".kdo" / "state.sqlite"
DESKTOP = Path.home() / "Desktop"

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

conn = sqlite3.connect(str(DB))
conn.row_factory = sqlite3.Row
rows = conn.execute("SELECT * FROM flywheel_log ORDER BY ts DESC").fetchall()
conn.close()

now = datetime.now().strftime("%Y-%m-%d %H:%M")
lines = [
    f"# KDO 飞轮日志 — {now}",
    f"",
    f"共 {len(rows)} 条迭代记录",
    f"",
    f"| 时间 | Agent | 类型 | Before | After | 为什么更好 | 下次尝试 |",
    f"|---|---|---|---|---|---|---|",
]

for r in rows:
    ts = r["ts"][:16] if r["ts"] else ""
    agent = r["agent_id"] or ""
    ttype = r["triangle_type"] or ""
    before = (r["before_note"] or "")[:50]
    after = (r["after_note"] or "")[:50]
    why = (r["why_better"] or "")[:50]
    next_try = (r["next_try"] or "")[:40]
    lines.append(f"| {ts} | {agent} | {ttype} | {before} | {after} | {why} | {next_try} |")

out = DESKTOP / "KDO-飞轮日志.md"
out.write_text("\n".join(lines), encoding="utf-8")
print(f"Exported {len(rows)} entries → {out}")
