#!/usr/bin/env python3
"""conveyor_probe.py — 传送带探针（#421）：队列状态变化检出 + PROPOSAL-PENDING 自动登记 + 飞书通知。

单扫描器纪律：一次扫描事件驱动「检出 → 登记 → 通知」，禁止第二套扫描器（E021/E028 同族教训）。
边界硬编码：只通知/只登记，不领取/不裁决/不流转（代码层无 claim/review/complete 能力）。
契约：`90_control/conveyor-probes-contract.md`（X-1 拍板成文）。

调度：Windows 计划任务 kdo-conveyor-probe（每 10 分钟，与 kdo-inbox-watch 同频）。
通道：飞书群机器人 webhook，配置 `kdo-tools/.feishu_webhooks.json`（URL 不进 git）；缺失 → dry-run 打印。

用法：
  python kdo-tools/conveyor_probe.py            # 常规扫描（检出→登记→通知）
  python kdo-tools/conveyor_probe.py --dry-run  # 登记照做，通知只打印不发送
  python kdo-tools/conveyor_probe.py --json     # 结构化输出（供调度/测试）
"""

import argparse
import base64
import hashlib
import hmac
import json
import sys
import time
import urllib.request
import yaml
from datetime import datetime
from pathlib import Path

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")

ROOT = Path(__file__).resolve().parent.parent
DIAG_DIR = ROOT / "60_feedback" / "diagnosis"
TASK_DIR = ROOT / "60_feedback" / "tasks"  # F-036 第七信号：终审意见落点扫描
QUEUE_FILE = ROOT / "70_product" / "tasks" / "production-queue.md"
STATE_FILE = ROOT / ".kdo" / "conveyor_state.json"
HOOKS_FILE = Path(__file__).resolve().parent / ".feishu_webhooks.json"
FAIL_LOG = Path(__file__).resolve().parent / ".conveyor_failures.log"

# #458 第四探针：六角色 friction-log 增量扫描面（+共享文件兼容历史习惯）
RETRO_ROOT = Path.home() / "Desktop" / "agent复盘"
FRICTION_ROLES = ["ouyangfeng", "huangyaoshi", "wangyuyan", "laowantong", "hongqigong", "duanwangye", "fengqingyang"]
SHARED_FRICTION = Path(__file__).resolve().parent.parent / ".agent" / "friction-log.md"
# #460 第五探针：门禁拦截日志（queue_transition 自动落盘，机器自报——零依赖自觉）
GATE_BLOCKED_LOG = Path(__file__).resolve().parent.parent / "90_control" / "gate-blocked.log"
FORCE_LEDGER = Path(__file__).resolve().parent.parent / "90_control" / "force-exceptions.log"  # #537 豁免留痕

PROPOSAL_BEGIN = "<!-- PROPOSAL-PENDING-BEGIN（自动登记：conveyor_probe.py；勿手改——王语嫣复核后划掉） -->"
PROPOSAL_BEGIN_OLD = "<!-- PROPOSAL-PENDING-BEGIN（建议书作者自登，王语嫣复核后划掉） -->"  # 迁移兼容旧段头
PROPOSAL_END = "<!-- PROPOSAL-PENDING-END -->"
SILENT_START_HOUR, SILENT_END_HOUR = 22, 8  # 夜间静默 22:00–08:00（登记照常，通知不发）

sys.path.insert(0, str(ROOT / "90_control" / "scripts"))
from queue_gate import parse_queue  # noqa: E402   # 唯一真相源读口，探针零写路径
from queue_lock import QueueLock  # noqa: E402   # #505：队列文件写点与 queue_transition 同锁
sys.path.insert(0, str(ROOT / "kdo-tools"))
import memory_capsule as mc  # noqa: E402   # #511：friction 事件层写入（log_event_safe 失败可见不阻断）

import functools  # noqa: E402


def _with_queue_lock(fn):
    """#505：队列文件写函数统一套 QueueLock（与 queue_transition 同锁名 production-queue）。

    消除 probe×transition read-modify-write 竞态（E050 反向变体/#488 行错位同族）：
    probe 读到旧版 → transition 改状态 → probe 写回旧版+段改动 = 状态变更被吞。
    装饰器注入而非改函数体：diff 最小，既有测试以函数对象调用不受影响。
    """
    @functools.wraps(fn)
    def wrapper(*args, **kwargs):
        with QueueLock("production-queue"):
            return fn(*args, **kwargs)
    return wrapper


def _load_state() -> dict:
    if STATE_FILE.exists():
        try:
            return json.loads(STATE_FILE.read_text(encoding="utf-8"))
        except Exception:
            pass
    return {"last_review_pending": [], "last_queued": [], "notified": []}


def _save_state(state: dict) -> None:
    STATE_FILE.write_text(json.dumps(state, ensure_ascii=False, indent=2), encoding="utf-8")


# ── 信号 1/2：队列状态 diff（相对上次快照）───────────────────

def _sha256(text: str) -> str:
    import hashlib as _hl
    return _hl.sha256(text.encode("utf-8")).hexdigest()


def _msg_key(role: str, text: str) -> str:
    """幂等键：角色 + 消息主体（去 emoji 前缀）。"""
    return f"{role}:{text.split('：')[1] if '：' in text else text}"


# #443：可领取通知按 assignee 路由——实例名/角色名映射表（E020 双口径），新增实例在此登记防再撞
ASSIGNEE_ROLE = {
    "huangyaoshi": "huangyaoshi",
    "laowantong": "laowantong",
    "hermes": "laowantong",      # 老顽童 Hermes CLI 实例
    "kimi": "laowantong",        # 老顽童 Kimi CLI 实例
    "wangyuyan": "wangyuyan",
    "ouyangfeng": "ouyangfeng",
    "fengqingyang": "laowantong",  # 观察者无独立通知通道，回落 laowantong 群
    "": "laowantong",            # 未知/缺省 assignee → 回落 laowantong（保守默认，不静默丢）
}


def _route_queued(rows: list) -> dict[str, list]:
    """把 new_queued 任务按 assignee 路由分桶：{role: [(task_id, seq)]}。"""
    buckets: dict[str, list] = {}
    for task_id, seq, assignee in rows:
        role = ASSIGNEE_ROLE.get(str(assignee).strip(), "laowantong")  # 未知实例名同样回落
        buckets.setdefault(role, []).append((task_id, seq))
    return buckets


