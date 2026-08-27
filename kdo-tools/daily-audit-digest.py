#!/usr/bin/env python3
"""daily-audit-digest.py — 每日审计轮段①：四样原料抽数聚合（#507）。

每日一次聚合落一份 digest（零 LLM token，纯机械抽数）：
  ① 胶囊事件增量：activity_log.db 自上次 digest 以来新事件
  ② 各角色 daily-context：最新文件清单 + 差异栏摘要
  ③ friction-log：新增行（共享 + 各角色）
  ④ production-queue：状态变更（新立项/领单/提审/终审/退回）
  ⑤ 待你拍板（#556）：conveyor_probe 第八信号在列集合——每日在列直到拍板或撤销

落盘：D:\\KDO-memory\\L2-digest\\YYYY-MM-DD.md（D 盘与 L1 同区；**不落 60_feedback/diagnosis**——
避免被探针误扫成建议书）。状态：同目录 _state.json（增量游标，重跑幂等）。
调度：计划任务 kdo-daily-audit-digest 每日 06:00（老朱 08-24 拍板锚点，覆盖凌晨场）。
失败可见：异常 → stderr + 非零退出码（schtasks Last Result 可查），不静默。

用法：
  python kdo-tools/daily-audit-digest.py              # 常规跑（落 digest + 存游标）
  python kdo-tools/daily-audit-digest.py --dry-run    # 只打印不落盘不存游标（诊断零副作用纪律）
  python kdo-tools/daily-audit-digest.py --date 2026-08-25   # 指定 digest 日期（默认今天）
"""

import argparse
import json
import sqlite3
import sys
from datetime import datetime, timedelta, timezone
from pathlib import Path

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")

WIKI = Path(__file__).resolve().parent.parent
ACTIVITY_DB = Path.home() / ".kdo-memory" / "L1" / "activity_log.db"  # 主库（F-044 口径）
RETRO_ROOT = Path.home() / "Desktop" / "agent复盘"
SHARED_FRICTION = WIKI / ".agent" / "friction-log.md"
QUEUE_PATH = WIKI / "70_product" / "tasks" / "production-queue.md"
CONVEYOR_STATE = WIKI / ".kdo" / "conveyor_state.json"  # #556 ⑤栏：第八信号在列集合（只读消费）
OUT_DIR = Path("D:/KDO-memory/L2-digest")
STATE_FILE = OUT_DIR / "_state.json"

FRICTION_ROLES = ["ouyangfeng", "huangyaoshi", "wangyuyan", "laowantong",
                  "hongqigong", "duanwangye", "fengqingyang"]

sys.path.insert(0, str(WIKI / "90_control" / "scripts"))
from queue_gate import parse_queue  # noqa: E402  # 队列解析唯一真相源


def _load_state() -> dict:
    if STATE_FILE.exists():
        try:
            return json.loads(STATE_FILE.read_text(encoding="utf-8"))
        except Exception:
            pass
    return {}


def _save_state(state: dict) -> None:
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    STATE_FILE.write_text(json.dumps(state, ensure_ascii=False, indent=2), encoding="utf-8")


# ── ① 胶囊事件增量 ──

def _capsule_events(state: dict) -> tuple[list[str], str]:
    """自上次游标以来的新事件。首次跑取最近 24h。返回 (行清单, 新游标 ts)。"""
    if not ACTIVITY_DB.exists():
        return [f"⚠️ 主库不存在: {ACTIVITY_DB}"], state.get("last_event_ts", "")
    since = state.get("last_event_ts")
    if not since:
        since = (datetime.now(timezone.utc) - timedelta(hours=24)).isoformat()
    con = sqlite3.connect(str(ACTIVITY_DB))
    rows = con.execute(
        "SELECT ts, agent_id, event_type, payload_summary FROM activity_log "
        "WHERE ts > ? ORDER BY ts", (since,)).fetchall()
    max_ts = con.execute("SELECT MAX(ts) FROM activity_log").fetchone()[0] or since
    con.close()
    lines = [f"- `{ts[:19]}` **{agent}** {etype}｜{(summary or '')[:80]}"
             for ts, agent, etype, summary in rows]
    return lines, max_ts


# ── ② 各角色 daily-context 差异摘要 ──

def _extract_diff_section(text: str) -> str:
    """提取「## 差异栏」节（到下一个 ## 标题为止）。"""
    idx = text.find("## 差异栏")
    if idx == -1:
        return ""
    nxt = text.find("\n## ", idx + 1)
    sec = text[idx:nxt if nxt > 0 else len(text)]
    # 去掉标题行，压空行
    body = [ln for ln in sec.splitlines()[1:] if ln.strip()]
    return "\n".join(body[:20])  # 摘要截 20 行防 digest 膨胀


def _daily_contexts(state: dict) -> list[str]:
    """每角色最新 daily-context 文件；自上次以来有更新（新文件或内容变化）才展开差异栏。"""
    seen = state.get("daily_context", {})
    new_seen = dict(seen)
    lines = []
    if not RETRO_ROOT.exists():
        return [f"⚠️ 复盘根目录不存在: {RETRO_ROOT}"]
    for role_dir in sorted(RETRO_ROOT.iterdir()):
        dc = role_dir / "daily-context"
        if not dc.is_dir():
            continue
        files = sorted(dc.glob("*.md"))
        if not files:
            continue
        latest = files[-1]
        text = latest.read_text(encoding="utf-8", errors="replace")
        import hashlib
        sig = f"{latest.name}|{hashlib.sha256(text.encode('utf-8')).hexdigest()[:12]}"
        role = role_dir.name
        if seen.get(role) == sig:
            continue  # 无更新
        new_seen[role] = sig
        diff = _extract_diff_section(text)
        lines.append(f"### {role} · {latest.name}")
        lines.append(diff if diff else "（无差异栏节）")
        lines.append("")
    state["daily_context"] = new_seen
    return lines


