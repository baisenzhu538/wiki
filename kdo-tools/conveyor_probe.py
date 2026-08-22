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
QUEUE_FILE = ROOT / "70_product" / "tasks" / "production-queue.md"
STATE_FILE = ROOT / ".kdo" / "conveyor_state.json"
HOOKS_FILE = Path(__file__).resolve().parent / ".feishu_webhooks.json"
FAIL_LOG = Path(__file__).resolve().parent / ".conveyor_failures.log"

PROPOSAL_BEGIN = "<!-- PROPOSAL-PENDING-BEGIN（自动登记：conveyor_probe.py；勿手改——王语嫣复核后划掉） -->"
PROPOSAL_BEGIN_OLD = "<!-- PROPOSAL-PENDING-BEGIN（建议书作者自登，王语嫣复核后划掉） -->"  # 迁移兼容旧段头
PROPOSAL_END = "<!-- PROPOSAL-PENDING-END -->"
SILENT_START_HOUR, SILENT_END_HOUR = 22, 8  # 夜间静默 22:00–08:00（登记照常，通知不发）

sys.path.insert(0, str(ROOT / "90_control" / "scripts"))
from queue_gate import parse_queue  # noqa: E402   # 唯一真相源读口，探针零写路径


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

def _msg_key(role: str, text: str) -> str:
    """幂等键：角色 + 消息主体（去 emoji 前缀）。"""
    return f"{role}:{text.split('：')[1] if '：' in text else text}"


def _queue_signal(state: dict) -> dict:
    """返回 [(task_id, seq)] 对（seq=队列序号，P2 修复：通知显示 #序号 非 slug 尾）。"""
    rows = parse_queue(QUEUE_FILE)
    review = [(r["task_id"], r["seq"]) for r in rows if r["status"] == "pending_review"]
    queued = [(r["task_id"], r["seq"]) for r in rows if r["status"] == "queued"]
    last_review = state.get("last_review_pending", [])
    last_queued = state.get("last_queued", [])
    new_review = [(t, s) for t, s in review if t not in last_review]
    new_queued = [(t, s) for t, s in queued if t not in last_queued]
    state["last_review_pending"], state["last_queued"] = [t for t, _ in review], [t for t, _ in queued]
    return {"new_review": new_review, "new_queued": new_queued}


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
        if "王语嫣" in str(fm.get("audience", "")) and str(fm.get("status", "")).strip() == "pending_orchestration":
            hits.append(fp.name)
    return hits


def _update_proposal_board(hits: list[str]) -> list[str]:
    """命中且未在段内的 → 自动写入 PROPOSAL-PENDING 段（路径级幂等）。
    对称 watch_inbox.update_orchestration_board：重写标记段，不碰任务表（状态机零干扰）。"""
    if not hits or not QUEUE_FILE.exists():
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
    """飞书群机器人加签：HMAC-SHA256(key, f'{ts}\\n{key}') → base64。"""
    string_to_sign = f"{ts}\n{key}"
    digest = hmac.new(key.encode("utf-8"), string_to_sign.encode("utf-8"), hashlib.sha256).digest()
    return base64.b64encode(digest).decode("utf-8")


def _send_hook(url: str, text: str, key: str | None = None) -> bool:
    payload = {"msg_type": "text", "content": {"text": text}}
    if key:  # 加签模式（机器人安全设置开了签名校验）
        ts = str(int(time.time()))
        payload["timestamp"] = ts
        payload["sign"] = _feishu_sign(ts, key)
    data = json.dumps(payload, ensure_ascii=False).encode("utf-8")
    req = urllib.request.Request(url, data=data, headers={"Content-Type": "application/json"})
    try:
        with urllib.request.urlopen(req, timeout=15) as resp:
            return resp.status == 200
    except Exception as e:
        FAIL_LOG.write_text(f"{datetime.now().isoformat()} {url[:40]}… {e}\n", encoding="utf-8")
        return False


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

    # 一次扫描事件：检出三类信号（单份逻辑）
    queue_sig = _queue_signal(state)
    proposal_hits = _scan_proposals()
    registered = _update_proposal_board(proposal_hits)  # 登记（幂等）

    messages: dict[str, str] = {}
    if queue_sig["new_review"]:
        ids = ", ".join(f"#{seq}" if seq else tid for tid, seq in queue_sig["new_review"])
        messages["ouyangfeng"] = f"🔔 KDO 新提审 {len(queue_sig['new_review'])} 单：{ids}，请终审"
    if queue_sig["new_queued"]:
        ids = ", ".join(f"#{seq}" if seq else tid for tid, seq in queue_sig["new_queued"])
        messages["laowantong"] = f"📥 KDO 可领取 {len(queue_sig['new_queued'])} 单：{ids}"
    if registered:
        messages["wangyuyan"] = f"📬 KDO 新建议书 {len(registered)} 份待裁定：{', '.join(registered)}"

    # 幂等：同 id 不重推（登记与通知同源——registered 是本次扫描产物）
    notified = set(state.get("notified", []))
    deduped = {}
    for role, text in messages.items():
        key = _msg_key(role, text)
        if key in notified:
            continue
        deduped[role] = text

    hour = datetime.now().hour
    silent = (hour >= SILENT_START_HOUR or hour < SILENT_END_HOUR) and not args.force_notify

    # P1 修复（终审）：静默期/dry-run 不消耗配额——静默期变更进 pending 天亮补发，发送成功才记 notified
    pending = state.get("pending_notify", {})
    to_send = {**pending, **deduped}
    if silent:
        state["pending_notify"] = to_send
        print(f"🔕 夜间静默：{len(to_send)} 条变更进待补发（天亮自动补发）")
    else:
        sent = _notify(to_send, args.dry_run, silent=False)
        for role in sent:
            notified.add(_msg_key(role, to_send[role]))
        state["pending_notify"] = {k: v for k, v in to_send.items() if k not in sent}  # 失败留待下次重试
    state["notified"] = sorted(notified)[-200:]  # 只留最近 200 条防膨胀
    _save_state(state)

    summary = {
        "new_review": queue_sig["new_review"],
        "new_queued": queue_sig["new_queued"],
        "registered": registered,
        "notified": list(deduped.keys()),
        "silent": silent,
    }
    if args.json:
        print(json.dumps(summary, ensure_ascii=False, indent=2))
    else:
        print(f"[conveyor_probe] 新提审 {len(queue_sig['new_review'])} / 新 queued {len(queue_sig['new_queued'])} / 新登记 {len(registered)} / 通知 {len(deduped)} 条{'（夜间静默）' if silent else ''}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
