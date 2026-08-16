#!/usr/bin/env python3
"""
kdo feature — 周期表"点菜"查询工具（#254 消费端协议技术底座）
数据源: feature-periodic-table-v0.9.json (#315: 100 Feature + aliases 别名)

用法:
  kdo feature list                    # 全量列表
  kdo feature query --layer L2        # 按层级过滤 (L0-L5)
  kdo feature query --dimension A     # 按维度过滤 (A/B/C/D)
  kdo feature query --scenario 作图   # 按场景模糊匹配
  kdo feature query --keyword 反向教学 # #315 全局关键词（含 aliases 命中）
  kdo feature pick --n 5              # 随机点菜
  kdo feature info F001               # 单 Feature 详情（含别名）
  kdo feature combo --scene 内容创作  # #316 场景→推荐 Feature 组合（含证据）
  kdo feature by-layer                # #318 分层水位报告（L0-L5 覆盖率）
"""
import argparse, json, random, sys
from pathlib import Path

DATA_PATH = Path(__file__).resolve().parent.parent / "10_raw" / "sources" / "feature-periodic-table-v1.0.json"
COMBO_PATH = Path(__file__).resolve().parent / "feature_combos.json"  # #316 组合种子数据
REVERIFY_MONTHS = 6  # #272 新鲜度 SLA：verified 后 6 个月未复验 → stale


def load():
    data = json.loads(DATA_PATH.read_text(encoding="utf-8"))
    return data.get("features", data) if isinstance(data, dict) else data


def _is_stale(f) -> bool:
    """#272: verified + verify_date 超 6 个月 → stale（降级不删除）。无 verify_date 的 verified 不算 stale（迁移中容忍）。"""
    if not f.get("verified"):
        return False
    vd = f.get("verify_date") or f.get("reverify_by")
    if not vd:
        return False
    from datetime import datetime
    try:
        vd_dt = datetime.strptime(vd, "%Y-%m-%d")
        from datetime import timedelta
        return datetime.now() > vd_dt + timedelta(days=REVERIFY_MONTHS * 30)
    except ValueError:
        return False


def fmt(f):
    v = "V" if f.get("verified") else "?"
    note = f.get("verify_note", "")
    note_str = f" [{note[:30]}]" if note else ""
    stale = " ⚠️stale" if _is_stale(f) else ""
    ev = f.get("evidence", {})
    ev_str = f" [{ev['grade']}]" if ev.get("grade") else ""
    return f"{f['id']} {v}{note_str}{stale}{ev_str} [{f['layer']}][{f['dimension']}] {f['name']:<20} {f['purpose'][:50]}"


def cmd_list():
    feats = load()
    print(f"\nFeature 周期表（{len(feats)} 个）\n")
    for f in feats:
        print(f"  {fmt(f)}")


def _match(f, kw: str) -> bool:
    """#315: 模糊匹配覆盖 name/purpose/scenario/aliases（别名命中 = 学员命名 → 周期表 Feature 映射）。"""
    fields = [f.get("name", ""), f.get("purpose", ""), f.get("scenario", ""), *f.get("aliases", [])]
    return any(kw in v.lower() for v in fields)


def cmd_query(args):
    feats = load()
    if args.layer:
        feats = [f for f in feats if f["layer"] == args.layer]
    if args.dimension:
        feats = [f for f in feats if f["dimension"] == args.dimension]
    if args.scenario:
        feats = [f for f in feats if _match(f, args.scenario.lower())]
    if args.keyword:
        kw = args.keyword.lower()
        feats = [f for f in feats if _match(f, kw)]
    print(f"\n{len(feats)} results\n")
    for f in feats:
        print(f"  {fmt(f)}")
        if f.get("aliases"):
            print(f"     ⚡ 别名: {' / '.join(f['aliases'][:8])}")


def cmd_pick(args):
    feats = load()
    n = min(args.n, len(feats))
    if args.seed is not None:
        random.seed(args.seed)
    picked = random.sample(feats, n)
    print(f"\n🎯 点菜 {n} 个 Feature\n")
    for f in picked:
        print(f"  {fmt(f)}")
        if f.get("case_ref"):
            print(f"     📎 {f['case_ref'][:120]}")


def cmd_info(args):
    feats = load()
    for f in feats:
        if f["id"] == args.id:
            state = "verified" if f.get("verified") else "unverified"
            if _is_stale(f):
                state += " (stale)"
            print(f"\n{f['id']} | {f['name']} | {f['layer']} | {f['dimension']} | {state}")
            print(f"  用途: {f['purpose']}")
            print(f"  场景: {f['scenario']}")
            if f.get("aliases"):
                print(f"  别名: {' / '.join(f['aliases'])}")
            if f.get("evidence"):
                ev = f["evidence"]
                print(f"  证据等级: {ev.get('grade', '?')}")
                if ev.get("metric"):
                    print(f"  证据指标: {ev['metric']}")
                if ev.get("source"):
                    print(f"  证据来源: {ev['source']}")
            if f.get("verify_date"):
                print(f"  认证日期: {f['verify_date']}")
            if f.get("reverify_by"):
                print(f"  复审期限: {f['reverify_by']}")
            if f.get("verify_note"):
                print(f"  认证注记: {f['verify_note']}")  # #264 v0.2 联动：info 也显示 verify_note
            if f.get("case_ref"):
                print(f"  溯源: {f['case_ref']}")
            return
    print(f"Feature {args.id} not found")