def _queue_signal(state: dict) -> dict:
    """返回 [(task_id, seq)] 对（seq=队列序号）。#462 新增流转完成信号（治编排者盲区）。"""
    rows = parse_queue(QUEUE_FILE)
    review = [(r["task_id"], r["seq"]) for r in rows if r["status"] == "pending_review"]
    queued = [(r["task_id"], r["seq"], r.get("assignee", "")) for r in rows if r["status"] == "queued"]
    reviewed = [(r["task_id"], r["seq"], r.get("assignee", "")) for r in rows if r["status"] == "reviewed"]
    last_review = state.get("last_review_pending", [])
    last_queued = state.get("last_queued", [])
    last_reviewed = state.get("last_reviewed", [])
    new_review = [(t, s) for t, s in review if t not in last_review]
    new_queued = [(t, s, a) for t, s, a in queued if t not in last_queued]
    # #462：流转完成信号——new_reviewed（新增终审通过）/ new_failback（pending_review→queued 退回）
    # #521 R1：reviewed 携带 assignee（PASS 按生产者路由，复用 #443 ASSIGNEE_ROLE）
    new_reviewed = [(t, s, a) for t, s, a in reviewed if t not in last_reviewed]
    now_pending = {t for t, _ in review}
    new_failback = [(t, s) for t, s in review if False]  # 占位（failback 需对比上次 pending 快照）
    # failback = 上次 pending_review 里的任务，现在既不在 pending 也不在 reviewed（=退回 queued）
    failback_candidates = [t for t in last_review if t not in now_pending and t not in {x for x, _, _ in reviewed}]
    new_failback = [(t, s, a) for t, s, a in queued if t in failback_candidates]
    state["last_review_pending"], state["last_queued"] = [t for t, _ in review], [t for t, _, _ in queued]
    state["last_reviewed"] = [t for t, _, _ in reviewed]
    return {
        "new_review": new_review, "new_queued": new_queued,
        "new_reviewed": new_reviewed, "new_failback": new_failback,
    }


# ── 信号 3：建议书三元组检出 + PROPOSAL-PENDING 登记（幂等）──

def _scan_proposals() -> list[str]:
    """diagnosis/ 内命中三元组（audience: 王语嫣 + status: pending_orchestration）的文件名。
    yaml.safe_load 结构化解析（E017），与 #425 指标 8 同源口径。"""
    hits = []
    for fp in sorted(DIAG_DIR.glob("*.md")):
        try:
            fm = yaml.safe_load(fp.read_text(encoding="utf-8").split("---", 2)[1])
        except Exception:
            continue
        if not isinstance(fm, dict):
            continue
        if _is_triple_hit(fm):  # #506：三元组判定单点化（与 near-miss 同源，防双轨漂移）
            hits.append(fp.name)
    return hits


# ── #506 建议书 near-miss 报警：疑似建议书但三元组不完整 → 显式报警，不静默 continue ──

# 终态白名单：这些 status 不算"待编排漂移"（已裁定/已闭环件不回看，防历史件噪声）
_PROPOSAL_TERMINAL_STATUS = {"resolved", "reviewed", "closed", "done", "orchestrated", "cancelled"}

# #506 向前生效（file-flow-protocol §9 同款）：只对生效日及之后新建的建议书报警，
# 存量历史 status 杂多（draft/completed/resolved/pending_laozhu…）既往不咎——
# 否则首轮即 53 条历史噪声洪泛（2026-08-25 全量干跑实测）。
_NEAR_MISS_EFFECTIVE_DATE = "20260825"

import re as _re  # noqa: E402

_DIAG_DATE_RE = _re.compile(r"^diag_(\d{8})_")


def _diag_file_date(name: str) -> str:
    """从文件名提取 diag_YYYYMMDD_ 日期（无日期返回 ''——调用方按'生效后'处理，畸形名正是漂移高发区）。"""
    m = _DIAG_DATE_RE.match(name)
    return m.group(1) if m else ""


def _is_triple_hit(fm: dict) -> bool:
    """三元组命中判定（与 _scan_proposals 同口径，单点定义防漂移）。"""
    return ("王语嫣" in str(fm.get("audience", ""))
            and str(fm.get("status", "")).strip() == "pending_orchestration")


def _proposal_near_miss_reason(fm: dict) -> str | None:
    """疑似建议书但三元组不完整 → 返回原因；非建议书形态/终态件 → None（不报警）。

    单轨口径（王语嫣 08-24 裁）：type: proposal / status: pending_orchestration / audience: 王语嫣。
    `to:` 与 `status: pending` 已 deprecated——命中即漂移（08-24 风清扬 4 份实证同型）。
    """
    aud = str(fm.get("audience", "")).strip()
    to = str(fm.get("to", "")).strip()
    status = str(fm.get("status", "")).strip()
    typ = str(fm.get("type", "")).strip()
    if to:
        return "用了 deprecated 字段 to:（单轨=audience: 王语嫣）"
    if status.lower() in _PROPOSAL_TERMINAL_STATUS:
        return None  # 终态件不回看（type: proposal + status: resolved 等已闭环形态）
    if typ == "proposal":
        missing = []
        if not aud:
            missing.append("缺 audience")
        if status != "pending_orchestration":
            missing.append(f"status={status or '缺失'}（应 pending_orchestration）")
        if missing:
            return "type: proposal 但三元组不完整：" + "、".join(missing)
        return None
    if (aud and status and status != "pending_orchestration"
            and status.lower() not in _PROPOSAL_TERMINAL_STATUS):
        return f"有 audience 但 status={status}（应 pending_orchestration）"
    if (status and status != "pending_orchestration"
            and status.lower() not in _PROPOSAL_TERMINAL_STATUS
            and ("pending" in status.lower() or "待" in status)):
        return f"status={status} 疑似待编排但非 pending_orchestration"
    return None


