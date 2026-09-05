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

import os
import re
import sys
from pathlib import Path

# KDO_QUEUE_PATH 环境变量允许测试/多环境指向替代队列（默认参数在函数定义
# 时绑定，monkeypatch 无效，只能在这里解耦）
QUEUE_PATH = Path(
    os.environ.get("KDO_QUEUE_PATH")
    or (Path(__file__).resolve().parent.parent.parent / "70_product" / "tasks" / "production-queue.md")
)


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
            # #647：表段可被段间块（划销清单/PROPOSAL 等非表行）打断——实证
            # production-queue.md 中 #430-444/#647/#648 落第二段，break 使后续
            # 队列行整体不可见（claim 报「不在生产队列中」）。改为跳过非表行
            # 继续扫到文件尾；下方 ≥5 列守卫继续过滤非队列表。
            if not line.startswith("|"):
                continue
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


def _is_batch_task(task_id: str) -> bool:
    """#492：任务单 frontmatter `batch: true` → 长程分批任务（批次提审不阻塞前方主线）。

    #426（739 张 tags 分批）每批提审一次就卡住后方所有任务——batch 标记让
    「批次提审」（验收后恢复 queued）与「整单提审」（终审闭环）可区分。
    """
    import re as _re
    fp = Path(__file__).resolve().parent.parent.parent / "60_feedback" / "tasks" / f"{task_id}.md"
    try:
        text = fp.read_text(encoding="utf-8", errors="ignore")
    except OSError:
        return False
    return bool(_re.search(r"^batch:\s*(true|True|1)\s*$", text, _re.M))


# #580（F-064）：任务单目录提为模块级——_is_rework_task 读侧可注入（测试用临时目录）
TASKS_DIR = Path(__file__).resolve().parent.parent.parent / "60_feedback" / "tasks"


def _is_rework_task(task_id: str) -> bool:
    """#580（F-064）：任务单 frontmatter `rework: true` → 终审 FAIL 打回的返工重提单。

    打标由 queue_transition.action_review 在 FAIL 打回/#538 改判时自动写入任务单——
    重提≠接新单，claim 不触发 #504 own-pending 阻塞。TASKS_DIR 模块级，测试可替换。
    """
    import re as _re
    fp = TASKS_DIR / f"{task_id}.md"
    try:
        text = fp.read_text(encoding="utf-8", errors="ignore")
    except OSError:
        return False
    return bool(_re.search(r"^rework:\s*(true|True|1)\s*$", text, _re.M))


