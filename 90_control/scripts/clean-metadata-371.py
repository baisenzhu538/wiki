#!/usr/bin/env python3
"""#371 正库元数据规范清洗——trust_level/type/status 枚举收敛 + domain 补全 + 重复键/缺字段。

用法：
    python 90_control/scripts/clean-metadata-371.py --dry-run    # 只统计+样本（默认）
    python 90_control/scripts/clean-metadata-371.py --apply      # 实际修改 frontmatter

规则（王语嫣裁定，2026-08-19）：
- trust_level: observed→medium, medium-high→high, medium-low→low, "medium#…"/"low#…"→#前部分, placeholder→medium
- type: dark-knowledge→dk
- status 归并: superseded→deprecated, revised/stable/approved→reviewed, active→enriched,
  proposed→draft, pending→pending_review, placeholder→draft, 缺省→draft
- domain 空: 文件名/目录 token 匹配合法 domain 值→填；否则 unknown（备案列表）
- 缺 type: 按 30_wiki 目录名映射（frameworks→framework 等）
- 重复键: yaml round-trip 去重（保留最后值）

只改 frontmatter，不动正文。
"""
import argparse
import json
import re
import shutil
import sys
import yaml
from collections import Counter
from pathlib import Path

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")

WIKI = Path(r"C:\Users\Administrator\Desktop\wiki")
WIKI_DIR = WIKI / "30_wiki"

TRUST_MAP = {
    "observed": "medium",
    "medium-high": "high",
    "medium-low": "low",
    "placeholder": "medium",
    "high#": "high", "medium#": "medium", "low#": "low",
}
STATUS_MAP = {
    "superseded": "deprecated",
    "revised": "reviewed",
    "stable": "reviewed",
    "approved": "reviewed",
    "active": "enriched",
    "proposed": "draft",
    "pending": "pending_review",
    "placeholder": "draft",
}
TYPE_DIR_MAP = {
    "frameworks": "framework", "tools": "tool", "cases": "case",
    "concepts": "concept", "dark-knowledges": "dk", "methods": "method",
    "systems": "system", "entities": "entity", "decisions": "decision",
    "projects": "project", "queries": "query", "domains": "domain",
    "agent-specs": "agent-spec", "skills": "skill",
}
VALID_DOMAINS = {
    "yitang", "src-unknown", "ai-collaboration", "design", "research", "management",
    "strategy", "master", "decision-science", "business-strategy", "ai-saas", "product",
    "kdo", "business-formula", "learning-methodology", "conversion-rate",
    "five-step-method", "healthcare", "modeling", "personal-os", "entrepreneurship",
    "decision-making", "content-production", "personal-growth", "sales",
    "sales-management", "demand-analysis", "growth", "cross-domain", "wanghuan",
    "yihang", "candy", "xuyang", "xujian", "guang", "ecommerce", "to-b",
    "wechat-collect", "serendipity", "patrolkit", "workflow", "agile", "okr",
}


# 高置信关键词规则（#371：yt- 前缀=一堂、医疗域等）
KEYWORD_RULES = [
    (re.compile(r"(^|[_-])yt([_-]|$)"), "yitang"),
    (re.compile(r"yitang"), "yitang"),
    (re.compile(r"(medicine|medical|smart-medicine|医疗|药柜|医院)"), "healthcare"),
    (re.compile(r"(人机协作|协作方法论|ai-collaboration)"), "ai-collaboration"),
    (re.compile(r"(^|[_-])ec([_-]|$)"), "ecommerce"),
    (re.compile(r"(supply-chain|供应链)"), "business-strategy"),
]


def infer_domain(path: Path, fm: dict) -> str | None:
    """Infer domain from filename/dir tokens + frontmatter fields."""
    hay = (path.name + " " + str(path.parent)).lower()
    for cand in sorted(VALID_DOMAINS, key=len, reverse=True):
        if cand in hay:
            return cand
    for field in ("aliases", "tags", "source_person"):
        v = fm.get(field)
        items = v if isinstance(v, list) else ([v] if isinstance(v, str) else [])
        for it in items:
            s = str(it).lower()
            for cand in sorted(VALID_DOMAINS, key=len, reverse=True):
                if cand in s:
                    return cand
    for rx, domain in KEYWORD_RULES:
        if rx.search(hay):
            return domain
    return None


def fix_trust(t: str) -> str:
    for k, v in TRUST_MAP.items():
        if t.startswith(k):
            return v
    return t


def collect_known_domains() -> dict[str, str]:
    """第一遍扫描：文件名/标题 → domain 映射（供 related 众数推断）。"""
    known: dict[str, str] = {}
    for p in sorted(WIKI_DIR.rglob("*.md")):
        if "_archive" in p.parts:
            continue
        try:
            raw = p.read_text(encoding="utf-8-sig", errors="replace")
            end = raw.find("\n---\n", 4)
            if end == -1:
                continue
            fm = yaml.safe_load(raw[4:end])
        except Exception:
            continue
        if not isinstance(fm, dict):
            continue
        d = fm.get("domain")
        if isinstance(d, str) and d.strip() and d.strip() != "unknown":
            known[p.stem] = d.strip()
            if fm.get("title"):
                known[str(fm["title"]).strip()] = d.strip()
            for a in (fm.get("aliases") or []):
                if isinstance(a, str):
                    known[a.strip()] = d.strip()
    return known


