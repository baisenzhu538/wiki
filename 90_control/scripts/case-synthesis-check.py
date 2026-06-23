#!/usr/bin/env python3
"""
跨案例合成触发检测。域内 case 卡 ≥ 15 张 → 自动生成王语嫣扫描任务。
集成到每日巡检: python case-synthesis-check.py
"""

import re, sys
from collections import defaultdict
from datetime import datetime
from pathlib import Path

VAULT = Path(r"C:\Users\Administrator\Desktop\wiki")
THRESHOLD = 15
TASK_DIR = VAULT / "60_feedback" / "tasks"


def scan():
    wiki = VAULT / "30_wiki"
    domains = defaultdict(list)

    for f in wiki.rglob("*.md"):
        if any(p in str(f) for p in ["_archive", "raw/", ".git"]):
            continue
        try:
            text = f.read_text(encoding="utf-8")[:2000]
        except:
            continue
        m = re.search(r"^id:\s*(.+)$", text, re.MULTILINE)
        if not m:
            continue
        cid = m.group(1).strip()
        m2 = re.search(r"^type:\s*(.+)$", text, re.MULTILINE)
        ctype = m2.group(1).strip() if m2 else "?"
        if ctype != "case":
            continue
        m3 = re.search(r"^domain:\s*\[(.*?)\]", text, re.MULTILINE)
        if not m3:
            m3 = re.search(r"^domain:\s*(.+)$", text, re.MULTILINE)
        if not m3:
            continue
        for d in m3.group(1).split(","):
            d = d.strip().strip('"').strip("'").strip("[").strip("]")
            if d and not d.startswith("-"):
                domains[d].append(cid)

    return domains


def check_already_flagged(domain: str) -> bool:
    """Check if synthesis task already exists for this domain."""
    task_file = TASK_DIR / f"task_synthesis_{domain}.md"
    return task_file.exists()


def generate_task(domain: str, case_ids: list[str], count: int):
    """Generate 王语嫣 synthesis task."""
    task_file = TASK_DIR / f"task_synthesis_{domain}.md"
    if task_file.exists():
        return False  # already exists

    now = datetime.now().strftime("%Y-%m-%d")
    content = f"""---
id: task_synthesis_{domain}
type: synthesis_trigger
created_at: {now}
domain: {domain}
case_count: {count}
assignee: 王语嫣
status: pending
---

# 跨案例合成任务：{domain} 域

> **自动触发**：{domain} 域 case 卡已达 {count} 张（≥{THRESHOLD} 阈值）。

## 任务

王语嫣扫描 {domain} 域全部 {count} 张 case 卡，输出 2-3 个跨案例模式。

### Step 1：扫描
- Read 全域 case 卡，提取每个案例的核心教训和失败模式
- 识别跨案例的共性根因和反直觉模式

### Step 2：输出
- 2-3 条跨案例洞察，写入 `60_feedback/audit/synthesis_{domain}.md`
- 每条洞察含：模式描述 + 支撑案例（≥3 个）+ 框架未覆盖的理由

### Step 3：传递
- 老顽童读取洞察，产 dk 卡（dk-{domain}-synthesis-*）

## 参考
- KF-025 三问自检第 3 条："这些案例有共同模式吗？"
- 黄药师成品验收顾问可咨询
"""
    task_file.parent.mkdir(parents=True, exist_ok=True)
    task_file.write_text(content, encoding="utf-8")
    return True


def main():
    domains = scan()
    triggered = []

    for domain, case_ids in sorted(domains.items(), key=lambda x: -len(x[1])):
        count = len(case_ids)
        if count < THRESHOLD:
            continue
        already = check_already_flagged(domain)
        if already:
            continue
        new = generate_task(domain, case_ids, count)
        if new:
            triggered.append((domain, count))

    if triggered:
        print(f"触发 {len(triggered)} 个新合成任务:")
        for d, c in triggered:
            print(f"  {d}: {c} 张 case → task_synthesis_{d}.md")

    # 输出当前所有达标域的状态
    print(f"\n域 case 统计（≥{THRESHOLD} 触发）:")
    for domain, case_ids in sorted(domains.items(), key=lambda x: -len(x[1])):
        count = len(case_ids)
        marker = "🔴 新触发" if domain in dict(triggered) else ("🟡 已有任务" if check_already_flagged(domain) else ("🟢 达标" if count >= THRESHOLD else "  ")))
        if count >= THRESHOLD or count >= 10:
            print(f"  {marker} {domain:30s} {count:4d} case")


if __name__ == "__main__":
    main()
