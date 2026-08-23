#!/usr/bin/env python3
"""infra-status.py — 基建资产健康快照（#488 任务2，`kdo infra status` 的 wiki 侧实现）。

一条命令输出各资产健康态（🟢 绿灯/🟡 黄灯/🔴 红灯/⚪ 未知），是 health-check 之上的
资产视图层（不替换 health-check——它跑逐项检查，本命令查资产存在性+关键健康信号）。

KDO CLI 侧 `kdo infra status` 集成待后续（#473 kdo lint 集成同模式，跨仓改动需
KDO 561 测试回归）。

用法：
  python kdo-tools/infra-status.py           # 全资产快照
  python kdo-tools/infra-status.py --json    # JSON 输出（供调度/审计）
退出码：有红灯=1；全绿=0。
"""

from __future__ import annotations

import argparse
import json
import shutil
import sqlite3
import subprocess
import sys
from pathlib import Path

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")

WIKI = Path(__file__).resolve().parent.parent
SCRIPTS = WIKI / "90_control" / "scripts"
KDO_TOOLS = Path(__file__).resolve().parent
MEM = Path.home() / ".kdo-memory"
D_MEM = Path("D:/KDO-memory")

# 资产清单：位置 + 名称 + 健康检查函数
def _file_ok(p: Path) -> bool:
    """文件/目录存在即健康（目录 st_size 可能为 0，不能当异常）。"""
    return p.exists()


def _task_exists(name: str) -> bool:
    try:
        r = subprocess.run(["schtasks", "/Query", "/TN", name], capture_output=True)
        return r.returncode == 0
    except OSError:
        return False


def _process_exists(name: str) -> bool:
    try:
        r = subprocess.run(["tasklist", "/FI", f"IMAGENAME eq {name}"], capture_output=True)
        return name.lower().encode() in r.stdout.lower()  # 二进制匹配防 GBK 解码乱码
    except OSError:
        return False


def _port_open(port: int) -> bool:
    import socket
    s = socket.socket()
    s.settimeout(0.5)
    try:
        s.connect(("127.0.0.1", port))
        return True
    except OSError:
        return False
    finally:
        s.close()


ASSETS: list[tuple[str, str, object]] = [
    # (名称, 类型, 检查)
    ("queue_transition", "门禁", SCRIPTS / "queue_transition.py"),
    ("queue_gate", "门禁", SCRIPTS / "queue_gate.py"),
    ("audit_queue_integrity", "门禁", SCRIPTS / "audit_queue_integrity.py"),
    ("health-check", "门禁", SCRIPTS / "health-check.py"),
    ("check-tags-health", "门禁", SCRIPTS / "check-tags-health.py"),
    ("conveyor_probe", "工具", KDO_TOOLS / "conveyor_probe.py"),
    ("memory_capsule", "工具", KDO_TOOLS / "memory_capsule.py"),
    ("l1_capture", "工具", KDO_TOOLS / "l1_capture.py"),
    ("daily-context-save", "工具", KDO_TOOLS / "daily-context-save.py"),
    ("review-check", "工具", KDO_TOOLS / "review-check.py"),
    ("file-flow-check", "工具", KDO_TOOLS / "file-flow-check.py"),
    ("tags-audit", "工具", KDO_TOOLS / "tags-audit.py"),
    ("queue_batch_accept", "工具", KDO_TOOLS / "queue_batch_accept.py"),
    ("infrastructure-inventory", "总表", WIKI / "90_control" / "infrastructure-inventory.md"),
    ("role-routes", "路由层", WIKI / "90_control" / "role-routes.md"),
    ("CAPSULE_STARTUP", "入口", WIKI / ".kdo" / "CAPSULE_STARTUP.md"),
    ("L1 主库", "数据", MEM / "L1" / "activity_log.db"),
    ("L1-full 主库", "数据", D_MEM / "L1-full"),
    ("L1 镜像", "数据", D_MEM / "L1-backup"),
    ("gate-blocked.log", "台账", WIKI / "90_control" / "gate-blocked.log"),
    ("force-exceptions.log", "台账", "OPTIONAL:" + str(WIKI / "90_control" / "force-exceptions.log")),
    ("计划任务 kdo-conveyor-probe", "计划任务", "kdo-conveyor-probe"),
    ("计划任务 kdo-l1-capture", "计划任务", "kdo-l1-capture"),
    ("计划任务 kdo-inbox-watch", "计划任务", "kdo-inbox-watch"),
    ("计划任务 kdo-health-daily", "计划任务", "kdo-health-daily"),
    ("服务 hermes", "服务", "hermes.exe"),
    ("服务 wx_video_download", "服务", 2022),
]


def _check(asset: tuple[str, str, object]) -> tuple[str, str, str]:
    name, kind, probe = asset
    try:
        if isinstance(probe, Path):
            ok = _file_ok(probe)
            return (name, kind, "🟢" if ok else "🔴")
        if isinstance(probe, str):
            if probe.startswith("OPTIONAL:"):
                # 可选台账：不存在=无例外记录=健康；存在=有记录（仅报告）
                return (name, kind, "🟢")
            ok = _task_exists(probe) if "计划任务" in kind else _process_exists(probe)
            return (name, kind, "🟢" if ok else "🔴")
        if isinstance(probe, int):
            return (name, kind, "🟢" if _port_open(probe) else "🟡")  # 端口服务黄灯（非致命）
    except Exception:
        return (name, kind, "⚪")
    return (name, kind, "⚪")


def main() -> int:
    ap = argparse.ArgumentParser(description="基建资产健康快照（#488）")
    ap.add_argument("--json", action="store_true")
    args = ap.parse_args()

    results = [_check(a) for a in ASSETS]
    reds = [r for r in results if r[2] == "🔴"]
    if args.json:
        print(json.dumps(
            {"assets": [{"name": n, "kind": k, "status": s} for n, k, s in results],
             "red": len(reds), "total": len(results)},
            ensure_ascii=False, indent=2))
        return 1 if reds else 0

    print(f"# 基建资产健康快照（#488 · {len(results)} 项）")
    for name, kind, status in results:
        print(f"  {status} [{kind}] {name}")
    print(f"\n红灯 {len(reds)}/{len(results)}" + ("（需人工核查）" if reds else "（全绿）"))
    return 1 if reds else 0


if __name__ == "__main__":
    sys.exit(main())
