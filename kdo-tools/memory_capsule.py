#!/usr/bin/env python3
"""memory_capsule.py — 记忆胶囊事件库（#432/#463，F-044 改名 L1）。

事件指针层：SQLite 主库（git 外）+ 第二盘镜像 + verify 可恢复证明。
L1 全量原文库见 l1_capture.py；L2/L3 不在本单。

A 主库：C:\\Users\\Administrator\\.kdo-memory\\L0\\activity_log.db（WAL 模式，git 外）
B 镜像：D:\\KDO-memory\\L0-backup\\（robocopy /MIR，先 checkpoint 再拷——WAL 合库防半写）

用法：
  python kdo-tools/memory_capsule.py init                        # 建 A 主库（幂等）
  python kdo-tools/memory_capsule.py log --agent <id> --event <type> [--payload <text>] [--session <id>]
  python kdo-tools/memory_capsule.py mirror                      # A → B（robocopy /MIR）
  python kdo-tools/memory_capsule.py status                      # 行数/最新 ts/WAL 完整性/B 状态
  python kdo-tools/memory_capsule.py verify                      # B 可恢复校验（hash 对比 + integrity）
  python kdo-tools/memory_capsule.py restore --to <dir>          # 从 B 恢复到指定目录（演练）

「可恢复」声明必须附 verify 输出；不附=未验证（#432 边界）。
"""

import argparse
import hashlib
import json
import sqlite3
import subprocess
import sys
import time
from datetime import datetime, timezone
from pathlib import Path

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")

A_DIR = Path.home() / ".kdo-memory" / "L1"  # F-044：L0→L1 改名（#463 顺带）
A_DB = A_DIR / "activity_log.db"
B_DIR = Path("D:/KDO-memory/L1-backup")  # F-044
SCHEMA = """
CREATE TABLE IF NOT EXISTS activity_log (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    agent_id TEXT NOT NULL,
    session_id TEXT,
    ts TEXT NOT NULL,
    event_type TEXT NOT NULL,
    payload_summary TEXT,
    payload_hash TEXT
);
"""


def _utcnow() -> str:
    return datetime.now(timezone.utc).isoformat()


def _sha256(text: str | bytes) -> str:
    data = text.encode("utf-8") if isinstance(text, str) else text
    return hashlib.sha256(data).hexdigest()


def _connect(db_path: Path) -> sqlite3.Connection:
    conn = sqlite3.connect(str(db_path))
    conn.execute("PRAGMA journal_mode=WAL")
    conn.execute("PRAGMA busy_timeout=5000")
    return conn


def cmd_init() -> int:
    A_DIR.mkdir(parents=True, exist_ok=True)
    conn = _connect(A_DB)
    conn.execute(SCHEMA)
    conn.commit()
    conn.close()
    print(f"✅ A 主库就绪: {A_DB}（WAL 模式）")
    return 0


def cmd_log(agent: str, event: str, payload: str | None, session: str | None) -> int:
    if not A_DB.exists():
        print("A 主库不存在，先跑 init", file=sys.stderr)
        return 1
    conn = _connect(A_DB)
    summary = (payload or "")[:1000]
    cur = conn.execute(
        "INSERT INTO activity_log (agent_id, session_id, ts, event_type, payload_summary, payload_hash) VALUES (?,?,?,?,?,?)",
        (agent, session, _utcnow(), event, summary, _sha256(payload or "")),
    )
    conn.commit()
    row_id = cur.lastrowid
    conn.close()
    print(f"✅ 事件 #{row_id} 已写入: agent={agent} event={event}")
    return 0


def _checkpoint(conn: sqlite3.Connection) -> None:
    """WAL 合库（TRUNCATE）——镜像前调用，防备份到半写 WAL。"""
    try:
        conn.execute("PRAGMA wal_checkpoint(TRUNCATE)")
    except sqlite3.OperationalError:
        pass  # 无 WAL 时忽略


def cmd_mirror() -> int:
    if not A_DB.exists():
        print("A 主库不存在，先跑 init", file=sys.stderr)
        return 1
    conn = _connect(A_DB)
    _checkpoint(conn)
    conn.close()
    B_DIR.mkdir(parents=True, exist_ok=True)
    # robocopy /MIR：镜像 A 目录 → B（含 db/wal/shm）；/NJH /NJS 静默头尾
    r = subprocess.run(
        ["robocopy", str(A_DIR), str(B_DIR), "/MIR", "/NJH", "/NJS", "/NP"],
        capture_output=True, text=True, encoding="utf-8", errors="replace",
    )
    # robocopy 退出码：0-7 为成功（8+ 为错误）
    if r.returncode >= 8:
        print(f"❌ robocopy 失败（exit {r.returncode}）", file=sys.stderr)
        print(r.stdout[-500:], file=sys.stderr)
        return 1
    print(f"✅ A → B 镜像完成: {A_DIR} → {B_DIR}（robocopy /MIR，exit {r.returncode}）")
    return 0


