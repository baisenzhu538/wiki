#!/usr/bin/env python3
"""recovery-check.py — 非破坏性恢复演练（健壮性 L5 自动化，#主动立项 2026-08-24）。

每天从事件库镜像复制副本 → integrity_check + 行数——验证"镜像真能救数据"
（不破坏真实库，副本用完即删）。挂 health-check 每日自动。

容灾口径：git 即容灾（wiki 资产在 git 历史）；L1-full 可再生（源仍在，重采集即重建）；
本检查验证 D 盘事件库镜像恢复路径持续可用。

用法：
  python kdo-tools/recovery-check.py           # 副本恢复验证
  python kdo-tools/recovery-check.py --json    # JSON 输出
退出码：0=PASS；1=FAIL（镜像缺失/副本不可读/数据不一致）
"""

from __future__ import annotations

import argparse
import json
import shutil
import sqlite3
import sys
import tempfile
from pathlib import Path

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")

MIRROR_DIR = Path("D:/KDO-memory/L1-backup")          # 事件库镜像（D 盘）
MIRROR_DB = MIRROR_DIR / "activity_log.db"


def verify_restore() -> tuple[bool, str]:
    """从镜像复制副本 → integrity_check + 行数。返回 (ok, 摘要)。"""
    if not MIRROR_DB.exists():
        return False, f"镜像库缺失: {MIRROR_DB}"
    tmp = Path(tempfile.mkdtemp())
    try:
        dst = tmp / "restored.db"
        shutil.copy2(MIRROR_DB, dst)
        con = sqlite3.connect(dst)
        try:
            integrity = con.execute("PRAGMA integrity_check").fetchone()[0]
            rows = con.execute("SELECT COUNT(*) FROM activity_log").fetchone()[0]
        finally:
            con.close()
        if integrity != "ok":
            return False, f"副本 integrity={integrity}（非 ok）"
        return True, f"镜像恢复副本 integrity=ok，{rows} 行"
    except Exception as e:
        return False, f"恢复验证异常: {e}"
    finally:
        shutil.rmtree(tmp, ignore_errors=True)


def main() -> int:
    ap = argparse.ArgumentParser(description="事件库恢复副本验证（健壮性 L5）")
    ap.add_argument("--json", action="store_true")
    args = ap.parse_args()

    ok, summary = verify_restore()
    if args.json:
        print(json.dumps({"status": "PASS" if ok else "FAIL", "summary": summary},
                         ensure_ascii=False))
        return 0 if ok else 1
    print(f"{'✅' if ok else '❌'} 恢复演练: {summary}")
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
