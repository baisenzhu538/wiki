#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""scan_skills_registry.py — #588 Skill 目录与挂载矩阵扫描生成器。

扫描 40_outputs/capabilities/skills/（shared/ + 根目录），从 SKILL.md frontmatter
（及 manifest.yaml 补充）提取 name/description/trigger.natural_language/adapted_from，
生成两份登记物：

  1. 40_outputs/capabilities/skills/INDEX.md         —— skill 目录菜单（可检索）
  2. 40_outputs/capabilities/skills/MOUNT-MATRIX.md  —— agent×skill 挂载矩阵

挂载判定（登记制，引用即挂载）：扫三类登记处的 token 引用——
  A. 90_control/role-routes.md 路由2 表（六角色）
  B. 30_wiki/agent-specs/*.md（spec 层）
  C. agents/*/ CLAUDE.md / AGENTS.md / SPEC.md / SOUL.md（实例层）

状态三档：已挂载（≥2 单元或入角色路由）/ 单点挂载（仅 1 单元）/ 无主（0 单元）。
无主+单点 = 「可挂未挂」清单，带关键词启发式归属建议（机械可审计）。

用法：
  python 40_outputs/code/scripts/scan_skills_registry.py            # 全量重生成
  python 40_outputs/code/scripts/scan_skills_registry.py --check    # 新鲜度门禁（stale→exit 1）

