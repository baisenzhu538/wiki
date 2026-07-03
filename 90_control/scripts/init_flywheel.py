"""Initialize the 双三角 flywheel log table in KDO SQLite state."""
import sqlite3
import sys
from pathlib import Path

WIKI = Path(__file__).resolve().parent.parent.parent
DB = WIKI / ".kdo" / "state.sqlite"

SQL = """
CREATE TABLE IF NOT EXISTS flywheel_log (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    ts TEXT NOT NULL,
    agent_id TEXT NOT NULL,
    session_id TEXT,
    -- Before-After comparison (聪美模式)
    before_note TEXT,       -- "之前我是怎么做的"
    after_note TEXT,        -- "这次做了什么改变"
    why_better TEXT,        -- "为什么更好"
    next_try TEXT,          -- "下次尝试什么"
    -- 双三角六要素分类
    triangle_type TEXT,     -- 审美 / 体系 / 创造力 / 场景 / 数据 / 基本功
    impact_loop TEXT,       -- 审美场景 / 体系数据 / 创造基本功
    -- 回流目标
    target_card TEXT,       -- 应更新哪张卡
    reflow_status TEXT DEFAULT 'pending',  -- pending / applied / rejected
    updated_at TEXT NOT NULL
);

CREATE INDEX IF NOT EXISTS idx_flywheel_agent ON flywheel_log(agent_id);
CREATE INDEX IF NOT EXISTS idx_flywheel_triangle ON flywheel_log(triangle_type);
CREATE INDEX IF NOT EXISTS idx_flywheel_ts ON flywheel_log(ts);
CREATE INDEX IF NOT EXISTS idx_flywheel_reflow ON flywheel_log(reflow_status);
"""

def init():
    if not DB.exists():
        print("ERROR: state.sqlite not found. Run kdo status first.", file=sys.stderr)
        return 1
    conn = sqlite3.connect(str(DB))
    conn.executescript(SQL)
    conn.commit()
    conn.close()
    print("flywheel_log table ready.")
    return 0

if __name__ == "__main__":
    sys.exit(init())
