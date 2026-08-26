"""on_duty.py — 在岗判定共享模块（#550：时段静默 → 在岗判定，老朱直令）。

口径（任务书 §2，满足其一即在岗，窗口 30 分钟对齐 L1 节拍）：
- 事件库（memory_capsule L1 activity_log.db）近 30 分钟有新事件
  ——排除机器自写事件类型（friction=探针镜像写入、token_usage=计量每日自写），
    否则探针每 10 分钟自证在岗=判定失效（循环依赖）
- L1 采集层（D:/KDO-memory/L1-full/<当日>/）近 30 分钟有新会话原文文件

不对称偏误拦方向：宁可误激活（多发通知）不可误静默（协作断连）。
两路信号都读不到 → 默认在岗（静默是例外不是默认）。

conveyor_probe.py 与 watch_inbox.py 同口径共用本模块（单一判定源，禁双份实现）。
"""
import os
import sqlite3
import time
from datetime import datetime, timedelta
from pathlib import Path

EVENT_DB = Path.home() / ".kdo-memory" / "L1" / "activity_log.db"
L1_ROOT = Path("D:/KDO-memory/L1-full")
WINDOW_MIN = 30
# 机器自写事件类型（不计入在岗证据）：friction=conveyor_probe 镜像写入；
# token_usage=token_meter 每日 02:07 自写（否则每天凌晨自欺在岗 30 分钟）
MACHINE_EVENT_TYPES = ("friction", "token_usage")


def _recent_event(event_db: Path, cutoff_iso: str) -> bool | None:
    """事件库近窗口有非机器事件 → True；无 → False；读不到 → None。"""
    if not event_db.exists():
        return None
    try:
        conn = sqlite3.connect(f"file:{event_db}?mode=ro", uri=True)
        placeholders = ",".join("?" * len(MACHINE_EVENT_TYPES))
        n = conn.execute(
            f"SELECT COUNT(*) FROM activity_log WHERE ts >= ? AND event_type NOT IN ({placeholders})",
            (cutoff_iso, *MACHINE_EVENT_TYPES),
        ).fetchone()[0]
        conn.close()
        return n > 0
    except Exception:
        return None


def _recent_l1_file(l1_root: Path, cutoff_ts: float) -> bool | None:
    """L1 当日目录近窗口有新文件 → True（首个新文件即短路返回，不扫全量）。"""
    today_dir = l1_root / datetime.now().strftime("%Y-%m-%d")
    if not today_dir.exists():
        return None
    try:
        for dirpath, _dirnames, filenames in os.walk(today_dir):
            for name in filenames:
                try:
                    if os.path.getmtime(os.path.join(dirpath, name)) >= cutoff_ts:
                        return True
                except OSError:
                    continue
        return False
    except OSError:
        return None


def any_agent_on_duty(event_db: Path | None = None, l1_root: Path | None = None,
                      window_min: int = WINDOW_MIN, now: datetime | None = None) -> tuple[bool, str]:
    """返回 (在岗?, 判定依据)。两路都不可得 → 默认在岗（True, "信号不可得默认激活"）。"""
    now = now or datetime.now()
    event_db = event_db or EVENT_DB
    l1_root = l1_root or L1_ROOT
    # 事件库 ts 是 UTC ISO 8601——cutoff 转 UTC ISO 对齐
    import datetime as _dt
    cutoff_utc = (now.astimezone(_dt.timezone.utc) - _dt.timedelta(minutes=window_min)).isoformat()

    ev = _recent_event(event_db, cutoff_utc)
    if ev is True:
        return True, f"事件库近 {window_min} 分钟有新事件"
    l1 = _recent_l1_file(l1_root, time.time() - window_min * 60)
    if l1 is True:
        return True, f"L1 采集层近 {window_min} 分钟有新会话文件"
    if ev is None and l1 is None:
        return True, "事件库与 L1 均读不到 → 默认激活（静默是例外）"
    return False, f"事件库近 {window_min} 分钟无新事件且 L1 无新文件"
