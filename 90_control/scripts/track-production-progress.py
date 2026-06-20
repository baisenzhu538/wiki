#!/usr/bin/env python3
"""
生产进度追踪器
读取任务清单 Markdown，解析各 Wave 的目标卡片 ID，
检查 30_wiki 下是否已有对应文件，计算各 Wave 和整体完成率。

用法：
    python 90_control/scripts/track-production-progress.py                              # 自动找最新任务文件
    python 90_control/scripts/track-production-progress.py --task <path-to-task-file>    # 指定任务文件
    python 90_control/scripts/track-production-progress.py --json                       # JSON 输出
    python 90_control/scripts/track-production-progress.py --missing                    # 仅列出未产出的卡片
"""

import argparse
import json
import re
import sys
from pathlib import Path
from datetime import datetime

VAULT_ROOT = Path(__file__).resolve().parent.parent.parent
TASKS_DIR = VAULT_ROOT / "60_feedback" / "tasks"
WIKI_CONCEPTS = VAULT_ROOT / "30_wiki" / "concepts"

# 匹配任务表格行中的卡片 ID：`card-id-here`
CARD_ID_RE = re.compile(r"`([a-z]+-[a-z]+-[a-z0-9-]+)`")

# 匹配 Wave 标题：## N、Wave N：
WAVE_HEADER_RE = re.compile(r"^#{2,4}\s*(?:[^#]*?Wave\s*(\d+)|[^#]*?第([一二三四五六七八九十]+)波)", re.IGNORECASE)

# 中文数字
CN_NUM = {"一": 1, "二": 2, "三": 3, "四": 4, "五": 5, "六": 6, "七": 7, "八": 8, "九": 9, "十": 10}


def find_latest_task():
    """在 tasks 目录找最新的任务清单文件"""
    if not TASKS_DIR.exists():
        return None
    task_files = sorted(TASKS_DIR.glob("task_*_调研专题*.md"), reverse=True)
    return task_files[0] if task_files else None


def parse_wave_number(header_text):
    """从标题文本解析 Wave 编号"""
    m = re.search(r"Wave\s*(\d+)", header_text, re.IGNORECASE)
    if m:
        return int(m.group(1))
    for cn, num in CN_NUM.items():
        if cn in header_text and ("Wave" in header_text or "波" in header_text):
            return num
    return None


def parse_task_file(task_path):
    """解析任务 Markdown 文件，提取各 Wave 的卡片 ID 列表"""
    text = task_path.read_text(encoding="utf-8")
    lines = text.splitlines()

    waves = {}
    current_wave = None
    current_section = None

    for line in lines:
        stripped = line.strip()

        # 检测 Wave 标题
        wave_match = re.search(r"Wave\s*(\d+)", stripped, re.IGNORECASE)
        if wave_match and stripped.startswith("#"):
            current_wave = int(wave_match.group(1))
            if current_wave not in waves:
                waves[current_wave] = {"title": stripped.lstrip("# "), "card_ids": [], "count": 0}
            current_section = "wave_header"
            continue

        # 检测章节标题（如 "### 3.1 清理 10 张旧卡"）
        if stripped.startswith("#") and current_wave is not None:
            current_section = stripped.lstrip("# ").strip()
            continue

        # 表格行：只看第一列（或第二列，如果第一列是序号）
        if stripped.startswith("|") and not stripped.startswith("|:") and not stripped.startswith("|---"):
            cells = [c.strip() for c in stripped.split("|")]
            # 跳过首尾空
            cells = [c for c in cells if c]
            if not cells:
                continue
            # 如果第一列是纯数字（序号），取第二列；否则取第一列
            target_cell_idx = 0
            if cells[0].isdigit() and len(cells) > 1:
                target_cell_idx = 1
            if target_cell_idx < len(cells):
                cid_match = CARD_ID_RE.search(cells[target_cell_idx])
                if cid_match and current_wave is not None:
                    cid = cid_match.group(1)
                    if not cid.startswith("src_") and not cid.startswith("http"):
                        if cid not in waves[current_wave]["card_ids"]:
                            waves[current_wave]["card_ids"].append(cid)
                            waves[current_wave]["count"] += 1
            continue

        # 非表格行：提取所有卡片 ID（用于列表、段落中的引用）
        ids_in_line = CARD_ID_RE.findall(line)
        for cid in ids_in_line:
            if cid.startswith("src_") or cid.startswith("http"):
                continue
            if current_wave is not None:
                if cid not in waves[current_wave]["card_ids"]:
                    waves[current_wave]["card_ids"].append(cid)
                    waves[current_wave]["count"] += 1

    return waves


