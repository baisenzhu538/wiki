#!/usr/bin/env python3
"""
广冷电子项目归档脚本 — 按三分类原则清理项目文件。

用法：
    python archive_project.py <项目路径> [选项]

选项：
    --dry-run       只预览，不执行（默认）
    --execute       实际执行
    --verbose       详细日志
"""

import argparse
import shutil
import hashlib
import json
import logging
import sys
import time
from datetime import datetime
from pathlib import Path

logging.basicConfig(level=logging.INFO, format="%(message)s")
log = logging.getLogger("archive")

# 可删除的扩展名（编译中间产物）
DELETE_EXTS = {".o", ".crf", ".d", ".htm", ".dep", ".iex", ".bak", ".lst", ".lnp", ".sct"}

# 可删除的文件名模式
DELETE_PATTERNS = {"JLinkLog.txt", "*.uvgui.*", "*.uvopt", "*.uvoptx"}

# 基准线扩展名（保留）
BASELINE_EXTS = {".sch", ".brd", ".json", ".csv", ".xlsx", ".c", ".h", ".hex", ".bin", ".pdf"}


def md5_of(path: Path) -> str:
    """计算文件 MD5，大文件分块读取。"""
    h = hashlib.md5()
    with open(path, "rb") as f:
        for chunk in iter(lambda: f.read(65536), b""):
            h.update(chunk)
    return h.hexdigest()


def scan_directory(root: Path) -> dict:
    """扫描目录，返回文件清单和统计。"""
    files = []
    total_size = 0
    delete_candidates = []
    duplicate_candidates = {}

    for p in root.rglob("*"):
        if not p.is_file():
            continue
        if any(part.startswith(".") for part in p.parts):
            continue  # 跳过隐藏目录

        ext = p.suffix.lower()
        size = p.stat().st_size
        total_size += size

        entry = {
            "path": str(p.relative_to(root)),
            "ext": ext,
            "size": size,
            "mtime": datetime.fromtimestamp(p.stat().st_mtime).isoformat(),
        }

        # 检测可删除的编译中间产物
        if ext in DELETE_EXTS:
            entry["action"] = "delete"
            delete_candidates.append(entry)
            continue

        # 检测 KEIL 临时文件
        if "uvgui" in p.name or p.name in {"JLinkLog.txt"}:
            entry["action"] = "delete"
            delete_candidates.append(entry)
            continue

        # 检测重复文件（按文件名分组）
        if ext in BASELINE_EXTS:
            key = p.name
            if key not in duplicate_candidates:
                duplicate_candidates[key] = []
            duplicate_candidates[key].append(entry)

        files.append(entry)

    # 标记重复文件
    for key, entries in duplicate_candidates.items():
        if len(entries) > 1:
            # 按修改时间排序，保留最新的
            entries.sort(key=lambda e: e["mtime"], reverse=True)
            for e in entries[1:]:
                e["action"] = "duplicate"
                delete_candidates.append(e)

    return {
        "total_files": len(files),
        "total_size": total_size,
        "delete_candidates": delete_candidates,
        "delete_size": sum(e["size"] for e in delete_candidates),
    }


def execute_cleanup(root: Path, candidates: list, dry_run: bool = True):
    """执行清理。"""
    if dry_run:
        log.info(f"[DRY-RUN] 将删除 {len(candidates)} 个文件，释放空间")
        for c in candidates[:10]:
            log.info(f"  🗑 {c['path']} ({c.get('action', '')})")
        if len(candidates) > 10:
            log.info(f"  ... 及另外 {len(candidates)-10} 个文件")
        return

    log.info(f"执行清理 {len(candidates)} 个文件...")
    deleted = 0
    for c in candidates:
        p = root / c["path"]
        try:
            p.unlink()
            deleted += 1
        except Exception as e:
            log.warning(f"  删除失败: {c['path']} — {e}")

    log.info(f"已删除 {deleted}/{len(candidates)} 个文件")


def main():
    parser = argparse.ArgumentParser(description="电子工程项目归档脚本")
    parser.add_argument("path", help="项目根目录路径")
    parser.add_argument("--dry-run", action="store_true", default=True, help="只预览不执行")
    parser.add_argument("--execute", action="store_true", help="实际执行")
    parser.add_argument("--verbose", action="store_true", help="详细输出")
    args = parser.parse_args()

    root = Path(args.path)
    if not root.is_dir():
        log.error(f"路径不存在: {root}")
        return 1

    if args.verbose:
        log.setLevel(logging.DEBUG)

    # 扫描
    log.info(f"扫描: {root}")
    t0 = time.time()
    result = scan_directory(root)
    elapsed = time.time() - t0
    log.info(f"扫描完成 ({elapsed:.1f}s)")

    # 输出统计
    log.info(f"\n总文件数: {result['total_files']}")
    log.info(f"总大小: {result['total_size'] / 1024 / 1024:.1f} MB")
    log.info(f"可删除: {len(result['delete_candidates'])} 个文件, "
             f"{result['delete_size'] / 1024 / 1024:.1f} MB")

    # 执行清理
    dry_run = not args.execute
    execute_cleanup(root, result["delete_candidates"], dry_run=dry_run)

    # 输出报告
    report = {
        "project": root.name,
        "scan_time": datetime.now().isoformat(),
        "summary": {
            "total_files": result["total_files"],
            "total_size_mb": round(result["total_size"] / 1024 / 1024, 1),
            "deleted_files": len(result["delete_candidates"]),
            "deleted_size_mb": round(result["delete_size"] / 1024 / 1024, 1),
        },
    }
    report_path = root / "_archive" / "06_Reports" / "cleanup_report.json"
    report_path.parent.mkdir(parents=True, exist_ok=True)
    report_path.write_text(json.dumps(report, indent=2, ensure_ascii=False), encoding="utf-8")
    log.info(f"\n报告已生成: {report_path}")

    return 0


if __name__ == "__main__":
    sys.exit(main())
