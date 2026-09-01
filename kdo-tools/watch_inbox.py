#!/usr/bin/env python3
"""Inbox watcher: detects new files in 00_inbox/ and dispatches to 王语嫣（质量门）.

调度（2026-08-19 迁移，原 WSL cron 因 WSL 不常驻失效）：
  Windows 计划任务 kdo-inbox-watch，每 10 分钟：
  "C:\\Program Files\\Python312\\python.exe" C:\\Users\\Administrator\\Desktop\\wiki\\kdo-tools\\watch_inbox.py

规则（2026-08-19 用户拍板）：**所有进入知识库的必须走质量门**——
  不再区分 P0/P2 路由（P2 曾直达老顽童 = 绕过质量门的旁路，已取消）。
  一律：dispatch → 王语嫣质量门/编排 → 任务单入队 → 老顽童生产 → 欧阳锋终审。
  _classify 的 P0/P2 标签仅作信息参考保留。

排除目录：wechat-collect（偶遇采集自有管线 wechat_promote.py 处理，避免重复派发）
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
TODOS_WANGYUYAN = ROOT / "90_control" / "todos" / "wangyuyan.md"
SILENT_START_HOUR, SILENT_END_HOUR = 22, 8  # [已废 #550] 时段静默常数保留兼容——判定切 on_duty 在岗制

import on_duty  # #550：在岗判定共享模块（conveyor_probe 同口径，单一判定源）
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

# #605（2026-09-02 王语嫣裁定）：dispatch 台账停发——17 份零签收，队列/收件箱监控
# 职能已由看门狗 v5（90_control/scripts/clock_watchdog.py：队列三段+gate 增量）覆盖；
# 保留 pending-cards 登记（update_orchestration_board）与王语嫣收件箱通知（_notify_inbox）。
DISPATCH_LEDGER_ENABLED = False


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
    return "P2"  # default P2——仅信息标签；2026-08-19 起所有素材一律走王语嫣质量门，无直达旁路


def scan() -> list[dict]:
    """Scan inbox for new/changed files. Returns list of new discoveries."""
    if not STATE_FILE.exists():
        STATE_FILE.parent.mkdir(parents=True, exist_ok=True)
        STATE_FILE.write_text("{}")

    state = json.loads(STATE_FILE.read_text(encoding="utf-8") or "{}")
    discoveries = []

    # #605（2026-09-02 王语嫣裁定）：目录树裁剪——只扫 00_inbox 顶层新素材 +
    # pending-cards/（Handle/_vlm_output/ocr_ingest 等大目录树出扫描面；
    # 全树递归曾产出单份 863KB/7908 行 dispatch，无人消费）
    scan_files = [p for p in INBOX.iterdir() if p.is_file()]
    pending_dir = INBOX / "pending-cards"
    if pending_dir.exists():
        scan_files += [p for p in pending_dir.rglob("*") if p.is_file()]

    for path in scan_files:
        fname = path.name
        ext = os.path.splitext(fname)[1].lower()
        if ext not in WATCH_EXTS:
            continue
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
    """写 dispatch 文件——2026-08-19 用户拍板：所有进入知识库的必须走质量门，
    取消 P2 直达老顽童的旁路。一律派给王语嫣（质量门+编排）；P0/P2 标签仅作信息参考。

    #605（2026-09-02 王语嫣裁定）：台账落盘下线（17 份零签收 + 单份可达 863KB），
    默认 DISPATCH_LEDGER_ENABLED=False；登记（看板）与通知职能保留不变。"""
    now = datetime.now(timezone.utc).strftime("%Y%m%d_%H%M%S")

    if not discoveries:
        return

    if DISPATCH_LEDGER_ENABLED:
        QUEUE_DIR.mkdir(parents=True, exist_ok=True)
        dispatch_file = QUEUE_DIR / f"dispatch_{now}.md"
        lines = [
            "# Inbox Dispatch\n",
            f"检测时间：{now}\n",
            "## 新素材（一律走王语嫣质量门——2026-08-19 起无例外）\n",
            "| 文件 | 参考优先级 | 大小 | 类型 |",
            "|------|------|------|------|",
        ]
        for d in discoveries:
            lines.append(f"| {d['file']} | {d['priority']} | {d['size']}B | {d['ext']} |")
        lines.append(f"\n**动作**：王语嫣诊断编排（六层交叉比对/质量门）→ 任务单入队 → 老顽童生产。任何素材不得绕过质量门直接产卡。\n")
        dispatch_file.write_text("\n".join(lines), encoding="utf-8")
        print(f"dispatched: {dispatch_file.name}（{len(discoveries)} 项 → 王语嫣质量门）")
    update_orchestration_board(discoveries)
    _notify_inbox(discoveries)


def _notify_inbox(discoveries: list[dict]):
    """#530：检测到→推王语嫣收件箱（编排触发器补推送通道——队列类事件全有推送，
    唯独编排触发器没有；08-25 词元经济素材躺看板 50 分钟实证）。

    幂等=scan() state 判重同键（discoveries 只含新文件，重跑天然不重复推）。
    静默口径（#550 老朱直令改版）：时段制已废——无 agent 在岗（事件库/L1 双信号判定，
    on_duty.py）才静默落盘带 🔕；有 agent 在岗一切照常。判定信号不可得=默认激活。
    """
    TODOS_WANGYUYAN.parent.mkdir(parents=True, exist_ok=True)
    if not TODOS_WANGYUYAN.exists():
        TODOS_WANGYUYAN.write_text("# 王语嫣待办\n\n", encoding="utf-8")
    now = datetime.now()
    # #550：时段静默 → 在岗判定（老朱直令）；判定异常=默认激活（宁可误激活不可误静默）
    try:
        _on, _why = on_duty.any_agent_on_duty()
    except Exception:
        _on, _why = True, "判定异常"
    silent = not _on
    n = len(discoveries)
    p0 = sum(1 for d in discoveries if d["priority"] == "P0")
    names = "、".join(Path(d["file"]).name for d in discoveries[:3])
    bell = "🔕" if silent else "📥"
    line = (f"- [{now.strftime('%Y-%m-%d %H:%M')}] {bell} 新素材 {n} 项（P0 {p0}）："
            f"{names}{'…' if n > 3 else ''}——请诊断编排（看板待编排段）\n")
    with TODOS_WANGYUYAN.open("a", encoding="utf-8") as f:
        f.write(line)
    print(f"{bell} 王语嫣收件箱已通知（{n} 项{'，无在岗静默落盘' if silent else ''}）")


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

    # 2026-08-31 看板瘦身护栏（老朱直令：token/上下文成本控制）：
    # 登记条目超 SOFT_CAP 时截断保留最新，整段迁入 archive 并留指针——防 state 重建后的全量重扫洪水（08-31 实证 7907 行/58万 tokens）
    SOFT_CAP = 120
    if len(items) > SOFT_CAP:
        overflow = items[:-SOFT_CAP]
        items = items[-SOFT_CAP:]
        arch_dir = PROD_QUEUE.parent / "archive"
        arch_dir.mkdir(exist_ok=True)
        arch_file = arch_dir / "inbox-pending-overflow.md"
        with open(arch_file, "a", encoding="utf-8") as af:
            af.write(f"\n## 溢出归档 {now}（{len(overflow)} 行）\n" + "\n".join(overflow) + "\n")
        print(f"📦 看板登记超 {SOFT_CAP} 行，{len(overflow)} 行溢出归档 → {arch_file.name}")

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
