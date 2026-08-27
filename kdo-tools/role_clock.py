#!/usr/bin/env python3
"""role_clock.py — 角色心跳调度器（#553，#525 四拆之二；设计稿 §2/§3）。

调度循环（schtasks 系统级 5 分钟节拍，不绑任何 CLI 会话）：
  查注册表（90_control/role-registry.json）→ 到点（pace）或有信号（pending_review 非空 →
  欧阳锋事件驱动即醒）→ 路由唤醒到 active 实例通道 → 写唤醒日志（.kdo/role-clock.log jsonl）。

唤醒语义统一层（设计稿 §3）：payload 统一文案，适配器薄壳：
  - cli/todos：90_control/todos/<role>.md 落盘（恒写——CLI 实例收件箱）
  - feishu：角色 webhook（复用 conveyor_probe._send_hook 加签通道）

红线（设计稿 §8）：只做唤醒路由无裁决权；活性判定失败→降级报警不自动切执行权；
误发>漏发；唤醒/降级全留日志（注意：唤醒日志走本地文件，不写胶囊事件层——
否则机器心跳把 on_duty 撑成常在岗，#550 判定失效）。

用法：
  python kdo-tools/role_clock.py run [--dry-run]     # 调度循环单拍（schtasks 调用）
  python kdo-tools/role_clock.py wake laowantong [--reason 验收]  # 手动唤醒（验收/调试用）
"""
import argparse
import json
import re
import sys
import time
from datetime import datetime
from pathlib import Path

# #568：GBK 控制台根治——stdout/stderr 统一 UTF-8（emoji/中文打印不再 UnicodeEncodeError；模式抄 watch_inbox.py）
if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")
if hasattr(sys.stderr, "reconfigure"):
    sys.stderr.reconfigure(encoding="utf-8", errors="replace")

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "90_control" / "scripts"))
sys.path.insert(0, str(ROOT / "kdo-tools"))

REGISTRY = ROOT / "90_control" / "role-registry.json"
STATE_FILE = ROOT / ".kdo" / "role-clock-state.json"
WAKE_LOG = ROOT / ".kdo" / "role-clock.log"
TODOS_DIR = ROOT / "90_control" / "todos"

WAKE_PAYLOAD = ("【叫醒】{role}：读 todos/{role}.md 未读段 + 看板名下状态"
                "（有任务按队列序施工；无任务报告待命）")

QUEUE_FILE = ROOT / "70_product" / "tasks" / "production-queue.md"
_REVIEW_LINE_RE = re.compile(
    r"^- #(\d+) (\S+)｜(\S+)｜提审 (\d{2})-(\d{2}) (\d{2}):(\d{2})")


