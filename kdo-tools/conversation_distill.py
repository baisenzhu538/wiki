#!/usr/bin/env python3
"""#645 对话蒸馏管线：会话上下文 → 三层分流（外部知识 / 对老朱洞察 / 对他人洞察）。

老朱 09-05 长期机制。读会话记录（kimi sessions wire + headless logs + hermes sessions），
按三层提示词蒸馏，写死分流规则，增量游标，原文锚红线。

数据源：
  1. kimi wire   ~/.kimi-code/sessions/*/session_*/agents/*/wire.jsonl（事件流：append_message=user，content.part text=assistant）
  2. headless    logs/headless-*.log（纯文本转录，日期取自文件名）
  3. hermes      ~/.hermes/state.db（sessions 表；空库/无表则优雅跳过并记日志）

分流（写死）：
  external → 00_inbox/pending-cards/distill-ext-*.md（候选卡，过王语嫣门禁）
  zhu      → 30_wiki/personal-os/zhu-conversation-insights.md 追加（隐私面：只进 personal-os 不外流）
  human    → 00_inbox/pending-cards/distill-human-*.md（人域 human-insights 候选，过门禁）

红线：蒸馏≠编造——每条产出必须带原文锚（anchor_quote 逐字摘自源文本），
脚本强制校验 quote 是 chunk 原文的子串（空白归一化后），校验不过的条目丢弃并计数。

节奏：每日 23:50 计划任务 kdo-conversation-distill（独立批次，与 daily-review 23:37 错开）。
增量：.kdo/conversation_distill_state.json 记录 per-file 字节游标 + 全局水位 ts。

用法：
  python kdo-tools/conversation_distill.py                      # 日常增量（走游标）
  python kdo-tools/conversation_distill.py --since 2026-09-02 --until 2026-09-05 --no-save   # 试跑
  python kdo-tools/conversation_distill.py --dry-run            # 只抽取+分块，不调 LLM
"""
import argparse
import datetime
import json
import os
import re
import sqlite3
import sys
import urllib.request
from pathlib import Path

try:
    import yaml
except ImportError:  # 极简兜底：只解析我们需要的 llm 节
    yaml = None

WIKI = Path(__file__).resolve().parents[1]
STATE_PATH = WIKI / ".kdo" / "conversation_distill_state.json"
PENDING_DIR = WIKI / "00_inbox" / "pending-cards"
ZHU_FILE = WIKI / "30_wiki" / "personal-os" / "zhu-conversation-insights.md"
LOG_DIR = WIKI / "logs"
CHUNK_CHARS = 7000
MAX_QUOTE = 120

PROMPT = """你是 KDO 对话蒸馏器。下面是一段真实会话记录（用户=老朱，assistant=各 agent）。
按三层分流提取有价值条目，只输出 JSON：

{"items":[{"layer":"external|zhu|human","title":"≤20字标题","insight":"蒸馏出的知识/洞察，≤100字","anchor_quote":"原文逐字引用（≤120字，必须是会话原文里连续出现的句子，不得改写）"}]}

三层口径：
- external：外部知识（客观世界的知识：方法论、行业事实、工具用法、技术方案）
- zhu：对老朱的洞察（他的思维模型、优缺点、决策模式、偏好、反馈习惯）
- human：对他人（对话中出现的第三方人物，如案主、合作者）的洞察

纪律：
- 蒸馏≠编造：anchor_quote 必须逐字摘自原文，宁可少提取不可编。
- 纯流程噪音（状态流转、时钟叫醒、报错堆栈）不提取。
- 没有值得提取的就返回 {"items":[]}。
- 只输出 JSON，不要任何其他文字。"""


def log(msg, fh=None):
    line = f"[{datetime.datetime.now().strftime('%H:%M:%S')}] {msg}"
    print(line)
    if fh:
        fh.write(line + "\n")


def load_llm_cfg():
    cfg_path = Path.home() / ".kdo" / "config.yaml"
    if yaml:
        return yaml.safe_load(cfg_path.read_text(encoding="utf-8"))["llm"]
    text = cfg_path.read_text(encoding="utf-8")
    sec = text.split("llm:", 1)[1]
    def grab(k):
        m = re.search(rf'{k}:\s*"([^"]+)"', sec)
        return m.group(1) if m else None
    return {"endpoint": grab("endpoint"), "model": grab("model"),
            "api_key": grab("api_key"), "max_tokens": 4096}


