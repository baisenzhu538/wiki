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

通道健康预检+fallback（#656，F-073：kimi 403 周额度/codex 余额尽两墙连撞的根治）：
  launch 前对 fallback 链逐通道打最小探针（1-token HTTP 或 CLI 级，见 channel_health.py）——
  首个健康通道执行拉起；主通道死→自动切下一个（todos+stdout 通知，stdout 走时钟契约=飞书 DM）；
  全部不健康→不硬派（假跑必撞墙），报王语嫣处置，exit 2。
  --no-probe 应急跳过预检；--force-dead kimi,claude 模拟死通道（测试钩）。
  认知表（CLI 名→真实供应商→模型→key 指纹）：90_control/channel-model-map.md

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
TODOS_DIR = WIKI / "90_control" / "todos"

sys.path.insert(0, str(Path(__file__).resolve().parent))
import channel_health

# 通知走 stdout（时钟契约=飞书 DM）——编码钉死 UTF-8（clock_watchdog.py 同款），不吃控制台 GBK
if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")

# 工具路由表：工具名 → 无头单发命令模板（{prompt}/{role} 为占位符）。
# 新工具上线前先实测其无头模式（-p/print/exec 形态+权限模式），再登记。
# 09-03 实测登记（王语嫣）：claude=deepseek-v4-flash（黄药师线）/ hermes=glm-5.3-flash（老顽童线，profile 走 -p flag，#650 前误用 HERMES_PROFILE env 致角色错载）/ codex=deepseek-v4-pro（欧阳锋线，需 relay 4444 活着）。
# 纪律：一律用原生 .exe——.cmd/.bat 壳在 DETACHED 无控制台环境下起不来（09-03 实测三次 0 字节日志）。
# 09-04 老朱令：黄药师线改 kimi K3（claude/DeepSeek 无订阅余额）——kimi 模板显式钉死 k3 别名防配置漂移
TOOLS = {
    "kimi": [r"C:\Users\Administrator\.kimi-code\bin\kimi.exe", "-m", "kimi-code/k3", "-p", "{prompt}"],
    "claude": [r"C:\Users\Administrator\AppData\Roaming\npm\node_modules\@anthropic-ai\claude-code\bin\claude.exe", "-p", "{prompt}", "--dangerously-skip-permissions"],
    "codex": [r"C:\Users\Administrator\AppData\Roaming\npm\node_modules\@openai\codex\node_modules\@openai\codex-win32-x64\vendor\x86_64-pc-windows-msvc\bin\codex.exe", "exec", "{prompt}", "--dangerously-bypass-approvals-and-sandbox", "--skip-git-repo-check"],
    # #650：hermes 角色切换必须走 -p {role} flag——HERMES_PROFILE env 在 hermes 的
    # profile 解析链里根本不被读（源码 _apply_profile_override：argv -p → active_profile
    # 文件 → HERMES_HOME env），env-only 拉起全部错载 active_profile（=huangyaoshi）。
    # 段王爷 09-06 实测三 profile 全自称错身份；-p flag PROFILE_OK。
    "hermes": [r"C:\Users\Administrator\AppData\Local\hermes\hermes-agent\venv\Scripts\hermes.exe", "-p", "{role}", "-z", "{prompt}", "--yolo"],
}

# 角色→默认工具路由（老朱 09-03 异构防线：不同模型防同构错误）。--tool 显式指定优先。
# 09-03 20:10 王语嫣调整：laowantong 暂回 kimi——hermes 通道两连死+一次锁挂（#626/#629 实例死亡、19:41 拉起即死 0 字节日志），待通道修复后恢复 hermes
ROLE_TOOL = {
    "huangyaoshi": "kimi",
    "laowantong": "kimi",
    "ouyangfeng": "codex",
}

# fallback 链顺序（#656）：主工具不健康 → 按此序找下一个健康通道。
# 依据：claude(GLM) 09-05 夜全通道连死时唯一全夜存活→最优先；codex(deepseek) 已充值复活次之；
# kimi/hermes 同上游 api.kimi.com（403 周额度连坐，探针按上游去重不撞二遍墙）→排最后。
FALLBACK_ORDER = ["claude", "codex", "kimi", "hermes"]


def chain_for(role, explicit_tool=None):
    primary = explicit_tool or ROLE_TOOL.get(role, "kimi")
    return [primary] + [t for t in FALLBACK_ORDER if t != primary]


def notify(role, lines):
    """通道切换/全死通知：stdout（时钟契约=送达飞书 DM，见 clock_watchdog.py 头注）+ todos 落账。"""
    for line in lines:
        print(line)
    try:
        todos = TODOS_DIR / f"{role}.md"
        if todos.exists():
            with open(todos, "a", encoding="utf-8") as f:
                for line in lines:
                    f.write(f"- [{time.strftime('%Y-%m-%d %H:%M')}] 【通道预检 #656】{line}\n")
    except OSError:
        pass