def cmd_by_layer(args):
    """#318: 按 L0-L5 统计 verified/evidence 覆盖率——分层水位报告（教练 agent"学哪层"数据依据）。"""
    feats = load()
    layers = ["L0", "L1", "L2", "L3", "L4", "L5"]
    print(f"\nFeature 分层水位报告（共 {len(feats)} 个）\n")
    print(f"  {'层':<4}{'总数':<6}{'verified':<10}{'覆盖率':<9}{'evidence 分布'}")
    print(f"  {'—'*60}")
    total_v = 0
    for layer in layers:
        fs = [f for f in feats if f.get("layer") == layer]
        n = len(fs)
        v = sum(1 for f in fs if f.get("verified"))
        total_v += v
        pct = f"{v/n*100:.0f}%" if n else "-"
        evs = [f.get("evidence", {}).get("grade", "") for f in fs]
        ev_cnt = {g: evs.count(g) for g in ("实测", "引用", "推演") if g in evs}
        ev_str = " ".join(f"{k}{v}" for k, v in ev_cnt.items()) if ev_cnt else "-"
        print(f"  {layer:<4}{n:<6}{v:<10}{pct:<9}{ev_str}")
    print(f"\n  verified 合计 {total_v}/{len(feats)}（{total_v/len(feats)*100:.0f}%）")

    # 解读：水位层 = verified 最集中的层；空白区 = 低覆盖层
    by_layer = {l: (sum(1 for f in feats if f.get("layer") == l and f.get("verified")),
                    sum(1 for f in feats if f.get("layer") == l)) for l in layers}
    water = max(layers, key=lambda l: (by_layer[l][0] / by_layer[l][1]) if by_layer[l][1] else 0)
    blank = min(layers, key=lambda l: (by_layer[l][0] / by_layer[l][1]) if by_layer[l][1] else 1)
    print(f"\n  解读：当前水位 = {water}（verified 最集中）；空白区 = {blank}（覆盖率最低）")
    print(f"  注：水位=用户群体已用并验证的层；空白区=补卡/引导优先方向（建议归编排侧）")


def cmd_combo(args):
    """#316: 场景 → 推荐 Feature 组合（叠加效应从卡变机制）。组合条目含 Feature 引用 + 证据来源（实测/推演）。"""
    data = json.loads(COMBO_PATH.read_text(encoding="utf-8"))
    combos = data.get("combos", [])
    scene = args.scene.lower() if args.scene else None
    hits = [c for c in combos if scene is None or any(scene in t.lower() for t in c.get("scene_tags", []))] if scene else combos

    print(f"\nFeature 组合库（{len(combos)} 个，来源: {data.get('source', '')}）\n")
    if args.scene:
        print(f"场景「{args.scene}」命中 {len(hits)} 个组合\n")
    for c in hits:
        ev = c.get("evidence", {})
        grade = ev.get("grade", "?")
        print(f"  🧩 {c['id']} · {c['name']}  [{grade}]")
        for f in c.get("features", []):
            print(f"     - {f['id']} {f['name']}：{f.get('role', '')}")
        print(f"     证据: {ev.get('case', '')} | {ev.get('metric', '')}")
        if c.get("note"):
            print(f"     注: {c['note'][:100]}")
        print()


def cmd_stale(args):
    """#272: 列出超期未复验的 verified Feature（降级不删除，标记证据待复验）。"""
    feats = load()
    stale = [f for f in feats if _is_stale(f)]
    missing_vd = [f for f in feats if f.get("verified") and not f.get("verify_date") and not f.get("reverify_by")]
    print(f"\nFeature stale 检查（#272 新鲜度 SLA，复审周期 {REVERIFY_MONTHS} 个月）\n")
    if stale:
        print(f"  ⚠️ 超期 {len(stale)} 个（verified 但超 {REVERIFY_MONTHS} 个月未复验）：")
        for f in stale:
            vd = f.get("verify_date") or f.get("reverify_by")
            print(f"    {f['id']} | 认证 {vd} | {f['name'][:40]}")
    else:
        print(f"  ✅ 无超期（{sum(1 for f in feats if f.get('verified'))} 个 verified 全部在复审期内）")
    if missing_vd:
        print(f"\n  ℹ️ verified 但缺认证日期 {len(missing_vd)} 个（待 #272 迁移补 verify_date）：")
        for f in missing_vd:
            print(f"    {f['id']} | {f['name'][:40]}")
    return 0


def main():
    p = argparse.ArgumentParser(description="kdo feature — 周期表点菜工具")
    sub = p.add_subparsers(dest="cmd")

    sub.add_parser("list", help="全量 Feature 列表")

    q = sub.add_parser("query", help="按条件过滤")
    q.add_argument("--layer")
    q.add_argument("--dimension")
    q.add_argument("--scenario")
    q.add_argument("--keyword", help="#315 全局关键词（name/purpose/scenario/aliases）")

    pk = sub.add_parser("pick", help="随机点菜")
    pk.add_argument("--n", type=int, default=5)
    pk.add_argument("--seed", type=int, help="随机种子（复现用）")

    info = sub.add_parser("info", help="单 Feature 详情")
    info.add_argument("id")

    sub.add_parser("stale", help="#272 列出超期未复验的 Feature")

    cb = sub.add_parser("combo", help="#316 场景→推荐 Feature 组合（叠加效应）")
    cb.add_argument("--scene", help="场景关键词（内容创作/课程/直播复盘/冷邮件…）")

    sub.add_parser("by-layer", help="#318 分层水位报告（L0-L5 verified 覆盖率）")

    args = p.parse_args()
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")

    if args.cmd == "list":
        cmd_list()
    elif args.cmd == "query":
        cmd_query(args)
    elif args.cmd == "pick":
        cmd_pick(args)
    elif args.cmd == "info":
        cmd_info(args)
    elif args.cmd == "stale":
        return cmd_stale(args)
    elif args.cmd == "combo":
        cmd_combo(args)
    elif args.cmd == "by-layer":
        cmd_by_layer(args)
    else:
        p.print_help()


if __name__ == "__main__":
    main()