def llm_call(cfg, chunk_text):
    body = json.dumps({
        "model": cfg["model"],
        "max_tokens": 4096,
        "messages": [{"role": "user", "content": PROMPT + "\n\n===会话记录===\n" + chunk_text}],
    }).encode("utf-8")
    req = urllib.request.Request(
        cfg["endpoint"], data=body,
        headers={"Content-Type": "application/json",
                 "x-api-key": cfg["api_key"],
                 "anthropic-version": "2023-06-01"})
    with urllib.request.urlopen(req, timeout=300) as r:
        resp = json.load(r)
    return "".join(p.get("text", "") for p in resp.get("content", []) if p.get("type") == "text")


def parse_items(raw):
    raw = raw.strip()
    m = re.search(r"\{.*\}", raw, re.S)
    if not m:
        return []
    try:
        data = json.loads(m.group(0))
    except json.JSONDecodeError:
        return []
    items = data.get("items", [])
    return [it for it in items if isinstance(it, dict) and it.get("layer") in ("external", "zhu", "human")]


def norm(s):
    return re.sub(r"\s+", "", s or "")


def anchor_ok(quote, chunk_text):
    q = norm(quote)
    return bool(q) and len(q) <= MAX_QUOTE * 2 and q in norm(chunk_text)


# ---------- 抽取 ----------

def iter_kimi_wire(since_ms, until_ms, offsets, use_cursor):
    """产出 (source_key, ts_ms, role, text)。"""
    root = Path.home() / ".kimi-code" / "sessions"
    if not root.exists():
        return
    for wire in root.glob("*/session_*/agents/*/wire.jsonl"):
        key = str(wire)
        start = offsets.get(key, 0) if use_cursor else 0
        try:
            size = wire.stat().st_size
            if start >= size:
                continue
            with wire.open("r", encoding="utf-8", errors="replace") as f:
                f.seek(start)
                for line in f:
                    try:
                        d = json.loads(line)
                    except json.JSONDecodeError:
                        continue
                    t = d.get("type")
                    ts = d.get("time") or int(wire.stat().st_mtime * 1000)
                    if not (since_ms <= ts < until_ms):
                        continue
                    if t == "context.append_message":
                        msg = d.get("message", {})
                        if msg.get("role") != "user":
                            continue
                        origin = msg.get("origin") or {}
                        if origin.get("kind") in ("injection", "cron"):
                            continue
                        for part in msg.get("content", []):
                            txt = part.get("text", "") if isinstance(part, dict) else ""
                            if txt and not txt.startswith(("<system-reminder", "<cron-fire")):
                                yield key, ts, "user", txt
                    elif t == "context.append_loop_event":
                        ev = d.get("event", {})
                        if ev.get("type") == "content.part" and ev.get("part", {}).get("type") == "text":
                            txt = ev["part"].get("text", "")
                            if txt:
                                yield key, ev.get("time") or ts, "assistant", txt
            offsets[key] = size
        except OSError:
            continue


def iter_headless(since_ms, until_ms, offsets, use_cursor):
    for fp in sorted(LOG_DIR.glob("headless-*.log")):
        m = re.search(r"headless-[a-z]+-(\d{8})-", fp.name)
        if not m:
            continue
        day = datetime.datetime.strptime(m.group(1), "%Y%m%d")
        day_ms = int(day.timestamp() * 1000)
        if not (since_ms <= day_ms < until_ms):
            continue
        key = str(fp)
        start = offsets.get(key, 0) if use_cursor else 0
        try:
            size = fp.stat().st_size
            if start >= size:
                continue
            text = fp.read_text(encoding="utf-8", errors="replace")[start:]
            offsets[key] = size
            if text.strip():
                yield key, day_ms, "transcript", text
        except OSError:
            continue


def iter_hermes(since_ms, until_ms):
    """hermes state.db 在 Windows 侧为空镜像（gateway 跑在 WSL）；有表则读，无则跳过。"""
    db_path = Path.home() / ".hermes" / "state.db"
    if not db_path.exists() or db_path.stat().st_size == 0:
        return
    try:
        db = sqlite3.connect(f"file:{db_path}?mode=ro", uri=True)
        tables = {r[0] for r in db.execute("SELECT name FROM sqlite_master WHERE type='table'")}
        if "messages" not in tables:
            db.close()
            return
        cols = {c[1] for c in db.execute("PRAGMA table_info(messages)")}
        role_c = "role" if "role" in cols else None
        text_c = next((c for c in ("content", "text", "body") if c in cols), None)
        ts_c = next((c for c in ("created_at", "timestamp", "time") if c in cols), None)
        if not (role_c and text_c):
            db.close()
            return
        for row in db.execute(f"SELECT {role_c}, {text_c}, {ts_c or 'NULL'} FROM messages"):
            role, text, ts = row
            if isinstance(ts, str):
                try:
                    ts = int(datetime.datetime.fromisoformat(ts).timestamp() * 1000)
                except ValueError:
                    ts = 0
            ts = ts or 0
            if text and role in ("user", "assistant") and since_ms <= ts < until_ms:
                yield str(db_path), ts, role, str(text)
        db.close()
    except sqlite3.Error:
        return