def infer_domain_from_related(fm: dict, known: dict[str, str]) -> str | None:
    """related/组件引用卡的 domain 众数推断。"""
    from collections import Counter
    cnt: Counter = Counter()
    refs = []
    for field in ("related", "component_of", "bridges_to"):
        v = fm.get(field)
        if isinstance(v, str):
            refs.append(v)
        elif isinstance(v, list):
            refs.extend(str(x) for x in v)
    for r in refs:
        r = r.strip()
        if r in known:
            cnt[known[r]] += 1
    if cnt:
        top, n = cnt.most_common(1)[0]
        if n >= 1 and top != "src-unknown":
            return top
    return None


def process_file(path: Path, apply: bool, report: dict, known_domains: dict[str, str] | None = None) -> None:
    raw = path.read_text(encoding="utf-8-sig", errors="replace")
    if not raw.startswith("---"):
        return
    end = raw.find("\n---\n", 4)
    if end == -1:
        return
    fm_text = raw[4:end]
    try:
        fm = yaml.safe_load(fm_text)
    except Exception:
        report["yaml_fail"].append(str(path.relative_to(WIKI)))
        return
    if not isinstance(fm, dict):
        return
    body = raw[end + 5:]

    changed = {}

    # trust_level
    t = fm.get("trust_level")
    if t is not None and t not in ("high", "medium", "low"):
        new_t = fix_trust(str(t))
        if new_t in ("high", "medium", "low"):
            changed["trust_level"] = (t, new_t)
            fm["trust_level"] = new_t

    # type: dark-knowledge -> dk
    if fm.get("type") == "dark-knowledge":
        changed["type"] = ("dark-knowledge", "dk")
        fm["type"] = "dk"
    elif not fm.get("type"):
        rel = str(path.relative_to(WIKI))
        parts = Path(rel).parts
        if len(parts) >= 2:
            inferred = TYPE_DIR_MAP.get(parts[1])
            if inferred:
                changed["type"] = ("<missing>", inferred)
                fm["type"] = inferred
            else:
                report["type_uninferrable"].append(rel)

    # status 归并（needs-review 是正式中间态，保留）
    st = fm.get("status")
    if st is None:
        changed["status"] = ("<missing>", "draft")
        fm["status"] = "draft"
    elif st not in ("reviewed", "deprecated", "draft", "pending_review", "enriched", "needs-review"):
        new_st = STATUS_MAP.get(st)
        if new_st:
            changed["status"] = (st, new_st)
            fm["status"] = new_st
        else:
            report["status_unmapped"].append((str(path.relative_to(WIKI)), st))

    # domain 补全：文件名/关键词 → related 卡众数 → unknown
    d = fm.get("domain")
    empty = d is None or (isinstance(d, list) and not d) or (isinstance(d, str) and not d.strip())
    if empty:
        inferred = infer_domain(path, fm)
        if not inferred and known_domains:
            inferred = infer_domain_from_related(fm, known_domains)
        if inferred:
            changed["domain"] = ("<empty>", inferred)
            fm["domain"] = inferred
        else:
            changed["domain"] = ("<empty>", "unknown")
            fm["domain"] = "unknown"
            report["domain_unknown"].append(str(path.relative_to(WIKI)))

    # 重复键：检测并去重（保留最后值）
    dup_keys = _detect_dup_keys(fm_text)
    if dup_keys:
        changed["dup_keys"] = dup_keys

    if not changed:
        return

    report["changed_files"] += 1
    for k, v in changed.items():
        report["changes"][k] = report["changes"].get(k, 0) + 1
    report["samples"].append({"file": str(path.relative_to(WIKI)), "changes": {k: str(v) for k, v in changed.items()}})

    if apply:
        new_fm = yaml.safe_dump(fm, allow_unicode=True, sort_keys=False, default_flow_style=False)
        path.write_text(f"---\n{new_fm}---\n{body}", encoding="utf-8")


def _detect_dup_keys(fm_text: str) -> list[str]:
    """文本级检测重复顶层 key（yaml 解析前的粗检测）。"""
    keys = []
    for line in fm_text.splitlines():
        m = re.match(r"^([A-Za-z_][\w-]*):", line)
        if m and not line.startswith(" "):
            keys.append(m.group(1))
    dup = [k for k in set(keys) if keys.count(k) > 1]
    return dup


def main():
    parser = argparse.ArgumentParser(description="#371 元数据清洗")
    parser.add_argument("--apply", action="store_true", help="实际修改（默认 dry-run）")
    args = parser.parse_args()

    report = {"changed_files": 0, "changes": {}, "samples": [], "domain_unknown": [],
              "yaml_fail": [], "status_unmapped": [], "type_uninferrable": []}

    known_domains = collect_known_domains()
    for p in sorted(WIKI_DIR.rglob("*.md")):
        if "_archive" in p.parts:
            continue  # 归档目录不在正库清洗范围
        process_file(p, args.apply, report, known_domains)

    print(f"mode: {'APPLY' if args.apply else 'DRY-RUN'} | 变更文件: {report['changed_files']}")
    print("变更统计:", json.dumps(report["changes"], ensure_ascii=False))
    print(f"domain 推断失败标 unknown: {len(report['domain_unknown'])}")
    print(f"yaml 解析失败: {len(report['yaml_fail'])} | status 未映射: {len(report['status_unmapped'])} | type 未推断: {len(report['type_uninferrable'])}")
    print("样本（前 8）:")
    for s in report["samples"][:8]:
        print("  ", s["file"], s["changes"])
    if report["status_unmapped"]:
        print("status 未映射:", report["status_unmapped"][:8])
    if report["domain_unknown"]:
        Path(WIKI / "_tmp_m371_domain_unknown.txt").write_text("\n".join(report["domain_unknown"]), encoding="utf-8")
        print(f"domain unknown 备案 → _tmp_m371_domain_unknown.txt")


if __name__ == "__main__":
    main()
