#!/usr/bin/env python3
"""kdo_session_boot_hook.py — #565：kimi-cli SessionStart 钩（门铃自检注入）。

挂法（~/.kimi-code/config.toml）：
    [[hooks]]
    event = "SessionStart"
    command = "python C:/Users/Administrator/Desktop/wiki/kdo-tools/kdo_session_boot_hook.py"

语义：每次会话启动/恢复，若 cwd=wiki 仓 → 往上下文注入门铃自检指令（stdout 进上下文）。
解决「会话级 cron 随会话死、新会话不知道要装门铃」的断点（08-26 时钟巡航 v2 随旧会话
死亡、新会话聋哑 5 小时实证）。注入=提醒模型执行 CronList/CronCreate——钩本身无权限
调会话工具，模型看到指令后自装。

与 .agent/startup.md 第 0 步互为双保险（一个靠读文件，一个靠事件注入）。
fail-open：任何异常静默 exit 0。
"""
import json
import sys
from pathlib import Path

WIKI_ROOT = Path(__file__).resolve().parent.parent

INSTRUCTION = (
    "【KDO 门铃自检 #565】本会话若为 KDO 角色会话：立即 CronList 查自己的临时门铃"
    "（15min 一拍：读 90_control/todos/<role>.md 未读段 + queue_transition.py myqueue <role>"
    "，有事施工无事待命）；没有就立即 CronCreate 重建。会话级 cron 随会话死——"
    "新会话必须自装，不等谁提醒。OS 级兜底=kdo-huangyaoshi-doorbell 计划任务（活着会被守卫跳过）。"
)


def main() -> int:
    try:
        payload = json.load(sys.stdin)
        cwd = (payload.get("cwd") or "").replace("\\", "/").rstrip("/")
        if cwd.lower() == str(WIKI_ROOT).replace("\\", "/").lower():
            print(INSTRUCTION)
    except Exception:
        pass
    return 0


if __name__ == "__main__":
    sys.exit(main())
