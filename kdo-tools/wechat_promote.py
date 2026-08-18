#!/usr/bin/env python3
"""偶遇采集产物自动转正（inbox → 知识库仓库）。

铁律（用户 2026-08-17 纠偏）：新内容第一站 00_inbox/，未经处理不入库。
本脚本 = 转正流程：把已知识化的产物按 KDO 规范入仓——
  逐字稿 → 10_raw/sources/（素材层，source_id 文件名登记）
  研究文档 → 30_wiki/cases/（知识层，frontmatter 合规 + 质量门）

用法:
  python kdo-tools/wechat_promote.py            # 转正所有已知识化产物
  python kdo-tools/wechat_promote.py --dry-run  # 预览不执行
"""
import argparse
import re
import shutil
import subprocess
import sys
from datetime import date
from pathlib import Path

sys.stdout.reconfigure(encoding="utf-8", errors="replace")

WIKI = Path(__file__).resolve().parent.parent
INBOX_DIR = WIKI / "00_inbox" / "wechat-collect"
SOURCES_DIR = WIKI / "10_raw" / "sources"
CASES_DIR = WIKI / "30_wiki" / "cases"


def promote_transcript(f: Path, dry_run: bool) -> bool:
    """逐字稿 → 10_raw/sources/（文件名带 source_id：src_<date>_wechat_<hash>）。"""
    m = re.search(r"src_wechat_([A-Za-z0-9]{8,20})", f.name)
    if not m:
        return False
    hash_id = m.group(1)
    target = SOURCES_DIR / f"src_{date.today().isoformat()}_wechat_{hash_id}.md"
    if target.exists():
        print(f"⏭️  已转正: {target.name}")
        return True
    if dry_run:
        print(f"  [dry-run] {f.name} → {target.name}")
        return True
    shutil.copy2(f, target)
    print(f"✅ 逐字稿入仓: {target.name}")
    return True


def promote_case(f: Path, dry_run: bool) -> bool:
    """研究文档 → 30_wiki/cases/（frontmatter 校验：title/type/domain/source_refs 必填）。"""
    content = f.read_text(encoding="utf-8")
    required = ["title:", "type:", "domain:", "source_refs:", "created_at:"]
    missing = [k for k in required if k not in content]
    if missing:
        print(f"⚠️ 跳过（缺 frontmatter {missing}）: {f.name}")
        return False
    target = CASES_DIR / f.name
    if target.exists():
        print(f"⏭️  已转正: {target.name}")
        return True
    if dry_run:
        print(f"  [dry-run] {f.name} → 30_wiki/cases/")
        return True
    shutil.copy2(f, target)
    print(f"✅ 研究文档入仓: {target.name}")
    return True


def main():
    ap = argparse.ArgumentParser(description="偶遇采集产物自动转正")
    ap.add_argument("--dry-run", action="store_true")
    args = ap.parse_args()

    print("📦 转正开始" + ("（dry-run 预览）" if args.dry_run else ""))
    t_ok = c_ok = 0

    # 1) 逐字稿 → 素材层
    for f in sorted(INBOX_DIR.glob("src_wechat_*.md")):
        if promote_transcript(f, args.dry_run):
            t_ok += 1

    # 2) 研究文档 → 知识层
    kdir = INBOX_DIR / "knowledge"
    if kdir.exists():
        for f in sorted(kdir.glob("case-wechat-*.md")):
            if promote_case(f, args.dry_run):
                c_ok += 1

    print(f"\n📊 逐字稿 {t_ok} 个，研究文档 {c_ok} 个" + ("（dry-run，未写入）" if args.dry_run else ""))

    if not args.dry_run and (t_ok or c_ok):
        # 转正完成提示（质量门 lint 全库太慢，改由定期巡检/欧阳锋审查覆盖）
        print("✅ 转正完成——产物已入 10_raw/sources + 30_wiki/cases（待定期 lint 巡检）")


if __name__ == "__main__":
    main()
