#!/usr/bin/env python3
"""quality_metrics.py — 质量指标基线统计（#514，口径=90_control/quality-metrics-spec-v1.md）。

四类指标（王语嫣裁决口径 v1）：
1. FAIL 率（动作级）= 终审退回动作数 ÷ 终审动作总数（PASS+退回）——数据源=队列历史划掉行
2. 打回率（单级）= 周期内至少被打回一次的任务单数 ÷ 周期内提审过的任务单数（去重计单）
3. 门禁拦截率 = gate-blocked.log 拦截条数 ÷ 流转动作数（代理分母=窗口内提审+终审动作，
   按类型分类：F-034/F-035/E040 交付物/pre-submit/其他）
4. 误判率代理 = force 例外次数 ÷ 拦截次数（force-exceptions.log ÷ gate-blocked.log）

阶段 0 纪律：只读统计，不改任何流程。按周聚合（周一~周日），每周一出上周报。

用法：
  python kdo-tools/quality_metrics.py                 # 上周（周一~周日）报告
  python kdo-tools/quality_metrics.py --from 2026-08-23 --to 2026-08-25   # 自定义窗口（回溯狗粮）
  python kdo-tools/quality_metrics.py --stdout        # 只打印不落盘
"""
import argparse
import re
import sys
from collections import Counter
from datetime import date, datetime, timedelta
from pathlib import Path

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")

VAULT_ROOT = Path(__file__).resolve().parent.parent
QUEUE_FILE = VAULT_ROOT / "70_product" / "tasks" / "production-queue.md"
GATE_BLOCKED_LOG = VAULT_ROOT / "90_control" / "gate-blocked.log"
FORCE_LOG = VAULT_ROOT / "90_control" / "force-exceptions.log"
OUT_DIR = VAULT_ROOT / "60_feedback" / "auto" / "quality-metrics"

# 队列历史划掉行：- ~~#SEQ task_id｜assignee｜提审 MM-DD HH:MM｜path~~ → 已终审 PASS X（YYYY-MM-DD …）/终审退回 …（YYYY-MM-DD …）
_ROW_RE = re.compile(
    r"^- ~~#(\d+) (\S+?)｜(\S+?)｜提审 (\d{2})-(\d{2}) (\d{2}:\d{2})｜(.*?)~~ → "
    r"(已终审 PASS\s*[A-]*|终审退回).*?（(\d{4})-(\d{2})-(\d{2})")
_GB_RE = re.compile(r"^(\d{4}-\d{2}-\d{2}) \d{2}:\d{2}:\d{2}｜(\S+?)｜(\S+?)｜")
_FORCE_RE = re.compile(r"^(\d{4}-\d{2}-\d{2}) \d{2}:\d{2}:\d{2}｜")


def parse_queue_history(text: str) -> list[dict]:
    """解析队列划掉行 → 终审动作流（每行=一次完整 提审→终审 动作）。"""
    actions = []
    for line in text.splitlines():
        m = _ROW_RE.match(line.strip())
        if not m:
            continue
        seq, tid, assignee, sm, sd, shm, _path, verdict, ty, tm, td = m.groups()
        terminal_date = date(int(ty), int(tm), int(td))
        # 提审行无年份：从终审日推（提审月日大于终审月日=跨年，回退一年）
        submit_date = date(terminal_date.year, int(sm), int(sd))
        if submit_date > terminal_date:
            submit_date = date(terminal_date.year - 1, int(sm), int(sd))
        actions.append({
            "seq": int(seq), "task_id": tid, "assignee": assignee,
            "submit": submit_date, "terminal": terminal_date,
            "pass": verdict.startswith("已终审"),
        })
    return actions


def parse_gate_blocked(text: str) -> list[tuple[date, str]]:
    """gate-blocked.log → [(日期, 拦截类型)]。类型归并：F-034/F-035/E040/pre-submit/其他。"""
    out = []
    for line in text.splitlines():
        m = _GB_RE.match(line.strip())
        if not m:
            continue
        d = date.fromisoformat(m.group(1))
        gate = m.group(3)
        if gate.startswith("F-034"):
            kind = "F-034 五字段"
        elif gate.startswith("F-035"):
            kind = "F-035 意见书"
        elif gate.startswith("E040"):
            kind = "E040 交付物入仓"
        elif "pre-submit" in gate.lower():
            kind = "pre-submit"
        elif gate.startswith(("L1-", "探针")):
            kind = "其他(机器自报)"
        else:
            kind = "其他"
        out.append((d, kind))
    return out


def parse_force_exceptions(text: str) -> list[date]:
    return [date.fromisoformat(m.group(1))
            for line in text.splitlines() if (m := _FORCE_RE.match(line.strip()))]


def _in(d: date, start: date, end: date) -> bool:
    return start <= d <= end


