#!/usr/bin/env python3
"""token_meter.py — 全厂 token 计量（#549）。

三引擎 usage 可得性（08-27 实测）：
- claude  ：~/.claude/projects/*/*.jsonl —— 每条 assistant 消息带 usage（input/output/cache_read/cache_creation）
- kimi    ：~/.kimi-code/sessions/*/agents/*/wire.jsonl —— usage{inputOther,output,inputCacheRead,inputCacheCreation}
- hermes  ：AppData/Local/hermes/profiles/*/state.db —— sessions 表会话级 token 累计+成本字段

口径：增量游标（字节偏移 / 会话累计差值），跑哪天记哪天。只计量不限制（#549 边界）。
产出：60_feedback/analytics/token-usage-YYYY-MM-DD.{json,md} + 事件层 token_usage 汇总事件。
预留 #514 接口：日 JSON 按 引擎×角色(归因) 分解 token，周聚合=日汇总求和 ÷ 同期完成单数。

用法：python kdo-tools/token_meter.py [--dry-run] [--date YYYY-MM-DD]
"""
import json
import sqlite3
import sys
from datetime import datetime
from pathlib import Path

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")

ROOT = Path(__file__).resolve().parent.parent
STATE_FILE = ROOT / ".kdo" / "token-meter-state.json"
OUT_DIR = ROOT / "60_feedback" / "analytics"

CLAUDE_GLOB = Path.home() / ".claude" / "projects"
KIMI_GLOB = Path.home() / ".kimi-code" / "sessions"
HERMES_PROFILES = Path.home() / "AppData" / "Local" / "hermes" / "profiles"

# jsonl usage 字段 → 归一（input/output/cache_read/cache_write）
CLAUDE_MAP = {"input_tokens": "input", "output_tokens": "output",
              "cache_read_input_tokens": "cache_read", "cache_creation_input_tokens": "cache_write"}
KIMI_MAP = {"inputOther": "input", "output": "output",
            "inputCacheRead": "cache_read", "inputCacheCreation": "cache_write"}


def _load_state() -> dict:
    try:
        return json.loads(STATE_FILE.read_text(encoding="utf-8"))
    except Exception:
        return {"files": {}, "hermes": {}}


def _save_state(state: dict) -> None:
    STATE_FILE.parent.mkdir(parents=True, exist_ok=True)
    tmp = STATE_FILE.with_suffix(".tmp")
    tmp.write_text(json.dumps(state, ensure_ascii=False, indent=2), encoding="utf-8")
    tmp.replace(STATE_FILE)


def _new_tokens(usage: dict, mapping: dict) -> dict:
    out = {"input": 0, "output": 0, "cache_read": 0, "cache_write": 0}
    for k, v in usage.items():
        if k in mapping and isinstance(v, (int, float)):
            out[mapping[k]] += int(v)
    return out


def _rec_ts(rec: dict) -> float | None:
    """记录时间戳（epoch 秒）。claude=ISO timestamp；kimi=毫秒 epoch time。无 → None。"""
    t = rec.get("timestamp")
    if isinstance(t, str):
        try:
            return datetime.fromisoformat(t.replace("Z", "+00:00")).timestamp()
        except ValueError:
            return None
    t = rec.get("time") or rec.get("created_at")
    if isinstance(t, (int, float)):
        return t / 1000 if t > 1e12 else float(t)
    return None


