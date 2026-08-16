#!/usr/bin/env python3
"""KDO 队列健康对账 v0（#284 第一部分 / E021 机器化）

任务单 frontmatter（id/status）vs production-queue.md 行全量比对：
  1. 队列行引用的任务单文件缺失
  2. 任务单非终态（非 reviewed/done/closed_cancelled）但队列无行
  3. 队列行与任务单状态不一致（E019 家族）

用法：
  python kdo-tools/queue_audit.py            # 全量对账，输出不一致清单
  python kdo-tools/queue_audit.py --brief    # 只输出计数（hooks/dashboard 用）
退出码：0 = 一致；1 = 存在不一致（供 hook 判断）
"""
import re
import sys
sys.stdout.reconfigure(encoding="utf-8", errors="replace")
import glob
import os

WIKI = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
QUEUE = os.path.join(WIKI, "70_product", "tasks", "production-queue.md")
TASK_DIRS = [
    os.path.join(WIKI, "60_feedback", "tasks"),
    os.path.join(WIKI, "70_product", "tasks"),
]
TERMINAL = {"reviewed", "done", "closed_cancelled", "deleted", "closed"}
# 历史体系外任务前缀（#284 判定：不追溯，不报 orphan）
# 已归档任务（#284 判定：文件已归档，任务已终态——不报 missing）
ARCHIVED_IDS = {
    "laowantong-batch-2026-06-20-wave1", "laowantong-batch-2026-06-20-wave2", "laowantong-batch-2026-06-20-wave3",
    "laowantong-batch-2026-06-20-wave4", "laowantong-batch-2026-06-20-wave5", "task_20260703_laowantong-yitang-Y-model-os",
    "task_20260712_wangyuyan-d-domain-p0-skeleton", "task_20260712_wangyuyan-d-domain-p1-tools", "task_20260712_wangyuyan-d-domain-p2-cases-batch1",
    "task_20260712_wangyuyan-d-domain-agent-and-closure", "task_20260712_wangyuyan-d-domain-p3-cases-batch2", "task_20260712_wangyuyan-d-domain-p1-tools-batch2",
    "task_20260712_wangyuyan-c-domain-scan-fix-structure", "task_20260712_wangyuyan-c-domain-scan-fix-assets", "task_20260713_wangyuyan-coach-dialogue-engine-protocol",
    "task_20260713_wangyuyan-decision-coach-engine-upgrade", "task_20260713_wangyuyan-c-domain-coach-engine-align", "task_20260713_wangyuyan-five-step-coach-agent",
    "task_20260713_wangyuyan-opc-sales-assistant-engine-adapt", "task_20260713_wangyuyan-opc-sales-d-domain-linking", "task_20260713_wangyuyan-c-domain-evidence-recheck",
    "task_20260713_wangyuyan-full-vault-yaml-audit", "task_20260713_wangyuyan-template-placeholder-hygiene", "task_20260713_wangyuyan-agent-spec-prompts-ingestion",
    "task_20260714_wangyuyan-material-gaps-tracking", "task_20260806_wangyuyan-deep-review-core", "task_20260806_wangyuyan-deep-review-backlinks",
}
LEGACY_PREFIXES = ("task_20260614_", "task_synthesis_", "task_20260620_", "task_2026062", "task_2026062", "task_20260623_", "task_20260624_", "task_20260625_")


def parse_queue():
    rows = {}
    try:
        data = open(QUEUE, "rb").read().decode("utf-8", errors="replace")
    except FileNotFoundError:
        return rows
    for ln in data.split("\n"):
        m = re.match(r"\|\s*(\d+)\s*\|\s*`([^`]+)`", ln)
        if m:
            cells = [c.strip().strip("`").strip() for c in ln.strip().strip("|").split("|")]
            rows[m.group(2)] = {"num": int(m.group(1)), "status": cells[3] if len(cells) > 3 else "?", "raw": ln}
    return rows


def read_frontmatter_status(path):
    try:
        txt = open(path, encoding="utf-8").read()
        m = re.search(r"(?m)^status:\s*[\"']?(\S+)", txt)
        return m.group(1).strip("\"'`") if m else "?"
    except (OSError, UnicodeDecodeError):
        return "?"


def audit():
    queue_rows = parse_queue()
    issues = []

    # 1. 队列行有但文件缺失（跳过已归档标注行）
    for name, info in queue_rows.items():
        if name in ARCHIVED_IDS:
            continue
        found = any(os.path.exists(os.path.join(d, name + ".md")) for d in TASK_DIRS)
        if not found:
            issues.append(("missing-file", name, f"队列#{info['num']} 文件不存在"))

    # 2/3. 任务单文件非终态但队列无行 / 状态不一致
    seen = set()
    for d in TASK_DIRS:
        for f in glob.glob(os.path.join(d, "task_*.md")):
            base = os.path.basename(f)[:-3]
            seen.add(base)
            st = read_frontmatter_status(f)
            if base in queue_rows:
                qs = queue_rows[base]["status"]
                norm_qs = qs.split("-")[0] if qs.startswith("claimed") else qs
                if qs != "?" and st not in TERMINAL and st not in ("?",) and qs != st and not (norm_qs == "claimed" and st == "in_progress"):
                    issues.append(("status-mismatch", base, f"队列={qs} 任务单={st} (E019)"))
            elif st not in TERMINAL and st not in ("?", "draft", "proposed", "wangyuyan-confirmed", "ready_for_production", "open") and not base.startswith(LEGACY_PREFIXES) and st not in ("enriched", "updated", "todo", "doing", "completed"):
                issues.append(("orphan", base, f"非终态({st})但队列无行"))

    return issues, queue_rows


def main():
    brief = "--brief" in sys.argv
    issues, rows = audit()
    if brief:
        print(f"QUEUE_AUDIT: total={len(rows)} issues={len(issues)} missing={sum(1 for i in issues if i[0]=='missing-file')} mismatch={sum(1 for i in issues if i[0]=='status-mismatch')} orphan={sum(1 for i in issues if i[0]=='orphan')}")
        sys.exit(1 if issues else 0)
    if not issues:
        print(f"✅ 队列对账：0 不一致（{len(rows)} 行）")
        sys.exit(0)
    print(f"⚠️ 队列对账发现 {len(issues)} 项不一致：")
    for kind, name, detail in issues:
        print(f"  [{kind}] {name}: {detail}")
    sys.exit(1)


if __name__ == "__main__":
    main()
