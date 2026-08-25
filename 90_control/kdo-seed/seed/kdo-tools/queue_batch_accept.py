#!/usr/bin/env python3
"""queue_batch_accept.py — 批次验收四步一体（#479，#426 批次线静默失败根治）。

背景：#426 第二批验收漏恢复队列行——text.replace 静默失败（打印"✅"实际未改）。
本工具核心价值=禁静默：每步 re.subn 计数=1 断言，失败即报错退出；前后 parse_queue
对账（E021 全量对账）；原子 git commit（#390 同款 path-scoped）。

四步一体（accept <task-id> --grade <等级>）：
  1. 任务单批次验收记录节检查（欧阳锋意见书落点）
  2. REVIEW-PENDING 提审行划线（保留原文+追加注记）
  3. 队列行恢复 queued
  4. 任务单 frontmatter status 同步 queued（#426 漏掉的第 4 步）
漏步不可能——四步一体。

用法：
  python kdo-tools/queue_batch_accept.py accept <task-id> --grade A- [--dry-run]
"""

from __future__ import annotations

import argparse
import re
import subprocess
import sys
from datetime import datetime
from pathlib import Path

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")

WIKI = Path(__file__).resolve().parent.parent
QUEUE_FILE = WIKI / "70_product" / "tasks" / "production-queue.md"
TASK_DIR = WIKI / "60_feedback" / "tasks"

sys.path.insert(0, str(WIKI / "90_control" / "scripts"))
from queue_gate import parse_queue  # noqa: E402

ACCEPT_SECTION = "## 批次验收记录"  # 欧阳锋意见书落点节


def _subn_assert(text: str, pattern: str, repl: str, step: str) -> str:
    """re.subn 计数=1 断言（禁静默——本工具核心价值）。返回替换后文本。"""
    new_text, n = re.subn(pattern, repl, text, count=1)
    if n != 1:
        raise RuntimeError(f"[{step}] 替换计数={n} ≠ 1（预期唯一命中）——中止，不落盘")
    return new_text


def _set_task_status(task_id: str, new_status: str) -> str:
    fp = TASK_DIR / f"{task_id}.md"
    text = fp.read_text(encoding="utf-8", errors="ignore")
    return _subn_assert(text, r"(?m)^(status:\s*)\S+", rf"\g<1>{new_status}", "frontmatter status")


def _commit_add_paths(task_id: str) -> list[str]:
    """#482：add 路径必须相对 WIKI 根（basename 会 pathspec 不匹配——
    production-queue.md 实际在 70_product/tasks/ 子目录；且不依赖调用方 cwd）。"""
    return [str(QUEUE_FILE.relative_to(WIKI)), f"60_feedback/tasks/{task_id}.md"]


def _git_commit(task_id: str, grade: str) -> None:
    """#390 同款原子 commit：path-scoped add（严禁 add -A）。git 失败不阻断，报警+留痕。"""
    try:
        subprocess.run(["git", "-C", str(WIKI), "add", *_commit_add_paths(task_id)],
                       check=True, capture_output=True)
        subprocess.run(["git", "-C", str(WIKI), "commit", "-m",
                        f"chore(queue): 批次验收 {task_id}（grade {grade}）— queue_batch_accept #479"],
                       check=True, capture_output=True)
        print("✅ 原子 commit 完成")
    except subprocess.CalledProcessError as e:
        print(f"🚨 git 提交失败（流转已成功，待收口）: {e.stderr.decode(errors='ignore')[:200]}",
              file=sys.stderr)
        log = WIKI / "90_control" / "pending-git-commits.log"
        log.parent.mkdir(parents=True, exist_ok=True)
        with log.open("a", encoding="utf-8") as f:
            f.write(f"\n# {datetime.now().strftime('%Y-%m-%d %H:%M')} 批次验收 git 失败 {task_id} grade={grade}\n")


