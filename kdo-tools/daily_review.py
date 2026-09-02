#!/usr/bin/env python3
"""#623 每日复盘计划任务化：四主力（老顽童/黄药师/欧阳锋）每日 Truman 复盘自动拉起。

老朱 09-02 直令：复盘从「会话收尾靠自觉」升级为「定期任务」。王语嫣自有收尾纪律不占此任务。

机制：
  1. 每角色先查「空班豁免」（F-062 成本纪律）：今日零 commit 零 todos 新增 → 跳过不拉起
  2. 非空班 → 经 kimi-headless-launch.py 依次拉起 headless 实例执行复盘指令
     （复盘输入全部来自仓库文件——headless 无会话记忆）
  3. 复盘指令模板见 REVIEW_INSTRUCTION（不从零发挥；禁编造，无产出如实写）

调度：schtasks kdo-daily-review（每日 23:37，S4U 无窗）→ kdo-tools/kdo-daily-review.cmd 包装。
登记：infrastructure-inventory.md（§5 计划任务 + 资产行）。
用法：python kdo-tools/daily_review.py
"""
import datetime
import subprocess
import sys
import time
from pathlib import Path

WIKI = Path(__file__).resolve().parents[1]
RETRO_BASE = WIKI.parent / "agent复盘"          # 桌面/agent复盘（与 daily-context-save 同源）
LOG_PATH = WIKI / "logs" / "daily-review.log"

# 三角色：王语嫣不占（自有收尾纪律）。中文名用于 git log 消息匹配（review by 欧阳锋 等）
ROLES = [
    ("laowantong", "老顽童"),
    ("huangyaoshi", "黄药师"),
    ("ouyangfeng", "欧阳锋"),
]

# 复盘指令模板（#623 任务 2：写进任务脚本，不从零发挥）
def review_instruction(role: str, cn: str, today: str) -> str:
    retro = RETRO_BASE / role / "daily-context" / f"{today}.md"
    todos = f"90_control/todos/{role}.md"
    return (
        f"执行今日（{today}）Truman 复盘，输入全部来自仓库文件（headless 无会话记忆）：\n"
        f"1. 搜集今日素材：Read {todos} 中日期={today} 的条目；跑 git -C {WIKI} log --since='{today} 00:00:00' "
        f"--pretty=%s 找含「{cn}」或「{role}」的 commit；按 commit 定位今日任务单 Read 其执行报告/终审记录。\n"
        f"2. 复盘文件 {retro}：已存在（同角色多实例/多场次）→ Read 全文后在文末追加新节 "
        f"「# {cn} daily-context {today}（{time.strftime('%H:%M')} 场）」；不存在 → 新建。\n"
        f"3. 严格按 agents/agent-os.md §10.2 Truman 11 章写（差异栏空白=C 级）。双三角要素逐轮映射照实写。"
        f"无实质产出→如实写「今日无施工」诚实空班节（禁编造，红线）。\n"
        f"4. 新错误/新坑 → 追加 {RETRO_BASE / role / '错误模式库.md'}（该角色有此文件时）。\n"
        f"5. 保存自检（禁 --stdin，F-030）：python kdo-tools/daily-context-save.py save --agent {role} "
        f"--truman --file {retro}——输出必须 🟢/🟡（🔴=重写再存）。\n"
        f"6. 收尾在 {todos} 追加一行「[{today} HH:MM] 复盘完成+自检等级」。\n"
        f"只做复盘范围内的事，不扩展其他任务。"
    )


def has_activity(role: str, cn: str, today: str) -> tuple[bool, str]:
    """空班豁免判据（#623 任务 3）：今日零 commit 零 todos 新增 = 跳过。"""
    todos_fp = WIKI / "90_control" / "todos" / f"{role}.md"
    todos_hits = 0
    if todos_fp.exists():
        for line in todos_fp.read_text(encoding="utf-8", errors="ignore").splitlines():
            if line.startswith(f"[{today}"):
                todos_hits += 1
    if todos_hits:
        return True, f"todos 今日 {todos_hits} 条"
    try:
        out = subprocess.run(
            ["git", "-C", str(WIKI), "log", "--since", f"{today} 00:00:00", "--pretty=%s"],
            capture_output=True, text=True, encoding="utf-8", errors="replace",
            timeout=30,
        ).stdout
    except Exception as e:
        return True, f"git 查询异常按有活动放行（{e}）"
    hits = [ln for ln in out.splitlines() if cn in ln or role in ln]
    if hits:
        return True, f"今日 commit {len(hits)} 条"
    return False, "零 commit 零 todos（空班豁免，F-062）"


def main() -> int:
    today = datetime.date.today().isoformat()
    log_lines = [f"=== kdo-daily-review {today} {time.strftime('%H:%M:%S')} ==="]
    launched = 0
    for role, cn in ROLES:
        active, why = has_activity(role, cn, today)
        if not active:
            line = f"[skip] {role}：{why}"
            print(line)
            log_lines.append(line)
            continue
        instruction = review_instruction(role, cn, today)
        rc = subprocess.run(
            [sys.executable, "90_control/scripts/kimi-headless-launch.py", role, instruction],
            cwd=str(WIKI), timeout=60,
        )
        line = f"[launch] {role}：{why}（rc={rc.returncode}）"
        print(line)
        log_lines.append(line)
        launched += 1
        time.sleep(1)  # headless 日志名按秒，错开防同名日志文件串写
    log_lines.append(f"--- 共拉起 {launched} 角色 ---")
    LOG_PATH.parent.mkdir(parents=True, exist_ok=True)
    with LOG_PATH.open("a", encoding="utf-8") as f:
        f.write("\n".join(log_lines) + "\n")
    return 0


if __name__ == "__main__":
    sys.exit(main())
