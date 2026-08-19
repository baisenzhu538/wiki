#!/usr/bin/env python3
"""Inbox watcher: detects new files in 00_inbox/ and dispatches to 王语嫣/老顽童.

调度（2026-08-19 迁移，原 WSL cron 因 WSL 不常驻失效）：
  Windows 计划任务 kdo-inbox-watch，每 10 分钟：
  "C:\\Program Files\\Python312\\python.exe" C:\\Users\\Administrator\\Desktop\\wiki\\kdo-tools\\watch_inbox.py

When new files are found:
  1. Classify as P0/P2
  2. Write dispatch file to 60_feedback/inbox-queue/（P0 王语嫣处理；P2 老顽童处理——
     P2 也落盘，原先只 print 到 stdout 无人消费 = 静默丢失）
  3. 排除目录：wechat-collect（偶遇采集自有管线 wechat_promote.py 处理，避免重复派发）
"""

import os, json, hashlib
import sys
if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")
if hasattr(sys.stderr, "reconfigure"):
    sys.stderr.reconfigure(encoding="utf-8", errors="replace")
from pathlib import Path
from datetime import datetime, timezone

ROOT = Path(__file__).resolve().parent.parent
INBOX = ROOT / "00_inbox"
STATE_FILE = ROOT / ".kdo" / "inbox_state.json"
QUEUE_DIR = ROOT / "60_feedback" / "inbox-queue"
PROD_QUEUE = ROOT / "70_product" / "tasks" / "production-queue.md"
BOARD_BEGIN = "<!-- INBOX-PENDING-BEGIN（watch_inbox 自动维护，勿手改） -->"
BOARD_END = "<!-- INBOX-PENDING-END -->"

# P0 keywords: 新域开荒、付费课程、客户录音、诊断访谈
P0_KEYWORDS = ["Truman", "月白", "纪浩", "半肥猫", "马易", "水水", "录音",
               "口述", "课程", "培训", "建模", "短剧", "药柜", "七件事",
               "招商", "访谈", "访谈", "诊断"]
# File extensions to watch
WATCH_EXTS = {".txt", ".md", ".json", ".pdf", ".docx", ".png", ".jpg"}
# 已有独立自动化管线处理的目录，不再重复派发
EXCLUDE_DIRS = {"wechat-collect"}


def _hash_file(path: Path) -> str:
    """Cheap file identity: size + mtime."""
    try:
        stat = path.stat()
        return hashlib.md5(f"{path.name}:{stat.st_size}:{stat.st_mtime}".encode()).hexdigest()
    except OSError:
        return ""


def _classify(name: str) -> str:
    """Classify file priority based on name and parent directory."""
    name_lower = name.lower()
    parent = Path(name).parent.name.lower() if "/" in name else ""
    combined = name_lower + " " + parent
    for kw in P0_KEYWORDS:
        if kw.lower() in combined:
            return "P0"
    return "P2"  # default to P2 (老顽童直接处理)


def scan() -> list[dict]:
    """Scan inbox for new/changed files. Returns list of new discoveries."""
    if not STATE_FILE.exists():
        STATE_FILE.parent.mkdir(parents=True, exist_ok=True)
        STATE_FILE.write_text("{}")

    state = json.loads(STATE_FILE.read_text(encoding="utf-8") or "{}")
    discoveries = []

    for root, dirs, files in os.walk(INBOX):
        dirs[:] = [d for d in dirs if not d.startswith(".") and d not in EXCLUDE_DIRS]
        for fname in files:
            ext = os.path.splitext(fname)[1].lower()
            if ext not in WATCH_EXTS:
                continue
            path = Path(root) / fname
            file_hash = _hash_file(path)
            key = str(path.relative_to(ROOT))
            if state.get(key) != file_hash:
                priority = _classify(fname)
                discoveries.append({
                    "file": key,
                    "priority": priority,
                    "size": path.stat().st_size,
                    "ext": ext,
                    "detected_at": datetime.now(timezone.utc).isoformat(),
                })
                state[key] = file_hash

    STATE_FILE.write_text(json.dumps(state, indent=2, ensure_ascii=False), encoding="utf-8")
    return discoveries


