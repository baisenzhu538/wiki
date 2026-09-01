#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""strip_skill_bom.py — #598 动作3：SKILL.md UTF-8 BOM 批量清理（黄药师基建）。

只动编码层不动内容：删除文件头 EF BB BF 三字节（UTF-8 BOM），其余字节级不变。
转换前做基线快照（sha256 + 长度），转换后断言：
  new_bytes == old_bytes[3:]           —— 字节级 diff 为零（仅去 BOM 头）
  不存在 BOM 残留                        —— 残留清零断言

--check 模式：只报告不修改（回归用，exit 1 = 仍有 BOM）。

用法：
  python 40_outputs/code/scripts/strip_skill_bom.py             # 全量清理 + 断言
  python 40_outputs/code/scripts/strip_skill_bom.py --check     # 只检查（门禁/回归）

任务单：60_feedback/tasks/task_20260902_huangyaoshi-bom-cleanup-health-radar.md
口径来源：60_feedback/diagnosis/建议书_20260901_skill健康度勘察与检测方法论.md §二（37/76 BOM）
"""

from __future__ import annotations

import argparse
import hashlib
import sys
from pathlib import Path

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")

WIKI = Path(__file__).resolve().parents[3]
SKILLS_DIR = WIKI / "40_outputs" / "capabilities" / "skills"
BOM = b"\xef\xbb\xbf"


def iter_skill_files():
    """扫 shared/ + 根目录全部 SKILL.md（与 scan_skills_registry.py 同一面）。"""
    if not SKILLS_DIR.exists():
        return
    for d in sorted(SKILLS_DIR.iterdir()):
        if not d.is_dir():
            continue
        scan_root = [d] if d.name != "shared" else sorted(d.iterdir())
        for sd in scan_root:
            if not sd.is_dir():
                continue
            sm = sd / "SKILL.md"
            if sm.exists():
                yield sm


def strip_file(p: Path) -> bool:
    """去 BOM 并做字节级零 diff 断言。返回是否发生修改。断言失败抛 AssertionError。"""
    raw = p.read_bytes()
    if not raw.startswith(BOM):
        return False
    baseline = hashlib.sha256(raw).hexdigest()
    new = raw[3:]
    # 零 diff 断言：新内容必须恰好等于原内容剥掉 BOM 头
    assert new == raw[len(BOM):], f"{p}: 剥离结果与基线不一致（非纯 BOM 头剥离）"
    assert hashlib.sha256(new).hexdigest() != baseline or not new, f"{p}: sha 未变化"
    # 幂等性自证：再次剥离应无变化
    assert not new.startswith(BOM), f"{p}: 剥离后仍有 BOM 残留"
    p.write_bytes(new)
    # 写后复核
    after = p.read_bytes()
    assert after == new, f"{p}: 写入后字节不一致"
    return True


def main() -> int:
    ap = argparse.ArgumentParser(description="#598 SKILL.md BOM 批量清理")
    ap.add_argument("--check", action="store_true", help="只检查不修改（残留→exit 1）")
    args = ap.parse_args()

    total = cleaned = 0
    residue = []
    for p in iter_skill_files():
        total += 1
        raw = p.read_bytes()
        if raw.startswith(BOM):
            residue.append(p)
            if not args.check:
                if strip_file(p):
                    cleaned += 1

    if args.check:
        if residue:
            print(f"🔴 BOM 残留 {len(residue)} 个：")
            for p in residue:
                print(f"   {p.relative_to(WIKI)}")
            return 1
        print(f"🟢 BOM 残留清零：{total} 个 SKILL.md 全部无 BOM")
        return 0

    print(f"✅ 清理完成：{total} 个 SKILL.md 扫描，{cleaned} 个去 BOM")
    # 执行后自证：残留必须清零
    left = [p for p in iter_skill_files() if p.read_bytes().startswith(BOM)]
    if left:
        print(f"🔴 异常：清理后仍有 {len(left)} 个残留")
        return 1
    print(f"🟢 残留清零断言通过（0/{total}）；字节级 diff=0（仅去 EF BB BF 头）")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
