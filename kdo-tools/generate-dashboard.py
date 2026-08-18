#!/usr/bin/env python3
"""从 production-queue.md 自动生成 dashboard.html。

用法:
    python kdo-tools/generate-dashboard.py [--input production-queue.md] [--output dashboard.html]
"""

import re
import sys
if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")
if hasattr(sys.stderr, "reconfigure"):
    sys.stderr.reconfigure(encoding="utf-8", errors="replace")
from pathlib import Path
from datetime import datetime

ROOT = Path(__file__).resolve().parent.parent
DEFAULT_INPUT = ROOT / "70_product/tasks/production-queue.md"
DEFAULT_OUTPUT = ROOT / "70_product/tasks/dashboard.html"
TASKS_DIR = ROOT / "60_feedback" / "tasks"

STATUS_LABELS = {
    "queued": ("待领取", "queued"),
    "pending_review": ("审查中", "pending"),
    "claimed": ("进行中", "active"),
    "reviewed": ("已完成", "done"),
    "done": ("已完成", "done"),
    "confirmed": ("已确认", "done"),
    "closed_cancelled": ("已取消", "done"),
    "closed_merged": ("已合并", "done"),
}


def parse_queue(path: Path) -> list[dict]:
    """解析 production-queue.md 表格，返回任务列表。

    表格检测使用纯 ASCII 分隔行 ``|:---``，不依赖中文表头——文件编码损坏时也能工作。
    """
    text = path.read_text(encoding="utf-8")
    tasks = []
    in_table = False
    for line in text.split("\n"):
        stripped = line.strip()
        if not in_table:
            # Detect table by separator row — pure ASCII, immune to encoding issues
            if stripped.startswith("|:---"):
                in_table = True
            continue
        # Skip separator / alignment rows
        if stripped.startswith("|:---"):
            continue
        # Skip blank lines between rows
        if not stripped:
            continue
        # End of table
        if not stripped.startswith("|"):
            break
        cells = [c.strip() for c in stripped.split("|")[1:-1]]
        if len(cells) >= 7:
            try:
                seq = int(cells[0].strip())
            except ValueError:
                continue
            task_id = cells[1].strip().strip("`")
            name = cells[2].strip()
            status_raw = cells[3].strip()
            assignee = cells[4].strip() if len(cells) > 4 else ""
            cards = cells[5].strip() if len(cells) > 5 else ""
            deps = cells[6].strip() if len(cells) > 6 else ""
            source = cells[7].strip().strip("`") if len(cells) > 7 else ""
            notes = cells[8].strip() if len(cells) > 8 else ""

            status = _normalize_status(status_raw)

            priority = _extract_priority(name, notes)

            # #284+ 终审等级提取：从注释列 "PASS(条件) A-/B+/C" 解析评定等级
            grade = ""
            conditional = False
            if "PASS" in notes:
                conditional = "条件" in notes
                m = re.search(r"PASS(?:[（(]\s*条件\s*[）)])?\s*(A-|A|B\+|B-|B|C)", notes)
                if m:
                    grade = m.group(1)
                elif "FAIL" in notes or "退回" in notes:
                    grade = "FAIL"

            tasks.append({
                "seq": seq,
                "id": task_id,
                "name": name,
                "status": status,
                "status_raw": status_raw,
                "assignee": _normalize_assignee(assignee),
                "cards": cards,
                "deps": deps,
                "source": source,
                "notes": _truncate(notes, 120),
                "priority": priority,
                "grade": grade,
                "conditional": conditional,
            })
    return tasks


def _normalize_status(raw: str) -> str:
    raw = raw.strip().lower()
    if raw.startswith("claimed"):
        return "claimed"
    if raw in STATUS_LABELS:
        return raw
    if "review" in raw:
        return "reviewed"
    return raw


