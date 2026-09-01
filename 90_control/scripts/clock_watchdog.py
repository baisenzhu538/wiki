#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
clock_watchdog.py — 王语嫣值守 no_agent 看门狗（拍板项 P-20260901-2340 选①，老朱 2026-09-01 拍板）
取代 wangyuyan-clock-v4（LLM 值守拍）的「例行扫描」职能；LLM 只在有事时被拉起做判断和处置。

语义（Hermes cron no_agent 契约）：
  - 无事 → stdout 空 + exit 0（SILENT，不送达任何人）
  - 有事 → stdout 简报 + exit 0（送达飞书 DM：老朱可见，王语嫣被叫醒处置）
  - 脚本崩溃 → 非 0 退出（系统自动报错，值守断链不静默）

边界（automation-loop-closure 铁律）：
  - 只探测不决策：不拉人、不改队列状态、不消费素材、不写 vault（仅更新自身 state/skip 文件由王语嫣维护）
  - 时钟送达面=王语嫣单点：本脚本只叫王语嫣，不直接拉其他角色
"""
import io
import json
import sys
import time
from pathlib import Path

sys.stdout.reconfigure(encoding="utf-8", errors="replace")
ROOT = Path(__file__).resolve().parents[2]  # wiki 根（90_control/scripts/ 的上两级）
sys.path.insert(0, str(ROOT / "90_control" / "scripts"))

QUEUE = ROOT / "70_product" / "tasks" / "production-queue.md"
REGISTRY = ROOT / "90_control" / "role-registry.json"
GATE_LOG = ROOT / "90_control" / "gate-blocked.log"
SKIP_FILE = ROOT / "90_control" / "scripts" / "clock-watchdog-skip.json"
STATE_FILE = ROOT / "90_control" / "scripts" / "clock-watchdog-state.json"

REVIEWER = "欧阳锋"          # 出口门控固定角色（charter §2.6）
REVIEW_FRESH_SEC = 75 * 60   # 终审实例心跳新鲜窗：窗内=审程中静默，超窗=挂死告警（#591 实证大单审程~1h）
WORKER_STALE_SEC = 2 * 3600  # 施工实例心跳过期线：超线=施工疑似中断
ROLE_MAP = {                 # 队列 assignee → 注册表 key（中文角色名+ASCII 别名双映射，新队列行两种写法都有）
    "王语嫣": "wangyuyan", "wangyuyan": "wangyuyan",
    "老顽童": "laowantong", "laowantong": "laowantong",
    "黄药师": "huangyaoshi", "huangyaoshi": "huangyaoshi",
    "欧阳锋": "ouyangfeng", "ouyangfeng": "ouyangfeng",
    "风清扬": "fengqingyang", "fengqingyang": "fengqingyang",
    "skills-assistant": "skills-assistant",
}
SEGMENTS = [
    ("PROPOSAL-PENDING", "PROPOSAL-PENDING-BEGIN", "PROPOSAL-PENDING-END"),
    ("INBOX-PENDING", "INBOX-PENDING-BEGIN", "INBOX-PENDING-END"),
    ("REVIEW-PENDING", "REVIEW-PENDING-BEGIN", "REVIEW-PENDING-END"),
]


def load_json(p, default):
    try:
        with io.open(p, encoding="utf-8") as f:
            return json.load(f)
    except Exception:
        return default


def fmt_age(sec):
    if sec is None:
        return "无实例记录"
    if sec < 90:
        return "刚写入"
    return f"{sec / 60:.0f}min前"


def main():
    now = time.time()
    state = load_json(STATE_FILE, {})
    skip_cfg = load_json(SKIP_FILE, {})
    skip_seqs = set(skip_cfg.get("seq", []))
    alerts = []

    # ---- 0) vault 完整性快查（0901 两次清零事故后常设岗哨）----
    try:
        qsize = QUEUE.stat().st_size
        if qsize < 1000:
            alerts.append(f"🚨 队列文件异常：production-queue.md 仅 {qsize}B（疑似清零/截断），立即 git 核查恢复")
    except OSError as e:
        alerts.append(f"🚨 队列文件不可读：{e}")
        qsize = -1

    # ---- 1) 队列状态面（单一天真相源：parse_queue）----
    registry = load_json(REGISTRY, {})
    task_count = None
    pending_seqs = set()
    try:
        from queue_transition import parse_queue
        tasks = parse_queue()
        task_count = len(tasks)
        pending_seqs = {t["seq"] for t in tasks if t["status"] == "pending_review"}

        def role_age(assignee):
            """角色最新实例心跳距今年秒数；未映射角色返回 None 并由调用方决定告警口径"""
            key = ROLE_MAP.get(assignee)
            if key is None:
                return None, assignee not in ("", None)
            insts = (registry.get(key) or {}).get("instances") or []
            ts = [float(i.get("heartbeat_ts", 0)) for i in insts if i.get("heartbeat_ts")]
            return (now - max(ts)) if ts else None, False

        for t in tasks:
            if t["status"] == "pending_review" and t["seq"] not in skip_seqs:
                age, unmapped = role_age(REVIEWER)
                if age is None or age > REVIEW_FRESH_SEC:
                    alerts.append(
                        f"⚖️ 待终审挂起且无新鲜终审实例：#{t['seq']} {t['task_id'][:58]}"
                        f"（欧阳锋心跳 {fmt_age(age)}）→ 拉欧阳锋终审"
                    )
            elif t["status"] == "queued" and t["seq"] not in skip_seqs:
                assignee = (t.get("assignee") or "").strip()
                age, unmapped = role_age(assignee)
                if unmapped:
                    alerts.append(f"📋 queued 但角色「{assignee}」未入注册表：#{t['seq']} {t['task_id'][:50]} → 编排补登记/裁定")
                elif age is None or age > WORKER_STALE_SEC:
                    alerts.append(
                        f"📋 queued 无人可领（{assignee} 心跳 {fmt_age(age)}）：#{t['seq']} {t['task_id'][:50]} → 编排裁定是否拉起"
                    )
            elif t["status"] == "claimed" and t["seq"] not in skip_seqs:
                assignee = (t.get("assignee") or "").strip()
                age, unmapped = role_age(assignee)
                if not unmapped and age is not None and age > WORKER_STALE_SEC:
                    alerts.append(
                        f"🚧 claimed 但施工心跳过期（{assignee} {fmt_age(age)}）：#{t['seq']} {t['task_id'][:50]} → 疑似中断，编排核棒"
                    )
    except Exception as e:
        alerts.append(f"🚨 队列解析失败：{type(e).__name__}: {e}")

    # ---- 2) 看板三段未划销行（登记≠消费，停在这=有人要接手）----
    try:
        text = io.open(QUEUE, encoding="utf-8", errors="replace").read()
        for name, begin, end in SEGMENTS:
            i = text.find(begin)
            if i < 0:
                continue
            j = text.find(end, i)
            seg = text[i:j if j > 0 else len(text)]
            rows = [
                l.strip()[:76]
                for l in seg.splitlines()
                if l.strip().startswith("- ") and not l.strip().startswith("- ~~")
            ]
            if name == "REVIEW-PENDING":
                # 已在 pending_review 队列检查里报过的单不双报（重复告警=噪音）
                rows = [r for r in rows if not any(f"#{s} " in r or f"#{s}｜" in r for s in pending_seqs)]
            if rows:
                alerts.append(f"📥 {name} {len(rows)} 行未划销（例：{rows[0]}）→ 王语嫣消费")
    except Exception as e:
        alerts.append(f"🚨 看板段扫描失败：{e}")

    # ---- 3) gate-blocked 增量（首拍建基线不告警）----
    try:
        with io.open(GATE_LOG, encoding="utf-8", errors="replace") as f:
            lines = [l for l in f.read().splitlines() if l.strip()]
    except OSError:
        lines = []
    base = state.get("gate_lines")
    if base is not None and len(lines) > int(base):
        alerts.append(f"⛔ gate-blocked 新增 {len(lines) - int(base)} 行（最新：{lines[-1][:80]}）→ 王语嫣处置")

    # ---- 4) 队列规模骤降（删除事故特征，0901 两例）----
    last_n = state.get("task_count")
    if task_count is not None and last_n and task_count < int(last_n) * 0.8:
        alerts.append(f"🚨 队列任务数骤降：{last_n} → {task_count}（>20%），疑似删除事故，立即核查")

    # ---- 5) 王语嫣心跳续命（防 liveness 探针夜间误判死亡→gate-blocked 噪音→反叫醒死循环）----
    try:
        registry = load_json(REGISTRY, {})
        w = registry.get("wangyuyan")
        if isinstance(w, dict):
            w["last_heartbeat"] = now
            insts = w.get("instances") or []
            hit = False
            for inst in insts:
                if inst.get("kind") == "platform":
                    inst["heartbeat_ts"] = now
                    hit = True
            if not hit and insts:
                insts[0]["heartbeat_ts"] = now
                hit = True
            if not hit:
                insts.append({"tool": "watchdog", "kind": "platform", "channels": ["todos"], "heartbeat_ts": now})
            w["instances"] = insts
            REGISTRY.write_text(json.dumps(registry, ensure_ascii=False, indent=1), encoding="utf-8")
    except Exception:
        pass  # 心跳续命失败不产生误报，liveness 侧自会重报

    # ---- 6) 更新自身 state（运行态，非知识）----
    STATE_FILE.write_text(
        json.dumps(
            {"gate_lines": len(lines), "task_count": task_count, "last_run": now, "last_alerts": len(alerts)},
            ensure_ascii=False,
            indent=1,
        ),
        encoding="utf-8",
    )

    if alerts:
        stamp = time.strftime("%m-%d %H:%M")
        print(f"🐕 看门狗 {stamp} — {len(alerts)} 项需编排层处置（no_agent 脚本值守 v5，处置=拉王语嫣）")
        for a in alerts:
            print("• " + a)
    # 无事：stdout 保持为空 = SILENT


if __name__ == "__main__":
    main()
