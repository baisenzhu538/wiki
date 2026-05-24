"""DeepSeek Token 用量监控 — 通过 Claude Code 会话文件增长速率间接监控。

每 5 分钟检查一次 Claude Code 会话文件（.jsonl）的大小变化。
如果任意文件在 5 分钟内增长超过阈值 → Windows 桌面弹窗告警。
如果单日累积增长超过日阈值 → 告警。

安装：
  python deepseek-usage-monitor.py --install   # 注册为 Windows 启动计划任务
  python deepseek-usage-monitor.py --run       # 直接运行（前台）
  python deepseek-usage-monitor.py --uninstall # 移除计划任务
"""

import argparse
import json
import os
import subprocess
import sys
import time
from datetime import datetime, timedelta
from pathlib import Path

# 强制 UTF-8 输出（Windows GBK 兼容）
if sys.stdout.encoding != "utf-8":
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")
if sys.stderr.encoding != "utf-8":
    sys.stderr.reconfigure(encoding="utf-8", errors="replace")

# ── 配置 ──────────────────────────────────────────────
CHECK_INTERVAL_SEC = 300       # 每 5 分钟检查一次
GROWTH_THRESHOLD_MB = 5        # 5 分钟内增长超过 5MB → 告警
DAILY_THRESHOLD_MB = 100       # 单日累计增长超过 100MB → 告警
COOLDOWN_MINUTES = 15          # 同一类型告警冷却时间（分钟）

# Claude Code 会话目录
CLAUDIAN_SESSIONS_DIR = Path(os.path.expandvars(
    r"%USERPROFILE%\.claude\projects\C--Users-Administrator-Desktop-wiki"
))

TASK_NAME = "DeepSeek Usage Monitor"
SCRIPT_PATH = Path(__file__).resolve()


def show_alert(title: str, message: str) -> None:
    """Windows 桌面弹窗 + 事件日志。"""
    # 转义单引号，防止破坏 PowerShell 字符串
    safe_msg = message.replace("'", "''")
    safe_title = title.replace("'", "''")
    ps_script = f"""
    Add-Type -AssemblyName System.Windows.Forms
    [System.Windows.Forms.MessageBox]::Show(
        '{safe_msg}',
        '{safe_title}',
        [System.Windows.Forms.MessageBoxButtons]::OK,
        [System.Windows.Forms.MessageBoxIcon]::Warning
    )
    """
    try:
        subprocess.run(
            ["powershell.exe", "-NoProfile", "-Command", ps_script],
            capture_output=True, timeout=10,
        )
    except (subprocess.TimeoutExpired, FileNotFoundError):
        pass

    # 控制台日志
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    try:
        print(f"[{timestamp}] ALERT: {title} — {message}")
    except UnicodeEncodeError:
        print(f"[{timestamp}] ALERT: {title} - {message}".encode("ascii", errors="replace").decode())


def get_jsonl_sizes(sessions_dir: Path) -> dict[str, int]:
    """返回 {filename: size_bytes} 映射。"""
    if not sessions_dir.exists():
        return {}
    return {
        f.name: f.stat().st_size
        for f in sessions_dir.glob("*.jsonl")
    }


def find_total_growth(
    current: dict[str, int],
    previous: dict[str, int],
) -> tuple[int, str]:
    """返回 (growth_bytes, detail_string)。"""
    total = 0
    details: list[str] = []
    for name, size in current.items():
        prev = previous.get(name, 0)
        if size > prev:
            delta = size - prev
            total += delta
            if delta > 1024 * 1024:  # 只报告 >1MB 的变化
                details.append(f"  {name}: +{delta / (1024*1024):.1f} MB")
    return total, "\n".join(details)