def _normalize_assignee(raw: str) -> str:
    raw = raw.strip().rstrip("）").rstrip(")")
    if not raw or raw in ("-", "—"):
        return ""
    # 提取中文名
    m = re.search(r"([一-鿿]{2,4})", raw)
    if m:
        name = m.group(1)
        if name in ("黄药师", "老顽童", "王语嫣", "欧阳锋", "洪七公", "段王爷"):
            return name
    # 英文 id
    m = re.search(r"([a-z_]+)", raw)
    if m:
        aid = m.group(1)
        id_map = {
            "huangyaoshi": "黄药师",
            "laowantong": "老顽童",
            "wangyuyan": "王语嫣",
            "ouyangfeng": "欧阳锋",
            "hongqigong": "洪七公",
            "duanwangye": "段王爷",
            "workbuddy": "WorkBuddy",
        }
        return id_map.get(aid, aid)
    return raw


def _extract_priority(name: str, notes: str) -> str:
    text = name + " " + notes
    m = re.search(r"\b(P0|P1|P2|P3)\b", text)
    if m:
        return m.group(1)
    return "P1"


def _truncate(s: str, n: int) -> str:
    if len(s) <= n:
        return s
    return s[:n] + "…"


def _assignee_class(name: str) -> str:
    m = {
        "黄药师": "huangyaoshi",
        "老顽童": "laowantong",
        "王语嫣": "wangyuyan",
        "欧阳锋": "ouyangfeng",
        "洪七公": "hongqigong",
    }
    return m.get(name, "laowantong")


def _status_group(status: str) -> str:
    """将状态映射到看板分组: pending / queued / active / done"""
    if status == "pending_review":
        return "pending"
    if status == "queued":
        return "queued"
    if status == "claimed":
        return "active"
    return "done"


def parse_rework_rounds() -> dict[str, dict]:
    """#269: 从任务单 frontmatter 提取首交率数据（#267+ 起记录 rework 字段）。

    约定（task-orchestration 硬规则 3 + #267 起）：
      rework: 0   # 一次通过
      rework: N   # 返工 N 次
    无 rework 字段的任务单不计入分母（不拉低首交率），显示"记录中"。

    返回 { "2026-08": {"pass": int, "total": int}, ... }
    """
    if not TASKS_DIR.is_dir():
        return {}
    months: dict[str, dict] = {}
    for f in sorted(TASKS_DIR.glob("task_*.md")):
        try:
            text = f.read_text(encoding="utf-8", errors="ignore")
        except OSError:
            continue
        fm = {}
        m = re.match(r"^---\n(.*?)\n---", text, re.S)
        if not m:
            continue
        for line in m.group(1).splitlines():
            if ":" in line:
                k, v = line.split(":", 1)
                fm[k.strip()] = v.strip()
        if "rework" not in fm:
            continue
        try:
            rework = int(fm["rework"])
        except ValueError:
            continue
        # 月份取 review_date（终审月）→ updated_at → 文件 mtime 兜底
        date_src = fm.get("review_date") or fm.get("updated_at") or ""
        month = date_src[:7] if re.match(r"^\d{4}-\d{2}", date_src) else datetime.fromtimestamp(f.stat().st_mtime).strftime("%Y-%m")
        months.setdefault(month, {"pass": 0, "total": 0})
        months[month]["total"] += 1
        if rework == 0:
            months[month]["pass"] += 1
    return months


def first_submit_rate_html(months: dict[str, dict]) -> str:
    """#269: 首交率区块——本月首交率 + 近 3 月趋势。无数据优雅降级。"""
    if not months:
        return """<div class="fsr-block">
<div class="fsr-title">首交通过率 First-Submit Rate</div>
<div class="fsr-empty">记录中 — 任务单补 `rework: 0/N` 字段后自动统计（#267+ 起）</div>
</div>"""
    cur = sorted(months.keys())[-1]
    cur_data = months[cur]
    rate = cur_data["pass"] / cur_data["total"] * 100 if cur_data["total"] else 0
    trend_months = sorted(months.keys())[-3:]
    trend_html = ""
    for mm in trend_months:
        d = months[mm]
        r = d["pass"] / d["total"] * 100 if d["total"] else 0
        bar = "█" * max(1, int(r / 10)) + "░" * (10 - max(1, int(r / 10)))
        trend_html += f'<div class="fsr-trend"><span class="fsr-month">{mm}</span> <span class="fsr-bar">{bar}</span> <span class="fsr-pct">{r:.0f}%</span> <span class="fsr-count">({d["pass"]}/{d["total"]})</span></div>'
    cls = "fsr-good" if rate >= 80 else ("fsr-mid" if rate >= 50 else "fsr-bad")
    note = "编排侧：规格质量" if rate < 50 else "编排侧：执行质量"
    return f"""<div class="fsr-block {cls}">
<div class="fsr-title">首交通过率 First-Submit Rate · {cur}</div>
<div class="fsr-big">{rate:.0f}%</div>
<div class="fsr-sub">一次通过 {cur_data['pass']} / 共 {cur_data['total']} 个任务 · {note}</div>
<div class="fsr-trends">{trend_html}</div>
</div>"""


