#!/usr/bin/env python3
"""
kdo feature — 周期表"点菜"查询工具（#254 消费端协议技术底座）
数据源: #248 feature-periodic-table JSON (96 Feature, 8 字段)

用法:
  kdo feature list                    # 全量列表
  kdo feature query --layer L2        # 按层级过滤 (L0-L5)
  kdo feature query --dimension A     # 按维度过滤 (A/B/C/D)
  kdo feature query --scenario 作图   # 按场景模糊匹配
  kdo feature pick --n 5              # 随机点菜
  kdo feature info F001               # 单 Feature 详情
"""
import argparse, json, random, sys
from pathlib import Path

DATA_PATH = Path(__file__).resolve().parent.parent / "10_raw" / "sources" / "feature-periodic-table-v0.8.json"


def load():
    data = json.loads(DATA_PATH.read_text(encoding="utf-8"))
    return data.get("features", data) if isinstance(data, dict) else data


def fmt(f):
    v = "V" if f.get("verified") else "?"
    return f"{f['id']} {v} [{f['layer']}][{f['dimension']}] {f['name']:<20} {f['purpose'][:50]}"


def cmd_list():
    feats = load()
    print(f"\nFeature 周期表（{len(feats)} 个）\n")
    for f in feats:
        print(f"  {fmt(f)}")


def cmd_query(args):
    feats = load()
    if args.layer:
        feats = [f for f in feats if f["layer"] == args.layer]
    if args.dimension:
        feats = [f for f in feats if f["dimension"] == args.dimension]
    if args.scenario:
        kw = args.scenario.lower()
        feats = [f for f in feats if kw in f.get("scenario", "").lower() or kw in f.get("purpose", "").lower()]
    print(f"\n{len(feats)} results\n")
    for f in feats:
        print(f"  {fmt(f)}")


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
            print(f"\n{f['id']} | {f['name']} | {f['layer']} | {f['dimension']} | {'verified' if f.get('verified') else 'unverified'}")
            print(f"  用途: {f['purpose']}")
            print(f"  场景: {f['scenario']}")
            if f.get("case_ref"):
                print(f"  溯源: {f['case_ref']}")
            return
    print(f"Feature {args.id} not found")


def main():
    p = argparse.ArgumentParser(description="kdo feature — 周期表点菜工具")
    sub = p.add_subparsers(dest="cmd")

    sub.add_parser("list", help="全量 Feature 列表")

    q = sub.add_parser("query", help="按条件过滤")
    q.add_argument("--layer")
    q.add_argument("--dimension")
    q.add_argument("--scenario")

    pk = sub.add_parser("pick", help="随机点菜")
    pk.add_argument("--n", type=int, default=5)
    pk.add_argument("--seed", type=int, help="随机种子（复现用）")

    info = sub.add_parser("info", help="单 Feature 详情")
    info.add_argument("id")

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
    else:
        p.print_help()


if __name__ == "__main__":
    main()