def compute_metrics(actions: list[dict], gates: list[tuple[date, str]],
                    forces: list[date], start: date, end: date) -> dict:
    """按口径 v1 计算四类指标。窗口闭区间 [start, end]，按事件发生日过滤。"""
    # 终审动作（按终审日入窗）
    term = [a for a in actions if _in(a["terminal"], start, end)]
    n_pass = sum(1 for a in term if a["pass"])
    n_fail = sum(1 for a in term if not a["pass"])
    fail_rate = n_fail / (n_pass + n_fail) if term else None

    # 打回率（单级）：提审日入窗的单为分母；其中至少一次终审退回（窗口内）的单为分子
    submitted = {a["task_id"] for a in actions if _in(a["submit"], start, end)}
    bounced = {a["task_id"] for a in term if not a["pass"]} & submitted
    bounce_rate = len(bounced) / len(submitted) if submitted else None

    # 门禁拦截（按日入窗，分类计数）；分母=窗口内流转动作（提审+终审，代理口径）
    gb = [g for g in gates if _in(g[0], start, end)]
    gb_by_kind = Counter(k for _, k in gb)
    n_submit_actions = sum(1 for a in actions if _in(a["submit"], start, end))
    flow_actions = n_submit_actions + len(term)
    block_rate = len(gb) / flow_actions if flow_actions else None

    # 误判率代理：force 例外 ÷ 拦截
    fx = [f for f in forces if _in(f, start, end)]
    force_rate = len(fx) / len(gb) if gb else None

    return {
        "window": (start, end),
        "review_actions": len(term), "pass": n_pass, "fail": n_fail, "fail_rate": fail_rate,
        "submitted_tasks": len(submitted), "bounced_tasks": len(bounced), "bounce_rate": bounce_rate,
        "gate_blocks": len(gb), "gate_by_kind": dict(gb_by_kind),
        "flow_actions": flow_actions, "block_rate": block_rate,
        "force_exceptions": len(fx), "force_rate": force_rate,
    }


def _pct(x: float | None) -> str:
    return "样本不足" if x is None else f"{x * 100:.1f}%"


def render_report(m: dict, out_path: Path | None) -> str:
    start, end = m["window"]
    kinds = "、".join(f"{k} {v}" for k, v in sorted(m["gate_by_kind"].items())) or "无"
    lines = [
        f"# 质量指标周报（{start} ~ {end}）",
        "",
        "> 口径：90_control/quality-metrics-spec-v1.md（王语嫣裁决 v1）；阶段 0 纯统计不改流程",
        "",
        "| 指标 | 值 | 分子/分母 |",
        "|:--|:--|:--|",
        f"| FAIL 率（动作级） | {_pct(m['fail_rate'])} | 终审退回 {m['fail']} ÷ 终审动作 {m['review_actions']}（PASS {m['pass']}） |",
        f"| 打回率（单级） | {_pct(m['bounce_rate'])} | 被打回单 {m['bounced_tasks']} ÷ 提审单 {m['submitted_tasks']}（去重） |",
        f"| 门禁拦截率 | {_pct(m['block_rate'])} | 拦截 {m['gate_blocks']} ÷ 流转动作 {m['flow_actions']}（代理分母=提审+终审） |",
        f"| 误判率（代理=force 放行率） | {_pct(m['force_rate'])} | force 例外 {m['force_exceptions']} ÷ 拦截 {m['gate_blocks']} |",
        "",
        f"门禁拦截分类：{kinds}",
        "",
        "口径注记：①拦截≠终审 FAIL（两类不合并）；②流转动作分母为代理（claim 无机器留痕）；"
        "③真误判需人工标注，基线期用代理（spec v1 §4）。",
    ]
    return "\n".join(lines) + "\n"


def last_week(today: date) -> tuple[date, date]:
    monday = today - timedelta(days=today.weekday())
    return monday - timedelta(days=7), monday - timedelta(days=1)


def main() -> int:
    ap = argparse.ArgumentParser(description="质量指标基线统计（#514）")
    ap.add_argument("--from", dest="start", help="窗口起 YYYY-MM-DD（默认上周一）")
    ap.add_argument("--to", dest="end", help="窗口止 YYYY-MM-DD（默认上周日）")
    ap.add_argument("--stdout", action="store_true", help="只打印不落盘")
    args = ap.parse_args()

    start, end = (
        (date.fromisoformat(args.start), date.fromisoformat(args.end))
        if args.start and args.end else last_week(date.today())
    )

    actions = parse_queue_history(QUEUE_FILE.read_text(encoding="utf-8")) if QUEUE_FILE.exists() else []
    gates = parse_gate_blocked(GATE_BLOCKED_LOG.read_text(encoding="utf-8", errors="replace")) if GATE_BLOCKED_LOG.exists() else []
    forces = parse_force_exceptions(FORCE_LOG.read_text(encoding="utf-8", errors="replace")) if FORCE_LOG.exists() else []

    m = compute_metrics(actions, gates, forces, start, end)
    report = render_report(m, None)
    print(report)
    if not args.stdout:
        OUT_DIR.mkdir(parents=True, exist_ok=True)
        out = OUT_DIR / f"{start.isoformat()}_{end.isoformat()}.md"
        out.write_text(report, encoding="utf-8")
        print(f"📄 报告落盘: {out}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
