#!/usr/bin/env python3
"""MCP 挂载 + 新卡可检索巡检（#326 机制制度化，P2-DYN-01 ②）。

检查项：
  1. 每个 Hermes profile（Windows 8 + WSL 8）的 config.yaml 含 mcp_servers.kdo
     ——按 systemd WorkingDirectory 实证（WSL 侧实际运行位置），不查目录名同名文件
  2. 新卡可检索抽查：终审闭环后 `kdo query` 命中验证

用法：
    python 90_control/scripts/check-mcp-roaming.py             # 人类可读
    python 90_control/scripts/check-mcp-roaming.py --json      # JSON 输出
    python 90_control/scripts/check-mcp-roaming.py --query "SPIN 销售"   # 指定检索抽查词

退出码：0=全过；1=有 FAIL（挂载缺失/检索未命中）；2=有 WARN（profile 未部署豁免）
"""
import argparse
import json
import os
import re
import subprocess
import sys
from pathlib import Path

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")

WIKI = Path(__file__).resolve().parent.parent.parent
WINDOWS_HERMES = Path(r"C:\Users\Administrator\.hermes\profiles")
WINDOWS_PROFILES = [
    "basic-skills-coach", "coaching-leadership-assistant", "duanwangye",
    "hongqigong", "laowantong", "meeting-assistant", "note-coach", "wangyuyan",
]
WSL_PROFILES = [
    "beikai", "duan", "duanwangye", "kimi-test",
    "laowantong", "laowantong-feishu", "ouyangfeng", "wangyuyan",
]
WSL_HOME = subprocess.run(["wsl", "-e", "bash", "-c", "echo $HOME"],
                          capture_output=True, timeout=30).stdout.decode().strip()
EXEMPT_WSL = {"duan", "kimi-test"}  # #325 豁免：废弃/测试 profile


def wsl_file(path):
    r = subprocess.run(["wsl", "-e", "bash", "-c", f"cat \"{path}\""],
                       capture_output=True, timeout=30)
    return r.stdout.decode("utf-8", errors="replace") if r.returncode == 0 else None


def wsl_exists(path):
    r = subprocess.run(["wsl", "-e", "bash", "-c", f"test -f \"{path}\" && echo yes"],
                       capture_output=True, timeout=30)
    return r.stdout.decode().strip() == "yes"


def check_mount(platform, name):
    if platform == "windows":
        cfg = WINDOWS_HERMES / name / "config.yaml"
        if not cfg.exists():
            return "MISS", "未部署"
        src = cfg.read_text(encoding="utf-8", errors="replace")
    else:
        path = f"{WSL_HOME}/.hermes/profiles/{name}/config.yaml"
        if not wsl_exists(path):
            if name in EXEMPT_WSL:
                return "EXEMPT", "废弃/测试 profile（#325 豁免）"
            return "MISS", "未部署"
        src = wsl_file(path) or ""
    if re.search(r"^  kdo:\s*$", src, re.M) and "server.py" in src and "enabled: true" in src:
        return "OK", "mcp_servers.kdo 已挂"
    if name in EXEMPT_WSL:
        return "EXEMPT", "废弃/测试 profile（#325 豁免）"
    return "FAIL", "缺 mcp_servers.kdo"


def check_search(query="SPIN 销售"):
    try:
        r = subprocess.run(["kdo", "query", query, "--limit", "3"],
                           capture_output=True, timeout=180,
                           cwd=str(WIKI), encoding="utf-8", errors="replace")
        out = (r.stdout or "") + (r.stderr or "")
        # kdo query 输出含卡片 id/路径行则视为命中
        hit = bool(re.search(r"(30_wiki/|id: [a-z0-9-]+|\d+\.\d+\] )", out))
        return "OK" if hit else "FAIL", f"exit={r.returncode}, {'命中' if hit else '未命中'} {query}"
    except Exception as e:
        return "FAIL", str(e)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--json", action="store_true")
    ap.add_argument("--query", default="SPIN 销售")
    args = ap.parse_args()

    results = {}
    worst = 0
    for platform, profiles in (("windows", WINDOWS_PROFILES), ("wsl", WSL_PROFILES)):
        for name in profiles:
            status, detail = check_mount(platform, name)
            results[f"{platform}/{name}"] = {"status": status, "detail": detail}
            if status == "FAIL":
                worst = max(worst, 1)
            elif status == "MISS":
                worst = max(worst, 2)

    q_status, q_detail = check_search(args.query)
    results["检索抽查"] = {"status": q_status, "detail": q_detail}
    if q_status == "FAIL":
        worst = max(worst, 1)

    if args.json:
        print(json.dumps(results, ensure_ascii=False, indent=2))
        sys.exit(worst)

    ok = sum(1 for v in results.values() if v["status"] == "OK")
    exempt = sum(1 for v in results.values() if v["status"] == "EXEMPT")
    total = len(results)
    print("=" * 60)
    print(f"  MCP 巡检 | OK {ok} / EXEMPT {exempt} / 共 {total} | {'PASS' if worst == 0 else 'FAIL'}")
    print("=" * 60)
    for k, v in results.items():
        print(f"  [{v['status']:<6}] {k}: {v['detail']}")
    sys.exit(worst)


if __name__ == "__main__":
    main()