def check_card_exists(card_id):
    """检查卡片文件是否存在于 30_wiki 下"""
    wiki_dir = VAULT_ROOT / "30_wiki"
    # 直接匹配文件名
    direct = WIKI_CONCEPTS / f"{card_id}.md"
    if direct.exists():
        return direct.relative_to(VAULT_ROOT).as_posix()

    # 搜索整个 wiki
    for fp in wiki_dir.rglob(f"{card_id}.md"):
        if "_archive" not in fp.parts:
            return fp.relative_to(VAULT_ROOT).as_posix()
    return None


def compute_progress(waves):
    """计算各 Wave 和整体的完成进度"""
    wave_results = {}
    total_target = 0
    total_done = 0

    for wave_num in sorted(waves.keys()):
        w = waves[wave_num]
        card_ids = w["card_ids"]
        done = []
        pending = []
        for cid in card_ids:
            path = check_card_exists(cid)
            if path:
                done.append((cid, path))
            else:
                pending.append(cid)

        wave_results[wave_num] = {
            "title": w["title"],
            "target": len(card_ids),
            "done": len(done),
            "done_ids": done,
            "pending": pending,
            "pct": round(len(done) / len(card_ids) * 100, 1) if card_ids else 0,
        }
        total_target += len(card_ids)
        total_done += len(done)

    return {
        "waves": wave_results,
        "total_target": total_target,
        "total_done": total_done,
        "total_pct": round(total_done / total_target * 100, 1) if total_target else 0,
        "scanned_at": datetime.now().isoformat(),
    }


def generate_report(progress, task_path):
    """生成 Markdown 进度报告"""
    lines = [
        "# 生产进度报告",
        "",
        f"**任务文件**：`{task_path.as_posix()}`",
        f"**扫描时间**：{progress['scanned_at']}",
        f"**整体进度**：{progress['total_done']}/{progress['total_target']} ({progress['total_pct']}%)",
        "",
        "```",
        f"{'█' * int(progress['total_pct'] / 5)}{'░' * (20 - int(progress['total_pct'] / 5))} {progress['total_pct']}%",
        "```",
        "",
        "---",
        "",
    ]

    for wave_num in sorted(progress["waves"].keys()):
        w = progress["waves"][wave_num]
        bar_len = int(w["pct"] / 5) if w["target"] else 0
        bar = "█" * bar_len + "░" * (20 - bar_len)

        lines.append(f"## Wave {wave_num}：{w['title']}")
        lines.append(f"**进度**：{w['done']}/{w['target']} ({w['pct']}%)")
        lines.append(f"```\n{bar} {w['pct']}%\n```")
        lines.append("")

        if w["pending"]:
            lines.append(f"### 待产 ({len(w['pending'])} 张)")
            lines.append("")
            for cid in w["pending"]:
                lines.append(f"- [ ] `{cid}`")
            lines.append("")

        if w["done_ids"]:
            lines.append(f"### 已产 ({len(w['done_ids'])} 张)")
            lines.append("")
            for cid, path in w["done_ids"]:
                lines.append(f"- [x] `{cid}` → `{path}`")
            lines.append("")

    lines.extend([
        "---",
        "",
        f"*生成：track-production-progress.py · {Path(__file__).name}*",
    ])

    return "\n".join(lines)


def main():
    parser = argparse.ArgumentParser(description="生产进度追踪器")
    parser.add_argument("--task", help="任务清单 Markdown 文件路径")
    parser.add_argument("--json", action="store_true", help="JSON 输出")
    parser.add_argument("--missing", action="store_true", help="仅列出未产出的卡片 ID")
    args = parser.parse_args()

    task_path = Path(args.task) if args.task else find_latest_task()
    if task_path is None:
        print("错误：未找到任务清单文件。请用 --task 指定。", file=sys.stderr)
        sys.exit(2)
    if not task_path.is_absolute():
        task_path = VAULT_ROOT / task_path

    waves = parse_task_file(task_path)
    progress = compute_progress(waves)

    if args.json:
        print(json.dumps(progress, ensure_ascii=False, indent=2))
    elif args.missing:
        for wave_num in sorted(progress["waves"].keys()):
            w = progress["waves"][wave_num]
            for cid in w["pending"]:
                print(cid)
    else:
        report = generate_report(progress, task_path)
        print(report)


if __name__ == "__main__":
    main()
