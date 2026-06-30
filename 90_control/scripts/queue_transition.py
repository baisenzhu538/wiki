"""Hard state transition enforcer for the KDO production queue.

All queue status changes MUST go through this script. Manual edits to
`production-queue.md` or task file `status` fields are forbidden.

Usage:
    python queue_transition.py claim <task-id> --instance <name>
    python queue_transition.py complete <task-id> --instance <name> [--evidence <path>]
    python queue_transition.py release <task-id> --instance <name>
    python queue_transition.py review <task-id> --verdict pass|fail --reviewer 欧阳锋

Exit codes:
    0 = transition applied
    1 = transition rejected / error
"""

from __future__ import annotations

import re
import sys
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

try:
    import yaml
except ImportError:  # pragma: no cover
    yaml = None

# Make queue_gate importable from the same directory
SCRIPT_DIR = Path(__file__).resolve().parent
sys.path.insert(0, str(SCRIPT_DIR))

from queue_gate import QUEUE_PATH, can_claim, find_task, parse_queue
from queue_lock import QueueLock

TASK_DIR = Path(__file__).resolve().parent.parent.parent / "60_feedback" / "tasks"
BATCH_DIR = Path(__file__).resolve().parent.parent.parent / "70_product" / "tasks"

# Valid transitions. Format: (current_status, action) -> new_status
# instance/reviewer checks are performed separately.
TRANSITIONS: dict[tuple[str, str], str] = {
    ("queued", "claim"): "claimed-{instance}",
    ("claimed-{instance}", "complete"): "pending_review",
    ("claimed-{instance}", "release"): "claimed-{instance}",
    ("pending_review", "review_pass"): "reviewed",
    ("pending_review", "review_fail"): "queued",
}


def parse_frontmatter(path: Path) -> tuple[dict[str, Any], str]:
    """Return (frontmatter_dict, body)."""
    text = path.read_text(encoding="utf-8")
    if not text.startswith("---"):
        return {}, text
    # Match leading frontmatter block: ---\n<yaml>\n---\n<body>
    match = re.match(r"^---\r?\n(.*?)\r?\n---\r?\n(.*)$", text, re.DOTALL)
    if not match:
        return {}, text
    fm_text, body = match.group(1), match.group(2)
    if yaml is None:
        raise RuntimeError("PyYAML is required to parse frontmatter")
    data = yaml.safe_load(fm_text) or {}
    return data, body


def write_frontmatter(path: Path, fm: dict[str, Any], body: str) -> None:
    """Write file with YAML frontmatter, preserving body."""
    if yaml is None:
        raise RuntimeError("PyYAML is required to write frontmatter")
    fm_text = yaml.safe_dump(fm, sort_keys=False, allow_unicode=True, default_flow_style=False)
    path.write_text(f"---\n{fm_text}---\n{body}", encoding="utf-8")


def find_task_file(task_id: str) -> Path | None:
    """Locate task file by id in known task directories."""
    candidates = [
        TASK_DIR / f"{task_id}.md",
        BATCH_DIR / f"{task_id}.md",
    ]
    for c in candidates:
        if c.exists():
            return c
    return None


def update_queue_status(task_id: str, new_status: str) -> None:
    """Atomically update the status cell in production-queue.md."""
    text = QUEUE_PATH.read_text(encoding="utf-8")
    lines = text.splitlines()
    updated = []
    tid = task_id.strip("`").strip("*")
    found = False
    for line in lines:
        if line.startswith("|") and not set(line.strip()) <= {"|", "-", ":", " "}:
            cells = [c for c in line.strip("|").split("|")]
            if len(cells) >= 4 and cells[1].strip().strip("*").strip("`").strip() == tid:
                # Replace only the 4th cell (status), preserving surrounding formatting
                cells[3] = f" {new_status} "
                updated.append("|" + "|".join(cells) + "|")
                found = True
                continue
        updated.append(line)
    if not found:
        raise ValueError(f"任务 {task_id} 未在生产队列中找到")
    QUEUE_PATH.write_text("\n".join(updated) + "\n", encoding="utf-8")


def update_task_frontmatter(task_file: Path, **updates: Any) -> None:
    """Update task file frontmatter keys."""
    fm, body = parse_frontmatter(task_file)
    for key, value in updates.items():
        if value is not None:
            fm[key] = value
    fm["updated_at"] = datetime.now(timezone.utc).isoformat()
    write_frontmatter(task_file, fm, body)


def current_utc_date() -> str:
    return datetime.now(timezone.utc).strftime("%Y-%m-%d")


def action_claim(task_id: str, instance: str) -> tuple[bool, str]:
    """Claim a queued task for an instance."""
    rows = parse_queue()
    ok, reason = can_claim(task_id, rows)
    if not ok:
        return False, reason

    task_file = find_task_file(task_id)
    if task_file is None:
        return False, f"找不到任务单文件: {task_id}"

    with QueueLock("production-queue"):
        # Re-check gate inside lock
        rows = parse_queue()
        ok, reason = can_claim(task_id, rows)
        if not ok:
            return False, reason

        new_status = f"claimed-{instance}"
        update_queue_status(task_id, new_status)
        update_task_frontmatter(task_file, assignee=instance, status="in_progress")

    return True, f"✅ {task_id} 已领取为 {new_status}"


