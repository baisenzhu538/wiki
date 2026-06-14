#!/usr/bin/env python3
"""Inbox watcher: detects new files in 00_inbox/ and dispatches to 王语嫣.

Add to crontab:
  */10 * * * * cd /mnt/c/Users/Administrator/Desktop/wiki && python3 kdo-tools/watch_inbox.py

When new files are found:
  1. Classify as P0/P1/P2
  2. Write dispatch file to 60_feedback/inbox-queue/
  3. 王语嫣's cron picks up and processes P0/P1
"""

import os, json, hashlib
from pathlib import Path
from datetime import datetime, timezone

ROOT = Path(__file__).resolve().parent.parent
INBOX = ROOT / "00_inbox"
STATE_FILE = ROOT / ".kdo" / "inbox_state.json"
QUEUE_DIR = ROOT / "60_feedback" / "inbox-queue"

# P0 keywords: 新域开荒、付费课程、客户录音、诊断访谈
P0_KEYWORDS = ["Truman", "月白", "纪浩", "半肥猫", "马易", "水水", "录音",
               "口述", "课程", "培训", "建模", "短剧", "药柜", "七件事",
               "招商", "访谈", "访谈", "诊断"]
# File extensions to watch
WATCH_EXTS = {".txt", ".md", ".json", ".pdf", ".docx", ".png", ".jpg"}


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
        dirs[:] = [d for d in dirs if not d.startswith(".")]
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
    """Write dispatch files for P0/P1 items, skip P2."""
    QUEUE_DIR.mkdir(parents=True, exist_ok=True)
    now = datetime.now(timezone.utc).strftime("%Y%m%d_%H%M%S")

    p0_items = [d for d in discoveries if d["priority"] == "P0"]
    p2_items = [d for d in discoveries if d["priority"] == "P2"]

    if p0_items:
        dispatch_file = QUEUE_DIR / f"dispatch_{now}.md"
        lines = [
            "# Inbox Dispatch — 王语嫣处理\n",
            f"检测时间：{now}\n",
            "## P0 文件（需要质量门）\n",
            "| 文件 | 大小 | 类型 |",
            "|------|------|------|",
        ]
        for d in p0_items:
            lines.append(f"| {d['file']} | {d['size']}B | {d['ext']} |")
        lines.append(f"\n**动作**：执行六层交叉比对 → 高价值段落索引 → 标注 confidence → 输出到 60_feedback/diagnosis/\n")
        dispatch_file.write_text("\n".join(lines), encoding="utf-8")
        print(f"王语嫣: {len(p0_items)} P0 file(s) queued")

    if p2_items:
        for d in p2_items:
            print(f"老顽童(P2): {d['file']}")


if __name__ == "__main__":
    new_files = scan()
    if new_files:
        dispatch(new_files)
        print(f"Total: {len(new_files)} new/changed, {sum(1 for d in new_files if d['priority']=='P0')} P0, {sum(1 for d in new_files if d['priority']=='P2')} P2")
    # else: silent — no new files
