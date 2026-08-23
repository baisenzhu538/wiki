#!/usr/bin/env python3
"""queue-archive.py — 队列归档瘦身（#453，老朱 08-23 指令：看板定期瘦身防 token 膨胀+注意力稀释）。

归档对象：主表 `reviewed` 且任务单 updated_at 超保留期（默认 14 天）的行 → 按月归档文件（追加式，不删内容）。
永不归档：queued / claimed / pending_review / blocked。
REVIEW-PENDING 段已划掉终审行：保留最近 N 天（默认 30），更早同步归档（审查链完整可溯）。
归档前后 status 对账（活跃数 = 归档前 - 归档行数，E021 全量对账）；归档 = git commit 一次（#390 同款原子化）。

真实归档由王语嫣定期执行（每周一会话收尾）；本脚本支持 --dry-run 演练。

用法：
  python kdo-tools/queue-archive.py --dry-run        # 演练：只打印将归档的行，不写文件
  python kdo-tools/queue-archive.py                  # 真实归档（王语嫣执行）
  python kdo-tools/queue-archive.py --days 30        # 自定义保留期
  python kdo-tools/queue-archive.py --max-active 150 # 活跃行超阈值时提示提前触发
"""

import argparse
import re
import subprocess
import sys
from datetime import datetime, timedelta
from pathlib import Path

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")

WIKI = Path(__file__).resolve().parent.parent
QUEUE_FILE = WIKI / "70_product" / "tasks" / "production-queue.md"
TASK_DIR = WIKI / "60_feedback" / "tasks"
ARCHIVE_DIR = WIKI / "70_product" / "tasks" / "archive"

sys.path.insert(0, str(WIKI / "90_control" / "scripts"))
from queue_gate import parse_queue  # noqa: E402

REVIEW_BEGIN = "<!-- REVIEW-PENDING-BEGIN（queue_transition 自动维护，勿手改） -->"
REVIEW_END = "<!-- REVIEW-PENDING-END -->"
NEVER_ARCHIVE = ("queued", "claimed", "pending_review", "blocked")
DATE_RE = re.compile(r"(20\d{2})[-/年](\d{1,2})[-/月](\d{1,2})")


def _task_updated_at(task_id: str) -> str | None:
    """读任务单 frontmatter updated_at（取前 10 位日期）。任务单缺失 → None（保守不归档）。"""
    fp = TASK_DIR / f"{task_id}.md"
    if not fp.exists():
        return None
    try:
        text = fp.read_text(encoding="utf-8", errors="ignore")
        m = re.search(r"^updated_at:\s*['\"]?([\d-]+)", text, re.M)
        return m.group(1)[:10] if m else None
    except OSError:
        return None


def _older_than(date_str: str, days: int, today: datetime) -> bool:
    try:
        d = datetime.strptime(date_str[:10], "%Y-%m-%d")
        return (today - d).days > days
    except ValueError:
        return False  # 日期解析失败 → 保守不归档


def _review_strike_date(line: str) -> str | None:
    """REVIEW-PENDING 划掉行里找终审日期（"→ 已终审 PASS A-（2026-08-23 欧阳锋）"）。"""
    m = DATE_RE.search(line)
    return f"{m.group(1)}-{int(m.group(2)):02d}-{int(m.group(3)):02d}" if m else None


def collect_archive_candidates(lines: list[str], days: int, today: datetime) -> tuple[list[str], list[str]]:
    """返回 (主表归档行, REVIEW-PENDING 归档行)。纯状态+时间判断，无内容判断（只拦机械项）。"""
    rows = parse_queue(QUEUE_FILE)
    row_map = {r["task_id"]: r["raw"] for r in rows}
    to_archive: list[str] = []
    for task_id, raw in row_map.items():
        r = next((x for x in rows if x["task_id"] == task_id), None)
        if r is None or r["status"] != "reviewed":
            continue
        upd = _task_updated_at(task_id)
        if upd is None:
            continue  # 任务单缺失/日期不可读 → 保守不归档
        if _older_than(upd, days, today):
            to_archive.append(raw)

    # REVIEW-PENDING 划掉行：保留最近 review_days 天
    text = QUEUE_FILE.read_text(encoding="utf-8")
    review_lines: list[str] = []
    if REVIEW_BEGIN in text and REVIEW_END in text:
        block = text.split(REVIEW_BEGIN)[1].split(REVIEW_END)[0]
        for ln in block.splitlines():
            if ln.startswith("- ~~"):
                d = _review_strike_date(ln)
                if d is None:
                    continue  # 无日期 → 保守保留
                if _older_than(d, days, today):
                    review_lines.append(ln)
    return to_archive, review_lines