def action_accept(task_id: str, grade: str, dry_run: bool = False) -> int:
    rows_before = parse_queue(QUEUE_FILE)  # 显式传参（queue_gate 默认参数绑定 import 时路径）
    row = next((r for r in rows_before if r["task_id"] == task_id), None)
    if row is None:
        print(f"⛔ 任务 {task_id} 不在队列", file=sys.stderr)
        return 1
    if row["status"] != "pending_review":
        print(f"⛔ 任务 {task_id} 状态为 {row['status']}，批次验收只对 pending_review", file=sys.stderr)
        return 1
    fp = TASK_DIR / f"{task_id}.md"
    if not fp.exists():
        print(f"⛔ 任务单文件不存在: {task_id}", file=sys.stderr)
        return 1
    task_text = fp.read_text(encoding="utf-8", errors="ignore")

    # 步 1：批次验收记录节检查（意见书已写——欧阳锋落点）
    if ACCEPT_SECTION not in task_text:
        print(f"⛔ 任务单缺「{ACCEPT_SECTION}」节（欧阳锋意见书落点）——先写验收记录再 accept", file=sys.stderr)
        return 1

    seq = row["seq"]
    now = datetime.now().strftime("%Y-%m-%d")
    esc_id = re.escape(task_id)

    if dry_run:
        print(f"[dry-run] 将对 {task_id}（#{seq}, grade {grade}）执行四步："
              f"验收节检查✅ → REVIEW-PENDING 划线 → 队列行恢复 queued → frontmatter 同步 queued")
        return 0

    queue_text = QUEUE_FILE.read_text(encoding="utf-8")

    # 步 2：REVIEW-PENDING 提审行划线（保留原文，追加批次验收注记；注记用原始 task_id 非转义）
    queue_text = _subn_assert(
        queue_text,
        rf"(?m)^(- )#{seq} {esc_id}(｜.*)$",
        rf"\1~~#{seq} {task_id}\2~~ → 批次验收（{grade}）（{now}）",
        "REVIEW-PENDING 划线")

    # 步 3：队列行恢复 queued（状态列精确替换，防误改他行）
    queue_text = _subn_assert(
        queue_text,
        rf"(?m)^(\| {seq} \| `{esc_id}` \|.*\| )pending_review( \|)",
        rf"\1queued\2",
        "队列行恢复 queued")

    # 步 4：frontmatter status 同步 queued（#426 漏掉的第 4 步）
    task_text = _set_task_status(task_id, "queued")

    if not dry_run:
        QUEUE_FILE.write_text(queue_text, encoding="utf-8")
        fp.write_text(task_text, encoding="utf-8")

    # 前后对账（E021 全量对账）：除目标行外全部一致 + 目标行 queued
    rows_after = parse_queue(QUEUE_FILE)
    diff = [r for r in rows_before if r["task_id"] != task_id]
    diff_after = {r["task_id"]: r["status"] for r in rows_after if r["task_id"] != task_id}
    mismatches = [r["task_id"] for r in diff if diff_after.get(r["task_id"]) != r["status"]]
    target = next((r for r in rows_after if r["task_id"] == task_id), None)
    if mismatches or target is None or target["status"] != "queued":
        print(f"⛔ 对账失败: 他行不一致={mismatches} 目标行={target and target['status']}——需人工核查",
              file=sys.stderr)
        return 1

    print(f"✅ 批次验收四步一体完成: #{seq} {task_id}（grade {grade}）→ queued，对账 PASS")
    _git_commit(task_id, grade)
    return 0


def main() -> int:
    ap = argparse.ArgumentParser(description="批次验收四步一体（#479，禁静默）")
    ap.add_argument("accept", nargs="?", help="accept 动作")
    ap.add_argument("task_id", nargs="?", help="任务 id（task_xxx）")
    ap.add_argument("--grade", required=False)
    ap.add_argument("--dry-run", action="store_true")
    args = ap.parse_args()

    if args.accept != "accept" or not args.task_id or not args.grade:
        print(__doc__, file=sys.stderr)
        return 1
    return action_accept(args.task_id, args.grade, args.dry_run)


if __name__ == "__main__":
    sys.exit(main())