def _scan_proposal_near_miss(state: dict, effective_date: str | None = None) -> list[str]:
    """扫描 diagnosis/ 三元组漂移件：stderr 显式报警 + 新件落 gate-blocked 式记录（state 幂等）。

    #506：登记链路不动（只通知只登记纪律）——本函数只让「写错 frontmatter」当场可见
    （E052 同族根治：机制依赖契约，契约破时不再静默失效）。落 GATE_BLOCKED_LOG 后由
    第五探针同事件拾取登记 PROPOSAL-PENDING + 通知王语嫣（闭环零新通道）。
    effective_date：向前生效截止日（默认 _NEAR_MISS_EFFECTIVE_DATE；测试/回放可注入）。
    """
    eff = effective_date or _NEAR_MISS_EFFECTIVE_DATE
    misses = []
    seen = set(state.get("near_miss_seen", []))
    new_seen = False
    try:
        log_f = GATE_BLOCKED_LOG.open("a", encoding="utf-8")
    except OSError:
        log_f = None
    for fp in sorted(DIAG_DIR.glob("*.md")):
        fdate = _diag_file_date(fp.name)
        try:
            fm = yaml.safe_load(fp.read_text(encoding="utf-8").split("---", 2)[1])
        except Exception:
            continue
        if not isinstance(fm, dict) or _is_triple_hit(fm):
            continue  # 正常登记件由 _scan_proposals 收，不重复报警
        if not fdate:
            # 无日期文件名：回落 frontmatter created_at/updated_at 判定新旧（proposal-self-learning-cron 实证）
            for k in ("created_at", "updated_at"):
                m = _re.search(r"(\d{4})-(\d{2})-(\d{2})", str(fm.get(k, "")))
                if m:
                    fdate = "".join(m.groups())
                    break
        if fdate and fdate < eff:
            continue  # 向前生效：存量历史件既往不咎（#506 噪声洪泛根治）
        reason = _proposal_near_miss_reason(fm)
        if not reason:
            continue
        misses.append(f"{fp.name}｜{reason}")
        print(f"⚠️ [near-miss] {fp.name} 疑似建议书但三元组不完整：{reason}"
              f"——探针不登记（#506：frontmatter 漂移当场可见，不再静默 continue）",
              file=sys.stderr)
        key = _sha256(f"{fp.name}｜{reason}")
        if key not in seen and log_f is not None:
            ts = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            log_f.write(f"{ts}｜{fp.name}｜near-miss-三元组（#506）｜{reason[:100]}｜conveyor_probe\n")
            seen.add(key)
            new_seen = True
    if log_f is not None:
        log_f.close()
    if new_seen:
        state["near_miss_seen"] = sorted(seen)[-500:]
    return misses


def _reject_duplicate_doc_ids(hits: list[str]) -> list[str]:
    """#450：登记口 doc_id 查重——同 doc_id 重复的建议书拒绝登记（登记即冻结，撞号=E045）。

    复用 file-flow-check.find_duplicate_doc_ids（单一真相源，禁副本）；加载失败降级
    只警告不阻断登记（探针不能因 lint 模块问题挂掉）。
    """
    try:
        import importlib.util
        _spec = importlib.util.spec_from_file_location(
            "file_flow_check", Path(__file__).resolve().parent / "file-flow-check.py")
        ffc = importlib.util.module_from_spec(_spec)
        _spec.loader.exec_module(ffc)
        dups = ffc.find_duplicate_doc_ids(DIAG_DIR)  # 传探针扫描面（测试可注入）
    except Exception as e:
        print(f"⚠️ [conveyor_probe] doc_id 查重模块加载失败，跳过查重: {e}", file=sys.stderr)
        return hits
    rejected = []
    for name in list(hits):
        fp = DIAG_DIR / name
        try:
            doc_id = yaml.safe_load(fp.read_text(encoding="utf-8").split("---", 2)[1]).get("doc_id")
        except Exception:
            continue
        if doc_id and doc_id in dups:
            rejected.append(f"{name} (doc_id={doc_id})")
            hits.remove(name)
    if rejected:
        print(f"⛔ [conveyor_probe] doc_id 重复拒绝登记: {'; '.join(rejected)}（E045 撞号，先订正再落盘）",
              file=sys.stderr)
    return hits


def _update_proposal_board(hits: list[str]) -> list[str]:
    """命中且未在段内的 → 自动写入 PROPOSAL-PENDING 段（路径级幂等）。
    对称 watch_inbox.update_orchestration_board：重写标记段，不碰任务表（状态机零干扰）。"""
    if not hits or not QUEUE_FILE.exists():
        return []
    hits = _reject_duplicate_doc_ids(hits)  # #450：登记即冻结，撞号当场拒绝
    if not hits:
        return []
    text = QUEUE_FILE.read_text(encoding="utf-8")
    if PROPOSAL_BEGIN_OLD in text:  # 迁移：旧"作者自登"段头升级为"自动维护"标注（2026-08-22 #421）
        text = text.replace(PROPOSAL_BEGIN_OLD, PROPOSAL_BEGIN)
        QUEUE_FILE.write_text(text, encoding="utf-8")
    items, known = [], set()
    if PROPOSAL_BEGIN in text and PROPOSAL_END in text:
        block = text.split(PROPOSAL_BEGIN)[1].split(PROPOSAL_END)[0]
        for line in block.splitlines():
            if line.startswith("- "):
                # 保留全部现有行（历史多行合法——同一文件可有多次独立裁定记录，2026-08-22 实证误删）
                items.append(line)
                # 去重键归一化：去划线标记 + 去路径前缀（旧行完整路径 vs 新行文件名）——只用于防新增
                entry = line[2:].lstrip("~~").strip()
                name = entry.split("｜")[0].strip().replace("60_feedback/diagnosis/", "")
                known.add(name)
    now = datetime.now().strftime("%m-%d %H:%M")
    added = []
    for name in hits:
        if name in known:
            continue
        items.append(f"- {name}｜{now}｜待王语嫣复核裁定")
        known.add(name)
        added.append(name)
    if not added and PROPOSAL_BEGIN in text:
        return []
    board = [
        PROPOSAL_BEGIN, "",
        "## 📬 PROPOSAL-PENDING（建议书到达，conveyor_probe.py 自动登记）", "",
        "> 王语嫣复核立项后划掉该行（流程不变）。勿手改段结构——重跑会整块重写。",
        "",
    ] + items + ["", PROPOSAL_END]
    if PROPOSAL_BEGIN in text:
        new_text = text.split(PROPOSAL_BEGIN)[0] + "\n".join(board) + text.split(PROPOSAL_END)[1]
    else:
        new_text = text.rstrip() + "\n\n" + "\n".join(board) + "\n"
    QUEUE_FILE.write_text(new_text, encoding="utf-8")
    return added


# ── 信号 4（#458）：friction 增量扫描——一行式记录自动上浮，不依赖建议书格式 ──

def _friction_files() -> list[Path]:
    files = [RETRO_ROOT / role / "friction-log.md" for role in FRICTION_ROLES]
    if SHARED_FRICTION.exists():
        files.append(SHARED_FRICTION)
    return [f for f in files if f.exists()]