def _task_card_html(task: dict, show_group: str) -> str:
    p = task["priority"].lower()
    status_groups = {
        "pending": ("审查中 · 等待欧阳锋", "pending"),
        "queued": ("待领取", "queued"),
        "active": ("进行中", "active"),
    }
    grade_badge = ""
    if task.get("grade"):
        cond_mark = "⚠" if task.get("conditional") else ""
        grade_badge = f'<span class="task-grade g-{task["grade"].replace("+", "p")}">{task["grade"]}{cond_mark}</span>'
    return f"""<div class="task-card">
<div class="task-prio {p}">{task['priority']}</div>
<div class="task-info">
<div class="task-id">#{task['seq']}{grade_badge}</div>
<div class="task-title">{task['name']}</div>
<div class="task-detail">{task['notes'] or task['cards'] + ' 张卡' if task['cards'] and task['cards'] != '0' else ''}</div>
</div>
<div class="task-meta">
<span class="task-assignee {_assignee_class(task['assignee'])}">{task['assignee']}</span>
</div>
</div>"""


def _git_head() -> str:
    import subprocess
    try:
        return subprocess.run(["git", "-C", str(ROOT), "rev-parse", "--short", "HEAD"],
                              capture_output=True, text=True, timeout=10).stdout.strip()
    except Exception:
        return "unknown"


def _record_derived_hash(output: Path) -> None:
    """#369: 生成后记录输出 hash 到基线文件，供 check-derivatives.py 手改检测。"""
    import hashlib, json
    hash_file = ROOT / "90_control" / "scripts" / ".derived-hashes.json"
    hashes = {}
    if hash_file.exists():
        try:
            hashes = json.loads(hash_file.read_text(encoding="utf-8"))
        except Exception:
            pass
    hashes[str(output)] = hashlib.sha256(output.read_bytes()).hexdigest()
    hash_file.write_text(json.dumps(hashes, indent=1, ensure_ascii=False), encoding="utf-8")