# ---------- 分块 ----------

def chunk_events(events):
    """产出 (first_src, text, segments)。

    segments = [(src, line_text), ...]——逐行携带真实源文件，
    禁止用 chunk 首事件 src 覆盖整块（#645 终审 P1）。
    """
    chunks, cur, cur_len, cur_src = [], [], 0, None
    cur_segs = []
    for src, ts, role, text in events:
        if cur_src is None:
            cur_src = src
        line = f"[{role}] {text.strip()}\n"
        if cur_len + len(line) > CHUNK_CHARS and cur:
            chunks.append((cur_src, "".join(cur), cur_segs))
            cur, cur_len, cur_src, cur_segs = [], 0, src, []
        # 单条超块（headless 整段日志）→ 硬切（单源，segments 只记一条）
        while len(line) > CHUNK_CHARS:
            piece = line[:CHUNK_CHARS]
            chunks.append((src, piece, [(src, piece)]))
            line = line[CHUNK_CHARS:]
        cur.append(line)
        cur_segs.append((src, line))
        cur_len += len(line)
    if cur:
        chunks.append((cur_src or "unknown", "".join(cur), cur_segs))
    return chunks


def resolve_src(quote, segments, fallback):
    """锚文命中后回查真实源文件：norm 子串落在哪一行，src 就是哪一行的。"""
    q = norm(quote)
    if q:
        for src, line in segments:
            if q in norm(line):
                return src
    return fallback


# ---------- 落盘 ----------

def write_candidate(layer, item, src, run_tag, seq):
    PENDING_DIR.mkdir(parents=True, exist_ok=True)
    fp = PENDING_DIR / f"distill-{layer}-{run_tag}-{seq:02d}.md"
    body = f"""---
id: distill-{layer}-{run_tag}-{seq:02d}
title: "[蒸馏候选] {item.get('title', '未命名')}"
type: distill-candidate
layer: {layer}
status: pending-triage
created_by: conversation_distill (#645)
created_at: {datetime.datetime.now().isoformat(timespec='seconds')}
gate: 王语嫣门禁（pending-cards 候选，未过门禁不入 30_wiki）
source_refs:
- "{src}"
---

# {item.get('title', '未命名')}

**层**：{layer}（{'外部知识→知识域候选' if layer == 'external' else '对他人洞察→人域 human-insights 候选'}）

**蒸馏内容**：{item.get('insight', '')}

**原文锚**（红线：逐字摘自源会话）：
> {item.get('anchor_quote', '')}

**来源**：`{src}`
"""
    fp.write_text(body, encoding="utf-8")
    return fp


def append_zhu(pairs, run_tag):
    """pairs = [(item, src), ...]——每条洞察携带自己的真实源（#645 终审 P2：来源列存完整 session 路径）。"""
    if not pairs:
        return None
    ZHU_FILE.parent.mkdir(parents=True, exist_ok=True)
    if not ZHU_FILE.exists():
        ZHU_FILE.write_text(f"""---
id: zhu-conversation-insights
title: 老朱对话洞察（蒸馏管线沉淀）
type: system
status: active
domain:
- personal-os
created_at: {datetime.date.today().isoformat()}
related:
- '[[zhu-feedback-patterns]]'
---

# 老朱对话洞察（#645 对话蒸馏管线沉淀）

> 隐私红线：本文件只在 personal-os，内容不外流。与 zhu-feedback-patterns 同族（该文件由王语嫣维护，本文件由蒸馏管线每日追加）。每条带原文锚，蒸馏≠编造。

""", encoding="utf-8")
    now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M")
    lines = [f"\n## {now} 蒸馏（run {run_tag}）\n",
             "| # | 洞察 | 原文锚 | 来源 |", "|:---|:---|:---|:---|"]
    for i, (it, src) in enumerate(pairs, 1):
        anchor = (it.get("anchor_quote", "") or "").replace("|", "\\|").replace("\n", " ")
        insight = (it.get("insight", "") or "").replace("|", "\\|").replace("\n", " ")
        lines.append(f"| {i} | **{it.get('title', '')}**：{insight} | {anchor} | `{src}` |")
    with ZHU_FILE.open("a", encoding="utf-8") as f:
        f.write("\n".join(lines) + "\n")
    return ZHU_FILE