def _scan_jsonl(files, state_files: dict, mapping: dict, engine: str,
                mtime_floor: float, acc: dict, bootstrap_since: float | None = None) -> None:
    """按字节偏移增量扫 jsonl，usage 增量累进 acc[engine][session]。
    bootstrap_since：首见文件不全量放行——只计该时刻之后的记录（首日取今日 00:00，
    满足「不回溯历史」又给首日真实读数）。"""
    for fp in files:
        try:
            if fp.stat().st_mtime < mtime_floor:
                continue  # 上次运行后没动过的文件跳过（性能）
            key = str(fp)
            size = fp.stat().st_size
            if key not in state_files:
                if bootstrap_since is None:
                    state_files[key] = size  # #549 边界：不回溯历史——首见文件从当前大小起计
                    continue
                offset = 0  # 首日引导：全扫但只计今日记录
            else:
                offset = state_files.get(key, 0)
                if size < offset:
                    offset = 0  # 文件被截断重建（罕见）→ 从头读
                if size == offset:
                    continue
            sess = fp.stem
            if sess == "wire":  # kimi wire.jsonl 全会话同名——用 <session_id>/<agent> 区分
                sess = f"{fp.parents[2].name}/{fp.parent.name}"
            with open(fp, "r", encoding="utf-8", errors="replace") as f:
                f.seek(offset)
                for line in f:
                    if '"usage"' not in line:
                        continue
                    try:
                        rec = json.loads(line)
                    except json.JSONDecodeError:
                        continue
                    if bootstrap_since is not None:
                        rts = _rec_ts(rec)
                        if rts is None or rts < bootstrap_since:
                            continue
                    usage = (rec.get("message") or {}).get("usage") or rec.get("usage") or {}
                    delta = _new_tokens(usage, mapping)
                    if any(delta.values()):
                        slot = acc.setdefault(engine, {}).setdefault(
                            sess, {"input": 0, "output": 0, "cache_read": 0, "cache_write": 0})
                        for k, v in delta.items():
                            slot[k] += v
                state_files[key] = f.tell()
        except OSError:
            continue


def _scan_hermes(state_hermes: dict, acc: dict, bootstrap_since: float | None = None) -> None:
    """hermes state.db 会话级累计 → 差值即增量。profile=角色归因。
    bootstrap：首见会话不计存量；但 started_at 在今日 bootstrap 窗口内的会话按全量计（首日读数）。"""
    if not HERMES_PROFILES.exists():
        return
    for db in HERMES_PROFILES.glob("*/state.db"):
        profile = db.parent.name
        try:
            conn = sqlite3.connect(f"file:{db}?mode=ro", uri=True)
            rows = conn.execute(
                "SELECT id, model, input_tokens, output_tokens, cache_read_tokens, "
                "cache_write_tokens, reasoning_tokens, estimated_cost_usd, started_at FROM sessions"
            ).fetchall()
            conn.close()
        except Exception:
            continue
        for sid, model, it, ot, cr, cw, rt, cost, started in rows:
            key = f"{profile}|{sid}"
            cur = {"input": it or 0, "output": ot or 0, "cache_read": cr or 0,
                   "cache_write": cw or 0, "reasoning": rt or 0, "cost_usd": cost or 0.0}
            old = state_hermes.get(key)
            if old:
                delta = {k: max(0, cur.get(k, 0) - old.get(k, 0)) for k in
                         ("input", "output", "cache_read", "cache_write")}
            elif bootstrap_since is not None and _hermes_started_after(started, bootstrap_since):
                delta = {k: cur[k] for k in ("input", "output", "cache_read", "cache_write")}
            else:
                delta = {k: 0 for k in ("input", "output", "cache_read", "cache_write")}  # 首见不计存量
            if any(delta.values()):
                slot = acc.setdefault("hermes", {}).setdefault(
                    profile, {"input": 0, "output": 0, "cache_read": 0, "cache_write": 0})
                for k, v in delta.items():
                    slot[k] += v
            state_hermes[key] = cur


def _hermes_started_after(started, since_ts: float) -> bool:
    """hermes started_at 兼容 ISO 字符串/epoch 秒/毫秒。"""
    if started is None:
        return False
    if isinstance(started, (int, float)):
        ts = started / 1000 if started > 1e12 else float(started)
        return ts >= since_ts
    try:
        return datetime.fromisoformat(str(started).replace("Z", "+00:00")).timestamp() >= since_ts
    except ValueError:
        return False


