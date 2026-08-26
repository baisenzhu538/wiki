"""#549 回归：token_meter 三引擎增量采集 + 不回溯历史 + 日汇总渲染。

运行：python -m pytest kdo-tools/tests/test_token_meter.py -q
"""
import importlib.util
import json
import sqlite3
from pathlib import Path

_SPEC = importlib.util.spec_from_file_location(
    "token_meter", Path(__file__).resolve().parent.parent / "token_meter.py"
)
tm = importlib.util.module_from_spec(_SPEC)
_SPEC.loader.exec_module(tm)


def _wire(tmp_path, monkeypatch):
    monkeypatch.setattr(tm, "STATE_FILE", tmp_path / ".kdo" / "state.json")
    monkeypatch.setattr(tm, "OUT_DIR", tmp_path / "analytics")
    claude = tmp_path / "claude" / "projects" / "proj"
    kimi = tmp_path / "kimi" / "sessions" / "wd_test" / "s1" / "agents" / "main"  # 真实结构两层：sessions/<wd>/<session>/agents/<agent>/
    hermes = tmp_path / "hermes" / "profiles"
    for d in (claude, kimi, hermes):
        d.mkdir(parents=True)
    monkeypatch.setattr(tm, "CLAUDE_GLOB", claude.parent)
    monkeypatch.setattr(tm, "KIMI_GLOB", kimi.parent.parent.parent.parent)  # → sessions/
    monkeypatch.setattr(tm, "HERMES_PROFILES", hermes)
    return claude, kimi, hermes


def _mk_hermes_db(hermes_root: Path, profile: str, tokens: dict):
    pdb = hermes_root / profile
    pdb.mkdir(parents=True, exist_ok=True)
    conn = sqlite3.connect(str(pdb / "state.db"))
    conn.execute("CREATE TABLE sessions (id TEXT, model TEXT, input_tokens INT, output_tokens INT,"
                 " cache_read_tokens INT, cache_write_tokens INT, reasoning_tokens INT, estimated_cost_usd REAL,"
                 " started_at TEXT)")
    conn.execute("INSERT INTO sessions VALUES ('sess1','deepseek',?,?,?,?,?,?,?)",
                 (tokens.get("input", 0), tokens.get("output", 0), tokens.get("cache_read", 0),
                  tokens.get("cache_write", 0), 0, 0.0, tokens.get("started_at", "2026-08-20T00:00:00")))
    conn.commit()
    conn.close()


def test_no_history_backfill_on_first_run(tmp_path, monkeypatch):
    """不回溯历史：首见文件/会话只建游标，增量=0。"""
    claude, kimi, hermes = _wire(tmp_path, monkeypatch)
    (claude / "old.jsonl").write_text(
        json.dumps({"message": {"usage": {"input_tokens": 9999, "output_tokens": 888}}}) + "\n",
        encoding="utf-8")
    _mk_hermes_db(hermes, "laowantong", {"input": 5000, "output": 500})
    acc, state = tm.collect()
    assert acc == {} or all(not s for s in acc.values()) or \
        all(sum(t.values()) == 0 for eng in acc.values() for t in eng.values())


def test_claude_incremental_delta(tmp_path, monkeypatch):
    """claude jsonl 追加 usage 行 → 第二次采集只计增量。"""
    claude, _, _ = _wire(tmp_path, monkeypatch)
    f = claude / "s.jsonl"
    f.write_text(json.dumps({"message": {"usage": {"input_tokens": 1, "output_tokens": 1}}}) + "\n",
                 encoding="utf-8")
    tm.collect()  # 建游标
    with open(f, "a", encoding="utf-8") as fh:
        fh.write(json.dumps({"message": {"usage": {
            "input_tokens": 100, "output_tokens": 20,
            "cache_read_input_tokens": 500, "cache_creation_input_tokens": 5}}}) + "\n")
    acc, _ = tm.collect()
    t = acc["claude"]["s"]
    assert t == {"input": 100, "output": 20, "cache_read": 500, "cache_write": 5}