def run(dry_run: bool, days: int, review_days: int, max_active: int) -> int:
    today = datetime.now()
    rows = parse_queue(QUEUE_FILE)
    active_before = len(rows)
    print(f"归档前主表活跃行: {active_before}（{today:%Y-%m-%d}）")

    main_rows, review_rows = collect_archive_candidates(
        QUEUE_FILE.read_text(encoding="utf-8").splitlines(), days, today)
    print(f"候选归档：主表 {len(main_rows)} 行（reviewed 超 {days} 天）+ REVIEW-PENDING 划掉行 {len(review_rows)} 行（超 {review_days} 天）")

    if not main_rows and not review_rows:
        print("无归档候选（PASS）")
        return 0
    if dry_run:
        print("\n[dry-run] 将归档主表行（前 5 行预览）:")
        for ln in main_rows[:5]:
            print(f"  {ln[:90]}")
        print(f"[dry-run] 将归档 REVIEW-PENDING 行 {len(review_rows)} 行（前 3 行预览）:")
        for ln in review_rows[:3]:
            print(f"  {ln[:90]}")
        print("\n[dry-run] 不写文件——演练结束")
        return 0

    # 归档文件（按月追加式）
    month = today.strftime("%Y-%m")
    ARCHIVE_DIR.mkdir(parents=True, exist_ok=True)
    af = ARCHIVE_DIR / f"production-queue-{month}.md"
    new_block = [f"<!-- 归档 {today:%Y-%m-%d}（#453 queue-archive.py）-->", ""] + main_rows + review_rows + ["", ""]
    with open(af, "a", encoding="utf-8") as f:
        f.write("\n".join(new_block))
    print(f"✅ 归档写入: {af}（+{len(main_rows) + len(review_rows)} 行）")

    # 主表移除（逐行过滤）+ REVIEW-PENDING 段移除
    text = QUEUE_FILE.read_text(encoding="utf-8")
    keep = [ln for ln in text.splitlines() if ln not in set(main_rows)]
    if REVIEW_BEGIN in text and REVIEW_END in text:
        block = text.split(REVIEW_BEGIN)[1].split(REVIEW_END)[0]
        keep_lines = [ln for ln in block.splitlines() if ln not in set(review_rows)]
        keep = keep[: keep.index(REVIEW_BEGIN) + 1] + keep_lines + keep[keep.index(REVIEW_END):]
    QUEUE_FILE.write_text("\n".join(keep) + "\n", encoding="utf-8")

    # 对账（E021）：活跃数 = 归档前 - 归档行数
    after = len(parse_queue(QUEUE_FILE))
    expected = active_before - len(main_rows)
    ok = after == expected
    print(f"对账: 归档后活跃 {after}（期望 {expected}）→ {'✅ 一致' if ok else '❌ 不一致，人工介入'}")

    # git commit（#390 原子化，path-scoped）
    try:
        subprocess.run(["git", "-C", str(WIKI), "add", "--", str(QUEUE_FILE), str(af)],
                       check=True, capture_output=True, timeout=15)
        subprocess.run(["git", "-C", str(WIKI), "commit", "-m",
                        f"chore(queue): #453 队列归档瘦身（{today:%Y-%m-%d}，主表 -{len(main_rows)} 行）",
                        "--", str(QUEUE_FILE), str(af)],
                       check=True, capture_output=True, timeout=15)
        print("✅ git 已收口（队列+归档文件原子化）")
    except subprocess.CalledProcessError as e:
        print(f"⚠️ git 收口失败（不阻断归档）: {e.stderr[:120] if e.stderr else e}")

    if active_before > max_active:
        print(f"⚠️ 主表仍超 {max_active} 活跃行（现 {after}）——建议提前下次归档")
    return 0 if ok else 1


def main() -> int:
    p = argparse.ArgumentParser(description="KDO 队列归档瘦身（#453）")
    p.add_argument("--dry-run", action="store_true", help="演练：只打印将归档的行")
    p.add_argument("--days", type=int, default=14, help="reviewed 保留期（默认 14 天）")
    p.add_argument("--review-days", type=int, default=30, help="REVIEW-PENDING 划掉行保留期（默认 30 天）")
    p.add_argument("--max-active", type=int, default=150, help="活跃行阈值（超则提示提前归档）")
    args = p.parse_args()
    return run(args.dry_run, args.days, args.review_days, args.max_active)


if __name__ == "__main__":
    sys.exit(main())
