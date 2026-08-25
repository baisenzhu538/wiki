#!/usr/bin/env python3
"""KDO 运行时漂移巡检（#364）——只读检测，发现漂移只报警不修复。

三项检测：
1. 进程版本漂移：kdo MCP server 进程启动时间 vs 相关源码最新 commit 时间
   （进程早于最新修复 = 生产跑旧代码，小昭第四轮 9 进程 21:41 旧代码事故制度化兜底）
2. 双索引同步：graph_index vs search_index 最后更新对比（#356 机制；#358 重建后生效）
3. 启动指针有效性：CAPSULE_STARTUP.md 路由引用目标存在（#366 指针 v2）

用法：
    python 90_control/scripts/check-runtime-drift.py           # 人类可读
    python 90_control/scripts/check-runtime-drift.py --json    # JSON 输出

退出码：0 = 无漂移；1 = 检测到漂移
"""

import argparse
import datetime as _dt
import json
import subprocess
import sys
from pathlib import Path

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")

VAULT_ROOT = Path(__file__).resolve().parent.parent.parent
KDO_REPO = Path(r"C:\Users\Administrator\Knowledge Delivery OS 0.0.1")

# 生产进程对应的源码路径（任一更新即需重启）
PROC_SOURCES = [
    ("wiki", "kdo-tools/mcp/tools.py"),
    ("wiki", "kdo-tools/mcp/server.py"),
    ("kdo", "kdo/commands/delivery.py"),
    ("kdo", "kdo/commands/graph.py"),
]


def git_commit_time(repo: Path, rel_path: str) -> float | None:
    """Latest commit time (epoch) touching rel_path in repo."""
    try:
        out = subprocess.run(
            ["git", "-C", str(repo), "log", "-1", "--format=%ct", "--", rel_path],
            capture_output=True, text=True, timeout=15,
        ).stdout.strip()
        return float(out) if out else None
    except Exception:
        return None


def list_mcp_server_processes() -> list[dict]:
    """Windows: MCP server.py processes with creation time (epoch)."""
    try:
        ps = subprocess.run(
            ["powershell", "-NoProfile", "-Command",
             "Get-CimInstance Win32_Process -Filter \"Name='python.exe'\" | "
             "Where-Object { $_.CommandLine -like '*kdo-tools*mcp*server.py*' } | "
             "ForEach-Object { $_.ProcessId.ToString() + '|' + [DateTimeOffset]::new($_.CreationDate.ToUniversalTime()).ToUnixTimeSeconds().ToString() }"],
            capture_output=True, text=True, timeout=30,
        ).stdout
    except Exception:
        return []
    procs = []
    for line in ps.splitlines():
        line = line.strip()
        if "|" in line:
            pid, created = line.split("|", 1)
            try:
                procs.append({"pid": int(pid), "created": float(created)})
            except ValueError:
                pass
    return procs


def main():
    parser = argparse.ArgumentParser(description="KDO 运行时漂移巡检（#364）")
    parser.add_argument("--json", action="store_true")
    args = parser.parse_args()

    findings: list[dict] = []

    # ── 1. 进程版本漂移 ──
    procs = list_mcp_server_processes()
    oldest_source = None
    for repo_name, rel in PROC_SOURCES:
        repo = KDO_REPO if repo_name == "kdo" else VAULT_ROOT
        t = git_commit_time(repo, rel)
        if t and (oldest_source is None or t > oldest_source):
            oldest_source = t

    drift_count = 0
    if procs and oldest_source:
        for p in procs:
            if p["created"] < oldest_source:
                drift_count += 1
                age_h = (oldest_source - p["created"]) / 3600
                findings.append({
                    "check": "process-version",
                    "level": "DRIFT",
                    "detail": f"PID {p['pid']} started before latest source commit ({age_h:.1f}h stale)",
                })
        if not drift_count:
            findings.append({
                "check": "process-version",
                "level": "OK",
                "detail": f"{len(procs)} MCP server process(es) all newer than latest source commit",
            })
    else:
        findings.append({
            "check": "process-version",
            "level": "INFO",
            "detail": f"no MCP server processes found (n={len(procs)}, latest_source={oldest_source is not None})",
        })

    # ── 2. 双索引同步 ──
    graph_state = VAULT_ROOT / ".kdo" / "graph_state.json"
    search_index = VAULT_ROOT / ".kdo" / "search_index.json"
    if graph_state.exists() and search_index.exists():
        g_t = graph_state.stat().st_mtime
        s_t = search_index.stat().st_mtime
        diff_h = abs(g_t - s_t) / 3600
        if diff_h > 24:
            findings.append({
                "check": "dual-index",
                "level": "DRIFT",
                "detail": f"graph_index vs search_index out of sync ({diff_h:.0f}h apart; graph={_dt.datetime.fromtimestamp(g_t):%m-%d %H:%M}, search={_dt.datetime.fromtimestamp(s_t):%m-%d %H:%M})",
            })
        else:
            findings.append({"check": "dual-index", "level": "OK", "detail": f"indexes within {diff_h:.1f}h of each other"})
    else:
        findings.append({"check": "dual-index", "level": "INFO", "detail": "one of graph_state/search_index missing"})

    # ── 3. 启动指针有效性 ──
    capsule = VAULT_ROOT / ".kdo" / "CAPSULE_STARTUP.md"
    if not capsule.exists():
        findings.append({"check": "startup-pointer", "level": "DRIFT", "detail": "CAPSULE_STARTUP.md missing (#366)"})
    else:
        # 路由引用目标抽查（§2 路由表里黄药师/王语嫣的必读文件）
        missing = []
        for rel in [".agent/huangyaoshi-context.md", ".agent/wangyuyan-context.md",
                    ".agent/context.md", "70_product/tasks/production-queue.md"]:
            if not (VAULT_ROOT / rel).exists():
                missing.append(rel)
        if missing:
            findings.append({"check": "startup-pointer", "level": "DRIFT", "detail": f"routed targets missing: {missing}"})
        else:
            findings.append({"check": "startup-pointer", "level": "OK", "detail": "pointer v2 present, routed targets exist"})

    drift = [f for f in findings if f["level"] == "DRIFT"]
    if args.json:
        print(json.dumps({"drift": findings, "stale": drift_count, "exit": 1 if drift else 0},
                         ensure_ascii=False, indent=2))
    else:
        print("=" * 60)
        print(f"  KDO Runtime Drift Check (#364)  |  {'DRIFT FOUND' if drift else 'CLEAN'}")
        print("=" * 60)
        for f in findings:
            print(f"  [{f['level']}] {f['check']}: {f['detail']}")
        print()
        if drift:
            print("[FAIL] 漂移已检测——先处置（重启/重建/修复）再继续，勿带病作业。")
        else:
            print("[PASS] 无漂移。")
    sys.exit(1 if drift else 0)


if __name__ == "__main__":
    main()