def run_monitor() -> None:
    """主监控循环。"""
    print(f"[{datetime.now().strftime('%H:%M:%S')}] DeepSeek 用量监控启动")
    print(f"  监控目录: {CLAUDIAN_SESSIONS_DIR}")
    print(f"  检查间隔: {CHECK_INTERVAL_SEC}s")
    print(f"  增长告警阈值: {GROWTH_THRESHOLD_MB} MB / {CHECK_INTERVAL_SEC}s")
    print(f"  单日告警阈值: {DAILY_THRESHOLD_MB} MB")

    # 状态文件路径
    state_file = Path(os.path.expandvars(
        r"%USERPROFILE%\.claude\.usage-monitor-state.json"
    ))

    # 加载或初始化状态
    if state_file.exists():
        try:
            state = json.loads(state_file.read_text(encoding="utf-8"))
        except (json.JSONDecodeError, ValueError):
            state = {}
    else:
        state = {}

    last_sizes: dict[str, int] = state.get("last_sizes", {})
    today = datetime.now().strftime("%Y-%m-%d")
    daily_total = state.get("daily_total_mb", 0.0) if state.get("date") == today else 0.0
    last_growth_alert = datetime.fromisoformat(state.get("last_growth_alert", "2000-01-01"))
    last_daily_alert = datetime.fromisoformat(state.get("last_daily_alert", "2000-01-01"))

    # 初始化时读取当前状态（不告警）
    if not last_sizes:
        last_sizes = get_jsonl_sizes(CLAUDIAN_SESSIONS_DIR)
        state["last_sizes"] = last_sizes
        state["date"] = today
        state["daily_total_mb"] = 0.0
        state_file.write_text(json.dumps(state, indent=2), encoding="utf-8")
        print(f"[{datetime.now().strftime('%H:%M:%S')}] 初始化完成，监控 {len(last_sizes)} 个会话文件")

    while True:
        try:
            time.sleep(CHECK_INTERVAL_SEC)
            now = datetime.now()

            # 日期翻转 → 重置日累计
            current_date = now.strftime("%Y-%m-%d")
            if current_date != today:
                today = current_date
                daily_total = 0.0

            # 获取当前文件大小并计算增长
            current_sizes = get_jsonl_sizes(CLAUDIAN_SESSIONS_DIR)
            growth_bytes, details = find_total_growth(current_sizes, last_sizes)
            growth_mb = growth_bytes / (1024 * 1024)
            daily_total += growth_mb

            ts = now.strftime("%H:%M:%S")

            if growth_mb > 0:
                print(f"[{ts}] +{growth_mb:.2f} MB (今日累计: {daily_total:.1f} MB)")

            # ── 检查 1: 短期增长过快 ──
            if growth_mb >= GROWTH_THRESHOLD_MB:
                if (now - last_growth_alert).total_seconds() > COOLDOWN_MINUTES * 60:
                    show_alert(
                        "⚠️ DeepSeek Token 用量告警",
                        f"过去 {CHECK_INTERVAL_SEC // 60} 分钟内消耗约 {growth_mb:.0f} MB 会话数据\n"
                        f"(估算 token 消耗异常偏高)\n\n"
                        f"详情:\n{details}\n\n"
                        f"今日累计: {daily_total:.1f} MB"
                    )
                    last_growth_alert = now

            # ── 检查 2: 单日累计超阈值 ──
            if daily_total >= DAILY_THRESHOLD_MB:
                if (now - last_daily_alert).total_seconds() > COOLDOWN_MINUTES * 60:
                    show_alert(
                        "🔴 DeepSeek 单日用量超限",
                        f"今日累计会话增长: {daily_total:.0f} MB\n"
                        f"已超过单日阈值 {DAILY_THRESHOLD_MB} MB\n\n"
                        f"建议检查是否有异常进程或死循环"
                    )
                    last_daily_alert = now

            # 持久化状态
            last_sizes = current_sizes
            state.update({
                "last_sizes": last_sizes,
                "date": today,
                "daily_total_mb": round(daily_total, 2),
                "last_growth_alert": last_growth_alert.isoformat(),
                "last_daily_alert": last_daily_alert.isoformat(),
                "last_check": now.isoformat(),
            })
            state_file.write_text(json.dumps(state, indent=2), encoding="utf-8")

        except KeyboardInterrupt:
            print("\n监控已停止。")
            break
        except Exception as exc:
            print(f"[{datetime.now().strftime('%H:%M:%S')}] 错误: {exc}")


def install_task() -> None:
    """注册为 Windows 启动计划任务。"""
    python_exe = sys.executable
    script = str(SCRIPT_PATH)
    # 用 cmd.exe 静默启动 python
    command = f'{python_exe} "{script}" --run'
    xml = f"""<?xml version="1.0" encoding="UTF-16"?>
<Task version="1.4" xmlns="http://schemas.microsoft.com/windows/2004/02/mit/task">
  <Triggers>
    <LogonTrigger>
      <Delay>PT1M</Delay>
    </LogonTrigger>
  </Triggers>
  <Principals>
    <Principal id="Author">
      <UserId>{os.environ.get('USERNAME', 'Administrator')}</UserId>
      <LogonType>InteractiveToken</LogonType>
      <RunLevel>LeastPrivilege</RunLevel>
    </Principal>
  </Principals>
  <Settings>
    <DisallowStartIfOnBatteries>false</DisallowStartIfOnBatteries>
    <StopIfGoingOnBatteries>false</StopIfGoingOnBatteries>
    <ExecutionTimeLimit>PT0S</ExecutionTimeLimit>
    <Hidden>true</Hidden>
    <MultipleInstancesPolicy>IgnoreNew</MultipleInstancesPolicy>
  </Settings>
  <Actions>
    <Exec>
      <Command>{python_exe}</Command>
      <Arguments>"{script}" --run</Arguments>
    </Exec>
  </Actions>
</Task>"""

    task_xml = SCRIPT_PATH.with_suffix(".xml")
    task_xml.write_text(xml, encoding="utf-16")

    try:
        # 先删旧任务
        subprocess.run(
            ["schtasks", "/delete", "/tn", TASK_NAME, "/f"],
            capture_output=True,
        )
        # 创建新任务
        result = subprocess.run(
            ["schtasks", "/create", "/tn", TASK_NAME, "/xml", str(task_xml), "/f"],
            capture_output=True, text=True,
        )
        if result.returncode == 0:
            print(f"[OK] 计划任务 '{TASK_NAME}' 已安装（系统启动时自动运行）")
        else:
            print(f"[FAIL] 安装失败: {result.stderr}")
    finally:
        task_xml.unlink(missing_ok=True)


def uninstall_task() -> None:
    """移除 Windows 计划任务。"""
    result = subprocess.run(
        ["schtasks", "/delete", "/tn", TASK_NAME, "/f"],
        capture_output=True, text=True,
    )
    if result.returncode == 0:
        print(f"✅ 计划任务 '{TASK_NAME}' 已移除")
    else:
        print(f"⚠️ 移除失败（可能不存在）: {result.stderr}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="DeepSeek Token 用量监控")
    parser.add_argument("--run", action="store_true", help="启动监控（前台运行）")
    parser.add_argument("--install", action="store_true", help="安装为 Windows 启动计划任务")
    parser.add_argument("--uninstall", action="store_true", help="移除 Windows 计划任务")
    args = parser.parse_args()

    if args.install:
        install_task()
    elif args.uninstall:
        uninstall_task()
    else:
        run_monitor()