增量机制：脚本幂等，新 skill 注册/新 agent 部署后重跑即刷新；INDEX.md 头部
写入 generated_at + skill 计数，--check 对比 SKILL.md 最新 mtime 判 stale。
健康巡检挂接见 90_control/infrastructure-inventory.md §巡检族。
"""

from __future__ import annotations

import argparse
import io
import re
import sys
from datetime import datetime
from pathlib import Path

try:
    import yaml
except ImportError:  # pragma: no cover
    print("需要 PyYAML：pip install pyyaml", file=sys.stderr)
    raise SystemExit(2)

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")

WIKI = Path(__file__).resolve().parents[3]
SKILLS_DIR = WIKI / "40_outputs" / "capabilities" / "skills"
INDEX_FILE = SKILLS_DIR / "INDEX.md"
MATRIX_FILE = SKILLS_DIR / "MOUNT-MATRIX.md"
ROLE_ROUTES = WIKI / "90_control" / "role-routes.md"
AGENT_SPECS_DIR = WIKI / "30_wiki" / "agent-specs"
AGENTS_DIR = WIKI / "agents"
AGENT_SOURCE_FILES = ("CLAUDE.md", "AGENTS.md", "SPEC.md", "SOUL.md")

# 关键词启发式归属建议表（可挂未挂清单用；机械规则，建议仅供参考）
ROLE_HINTS = [
    ("洪七公", ("image", "video", "audio", "ocr", "vlm", "visual", "voice", "tts", "canvas", "montage", "ppt", "presentation", "drawio", "comfyui", "设计")),
    ("老顽童", ("content", "article", "writing", "collect", "production", "draft", "cangjie", "darwin", "xiaohongshu", "note", "卡")),
    ("王语嫣", ("research", "demand", "strategy", "decision", "five-step", "orchestr", "diagnos", "stage-", "collision", "orchestration")),
    ("欧阳锋", ("review", "check", "validation", "cross-validation", "attack", "pre-ship", "quality", "linter", "debug")),
    ("黄药师", ("config", "hermes", "agent", "self-evolution", "migration", "llm", "prompt", "parser", "document", "lib", "curator")),
    ("段王爷", ("publish", "feishu", "ship")),
]


def read_text(p: Path) -> str:
    # utf-8-sig：吃掉 BOM（部分 SKILL.md 带 BOM，会让 ^--- frontmatter 正则失配）
    return io.open(p, encoding="utf-8-sig", errors="replace").read()


def parse_frontmatter(text: str) -> dict:
    """取 YAML frontmatter 并 safe_load（P-18 铁律：禁手写解析器）。"""
    m = re.match(r"^---\s*\r?\n(.*?)\r?\n---\s*\r?\n", text, re.S)
    if not m:
        return {}
    try:
        data = yaml.safe_load(m.group(1))
        return data if isinstance(data, dict) else {}
    except yaml.YAMLError:
        return {}


def load_manifest(skill_dir: Path) -> dict:
    mf = skill_dir / "manifest.yaml"
    if not mf.exists():
        return {}
    try:
        data = yaml.safe_load(read_text(mf))
        return data if isinstance(data, dict) else {}
    except yaml.YAMLError:
        return {}


def scan_skills() -> list[dict]:
    """扫描全部 skill 目录（shared/ + 根目录），返回结构化记录。"""
    records = []
    if not SKILLS_DIR.exists():
        return records
    for d in sorted(SKILLS_DIR.iterdir()):
        if not d.is_dir():
            continue
        is_shared = d.name == "shared"
        scan_root = d
        location = "shared/" if is_shared else ""
        for sd in sorted(scan_root.iterdir()):
            if not sd.is_dir():
                continue
            sm = sd / "SKILL.md"
            if not sm.exists():
                continue  # 无 SKILL.md 不算 skill（如 README）
            fm = parse_frontmatter(read_text(sm))
            man = load_manifest(sd)
            name = str(fm.get("name") or man.get("name") or sd.name).strip().strip("'\"")
            desc = str(fm.get("description") or man.get("description") or "").strip().replace("\n", " ")
            trig = []
            for src in (fm.get("trigger"), man.get("trigger")):
                if isinstance(src, dict):
                    nl = src.get("natural_language") or []
                    if isinstance(nl, list):
                        trig.extend(str(x) for x in nl)
            adapted = fm.get("adapted_from") or man.get("adapted_from") or ""
            author = fm.get("author") or man.get("author") or ""
            records.append({
                "dir": sd.name,
                "name": name,
                "desc": desc,
                "triggers": trig,
                "adapted_from": str(adapted).strip(),
                "author": str(author).strip(),
                "location": (location + sd.name) if location else sd.name,
                "path": sd,
                "mtime": max(sm.stat().st_mtime, (sd / "manifest.yaml").stat().st_mtime if (sd / "manifest.yaml").exists() else 0),
            })
    return records


TOKEN_RE = re.compile(r"[A-Za-z0-9_\-]{3,}")


def tokens_of(text: str) -> set[str]:
    return set(TOKEN_RE.findall(text))


def scan_mounts(skill_names: set[str], alias: dict[str, str]) -> dict[str, dict]:
    """返回 mount_units：单元名 → {layer, files, skills:set[canonical_dir]}"""
    units: dict[str, dict] = {}

    def add_unit(unit: str, layer: str, path: Path):
        if unit not in units:
            units[unit] = {"layer": layer, "files": [], "skills": set(), "skill_files": {}}
        units[unit]["files"].append(str(path.relative_to(WIKI)))
        toks = tokens_of(read_text(path))
        for t in toks:
            canon = t if t in skill_names else alias.get(t)
            if canon:
                units[unit]["skills"].add(canon)
                units[unit]["skill_files"].setdefault(canon, []).append(path.name)

    # A. 六角色（role-routes 路由2 表）
    root_skill_names = {d.name for d in SKILLS_DIR.iterdir()
                        if d.is_dir() and d.name != "shared" and (d / "SKILL.md").exists()} if SKILLS_DIR.exists() else set()
    if ROLE_ROUTES.exists():
        for line in read_text(ROLE_ROUTES).splitlines():
            m = re.match(r"^\|\s*(黄药师|王语嫣|老顽童|欧阳锋|洪七公|段王爷)[^|]*\|([^|]*)\|", line)
            if m:
                role = m.group(1)
                if role not in units:
                    units[role] = {"layer": "角色路由(role-routes)", "files": [], "skills": set(), "skill_files": {}, "root_refs": set()}
                units[role].setdefault("root_refs", set())
                for t in tokens_of(m.group(2)):
                    canon = t if t in skill_names else alias.get(t)
                    if canon:
                        units[role]["skills"].add(canon)
                        units[role]["skill_files"].setdefault(canon, []).append("role-routes.md")
                    elif t in root_skill_names:
                        units[role]["root_refs"].add(t)  # 根目录 legacy skill 引用——不在 shared 登记面，显式登记不吞掉
                units[role]["files"].append("90_control/role-routes.md#路由2")

    # B. agent-specs
    if AGENT_SPECS_DIR.exists():
        for f in sorted(AGENT_SPECS_DIR.glob("*.md")):
            add_unit(f.stem, "agent-spec", f)

    # C. agents/ 实例
    if AGENTS_DIR.exists():
        for d in sorted(p for p in AGENTS_DIR.iterdir() if p.is_dir()):
            for fn in AGENT_SOURCE_FILES:
                f = d / fn
                if f.exists():
                    add_unit(d.name, "agents实例", f)
    return units


def status_of(n_units: int, in_routes: bool) -> str:
    if n_units >= 2 or in_routes:
        return "已挂载"
    if n_units == 1:
        return "单点挂载"
    return "无主"


def suggest_role(skill: dict, mounted: list[str]) -> str:
    if mounted:
        return "—"
    name = (skill["dir"] + " " + skill["desc"]).lower()
    for role, kws in ROLE_HINTS:
        if any(k.lower() in name for k in kws):
            return role
    return "待议"


def gen_index(skills: list[dict], mounted_by: dict[str, list[str]]) -> str:
    now = datetime.now().strftime("%Y-%m-%d %H:%M")
    L = []
    L.append("# Skills 目录索引（INDEX）")
    L.append("")
    L.append(f"> #588 扫描生成物（生成时间 {now}，共 {len(skills)} 个 skill）。")
    L.append("> **真相源 = 各 skill 的 SKILL.md frontmatter**；本文件是生成物，勿手改——")
    L.append("> 新增/下架 skill 后重跑 `python 40_outputs/code/scripts/scan_skills_registry.py` 刷新。")
    L.append("> 挂载现状对照见同目录 `MOUNT-MATRIX.md`；登记/维护归 Skills 助理（#587 分工表）。")
    L.append("")
    L.append(f"| # | skill | 一句话说明 | 触发词 | 来源卡 | 位置 | 已挂载 |")
    L.append("|--:|:--|:--|:--|:--|:--|:--|")
    for i, s in enumerate(skills, 1):
        trig = "；".join(s["triggers"][:4]) + ("…" if len(s["triggers"]) > 4 else "") if s["triggers"] else "（未登记，补 manifest.trigger.natural_language）"
        adapted = s["adapted_from"] or "（自建，无来源卡）"
        mounts = "、".join(mounted_by.get(s["dir"], [])) or "（无）"
        name_note = "" if s["name"] == s["dir"] else f"（frontmatter name={s['name']}）"
        L.append(f"| {i} | `{s['dir']}`{name_note} | {s['desc'][:80] or '—'} | {trig} | {adapted[:60] or '—'} | {s['location']} | {mounts} |")
    L.append("")
    L.append("## 待补登记（缺口清单，Skills 助理维护面）")
    no_trig = [s["dir"] for s in skills if not s["triggers"]]
    no_adapt = [s["dir"] for s in skills if not s["adapted_from"]]
    L.append(f"- 缺 trigger.natural_language：{len(no_trig)} 个（触发词路由不可用，建议按 anti-ai-bs-three-moves manifest 先例补）")
    L.append(f"- 缺 adapted_from 来源卡：{len(no_adapt)} 个")
    L.append(f"- frontmatter name 与目录名不一致：{[s['dir'] for s in skills if s['name'] != s['dir']]}")
    L.append("")
    return "\r\n".join(L) + "\r\n"


def gen_matrix(skills: list[dict], units: dict[str, dict]) -> str:
    now = datetime.now().strftime("%Y-%m-%d %H:%M")
    name_to_dir = {s["name"]: s["dir"] for s in skills}
    dir_set = set(name_to_dir.values())
    mounted_by: dict[str, list[str]] = {s["dir"]: [] for s in skills}
    routes_roles = {u for u, v in units.items() if v["layer"].startswith("角色路由")}
    for u, v in units.items():
        for sk in v["skills"]:
            if sk in dir_set and u not in mounted_by[sk]:
                mounted_by[sk].append(u)

    L = []
    L.append("# Agent × Skill 挂载矩阵（MOUNT-MATRIX）")
    L.append("")
    L.append(f"> #588 扫描生成物（生成时间 {now}）。**登记制：文件引用即挂载**（含历史引用，")
    L.append("> 与「实际运行时可用」可能有出入——引用面是登记真相源）。生成物勿手改，")
    L.append("> 重跑 `python 40_outputs/code/scripts/scan_skills_registry.py` 刷新；挂载变更走 #587 Skills 助理。")
    L.append("")
    # 表1：挂载单元 → 已挂 skill
    L.append("## 一、挂载单元清单（谁挂了什么）")
    L.append("")
    L.append("| 挂载单元 | 层 | 挂载 skill 数 | skill 清单 |")
    L.append("|:--|:--|--:|:--|")
    for u in sorted(units, key=lambda x: (units[x]["layer"], -len(units[x]["skills"]))):
        v = units[u]
        lst = "、".join(f"`{s}`" for s in sorted(v["skills"])) or "（无 skill 引用）"
        L.append(f"| {u} | {v['layer']} | {len(v['skills'])} | {lst} |")
    # 表2：skill → 挂载单元（含状态）
    L.append("")
    L.append("## 二、skill 对照表（状态三档：已挂载/单点挂载/无主）")
    L.append("")
    L.append("| skill | 状态 | 已挂载单元 | 可挂建议 |")
    L.append("|:--|:--|:--|:--|")
    counts = {"已挂载": 0, "单点挂载": 0, "无主": 0}
    for s in sorted(skills, key=lambda x: (status_of(len(mounted_by[x["dir"]]), bool(set(mounted_by[x["dir"]]) & routes_roles)), x["dir"])):
        st = status_of(len(mounted_by[s["dir"]]), bool(set(mounted_by[s["dir"]]) & routes_roles))
        counts[st] += 1
        ms = "、".join(mounted_by[s["dir"]]) or "（无）"
        sug = suggest_role(s, mounted_by[s["dir"]])
        L.append(f"| `{s['dir']}` | {st} | {ms} | {sug} |")
    # 表3：可挂未挂 actionable
    root_refs_all = sorted({r for v in units.values() for r in v.get("root_refs", set())})
    L.append("")
    L.append("## 三、可挂未挂清单（无主 + 单点挂载，actionable）")
    L.append("")
    if root_refs_all:
        L.append(f"- ℹ️ 角色路由另引用 {len(root_refs_all)} 个**根目录 legacy skill**（不在 shared/ 73 登记面，未计入上表）：{'、'.join(f'`{r}`' for r in root_refs_all)}——是否迁入 shared 归 Skills 助理裁定")
    L.append("")
    L.append(f"- **无主 skill：{counts['无主']} 个**（任何登记处零引用——先判定归属或明确废弃）")
    L.append(f"- **单点挂载：{counts['单点挂载']} 个**（仅 1 单元引用——评估是否值得推广挂载）")
    L.append(f"- **已挂载：{counts['已挂载']} 个**")
    orphans = [s for s in skills if status_of(len(mounted_by[s["dir"]]), bool(set(mounted_by[s["dir"]]) & routes_roles)) == "无主"]
    if orphans:
        L.append("")
        L.append("### 无主 skill 归属建议（关键词启发式，机械可审计；落地由 Skills 助理登记）")
        L.append("")
        for s in orphans:
            L.append(f"- `{s['dir']}` → 建议 {suggest_role(s, [])}")
    L.append("")
    L.append("## 四、挂载纪律（#587 SPEC §六 口径）")
    L.append("")
    L.append("- agent-spec 模板增补「已挂载skills」标准节，格式：`- skill-name: 用途一句话`（见 workflow-kdo-agent-production-pipeline Step 1/2）")
    L.append("- 挂载变更 = 三写一致：spec 节 / 本矩阵（重跑刷新）/ skill manifest 适用agent")
    L.append("- 挂载变更同步：王语嫣（编排视图）+ 黄药师（基建视图）；登记维护归 Skills 助理")
    L.append("")
    return "\r\n".join(L) + "\r\n"


def write_stale_marker() -> None:
    (SKILLS_DIR / ".registry-last-scan").write_text(datetime.now().isoformat(), encoding="utf-8")


def check_stale(skills: list[dict]) -> int:
    if not INDEX_FILE.exists() or not MATRIX_FILE.exists():
        print("🔴 INDEX.md / MOUNT-MATRIX.md 不存在——先跑一次全量生成")
        return 1
    newest = max((s["mtime"] for s in skills), default=0)
    reg_ts = INDEX_FILE.stat().st_mtime
    if newest > reg_ts:
        print(f"🔴 stale：SKILL.md/manifest 最新修改晚于 INDEX.md 生成时间——重跑 scan_skills_registry.py")
        return 1
    n_index = len(re.findall(r"^\| \d+ \|", read_text(INDEX_FILE), re.M))
    if n_index != len(skills):
        print(f"🔴 计数漂移：INDEX 行数 {n_index} ≠ 实测 skill {len(skills)}")
        return 1
    print(f"🟢 fresh：{len(skills)} skills，INDEX/MOUNT 与源一致")
    return 0


def main() -> int:
    ap = argparse.ArgumentParser(description="#588 skills 目录+挂载矩阵扫描")
    ap.add_argument("--check", action="store_true", help="只做新鲜度检查（stale→exit 1）")
    args = ap.parse_args()

    skills = scan_skills()
    if args.check:
        return check_stale(skills)

    alias = {s["name"]: s["dir"] for s in skills if s["name"] != s["dir"]}
    units = scan_mounts({s["dir"] for s in skills}, alias)
    mounted_by: dict[str, list[str]] = {s["dir"]: [] for s in skills}
    for u, v in units.items():
        for sk in v["skills"]:
            if sk in mounted_by and u not in mounted_by[sk]:
                mounted_by[sk].append(u)

    INDEX_FILE.write_text(gen_index(skills, mounted_by), encoding="utf-8", newline="")
    MATRIX_FILE.write_text(gen_matrix(skills, units), encoding="utf-8", newline="")
    write_stale_marker()

    print(f"✅ INDEX.md：{len(skills)} skills → {INDEX_FILE}")
    print(f"✅ MOUNT-MATRIX.md：{len(units)} 挂载单元 × {len(skills)} skills → {MATRIX_FILE}")
    st_counts = {"已挂载": 0, "单点挂载": 0, "无主": 0}
    routes_roles = {u for u, v in units.items() if v["layer"].startswith("角色路由")}
    for s in skills:
        st = status_of(len(mounted_by[s["dir"]]), bool(set(mounted_by[s["dir"]]) & routes_roles))
        st_counts[st] += 1
    print(f"   状态分布：已挂载 {st_counts['已挂载']} / 单点 {st_counts['单点挂载']} / 无主 {st_counts['无主']}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
