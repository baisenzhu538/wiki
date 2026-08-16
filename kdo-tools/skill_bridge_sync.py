#!/usr/bin/env python3
"""
kdo skill bridge — 双轨 Skill 同步（#267 双轨 Skill 同步机制 B1）

shared/（Hermes 格式，事实源）→ .claude/skills/（Claude Code 格式）
幂等：已同步且版本一致的跳过；版本不一致的更新。

用法:
  python kdo-tools/skill_bridge_sync.py status           # 双轨差异总览
  python kdo-tools/skill_bridge_sync.py sync [--dry-run] # 同步缺失+版本漂移
  python kdo-tools/skill_bridge_sync.py convert <skill>  # 单 skill 转换预览
"""
import argparse
import re
import shutil
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
SHARED = WIKI / "40_outputs" / "capabilities" / "skills" / "shared"
CLAUDE = WIKI / ".claude" / "skills"

# 需要从 Hermes frontmatter 提取的字段（转换后保留）
KEEP_KEYS = ("name", "version", "description")
# Claude Code frontmatter 需要的额外字段
ALLOWED_TOOLS_DEFAULT = ["Read", "Write", "Skill", "WebSearch"]


def read_fm(path: Path) -> dict:
    """读 frontmatter，返回 dict + 是否含 metadata.hermes。"""
    try:
        text = path.read_text(encoding="utf-8")
    except Exception:
        return {}
    m = re.match(r"^---\n(.*?)\n---", text, re.S)
    if not m:
        return {}
    fm = {}
    in_hermes = False
    for line in m.group(1).splitlines():
        if line.strip() == "metadata:":
            in_hermes = True
            continue
        if in_hermes and not line.startswith(" "):
            in_hermes = False
        if ":" in line and not in_hermes:
            k, v = line.split(":", 1)
            fm[k.strip()] = v.strip().strip('"').strip("'")
    return fm


def _strip_bom(text: str) -> str:
    return text[1:] if text.startswith("﻿") else text


def convert_to_claude(skill_name: str) -> str:
    """把 shared skill 的 SKILL.md 转成 Claude Code 格式（frontmatter 替换，body 保留）。"""
    src = SHARED / skill_name / "SKILL.md"
    text = _strip_bom(src.read_text(encoding="utf-8"))
    m = re.match(r"^---\n(.*?)\n---", text, re.S)
    if not m:
        return text  # 无 frontmatter 原样复制
    fm = read_fm(src)
    name = fm.get("name", skill_name)
    version = fm.get("version", "1.0.0")
    desc = fm.get("description", "")
    # 触发词：优先取 description 里的中文触发词；无则从 body 的"触发词"节提取
    triggers = ""
    tm = re.search(r"^## 触发词\n(.*?)(?=^## |\Z)", text, re.S | re.M)
    if tm:
        triggers = tm.group(1).strip().replace("\n", "、")
    new_fm = f"""---
name: {name}
version: "{version}"
allowed-tools:
  - Read
  - Write
  - Skill
  - WebSearch
description: |
  {desc}
  触发词：{triggers if triggers else name}
---

"""
    body = text[m.end():]
    body = body.lstrip("\n")  # 去掉 body 开头空行，避免双空行
    return new_fm + body


def diff_status() -> list[dict]:
    """返回双轨差异清单。漂移 = version 不同 或 body 内容不同（防版本号没变内容变了）。"""
    import hashlib

    def _body_hash(p: Path) -> str:
        try:
            text = _strip_bom(p.read_text(encoding="utf-8"))
        except Exception:
            return ""
        m = re.match(r"^---\n.*?\n---\n", text, re.S)
        body = text[m.end():] if m else text
        return hashlib.sha1(body.encode("utf-8")).hexdigest()[:12]

    shared_names = sorted(d.name for d in SHARED.iterdir() if d.is_dir())
    claude_names = sorted(d.name for d in CLAUDE.iterdir() if d.is_dir())
    missing = [n for n in shared_names if n not in claude_names]
    drifted = []
    for n in claude_names:
        if n in shared_names:
            sv = read_fm(SHARED / n / "SKILL.md").get("version", "")
            cv = read_fm(CLAUDE / n / "SKILL.md").get("version", "")
            version_diff = bool(sv and cv and sv != cv)
            body_diff = _body_hash(SHARED / n / "SKILL.md") != _body_hash(CLAUDE / n / "SKILL.md")
            if version_diff or body_diff:
                drifted.append({"name": n, "shared": sv, "claude": cv, "body_diff": body_diff})
    return {"missing": missing, "drifted": drifted, "shared_count": len(shared_names), "claude_count": len(claude_names)}


