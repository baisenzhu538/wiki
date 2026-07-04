#!/usr/bin/env python3
"""
Agent 总控面板：健康监控 + 飞轮转速 + 迭代状态

Usage:
  python kdo-tools/agent-status.py
  python kdo-tools/agent-status.py --days 14
"""

import argparse
import sqlite3
import sys
from collections import Counter
from datetime import datetime, timezone
from pathlib import Path

WIKI = Path(__file__).resolve().parent.parent
DB = WIKI / ".kdo" / "state.sqlite"
AGENTS_DIR = WIKI / "agents"
TOOLS_DIR = WIKI / "30_wiki" / "tools"
SYSTEMS_DIR = WIKI / "30_wiki" / "systems"

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")


def now_iso():
    return datetime.now(timezone.utc).isoformat()


def discover_agents() -> list[dict]:
    """Find all agents from agents/ directory and agent-spec cards."""
    agents = {}

    # From agents/ directory
    if AGENTS_DIR.exists():
        for d in AGENTS_DIR.iterdir():
            if d.is_dir() and (d / "CLAUDE.md").exists():
                agents[d.name] = {"id": d.name, "source": "agents/", "title": d.name}

    # From agent-spec cards
    for d in (TOOLS_DIR, SYSTEMS_DIR):
        if not d.exists():
            continue
        for p in d.glob("*.md"):
            try:
                text = p.read_text(encoding="utf-8", errors="ignore")
                if "agent-spec" in text[:500].lower() or "tool-agent-spec" in str(p):
                    pass  # continue to parse
                else:
                    continue
            except Exception:
                continue

            import yaml
            try:
                fm, _ = p.read_text(encoding="utf-8", errors="ignore").split("---", 2)[:2]
                fm = yaml.safe_load(fm) or {}
            except Exception:
                continue

            agent_id = fm.get("id", p.stem)
            if agent_id not in agents:
                agents[agent_id] = {
                    "id": agent_id,
                    "source": "30_wiki/",
                    "title": fm.get("title", p.stem),
                }

    # Also include agents that only appear in flywheel log (e.g. Claude Code CLI agents like huangyaoshi)
    if DB.exists():
        conn = sqlite3.connect(str(DB))
        flywheel_agents = conn.execute("SELECT DISTINCT agent_id FROM flywheel_log").fetchall()
        conn.close()
        for (aid,) in flywheel_agents:
            if aid not in agents:
                agents[aid] = {"id": aid, "source": "flywheel", "title": aid}

    return list(agents.values())


def get_flywheel_stats(days: int) -> dict:
    """Get flywheel stats per agent from SQLite."""
    if not DB.exists():
        return {}

    conn = sqlite3.connect(str(DB))
    conn.row_factory = sqlite3.Row

    stats = {}
    rows = conn.execute(
        f"""SELECT agent_id,
                   COUNT(*) as total,
                   MAX(ts) as last_ts,
                   SUM(CASE WHEN reflow_status='pending' THEN 1 ELSE 0 END) as pending
            FROM flywheel_log
            WHERE ts > date('now', '-{days} days')
            GROUP BY agent_id"""
    ).fetchall()

    for r in rows:
        stats[r["agent_id"]] = {
            "total": r["total"],
            "last_ts": r["last_ts"][:10] if r["last_ts"] else "never",
            "pending": r["pending"],
        }

    # Get type distribution for each agent
    type_rows = conn.execute(
        f"""SELECT agent_id, triangle_type, COUNT(*) as cnt
            FROM flywheel_log
            WHERE ts > date('now', '-{days} days')
            GROUP BY agent_id, triangle_type"""
    ).fetchall()

    for r in type_rows:
        if r["agent_id"] in stats:
            if "types" not in stats[r["agent_id"]]:
                stats[r["agent_id"]]["types"] = {}
            stats[r["agent_id"]]["types"][r["triangle_type"]] = r["cnt"]

    conn.close()
    return stats


def main():
    parser = argparse.ArgumentParser(description="Agent 总控面板")
    parser.add_argument("--days", type=int, default=14, help="统计天数")
    args = parser.parse_args()

    agents = discover_agents()
    flywheel = get_flywheel_stats(args.days)

    print(f"Agent 总控面板 — {now_iso()[:19]}")
    print(f"{'='*70}")

    # Summary
    active = sum(1 for a in agents if flywheel.get(a["id"], {}).get("total", 0) > 0)
    iterating = sum(1 for a in agents if flywheel.get(a["id"], {}).get("total", 0) >= 3)
    stale = sum(1 for a in agents if flywheel.get(a["id"], {}).get("total", 0) == 0)

    print(f"\n发现 {len(agents)} 个 Agent")
    print(f"  活跃（{args.days}天内有记录）: {active}")
    print(f"  正在迭代（≥3次）: {iterating}")
    print(f"  待启动（无记录）: {stale}")

    # Per-agent detail
    print(f"\n{'Agent':<35} {'迭代':<5} {'最近':<12} {'待回流':<5} {'状态':<10} {'回路分布'}")
    print(f"{'-'*35} {'-'*5} {'-'*12} {'-'*5} {'-'*10} {'-'*20}")

    for a in sorted(agents, key=lambda x: flywheel.get(x["id"], {}).get("total", 0), reverse=True):
        fw = flywheel.get(a["id"], {})
        total = fw.get("total", 0)
        last = fw.get("last_ts", "—")
        pending = fw.get("pending", 0)
        types = fw.get("types", {})

        if total >= 3:
            health = "🟢 迭代中"
        elif total > 0:
            health = "🟡 启动中"
        else:
            health = "⚪ 待启动"

        type_str = " ".join(f"{t}:{c}" for t, c in sorted(types.items(), key=lambda x: -x[1])[:4])
        print(f"  {a['id']:<33} {total:<5} {last:<12} {pending:<5} {health:<10} {type_str}")

    # Warnings
    print(f"\n{'='*70}")
    pending_total = sum(fw.get("pending", 0) for fw in flywheel.values())
    if pending_total > 0:
        print(f"⚠️  {pending_total} 条待回流记录。运行 flywheel.py pattern 查看加速信号。")

    if stale > 0 and active > 0:
        print(f"💡 {stale} 个 Agent 尚未启动飞轮。建议首次实测后立即记录一条 before-after。")

    return 0


if __name__ == "__main__":
    sys.exit(main())
