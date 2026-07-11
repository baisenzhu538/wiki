#!/usr/bin/env python3
"""
Changeset 申报对账器 — 扫实动文件 vs 申报清单求差。
堵「申报≠实动」系统病。

用法:
  python changeset_audit.py --since "2026-07-12 05:00" --manifest manifest.txt
  python changeset_audit.py --since "2026-07-12 05:00" --manifest manifest.txt --json  # 机读输出
  python changeset_audit.py --window-minutes 180 --manifest manifest.txt

manifest 格式：每行一个文件路径（相对 wiki root），# 开头为注释。
"""

import argparse
import json
import os
import sys
from datetime import datetime
from pathlib import Path

VAULT_ROOT = Path(__file__).resolve().parent.parent.parent
CARD_DIRS = [
    "30_wiki/concepts", "30_wiki/frameworks", "30_wiki/tools", "30_wiki/cases",
    "30_wiki/methods", "30_wiki/systems", "30_wiki/operations", "30_wiki/dark-knowledges",
]


def parse_manifest(path: str) -> set[str]:
    """解析申报清单——每行一个路径，去注释去空白去引号。"""
    p = Path(path)
    if not p.exists():
        print(f"ERROR: manifest file not found: {path}", file=sys.stderr)
        sys.exit(1)

    raw = p.read_text(encoding="utf-8-sig")  # utf-8-sig 自动去 BOM
    entries = set()
    for line in raw.splitlines():
        line = line.strip()
        if not line or line.startswith("#"):
            continue
        # 去引号和 [[ ]]
        line = line.strip("'\"")
        line = line.removeprefix("[[").removesuffix("]]")
        # 统一分隔符
        line = line.replace("\\", "/")
        if line:
            entries.add(line)
    return entries


def scan_actual(since: datetime, until: datetime, dirs: list[str]) -> set[str]:
    """扫描指定目录下在时间窗内修改过的 .md 文件。"""
    actual = set()
    since_ts = since.timestamp()
    until_ts = until.timestamp()

    for d in dirs:
        card_dir = VAULT_ROOT / d
        if not card_dir.is_dir():
            continue
        for f in card_dir.rglob("*.md"):
            try:
                mtime = f.stat().st_mtime
            except OSError:
                continue
            if since_ts <= mtime <= until_ts:
                actual.add(str(f.relative_to(VAULT_ROOT)).replace("\\", "/"))
    return actual


def run(manifest_path: str, since: datetime, until: datetime, dirs: list[str]) -> dict:
    declared = parse_manifest(manifest_path)
    actual = scan_actual(since, until, dirs)

    matched = declared & actual
    undeclared = actual - declared    # 动了但没申报 🔴
    phantom = declared - actual        # 申报了但没动 🟡

    return {
        "window": f"{since.isoformat()} → {until.isoformat()}",
        "declared_count": len(declared),
        "actual_count": len(actual),
        "matched": sorted(matched),
        "undeclared": sorted(undeclared),
        "phantom": sorted(phantom),
        "clean": len(undeclared) == 0 and len(phantom) == 0,
    }


def main():
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")

    parser = argparse.ArgumentParser(description="Changeset 申报对账器")
    parser.add_argument("--manifest", required=True, help="申报清单文件路径")
    parser.add_argument("--since", help="起始时间 (ISO format, e.g. '2026-07-12 05:00')")
    parser.add_argument("--until", help="截止时间 (默认 now)")
    parser.add_argument("--window-minutes", type=int, help="时间窗（分钟），与 --since 二选一")
    parser.add_argument("--dirs", nargs="*", default=CARD_DIRS,
                        help="扫描目录（默认 wiki 卡目录）")
    parser.add_argument("--json", action="store_true", help="JSON 输出")
    args = parser.parse_args()

    # 时间窗
    now = datetime.now()
    if args.since:
        since = datetime.fromisoformat(args.since)
    elif args.window_minutes:
        since = datetime.fromtimestamp(now.timestamp() - args.window_minutes * 60)
    else:
        print("ERROR: --since or --window-minutes required", file=sys.stderr)
        sys.exit(1)
    until = datetime.fromisoformat(args.until) if args.until else now

    result = run(args.manifest, since, until, args.dirs)

    if args.json:
        print(json.dumps(result, ensure_ascii=False, indent=2))
    else:
        print("=" * 55)
        print("Changeset Audit — 申报对账")
        print("=" * 55)
        print(f"  时间窗:  {result['window']}")
        print(f"  申报:    {result['declared_count']} 个文件")
        print(f"  实动:    {result['actual_count']} 个文件")
        print()

        if result["undeclared"]:
            print(f"  🔴 UNDECLARED ({len(result['undeclared'])}): 动了但未申报")
            for f in result["undeclared"]:
                print(f"     {f}")
            print()

        if result["phantom"]:
            print(f"  🟡 PHANTOM ({len(result['phantom'])}): 申报了但未改动")
            for f in result["phantom"]:
                print(f"     {f}")
            print()

        if result["matched"]:
            print(f"  🟢 OK ({len(result['matched'])}): 申报与实动一致")
            print()

        if result["clean"]:
            print("✅ 对账通过——申报集 = 实动集")
        else:
            print("❌ 对账失败——申报集 ≠ 实动集，修正后重新申报")
            sys.exit(1)


if __name__ == "__main__":
    main()