def _update_proposal_board_friction(new_lines: list[str]) -> None:
    """#458：friction 线索登记 PROPOSAL-PENDING 段（[friction] 类型，幂等——按行文本去重）。"""
    if not new_lines or not QUEUE_FILE.exists():
        return
    text = QUEUE_FILE.read_text(encoding="utf-8")
    items, known = [], set()
    if PROPOSAL_BEGIN in text and PROPOSAL_END in text:
        block = text.split(PROPOSAL_BEGIN)[1].split(PROPOSAL_END)[0]
        for ln in block.splitlines():
            if ln.startswith("- "):
                items.append(ln)
                known.add(ln[2:].split("｜")[0].strip())
    now = datetime.now().strftime("%m-%d %H:%M")
    added = 0
    for ln in new_lines:
        marker = f"[friction] {ln.split('｜')[0].strip()}"
        if marker in known:
            continue
        # ln 已含 [角色] 前缀 + 完整一行（避免 marker 与内容重复显示，2026-08-23 狗粮修正）
        items.append(f"- {marker}｜{now}｜待王语嫣复核处置｜{ln}")
        known.add(marker)
        added += 1
    if not added and PROPOSAL_BEGIN in text:
        return
    board = [
        PROPOSAL_BEGIN, "",
        "## 📬 PROPOSAL-PENDING（建议书到达，conveyor_probe.py 自动登记）", "",
        "> 王语嫣复核立项后划掉该行（流程不变）。勿手改段结构——重跑会整块重写。",
        "",
    ] + items + ["", PROPOSAL_END]
    if PROPOSAL_BEGIN in text:
        new_text = text.split(PROPOSAL_BEGIN)[0] + "\n".join(board) + text.split(PROPOSAL_END)[1]
    else:
        new_text = text.rstrip() + "\n\n" + "\n".join(board) + "\n"
    QUEUE_FILE.write_text(new_text, encoding="utf-8")
    print(f"🩹 friction 线索登记: +{added}（累计 {len(items)} 条）→ PROPOSAL-PENDING")


def _scan_friction(state: dict) -> list[str]:
    """扫 friction-log 增量：state 记每文件已见行（行文本 hash）。返回新行（含来源角色标识）。"""
    seen = state.setdefault("friction_seen", {})
    new_lines = []
    for fp in _friction_files():
        try:
            text = fp.read_text(encoding="utf-8", errors="ignore")
        except OSError:
            continue
        key = str(fp)
        known = set(seen.get(key, []))
        fresh = []
        for ln in text.splitlines():
            line = ln.strip()
            if not line or line.startswith(("#", "|", ">")):
                continue  # 表头/注释/表分隔行不算
            if "｜" not in line and "|" not in line:
                continue  # 一行式格式校验（含分隔符才算记录）
            h = _sha256(line)
            if h not in known:
                known.add(h)
                fresh.append(line)
        seen[key] = sorted(known)[-500:]  # 防膨胀
        for ln in fresh:
            role = fp.parent.name if fp.parent != SHARED_FRICTION.parent else "shared"
            new_lines.append(f"[{role}] {ln}")
    return new_lines


# ── #537 第七信号：总账登记机器核查（基础设施单 reviewed 时矩阵未同步→提醒）──

# 基础设施面清单（初版宁窄勿宽，误报比漏报贵；扩充走后续单）
INFRA_WATCH = [
    "kdo-tools/conveyor_probe.py",
    "kdo-tools/watch_inbox.py",
    "90_control/scripts/queue_transition.py",
    "kdo-tools/generate-dashboard.py",
]
MATRIX_FILE = "90_control/notification-coverage-matrix.md"


def _matrix_sync_check(task_id: str, seq: str, root: Path) -> str | None:
    """基础设施单 reviewed 时核查矩阵同步。返回问题文案（None=通过/不适用）。

    口径：任务单 code_files 触及 INFRA_WATCH → 该单**功能 commit**（非流转 chore）
    须同改矩阵；frontmatter `matrix_exempt: true` → 跳过+豁免留痕（#444 台账同款）。
    机器只查「登没登」（存在性），不判「登得对不对」（#433 同哲学）。

    #537 改判 FAIL 双 bug 修复（欧阳锋 08-26 自我纠错附证）：
    ①窗口口径——流转 commit（chore(queue)/vault backup）必然插队把功能 commit 挤出
    窗口，改查「该单的功能笔」（流转/备份笔剔除后取近 3 笔，log 窗口放宽 10 笔再滤）；
    ②seq 从调用点元组传入（task_id 不含序号，split 推导恒错成「#task」）。
    """
    fp = TASK_DIR / f"{task_id}.md"
    if not fp.exists():
        return None
    try:
        import yaml as _yaml
        fm = _yaml.safe_load(fp.read_text(encoding="utf-8").split("---", 2)[1]) or {}
    except Exception:
        return None
    if fm.get("matrix_exempt") is True:
        return "EXEMPT"
    code_files = fm.get("code_files") or []
    if isinstance(code_files, str):
        code_files = [code_files]
    touched = [c for c in map(str, code_files) if c in INFRA_WATCH]
    if not touched:
        return None
    try:
        import subprocess as _sp
        lines = _sp.run(
            ["git", "-C", str(root), "log", "-n", "10", "--format=%H%x1f%s",
             "--", f"60_feedback/tasks/{task_id}.md"],
            capture_output=True, text=True, timeout=15,
            encoding="utf-8", errors="replace").stdout.splitlines()
        # 流转/备份 commit 剔除（只碰状态字段，与功能交付无关）
        functional = [ln.split("\x1f")[0] for ln in lines
                      if ln.strip() and not ln.split("\x1f", 1)[1].startswith(("chore(queue)", "vault backup"))]
        # 逐功能 commit 查全量文件清单（pathspec 过滤会连名单一起过滤——须两段查）
        names = []
        for h in functional[:3]:
            names += _sp.run(
                ["git", "-C", str(root), "diff-tree", "--no-commit-id", "--name-only", "-r", h],
                capture_output=True, text=True, timeout=15,
                encoding="utf-8", errors="replace").stdout.split()
    except Exception:
        return None  # git 异常 fail-open
    if functional and MATRIX_FILE not in names:
        return (f"⛔ 总账未同步：#{seq} 触碰基础设施"
                f"（{Path(touched[0]).name}）但 notification-coverage-matrix 未同改——"
                f"终审暂缓闭环，请核查（§3.19/#537；纯重构请在任务单标 matrix_exempt: true 并注明理由）")
    return None