def _pending_review_details(now: float | None = None) -> str:
    """#565 任务2：唤醒载荷附 REVIEW-PENDING 明细（单号+挂起时长+阻塞谁=任务属主）。

    挂起超 30min 升级 🚨 加急措辞。解析 production-queue.md REVIEW-PENDING 段
    （未划销行）；解析失败/为空=返回空串，载荷退回基础模板（不阻断唤醒）。
    """
    try:
        text = QUEUE_FILE.read_text(encoding="utf-8")
    except OSError:
        return ""
    m = re.search(r"<!-- REVIEW-PENDING-BEGIN[^>]*-->(.*?)<!-- REVIEW-PENDING-END",
                  text, re.S)
    if not m:
        return ""
    now_dt = datetime.fromtimestamp(now or time.time())
    items = []
    for ln in m.group(1).splitlines():
        ln = ln.strip()
        if ln.startswith("- ~~"):  # 已终审划销行
            continue
        mm = _REVIEW_LINE_RE.match(ln)
        if not mm:
            continue
        seq, _tid, assignee, mo, dd, hh, mi = mm.groups()
        try:
            submitted = datetime(now_dt.year, int(mo), int(dd), int(hh), int(mi))
        except ValueError:
            continue
        age_min = int((now_dt - submitted).total_seconds() // 60)
        if age_min < 0:  # 跨年/时钟异常的负年龄不当挂起
            age_min = 0
        items.append((seq, assignee, age_min))
    if not items:
        return ""
    worst = max(i[2] for i in items)
    detail = "；".join(f"#{s}（{a} 的单，挂审 {age}min）" for s, a, age in items)
    if worst > 30:
        return f"🚨 待终审挂起超 30min：{detail}"
    return f"待终审明细：{detail}"

# 事件驱动角色：pending_review 非空即醒（设计稿 §3 欧阳锋口径）；最小间隔防抖
EVENT_DRIVEN = {"ouyangfeng": {"signal": "pending_review", "min_interval_min": 10}}


def _load_json(path: Path, default):
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except Exception:
        return default


def _save_json(path: Path, data) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    tmp = path.with_suffix(".tmp")
    tmp.write_text(json.dumps(data, ensure_ascii=False, indent=2), encoding="utf-8")
    tmp.replace(path)


def _log_wake(role: str, reason: str, channels: list[str]) -> None:
    try:
        WAKE_LOG.parent.mkdir(parents=True, exist_ok=True)
        with WAKE_LOG.open("a", encoding="utf-8") as f:
            f.write(json.dumps({"ts": datetime.now().isoformat(timespec="seconds"),
                                "role": role, "reason": reason, "channels": channels},
                               ensure_ascii=False) + "\n")
    except OSError as e:
        print(f"⚠️ 唤醒日志写入失败: {e}", file=sys.stderr)


def _pending_review_exists() -> bool:
    try:
        from queue_gate import parse_queue
        return any(r["status"] == "pending_review" for r in parse_queue())
    except Exception:
        return False


def due_roles(now: float | None = None, registry: dict | None = None,
              state: dict | None = None) -> list[tuple[str, str]]:
    """到期角色清单：[(role, reason)]。pace 到点 OR 事件驱动信号命中。"""
    now = now or time.time()
    reg = registry if registry is not None else _load_json(REGISTRY, {})
    state = state if state is not None else _load_json(STATE_FILE, {})
    last_wake = state.get("last_wake", {})
    try:
        import role_registry as rr
        pace_map = rr.ROLE_PACE_MIN
        default_pace = rr.DEFAULT_PACE_MIN
    except Exception:
        pace_map, default_pace = {}, 30
    due = []
    pv_exists = None  # 惰性查一次
    for role, entry in reg.items():
        if not isinstance(entry, dict):
            continue
        lw = float(last_wake.get(role, 0))
        # 事件驱动优先
        ev = EVENT_DRIVEN.get(role)
        if ev:
            if pv_exists is None:
                pv_exists = _pending_review_exists()
            if pv_exists and now - lw >= ev["min_interval_min"] * 60:
                due.append((role, "事件驱动：有待终审"))
                continue
        pace = float(entry.get("wake_pace_min") or pace_map.get(role, default_pace))
        if now - lw >= pace * 60:
            due.append((role, f"到点（节奏 {pace:.0f}min）"))
    return due


def deliver(role: str, text: str, reason: str, entry: dict | None = None,
            dry_run: bool = False, feishu_by_hook: bool = False) -> list[str]:
    """统一层消息投递（#554 换轨落点）：todos 落盘 + feishu 适配。
    与 wake() 的固定模板不同——本函数投递调用方给定文本（🔔/⚖️/📥 emoji 契约不动）。
    feishu 通道二选一触发：feishu_by_hook=True（事件通知换轨：webhook 配置可得即推，
    通道不缩水原则）或 active 实例 channels 含 feishu（周期叫醒：按注册表面向实例路由）。
    返回实际触达通道列表。"""
    line = f"- [{datetime.now().strftime('%Y-%m-%d %H:%M')}] {text}（{reason}）\n"
    touched = []
    if not dry_run:
        todos = TODOS_DIR / f"{role}.md"
        TODOS_DIR.mkdir(parents=True, exist_ok=True)
        if not todos.exists():
            todos.write_text(f"# {role} 待办\n\n", encoding="utf-8")
        with todos.open("a", encoding="utf-8") as f:
            f.write(line)
    touched.append("todos")

    entry = entry or _load_json(REGISTRY, {}).get(role, {})
    active = entry.get("active")
    inst = next((i for i in entry.get("instances", []) if i.get("tool") == active), None)
    want_feishu = feishu_by_hook or (inst and "feishu" in (inst.get("channels") or []))
    if want_feishu:
        try:
            import conveyor_probe as cp
            hooks = cp._load_hooks()
            hook = hooks.get(role)
            if hook:
                ok = cp._send_hook(hook["url"], f"{text}（{reason}）", hook["key"])
                if ok:
                    touched.append("feishu")
        except Exception as e:
            print(f"⚠️ feishu 适配器失败（todos 已落，不阻断）: {e}", file=sys.stderr)
    _log_wake(role, reason, touched)
    return touched


def wake(role: str, reason: str, entry: dict | None = None, dry_run: bool = False) -> list[str]:
    """唤醒单角色：统一模板文案走 deliver（#554 后 wake=deliver 的模板特化）。
    #565：载荷附 REVIEW-PENDING 明细（有则挂尾，无则基础模板）。"""
    payload = WAKE_PAYLOAD.format(role=role)
    details = _pending_review_details()
    if details:
        payload = f"{payload}——{details}"
    return deliver(role, payload, reason, entry, dry_run)


def run(dry_run: bool = False, now: float | None = None) -> int:
    reg = _load_json(REGISTRY, {})
    if not reg:
        print("注册表为空——无角色可调度")
        return 0
    state = _load_json(STATE_FILE, {})
    due = due_roles(now=now, registry=reg, state=state)
    if not due:
        print("[role_clock] 无到期角色")
        return 0
    last_wake = state.setdefault("last_wake", {})
    ts = now or time.time()
    for role, reason in due:
        # 红线：活性判定失败（active 实例 stale）→ 降级报警不自动切执行权
        try:
            import role_registry as rr
            lv = rr.liveness(role, now=ts, reg=reg)
            if lv["registered"] and lv["all_dead"]:
                rr.check_liveness(now=ts)  # 全死自报（gate-blocked 通道），唤醒照发不误（误发>漏发）
        except Exception:
            pass
        touched = wake(role, reason, reg.get(role), dry_run=dry_run)
        print(f"⏰ 唤醒 {role}（{reason}）→ {touched}")
        if not dry_run:
            last_wake[role] = ts
    if not dry_run:
        _save_json(STATE_FILE, state)
    return 0


def main() -> int:
    p = argparse.ArgumentParser(description="角色心跳调度器（#553）")
    sub = p.add_subparsers(dest="cmd", required=True)
    pr = sub.add_parser("run", help="调度单拍")
    pr.add_argument("--dry-run", action="store_true")
    pw = sub.add_parser("wake", help="手动唤醒单角色")
    pw.add_argument("role")
    pw.add_argument("--reason", default="手动唤醒")
    args = p.parse_args()
    if args.cmd == "run":
        return run(dry_run=args.dry_run)
    if args.cmd == "wake":
        touched = wake(args.role, args.reason)
        print(f"⏰ 已唤醒 {args.role}（{args.reason}）→ {touched}")
        return 0
    return 1


if __name__ == "__main__":
    sys.exit(main())
