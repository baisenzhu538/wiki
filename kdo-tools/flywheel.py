#!/usr/bin/env python3
"""
双三角飞轮引擎：记录每次Agent会话的 before-after 迭代。

Usage:
  python kdo-tools/flywheel.py log --agent <id> --type <审美|体系|创造力|场景|数据|基本功> [--before <...> --after <...> --why <...> --next <...>]
  python kdo-tools/flywheel.py status [--days 21] [--agent <id>]
  python kdo-tools/flywheel.py pattern [--days 21]   # 检测重复模式
"""

import argparse
import sqlite3
import sys
from collections import Counter
from datetime import datetime, timezone
from pathlib import Path

# Fix Windows GBK encoding
if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")
if hasattr(sys.stderr, "reconfigure"):
    sys.stderr.reconfigure(encoding="utf-8")

WIKI = Path(__file__).resolve().parent.parent
DB = WIKI / ".kdo" / "state.sqlite"


def now_iso():
    return datetime.now(timezone.utc).isoformat()


def cmd_log(args):
    if not DB.exists():
        print("ERROR: state.sqlite not found.", file=sys.stderr)
        return 1

    conn = sqlite3.connect(str(DB))
    conn.execute(
        """INSERT INTO flywheel_log
           (ts, agent_id, triangle_type, before_note, after_note, why_better, next_try, updated_at)
           VALUES (?, ?, ?, ?, ?, ?, ?, ?)""",
        (now_iso(), args.agent, args.type, args.before, args.after, args.why, args.next, now_iso()),
    )
    conn.commit()
    conn.close()
    # Auto-backup + export to desktop after every log entry
    import subprocess
    subprocess.run([sys.executable, str(WIKI / "90_control" / "scripts" / "backup-sqlite.py")],
                   capture_output=True)
    subprocess.run([sys.executable, str(WIKI / "kdo-tools" / "flywheel-export.py")],
                   capture_output=True)
    print(f"飞轮日志已记录: agent={args.agent} type={args.type}")
    return 0


def _where_clause(agent_id, days):
    """Return (where_sql, params). days is inserted directly for SQLite date math."""
    params = []
    where = f"ts > date('now', '-{days} days')"
    if agent_id:
        where += " AND agent_id = ?"
        params.append(agent_id)
    return where, params


def cmd_status(args):
    if not DB.exists():
        print("Flywheel not initialized. Run kdo status first.")
        return 1

    days = args.days
    where, params = _where_clause(args.agent, days)

    conn = sqlite3.connect(str(DB))
    conn.row_factory = sqlite3.Row

    total = conn.execute(
        f"SELECT COUNT(*) as cnt FROM flywheel_log WHERE {where}", params
    ).fetchone()["cnt"]

    by_type = conn.execute(
        f"""SELECT triangle_type, COUNT(*) as cnt FROM flywheel_log
            WHERE {where}
            GROUP BY 1 ORDER BY cnt DESC""",
        params,
    ).fetchall()

    loop_where = f"{where} AND impact_loop != ''"
    by_loop = conn.execute(
        f"""SELECT impact_loop, COUNT(*) as cnt FROM flywheel_log
            WHERE {loop_where}
            GROUP BY 1 ORDER BY cnt DESC""",
        params,
    ).fetchall()

    pending = conn.execute(
        "SELECT COUNT(*) as cnt FROM flywheel_log WHERE reflow_status = 'pending'"
    ).fetchone()["cnt"]

    recent = conn.execute(
        f"""SELECT agent_id, triangle_type, before_note, after_note, why_better
            FROM flywheel_log
            WHERE {where}
            ORDER BY ts DESC LIMIT 5""",
        params,
    ).fetchall()

    print(f"飞轮状态 (最近 {days} 天)")
    print(f"{'='*50}")
    print(f"  总记录: {total}")
    print(f"  待回流: {pending}")
    print()
    print("按类型分布:")
    for r in by_type:
        print(f"  {r['triangle_type']}: {r['cnt']}")
    print()
    print("按回路分布:")
    for r in by_loop:
        print(f"  {r['impact_loop']}: {r['cnt']}")
    print()
    print("最近 5 条:")
    for r in recent:
        print(f"  [{r['agent_id']}] {r['triangle_type']}: {r['before_note'][:60]} → {r['after_note'][:60]}")
        if r['why_better']:
            print(f"    为什么更好: {r['why_better'][:80]}")

    conn.close()
    return 0