def _escalate_near_miss(state: dict, misses: list[str], dry_run: bool, silent: bool) -> None:
    """#536：near-miss 超期升级推送——同一文件 ≥3 轮（≈30 分钟）仍未修正 → 推王语嫣收件箱。

    - state 记账：near_miss_rounds（轮数）/near_miss_first_seen（首次检出 ts）/
      near_miss_escalated（幂等：同文件同理由不重复推）
    - 修正消项：不再违例的 key 出账（三元组补齐或转终态后自动消，不重复推）
    - 夜间静默：near-miss 非终审类——静默期跳过，轮数照计，天亮后首个非静默拍补发
    """
    rounds = state.get("near_miss_rounds", {})
    first_seen = state.get("near_miss_first_seen", {})
    escalated = set(state.get("near_miss_escalated", []))
    current = {}
    for m in misses:
        key = _sha256(m)
        fname, _, reason = m.partition("｜")
        rounds[key] = rounds.get(key, 0) + 1
        first_seen.setdefault(key, datetime.now().strftime("%Y-%m-%d %H:%M"))
        current[key] = (fname, reason)
    for key in list(rounds):  # 修正消项：不再违例即出账
        if key not in current:
            rounds.pop(key)
            first_seen.pop(key, None)
    fired = [(k, *v) for k, v in current.items() if rounds[k] >= 3 and k not in escalated]
    if fired and not dry_run and not silent:
        for key, fname, reason in fired:
            _append_role_todo(
                "wangyuyan",
                f"⚠️ near-miss 超期升级：{fname} 三元组违例已 {rounds[key]} 轮未修正"
                f"（首检出 {first_seen[key]}；{reason[:60]}）——请捞处置（#536）")
            escalated.add(key)
            print(f"📤 near-miss 升级推送: {fname}（{rounds[key]} 轮未修正）")
    elif fired and silent:
        print(f"🔕 near-miss 升级 {len(fired)} 件 defer 天亮补发（轮数照计）")
    state["near_miss_rounds"] = rounds
    state["near_miss_first_seen"] = first_seen
    state["near_miss_escalated"] = sorted(escalated)[-200:]


def _scan_issue_no_disposition(state: dict, new_reviewed: list) -> list[str]:
    """F-036 第七信号兜底：新终审意见书含 🟠/🟡 但无落点 → 提醒欧阳锋补建议书。

    判定复用 queue_gate.check_issue_disposition（共享真相源，探针边界=不 import
    queue_transition——无流转能力）；state 去重（已提醒过的不重复）。"""
    try:
        sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "90_control" / "scripts"))
        from queue_gate import check_issue_disposition
    except Exception as e:
        print(f"⚠️ [conveyor_probe] F-036 判定模块加载失败，跳过: {e}", file=sys.stderr)
        return []
    notified = set(state.get("issue_disposition_notified", []))
    hits = []
    for task_id, _seq, _assignee in new_reviewed:
        if task_id in notified:
            continue
        fp = TASK_DIR / f"{task_id}.md"
        if not fp.exists():
            continue
        body = fp.read_text(encoding="utf-8", errors="ignore")
        idx = body.find("## 终审记录")
        if idx == -1:
            continue
        nxt = body.find("\n## ", idx + 1)
        opinion = body[idx:nxt] if nxt > 0 else body[idx:]
        ok, _msg = check_issue_disposition(opinion)
        if not ok:
            hits.append(task_id)
            notified.add(task_id)
    state["issue_disposition_notified"] = sorted(notified)
    return hits


def _scan_gate_blocked(state: dict) -> list[str]:
    """#460 第五探针：gate-blocked.log 增量扫描（行 hash 幂等）——门禁拦截自动上浮，零依赖 agent 自觉。"""
    if not GATE_BLOCKED_LOG.exists():
        return []
    seen = state.setdefault("gate_seen", [])
    known = set(seen)
    new_lines = []
    try:
        for ln in GATE_BLOCKED_LOG.read_text(encoding="utf-8", errors="ignore").splitlines():
            line = ln.strip()
            if not line or "｜" not in line:
                continue
            h = _sha256(line)
            if h not in known:
                known.add(h)
                new_lines.append(line)
    except OSError:
        return []
    state["gate_seen"] = sorted(known)[-500:]
    return new_lines


def _update_proposal_board_gate(new_lines: list[str]) -> None:
    """#460：门禁拦截登记 PROPOSAL-PENDING（[gate-blocked] 类型，幂等）。"""
    if not new_lines or not QUEUE_FILE.exists():
        return
    text = QUEUE_FILE.read_text(encoding="utf-8")
    items, known = [], set()
    if PROPOSAL_BEGIN in text and PROPOSAL_END in text:
        block = text.split(PROPOSAL_BEGIN)[1].split(PROPOSAL_END)[0]
        for ln in block.splitlines():
            if ln.startswith("- "):
                items.append(ln)
                known.add(ln[2:].split("｜")[0].strip())
    now = datetime.now().strftime("%m-%d %H:%M")
    added = 0
    for ln in new_lines:
        marker = f"[gate-blocked] {ln.split('｜')[1].strip()}"
        if marker in known:
            continue
        items.append(f"- {marker}｜{now}｜待王语嫣复核处置｜{ln}")
        known.add(marker)
        added += 1
    if not added and PROPOSAL_BEGIN in text:
        return
    board = [
        PROPOSAL_BEGIN, "",
        "## 📬 PROPOSAL-PENDING（建议书到达，conveyor_probe.py 自动登记）", "",
        "> 王语嫣复核立项后划掉该行（流程不变）。勿手改段结构——重跑会整块重写。",
        "",
    ] + items + ["", PROPOSAL_END]
    if PROPOSAL_BEGIN in text:
        new_text = text.split(PROPOSAL_BEGIN)[0] + "\n".join(board) + text.split(PROPOSAL_END)[1]
    else:
        new_text = text.rstrip() + "\n\n" + "\n".join(board) + "\n"
    QUEUE_FILE.write_text(new_text, encoding="utf-8")
    print(f"⛔ gate-blocked 登记: +{added} → PROPOSAL-PENDING")


# #505：队列文件 4 个写点（3 个写函数）统一过 QueueLock——与 queue_transition 同锁，
# 并发写一族的工具层兜底（约定见 90_control/file-flow-protocol-amend-shared-file-write.md）。
_update_proposal_board = _with_queue_lock(_update_proposal_board)
_update_proposal_board_friction = _with_queue_lock(_update_proposal_board_friction)
_update_proposal_board_gate = _with_queue_lock(_update_proposal_board_gate)


