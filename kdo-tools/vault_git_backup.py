#!/usr/bin/env python3
"""vault git 快照备份（#607：系统级调度版，替代会话级 cron）。

根因背景：历史「vault backup: <ts>」commit 由会话级 cron 产生——无 schtasks 条目、
vault 内无脚本、节拍随会话生死；2026-08-26 22:56 系统重启杀掉承载会话后停摆 6 天
（08-27~09-01 零 backup）无人察觉。本脚本改挂系统级 schtasks（kdo-vault-git-backup，
每 30 分钟），会话生死不再影响备份面。

语义与历史一致：工作区有变更才全树快照 commit，无变更静默 exit 0。
只探测/落盘，不做任何通知（停摆报警在 conveyor_probe `_scan_backup_stall`）。

#625 大文件门禁第二层（提交链路拦截）：git add -A 后、commit 前扫描暂存区文件大小——
- >100MB（GitHub 硬限）→ 把该文件移出暂存区（git rm --cached，工作区文件不动），
  其余变更照常 commit（硬拦文件入仓 ≠ 硬拦整个备份——整单拒提会把备份打成停摆事故），
  stderr 打印 + 台账 90_control/large-file-gate.log 留痕；
- >15MB → WARNING 打印 + 台账（不拦）。
背景：391MB zip 经本脚本 add -A 静默入仓 → GitHub 100MB 硬限断 push 3 个月（2026-09-02 实证）。
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

# #625 阈值（任务单口径：>100MB 硬拦、>15MB WARNING）
HARD_LIMIT_BYTES = 100 * 1024 * 1024
WARN_LIMIT_BYTES = 15 * 1024 * 1024
GATE_LOG = ROOT / "90_control" / "large-file-gate.log"

_EDU = "GitHub 100MB 硬限，391MB zip 曾断 push 3 个月（2026-09-02 实证）"


def run(args: list[str]) -> subprocess.CompletedProcess:
    return subprocess.run(args, cwd=ROOT, capture_output=True, text=True,
                          encoding="utf-8", errors="replace", timeout=180)


def _log_gate(lines: list[str]) -> None:
    """台账留痕（失败不阻断备份主流程）。"""
    try:
        GATE_LOG.parent.mkdir(parents=True, exist_ok=True)
        ts = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        with GATE_LOG.open("a", encoding="utf-8") as f:
            for line in lines:
                f.write(f"{ts}｜{line}\n")
    except Exception as e:
        print(f"⚠️ large-file-gate 台账写入失败（不阻断备份）: {e}", file=sys.stderr)


def gate_staged_large_files() -> tuple[list[str], list[str]]:
    """#625：暂存区大文件门禁。返回 (blocked, warned) 路径列表。

    >100MB：git rm --cached 移出暂存（工作区文件保留）→ 该文件不进仓；
    >15MB：WARNING 照提。盘上已读不到/大小异常的文件跳过（fail-open 不阻断备份）。
    """
    out = run(["git", "diff", "--cached", "--name-only", "--diff-filter=ACMR", "-z"]).stdout
    blocked: list[str] = []
    warned: list[str] = []
    for rel in [p for p in out.split("\0") if p]:
        try:
            size = (ROOT / rel).stat().st_size
        except OSError:
            continue
        if size > HARD_LIMIT_BYTES:
            run(["git", "rm", "--cached", "--quiet", "--", rel])
            blocked.append(rel)
            print(f"⛔ 大文件硬拦（>{HARD_LIMIT_BYTES >> 20}MB）：{rel}（{size >> 20}MB）"
                  f"已移出本次提交，工作区文件保留；{_EDU}。"
                  f"处置：移 D:\\KDO-memory\\ 归档或走 .gitignore #625 白名单豁免（需王语嫣/老朱拍板）",
                  file=sys.stderr)
        elif size > WARN_LIMIT_BYTES:
            warned.append(rel)
            print(f"⚠️ 大文件 WARNING（>{WARN_LIMIT_BYTES >> 20}MB）：{rel}（{size >> 20}MB）"
                  f"本次照提；{_EDU}——持续增长请评估归档", file=sys.stderr)
    ledger = [f"BLOCKED｜{p}" for p in blocked] + [f"WARNING｜{p}" for p in warned]
    if ledger:
        _log_gate(ledger)
    return blocked, warned


def main() -> int:
    if not run(["git", "status", "--porcelain"]).stdout.strip():
        return 0  # 无变更静默
    run(["git", "add", "-A"])
    blocked, _warned = gate_staged_large_files()
    if blocked and not run(["git", "diff", "--cached", "--name-only"]).stdout.strip():
        print("⚠️ 全部暂存变更均被大文件硬拦，本次无快照 commit", file=sys.stderr)
        return 1
    msg = f"vault backup: {datetime.now():%Y-%m-%d %H:%M:%S}"
    r = run(["git", "commit", "-m", msg])
    if r.returncode != 0:
        print(f"⚠️ vault backup commit 失败: {r.stderr[-300:]}", file=sys.stderr)
        return 1
    print(msg)
    return 0


if __name__ == "__main__":
    sys.exit(main())
