#!/usr/bin/env python3
"""pre_review.py — 机器预审管线（#515，全自动阶段 1 参考层）。

提审单（complete）时自动跑四项机器判据，出「机器预审报告」附任务单：
  1. 声称-交付差集：执行报告交付物路径 vs 文件实测（存在/git 跟踪/无脏改动）
     ——判法原型=欧阳锋 08-24 差集（#499 实证 37 张漏清单）
  2. lint：任务单自身 YAML/frontmatter 可解析 + F-034 五字段在位（复用既有门禁检查器）
  3. 负向判词核查：执行报告含负向断言词时的锚点检查（#433 判据前移生产侧）
  4. 存在性核查锚点：负向判词触发时 **存在性核查** 节在位性

纪律（红线）：预审报告只做参考层——不自动放行、不自动拦截、机器建议不入档为结论。
判据清单后校准（老朱 08-26 拍板：先建管线后校准，不等满 2 周基线）；
欧阳锋终审对照（一致率目标 ≥90% 跑 2 周，对照数据源=#514 基线）。

用法：
  python 90_control/scripts/pre_review.py <task_id>          # 打印预审报告
  queue_transition complete 内部自动调用（预审报告随提审 commit 入冻结版）
"""
import sys
from pathlib import Path

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")

_SCRIPT_DIR = Path(__file__).resolve().parent
sys.path.insert(0, str(_SCRIPT_DIR))

import queue_transition as qt  # 复用既有检查器（单一真相源，不另写判据）

PRE_REVIEW_HEADER = "## 机器预审报告"
PRE_REVIEW_DISCLAIMER = "> 🤖 机器预审参考层（#515）：仅供欧阳锋终审参考，不构成结论、不放行不拦截"


def run_pre_review(task_file: Path, wiki_root: Path | None = None) -> str:
    """对提审任务单跑四项机器判据，返回 Markdown 预审报告节（纯函数，不写文件）。"""
    wiki_root = wiki_root or qt._WIKI_ROOT
    body = task_file.read_text(encoding="utf-8", errors="ignore")
    fm, _ = qt.parse_frontmatter(task_file)
    report = qt._extract_exec_report(body)

    lines = [PRE_REVIEW_HEADER, "", PRE_REVIEW_DISCLAIMER, ""]

    # ① 声称-交付差集：报告声称的交付物路径 vs 文件实测
    claimed = qt._extract_deliverable_paths(report, task_file.name) if report else []
    code_files = fm.get("code_files") or []
    if isinstance(code_files, str):
        code_files = [code_files]
    code_files = [str(c) for c in code_files]
    declared = sorted(set(claimed) | {c for c in code_files if "/" in c})
    if not declared:
        lines.append("### ① 声称-交付差集\n\n⚪ 无路径级交付物声明（纯文档/诊断类或未用反引号标注路径）——差集无检查面")
    else:
        missing, untracked, dirty = [], [], []
        for rel in declared:
            if "Knowledge Delivery OS" in rel:  # 跨仓路径本层不展开（#363 门禁已管 dirty）
                continue
            fp = wiki_root / rel
            if not fp.exists():
                missing.append(rel)
                continue
            if not qt._git_tracked(wiki_root, rel):
                untracked.append(rel)
            elif qt._git_uncommitted(wiki_root, [rel]):
                dirty.append(rel)
        if not (missing or untracked or dirty):
            lines.append(f"### ① 声称-交付差集\n\n✅ {len(declared)} 个声明路径全部存在+已跟踪+无脏改动")
        else:
            lines.append("### ① 声称-交付差集\n")
            for r in missing:
                lines.append(f"- 🔴 声称但文件不存在: `{r}`")
            for r in untracked:
                lines.append(f"- 🔴 声称但未入仓（untracked）: `{r}`")
            for r in dirty:
                lines.append(f"- 🟡 声称但有未提交改动: `{r}`")

    # ② lint：任务单 frontmatter 可解析 + F-034 五字段在位
    fm_ok = bool(fm.get("id") and fm.get("assignee"))
    fields_missing = [name for name, anchors in qt.DELIVERY_FIELDS.items()
                      if not any(a in report for a in anchors)] if report else list(qt.DELIVERY_FIELDS)
    lint_ok = fm_ok and not fields_missing
    lines.append("### ② lint\n\n"
                 + ("✅ frontmatter 可解析 + F-034 五字段在位" if lint_ok else
                    f"🔴 frontmatter 缺字段（{'✓' if fm_ok else 'id/assignee 缺'}）/五字段缺：{'、'.join(fields_missing) or '无'}"))

    # ③④ 负向判词 + 存在性核查锚点（#433 判据，前移生产侧执行报告）
    neg_ok, neg_msg = qt._check_negative_claims(report or "")
    anchor = "✅ 存在性核查锚点在位" if qt.EVIDENCE_ANCHOR in (report or "") else "⚪ 无锚点"
    if neg_ok and not neg_msg:
        lines.append("### ③ 负向判词 / ④ 存在性核查\n\n✅ 执行报告无负向断言词（检查面=执行报告节）")
    elif neg_ok:
        lines.append(f"### ③ 负向判词 / ④ 存在性核查\n\n🟡 {neg_msg}；锚点：{anchor}")
    else:
        lines.append(f"### ③ 负向判词 / ④ 存在性核查\n\n🔴 {neg_msg}（生产侧同口径，供终审对照）")

    return "\n".join(lines) + "\n"


def attach_pre_review(task_file: Path, report: str) -> None:
    """预审报告写入任务单（幂等：替换既有节，不 append 堆叠）。

    插入位置：「## 终审记录」前；无则文件尾。complete 流转的自动 commit 会把它
    收进提审冻结版（预审报告=提审版本的一部分，版本对齐不破）。
    """
    body = task_file.read_text(encoding="utf-8")
    idx = body.find(PRE_REVIEW_HEADER)
    if idx != -1:
        nxt = body.find("\n## ", idx + 1)
        body = body[:idx] + (body[nxt + 1:] if nxt > 0 else "")
        body = body.rstrip("\n") + "\n\n"
    anchor = body.find("\n## 终审记录")
    if anchor > 0:
        body = body[:anchor] + "\n" + report + body[anchor:]
    else:
        body = body.rstrip("\n") + "\n\n" + report
    task_file.write_text(body, encoding="utf-8")


def main() -> int:
    if len(sys.argv) < 2:
        print("用法: python 90_control/scripts/pre_review.py <task_id>")
        return 2
    task_file = qt._find_task_file_dual(sys.argv[1])
    if task_file is None:
        print(f"找不到任务单: {sys.argv[1]}")
        return 1
    print(run_pre_review(task_file))
    return 0


if __name__ == "__main__":
    sys.exit(main())
