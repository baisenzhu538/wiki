#!/usr/bin/env python3
"""
KDO 健康检查统一入口
一键运行全部质量检查：lint + source_refs + VLM quality + production progress + agent config。
输出统一报告，退出码反映最高严重级别。

用法：
    python 90_control/scripts/health-check.py                    # 全部检查
    python 90_control/scripts/health-check.py --quick             # 快速模式（仅 lint + source_refs）
    python 90_control/scripts/health-check.py --domain yitang     # 仅检查指定域
    python 90_control/scripts/health-check.py --json              # JSON 输出
"""

import argparse
import json
import subprocess
import sys
from pathlib import Path

# Ensure UTF-8 stdout
if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")

VAULT_ROOT = Path(__file__).resolve().parent.parent.parent
SCRIPTS_DIR = VAULT_ROOT / "90_control" / "scripts"


def run_script(name, args=None):
    """运行一个检查脚本，返回 (exit_code, output_summary)"""
    script = SCRIPTS_DIR / f"{name}.py"
    if not script.exists():
        return -1, f"脚本不存在: {script}"

    cmd = ["python", str(script)]
    if args:
        cmd.extend(args)
    try:
        result = subprocess.run(cmd, capture_output=True, text=True, timeout=120,
                                cwd=str(VAULT_ROOT), encoding="utf-8")
        # 提取关键统计行
        lines = result.stdout.strip().split("\n")
        stat_lines = [l for l in lines if "Files checked" in l or "扫描" in l or "P0" in l or "整体进度" in l or "正常" in l]
        if stat_lines:
            summary = stat_lines[0][:120]
        else:
            summary = [l for l in lines if l and not l.startswith("=")][:2]
            summary = summary[-1][:120] if summary else "no output"
        return result.returncode, summary
    except subprocess.TimeoutExpired:
        return -1, "超时"
    except Exception as e:
        return -1, str(e)


def main():
    parser = argparse.ArgumentParser(description="KDO 健康检查统一入口")
    parser.add_argument("--quick", action="store_true", help="快速模式")
    parser.add_argument("--domain", help="仅检查指定域")
    parser.add_argument("--json", action="store_true")
    args = parser.parse_args()

    checks = [
        ("kdo_lint", [], "Lint 格式校验"),
    ]

    if not args.quick:
        checks.extend([
            ("check-source-refs", ["--json"] if args.json else [], "source_refs 健康检查"),
            ("scan-vlm-parse-errors", [], "VLM 描述质量"),
            ("track-production-progress", ["--json"] if args.json else [], "生产进度"),
            ("check-agent-config", [], "Agent 配置自检"),
        ])

    if args.domain:
        for i, (name, cargs, desc) in enumerate(checks):
            if name == "check-source-refs":
                checks[i] = (name, ["--domain", args.domain], desc)

    if args.json:
        results = {}
        for name, cargs, desc in checks:
            ec, summary = run_script(name, cargs)
            results[name] = {"exit_code": ec, "summary": summary}
            print(json.dumps(results, ensure_ascii=False, indent=2))
        sys.exit(0 if all(r["exit_code"] == 0 for r in results.values()) else 1)

    # 人类可读报告（讲香升级：场景化输出）
    check_results = []
    worst = 0
    all_ok = True
    passed = 0
    for name, cargs, desc in checks:
        ec, summary = run_script(name, cargs)
        status_icon = "[PASS]" if ec == 0 else ("[WARN]" if ec < 0 else "[FAIL]")
        if ec > 0:
            all_ok = False
            worst = max(worst, ec)
        elif ec < 0:
            all_ok = False
            worst = 1
        else:
            passed += 1
        check_results.append({"desc": desc, "status": status_icon, "summary": summary[:120]})

    total = len(check_results)
    health_pct = int(passed / total * 100) if total else 0

    verdict = "PASS" if all_ok else "FAIL"
    lines = [
        "=" * 60,
        f"  KDO Health Check  |  {passed}/{total} passed  |  score {health_pct}/100  |  {verdict}",
        "=" * 60,
        "",
    ]

    # Add scenario-based context for each check
    hints = {
        "Lint 格式校验": "门禁第一关——frontmatter 格式、dk 七段、section 拼写、搜索可达性。红灯=老顽童提交前必须修。",
        "source_refs 健康检查": "溯源链是否完整——每张卡能不能追溯到原始素材。断链=欧阳锋无法验证事实。",
        "VLM 描述质量": "OCR/VLM 解析是否正常——影响洪七公的图片→prompt 管线。",
        "生产进度": "老顽童的产能仪表盘——多少卡在生产/待审/入库。红灯=队列堵塞。",
        "Agent 配置自检": "各 Agent 的 context/skill/权限是否一致——配置漂移=Agent 行为不可预期。",
    }

    for r in check_results:
        hint = hints.get(r["desc"], "")
        lines.append(f"  {r['status']} {r['desc']}")
        if r["summary"] and r["summary"] != "no output":
            lines.append(f"     {r['summary']}")
        if hint:
            lines.append(f"     {hint}")
        lines.append("")

    if all_ok:
        lines.append("[PASS] All green — safe to submit.")
    else:
        lines.append(f"[FAIL] {total - passed}/{total} checks failed. See hints above for what each means. Fix and re-run.")

    print("\n".join(lines))
    sys.exit(worst)


if __name__ == "__main__":
    main()