# ---------- 主流程 ----------

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--since", help="YYYY-MM-DD（试跑用；默认走增量水位）")
    ap.add_argument("--until", help="YYYY-MM-DD（含当日，闭区间）")
    ap.add_argument("--max-chunks", type=int, default=8, help="LLM 成本控制（F-062）")
    ap.add_argument("--dry-run", action="store_true", help="只抽取+分块，不调 LLM")
    ap.add_argument("--no-save", action="store_true", help="不写游标（试跑用）")
    args = ap.parse_args()

    state = {"watermark_ts": 0, "files": {}}
    if STATE_PATH.exists():
        try:
            state = json.loads(STATE_PATH.read_text(encoding="utf-8"))
        except json.JSONDecodeError:
            pass

    if args.since:
        since_ms = int(datetime.datetime.fromisoformat(args.since).timestamp() * 1000)
        until_d = datetime.date.fromisoformat(args.until or args.since) + datetime.timedelta(days=1)
        until_ms = int(datetime.datetime.combine(until_d, datetime.time()).timestamp() * 1000)
        use_cursor = False
    else:
        since_ms = state.get("watermark_ts", 0) or int(
            (datetime.datetime.now() - datetime.timedelta(days=1)).timestamp() * 1000)
        until_ms = int(datetime.datetime.now().timestamp() * 1000)
        use_cursor = True

    run_tag = datetime.datetime.now().strftime("%Y%m%d")
    LOG_DIR.mkdir(exist_ok=True)
    log_fp = LOG_DIR / f"conversation-distill-{datetime.datetime.now().strftime('%Y%m%d-%H%M%S')}.log"
    offsets = dict(state.get("files", {}))

    with log_fp.open("w", encoding="utf-8") as fh:
        log(f"#645 conversation_distill 启动 since={since_ms} until={until_ms} cursor={use_cursor}", fh)
        events = []
        n_kimi = 0
        for ev in iter_kimi_wire(since_ms, until_ms, offsets, use_cursor):
            events.append(ev); n_kimi += 1
        n_head = 0
        for ev in iter_headless(since_ms, until_ms, offsets, use_cursor):
            events.append(ev); n_head += 1
        n_hermes = 0
        for ev in iter_hermes(since_ms, until_ms):
            events.append(ev); n_hermes += 1
        events.sort(key=lambda e: e[1])
        log(f"抽取：kimi {n_kimi} 条 / headless {n_head} 段 / hermes {n_hermes} 条", fh)

        chunks = chunk_events(events)
        # kimi wire（真实对话）优先，headless 日志（stdout 噪音多）靠后
        chunks.sort(key=lambda c: 0 if "wire.jsonl" in c[0] else (2 if "headless" in c[0] else 1))
        log(f"分块 {len(chunks)} 个（上限 {args.max_chunks}）", fh)
        if args.dry_run:
            for i, (src, text, _segs) in enumerate(chunks[:args.max_chunks]):
                log(f"  chunk{i}: {len(text)} chars src={Path(src).name}", fh)
            log("dry-run 结束（未调 LLM）", fh)
            return 0

        cfg = load_llm_cfg()
        stats = {"external": 0, "zhu": 0, "human": 0, "dropped_anchor": 0, "calls": 0, "failed_calls": 0}
        zhu_buf = []
        seq = {"external": 0, "human": 0}
        for src, text, segs in chunks[:args.max_chunks]:
            stats["calls"] += 1
            try:
                raw = llm_call(cfg, text)
            except Exception as e:
                stats["failed_calls"] += 1
                log(f"LLM 调用失败（{Path(src).name}）：{e}", fh)
                continue
            items = parse_items(raw)
            kept = 0
            for it in items:
                if not anchor_ok(it.get("anchor_quote"), text):
                    stats["dropped_anchor"] += 1
                    continue
                kept += 1
                stats[it["layer"]] += 1
                # 溯源回查：锚文实际出自 chunk 内哪条事件的源文件（不用首事件 src 覆盖）
                real_src = resolve_src(it.get("anchor_quote"), segs, src)
                if it["layer"] == "zhu":
                    zhu_buf.append((it, real_src))
                else:
                    seq[it["layer"]] += 1
                    fp = write_candidate(it["layer"], it, real_src, run_tag, seq[it["layer"]])
                    log(f"  落候选卡 {fp.name}", fh)
            log(f"chunk {Path(src).name}: 提取 {len(items)} 条，过锚校验 {kept} 条", fh)

        if zhu_buf:
            fp = append_zhu(zhu_buf, run_tag)
            log(f"zhu 洞察 {len(zhu_buf)} 条追加 → {fp}", fh)

        log(f"完成：{stats}", fh)
        print("SUMMARY " + json.dumps(stats, ensure_ascii=False))

    if not args.no_save and not args.dry_run:
        state["watermark_ts"] = until_ms
        state["files"] = offsets
        STATE_PATH.write_text(json.dumps(state, ensure_ascii=False, indent=2), encoding="utf-8")
    return 0


if __name__ == "__main__":
    sys.exit(main())