def parse_args(argv):
    """→ dict(role, instruction, tool, no_probe, force_dead)。位置参数之外的 flag 原样吞掉。"""
    opts = {"role": None, "instruction": None, "tool": None, "no_probe": False, "force_dead": []}
    positional = []
    i = 0
    while i < len(argv):
        a = argv[i]
        if a == "--tool":
            i += 1
            opts["tool"] = argv[i] if i < len(argv) else ""
        elif a == "--no-probe":
            opts["no_probe"] = True
        elif a == "--force-dead":
            i += 1
            if i < len(argv):
                opts["force_dead"] = [t for t in argv[i].split(",") if t]
        else:
            positional.append(a)
        i += 1
    if len(positional) > 0:
        opts["role"] = positional[0]
    if len(positional) > 1:
        opts["instruction"] = positional[1]
    return opts


def select_channel(role, chain, force_dead=(), prober=None):
    """预检+选通道：返回 (选中工具, 探测结果列表)。全死→(None, results)。"""
    results = channel_health.probe_chain(chain, force_dead=force_dead, prober=prober)
    ok = channel_health.first_healthy(results)
    selected = ok.tool if ok else None
    channel_health.log_results(results, decision=f"{role}->{selected or '全死不硬派'}")
    return selected, results

# 工具级环境变量（{role} 占位符同样替换）。
# #650：hermes 的 HERMES_PROFILE env 条目已移除——hermes 从不读它（无头解析链只认
# -p flag / active_profile 文件 / HERMES_HOME env），留着的死配置会误导后人以为 env 在管角色。
TOOL_ENV = {}

PROMPT_TEMPLATE = """你是{role}（KDO 知识工厂角色）。工作目录 {wiki}（先 cd 进去，一切操作在该目录下）。

启动恢复（必做）：
1. Read .agent/startup.md
2. Read .agent/{role}-context.md（若不存在跳过，改读 20_memory/{role}-amnesia-recovery.md）
3. Read 90_control/todos/{role}.md 的最后 20 行（未读段）

然后执行本次任务指令：
{instruction}

通用纪律（不可协商）：
- 行为宪法（#652 老朱 09-06 拍板，五条行为底线，全 agent 强制）：Read 90_control/agent-behavior-constitution.md——断言三级标注【实证/推断/猜测】、负向判词必附存在性核查锚点、疑问先检索再开口（商业主体调研用 business-research skill，其余 kdo query+grep）、解放-检验循环、Y模型三问后才方案。
- 队列状态流转只走 python 90_control/scripts/queue_transition.py（claim <task_id> --instance {role} / complete ... --evidence ... / review ...），禁止手改队列和任务单 status。实例名=裸角色名（#620 老朱 09-02 铁律：工具=变量不进名字）。
- 完工在 90_control/todos/{role}.md 追加一行（[YYYY-MM-DD HH:MM] 动作+任务号+结果）。
- 提审前任务单内必须有五字段执行报告（**交付物**/**完成内容**/**验证**/**边界**/**需要谁动作** 各起一行）。
- 只做本次指令范围内的事，做完收工，不扩展到其他任务。
- 备份避让（#628）：vault 自动备份每 30min 一拍（kdo-vault-git-backup，现落 :20/:50，以 logs/vault-git-backup.log 尾行为准）——拍前 5 分钟禁 stash/worktree 切换类操作，未提交在制品保持落盘可见即可（有活动会话备份会自行跳拍）；长任务隔离验证一律 git worktree。
"""


def main(argv=None) -> int:
    opts = parse_args(sys.argv[1:] if argv is None else argv)
    role, instruction, tool = opts["role"], opts["instruction"], opts["tool"]
    if not role or not instruction:
        print(__doc__)
        return 1
    if tool is not None and tool not in TOOLS:
        print(f"未知工具 {tool}（已登记：{list(TOOLS)}）——先实测无头模式再登记 TOOLS 表")
        return 1

    chain = chain_for(role, tool)
    if opts["no_probe"]:
        tool = chain[0]  # 应急直通：跳过预检，按主通道硬拉
    else:
        tool, results = select_channel(role, chain, force_dead=opts["force_dead"])
        if tool is None:
            dead = "；".join(f"{r.tool}: {r.reason}" for r in results)
            notify(role, [
                f"【通道全死】{role} 拉起中止，不硬派（假跑必撞墙）——报王语嫣处置",
                f"探测明细：{dead}",
                "应急直通：python 90_control/scripts/kimi-headless-launch.py {r} '<指令>' --no-probe".replace("{r}", role),
            ])
            return 2
        if tool != chain[0]:
            dead = next(r for r in results if r.tool == chain[0])
            notify(role, [
                f"【通道fallback】{chain[0]} 不健康（{dead.reason}）→ {role} 已切 {tool}"
                f"（上游 {channel_health.TOOL_UPSTREAM.get(tool, '?')}）",
            ])

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