# ── 通知：飞书群机器人 webhook（配置驱动；缺失 → dry-run 打印）──

def _load_hooks() -> dict:
    """配置格式：{"角色": {"url": "...", "key": "..."} | "角色": "<url>"（无签名兼容）}。"""
    if HOOKS_FILE.exists():
        try:
            cfg = json.loads(HOOKS_FILE.read_text(encoding="utf-8"))
            hooks = {}
            for role, v in cfg.items():
                if isinstance(v, str) and v:
                    hooks[role] = {"url": v, "key": None}
                elif isinstance(v, dict) and v.get("url"):
                    hooks[role] = {"url": v["url"], "key": v.get("key")}
            return hooks
        except Exception:
            pass
    return {}


def _feishu_sign(ts: str, key: str) -> str:
    """飞书群机器人加签（官方算法）：string_to_sign = f'{ts}\\n{key}'，整体作为 HMAC 密钥、消息为空 → base64。

    2026-08-23 实测修正：原实现（key=密钥, msg=ts\\n密钥）被飞书拒（code 19021 sign match fail）。
    官方示例：hmac.new(string_to_sign.encode(), digestmod=sha256)——即 key=string_to_sign。
    """
    string_to_sign = f"{ts}\n{key}"
    digest = hmac.new(string_to_sign.encode("utf-8"), digestmod=hashlib.sha256).digest()
    return base64.b64encode(digest).decode("utf-8")


TODOS_DIR = Path(__file__).resolve().parent.parent / "90_control" / "todos"


def _append_role_todo(role: str, text: str) -> None:
    """#501 角色待办收件箱：探针通知双通道——飞书（在外实例）+ todos/<role>.md
    落盘（CLI 实例收件箱，启动读）。追加式防覆盖，重复由 state 去重兜底。"""
    try:
        TODOS_DIR.mkdir(parents=True, exist_ok=True)
        ts = datetime.now().strftime("%Y-%m-%d %H:%M")
        fp = TODOS_DIR / f"{role}.md"
        if not fp.exists():
            fp.write_text(
                f"# {role} 待办（探针通知 CLI 收件箱——启动读此文件；在外实例走飞书）\n\n",
                encoding="utf-8")
        with fp.open("a", encoding="utf-8") as f:
            f.write(f"- [{ts}] {text}\n")
    except OSError as e:
        print(f"⚠️ 待办文件写入失败: {e}", file=sys.stderr)


def _review_brief(task_id: str) -> str:
    """#535：终审落点简报——读任务单终审/复审记录节，提取 结论+等级+返工项/O2 标记。
    格式：PASS A / FAIL / PASS A-·O2（无记录返回空串）。"""
    fp = TASK_DIR / f"{task_id}.md"
    if not fp.exists():
        return ""
    try:
        body = fp.read_text(encoding="utf-8", errors="ignore")
    except OSError:
        return ""
    idx = max(body.rfind("## 终审记录"), body.rfind("## 复审记录"))
    if idx == -1:
        return ""
    section = body[idx:idx + 2500]
    m = _re.search(r"\*\*(PASS(?:\s*A-?|B[+-]?|C)?|FAIL)\*\*", section)
    verdict = m.group(1).replace("  ", " ") if m else ""
    marks = []
    if "O2" in section:
        marks.append("O2")
    if verdict == "FAIL" or "返工" in section:
        marks.append("有返工项")
    return ("·".join([verdict] + marks)) if verdict else ""


def _prepend_role_todo(role: str, text: str) -> None:
    """#535 FAIL 置顶：终审退回通知插到收件箱条目区最顶（标题行之后）——
    返工优先（E019 完成未闭环优先），不等扫到底才看见。"""
    try:
        TODOS_DIR.mkdir(parents=True, exist_ok=True)
        ts = datetime.now().strftime("%Y-%m-%d %H:%M")
        fp = TODOS_DIR / f"{role}.md"
        if not fp.exists():
            fp.write_text(
                f"# {role} 待办（探针通知 CLI 收件箱——启动读此文件；在外实例走飞书）\n\n",
                encoding="utf-8")
        body = fp.read_text(encoding="utf-8")
        head, sep, rest = body.partition("\n\n")
        line = f"- [{ts}] {text}\n"
        fp.write_text(head + sep + line + rest, encoding="utf-8")
    except OSError as e:
        print(f"⚠️ 待办文件置顶写入失败: {e}", file=sys.stderr)


def _send_hook(url: str, text: str, key: str | None = None) -> bool:
    """发送飞书消息。**必须校验响应 body 的 code**——飞书业务失败也返回 HTTP 200（2026-08-23 实证：
    签名错误 code 19021 曾被当成功，全部消息假发送）。"""
    payload = {"msg_type": "text", "content": {"text": text}}
    if key:  # 加签模式（机器人安全设置开了签名校验）
        ts = str(int(time.time()))
        payload["timestamp"] = ts
        payload["sign"] = _feishu_sign(ts, key)
    data = json.dumps(payload, ensure_ascii=False).encode("utf-8")
    req = urllib.request.Request(url, data=data, headers={"Content-Type": "application/json"})
    try:
        with urllib.request.urlopen(req, timeout=15) as resp:
            body = resp.read().decode("utf-8", errors="replace")
            try:
                code = json.loads(body).get("code")
            except Exception:
                code = None
            if code not in (0, None):  # None=无业务码（非飞书标准响应）保守视为失败？—— 0 才成功
                FAIL_LOG.write_text(f"{datetime.now().isoformat()} 飞书业务失败 code={code}: {body[:200]}\n", encoding="utf-8")
                return False
            return resp.status == 200 and code == 0
    except Exception as e:
        FAIL_LOG.write_text(f"{datetime.now().isoformat()} {url[:40]}… {e}\n", encoding="utf-8")
        return False


def _split_silent_exempt(to_send: dict[str, str], exempt_roles: set[str]) -> tuple[dict[str, str], dict[str, str]]:
    """#520 R1 夜间静默分级：终审类信号（exempt_roles）豁免静默照常推，其余进待补发。

    老朱 08-25 拍板豁免范围（与 #521 同口径）：终审完成类信号（提审叫醒/PASS 路由）
    豁免 22-08 静默；可领取/建议书等维持静默。返回 (待补发, 豁免发)。
    """
    defer = {r: t for r, t in to_send.items() if r not in exempt_roles}
    exempt = {r: t for r, t in to_send.items() if r in exempt_roles}
    return defer, exempt


