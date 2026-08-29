#!/usr/bin/env python3
"""check-review-sla.py — 审查供给 SLA 观测 + 超时必推（#520 R3 → #574 R1 升级）。

解析 production-queue.md REVIEW-PENDING 段活跃行（未划销），
计算 pending_review 最大年龄；分级推送（#574 R1）：
  30min 提醒 → 推审查者（ouyangfeng）webhook + todos 落盘；
  2h 升级   → 推审查者 + 王语嫣群（老朱在群可达，@ 负责人/老板）。

复用 conveyor_probe._send_hook/_load_hooks/_append_role_todo 加签（零新基建）。
消息含「#xxx 待终审 + 挂审时长 + 任务单路径」。

用法：
  python 90_control/scripts/check-review-sla.py            # 常规（超时推送）
  python 90_control/scripts/check-review-sla.py --dry-run  # 只打印不发送（测试）
"""
import re
import sys
from datetime import datetime
from pathlib import Path

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")
# #568：通知类打印改走 stderr（GBK 控制台下 stdout 污染）
if hasattr(sys.stderr, "reconfigure"):
    sys.stderr.reconfigure(encoding="utf-8", errors="replace")

VAULT_ROOT = Path(__file__).resolve().parent.parent.parent
QUEUE_FILE = VAULT_ROOT / "70_product" / "tasks" / "production-queue.md"
REVIEW_BEGIN = "<!-- REVIEW-PENDING-BEGIN"
REVIEW_END = "<!-- REVIEW-PENDING-END -->"

# #574 R1 分级阈值
REMIND_MIN = 30        # 30min 提醒（软）
ESCALATE_HOURS = 2     # 2h 升级（硬，破线 exit 1）
REVIEWER = "ouyangfeng"                # 终审者（审查者固定=欧阳锋）
ESCALATE_ROLES = ["ouyangfeng", "wangyuyan"]  # 2h 升级推送面（王语嫣群可 @ 老朱）

# 复用 conveyor_probe 推送层（零新基建）
sys.path.insert(0, str(VAULT_ROOT / "kdo-tools"))
import conveyor_probe as _cp  # noqa: E402

# 活跃行：- #505 task_...｜huangyaoshi｜提审 08-25 00:51｜60_feedback/tasks/xxx.md（划销行 - ~~...~~ 跳过）
_ROW_RE = re.compile(r"^- #(\d+) (\S+)｜(\S+)｜提审 (\d{2}-\d{2}) (\d{2}:\d{2})｜(\S+)")


def _fmt_age(minutes: float) -> str:
    """挂审时长人性化：35min / 2.5h。"""
    if minutes < 60:
        return f"{minutes:.0f}min"
    return f"{minutes / 60:.1f}h"


def _push(role: str, text: str, dry_run: bool) -> bool:
    """复用 conveyor_probe webhook（加签）；dry-run 只打印。返回是否真正发送成功。"""
    if dry_run:
        print(f"🧪 dry-run 不发送：{role} → {text}", file=sys.stderr)
        return False
    hooks = _cp._load_hooks()
    hook = hooks.get(role)
    if not hook:
        print(f"⚠️ 无 webhook 配置（不发送）：{role}", file=sys.stderr)
        return False
    ok = _cp._send_hook(hook["url"], text, hook["key"])
    print(f"{'✅' if ok else '❌'} 通知 {role}：{text}", file=sys.stderr)
    return ok


def main() -> int:
    dry_run = "--dry-run" in sys.argv
    if not QUEUE_FILE.exists():
        print(f"FAIL: 队列文件不存在: {QUEUE_FILE}")
        return 1
    text = QUEUE_FILE.read_text(encoding="utf-8")
    if REVIEW_BEGIN not in text or REVIEW_END not in text:
        print("FAIL: REVIEW-PENDING 段标记缺失")
        return 1
    block = text.split(REVIEW_BEGIN)[1].split(REVIEW_END)[0]

    now = datetime.now()
    items = []  # (seq, tid, assignee, age_min, path)
    for line in block.splitlines():
        if line.startswith("- ~~"):
            continue
        m = _ROW_RE.match(line)
        if not m:
            continue
        seq, tid, assignee, md, hm, path = m.groups()
        submitted = datetime.strptime(f"{now.year}-{md} {hm}", "%Y-%m-%d %H:%M")
        if submitted > now:  # 跨年边界回退
            submitted = submitted.replace(year=now.year - 1)
        age_min = (now - submitted).total_seconds() / 60
        items.append((seq, tid, assignee, age_min, path))

    if not items:
        print("review SLA 正常：REVIEW-PENDING 段零积压")
        return 0

    worst = max(items, key=lambda i: i[3])
    seq, tid, assignee, age_min, path = worst

    # 2h 升级（硬破线）：@ 负责人/老板，推审查者 + 王语嫣群
    if age_min > ESCALATE_HOURS * 60:
        msg = (f"🚨 @负责人 @老朱 待终审升级：#{seq} {tid}（{assignee} 的单）"
               f"挂审 {_fmt_age(age_min)} 未终审，任务单 {path}")
        for role in ESCALATE_ROLES:
            _push(role, msg, dry_run)
        if not dry_run:
            _cp._append_role_todo(REVIEWER, f"🚨 待终审升级：#{seq} 挂审 {_fmt_age(age_min)} 未终审")
        print(f"FAIL: 审查 SLA 破线——{len(items)} 单待终审，最大年龄 {_fmt_age(age_min)} > {ESCALATE_HOURS}h：#{seq} {tid}")
        return 1

    # 30min 提醒（软）：推审查者
    if age_min > REMIND_MIN:
        msg = (f"🔔 待终审提醒：#{seq} {tid}（{assignee} 的单）"
               f"挂审 {_fmt_age(age_min)} 未终审，任务单 {path}")
        _push(REVIEWER, msg, dry_run)
        if not dry_run:
            _cp._append_role_todo(REVIEWER, f"🔔 待终审提醒：#{seq} 挂审 {_fmt_age(age_min)}")
        print(f"review SLA 提醒：{len(items)} 单待终审，最大年龄 {_fmt_age(age_min)} > {REMIND_MIN}min（已推送提醒）")
        return 0

    print(f"review SLA 正常：{len(items)} 单待终审，最大年龄 {_fmt_age(age_min)}（阈值 {REMIND_MIN}min）")
    return 0


if __name__ == "__main__":
    sys.exit(main())
