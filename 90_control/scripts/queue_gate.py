"""Queue advance gate for KDO production queue.

Validates whether a task can be claimed by a Producer instance.
Hard rules:
- Only tasks with status `queued` can be claimed.
- No earlier task in the queue may be in `pending_review` status (must wait for 欧阳锋终审).
- Producer must never change a task status to `reviewed`; only 欧阳锋 can do that.

Usage:
    python queue_gate.py check <task-id>         # Check if task can be claimed
    python queue_gate.py next                    # Show the next claimable task
    python queue_gate.py status                  # Show blocking pending_review tasks

Exit codes:
    0 = claimable / gate passes
    1 = not claimable / gate fails
"""

from __future__ import annotations
import sys
if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")
if hasattr(sys.stderr, "reconfigure"):
    sys.stderr.reconfigure(encoding="utf-8", errors="replace")

import re
import sys
from pathlib import Path

QUEUE_PATH = Path(__file__).resolve().parent.parent.parent / "70_product" / "tasks" / "production-queue.md"


def parse_queue(path: Path = QUEUE_PATH) -> list[dict]:
    """Parse production-queue.md table rows.

    Detection is encoding-robust: uses the ASCII separator row ``|:---:|…``
    to find the queue data table rather than matching Chinese header text.
    """
    rows = []
    in_table = False
    with open(path, "r", encoding="utf-8") as f:
        for line in f:
            line = line.rstrip("\n")
            if not in_table:
                # Detect table by separator row — pure ASCII, immune to
                # Mojibake / double-encoding issues on Chinese headers.
                if re.match(r"^\|:---", line.strip()):
                    in_table = True
                continue
            # Skip separator / alignment rows (belt-and-suspenders)
            if re.match(r"^\|:---", line.strip()):
                continue
            # Skip blank lines between rows
            if line.strip() == "":
                continue
            # End of table
            if not line.startswith("|"):
                break
            cells = [c.strip() for c in line.strip("|").split("|")]
            if len(cells) < 5:
                continue
            def clean(s: str) -> str:
                return s.strip().strip("*").strip("`").strip()

            rows.append({
                "seq": clean(cells[0]),
                "task_id": clean(cells[1]),
                "name": clean(cells[2]),
                "status": clean(cells[3]),
                "assignee": clean(cells[4]) if len(cells) > 4 else "",
                "raw": line,
            })
    return rows


def find_task(task_id: str, rows: list[dict] | None = None) -> dict | None:
    if rows is None:
        rows = parse_queue()
    tid = task_id.strip("`")
    for row in rows:
        if row["task_id"] == tid:
            return row
    return None


def find_blockers(rows: list[dict] | None = None) -> tuple[list[dict], list[dict]]:
    """Return (pending_review_tasks, claimed_tasks) that block queue advance."""
    if rows is None:
        rows = parse_queue()
    pending = []
    claimed = []
    for row in rows:
        status = row["status"]
        if status == "pending_review":
            pending.append(row)
        elif status.startswith("claimed-"):
            claimed.append(row)
    return pending, claimed


def can_claim(task_id: str, rows: list[dict] | None = None, instance: str = "") -> tuple[bool, str]:
    """Return (ok, reason).

    不同实例可以并行领取（Hermes 不堵 Kimi，Kimi 不堵 Claude）。
    同一实例不能跳队——前方有自己的 claimed 任务时必须等释放。
    """
    if rows is None:
        rows = parse_queue()

    task = find_task(task_id, rows)
    if task is None:
        return False, f"任务 {task_id} 不在生产队列中"

    if task["status"] == "reviewed":
        return False, f"任务 {task_id} 已经是 reviewed，无需领取"

    if task["status"] == "pending_review":
        return False, f"任务 {task_id} 是 pending_review，等待欧阳锋终审，老顽童不能领取"

    if task["status"] == "blocked":
        return False, f"任务 {task_id} 被阻塞（blocked），不能领取"

    if not task["status"].startswith("queued"):
        return False, f"任务 {task_id} 状态为 {task['status']}，不是可领取的 queued 状态"

    # Find earlier tasks
    pending, claimed = find_blockers(rows)
    earlier_pending = [r for r in pending if r["task_id"] != task_id]

    if earlier_pending:
        ids = ", ".join(f"#{r['seq']} {r['task_id']}" for r in earlier_pending)
        return False, f"队列前方还有 pending_review 任务未终审：{ids}。必须等它们 reviewed 后才能领取 {task_id}"

    # claimed 阻塞规则：只有同一实例的 claimed 才阻塞
    if instance:
        same_instance_claimed = [
            r for r in claimed
            if r["task_id"] != task_id and instance in r.get("assignee", "")
        ]
    else:
        same_instance_claimed = [r for r in claimed if r["task_id"] != task_id]

    if same_instance_claimed:
        ids = ", ".join(f"#{r['seq']} {r['task_id']}" for r in same_instance_claimed)
        return False, f"你的实例 {instance} 还有 claimed 任务未释放：{ids}。必须等它们释放后才能领取 {task_id}"

    return True, f"任务 {task_id} 可领取"


def next_claimable(rows: list[dict] | None = None, instance: str = "") -> dict | None:
    if rows is None:
        rows = parse_queue()
    for row in rows:
        ok, _ = can_claim(row["task_id"], rows, instance)
        if ok:
            return row
    return None


def main() -> int:
    cmd = sys.argv[1] if len(sys.argv) > 1 else "status"

    if cmd == "check":
        if len(sys.argv) < 3:
            print("Usage: queue_gate.py check <task-id>", file=sys.stderr)
            return 1
        task_id = sys.argv[2]
        ok, reason = can_claim(task_id)
        print(reason)
        return 0 if ok else 1

    elif cmd == "next":
        rows = parse_queue()
        task = next_claimable(rows)
        if task:
            print(f"NEXT_CLAIMABLE #{task['seq']} {task['task_id']} — {task['name']}")
            return 0
        else:
            pending, claimed = find_blockers(rows)
            if pending:
                ids = ", ".join(f"#{r['seq']} {r['task_id']}" for r in pending)
                print(f"BLOCKED_BY_PENDING_REVIEW: {ids}")
            elif claimed:
                ids = ", ".join(f"#{r['seq']} {r['task_id']}" for r in claimed)
                print(f"BLOCKED_BY_CLAIMED: {ids}")
            else:
                print("NO_QUEUED_TASKS")
            return 1

    elif cmd == "status":
        rows = parse_queue()
        pending, claimed = find_blockers(rows)
        next_task = next_claimable(rows)
        print(f"队列总任务数: {len(rows)}")
        print(f"pending_review 阻塞数: {len(pending)}")
        for r in pending:
            print(f"  #{r['seq']} {r['task_id']} — {r['name']}")
        print(f"claimed 执行中数: {len(claimed)}")
        for r in claimed:
            print(f"  #{r['seq']} {r['task_id']} — {r['assignee']}")
        if next_task:
            print(f"下一个可领取: #{next_task['seq']} {next_task['task_id']} — {next_task['name']}")
        else:
            print("下一个可领取: 无")
        return 0

    else:
        print("Usage: queue_gate.py [check <task-id>|next|status]", file=sys.stderr)
        return 1


if __name__ == "__main__":
    sys.exit(main())