def _notify(messages: dict[str, str], dry_run: bool, silent: bool) -> list[str]:
    """发送通知，返回**真正发送成功**的 role 列表（#421 终审 P1 修复）。

    silent/dry-run/无配置 = 不发送且不消耗幂等配额——由调用方决定是否记 notified
    （原实现无条件记 notified，导致夜间静默的变更永不补发、dry-run 吞掉真实配额）。
    """
    hooks = _load_hooks()
    sent = []
    for role, text in messages.items():
        if silent:
            print(f"🔕 夜间静默，跳过通知：{role} → {text}")
            continue
        hook = hooks.get(role)
        if not hook:
            print(f"⚠️ 无 webhook 配置（不发送）：{role} → {text}")
            continue
        if dry_run:
            print(f"🧪 dry-run 不发送：{role} → {text}")
            continue
        ok = _send_hook(hook["url"], text, hook["key"])
        print(f"{'✅' if ok else '❌'} 通知 {role}：{text}")
        if ok:
            sent.append(role)
    return sent


# ── main ──────────────────────────────────────────────────

def main() -> int:
    p = argparse.ArgumentParser(description="KDO 传送带探针（#421）")
    p.add_argument("--dry-run", action="store_true", help="登记照做，通知只打印")
    p.add_argument("--force-notify", action="store_true", help="跳过夜间静默强制通知（仅测试/验收用，生产红线不变）")
    p.add_argument("--json", action="store_true", help="结构化输出")
    args = p.parse_args()

    state = _load_state()

    # #501 故障窗口补偿：运行间隔 > 2×周期（20 分钟）提示补扫（增量机制自动补，
    # 只要 state 未被消费；此检查只做提示，日志有痕）
    import time as _time
    now_ts = _time.time()
    last_ts = state.get("last_run_ts")
    if last_ts and now_ts - last_ts > 1200:
        print(f"⚠️ [conveyor_probe] 距上次运行 {int(now_ts - last_ts)}s（>20min）——"
              f"期间信号已由增量机制补扫（dry-run 已修不消费 state）", file=sys.stderr)
    state["last_run_ts"] = now_ts

    # 一次扫描事件：检出六类信号（单份逻辑，#458 第四探针 + #460 第五探针同事件）
    queue_sig = _queue_signal(state)
    proposal_hits = _scan_proposals()
    registered = _update_proposal_board(proposal_hits)  # 登记（幂等）
    # #506：三元组漂移 near-miss 显式报警（写 gate-blocked 式记录 → 下方第五探针同事件拾取闭环）
    near_miss = _scan_proposal_near_miss(state)
    friction_new = _scan_friction(state)  # 增量检测（state 幂等）
    gate_new = _scan_gate_blocked(state)  # 门禁拦截增量（#460 机器自报 + #506 near-miss）
    # F-036 第七信号：新终审意见书含 🟠/🟡 但无落点 → 提醒欧阳锋补建议书（兜底）
    issue_no_disp = _scan_issue_no_disposition(state, queue_sig["new_reviewed"])

    messages: dict[str, str] = {}
    failback_roles: set[str] = set()  # #535：退回角色收件箱置顶写
    # #520 R1：终审类信号豁免夜间静默（老朱 08-25 拍板，与 #521 同口径）——
    # 提审叫醒（→审查者）/终审完成（→生产者路由 #521）照常推，可领取/建议书等维持静默。
    # 跟随最终文本类别：非豁免类别覆盖同角色消息时摘除豁免标记。
    exempt_roles: set[str] = set()
    if queue_sig["new_review"]:
        ids = ", ".join(f"#{seq}" if seq else tid for tid, seq in queue_sig["new_review"])
        messages["ouyangfeng"] = f"🔔 KDO 新提审 {len(queue_sig['new_review'])} 单：{ids}，请终审"
        exempt_roles.add("ouyangfeng")  # #520 R1：提审叫醒=终审类信号，豁免静默
    if queue_sig["new_queued"]:
        # #443：按 assignee 路由分桶（修硬编码 laowantong——#442 实证通知错人）
        for role, items in _route_queued(queue_sig["new_queued"]).items():
            ids = ", ".join(f"#{seq}" if seq else tid for tid, seq in items)
            messages[role] = f"📥 KDO 可领取 {len(items)} 单：{ids}"
    if registered:
        messages["wangyuyan"] = f"📬 KDO 新建议书 {len(registered)} 份待裁定：{', '.join(registered)}"
    if friction_new:
        # #458：friction 线索登记 PROPOSAL-PENDING（[friction] 类型）+ 通知王语嫣
        _update_proposal_board_friction(friction_new)
        # #511：friction 事件层（单写入面=本扫描——friction_seen state 幂等，重跑不重复事件）
        for ln in friction_new:
            m = _re.match(r"^\[([^\]]+)\]", ln)
            mc.log_event_safe(m.group(1) if m else "conveyor_probe", "friction", ln[:300])
        messages["wangyuyan"] = f"🩹 KDO 新问题线索 {len(friction_new)} 条（friction）：{friction_new[0][:60]}{'…' if len(friction_new) > 1 else ''}"
    if gate_new:
        # #460：门禁拦截自动登记（[gate-blocked]）+ 通知——机器自报，零依赖 agent 自觉
        _update_proposal_board_gate(gate_new)
        messages["wangyuyan"] = f"⛔ KDO 门禁拦截 {len(gate_new)} 次（gate-blocked）：{gate_new[0][:70]}{'…' if len(gate_new) > 1 else ''}"
    if queue_sig["new_reviewed"]:
        # #521 R1：PASS 按 assignee 路由生产者（复用 #443 ASSIGNEE_ROLE）+ 王语嫣抄送保留；
        # R2：终审完成类信号豁免夜间静默（老朱 08-25 拍板，exempt_roles 机制 #520 同批建）
        items = ", ".join(f"#{seq}" if seq else tid for tid, seq, _a in queue_sig["new_reviewed"])
        messages["wangyuyan"] = f"⚖️ KDO 已终审 {len(queue_sig['new_reviewed'])} 单：{items}（待部署/已闭环）"
        exempt_roles.add("wangyuyan")  # 终审抄送=终审类信号，豁免静默
        for role, items_r in _route_queued(queue_sig["new_reviewed"]).items():
            # #535：落点简报——每单带 结论+等级+返工项/O2 标记（扫描者不再把「没变化」误读为「仍在审」）
            ids = ", ".join(
                (f"#{seq}" if seq else tid) + (f"（{_review_brief(tid)}）" if _review_brief(tid) else "")
                for tid, seq in items_r)
            messages[role] = f"✅ KDO 终审通过 {len(items_r)} 单：{ids}——你的单过了，见任务单终审记录"
            exempt_roles.add(role)  # PASS 生产者路由=终审类信号，豁免静默
    if issue_no_disp:
        # F-036 第七信号：终审意见 🟠/🟡 无落点 → 提醒欧阳锋补建议书（兜底，不靠用户提醒）
        todo = (f"{len(issue_no_disp)} 单终审意见含 🟠/🟡 但未给落点"
                f"（建议书/停车场/立项）：{', '.join(issue_no_disp[:3])}——请补落点")
        messages["ouyangfeng"] = f"✍️ F-036 提醒：{todo}"
        exempt_roles.discard("ouyangfeng")  # F-036 非终审类信号：覆盖叫醒文本时摘除豁免
    if queue_sig["new_failback"]:
        # #462：终审退回 → 按 assignee 路由通知（#443 同款；生产者返工不再靠自觉）
        # #535：FAIL 通知带「返工优先」标记，收件箱置顶（E019 完成未闭环优先）
        for tid, seq, assignee in queue_sig["new_failback"]:
            role = ASSIGNEE_ROLE.get(str(assignee).strip(), "laowantong")
            brief = _review_brief(tid)
            messages[role] = f"🔴 KDO 退回 1 单（返工优先）：#{seq}（{tid}）{f'〔{brief}〕' if brief else ''}，见任务单终审记录"
            failback_roles.add(role)

    # #537 第七信号：总账登记核查——基础设施单 reviewed 时矩阵未同步 → 双推欧阳锋+抄送王语嫣
    # （非终审类信号：不豁免夜间静默；幂等=matrix_checked 每单只查一次）
    matrix_checked = set(state.get("matrix_checked", []))
    matrix_dirty = False
    for tid, _seq, _a in queue_sig["new_reviewed"]:
        if tid in matrix_checked:
            continue
        issue = _matrix_sync_check(tid, _seq, ROOT)
        matrix_checked.add(tid)
        matrix_dirty = True
        if issue == "EXEMPT":
            try:  # 豁免留痕（#444 台账同款）
                with FORCE_LEDGER.open("a", encoding="utf-8") as f:
                    f.write(f"{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}｜task={tid}｜"
                            f"instance=conveyor_probe｜bypass=matrix 登记核查（matrix_exempt）｜"
                            f"reason=任务单声明豁免（§3.19 例外）\n")
            except OSError as e:
                print(f"⚠️ 豁免台账写入失败: {e}", file=sys.stderr)
        elif issue:
            messages["ouyangfeng"] = issue
            exempt_roles.discard("ouyangfeng")  # 非终审类：摘除可能残留的豁免标记
            cc = f"📋 抄送：{issue[:60]}…"
            messages["wangyuyan"] = (messages["wangyuyan"] + "；" + cc) if "wangyuyan" in messages else cc
    if matrix_dirty:
        state["matrix_checked"] = sorted(matrix_checked)[-300:]

    # 幂等：同 id 不重推（登记与通知同源——registered 是本次扫描产物）
    notified = set(state.get("notified", []))
    deduped = {}
    for role, text in messages.items():
        key = _msg_key(role, text)
        if key in notified:
            continue
        deduped[role] = text

    # #501 角色待办收件箱：所有将发送通知同时落盘 todos/<role>.md（CLI 实例收件箱）
    # #535：FAIL 退回通知置顶（返工优先），其余追加
    if not args.dry_run:
        for role, text in deduped.items():
            if role in failback_roles:
                _prepend_role_todo(role, text)
            else:
                _append_role_todo(role, text)

    hour = datetime.now().hour
    silent = (hour >= SILENT_START_HOUR or hour < SILENT_END_HOUR) and not args.force_notify

    # P1 修复（终审）：静默期/dry-run 不消耗配额——静默期变更进 pending 天亮补发，发送成功才记 notified
    pending = state.get("pending_notify", {})
    to_send = {**pending, **deduped}
    if silent:
        # #520 R1：终审类信号（提审叫醒等，exempt_roles）豁免静默照常推；其余进待补发
        to_defer, to_exempt = _split_silent_exempt(to_send, exempt_roles)
        state["pending_notify"] = to_defer
        if to_defer:
            print(f"🔕 夜间静默：{len(to_defer)} 条变更进待补发（天亮自动补发）")
        if to_exempt:
            sent = _notify(to_exempt, args.dry_run, silent=False)
            for role in sent:
                notified.add(_msg_key(role, to_exempt[role]))
            state["pending_notify"].update({k: v for k, v in to_exempt.items() if k not in sent})
            if sent:
                print(f"🔔 夜间静默豁免：终审类信号照常推 {sorted(sent)}（#520 老朱拍板口径）")
    else:
        sent = _notify(to_send, args.dry_run, silent=False)
        for role in sent:
            notified.add(_msg_key(role, to_send[role]))
        state["pending_notify"] = {k: v for k, v in to_send.items() if k not in sent}  # 失败留待下次重试
    state["notified"] = sorted(notified)[-200:]  # 只留最近 200 条防膨胀
    # #536：near-miss 超期升级（≥3 轮未修正推王语嫣收件箱；修正自动消项；静默期 defer）
    _escalate_near_miss(state, near_miss, args.dry_run, silent)
    # dry-run 不保存 state——否则会消费真实信号（通知去重/提醒去重被 dry-run 吞掉，
    # 真实运行"通知 0 条"）——2026-08-24 F-036 实害实证：dry-run 消费后待办不落盘
    if not args.dry_run:
        _save_state(state)

    summary = {
        "new_review": queue_sig["new_review"],
        "new_queued": queue_sig["new_queued"],
        "registered": registered,
        "near_miss": near_miss,  # #506：三元组漂移件（当场可见，不靠事后捞）
        "notified": list(deduped.keys()),
        "silent": silent,
    }
    if args.json:
        print(json.dumps(summary, ensure_ascii=False, indent=2))
    else:
        print(f"[conveyor_probe] 新提审 {len(queue_sig['new_review'])} / 新 queued {len(queue_sig['new_queued'])} / 新登记 {len(registered)} / near-miss {len(near_miss)} / 通知 {len(deduped)} 条{'（夜间静默）' if silent else ''}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
