#!/usr/bin/env python3
"""
Agent 实测对话存储。用于飞轮加速：每次Agent会话后，存储结构化trace，下次迭代时回放对比。

Usage:
  python kdo-tools/agent-trace.py save --agent <id> --scenario <描述> --trace <对话文本路径>
  python kdo-tools/agent-trace.py list --agent <id>
  python kdo-tools/agent-trace.py compare --scenario <描述>  # 对比同一场景的多次迭代
"""

import argparse
import json
import sqlite3
import sys
from datetime import datetime, timezone
from pathlib import Path

WIKI = Path(__file__).resolve().parent.parent
DB = WIKI / ".kdo" / "state.sqlite"
TRACE_DIR = WIKI / "60_feedback" / "agent-traces"

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

def now_iso():
    return datetime.now(timezone.utc).isoformat()

def init_table():
    conn = sqlite3.connect(str(DB))
    conn.executescript("""
        CREATE TABLE IF NOT EXISTS agent_traces (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            ts TEXT NOT NULL,
            agent_id TEXT NOT NULL,
            scenario TEXT NOT NULL,
            trace_path TEXT NOT NULL,
            key_findings TEXT,
            updated_at TEXT NOT NULL
        );
        CREATE INDEX IF NOT EXISTS idx_agent_traces_agent ON agent_traces(agent_id);
        CREATE INDEX IF NOT EXISTS idx_agent_traces_scenario ON agent_traces(scenario);
    """)
    conn.commit()
    conn.close()

def cmd_save(args):
    init_table()
    TRACE_DIR.mkdir(parents=True, exist_ok=True)

    trace_src = Path(args.trace)
    if not trace_src.exists():
        print(f"ERROR: Trace file not found: {trace_src}", file=sys.stderr)
        return 1

    ts = now_iso()
    safe_name = args.agent + "-" + ts[:10] + "-" + args.scenario[:30].replace(" ", "-").replace("/", "-")
    dest = TRACE_DIR / f"{safe_name}.md"
    dest.write_text(trace_src.read_text(encoding="utf-8", errors="ignore"), encoding="utf-8")

    conn = sqlite3.connect(str(DB))
    conn.execute(
        "INSERT INTO agent_traces (ts, agent_id, scenario, trace_path, key_findings, updated_at) VALUES (?,?,?,?,?,?)",
        (ts, args.agent, args.scenario, str(dest.relative_to(WIKI)), args.findings or "", ts),
    )
    conn.commit()

    # Count iterations for this scenario
    count = conn.execute(
        "SELECT COUNT(*) FROM agent_traces WHERE agent_id=? AND scenario=?",
        (args.agent, args.scenario),
    ).fetchone()[0]
    conn.close()

    print(f"Trace saved: {dest.relative_to(WIKI)}")
    print(f"  Agent: {args.agent} | Scenario: {args.scenario} | Iteration #{count}")
    if count >= 3:
        print(f"  🔴 同一场景已积累 {count} 次迭代——该做 before-after 对比了：python kdo-tools/agent-trace.py compare --scenario '{args.scenario}'")
    return 0

def cmd_list(args):
    init_table()
    conn = sqlite3.connect(str(DB))
    conn.row_factory = sqlite3.Row

    where = "WHERE agent_id = ?" if args.agent else ""
    params = (args.agent,) if args.agent else ()

    rows = conn.execute(
        f"SELECT ts, agent_id, scenario, key_findings FROM agent_traces {where} ORDER BY ts DESC LIMIT 20",
        params,
    ).fetchall()

    print(f"Agent 实测记录 ({len(rows)} 条)")
    print(f"{'='*60}")
    for r in rows:
        print(f"  [{r['ts'][:16]}] {r['agent_id']} | {r['scenario'][:50]}")
        if r['key_findings']:
            print(f"    {r['key_findings'][:100]}")
    conn.close()
    return 0

def cmd_compare(args):
    init_table()
    conn = sqlite3.connect(str(DB))
    conn.row_factory = sqlite3.Row

    rows = conn.execute(
        "SELECT ts, agent_id, trace_path, key_findings FROM agent_traces WHERE scenario = ? ORDER BY ts",
        (args.scenario,),
    ).fetchall()
    conn.close()

    if len(rows) < 2:
        print(f"只有 {len(rows)} 次迭代——需要至少2次才能对比")
        return 0

    print(f"场景对比: {args.scenario} ({len(rows)} 次迭代)")
    print(f"{'='*60}")
    for i, r in enumerate(rows, 1):
        print(f"\n  #{i} [{r['ts'][:16]}] {r['agent_id']}")
        if r['key_findings']:
            print(f"  发现: {r['key_findings'][:120]}")
    print(f"\n💡 建议: 同一场景 {len(rows)} 次迭代——运行飞轮模式检测：python kdo-tools/flywheel.py pattern --agent {rows[0]['agent_id']}")
    return 0

def main():
    parser = argparse.ArgumentParser(description="Agent 实测对话存储")
    sub = parser.add_subparsers(dest="cmd", required=True)

    p_save = sub.add_parser("save", help="保存一次 Agent 实测对话")
    p_save.add_argument("--agent", required=True)
    p_save.add_argument("--scenario", required=True)
    p_save.add_argument("--trace", required=True, help="对话文本路径")
    p_save.add_argument("--findings", default="", help="关键发现")

    p_list = sub.add_parser("list", help="列出 Agent 实测记录")
    p_list.add_argument("--agent", default="")

    p_compare = sub.add_parser("compare", help="对比同一场景的多次迭代")
    p_compare.add_argument("--scenario", required=True)

    args = parser.parse_args()
    if args.cmd == "save":
        return cmd_save(args)
    elif args.cmd == "list":
        return cmd_list(args)
    elif args.cmd == "compare":
        return cmd_compare(args)

if __name__ == "__main__":
    sys.exit(main())
