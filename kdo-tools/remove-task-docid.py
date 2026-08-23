#!/usr/bin/env python3
"""remove-task-docid.py — 任务单/spec 卡 doc_id 字段移除（#477，E045 闭环）

任务单编号空间=#队列号（doc_id 只用于建议书/诊断/审查意见书，#449 规范 §2）。
本脚本只删 frontmatter 顶层 doc_id 行，其余字段/正文不动；删后 yaml.safe_load
校验（E017 族：结构化校验，禁手搓正则删块）。

用法：
  python kdo-tools/remove-task-docid.py --dry-run   # 只列清单+校验
  python kdo-tools/remove-task-docid.py --apply     # 执行移除
"""

from __future__ import annotations

import argparse
import sys
from pathlib import Path

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")

WIKI_ROOT = Path(__file__).resolve().parent.parent
TASK_DIR = WIKI_ROOT / "60_feedback" / "tasks"
SPEC_DIR = WIKI_ROOT / "30_wiki" / "agent-specs"


def scan_violations():
    """frontmatter 含 doc_id 的任务单/spec 卡（yaml.safe_load 结构化判定）。"""
    import yaml
    viol = []
    for d in (TASK_DIR, SPEC_DIR):
        for fp in sorted(d.glob("*.md")):
            try:
                with fp.open("r", encoding="utf-8", errors="ignore") as f:
                    lines = []
                    for i, line in enumerate(f):
                        if i == 0 and not line.startswith("---"):
                            break
                        if i > 0 and line.startswith("---"):
                            break
                        lines.append(line)
                fm = yaml.safe_load("".join(lines)) or {}
            except Exception:
                continue
            if fm.get("doc_id"):
                viol.append((fp, fm.get("doc_id")))
    return viol


def _remove_docid_lines(fp: Path) -> bool:
    """删除 frontmatter 内顶层 doc_id 行（保持其他行原样）。返回是否改动。"""
    with fp.open("r", encoding="utf-8", errors="ignore") as f:
        text = f.read()
    lines = text.splitlines(keepends=True)
    in_fm = text.startswith("---")
    changed = False
    out = []
    for idx, line in enumerate(lines):
        stripped = line.lstrip()
        # frontmatter 顶层 key：无缩进
        if in_fm and idx > 0 and stripped and not stripped.startswith("-") \
                and not stripped.startswith("#") and not stripped.startswith("---") \
                and ":" in stripped and not stripped[0].isspace():
            key = stripped.split(":", 1)[0].strip()
            if key == "doc_id":
                changed = True
                continue
        out.append(line)
    if changed:
        fp.write_text("".join(out), encoding="utf-8")
    return changed


def _validate(fp: Path) -> bool:
    """移除后 frontmatter 仍 yaml.safe_load 合法。"""
    import yaml
    try:
        with fp.open("r", encoding="utf-8", errors="ignore") as f:
            lines = []
            for i, line in enumerate(f):
                if i == 0 and not line.startswith("---"):
                    return True  # 无 frontmatter 不校验
                if i > 0 and line.startswith("---"):
                    break
                lines.append(line)
        fm = yaml.safe_load("".join(lines))
        return isinstance(fm, dict) and "doc_id" not in fm
    except Exception:
        return False


def main() -> int:
    ap = argparse.ArgumentParser(description="任务单 doc_id 移除（#477）")
    ap.add_argument("--dry-run", action="store_true")
    ap.add_argument("--apply", action="store_true")
    args = ap.parse_args()

    viol = scan_violations()
    print(f"违规 {len(viol)} 份:")
    for fp, did in viol:
        print(f"  {fp.relative_to(WIKI_ROOT)} | doc_id={did}")

    if args.dry_run or not args.apply:
        print("\n[dry-run] 以上为将移除 doc_id 的文件清单（只删 doc_id 行，其余不动）")
        return 0

    ok, fail = 0, 0
    for fp, _ in viol:
        if _remove_docid_lines(fp) and _validate(fp):
            ok += 1
            print(f"✅ {fp.relative_to(WIKI_ROOT)}")
        else:
            fail += 1
            print(f"⛔ 失败/校验不过: {fp.relative_to(WIKI_ROOT)}")
    print(f"\n移除完成: {ok} 成功 / {fail} 失败")
    return 1 if fail else 0


if __name__ == "__main__":
    sys.exit(main())
