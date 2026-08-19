#!/usr/bin/env python3
"""
⛔ DEPRECATED（2026-08-19，#377 收敛决议）——请用 `kdo pre-submit`（KDO CLI，L4 法定门禁）。

本脚本与 CLI 门禁规则引擎不一致已造成实测分叉：同一批卡本脚本 FAIL 而
`kdo pre-submit` PASS（kdo_lint.py 把 "source_refs→00_inbox" 这条文本为 WARN 的
规则以 ERROR 级拦截，CLI 无此规则）。双门禁并存 = 迟早误杀好卡或放过坏卡。

保留原因：历史任务单引用追溯。新工作一律：
  python -m kdo pre-submit --files <files...>     # 或 --batch <任务单>

诊断报告与规则差异全表：60_feedback/tasks/task_20260819_huangyaoshi-presubmit-gate-convergence.md
---
Pre-submit 门禁 — 交卷前自检，增量错误清零才放行。

用法:
  python pre_submit.py --manifest manifest.txt
  python pre_submit.py --files 30_wiki/concepts/foo.md 30_wiki/frameworks/bar.md

流程:
  1. 读 manifest → 申报文件清单
  2. 跑 kdo_lint --incremental（全量快，基线已滤掉历史债）
  3. 只看申报文件的增量错误
  4. 零新增 → PASS；有新增 → FAIL + 列出错误
"""

import argparse
import subprocess
import sys
from pathlib import Path

VAULT_ROOT = Path(__file__).resolve().parent.parent.parent
LINT_SCRIPT = Path(__file__).resolve().parent / "kdo_lint.py"


def read_manifest(path: str) -> set[str]:
    """读申报清单，返回文件路径集合（规范化分隔符）。"""
    p = Path(path)
    if not p.exists():
        print(f"ERROR: manifest not found: {path}", file=sys.stderr)
        sys.exit(1)

    files = set()
    for line in p.read_text(encoding="utf-8-sig").splitlines():
        line = line.strip()
        if not line or line.startswith("#"):
            continue
        line = line.strip("'\"")
        line = line.removeprefix("[[").removesuffix("]]")
        line = line.replace("\\", "/")
        if line:
            files.add(line)
    return files


def normalize_path(p: str) -> str:
    """统一路径格式，用于匹配。"""
    return p.replace("\\", "/").removeprefix(str(VAULT_ROOT).replace("\\", "/")).strip("/")


def run_lint() -> tuple[list[str], int]:
    """跑 kdo_lint --incremental，返回 (output_lines, exit_code)。"""
    try:
        result = subprocess.run(
            [sys.executable, str(LINT_SCRIPT), "--incremental"],
            capture_output=True, text=True, timeout=120,
            cwd=str(VAULT_ROOT),
            encoding="utf-8", errors="replace",
        )
        return result.stdout.splitlines() + result.stderr.splitlines(), result.returncode
    except subprocess.TimeoutExpired:
        return ["ERROR: lint timed out"], 1
    except Exception as e:
        return [f"ERROR: lint failed: {e}"], 1


def extract_file_errors(lint_output: list[str], target_files: set[str]) -> list[str]:
    """从 lint 输出中提取目标文件的错误行。
    错误行格式: "  [ERROR] path/to/file.md: error message"
    """
    errors = []
    for line in lint_output:
        line = line.strip()
        if not line.startswith("[ERROR]"):
            continue
        for f in target_files:
            # 匹配路径（子串或规范化后）
            if f in line or normalize_path(f) in normalize_path(line):
                errors.append(line)
                break
    return errors


def main():
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    print("⛔ DEPRECATED：本门禁已废弃（#377，2026-08-19）——与法定门禁 `kdo pre-submit` 规则不一致。"
          "请改用：python -m kdo pre-submit --files <files...>。本脚本结果不作为交卷依据。", file=sys.stderr)

    parser = argparse.ArgumentParser(description="Pre-submit 门禁（已废弃，见 stderr）")
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument("--manifest", help="申报清单文件")
    group.add_argument("--files", nargs="*", help="直接指定文件列表")
    args = parser.parse_args()

    if args.manifest:
        target_files = read_manifest(args.manifest)
    else:
        target_files = {normalize_path(f) for f in args.files}

    if not target_files:
        print("No files to check.")
        sys.exit(0)

    print("=" * 55)
    print("Pre-submit Gate")
    print("=" * 55)
    print(f"  申报文件: {len(target_files)}")
    print(f"  检查项:   F1+F2+F3+F4 (updated_at/链接/重复/MOC死链) + DK_SECTION (dk七段) + SECTION_TYPO (拼写) + R6 (搜索可达性) + schema")
    print()

    # 跑 lint
    lint_output, lint_rc = run_lint()

    # 只看申报文件的错误
    errors = extract_file_errors(lint_output, target_files)

    if errors:
        print(f"❌ GATE FAILED — {len(errors)} new error(s) on submitted files:")
        print()
        for e in errors:
            print(f"  {e}")
        print()
        print("Fix the above, re-run pre_submit, then submit.")
        sys.exit(1)
    else:
        print("✅ GATE PASSED — zero new errors on submitted files.")
        if lint_rc != 0:
            print("   (non-submitted files have errors — not blocking this submission)")
        print()
        print("Ready to submit for review.")
        sys.exit(0)


if __name__ == "__main__":
    main()
