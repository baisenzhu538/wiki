#!/usr/bin/env python3
"""kdo_memory_root.py — KDO-memory 数据盘定位器（#690 E 盘迁移+便携基建盘）。

守卫 2（盘符漂移防护）+ 便携化要求 1（自定位不锁盘符）的落地组件：
脚本一律经本模块取 KDO-memory 根路径，不裸写盘符。

定位顺序：
1. 环境变量 KDO_MEMORY_ROOT（应急/测试覆盖；指向目录需存在才采用）
2. 扫描 A-Z 各盘根 <X>:\\KDO-memory\\.disk-id 标记文件（便携盘自定位，
   盘符在异机漂移成 F:/G: 也能找到；命中多个时取盘符序最先者）
3. 遗留回退 D:\\KDO-memory（迁移过渡期兼容——命中回退即写
   90_control/gate-blocked.log 告警（#472 格式），不静默失败（守卫 1）

CLI（供 .cmd/.bat for /f 取用）：
  python kdo-tools/kdo_memory_root.py          # 打印根路径，找不到退出码 1
  python kdo-tools/kdo_memory_root.py --check  # 打印定位来源诊断（env/marker/fallback/none）

红线口径：回退 D 盘保生产不断拍（#690 零中断），但告警必写——回退≠正常态。
"""

from __future__ import annotations

import argparse
import json
import os
import string
import sys
from datetime import datetime
from pathlib import Path

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")

WIKI = Path(__file__).resolve().parent.parent
GATE_LOG = WIKI / "90_control" / "gate-blocked.log"
MARKER_REL = Path("KDO-memory") / ".disk-id"
LEGACY_ROOT = Path("D:/KDO-memory")
ALARM_DEDUP_HOURS = 1  # 同一告警 1h 内不重复写（探针 10min 一拍，防刷爆 gate 日志）


def _gate_block(reason: str, detail: str) -> None:
    """#472 格式落 gate-blocked.log；同 reason 1h 内去重。"""
    try:
        if GATE_LOG.exists():
            cutoff = datetime.now().timestamp() - ALARM_DEDUP_HOURS * 3600
            for line in GATE_LOG.read_text(encoding="utf-8", errors="replace").splitlines()[-200:]:
                parts = line.split("｜")
                if len(parts) >= 3 and parts[1] == "kdo-memory-root" and parts[2] == reason:
                    try:
                        if datetime.strptime(parts[0], "%Y-%m-%d %H:%M:%S").timestamp() > cutoff:
                            return  # 去重：近期已报
                    except ValueError:
                        pass
        ts = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        with open(GATE_LOG, "a", encoding="utf-8") as f:
            f.write(f"{ts}｜kdo-memory-root｜{reason}｜{detail[:200]}｜kdo_memory_root\n")
    except OSError:
        pass  # 告警通道本身失败不拖垮调用方


def _scan_marker_drives() -> Path | None:
    """扫描 A-Z 盘根找 .disk-id 标记。"""
    for letter in string.ascii_uppercase:
        marker = Path(f"{letter}:/") / MARKER_REL
        try:
            if marker.is_file():
                return marker.parent
        except OSError:
            continue
    return None


def find_memory_root(with_source: bool = False):
    """返回 KDO-memory 根路径（with_source=True 时返回 (path|None, source)）。

    source ∈ env / marker / fallback / none。fallback 与 env 失效均写告警。
    """
    env = os.environ.get("KDO_MEMORY_ROOT", "").strip()
    if env:
        p = Path(env)
        if p.is_dir():
            return (p, "env") if with_source else p
        _gate_block("env-override-invalid",
                    f"KDO_MEMORY_ROOT={env} 指向不存在目录，忽略并继续定位")

    hit = _scan_marker_drives()
    if hit is not None:
        return (hit, "marker") if with_source else hit

    if LEGACY_ROOT.is_dir():
        _gate_block("marker-missing-fallback-D",
                    "全盘未找到 KDO-memory\\.disk-id 标记（E 盘缺位？），回退遗留 D:\\KDO-memory 保生产——请检查便携盘在位")
        return (LEGACY_ROOT, "fallback") if with_source else LEGACY_ROOT

    _gate_block("memory-root-not-found",
                "KDO-memory 定位失败：env 未设/失效 + 全盘无 .disk-id 标记 + D:\\KDO-memory 不存在")
    return (None, "none") if with_source else None


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--check", action="store_true", help="打印定位来源诊断")
    ap.add_argument("--json", action="store_true", help="JSON 输出")
    args = ap.parse_args()

    root, source = find_memory_root(with_source=True)
    if args.json:
        print(json.dumps({"root": str(root) if root else None, "source": source},
                         ensure_ascii=False))
    elif args.check:
        print(f"source={source} root={root if root else '(none)'}")
    else:
        if root is not None:
            print(root)
    return 0 if root is not None else 1


if __name__ == "__main__":
    raise SystemExit(main())