def find_blockers(rows: list[dict] | None = None) -> tuple[list[dict], list[dict]]:
    """Return (pending_review_tasks, claimed_tasks) that block queue advance.

    #492：batch:true 任务的 pending_review 不阻塞前方（长程分批任务豁免）。
    """
    if rows is None:
        rows = parse_queue()
    pending = []
    claimed = []
    for row in rows:
        status = row["status"]
        if status == "pending_review":
            if not _is_batch_task(row["task_id"]):  # #492：批次提审豁免
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

    if task["status"] == "cancelled":
        return False, f"任务 {task_id} 已取消（cancelled，#461）——重新做=新单，不可领取"

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
        # #504 洞B/C：pending_review 占执行者位——执行者有自己的待终审任务（不论队列前后，
        # 角色维度与 #503 锁匹配一致）→ 审查等待期不接新单，提示等待欧阳锋终审
        # （08-24 实证：37 分钟提审 4 单不等审查，#498 FAIL = 质量无人把关代价）。
        # batch:true 任务的 pending_review 豁免（#492/F-050，find_blockers 已过滤）。
        cur_role = (task.get("assignee") or "").strip()
        own = [r for r in earlier_pending
               if cur_role and r.get("assignee", "").strip() == cur_role]
        if own and _is_rework_task(task_id):
            # #580（F-064）：rework:true 单 = 终审 FAIL 打回后的返工重提，重提≠接新单——
            # own pending 不阻塞（08-30 实证：#578 返工 claim 被 #504 误拦只能 --force；
            # 注意 #575 在 #578 队列位之前，仅跳过 own 分支会跌入下方 FIFO 分支照样被拦，
            # 故须把 own 从阻塞集剔除）。他人前方 pending 仍按 FIFO 阻塞、#503 claimed 锁照旧。
            own_ids = {o["task_id"] for o in own}
            earlier_pending = [r for r in earlier_pending
                               if r["task_id"] not in own_ids]
            own = []
        if own:
            own_ids = ", ".join(f"#{r['seq']} {r['task_id']}" for r in own)
            return False, (f"你（{cur_role}）还有 pending_review 任务待欧阳锋终审：{own_ids}。"
                           f"审查等待期不接新单（#504）——等终审后再领取 {task_id}")
        if earlier_pending:
            ids = ", ".join(f"#{r['seq']} {r['task_id']}" for r in earlier_pending)
            return False, f"队列前方还有 pending_review 任务未终审：{ids}。必须等它们 reviewed 后才能领取 {task_id}"

    # claimed 阻塞规则（#503 洞A 根治）：同一执行者同一时刻最多一个 in_progress。
    # 旧实现 `instance in r.get("assignee")` 子串匹配在 #444 写侧改角色名后静默失效
    # （"hermes" in "laowantong" = False → 老顽童 in_progress 从不阻塞自己，可无限并行）。
    # 修复后按两个维度判定"同一执行者"：
    #   ① status 前缀 claimed-<instance> 与当前 instance 相同（同实例）；
    #   ② claimed 行 assignee（#444 起为角色名）与本次领取任务的 assignee 相同
    #      （同角色——覆盖老顽童 hermes/kimi 多实例并行；kimi 多角色共用场景按任务
    #      归属角色判定，领取谁的单就以谁的角色身份入锁）。
    def _same_executor(r: dict) -> bool:
        if r["task_id"] == task_id:
            return False
        if r["status"] == f"claimed-{instance}":
            return True
        cur_role = (task.get("assignee") or "").strip()
        if cur_role and r.get("assignee", "").strip() == cur_role:
            return True
        return False

    if instance:
        same_instance_claimed = [r for r in claimed if _same_executor(r)]
    else:
        same_instance_claimed = [r for r in claimed if r["task_id"] != task_id]

    if same_instance_claimed:
        ids = ", ".join(f"#{r['seq']} {r['task_id']}" for r in same_instance_claimed)
        return False, f"你（实例 {instance} / 同角色）还有 claimed 任务未释放：{ids}。必须等它们释放后才能领取 {task_id}"

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


# F-036 问题落点判定（#主动立项 2026-08-24 方案 C）：审查发现问题必须给出去向。
# 放 queue_gate=共享真相源（queue_transition 门禁 + conveyor_probe 第七信号共用，禁副本）
ISSUE_DISPOSITION_HINTS = ("建议书", "停车场", "F-", "立项", "另立项", "friction", "待王语嫣", "待老朱", "TODO")

# #612 任务1：否定语境豁免——「不落 🟠」「不构成 🟡 级问题」「无 🟠/🟡」类
# 否定声明句的 emoji 字样不计入问题条目（emoji 字面出现≠标记问题）。
# 实证：#608 终审意见书含「不落 🟠/🟡」被连拦两轮，删字样才放行（F-036 误伤）。
# 判定口径：否定前挂词紧邻 emoji（允许空白间隔，连写的 🟠/🟡 对共享同一否定）→ 剔除。
_NEGATION_EMOJI_RE = re.compile(
    r"(?:不落|不构成|不算|不标|不判|不记|不涉及|没有|无|非)\s*[🟠🟡](?:\s*/\s*[🟠🟡])*")


def check_issue_disposition(opinion_text: str) -> tuple[bool, str]:
    """F-036：终审意见书"发现问题"节含 🟠/🟡 条目时必须注明落点。

    判定：含 🟠 或 🟡（非仅 🔵 无实质缺陷）且不含落点词 → 拦截。
    豁免：否定前挂词（不落/不构成/无……）紧邻的 emoji 字样不计入（#612）。
    """
    stripped = _NEGATION_EMOJI_RE.sub("", opinion_text)
    if "🟠" not in stripped and "🟡" not in stripped:
        return True, ""
    if any(h in opinion_text for h in ISSUE_DISPOSITION_HINTS):
        return True, ""
    lines = [l.strip() for l in stripped.splitlines() if "🟠" in l or "🟡" in l]
    sample = "；".join(l[:60] for l in lines[:3])
    return False, (f"审查发现问题未给落点（F-036）：{sample}——"
                   "必须在意见书注明去向（建议书路径 / 停车场 F-xxx / 任务单立项），否则终审不闭环"
                   "；若该 emoji 出现在否定声明句，请删去字样或写成「不落/不构成/无 + emoji」前挂否定形式")
