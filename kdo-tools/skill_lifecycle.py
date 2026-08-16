#!/usr/bin/env python3
"""
kdo skill lifecycle — Skill 生命周期管理（#267 调研落地）
数据源: 40_outputs/capabilities/skills/*/SKILL.md frontmatter（唯一真相，P-16 教训）

用法:
  python kdo-tools/skill_lifecycle.py list
  python kdo-tools/skill_lifecycle.py status <skill>
  python kdo-tools/skill_lifecycle.py set <skill> --status draft|published|deprecated [--owner X] [--version 1.0] [--apply]
  python kdo-tools/skill_lifecycle.py eval <skill> [--regression] [--baseline] [--apply]
  python kdo-tools/skill_lifecycle.py stats
"""
import argparse
import json
import re
import sys
from pathlib import Path

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")
if sys.platform == "win32":
    try:
        import ctypes
        ctypes.windll.kernel32.SetConsoleOutputCP(65001)
    except Exception:
        pass

WIKI = Path(__file__).resolve().parent.parent
SKILLS_DIR = WIKI / "40_outputs" / "capabilities" / "skills"

# 旧 status 值 → 生命周期三态（向后兼容映射，不批量改文件）
LEGACY_MAP = {
    "stable": "published",
    "ready": "published",
    "active": "published",
    "self-evolution": "published",
    "draft": "draft",
    "published": "published",
    "deprecated": "deprecated",
}

def find_skill(name: str) -> Path | None:
    for d in SKILLS_DIR.iterdir():
        if d.is_dir() and d.name == name:
            return d
    return None


def read_frontmatter(path: Path) -> dict:
    """读 SKILL.md frontmatter，返回 dict。解析失败返回 {}。"""
    try:
        text = path.read_text(encoding="utf-8")
    except Exception:
        return {}
    m = re.match(r"^---\n(.*?)\n---", text, re.S)
    if not m:
        return {}
    fm = {}
    for line in m.group(1).splitlines():
        if ":" in line:
            k, v = line.split(":", 1)
            fm[k.strip()] = v.strip().strip('"').strip("'")
    return fm


def write_frontmatter(path: Path, updates: dict, dry_run: bool) -> bool:
    """更新 frontmatter 指定字段。非空值覆盖受控（用户显式指定才覆盖）。"""
    text = path.read_text(encoding="utf-8")
    m = re.match(r"^---\n(.*?)\n---", text, re.S)
    if not m:
        print(f"  ⚠️  {path.name} 无 frontmatter，跳过", file=sys.stderr)
        return False
    fm_text = m.group(1)
    changed = []
    for k, v in updates.items():
        pattern = re.compile(rf"^{re.escape(k)}:.*$", re.M)
        if pattern.search(fm_text):
            fm_text = pattern.sub(f"{k}: {v}", fm_text, count=1)
        else:
            fm_text += f"\n{k}: {v}"
        changed.append(f"{k}: {v}")
    if not dry_run:
        new_text = text[: m.start()] + "---\n" + fm_text + "\n---" + text[m.end():]
        path.write_text(new_text, encoding="utf-8")
        # round-trip 校验（P-18/P-29 教训）
        ok = read_frontmatter(path)
        for k in updates:
            if ok.get(k) != updates[k]:
                print(f"  🔴 round-trip 校验失败: {k}", file=sys.stderr)
                return False
    return True


def skill_rows():
    """[(skill_dir_name, frontmatter_dict, has_eval_log)]"""
    rows = []
    for d in sorted(SKILLS_DIR.iterdir()):
        if not d.is_dir():
            continue
        sk = d / "SKILL.md"
        if not sk.exists():
            # 子目录版本（如 note-coach/1.0.0/manifest.yaml）只认顶层
            continue
        fm = read_frontmatter(sk)
        rows.append((d.name, fm, (d / "eval-log.md").exists()))
    return rows


