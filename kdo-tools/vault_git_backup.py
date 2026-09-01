#!/usr/bin/env python3
"""vault git 快照备份（#607：系统级调度版，替代会话级 cron）。

根因背景：历史「vault backup: <ts>」commit 由会话级 cron 产生——无 schtasks 条目、
vault 内无脚本、节拍随会话生死；2026-08-26 22:56 系统重启杀掉承载会话后停摆 6 天
（08-27~09-01 零 backup）无人察觉。本脚本改挂系统级 schtasks（kdo-vault-git-backup，
每 30 分钟），会话生死不再影响备份面。

语义与历史一致：工作区有变更才全树快照 commit，无变更静默 exit 0。
只探测/落盘，不做任何通知（停摆报警在 conveyor_probe `_scan_backup_stall`）。
"""
import subprocess
import sys
from datetime import datetime
from pathlib import Path

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")
if hasattr(sys.stderr, "reconfigure"):
    sys.stderr.reconfigure(encoding="utf-8", errors="replace")

ROOT = Path(__file__).resolve().parent.parent


def run(args: list[str]) -> subprocess.CompletedProcess:
    return subprocess.run(args, cwd=ROOT, capture_output=True, text=True,
                          encoding="utf-8", errors="replace", timeout=180)


def main() -> int:
    if not run(["git", "status", "--porcelain"]).stdout.strip():
        return 0  # 无变更静默
    run(["git", "add", "-A"])
    msg = f"vault backup: {datetime.now():%Y-%m-%d %H:%M:%S}"
    r = run(["git", "commit", "-m", msg])
    if r.returncode != 0:
        print(f"⚠️ vault backup commit 失败: {r.stderr[-300:]}", file=sys.stderr)
        return 1
    print(msg)
    return 0


if __name__ == "__main__":
    sys.exit(main())
