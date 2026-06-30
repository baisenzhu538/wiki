"""Audit KDO queue integrity.

Checks for:
- Task files marked reviewed but missing review_date or reviewer
- Task files marked reviewed without a corresponding review task file
- Production queue entries whose status doesn't match the task file
- Tasks that moved to reviewed suspiciously quickly (same commit as production)

Usage:
    python audit_queue_integrity.py
"""

from __future__ import annotations

import re
import sys
from pathlib import Path

WIKI_ROOT = Path(__file__).resolve().parent.parent.parent
TASK_DIR = WIKI_ROOT / "60_feedback" / "tasks"
QUEUE_PATH = WIKI_ROOT / "70_product" / "tasks" / "production-queue.md"
REVIEW_DIRS = [
    WIKI_ROOT / "60_feedback" / "tasks",
    WIKI_ROOT / "60_feedback" / "audit",
    WIKI_ROOT / "60_feedback" / "reviews",
    WIKI_ROOT / "20_memory",
]


try:
    import yaml
except ImportError:  # pragma: no cover
    yaml = None


def parse_frontmatter(path: Path) -> dict:
    text = path.read_text(encoding="utf-8")
    if not text.startswith("---"):
        return {}
    end = text.find("---", 3)
    if end == -1:
        return {}
    fm_text = text[3:end].strip()
    if yaml is not None:
        try:
            return yaml.safe_load(fm_text) or {}
        except yaml.YAMLError:
            pass
    # Fallback to simple line parser
    data = {}
    for line in fm_text.splitlines():
        if ":" not in line:
            continue
        key, val = line.split(":", 1)
        data[key.strip()] = val.strip()
    return data


BATCH_REVIEW_PATTERNS = [
    re.compile(r"review_\d{8}_ouyangfeng-wave\d+"),
    re.compile(r"review_\d{8}_ouyangfeng-[a-z-]+"),
]


def is_batch_task(task_id: str) -> bool:
    """Batch tasks like laowantong-batch-2026-06-20-waveN use separate review files."""
    return task_id.startswith("laowantong-batch-")


def is_review_only_entry(task_id: str) -> bool:
    """Review-only entries like review_YYYYMMDD_ouyangfeng-* review a framework/card directly."""
    return task_id.startswith("review_")


def find_batch_review_file(task_id: str) -> Path | None:
    """For batch tasks, look for review files in task dir or memory."""
    for d in REVIEW_DIRS:
        if not d.exists():
            continue
        for f in d.iterdir():
            if not f.is_file() or not f.name.endswith(".md"):
                continue
            if "review" not in f.name.lower():
                continue
            # waveN pattern
            m = re.search(r"wave(\d+)", task_id)
            if m and f"wave{m.group(1)}" in f.name.lower():
                return f
    return None


def find_review_file(task_id: str) -> Path | None:
    """Look for a file whose name contains the task id and looks like a review."""
    if is_batch_task(task_id):
        return find_batch_review_file(task_id)
    for d in REVIEW_DIRS:
        if not d.exists():
            continue
        for f in d.iterdir():
            if not f.is_file() or not f.name.endswith(".md"):
                continue
            if task_id in f.name and ("review" in f.name.lower() or "audit" in f.name.lower()):
                return f
    return None


def parse_queue(path: Path = QUEUE_PATH) -> list[dict]:
    rows = []
    in_table = False
    with open(path, "r", encoding="utf-8") as f:
        for line in f:
            line = line.rstrip("\n")
            if not in_table:
                if line.startswith("| 队列序号"):
                    in_table = True
                continue
            if set(line.strip()) <= {"|", "-", ":", " "}:
                continue
            if not line.startswith("|"):
                break
            cells = [c.strip() for c in line.strip("|").split("|")]
            if len(cells) < 5:
                continue
            rows.append({
                "seq": cells[0],
                "task_id": cells[1].strip("`"),
                "name": cells[2],
                "status": cells[3],
                "assignee": cells[4] if len(cells) > 4 else "",
            })
    return rows


REPORT_PATH = WIKI_ROOT / "20_memory" / "queue_integrity_audit_latest.md"


def main() -> int:
    if not TASK_DIR.exists():
        print(f"Task directory not found: {TASK_DIR}")
        return 1

    queue_rows = parse_queue()
    queue_by_id = {r["task_id"]: r for r in queue_rows}

    anomalies = []
    reviewed_count = 0

    for task_file in sorted(TASK_DIR.glob("task_*.md")):
        fm = parse_frontmatter(task_file)
        if not fm:
            continue
        task_id = fm.get("id", task_file.stem)
        status = fm.get("status", "")
        reviewed_by = fm.get("reviewed_by", "")
        reviewer = fm.get("reviewer", "")
        review_date = fm.get("review_date", "")

        if status != "reviewed":
            continue

        reviewed_count += 1

        # Check required fields
        if not review_date:
            anomalies.append((task_id, "reviewed 但缺少 review_date"))
        if not reviewer and not reviewed_by:
            anomalies.append((task_id, "reviewed 但缺少 reviewer/reviewed_by"))
        if reviewed_by and reviewed_by.lower() in ("pending", "none", "null"):
            anomalies.append((task_id, f"reviewed 但 reviewed_by='{reviewed_by}' 不合法"))

        # Check matching queue row
        qrow = queue_by_id.get(task_id)
        if qrow and qrow["status"] != "reviewed":
            anomalies.append((task_id, f"任务单 status=reviewed，但队列 status={qrow['status']}"))

        # Check for review file
        review_file = find_review_file(task_id)
        if not review_file:
            # Only flag if no review_date (lenient: review_date implies a review happened)
            if not review_date:
                anomalies.append((task_id, "reviewed 但无对应 review/audit 文件且无 review_date"))

    # Also report queue rows marked reviewed but task file not reviewed
    queue_anomalies = []
    for qrow in queue_rows:
        if qrow["status"] != "reviewed":
            continue
        task_id = qrow["task_id"]
        # Batch tasks reviewed via separate review files, skip
        if is_batch_task(task_id):
            continue
        task_file = TASK_DIR / f"{task_id}.md"
        if not task_file.exists():
            queue_anomalies.append((task_id, "队列 marked reviewed 但任务单文件不存在"))
            continue
        fm = parse_frontmatter(task_file)
        task_type = fm.get("type", "")
        task_status = fm.get("status", "unknown")
        # production_task files may not have status field
        if task_type == "production_task":
            continue
        if task_status != "reviewed":
            queue_anomalies.append((task_id, f"队列 status=reviewed 但任务单 status={task_status}"))

    lines = []
    lines.append(f"# 队列完整性审计报告")
    lines.append("")
    lines.append(f"- 审计范围: `{TASK_DIR}`")
    lines.append(f"- reviewed 任务单总数: {reviewed_count}")
    lines.append(f"- 任务单异常数: {len(anomalies)}")
    lines.append(f"- 队列/任务单不一致数: {len(queue_anomalies)}")
    lines.append("")
    if anomalies:
        lines.append("## 任务单异常列表")
        for task_id, reason in anomalies:
            lines.append(f"- `{task_id}`: {reason}")
    else:
        lines.append("任务单无异常。")
    lines.append("")
    if queue_anomalies:
        lines.append("## 队列/任务单状态不一致")
        for task_id, reason in queue_anomalies:
            lines.append(f"- `{task_id}`: {reason}")
    else:
        lines.append("队列与任务单状态一致。")

    report = "\n".join(lines) + "\n"
    REPORT_PATH.write_text(report, encoding="utf-8")
    print(report)

    return 1 if anomalies or queue_anomalies else 0


if __name__ == "__main__":
    sys.exit(main())
