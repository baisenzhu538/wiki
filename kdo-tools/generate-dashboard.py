#!/usr/bin/env python3
"""从 production-queue.md 自动生成 dashboard.html。

用法:
    python kdo-tools/generate-dashboard.py [--input production-queue.md] [--output dashboard.html]
"""

import re
import sys
from pathlib import Path
from datetime import datetime

ROOT = Path(__file__).resolve().parent.parent
DEFAULT_INPUT = ROOT / "70_product/tasks/production-queue.md"
DEFAULT_OUTPUT = ROOT / "70_product/tasks/dashboard.html"

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
    """解析 production-queue.md 表格，返回任务列表。"""
    text = path.read_text(encoding="utf-8")
    tasks = []
    in_table = False
    for line in text.split("\n"):
        line = line.strip()
        if line.startswith("| 队列序号"):
            in_table = True
            continue
        if in_table and line.startswith("|---"):
            continue
        if in_table and line.startswith("|") and not line.startswith("| 队列序号"):
            cells = [c.strip() for c in line.split("|")[1:-1]]
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
                })
        elif in_table and not line.startswith("|"):
            break
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


def _task_card_html(task: dict, show_group: str) -> str:
    p = task["priority"].lower()
    status_groups = {
        "pending": ("审查中 · 等待欧阳锋", "pending"),
        "queued": ("待领取", "queued"),
        "active": ("进行中", "active"),
    }
    return f"""<div class="task-card">
<div class="task-prio {p}">{task['priority']}</div>
<div class="task-info">
<div class="task-id">#{task['seq']}</div>
<div class="task-title">{task['name']}</div>
<div class="task-detail">{task['notes'] or task['cards'] + ' 张卡' if task['cards'] and task['cards'] != '0' else ''}</div>
</div>
<div class="task-meta">
<span class="task-assignee {_assignee_class(task['assignee'])}">{task['assignee']}</span>
</div>
</div>"""


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
    }

    sections_html = ""
    for key, (label, cls) in section_labels.items():
        if not grouped[key]:
            continue
        cards = "\n".join(_task_card_html(t, key) for t in grouped[key])
        sections_html += f"""
<div class="task-group">
<div class="group-header {cls}">{label}</div>
{cards}
</div>"""

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
.task-card{{background:var(--card);border:1px solid var(--border);border-radius:10px;padding:14px 16px;margin-bottom:8px;display:flex;align-items:center;gap:14px;transition:border-color .15s}}
.task-card:hover{{border-color:#4a4d57}}
.task-prio{{width:28px;height:28px;border-radius:7px;display:flex;align-items:center;justify-content:center;font-size:12px;font-weight:800;flex-shrink:0}}
.task-prio.p0{{background:rgba(217,83,79,.2);color:var(--blocked)}}
.task-prio.p1{{background:rgba(240,173,78,.2);color:var(--queued)}}
.task-prio.p2{{background:rgba(107,112,128,.2);color:var(--muted)}}
.task-info{{flex:1;min-width:0}}
.task-id{{font-size:11px;color:var(--muted);margin-bottom:2px}}
.task-title{{font-size:14px;font-weight:600;white-space:nowrap;overflow:hidden;text-overflow:ellipsis}}
.task-detail{{font-size:12px;color:var(--muted);margin-top:4px;white-space:nowrap;overflow:hidden;text-overflow:ellipsis}}
.task-meta{{display:flex;gap:12px;align-items:center;flex-shrink:0}}
.task-assignee{{font-size:12px;padding:4px 10px;border-radius:20px;font-weight:600}}
.task-assignee.laowantong{{background:rgba(26,115,232,.12);color:var(--ai)}}
.task-assignee.huangyaoshi{{background:rgba(231,76,60,.12);color:var(--human)}}
.task-assignee.wangyuyan{{background:rgba(92,184,92,.12);color:var(--review)}}
.task-assignee.ouyangfeng{{background:rgba(240,173,78,.12);color:var(--queued)}}
.task-eta{{font-size:12px;color:var(--muted)}}
footer{{text-align:center;color:var(--muted);font-size:11px;margin-top:32px;padding-top:16px;border-top:1px solid var(--border)}}
</style>
</head>
<body>
<h1>KDO 生产看板</h1>
<p class="subtitle">production-queue.md · 自动生成于 {now}</p>

<div class="stats">
{stats_html}
</div>

{sections_html}

<footer>KDO 知识工厂 · 由 generate-dashboard.py 自动生成 · {now}</footer>
</body>
</html>"""
    output.write_text(html, encoding="utf-8")
    print(f"✅ dashboard.html 已生成 ({len(tasks)} 个任务)")
    print(f"   待领取: {counts['queued']}  |  审查中: {counts['pending']}  |  进行中: {counts['active']}  |  已完成: {counts['done']}")


def main():
    input_path = Path(sys.argv[1]) if len(sys.argv) > 1 else DEFAULT_INPUT
    output_path = Path(sys.argv[2]) if len(sys.argv) > 2 else DEFAULT_OUTPUT
    if not input_path.exists():
        print(f"❌ 找不到 {input_path}")
        sys.exit(1)
    tasks = parse_queue(input_path)
    generate_html(tasks, output_path)


if __name__ == "__main__":
    main()
