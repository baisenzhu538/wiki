#!/usr/bin/env python3
"""
KDO 跨案例合成触发检测。
扫描全库 case 卡，域内 >= 15 张 case -> 自动生成王语嫣合成任务。
集成到每日巡检: python 90_control/scripts/case-synthesis-check.py
"""
import re
from collections import defaultdict
from datetime import datetime
from pathlib import Path

VAULT = Path(r"C:\Users\Administrator\Desktop\wiki\30_wiki")
TASK_DIR = Path(r"C:\Users\Administrator\Desktop\wiki\60_feedback\tasks")
THRESHOLD = 15


def scan() -> dict[str, list[str]]:
    domains = defaultdict(list)
    for f in VAULT.rglob("*.md"):
        if any(p in str(f) for p in ["_archive", "raw/", ".git"]):
            continue
        try:
            text = f.read_text(encoding="utf-8")[:2000]
        except Exception:
            continue
        m = re.search(r"^id:\s*(.+)$", text, re.MULTILINE)
        if not m:
            continue
        cid = m.group(1).strip()
        m2 = re.search(r"^type:\s*(.+)$", text, re.MULTILINE)
        ctype = m2.group(1).strip() if m2 else ""
        if ctype != "case":
            continue
        m3 = re.search(r"^domain:\s*\[(.*?)\]", text, re.MULTILINE)
        if not m3:
            m3 = re.search(r"^domain:\s*(.+)$", text, re.MULTILINE)
        if not m3:
            continue
        for d in m3.group(1).split(","):
            d = d.strip().strip('"').strip("'").strip("[").strip("]")
            if d and not d.startswith("-") and d != "master":
                domains[d].append(cid)
    return dict(domains)


def already_flagged(domain: str) -> bool:
    return (TASK_DIR / f"task_synthesis_{domain}.md").exists()


def generate_task(domain: str, count: int):
    task_file = TASK_DIR / f"task_synthesis_{domain}.md"
    if task_file.exists():
        return False
    now = datetime.now().strftime("%Y-%m-%d")
    content = (
        f"---\n"
        f"id: task_synthesis_{domain}\n"
        f"type: synthesis_trigger\n"
        f"created_at: {now}\n"
        f"domain: {domain}\n"
        f"case_count: {count}\n"
        f"assignee: 王语嫣\n"
        f"status: pending\n"
        f"---\n\n"
        f"# 跨案例合成任务: {domain} 域\n\n"
        f"> 自动触发: case 卡 {count} 张 >= {THRESHOLD} 阈值\n\n"
        f"## Step 1: 王语嫣扫描全域 case 卡\n"
        f"- 提取每个案例的核心教训和失败模式\n"
        f"- 识别跨案例的共性根因和反直觉模式\n\n"
        f"## Step 2: 输出 2-3 条跨案例洞察\n"
        f"- 写入 `60_feedback/audit/synthesis_{domain}.md`\n"
        f"- 每条洞察含: 模式描述 + 支撑案例 (>=3) + 框架未覆盖的理由\n\n"
        f"## Step 3: 传递老顽童\n"
        f"- 老顽童读取洞察, 产 dk 卡 (dk-{domain}-synthesis-*)\n"
        f"- 黄药师可咨询\n"
        f"- 参考: KF-025 三问第 3 条\n"
    )
    TASK_DIR.mkdir(parents=True, exist_ok=True)
    task_file.write_text(content, encoding="utf-8")
    return True


def main():
    domains = scan()
    triggered = []
    for domain, case_ids in sorted(domains.items(), key=lambda x: -len(x[1])):
        count = len(case_ids)
        if count < THRESHOLD:
            continue
        if already_flagged(domain):
            continue
        if generate_task(domain, count):
            triggered.append((domain, count))

    if triggered:
        print(f"NEW SYNTHESIS TASKS: {len(triggered)}")
        for d, c in triggered:
            print(f"  {d}: {c} cases -> task_synthesis_{d}.md")

    print(f"\nDomain case counts (threshold={THRESHOLD}):")
    for domain, case_ids in sorted(domains.items(), key=lambda x: -len(x[1])):
        count = len(case_ids)
        if count >= 10:
            if domain in dict(triggered):
                tag = "NEW"
            elif already_flagged(domain):
                tag = "TASKED"
            elif count >= THRESHOLD:
                tag = "READY"
            else:
                tag = ""
            print(f"  {tag:6s}  {domain:30s} {count:4d}")


if __name__ == "__main__":
    main()
