#!/usr/bin/env python3
"""存量 draft 超龄巡检（#380 王语嫣 2026-08-20 拍板 A 方案配套）。

扫描 30_wiki/ 内 status=draft 且创建超 24h 未审的卡，输出报警清单。
定位：只报警不自动改——接收方是王语嫣（编排门禁：逐张判定退回/留存，
值得留的才送欧阳锋终审）。覆盖存量 646 张 draft + 例外监控。

退出码恒 0（advisory）：存量 draft 是常态，不该让 health-check 整体 FAIL。
清单默认只显示前 20 条（防 646 张刷屏），全量用 --json 或 --all。

用法：
    python 90_control/scripts/check-draft-aging.py            # 人类可读摘要
    python 90_control/scripts/check-draft-aging.py --all      # 全量清单
    python 90_control/scripts/check-draft-aging.py --json     # JSON 输出
"""

import argparse
import json
import sys
from datetime import datetime, timezone
from pathlib import Path

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")

VAULT_ROOT = Path(__file__).resolve().parent.parent.parent
WIKI_DIR = VAULT_ROOT / "30_wiki"
AGING_HOURS = 24
# 与 search_index.build 同口径：系统文件不算知识卡
SKIP_NAMES = {"index.md", "log.md", "contradictions.md"}


def _parse_created_at(raw: str, path: Path) -> datetime:
    """created_at 格式不一（ISO / 'YYYY-MM-DD HH:MM' / 日期），解析失败回退文件 mtime。"""
    raw = raw.strip().strip('"').strip("'")
    for fmt in ("%Y-%m-%dT%H:%M:%S%z", "%Y-%m-%d %H:%M", "%Y-%m-%d"):
        try:
            dt = datetime.strptime(raw[:25], fmt) if fmt.endswith("%z") else datetime.strptime(raw[:len(fmt) + 2], fmt)
            if dt.tzinfo is None:
                dt = dt.replace(tzinfo=timezone.utc)
            return dt
        except ValueError:
            continue
    try:
        return datetime.fromisoformat(raw.replace("Z", "+00:00"))
    except ValueError:
        return datetime.fromtimestamp(path.stat().st_mtime, tz=timezone.utc)


def scan() -> list[dict]:
    now = datetime.now(timezone.utc)
    stale: list[dict] = []
    for path in sorted(WIKI_DIR.rglob("*.md")):
        if path.name in SKIP_NAMES or "decisions" in str(path):
            continue
        try:
            head = path.read_text(encoding="utf-8", errors="replace")[:3000]
        except OSError:
            continue
        if not head.startswith("---"):
            continue
        fm_end = head.find("\n---", 3)
        if fm_end == -1:
            continue
        fm_text = head[3:fm_end]
        # 轻量解析：只取 status/created_at/title 三个键（不引 yaml 依赖全量解析）
        fields = {}
        for line in fm_text.splitlines():
            if ":" in line and not line.startswith((" ", "-")):
                k, _, v = line.partition(":")
                fields[k.strip()] = v.strip()
        if fields.get("status", "").strip('"').strip("'") != "draft":
            continue
        created = _parse_created_at(fields.get("created_at", ""), path)
        age_h = (now - created).total_seconds() / 3600
        if age_h <= AGING_HOURS:
            continue
        stale.append({
            "path": str(path.relative_to(VAULT_ROOT)).replace("\\", "/"),
            "title": fields.get("title", "").strip('"').strip("'") or path.stem,
            "created_at": created.strftime("%Y-%m-%d %H:%M"),
            "age_hours": round(age_h, 1),
        })
    stale.sort(key=lambda x: -x["age_hours"])
    return stale


def main():
    ap = argparse.ArgumentParser(description="存量 draft>24h 未审巡检（#380）")
    ap.add_argument("--json", action="store_true")
    ap.add_argument("--all", action="store_true", help="显示全量清单（默认只显示前 20 条）")
    args = ap.parse_args()

    stale = scan()

    if args.json:
        print(json.dumps({"aging_hours": AGING_HOURS, "count": len(stale), "cards": stale},
                         ensure_ascii=False, indent=2))
        return 0

    print(f"扫描 30_wiki: {len(stale)} 张 draft 超 {AGING_HOURS}h 未审")
    if stale:
        print(f"接收方=王语嫣（编排门禁）：逐张判定 退回重提取 / 留存送欧阳锋终审")
        print("-" * 60)
        shown = stale if args.all else stale[:20]
        for c in shown:
            print(f"  [{c['age_hours']:.0f}h] {c['path']}")
            print(f"        {c['title']}（创建于 {c['created_at']}）")
        if not args.all and len(stale) > 20:
            print(f"  ... 其余 {len(stale) - 20} 张省略，--all 或 --json 看全量")
    return 0  # advisory：只报警，不阻断


if __name__ == "__main__":
    sys.exit(main())