def cmd_restore(args):
    """Restore flywheel_log and zhu_decisions from JSON backups to SQLite."""
    import json
    backups = WIKI / ".kdo" / "backups"
    if not backups.exists():
        print("No backups found. Run on the original machine first.", file=sys.stderr)
        return 1

    conn = sqlite3.connect(str(DB))
    restored = 0

    for t in ["flywheel_log", "zhu_decisions"]:
        bf = backups / f"{t}.json"
        if not bf.exists():
            continue
        data = json.loads(bf.read_text(encoding="utf-8"))
        if not data:
            continue
        cols = list(data[0].keys())
        placeholders = ",".join(["?"] * len(cols))
        for row in data:
            try:
                conn.execute(
                    f"INSERT OR IGNORE INTO {t} ({','.join(cols)}) VALUES ({placeholders})",
                    [row.get(c) for c in cols],
                )
                restored += 1
            except sqlite3.OperationalError:
                pass
        conn.commit()
        print(f"  {t}: {len(data)} rows restored")

    conn.commit()
    conn.close()
    print(f"Restore complete: {restored} total rows")
    return 0


def cmd_pattern(args):
    """Detect repeating patterns in flywheel log — signals for acceleration."""
    days = args.days
    where, params = _where_clause(args.agent, days)

    conn = sqlite3.connect(str(DB))
    conn.row_factory = sqlite3.Row

    # Find triangle types that appear >=3 times — acceleration signal
    frequent = conn.execute(
        f"""SELECT triangle_type, COUNT(*) as cnt FROM flywheel_log
            WHERE {where}
            GROUP BY 1 HAVING cnt >= 3 ORDER BY cnt DESC""",
        params,
    ).fetchall()

    # Find agents with most iterations
    top_agents = conn.execute(
        f"""SELECT agent_id, COUNT(*) as cnt FROM flywheel_log
            WHERE {where}
            GROUP BY 1 ORDER BY cnt DESC LIMIT 5""",
        params,
    ).fetchall()

    # Find pending reflows that have accumulated
    stale = conn.execute(
        """SELECT agent_id, triangle_type, before_note FROM flywheel_log
           WHERE reflow_status = 'pending' ORDER BY ts ASC LIMIT 5"""
    ).fetchall()

    print(f"飞轮模式检测 (最近 {days} 天)")
    print(f"{'='*50}")

    if frequent:
        print("\n🔴 加速信号（同一类型出现 ≥3 次，该回路该加速了）:")
        for r in frequent:
            print(f"  {r['triangle_type']}: {r['cnt']}次 — 飞轮该加速这个回路")
    else:
        print("\n🟢 无明显模式信号。继续积累。")

    if top_agents:
        print("\n📊 迭代最活跃的 Agent:")
        for r in top_agents:
            print(f"  {r['agent_id']}: {r['cnt']}次迭代")

    if stale:
        print(f"\n⚠️  {len(stale)} 条待回流记录，最早的是:")
        for r in stale[:3]:
            print(f"  [{r['agent_id']}] {r['triangle_type']}: {r['before_note'][:60]}")

    conn.close()
    return 0


def main():
    parser = argparse.ArgumentParser(description="双三角飞轮引擎")
    sub = parser.add_subparsers(dest="cmd", required=True)

    p_log = sub.add_parser("log", help="记录一条飞轮日志")
    p_log.add_argument("--agent", required=True)
    p_log.add_argument("--type", required=True, choices=["审美","体系","创造力","场景","数据","基本功"])
    p_log.add_argument("--before", default="")
    p_log.add_argument("--after", default="")
    p_log.add_argument("--why", default="")
    p_log.add_argument("--next", default="")

    p_status = sub.add_parser("status", help="飞轮状态概览")
    p_status.add_argument("--days", type=int, default=21)
    p_status.add_argument("--agent", default="")

    p_pattern = sub.add_parser("pattern", help="检测重复模式")
    p_pattern.add_argument("--days", type=int, default=21)
    p_pattern.add_argument("--agent", default="")

    p_restore = sub.add_parser("restore", help="从 JSON 备份恢复 SQLite（新电脑上执行）")
    p_restore.add_argument("--yes", action="store_true", help="确认恢复")

    args = parser.parse_args()
    if args.cmd == "log":
        return cmd_log(args)
    elif args.cmd == "status":
        return cmd_status(args)
    elif args.cmd == "pattern":
        return cmd_pattern(args)
    elif args.cmd == "restore":
        return cmd_restore(args)


if __name__ == "__main__":
    sys.exit(main())