def dispatch(discoveries: list[dict]):
    """写 dispatch 文件：P0 → 王语嫣（质量门），P2 → 老顽童（直接处理）。两级都落盘。"""
    QUEUE_DIR.mkdir(parents=True, exist_ok=True)
    now = datetime.now(timezone.utc).strftime("%Y%m%d_%H%M%S")

    p0_items = [d for d in discoveries if d["priority"] == "P0"]
    p2_items = [d for d in discoveries if d["priority"] == "P2"]
    if not (p0_items or p2_items):
        return

    dispatch_file = QUEUE_DIR / f"dispatch_{now}.md"
    lines = [
        "# Inbox Dispatch\n",
        f"检测时间：{now}\n",
    ]
    if p0_items:
        lines += [
            "## P0 文件（王语嫣处理·需要质量门）\n",
            "| 文件 | 大小 | 类型 |",
            "|------|------|------|",
        ]
        for d in p0_items:
            lines.append(f"| {d['file']} | {d['size']}B | {d['ext']} |")
        lines.append(f"\n**动作**：执行六层交叉比对 → 高价值段落索引 → 标注 confidence → 输出到 60_feedback/diagnosis/\n")
    if p2_items:
        lines += [
            "## P2 文件（老顽童处理·直接消化）\n",
            "| 文件 | 大小 | 类型 |",
            "|------|------|------|",
        ]
        for d in p2_items:
            lines.append(f"| {d['file']} | {d['size']}B | {d['ext']} |")
        lines.append("")
    dispatch_file.write_text("\n".join(lines), encoding="utf-8")
    print(f"dispatched: {dispatch_file.name}（P0={len(p0_items)} P2={len(p2_items)}）")
    update_orchestration_board(p0_items + p2_items)


def update_orchestration_board(discoveries: list[dict]):
    """把待编排素材写入 production-queue.md 的专管 section（2026-08-19 机制补丁）。

    断链实证：dispatch 写进 60_feedback/inbox-queue/ 抽屉目录，王语嫣启动步骤不含
    检查该目录 → 素材"转了存、存了忘"（Live86 逐字稿事件）。她维护看板必读
    production-queue.md，所以把待编排清单写进该文件的标记 section。

    设计约束：
    - 条目用列表（非表格行），queue_transition 的 parse_queue 不会误读
    - 整块标记 section 重写（幂等），不碰任务表——状态机零干扰
    - 路径级去重；她编排完一个就划掉一行（或清空 section）
    """
    if not PROD_QUEUE.exists() or not discoveries:
        return
    text = PROD_QUEUE.read_text(encoding="utf-8")

    # 读现有条目（路径级去重）
    items: list[str] = []
    known: set[str] = set()
    if BOARD_BEGIN in text and BOARD_END in text:
        block = text.split(BOARD_BEGIN)[1].split(BOARD_END)[0]
        for line in block.splitlines():
            if line.startswith("- "):
                items.append(line)
                # 条目格式：- path｜P0/P2｜size｜检测到 ……（首段即路径）
                known.add(line[2:].split("｜")[0].strip())

    now = datetime.now(timezone.utc).strftime("%m-%d %H:%M")
    added = 0
    for d in discoveries:
        fpath = d["file"].replace("\\", "/")
        if fpath in known:
            continue
        items.append(f"- {fpath}｜{d['priority']}｜{d['size']}B｜检测到 {now}｜待王语嫣编排")
        known.add(fpath)
        added += 1
    if not added and BOARD_BEGIN in text:
        return  # 无新增且 section 已存在——不重写

    board = [
        BOARD_BEGIN, "",
        "## 📥 待编排（inbox 新素材，watch_inbox 自动登记）", "",
        "> 王语嫣维护看板时处理：诊断 → 写任务单 → 入队后把对应行划掉。编排规则不变，这里只解决「没人被通知」。",
        "",
    ] + items + ["", BOARD_END]

    if BOARD_BEGIN in text:
        new_text = text.split(BOARD_BEGIN)[0] + "\n".join(board) + text.split(BOARD_END)[1]
    else:
        new_text = text.rstrip() + "\n\n" + "\n".join(board) + "\n"
    PROD_QUEUE.write_text(new_text, encoding="utf-8")
    print(f"📥 待编排看板更新: +{added}（累计 {len(items)} 条）→ production-queue.md")


if __name__ == "__main__":
    new_files = scan()
    if new_files:
        dispatch(new_files)
        print(f"Total: {len(new_files)} new/changed, {sum(1 for d in new_files if d['priority']=='P0')} P0, {sum(1 for d in new_files if d['priority']=='P2')} P2")
    # else: silent — no new files
