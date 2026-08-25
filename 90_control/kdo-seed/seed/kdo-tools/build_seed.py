#!/usr/bin/env python3
"""build_seed.py — kdo-seed 种子包构建器（#532）。

A 层机制文件全集 → 90_control/kdo-seed/（可重复构建，清单即文档）：
  角色文件 .agent/*.md + agents/{五角色}/、制度层（charter/schemas/quality-gates/
  quality-metrics-spec/consumer-retrieval-protocol）、工具层（kdo-tools 核心+
  90_control/scripts 检查/流转类）、九层空骨架、agent复盘骨架说明。

剔除（边界）：域相关采集脚本（wechat/douyin/利润为王系）、一次性修复批（fix-*.py/
stage4-*）、_tmp 划痕、C 实例内容层（30_wiki 卡片/队列/复盘历史）一律不进种子。

用法：python kdo-tools/build_seed.py [--out DIR]（默认 90_control/kdo-seed/）
"""
import argparse
import shutil
import sys
from pathlib import Path

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")

ROOT = Path(__file__).resolve().parent.parent

ROLES = ["huangyaoshi", "laowantong", "wangyuyan", "ouyangfeng", "fengqingyang"]

# 工具层核心清单（生产在跑+检查/流转类；域采集与一次性修复不入列）
KDO_TOOLS = [
    "conveyor_probe.py", "l1_capture.py", "daily-context-save.py", "quality_metrics.py",
    "memory_capsule.py", "review-check.py", "watch_inbox.py", "generate-dashboard.py",
    "queue_batch_accept.py", "tags-audit.py", "infra-status.py", "recovery-check.py",
    "build_seed.py",
]
CONTROL_SCRIPTS = [
    "queue_transition.py", "queue_gate.py", "queue_lock.py", "health-check.py",
    "check-conveyor-state.py", "check-review-sla.py", "check-depended-draft.py",
    "pre_review.py", "audit_queue_integrity.py", "shared_file_guard.py",
    "full-library-rescan.py", "check-runtime-drift.py", "check-derivatives.py",
    "check-draft-aging.py", "check-tags-health.py", "file-flow-check.py",
]
CMD_WRAPPERS = [
    "kdo-conveyor-probe.cmd", "kdo-l1-capture.cmd", "kdo-quality-metrics.cmd",
    "run-daily-audit-digest.cmd", "run-kdo-health.cmd", "run-l1-archive.cmd",
]
GOVERNANCE = [
    "90_control/kdo-charter-v0.1-draft.md", "90_control/quality-metrics-spec-v1.md",
    "90_control/consumer-retrieval-protocol.md", "90_control/role-clock-architecture.md",
    "90_control/infrastructure-inventory.md", "90_control/file-flow-protocol.md",
    "90_control/conveyor-probes-contract.md", "90_control/robustness-checklist.md",
]
GOVERNANCE_DIRS = ["90_control/schemas", "90_control/quality-gates"]
NINE_LAYERS = ["00_inbox", "10_raw", "20_memory", "30_wiki", "40_outputs",
               "50_delivery", "60_feedback", "70_product", "90_control", ".kdo"]


def build(out_dir: Path) -> dict:
    out_dir.mkdir(parents=True, exist_ok=True)
    stats = {"files": 0, "dirs": 0}

    def cp(rel: str, dst_sub: str):
        src = ROOT / rel
        dst = out_dir / dst_sub
        dst.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(src, dst)
        stats["files"] += 1

    # 1. 角色文件：.agent/*.md + agents/{五角色}/ + 20_memory 失忆锚点
    for f in (ROOT / ".agent").glob("*.md"):
        cp(f".agent/{f.name}", f"seed/.agent/{f.name}")
    for f in (ROOT / "20_memory").glob("*-amnesia-recovery.md"):
        cp(f"20_memory/{f.name}", f"seed/20_memory/{f.name}")
    for role in ROLES:
        src = ROOT / "agents" / role
        if src.is_dir():
            dst = out_dir / "seed" / "agents" / role
            if dst.exists():
                shutil.rmtree(dst)
            shutil.copytree(src, dst)
            stats["files"] += sum(1 for f in dst.rglob("*") if f.is_file())

    # 2. 制度层
    for rel in GOVERNANCE:
        if (ROOT / rel).exists():
            cp(rel, f"seed/{rel}")
    for d in GOVERNANCE_DIRS:
        src = ROOT / d
        if src.is_dir():
            dst = out_dir / "seed" / d
            if dst.exists():
                shutil.rmtree(dst)
            shutil.copytree(src, dst)
            stats["files"] += sum(1 for f in dst.rglob("*") if f.is_file())

    # 3. 工具层
    for f in KDO_TOOLS:
        if (ROOT / "kdo-tools" / f).exists():
            cp(f"kdo-tools/{f}", f"seed/kdo-tools/{f}")
    for f in CONTROL_SCRIPTS:
        if (ROOT / "90_control" / "scripts" / f).exists():
            cp(f"90_control/scripts/{f}", f"seed/90_control/scripts/{f}")
    for f in CMD_WRAPPERS:
        if (ROOT / "kdo-tools" / f).exists():
            cp(f"kdo-tools/{f}", f"seed/kdo-tools/{f}")

    # 4. 九层空骨架 + agent复盘骨架
    for layer in NINE_LAYERS:
        d = out_dir / "seed" / layer
        d.mkdir(parents=True, exist_ok=True)
        (d / ".gitkeep").write_text("", encoding="utf-8")
        stats["dirs"] += 1
    for role in ROLES:
        d = out_dir / "seed" / "agent复盘" / role / "daily-context"
        d.mkdir(parents=True, exist_ok=True)
        (d / ".gitkeep").write_text("", encoding="utf-8")
        stats["dirs"] += 1

    return stats


def main() -> int:
    ap = argparse.ArgumentParser(description="kdo-seed 种子包构建（#532）")
    ap.add_argument("--out", help="输出目录（默认 90_control/kdo-seed）")
    args = ap.parse_args()
    out = Path(args.out) if args.out else ROOT / "90_control" / "kdo-seed"
    stats = build(out)
    print(f"🌱 种子包构建完成: {out}（{stats['files']} 文件，{stats['dirs']} 骨架目录）")
    return 0


if __name__ == "__main__":
    sys.exit(main())
