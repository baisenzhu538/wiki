"""Backup .kdo/state.sqlite to git-tracked JSON in .kdo/backups/."""
import json
import sqlite3
import sys
from datetime import datetime, timezone
from pathlib import Path

WIKI = Path(__file__).resolve().parent.parent.parent
DB = WIKI / ".kdo" / "state.sqlite"
BACKUP_DIR = WIKI / ".kdo" / "backups"


def backup():
    if not DB.exists():
        print("No SQLite database to backup.", file=sys.stderr)
        return 1

    BACKUP_DIR.mkdir(parents=True, exist_ok=True)
    conn = sqlite3.connect(str(DB))

    # Export key tables as JSON
    tables = ["flywheel_log", "zhu_decisions"]
    for t in tables:
        try:
            rows = conn.execute(f"SELECT * FROM {t}").fetchall()
            cols = [d[0] for d in conn.execute(f"PRAGMA table_info({t})").fetchall()]
            data = [dict(zip(cols, r)) for r in rows]
            out = BACKUP_DIR / f"{t}.json"
            out.write_text(json.dumps(data, ensure_ascii=False, indent=2, default=str), encoding="utf-8")
            print(f"  {t}: {len(data)} rows → {out.name}")
        except sqlite3.OperationalError:
            pass

    conn.close()

    # Write timestamp
    ts = datetime.now(timezone.utc).isoformat()
    (BACKUP_DIR / ".last_backup").write_text(ts)
    print(f"Backup complete: {ts}")
    return 0


if __name__ == "__main__":
    sys.exit(backup())