def test_kimi_wire_format(tmp_path, monkeypatch):
    """kimi wire.jsonl 字段映射（inputOther/output/inputCacheRead/inputCacheCreation）。"""
    _, kimi, _ = _wire(tmp_path, monkeypatch)
    f = kimi / "wire.jsonl"
    f.write_text("{}\n", encoding="utf-8")
    tm.collect()
    with open(f, "a", encoding="utf-8") as fh:
        fh.write(json.dumps({"usage": {"inputOther": 10, "output": 3,
                                       "inputCacheRead": 700, "inputCacheCreation": 0}}) + "\n")
    acc, _ = tm.collect()
    t = acc["kimi"]["s1/main"]  # wire.jsonl 同名防撞：key=<session>/<agent>
    assert t == {"input": 10, "output": 3, "cache_read": 700, "cache_write": 0}


def test_hermes_session_delta(tmp_path, monkeypatch):
    """hermes state.db：首见清零建基线，token 增长部分记增量，profile=角色归因。"""
    _, _, hermes = _wire(tmp_path, monkeypatch)
    db = hermes / "laowantong" / "state.db"
    _mk_hermes_db(hermes, "laowantong", {"input": 1000, "output": 100})
    acc, _ = tm.collect()
    assert acc == {}  # 首见不计存量
    # 增长 200/30
    conn = sqlite3.connect(str(db))
    conn.execute("UPDATE sessions SET input_tokens=1200, output_tokens=130 WHERE id='sess1'")
    conn.commit(); conn.close()
    acc, _ = tm.collect()
    t = acc["hermes"]["laowantong"]
    assert t["input"] == 200 and t["output"] == 30


def test_daily_summary_render(tmp_path, monkeypatch):
    """日汇总 md：引擎×会话表格 + 合计行 + #514 口径注记。"""
    acc = {"claude": {"s1": {"input": 1, "output": 2, "cache_read": 3, "cache_write": 4}}}
    md = tm.render_markdown("2026-08-27", acc)
    assert "2026-08-27" in md and "合计" in md and "#514" in md


def test_dry_run_does_not_consume_cursor(tmp_path, monkeypatch):
    """dry-run 零副作用（F-036 教训）：save=False 不落游标，正式跑仍能吃到同批增量。"""
    claude, _, _ = _wire(tmp_path, monkeypatch)
    f = claude / "s.jsonl"
    f.write_text(json.dumps({"message": {"usage": {"input_tokens": 1, "output_tokens": 1}}}) + "\n",
                 encoding="utf-8")
    tm.collect()  # 建游标
    with open(f, "a", encoding="utf-8") as fh:
        fh.write(json.dumps({"message": {"usage": {"input_tokens": 42, "output_tokens": 7}}}) + "\n")
    acc_dry, _ = tm.collect(save=False)   # dry-run：看得见
    assert acc_dry["claude"]["s"]["input"] == 42
    acc_real, _ = tm.collect()            # 正式跑：游标未被 dry-run 消费，同批增量还在
    assert acc_real["claude"]["s"]["input"] == 42
    assert tm.collect()[0] == {}          # 之后无新增 → 空


def test_bootstrap_counts_today_only(tmp_path, monkeypatch):
    """首日引导：首见文件全扫但只计今日记录——昨日历史不回溯，今日读数真实。"""
    import datetime as _dt
    claude, _, _ = _wire(tmp_path, monkeypatch)
    today = _dt.datetime.now().strftime("%Y-%m-%dT01:00:00")
    yesterday = (_dt.datetime.now() - _dt.timedelta(days=1)).strftime("%Y-%m-%dT23:00:00")
    f = claude / "s.jsonl"
    nl = chr(10)  # P-34：heredoc 转义教训——换行用 chr(10) 不写字面 \n
    f.write_text(
        json.dumps({"timestamp": yesterday, "message": {"usage": {"input_tokens": 999, "output_tokens": 9}}}) + nl
        + json.dumps({"timestamp": today, "message": {"usage": {"input_tokens": 50, "output_tokens": 5}}}) + nl,
        encoding="utf-8")
    boot = _dt.datetime.now().replace(hour=0, minute=0, second=0, microsecond=0).timestamp()
    acc, _ = tm.collect(bootstrap_since=boot)
    t0 = acc["claude"]["s"]
    assert t0["input"] == 50 and t0["output"] == 5  # 昨日 999 不回溯
    # 引导后游标已落 → 正常增量不重计
    acc2, _ = tm.collect()
    assert acc2 == {}
