#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
#671 graph index 覆盖率探针（检索失明第三层根因的防复发门）。

对照两边：
  A. 30_wiki 各子目录实际卡数（复用 kdo.commands.graph._collect_all_wiki_pages
     ——与构建脚本同一套收集逻辑，不会漂移）
  B. .kdo/graph_state.json path_map（title -> path）

缺口=该入索引而没进的卡。>0 即报警（#472 gate-blocked 格式），两圈同拦：
  - 子目录级：目录在盘上有卡、索引里 0 张或少数（#671 实证形态：dark-knowledges 0/332）
  - 标题撞车级：path_map 按 title 键，同 title 后者覆盖前者（#671 实证形态：
    dk-research-triangulation-stop-rule 被 skills 同名卡顶掉，dk 少 1 张）

每次运行追加一行到 logs/graph-index-coverage.log（探针心跳）；异常另写
90_control/gate-blocked.log。Exit 0 = 覆盖完整，1 = 有缺口。

Called by: kdo-tools/run-kdo-health.cmd（计划任务 kdo-health-daily 每日 02:07）
Standalone: python graph-index-coverage-probe.py [--json]
"""
import argparse
import json
import sys
from collections import Counter
from datetime import datetime
from pathlib import Path

sys.stdout.reconfigure(encoding="utf-8", errors="replace")

VAULT = Path(__file__).resolve().parents[2]
STATE_FILE = VAULT / ".kdo" / "graph_state.json"
GATE_LOG = VAULT / "90_control" / "gate-blocked.log"
HEARTBEAT_LOG = VAULT / "logs" / "graph-index-coverage.log"
TASK_TAG = "graph-index-coverage"


def gate_block(reason: str, detail: str):
    ts = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    line = f"{ts}｜{TASK_TAG}｜{reason}｜{detail[:200]}｜graph-index-coverage-probe\n"
    try:
        with open(GATE_LOG, "a", encoding="utf-8") as f:
            f.write(line)
        print(f"[GATE-BLOCKED] {reason}: {detail}")
    except OSError as e:
        print(f"[GATE-BLOCKED-WRITE-FAIL] {e}: {reason}: {detail}")


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--json", action="store_true", help="machine-readable output")
    args = ap.parse_args()

    from kdo.commands.graph import _collect_all_wiki_pages

    pages = _collect_all_wiki_pages(VAULT)
    disk_by_dir = Counter(Path(p["path"]).parent.name for p in pages)
    disk_paths = {p["path"] for p in pages}

    anomalies: list[str] = []
    detail_lines: list[str] = []
    per_dir: dict[str, int] = {}
    idx_by_dir: Counter = Counter()
    path_map: dict = {}

    if not STATE_FILE.exists():
        anomalies.append("索引状态文件缺失（graph_state.json 不存在——kdo graph rebuild 未跑过？）")
    else:
        state = json.loads(STATE_FILE.read_text(encoding="utf-8"))
        path_map = state.get("path_map", {})
        if not path_map:
            anomalies.append("path_map 为空（索引疑似未构建）")
        for v in path_map.values():
            idx_by_dir[Path(v).parent.name] += 1

    # 子目录级缺口：盘上有卡、索引没进全
    for d in sorted(disk_by_dir):
        gap = disk_by_dir[d] - idx_by_dir[d]
        per_dir[d] = gap
        detail_lines.append(f"{d}: disk={disk_by_dir[d]} indexed={idx_by_dir[d]} gap={gap}")
        if gap > 0:
            if idx_by_dir[d] == 0:
                anomalies.append(f"30_wiki/{d} 全目录未入索引（0/{disk_by_dir[d]}——#671 同型检索失明）")
            else:
                anomalies.append(f"30_wiki/{d} 部分卡未入索引（{idx_by_dir[d]}/{disk_by_dir[d]}）")
    for d in sorted(idx_by_dir):
        if d not in disk_by_dir:
            anomalies.append(f"30_wiki/{d} 索引有 {idx_by_dir[d]} 张但盘上已无卡（陈旧索引，需 kdo graph rebuild --full）")

    # 标题撞车级缺口：收集到的卡有 path 不在 path_map 值集合里
    missing_by_title = [p for p in pages if p["path"] not in set(path_map.values())]
    if missing_by_title:
        names = ", ".join(Path(p["path"]).name for p in missing_by_title[:5])
        more = f" 等 {len(missing_by_title)} 张" if len(missing_by_title) > 5 else ""
        anomalies.append(
            f"标题撞车致 {len(missing_by_title)} 张卡被 path_map 覆盖丢失：{names}{more}"
            "（同名 title 后者覆盖前者——撞名卡需改名，改卡走内容侧流程）"
        )
        detail_lines.append("title-collision victims: " + names)

    ok = not anomalies
    ts = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    summary = f"coverage {'OK' if ok else 'GAP'} pages={len(pages)} path_map={len(path_map)}"
    try:
        with open(HEARTBEAT_LOG, "a", encoding="utf-8") as f:
            f.write(f"{ts} {summary}\n")
    except OSError:
        pass

    if args.json:
        print(json.dumps({
            "ts": ts, "ok": ok, "pages": len(pages), "path_map": len(path_map),
            "gap_by_dir": per_dir,
            "anomalies": anomalies,
        }, ensure_ascii=False, indent=2))
    else:
        print(summary)
        for l in detail_lines:
            print("  ", l)
        for a in anomalies:
            gate_block("graph index 覆盖缺口", a)

    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