def cmd_list(_args):
    rows = skill_rows()
    print(f"\nKDO Skill 生命周期（{len(rows)} 个）\n")
    print(f"  {'skill':<32} {'status':<12} {'owner':<12} {'version':<8} {'eval':<5}")
    print("  " + "-" * 75)
    n = {"draft": 0, "published": 0, "deprecated": 0, "unknown": 0}
    for name, fm, has_eval in rows:
        raw = fm.get("status", "")
        status = LEGACY_MAP.get(raw, "unknown")
        n[status] = n.get(status, 0) + 1
        owner = fm.get("owner", "-") or "-"
        ver = fm.get("version", "-") or "-"
        ev = "✅" if has_eval else "-"
        print(f"  {name:<32} {status:<12} {owner:<12} {ver:<8} {ev:<5}")
    print(f"\n  分布: draft={n['draft']} published={n['published']} deprecated={n['deprecated']} unknown={n['unknown']}")
    print(f"  （unknown = frontmatter 无 status 或缺 SKILL.md，需 `set` 补标）")


def cmd_status(args):
    d = find_skill(args.skill)
    if not d:
        print(f"Error: Skill not found: {args.skill}", file=sys.stderr)
        return 1
    sk = d / "SKILL.md"
    if not sk.exists():
        print(f"Error: {d.name}/SKILL.md not found", file=sys.stderr)
        return 1
    fm = read_frontmatter(sk)
    raw = fm.get("status", "")
    status = LEGACY_MAP.get(raw, "unknown")
    print(f"\n{args.skill}")
    print(f"  status   : {status}" + (f"  (raw: {raw})" if raw != status else ""))
    print(f"  owner    : {fm.get('owner', '-')}")
    print(f"  version  : {fm.get('version', '-')}")
    if fm.get("dependencies"):
        print(f"  deps     : {fm.get('dependencies')}")
    print(f"  eval-log : {'✅ ' + str(len((d/'eval-log.md').read_text(encoding='utf-8').splitlines())) + ' 行' if (d/'eval-log.md').exists() else '无'}")
    return 0


def cmd_set(args):
    d = find_skill(args.skill)
    if not d:
        print(f"Error: Skill not found: {args.skill}", file=sys.stderr)
        return 1
    sk = d / "SKILL.md"
    if not sk.exists():
        print(f"Error: {d.name}/SKILL.md not found", file=sys.stderr)
        return 1
    updates = {}
    if args.status:
        if args.status not in ("draft", "published", "deprecated"):
            print(f"Error: --status 必须是 draft|published|deprecated", file=sys.stderr)
            return 1
        updates["status"] = args.status
    if args.owner:
        updates["owner"] = args.owner
    if args.version:
        updates["version"] = args.version
    if not updates:
        print("Error: 至少指定 --status/--owner/--version 之一", file=sys.stderr)
        return 1
    print(f"\n{args.skill}/SKILL.md")
    for k, v in updates.items():
        print(f"  {'[dry-run] ' if not args.apply else ''}{k}: {v}")
    ok = write_frontmatter(sk, updates, dry_run=not args.apply)
    if ok and args.apply:
        print("  ✅ 已写入（round-trip 校验通过）")
    elif ok:
        print("  （dry-run 预览，加 --apply 生效）")
    return 0


