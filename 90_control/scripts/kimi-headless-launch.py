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

# 工具路由表：工具名 → 无头单发命令模板（{prompt}/{role} 为占位符）。
# 新工具上线前先实测其无头模式（-p/print/exec 形态+权限模式），再登记。
# 09-03 实测登记（王语嫣）：claude=deepseek-v4-flash（黄药师线）/ hermes=glm-5.3-flash（老顽童线，profile 走 HERMES_PROFILE env）/ codex=deepseek-v4-pro（欧阳锋线，需 relay 4444 活着）。
# 纪律：一律用原生 .exe——.cmd/.bat 壳在 DETACHED 无控制台环境下起不来（09-03 实测三次 0 字节日志）。
# 09-04 老朱令：黄药师线改 kimi K3（claude/DeepSeek 无订阅余额）——kimi 模板显式钉死 k3 别名防配置漂移
TOOLS = {
    "kimi": [r"C:\Users\Administrator\.kimi-code\bin\kimi.exe", "-m", "kimi-code/k3", "-p", "{prompt}"],
    "claude": [r"C:\Users\Administrator\AppData\Roaming\npm\node_modules\@anthropic-ai\claude-code\bin\claude.exe", "-p", "{prompt}", "--dangerously-skip-permissions"],
    "codex": [r"C:\Users\Administrator\AppData\Roaming\npm\node_modules\@openai\codex\node_modules\@openai\codex-win32-x64\vendor\x86_64-pc-windows-msvc\bin\codex.exe", "exec", "{prompt}", "--dangerously-bypass-approvals-and-sandbox", "--skip-git-repo-check"],
    "hermes": [r"C:\Users\Administrator\AppData\Local\hermes\hermes-agent\venv\Scripts\hermes.exe", "-z", "{prompt}", "--yolo"],
}

# 角色→默认工具路由（老朱 09-03 异构防线：不同模型防同构错误）。--tool 显式指定优先。
# 09-03 20:10 王语嫣调整：laowantong 暂回 kimi——hermes 通道两连死+一次锁挂（#626/#629 实例死亡、19:41 拉起即死 0 字节日志），待通道修复后恢复 hermes
ROLE_TOOL = {
    "huangyaoshi": "kimi",
    "laowantong": "kimi",
    "ouyangfeng": "codex",
}

# 工具级环境变量（{role} 占位符同样替换）——hermes 用 HERMES_PROFILE 选 profile。
TOOL_ENV = {
    "hermes": {"HERMES_PROFILE": "{role}"},
}

PROMPT_TEMPLATE = """你是{role}（KDO 知识工厂角色）。工作目录 {wiki}（先 cd 进去，一切操作在该目录下）。

启动恢复（必做）：
1. Read .agent/startup.md
2. Read .agent/{role}-context.md（若不存在跳过，改读 20_memory/{role}-amnesia-recovery.md）
3. Read 90_control/todos/{role}.md 的最后 20 行（未读段）

然后执行本次任务指令：
{instruction}

通用纪律（不可协商）：
- 队列状态流转只走 python 90_control/scripts/queue_transition.py（claim <task_id> --instance {role} / complete ... --evidence ... / review ...），禁止手改队列和任务单 status。实例名=裸角色名（#620 老朱 09-02 铁律：工具=变量不进名字）。
- 完工在 90_control/todos/{role}.md 追加一行（[YYYY-MM-DD HH:MM] 动作+任务号+结果）。
- 提审前任务单内必须有五字段执行报告（**交付物**/**完成内容**/**验证**/**边界**/**需要谁动作** 各起一行）。
- 只做本次指令范围内的事，做完收工，不扩展到其他任务。
- 备份避让（#628）：vault 自动备份每 30min 一拍（kdo-vault-git-backup，现落 :20/:50，以 logs/vault-git-backup.log 尾行为准）——拍前 5 分钟禁 stash/worktree 切换类操作，未提交在制品保持落盘可见即可（有活动会话备份会自行跳拍）；长任务隔离验证一律 git worktree。
"""


def main() -> int:
    args = [a for a in sys.argv[1:] if not a.startswith("--tool")]
    tool = None
    if "--tool" in sys.argv:
        tool = sys.argv[sys.argv.index("--tool") + 1]
    args = [a for a in args if a != tool]
    if len(args) < 2:
        print(__doc__)
        return 1
    role, instruction = args[0], args[1]
    if tool is None:
        tool = ROLE_TOOL.get(role, "kimi")  # 默认走角色路由，未登记角色回落 kimi
    if tool not in TOOLS:
        print(f"未知工具 {tool}（已登记：{list(TOOLS)}）——先实测无头模式再登记 TOOLS 表")
        return 1
    prompt = PROMPT_TEMPLATE.format(role=role, wiki=str(WIKI), instruction=instruction)
    cmd = [part.replace("{prompt}", prompt).replace("{role}", role) for part in TOOLS[tool]]
    # .cmd/.bat 壳在 DETACHED 下 CreateProcess 起不来（无控制台）——一律显式 cmd /c 包一层
    if cmd[0].lower().endswith((".cmd", ".bat")):
        cmd = ["cmd.exe", "/c"] + cmd

    import os
    env = dict(os.environ)
    for k, v in TOOL_ENV.get(tool, {}).items():
        env[k] = v.replace("{role}", role)

    ts = time.strftime("%Y%m%d-%H%M%S")
    log_path = WIKI / "logs" / f"headless-{role}-{ts}.log"
    log = open(log_path, "ab")

    # 09-04 闪窗修复：DETACHED（无控制台）会让 codex 的子进程（powershell 执行器）
    # 各自开新可见窗口→蓝框屏闪。改 CREATE_NEW_CONSOLE + SW_HIDE：给被拉起工具一个
    # 隐藏控制台，其子进程附着同一控制台不开新窗（kimi/codex/hermes 全工具统一口径）。
    CREATE_NEW_CONSOLE = 0x00000010
    CREATE_NEW_PROCESS_GROUP = 0x00000200
    STARTF_USESHOWWINDOW = 0x00000001
    si = subprocess.STARTUPINFO()
    si.dwFlags |= STARTF_USESHOWWINDOW
    si.wShowWindow = 0  # SW_HIDE
    p = subprocess.Popen(
        cmd,
        cwd=str(WIKI),
        stdout=log,
        stderr=log,
        creationflags=CREATE_NEW_CONSOLE | CREATE_NEW_PROCESS_GROUP,
        startupinfo=si,
        env=env,
    )
    print(f"proc_{role}_{p.pid} | tool={tool} | log={log_path} | {time.strftime('%H:%M:%S')}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
