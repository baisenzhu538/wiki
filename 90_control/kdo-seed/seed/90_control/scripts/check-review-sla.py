#!/usr/bin/env python3
"""check-review-sla.py — 审查供给 SLA 观测（#520 R3）。

解析 production-queue.md REVIEW-PENDING 段活跃行（未划掉），
计算 pending_review 最大年龄；超阈值（2h）→ exit 1 入健康检查报告。
卡点从「被发现」变「被预测」（#505 实证：审查供给触发器曾=老朱发现）。

用法：python 90_control/scripts/check-review-sla.py
"""
import re
import sys
from datetime import datetime
from pathlib import Path

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")

VAULT_ROOT = Path(__file__).resolve().parent.parent.parent
QUEUE_FILE = VAULT_ROOT / "70_product" / "tasks" / "production-queue.md"
REVIEW_BEGIN = "<!-- REVIEW-PENDING-BEGIN"
REVIEW_END = "<!-- REVIEW-PENDING-END -->"
SLA_HOURS = 2  # pending_review 最大年龄阈值（#520 R3）

# 活跃行：- #505 task_...｜huangyaoshi｜提审 08-25 00:51｜path（划掉行 - ~~...~~ 跳过）
_ROW_RE = re.compile(r"^- #(\d+) (\S+)｜(\S+)｜提审 (\d{2}-\d{2}) (\d{2}:\d{2})｜")


def main() -> int:
    if not QUEUE_FILE.exists():
        print(f"FAIL: 队列文件不存在: {QUEUE_FILE}")
        return 1
    text = QUEUE_FILE.read_text(encoding="utf-8")
    if REVIEW_BEGIN not in text or REVIEW_END not in text:
        print("FAIL: REVIEW-PENDING 段标记缺失")
        return 1
    block = text.split(REVIEW_BEGIN)[1].split(REVIEW_END)[0]

    now = datetime.now()
    oldest: tuple[str, float] | None = None
    active = 0
    for line in block.splitlines():
        if line.startswith("- ~~"):
            continue
        m = _ROW_RE.match(line)
        if not m:
            continue
        active += 1
        seq, tid, assignee, md, hm = m.groups()
        # 提审时间无年份——按今年解析，未来值（跨年边界）回退一年
        submitted = datetime.strptime(f"{now.year}-{md} {hm}", "%Y-%m-%d %H:%M")
        if submitted > now:
            submitted = submitted.replace(year=now.year - 1)
        age_h = (now - submitted).total_seconds() / 3600
        if oldest is None or age_h > oldest[1]:
            oldest = (f"#{seq} {tid}（{assignee}，提审 {md} {hm}）", age_h)

    if active == 0:
        print("review SLA 正常：REVIEW-PENDING 段零积压")
        return 0
    assert oldest is not None
    if oldest[1] > SLA_HOURS:
        print(f"FAIL: 审查 SLA 破线——{active} 单待终审，最大年龄 {oldest[1]:.1f}h > {SLA_HOURS}h：{oldest[0]}")
        return 1
    print(f"review SLA 正常：{active} 单待终审，最大年龄 {oldest[1]:.1f}h（阈值 {SLA_HOURS}h）：{oldest[0]}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