def action_complete(task_id: str, instance: str, evidence: str | None) -> tuple[bool, str]:
    """Mark a claimed task as pending_review."""
    rows = parse_queue()
    task = find_task(task_id, rows)
    if task is None:
        return False, f"任务 {task_id} 不在队列中"

    expected = f"claimed-{instance}"
    if task["status"] != expected:
        return False, f"任务 {task_id} 状态为 {task['status']}，不是由 {instance} 领取的 {expected}"

    task_file = find_task_file(task_id)
    if task_file is None:
        return False, f"找不到任务单文件: {task_id}"

    fm, _ = parse_frontmatter(task_file)
    if evidence is None:
        # Default evidence: task file must contain an execution report / pre-submit section
        body = task_file.read_text(encoding="utf-8")
        has_evidence = "pre-submit" in body.lower() or "执行报告" in body or "验收" in body
        if not has_evidence:
            return False, "任务单中缺少生产完成证据（pre-submit / 执行报告 / 验收）。老顽童不能标 pending_review。"

    with QueueLock("production-queue"):
        rows = parse_queue()
        task = find_task(task_id, rows)
        if task is None or task["status"] != expected:
            return False, "队列状态在加锁期间发生变化，请重试"

        update_queue_status(task_id, "pending_review")
        update_task_frontmatter(task_file, status="pending_review")

    return True, f"✅ {task_id} 已提交为 pending_review，等待欧阳锋终审"


def action_release(task_id: str, instance: str) -> tuple[bool, str]:
    """Release a claimed task back to queued."""
    rows = parse_queue()
    task = find_task(task_id, rows)
    if task is None:
        return False, f"任务 {task_id} 不在队列中"

    expected = f"claimed-{instance}"
    if task["status"] != expected:
        return False, f"任务 {task_id} 状态为 {task['status']}，不是 {expected}"

    task_file = find_task_file(task_id)
    if task_file is None:
        return False, f"找不到任务单文件: {task_id}"

    with QueueLock("production-queue"):
        update_queue_status(task_id, "queued")
        update_task_frontmatter(task_file, status="queued")

    return True, f"✅ {task_id} 已释放回 queued"


def action_review(task_id: str, verdict: str, reviewer: str) -> tuple[bool, str]:
    """Ouyangfeng-only: review a pending_review task."""
    if reviewer != "欧阳锋":
        return False, "只有欧阳锋可以执行 review 操作"

    rows = parse_queue()
    task = find_task(task_id, rows)
    if task is None:
        return False, f"任务 {task_id} 不在队列中"
    if task["status"] != "pending_review":
        return False, f"任务 {task_id} 状态为 {task['status']}，不是 pending_review，无法终审"

    task_file = find_task_file(task_id)
    if task_file is None:
        return False, f"找不到任务单文件: {task_id}"

    with QueueLock("production-queue"):
        if verdict == "pass":
            update_queue_status(task_id, "reviewed")
            update_task_frontmatter(
                task_file,
                status="reviewed",
                reviewed_by=reviewer,
                review_date=current_utc_date(),
            )
            return True, f"✅ {task_id} 终审通过，状态更新为 reviewed"
        else:
            update_queue_status(task_id, "queued")
            update_task_frontmatter(task_file, status="queued")
            return True, f"⚠️ {task_id} 终审不通过，状态退回 queued"


def main() -> int:
    if yaml is None:
        print("ERROR: PyYAML is required. Install with: pip install pyyaml", file=sys.stderr)
        return 1

    args = sys.argv[1:]
    if not args:
        print(__doc__, file=sys.stderr)
        return 1

    action = args[0]

    if action == "status":
        rows = parse_queue()
        pending = [r for r in rows if r["status"] == "pending_review"]
        claimed = [r for r in rows if r["status"].startswith("claimed-")]
        queued = [r for r in rows if r["status"] == "queued"]
        print(f"队列总任务数: {len(rows)}")
        print(f"queued: {len(queued)}")
        print(f"claimed: {len(claimed)}")
        print(f"pending_review: {len(pending)}")
        for r in pending:
            print(f"  #{r['seq']} {r['task_id']} — {r['name']}")
        return 0

    if len(args) < 2:
        print(__doc__, file=sys.stderr)
        return 1

    task_id = args[1]

    instance = None
    evidence = None
    verdict = None
    reviewer = None

    i = 2
    while i < len(args):
        if args[i] == "--instance" and i + 1 < len(args):
            instance = args[i + 1]
            i += 2
        elif args[i] == "--evidence" and i + 1 < len(args):
            evidence = args[i + 1]
            i += 2
        elif args[i] == "--verdict" and i + 1 < len(args):
            verdict = args[i + 1]
            i += 2
        elif args[i] == "--reviewer" and i + 1 < len(args):
            reviewer = args[i + 1]
            i += 2
        else:
            print(f"未知参数: {args[i]}", file=sys.stderr)
            return 1

    if action == "claim":
        if not instance:
            print("claim 需要 --instance <instance>", file=sys.stderr)
            return 1
        ok, msg = action_claim(task_id, instance)
    elif action == "complete":
        if not instance:
            print("complete 需要 --instance <instance>", file=sys.stderr)
            return 1
        ok, msg = action_complete(task_id, instance, evidence)
    elif action == "release":
        if not instance:
            print("release 需要 --instance <instance>", file=sys.stderr)
            return 1
        ok, msg = action_release(task_id, instance)
    elif action == "review":
        if verdict not in ("pass", "fail"):
            print("review 需要 --verdict pass|fail", file=sys.stderr)
            return 1
        if not reviewer:
            reviewer = "欧阳锋"
        ok, msg = action_review(task_id, verdict, reviewer)
    else:
        print(__doc__, file=sys.stderr)
        return 1

    print(msg)
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