def collect(last_run_ts: float = 0.0, save: bool = True, bootstrap_since: float | None = None) -> dict:
    """采集三引擎增量。返回 {engine: {session_or_profile: {input/output/cache_read/cache_write}}}
    save=False（dry-run）→ 不存游标（dry-run 零副作用纪律：不消费真实游标，F-036 教训）。
    bootstrap_since：首日引导（首次运行）——首见文件/会话只计该时刻后的记录。"""
    state = _load_state()
    acc: dict = {}
    if CLAUDE_GLOB.exists():
        _scan_jsonl(CLAUDE_GLOB.glob("*/*.jsonl"), state["files"], CLAUDE_MAP,
                    "claude", last_run_ts, acc, bootstrap_since)
    if KIMI_GLOB.exists():
        _scan_jsonl(KIMI_GLOB.glob("*/*/agents/*/wire.jsonl"), state["files"], KIMI_MAP,
                    "kimi", last_run_ts, acc, bootstrap_since)
    _scan_hermes(state["hermes"], acc, bootstrap_since)
    state["last_run"] = datetime.now().isoformat(timespec="seconds")
    if save:
        _save_state(state)  # 采完即存游标——崩在 collect 与落盘之间也不丢偏移（丢了=下次重复计）
    return acc, state


def render_markdown(day: str, acc: dict) -> str:
    lines = [f"# 全厂 token 日计量 {day}（#549）", "",
             "| 引擎 | 会话/角色 | input | output | cache_read | cache_write | 计", "|---|---|---|---|---|---|---|"]
    totals = {"input": 0, "output": 0, "cache_read": 0, "cache_write": 0}
    for engine, sessions in sorted(acc.items()):
        for sess, t in sorted(sessions.items()):
            total = sum(t.values())
            lines.append(f"| {engine} | {sess} | {t['input']} | {t['output']} | {t['cache_read']} | {t['cache_write']} | {total} |")
            for k in totals:
                totals[k] += t[k]
    grand = sum(totals.values())
    lines.append(f"| **合计** | — | {totals['input']} | {totals['output']} | {totals['cache_read']} | {totals['cache_write']} | {grand} |")
    lines += ["", "> hermes 行=角色（profile 名）；claude/kimi 行=会话文件（角色归因=cwd 粒度，混合角色会话为估算口径）。",
              "> #514 接口：周聚合 = 本周日 JSON 合计 ÷ 同期 reviewed 单数（质量基线周报同源）。"]
    return "\n".join(lines)


def main() -> int:
    import argparse
    p = argparse.ArgumentParser(description="全厂 token 计量（#549）")
    p.add_argument("--dry-run", action="store_true", help="只打印不落盘不写事件")
    p.add_argument("--date", default=None, help="汇总日期（默认今天）")
    args = p.parse_args()

    day = args.date or datetime.now().strftime("%Y-%m-%d")
    state0 = _load_state()
    last_run_ts = 0.0
    bootstrap_since = None
    if state0.get("last_run"):
        try:
            last_run_ts = datetime.fromisoformat(state0["last_run"]).timestamp()
        except ValueError:
            pass
    else:
        # 首次运行=首日引导：首见文件/会话只计今日 00:00 后的记录（不回溯历史但有首日读数）
        bootstrap_since = datetime.now().replace(hour=0, minute=0, second=0, microsecond=0).timestamp()

    acc, state = collect(last_run_ts, save=not args.dry_run, bootstrap_since=bootstrap_since)
    md = render_markdown(day, acc)

    if args.dry_run:
        print(md)
        return 0

    OUT_DIR.mkdir(parents=True, exist_ok=True)
    (OUT_DIR / f"token-usage-{day}.json").write_text(
        json.dumps({"date": day, "collected_at": datetime.now().isoformat(timespec="seconds"),
                    "usage": acc}, ensure_ascii=False, indent=2), encoding="utf-8")
    (OUT_DIR / f"token-usage-{day}.md").write_text(md, encoding="utf-8")

    # 事件层：日汇总事件（单写入面 memory_capsule；失败可见不阻断）
    try:
        sys.path.insert(0, str(ROOT / "kdo-tools"))
        import memory_capsule as mc
        grand = sum(sum(t.values()) for eng in acc.values() for t in eng.values())
        mc.log_event_safe("token_meter", "token_usage",
                          f"date={day};engines={len(acc)};total_delta_tokens={grand}")
    except Exception as e:
        print(f"⚠️ 事件层写入失败（不阻断）: {e}", file=sys.stderr)

    print(f"✅ token 日汇总已落盘: {OUT_DIR / f'token-usage-{day}.md'}（引擎 {len(acc)} 个）")
    return 0


if __name__ == "__main__":
    sys.exit(main())