def _db_stats(db_path: Path) -> dict:
    conn = _connect(db_path)
    count = conn.execute("SELECT COUNT(*) FROM activity_log").fetchone()[0]
    latest = conn.execute("SELECT MAX(ts) FROM activity_log").fetchone()[0]
    integrity = conn.execute("PRAGMA integrity_check").fetchone()[0]
    conn.close()
    return {"count": count, "latest_ts": latest, "integrity": integrity}


def cmd_status() -> int:
    if not A_DB.exists():
        print("❌ A 主库不存在（未 init）")
        return 1
    s = _db_stats(A_DB)
    b_ok = (B_DIR / "activity_log.db").exists()
    print(f"A 主库: {A_DB}")
    print(f"  行数: {s['count']} | 最新 ts: {s['latest_ts']} | integrity: {s['integrity']}")
    print(f"B 镜像: {'✅ 存在' if b_ok else '❌ 缺失（跑 mirror）'} {B_DIR}")
    return 0


def cmd_verify() -> int:
    """B 可恢复校验：文件 hash 对比 + 从 B 打开跑 integrity + 行数一致。"""
    if not (B_DIR / "activity_log.db").exists():
        print("❌ B 镜像缺失，先跑 mirror", file=sys.stderr)
        return 1
    mismatches = []
    for name in ("activity_log.db", "activity_log.db-wal", "activity_log.db-shm"):
        a = A_DIR / name
        b = B_DIR / name
        if a.exists() != b.exists():
            mismatches.append(f"{name}: 存在性不一致（A={a.exists()} B={b.exists()}）")
            continue
        if a.exists() and _sha256(a.read_bytes()) != _sha256(b.read_bytes()):
            mismatches.append(f"{name}: hash 不一致")
    if mismatches:
        print("❌ verify FAIL：")
        for m in mismatches:
            print(f"  - {m}")
        return 1
    # 从 B 打开校验（可恢复性证明）
    b_stats = _db_stats(B_DIR / "activity_log.db")
    a_stats = _db_stats(A_DB)
    ok = b_stats["integrity"] == "ok" and b_stats["count"] == a_stats["count"]
    print(f"✅ verify PASS：B 镜像文件 hash 全一致；从 B 打开 integrity={b_stats['integrity']} 行数 {b_stats['count']}（A 同 {a_stats['count']}）")
    return 0 if ok else 1


def cmd_restore(to: str) -> int:
    """从 B 恢复到指定目录（演练用：删 A 后恢复）。verify 恢复结果。"""
    if not (B_DIR / "activity_log.db").exists():
        print("❌ B 镜像缺失，先跑 mirror", file=sys.stderr)
        return 1
    dst = Path(to)
    dst.mkdir(parents=True, exist_ok=True)
    for name in ("activity_log.db", "activity_log.db-wal", "activity_log.db-shm"):
        src = B_DIR / name
        if src.exists():
            (dst / name).write_bytes(src.read_bytes())
    s = _db_stats(dst / "activity_log.db")
    ok = s["integrity"] == "ok"
    print(f"✅ 恢复演练: B → {dst}；integrity={s['integrity']} 行数={s['count']}")
    return 0 if ok else 1


def main() -> int:
    p = argparse.ArgumentParser(description="记忆胶囊 L0（#432）：全量留痕 + 第二盘镜像 + verify")
    sub = p.add_subparsers(dest="cmd", required=True)
    sub.add_parser("init", help="建 A 主库（幂等）")
    plog = sub.add_parser("log", help="写入事件")
    plog.add_argument("--agent", required=True)
    plog.add_argument("--event", required=True)
    plog.add_argument("--payload", default=None)
    plog.add_argument("--session", default=None)
    sub.add_parser("mirror", help="A → B（robocopy /MIR，先 checkpoint）")
    sub.add_parser("status", help="A/B 状态")
    sub.add_parser("verify", help="B 可恢复校验")
    prestore = sub.add_parser("restore", help="从 B 恢复到指定目录")
    prestore.add_argument("--to", required=True)
    args = p.parse_args()

    if args.cmd == "init":
        return cmd_init()
    if args.cmd == "log":
        return cmd_log(args.agent, args.event, args.payload, args.session)
    if args.cmd == "mirror":
        return cmd_mirror()
    if args.cmd == "status":
        return cmd_status()
    if args.cmd == "verify":
        return cmd_verify()
    if args.cmd == "restore":
        return cmd_restore(args.to)
    return 1


if __name__ == "__main__":
    sys.exit(main())