def cmd_status(_args):
    st = diff_status()
    print(f"\n双轨 Skill 状态（#267）")
    print(f"  shared（Hermes 事实源）: {st['shared_count']} 个")
    print(f"  .claude（Claude Code）: {st['claude_count']} 个")
    print(f"  缺失（shared→.claude）: {len(st['missing'])} 个")
    for n in st["missing"]:
        print(f"    ❌ {n}")
    print(f"  版本漂移: {len(st['drifted'])} 个")
    for d in st["drifted"]:
        reason = "内容不同" if d.get("body_diff") else "版本号不同"
        print(f"    ⚠️  {d['name']}: shared={d['shared']} vs .claude={d['claude']}（{reason}）")
    return 0


def cmd_sync(args):
    st = diff_status()
    targets = st["missing"] + [d["name"] for d in st["drifted"]]
    # references 缺失/漂移也纳入（已存在但 references 子目录缺失的）
    ref_fixes = []
    for n in sorted(d.name for d in CLAUDE.iterdir() if d.is_dir()):
        ref_src = SHARED / n / "references"
        if ref_src.exists():
            dst_ref = CLAUDE / n / "references"
            if not dst_ref.exists():
                ref_fixes.append(n)
    total = len(targets) + len(ref_fixes)
    print(f"\n待同步: {total} 个（缺失 {len(st['missing'])} + 漂移 {len(st['drifted'])} + references 缺失 {len(ref_fixes)}）")
    for n in targets + ref_fixes:
        print(f"  {'[dry-run] ' if args.dry_run else ''}→ {n}")
        if not args.dry_run:
            dst_dir = CLAUDE / n
            dst_dir.mkdir(parents=True, exist_ok=True)
            converted = convert_to_claude(n)
            (dst_dir / "SKILL.md").write_text(converted, encoding="utf-8")
            # references/ 子目录整体复制
            ref_src = SHARED / n / "references"
            if ref_src.exists():
                shutil.copytree(ref_src, dst_dir / "references", dirs_exist_ok=True)
    if args.dry_run:
        print("\n（dry-run 预览，加 --apply 生效）")
    else:
        # 验证：回读 frontmatter 确认转换成功（allowed-tools 是列表，键存在即通过）
        bad = 0
        for n in targets:
            fm = read_fm(CLAUDE / n / "SKILL.md")
            if not fm.get("name") or "allowed-tools" not in fm:
                bad += 1
                print(f"  🔴 转换校验失败: {n}")
        print(f"\n✅ 同步完成，校验 {'全部通过' if bad == 0 else f'{bad} 个失败'}")
    return 0


def cmd_convert(args):
    n = args.skill
    if not (SHARED / n).exists():
        print(f"Error: {n} 不在 shared/", file=sys.stderr)
        return 1
    print(f"\n=== 转换预览: {n} ===")
    print(convert_to_claude(n)[:1500])
    return 0


def main():
    p = argparse.ArgumentParser(description="kdo skill bridge — 双轨 Skill 同步")
    sub = p.add_subparsers(dest="cmd")
    sub.add_parser("status", help="双轨差异总览")
    s = sub.add_parser("sync", help="同步缺失+漂移（默认 dry-run）")
    s.add_argument("--apply", dest="dry_run", action="store_false", help="真正写入")
    c = sub.add_parser("convert", help="单 skill 转换预览")
    c.add_argument("skill")
    args = p.parse_args()
    if args.cmd == "status":
        return cmd_status(args)
    if args.cmd == "sync":
        return cmd_sync(args)
    if args.cmd == "convert":
        return cmd_convert(args)
    p.print_help()
    return 0


if __name__ == "__main__":
    sys.exit(main())