def generate_html(tasks: list[dict], output: Path) -> None:
    grouped = {"pending": [], "queued": [], "active": [], "done": []}
    for t in tasks:
        g = _status_group(t["status"])
        grouped[g].append(t)

    # 去重：active 中的任务如果在 pending 中已出现，从 active 移除
    pending_ids = {t["id"] for t in grouped["pending"]}
    grouped["active"] = [t for t in grouped["active"] if t["id"] not in pending_ids]

    counts = {k: len(v) for k, v in grouped.items()}
    active_agents = len(set(t["assignee"] for t in tasks if t["assignee"]))

    status_groups = [
        ("queued", "待领取 Queued", "queued"),
        ("pending", "审查中 Review", "pending"),
        ("active", "进行中 Active", "active"),
        ("done", "已完成 Done", "done"),
    ]

    stats_html = "\n".join(
        f'<div class="stat {cls}"><div class="stat-num">{counts[k]}</div><div class="stat-label">{label}</div></div>'
        for k, label, cls in status_groups
    )
    stats_html += f'\n<div class="stat owner"><div class="stat-num">{active_agents}</div><div class="stat-label">活跃角色</div></div>'

    section_labels = {
        "pending": ("审查中 · 等待欧阳锋", "pending"),
        "queued": ("待领取", "queued"),
        "active": ("进行中", "active"),
        "done": ("已完成 · 终审评级", "done"),
    }

    sections_html = ""
    for key, (label, cls) in section_labels.items():
        items = grouped[key] if key != "done" else [t for t in grouped["done"] if t.get("grade")]
        if not items:
            continue
        cards = "\n".join(_task_card_html(t, key) for t in items)
        sections_html += f"""
<div class="task-group">
<div class="group-header {cls}">{label}</div>
{cards}
</div>"""

    fsr_html = first_submit_rate_html(parse_rework_rounds())

    now = datetime.now().strftime("%Y-%m-%d %H:%M")
    html = f"""<!DOCTYPE html>
<html lang="zh-CN">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>KDO 生产看板</title>
<style>
:root{{--bg:#0f1117;--card:#1a1d27;--border:#2a2d37;--text:#e1e4ea;--muted:#6b7080;--human:#e74c3c;--ai:#1a73e8;--queued:#f0ad4e;--review:#5cb85c;--blocked:#d9534f;--merged:#6b7080;}}
*{{margin:0;padding:0;box-sizing:border-box}}
body{{font-family:-apple-system,BlinkMacSystemFont,'Segoe UI','PingFang SC','Microsoft YaHei',sans-serif;background:var(--bg);color:var(--text);padding:24px;min-height:100vh}}
h1{{font-size:20px;font-weight:700;margin-bottom:4px;letter-spacing:-0.3px}}
.subtitle{{color:var(--muted);font-size:13px;margin-bottom:24px}}
.stats{{display:grid;grid-template-columns:repeat(5,1fr);gap:12px;margin-bottom:24px}}
.stat{{padding:16px;border-radius:10px;text-align:center}}
.stat-num{{font-size:28px;font-weight:800;letter-spacing:-1px}}
.stat-label{{font-size:11px;text-transform:uppercase;letter-spacing:0.5px;margin-top:4px;color:var(--muted)}}
.stat.queued{{background:#2a2410;border:1px solid #4a3a10}}.stat.queued .stat-num{{color:var(--queued)}}
.stat.pending{{background:#1a2a1a;border:1px solid #2a4a2a}}.stat.pending .stat-num{{color:var(--review)}}
.stat.active{{background:#1a1a2a;border:1px solid #2a2a4a}}.stat.active .stat-num{{color:var(--ai)}}
.stat.done{{background:#1a2227;border:1px solid #2a3237}}.stat.done .stat-num{{color:var(--muted)}}
.stat.owner{{background:#2a1a1a;border:1px solid #4a2a2a}}.stat.owner .stat-num{{color:var(--human)}}
.task-group{{margin-bottom:20px}}
.group-header{{font-size:12px;font-weight:700;text-transform:uppercase;letter-spacing:1px;margin-bottom:10px;padding:6px 12px;border-radius:6px;display:inline-block}}
.group-header.queued{{background:rgba(240,173,78,.12);color:var(--queued)}}
.group-header.pending{{background:rgba(92,184,92,.12);color:var(--review)}}
.group-header.active{{background:rgba(26,115,232,.12);color:var(--ai)}}
.group-header.done{{background:rgba(107,112,128,.12);color:var(--muted)}}
.task-card{{background:var(--card);border:1px solid var(--border);border-radius:10px;padding:14px 16px;margin-bottom:8px;display:flex;align-items:center;gap:14px;transition:border-color .15s}}
.task-card:hover{{border-color:#4a4d57}}
.task-prio{{width:28px;height:28px;border-radius:7px;display:flex;align-items:center;justify-content:center;font-size:12px;font-weight:800;flex-shrink:0}}
.task-prio.p0{{background:rgba(217,83,79,.2);color:var(--blocked)}}
.task-prio.p1{{background:rgba(240,173,78,.2);color:var(--queued)}}
.task-prio.p2{{background:rgba(107,112,128,.2);color:var(--muted)}}
.task-info{{flex:1;min-width:0}}
.task-id{{font-size:11px;color:var(--muted);margin-bottom:2px;display:flex;align-items:center;gap:6px}}
.task-grade{{font-size:10px;font-weight:800;padding:1px 5px;border-radius:4px}}
.task-grade.g-A{{background:rgba(60,179,113,.25);color:#2e9e66}}
.task-grade.g-Ap{{background:rgba(60,179,113,.25);color:#2e9e66}}
.task-grade.g-Bp{{background:rgba(240,173,78,.3);color:#d99a2b}}
.task-grade.g-B{{background:rgba(240,173,78,.2);color:#c98a1e}}
.task-grade.g-C{{background:rgba(217,83,79,.25);color:var(--blocked)}}
.task-title{{font-size:14px;font-weight:600;white-space:nowrap;overflow:hidden;text-overflow:ellipsis}}
.task-detail{{font-size:12px;color:var(--muted);margin-top:4px;white-space:nowrap;overflow:hidden;text-overflow:ellipsis}}
.task-meta{{display:flex;gap:12px;align-items:center;flex-shrink:0}}
.task-assignee{{font-size:12px;padding:4px 10px;border-radius:20px;font-weight:600}}
.task-assignee.laowantong{{background:rgba(26,115,232,.12);color:var(--ai)}}
.task-assignee.huangyaoshi{{background:rgba(231,76,60,.12);color:var(--human)}}
.task-assignee.wangyuyan{{background:rgba(92,184,92,.12);color:var(--review)}}
.task-assignee.ouyangfeng{{background:rgba(240,173,78,.12);color:var(--queued)}}
.task-eta{{font-size:12px;color:var(--muted)}}
.fsr-block{{background:var(--card);border:1px solid var(--border);border-radius:10px;padding:16px;margin-bottom:24px}}
.fsr-block.fsr-good{{border-color:#2a4a3a}}.fsr-block.fsr-mid{{border-color:#4a3a10}}.fsr-block.fsr-bad{{border-color:#4a2a2a}}
.fsr-title{{font-size:12px;font-weight:700;text-transform:uppercase;letter-spacing:1px;color:var(--muted);margin-bottom:8px}}
.fsr-big{{font-size:32px;font-weight:800;color:var(--review)}}
.fsr-sub{{font-size:12px;color:var(--muted);margin-bottom:12px}}
.fsr-trend{{font-size:12px;color:var(--muted);margin-top:4px;font-family:monospace}}
.fsr-bar{{color:var(--review)}}
.fsr-pct{{color:var(--text);font-weight:600}}
.fsr-count{{color:var(--muted)}}
.fsr-empty{{font-size:13px;color:var(--muted)}}
footer{{text-align:center;color:var(--muted);font-size:11px;margin-top:32px;padding-top:16px;border-top:1px solid var(--border)}}
</style>
</head>
<body>
<h1>KDO 生产看板</h1>
<p class="subtitle">production-queue.md · 自动生成于 {now}</p>

<div class="stats">
{stats_html}
</div>

{fsr_html}

{sections_html}

<header style="display:none"><!-- generated-by: generate-dashboard.py · updated_at: {now} · git_head: {_git_head()} --></header>
<footer>KDO 知识工厂 · 由 generate-dashboard.py 自动生成 · {now}</footer>
</body>
</html>"""
    output.write_text(html, encoding="utf-8")
    _record_derived_hash(output)
    print(f"✅ dashboard.html 已生成 ({len(tasks)} 个任务)")
    print(f"   待领取: {counts['queued']}  |  审查中: {counts['pending']}  |  进行中: {counts['active']}  |  已完成: {counts['done']}")


def main(input_path=None, output_path=None):
    input_path = Path(input_path) if input_path else DEFAULT_INPUT
    output_path = Path(output_path) if output_path else DEFAULT_OUTPUT
    if not input_path.exists():
        print(f"❌ 找不到 {input_path}", file=sys.stderr)
        sys.exit(1)
    tasks = parse_queue(input_path)
    generate_html(tasks, output_path)


if __name__ == "__main__":
    main()
