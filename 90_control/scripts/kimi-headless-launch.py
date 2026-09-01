#!/usr/bin/env python3
"""角色无头拉起器（09-02 老朱直令：新工作流——王语嫣时钟唯一，拉起其他角色干活）。

工具无关设计（09-02 老朱追加口径）：拉起工具=可替换变量（kimi/codex/其他 CLI），
角色=资产。新增工具时在 TOOLS 表登记一行即可，拉起流程不变。
王语嫣=唯一时钟+探针出口+对老朱沟通通道。

用法:
  python 90_control/scripts/kimi-headless-launch.py <role> "<本次任务指令>" [--tool kimi]

机制：
  <tool> 无头单发 "<自包含 prompt>"（cwd=wiki，DETACHED 后台，日志 logs/headless-<role>-<ts>.log）
  prompt = 角色恢复（读 .agent/<role>-context.md）+ 队列纪律 + 本次任务指令 + 收尾留痕

纪律（写死进 prompt，每次拉起自带）：
  - 状态流转只走 90_control/scripts/queue_transition.py（claim/complete/review）
  - 完工在 90_control/todos/<role>.md 追加一行（时间戳+动作+任务号）
  - 执行报告五字段（交付物/完成内容/验证/边界/需要谁动作）
"""
import subprocess
import sys
import time
from pathlib import Path

WIKI = Path(r"C:\Users\Administrator\Desktop\wiki")

# 工具路由表：工具名 → 无头单发命令模板（{prompt} 为占位符）。
# 新工具上线前先实测其无头模式（-p/print/exec 形态+权限模式），再登记。
TOOLS = {
    "kimi": [r"C:\Users\Administrator\.kimi-code\bin\kimi.exe", "-p", "{prompt}"],
    # "codex": [...],  # 待接入时登记
}

PROMPT_TEMPLATE = """你是{role}（KDO 知识工厂角色）。工作目录 {wiki}（先 cd 进去，一切操作在该目录下）。

启动恢复（必做）：
1. Read .agent/startup.md
2. Read .agent/{role}-context.md（若不存在跳过，改读 20_memory/{role}-amnesia-recovery.md）
3. Read 90_control/todos/{role}.md 的最后 20 行（未读段）

然后执行本次任务指令：
{instruction}

通用纪律（不可协商）：
- 队列状态流转只走 python 90_control/scripts/queue_transition.py（claim <task_id> --instance {role}-kimi / complete ... --evidence ... / review ...），禁止手改队列和任务单 status。
- 完工在 90_control/todos/{role}.md 追加一行（[YYYY-MM-DD HH:MM] 动作+任务号+结果）。
- 提审前任务单内必须有五字段执行报告（**交付物**/**完成内容**/**验证**/**边界**/**需要谁动作** 各起一行）。
- 只做本次指令范围内的事，做完收工，不扩展到其他任务。
"""


def main() -> int:
    args = [a for a in sys.argv[1:] if not a.startswith("--tool")]
    tool = "kimi"
    if "--tool" in sys.argv:
        tool = sys.argv[sys.argv.index("--tool") + 1]
    if len(args) < 2:
        print(__doc__)
        return 1
    role, instruction = args[0], args[1]
    if tool not in TOOLS:
        print(f"未知工具 {tool}（已登记：{list(TOOLS)}）——先实测无头模式再登记 TOOLS 表")
        return 1
    prompt = PROMPT_TEMPLATE.format(role=role, wiki=str(WIKI), instruction=instruction)
    cmd = [part.replace("{prompt}", prompt) for part in TOOLS[tool]]

    ts = time.strftime("%Y%m%d-%H%M%S")
    log_path = WIKI / "logs" / f"headless-{role}-{ts}.log"
    log = open(log_path, "ab")

    DETACHED = 0x00000008 | 0x00000200  # DETACHED_PROCESS | CREATE_NEW_PROCESS_GROUP
    p = subprocess.Popen(
        cmd,
        cwd=str(WIKI),
        stdout=log,
        stderr=log,
        creationflags=DETACHED,
    )
    print(f"proc_{role}_{p.pid} | tool={tool} | log={log_path} | {time.strftime('%H:%M:%S')}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