# ── ③ friction-log 新增行 ──

def _friction_files() -> list[Path]:
    files = [SHARED_FRICTION] if SHARED_FRICTION.exists() else []
    for role in FRICTION_ROLES:
        fp = RETRO_ROOT / role / "friction-log.md"
        if fp.exists():
            files.append(fp)
    return files


def _friction_new(state: dict) -> list[str]:
    """各 friction 文件的新增行（按行 hash 去重，游标截尾防膨胀）。"""
    import hashlib
    seen = state.get("friction_seen", {})
    lines = []
    for fp in _friction_files():
        key = str(fp)
        known = set(seen.get(key, []))
        added = []
        try:
            for ln in fp.read_text(encoding="utf-8", errors="replace").splitlines():
                s = ln.strip()
                if not s or s.startswith("#"):
                    continue
                h = hashlib.sha256(s.encode("utf-8")).hexdigest()[:16]
                if h not in known:
                    known.add(h)
                    added.append(s)
        except OSError:
            continue
        seen[key] = sorted(known)[-500:]
        for s in added:
            lines.append(f"- [{fp.parent.name}] {s[:150]}")
    state["friction_seen"] = seen
    return lines


# ── ④ production-queue 状态变更 ──

def _queue_diff(state: dict) -> list[str]:
    """队列快照 diff：新立项 / 状态流转。首次跑只给计数摘要（防 99 行全量 dump）。"""
    rows = parse_queue(QUEUE_PATH)
    cur = {r["task_id"]: (r["status"], r["seq"]) for r in rows}
    prev = state.get("queue_snapshot")
    state["queue_snapshot"] = cur
    if prev is None:
        counts = {}
        for status, _ in cur.values():
            counts[status] = counts.get(status, 0) + 1
        summary = " / ".join(f"{k}={v}" for k, v in sorted(counts.items()))
        return [f"首次基线（后续跑只报变更）：总 {len(cur)} 任务｜{summary}"]
    lines = []
    for tid, (status, seq) in cur.items():
        old = prev.get(tid)
        if old is None:
            lines.append(f"- 🆕 #{seq} `{tid}` 新立项（{status}）")
        elif old[0] != status:
            lines.append(f"- 🔄 #{seq} `{tid}`：{old[0]} → {status}")
    for tid in prev:
        if tid not in cur:
            lines.append(f"- 🗑 `{tid}` 出队（归档/移除）")
    return lines


# ── ⑤ 待你拍板（#556）──

def _pending_decisions() -> list[str]:
    """读 conveyor_probe 第八信号在列集合（单扫描器纪律：digest 只消费不检出）。
    幂等：每日在列直到拍板或撤销（探针侧自动消项后本栏自然清空）。"""
    if not CONVEYOR_STATE.exists():
        return ["（conveyor state 不存在——探针未跑过？）"]
    try:
        items = json.loads(CONVEYOR_STATE.read_text(encoding="utf-8")).get("pending_decisions", {})
    except Exception:
        return ["⚠️ conveyor state 解析失败"]
    return [f"- #{c.get('seq', '?')} `{tid}`（首检出 {c.get('since', '?')}，命中：{c.get('source', '?')}）"
            for tid, c in sorted(items.items(), key=lambda kv: kv[1].get("since", ""))]


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--dry-run", action="store_true", help="只打印不落盘不存游标")
    ap.add_argument("--date", default=None, help="digest 日期 YYYY-MM-DD（默认今天）")
    args = ap.parse_args()

    date_str = args.date or datetime.now().strftime("%Y-%m-%d")
    state = _load_state()

    events, new_event_ts = _capsule_events(state)
    contexts = _daily_contexts(state)
    friction = _friction_new(state)
    queue_changes = _queue_diff(state)
    decisions = _pending_decisions()  # #556：⑤ 待你拍板（不耗游标，读探针在列集合）

    parts = [
        f"# 每日审计 digest · {date_str}",
        "",
        f"> 段①抽数原料（#507，零 LLM token）。生成：{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}。",
        "> 段②风清扬每日一审只读本文件（不翻全量）。",
        "",
        f"## ① 胶囊事件增量（{len(events)} 条）",
        "",
        *(events or ["（无增量）"]),
        "",
        f"## ② daily-context 更新（{sum(1 for l in contexts if l.startswith('### '))} 角色）",
        "",
        *(contexts or ["（无更新）"]),
        "",
        f"## ③ friction 新增（{len(friction)} 条）",
        "",
        *(friction or ["（无新增）"]),
        "",
        f"## ④ 队列变更（{len(queue_changes)} 条）",
        "",
        *(queue_changes or ["（无变更）"]),
        "",
        f"## ⑤ 待你拍板（{len(decisions)} 项——每日在列直到拍板或撤销，#556）",
        "",
        *(decisions or ["（无在列项）"]),
        "",
    ]
    digest = "\n".join(parts)

    if args.dry_run:
        print(digest)
        print("\n[dry-run] 未落盘未存游标")
        return 0

    state["last_event_ts"] = new_event_ts
    state["last_run"] = datetime.now().isoformat()
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    out = OUT_DIR / f"{date_str}.md"
    out.write_text(digest, encoding="utf-8")  # 同日重跑覆盖（幂等，不 append 重复）
    _save_state(state)
    print(f"✅ digest 落盘: {out}（事件 {len(events)} / 上下文 {len(contexts)} / friction {len(friction)} / 队列 {len(queue_changes)} / 待拍板 {len(decisions)}）")
    return 0


if __name__ == "__main__":
    sys.exit(main())
