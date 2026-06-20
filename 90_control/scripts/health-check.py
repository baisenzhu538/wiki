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
        # 提取关键统计行作为 summary
        lines = result.stdout.strip().split("\n")
        stat_lines = [l for l in lines if l.startswith("**")]
        summary = stat_lines[0] if stat_lines else (lines[0][:100] if lines else "no output")
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

    # 人类可读报告
    lines = [
        "# KDO 健康检查报告",
        f"**模式**: {'快速' if args.quick else '完整'} | **域**: {args.domain or '全库'}",
        "",
        "| 检查项 | 状态 | 摘要 |",
        "|---|---|---|",
    ]

    worst = 0
    all_ok = True
    for name, cargs, desc in checks:
        ec, summary = run_script(name, cargs)
        if ec > 0:
            status = "❌ FAIL"
            all_ok = False
            worst = max(worst, ec)
        elif ec < 0:
            status = "⚠️ ERROR"
            all_ok = False
            worst = 1
        else:
            status = "✅ PASS"
        lines.append(f"| {desc} | {status} | {summary[:100]} |")

    lines.append("")
    if all_ok:
        lines.append("✅ 全部检查通过。")
    else:
        lines.append("❌ 存在不健康项，请逐项检查。")

    print("\n".join(lines))
    sys.exit(worst)


if __name__ == "__main__":
    main()