def cmd_eval(args):
    """能力 eval + 回归 eval + baseline 对比。写 eval-log.md（按迭代轮次追加）。"""
    d = find_skill(args.skill)
    if not d:
        print(f"Error: Skill not found: {args.skill}", file=sys.stderr)
        return 1
    sk = d / "SKILL.md"
    if not sk.exists():
        print(f"Error: {d.name}/SKILL.md not found", file=sys.stderr)
        return 1
    text = sk.read_text(encoding="utf-8")
    fm = read_frontmatter(sk)
    status = LEGACY_MAP.get(fm.get("status", ""), "unknown")
    log = d / "eval-log.md"
    history = log.read_text(encoding="utf-8") if log.exists() else ""

    print(f"\n═══ kdo skill eval: {args.skill} ═══")
    print(f"  status: {status}")

    # 1. 机械结构检查（自动门禁）
    checks = []
    checks.append(("frontmatter status", "✅" if fm.get("status") else "❌ 缺 status"))
    checks.append(("SKILL.md ≤500 行", "✅" if len(text.splitlines()) <= 500 else f"⚠️ {len(text.splitlines())} 行"))
    trigger = re.search(r"^## .*(触发|Trigger|When to Use|何时)", text, re.M)
    checks.append(("触发词节", "✅" if trigger else "⚠️ 未发现触发节"))
    example = re.search(r"示例|example|Example|```", text)
    checks.append(("示例/代码块", "✅" if example else "⚠️ 无示例"))
    for name, res in checks:
        print(f"    {res}  {name}")

    # 2. 能力 eval 场景提取（从 SKILL.md 标题结构提取代表性任务）
    sections = re.findall(r"^## (.+)$", text, re.M)[:6]
    print(f"\n  [能力 eval] 代表性任务（取自 SKILL.md 章节）:")
    for i, s in enumerate(sections[:5], 1):
        print(f"    {i}. {s.strip()}")

    # 3. 回归 eval：历史失败场景（从 eval-log 提取 FAIL 行）
    fails = [l for l in history.splitlines() if "FAIL" in l or "🔴" in l]
    print(f"\n  [回归 eval] 历史失败场景: {len(fails)} 条" + ("" if fails else "（无历史 FAIL）"))
    for l in fails[-5:]:
        print(f"    ↳ {l.strip()[:100]}")

    # 4. baseline 对比（无 skill vs 有 skill）
    baselines = [l for l in history.splitlines() if "baseline" in l]
    print(f"\n  [baseline] 历史对比记录: {len(baselines)} 条")
    for l in baselines[-3:]:
        print(f"    ↳ {l.strip()[:100]}")

    if not args.apply:
        print(f"\n  （dry-run：未写 eval-log。加 --apply 记录本轮 eval 结果）")
        print(f"  建议执行：真实跑 1-2 个代表性任务后，用 --apply 记录结果")
        return 0

    # 写 eval-log（追加，不覆盖——P-32 教训）
    import datetime
    ts = datetime.datetime.now().strftime("%Y-%m-%d")
    entry = [
        f"\n## iteration {ts}",
        f"- status: {status}",
        f"- 机械门禁: {sum(1 for _, r in checks if r.startswith('✅'))}/{len(checks)} 过",
        f"- 能力任务数: {len(sections[:5])}",
        f"- 回归场景数: {len(fails)}",
        f"- baseline 记录数: {len(baselines)}",
    ]
    with log.open("a", encoding="utf-8") as f:
        f.write("\n".join(entry) + "\n")
    print(f"\n  ✅ eval-log 已追加: {log.relative_to(WIKI)}")
    return 0


def cmd_stats(_args):
    rows = skill_rows()
    total = len(rows)
    by_status = {}
    by_owner = {}
    with_eval = 0
    for name, fm, has_eval in rows:
        s = LEGACY_MAP.get(fm.get("status", ""), "unknown")
        by_status[s] = by_status.get(s, 0) + 1
        o = fm.get("owner", "-") or "-"
        by_owner[o] = by_owner.get(o, 0) + 1
        with_eval += 1 if has_eval else 0
    print(f"\nSkill 生命周期统计（{total} 个）")
    print(f"  按状态: " + "  ".join(f"{k}={v}" for k, v in sorted(by_status.items())))
    print(f"  按 owner: " + "  ".join(f"{k}={v}" for k, v in sorted(by_owner.items(), key=lambda x: -x[1])))
    print(f"  有 eval-log: {with_eval}/{total}")
    return 0


def main():
    p = argparse.ArgumentParser(description="kdo skill lifecycle — Skill 生命周期管理")
    sub = p.add_subparsers(dest="cmd")
    sub.add_parser("list", help="全量生命周期列表")
    sub.add_parser("stats", help="生命周期统计")
    st = sub.add_parser("status", help="单 skill 状态")
    st.add_argument("skill")
    se = sub.add_parser("set", help="设置 status/owner/version（默认 dry-run）")
    se.add_argument("skill")
    se.add_argument("--status", choices=["draft", "published", "deprecated"])
    se.add_argument("--owner")
    se.add_argument("--version")
    se.add_argument("--apply", action="store_true", help="真正写入 frontmatter")
    ev = sub.add_parser("eval", help="能力 eval + 回归 eval + baseline（默认 dry-run）")
    ev.add_argument("skill")
    ev.add_argument("--apply", action="store_true", help="写 eval-log")
    args = p.parse_args()

    if args.cmd == "list":
        return cmd_list(args)
    if args.cmd == "status":
        return cmd_status(args)
    if args.cmd == "set":
        return cmd_set(args)
    if args.cmd == "eval":
        return cmd_eval(args)
    if args.cmd == "stats":
        return cmd_stats(args)
    p.print_help()
    return 0


if __name__ == "__main__":
    sys.exit(main())
