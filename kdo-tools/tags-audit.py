#!/usr/bin/env python3
"""tags-audit.py — 全库标签摸底体检（#474，只读零修改）

四项指标：
  ① 脏词残留   STRONG 子串硬命中（为空/空值/不存在/未备份）+ PATTERN 正则断言句；
                SOFT（截断/损坏/乱码/半写）只统计频次供误报率观察，不进脏词率分母
                （风清扬三层分档口径：正向核查声明里这些词高频，子串硬拦是自伤）
  ② 来源轴缺失 有 source_person/source_context 但 tags 无来源词的卡
  ③ 无轴域地图 按 domain 字段聚合卡数，标记词池轴域（human-insights/decision-making/ai-collaboration）
  ④ 空值与格式 tags 缺失/null/空列表/非列表格式

产出：90_control/tags-audit-20260823.md（体检报告）
用法：python kdo-tools/tags-audit.py [--domain <d>]（限定域，用于 L2 对账）
"""

from __future__ import annotations

import argparse
import re
import sys
from collections import Counter, defaultdict
from pathlib import Path

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")

WIKI_ROOT = Path(__file__).resolve().parent.parent
CARDS_DIR = WIKI_ROOT / "30_wiki"
REPORT_PATH = WIKI_ROOT / "90_control" / "tags-audit-20260823.md"

# ① 三层分档（#474 吸收 diag_20260823_fengqingyang-negative-gate-vocab-review 口径）
STRONG_WORDS = ["为空", "空值", "不存在", "未备份"]
PATTERN_RE = re.compile(r"(?:字段|值|数据|内容|文件).{0,6}(?:为空|损坏|截断|乱码|半写)")
SOFT_WORDS = ["截断", "损坏", "乱码", "半写"]  # 只观察频次，不进脏词率分母

# ①b 课程名/来源混入脏词（#426 迁移映射思路：课程名禁入 tags，source_refs 唯一归宿）
COURSE_END_RE = re.compile(r".*课$")            # 实操课/系列课/情报调研课
COURSE_PREFIX_RE = re.compile(r".+之.+")         # X之Y 课程名前缀（五步法之需求分析）
COURSE_INST_RE = re.compile(r"训练营|公开课|直播课")
SRC_MIX_RE = re.compile(r"口述|live|拆书|开放麦")  # 来源词混入内容 tag（纯来源词是受控的）
LONG_TAG_LEN = 12                                # 超长短语 SOFT 观察线

# ② 来源词池（拆书/Live/开放麦等来源类标注）
SOURCE_WORDS = ["拆书", "live", "开放麦", "半肥猫", "楚门", "一堂", "口述", "直播"]

# ③ 词池轴域（已有受控轴的域）
AXIS_DOMAINS = {"human-insights", "decision-making", "ai-collaboration"}


def read_frontmatter(fp: Path, max_lines: int = 300) -> dict | None:
    """逐行读到第二个 ---（frontmatter 可超 1500B，截断解析=yaml 崩溃——#168 教训）。"""
    try:
        with fp.open("r", encoding="utf-8", errors="ignore") as f:
            lines = []
            for i, line in enumerate(f):
                if i == 0 and not line.startswith("---"):
                    return None
                if i > 0 and line.startswith("---"):
                    break
                if i > max_lines:
                    return None
                lines.append(line)
    except OSError:
        return None
    try:
        import yaml
        return yaml.safe_load("".join(lines)) or {}
    except Exception:
        return None


def tags_text(tags) -> str:
    if isinstance(tags, list):
        return " ".join(str(t) for t in tags)
    return str(tags) if tags is not None else ""


def scan_cards(domain_filter: str | None = None):
    """全库卡扫描，返回 (cards, skipped)。cards=[(path, fm)]。"""
    cards = []
    for fp in sorted(CARDS_DIR.rglob("*.md")):
        fm = read_frontmatter(fp)
        if not fm:
            continue
        if domain_filter:
            dom = fm.get("domain") or []
            if isinstance(dom, str):
                dom = [dom]
            if not any(domain_filter in str(d) or ("科学决策" in str(d) and domain_filter in ("decision", "决策")) for d in dom):
                continue
        cards.append((fp, fm))
    return cards


def audit(cards) -> dict:
    dirty = []           # (path, word, level) 负向断言类
    dirty_course = []    # (path, tag, reason) 课程名/来源混入类
    long_hits = Counter()  # 超长短语 SOFT 观察
    source_missing = []  # (path, source_person, source_context)
    domain_counts = Counter()
    empty_bad = []      # (path, reason)
    soft_hits = Counter()
    total = len(cards)

    for fp, fm in cards:
        dom = fm.get("domain") or []
        if isinstance(dom, str):
            dom = [dom]
        for d in dom:
            domain_counts[str(d)] += 1

        t = fm.get("tags")
        txt = tags_text(t)

        # ① 脏词·负向断言类（三层分档）
        for w in STRONG_WORDS:
            if w in txt:
                dirty.append((fp, w, "STRONG"))
        if PATTERN_RE.search(txt):
            m = PATTERN_RE.search(txt)
            dirty.append((fp, m.group(0), "PATTERN"))
        for w in SOFT_WORDS:
            if w in txt:
                soft_hits[w] += 1

        # ①b 脏词·课程名/来源混入类（#426 迁移映射思路）
        if isinstance(t, list):
            for tag in t:
                tag = str(tag)
                if COURSE_END_RE.match(tag):
                    dirty_course.append((fp, tag, "课程名结尾（禁入 tags，source_refs 唯一归宿）"))
                elif COURSE_PREFIX_RE.match(tag):
                    dirty_course.append((fp, tag, "X之Y 课程名前缀（应拆为内容词）"))
                elif COURSE_INST_RE.search(tag):
                    dirty_course.append((fp, tag, "训练营/公开课形态"))
                elif len(tag) > 6 and SRC_MIX_RE.search(tag):
                    dirty_course.append((fp, tag, "来源词混入内容 tag（应拆出来源词）"))
                elif len(tag) > LONG_TAG_LEN:
                    long_hits[">12字符"] += 1

        # ② 来源轴缺失
        sp = fm.get("source_person")
        sc = fm.get("source_context")
        if (sp or sc) and not any(w in txt.lower() for w in SOURCE_WORDS):
            source_missing.append((fp, sp, sc))

        # ④ 空值与格式
        if t is None:
            empty_bad.append((fp, "tags 缺失"))
        elif isinstance(t, str) and not t.strip():
            empty_bad.append((fp, "tags 空字符串"))
        elif t == []:
            empty_bad.append((fp, "tags 空列表"))
        elif isinstance(t, str) and "," in t:
            empty_bad.append((fp, "tags 字符串含逗号（应为 YAML 列表）"))

    return {
        "total": total,
        "dirty": dirty,
        "dirty_course": dirty_course,
        "dirty_rate": round((len(dirty) + len(dirty_course)) / total * 100, 1) if total else 0,
        "soft_hits": dict(soft_hits),
        "long_hits": dict(long_hits),
        "source_missing": source_missing,
        "domain_counts": domain_counts,
        "empty_bad": empty_bad,
        "empty_rate": round(len(empty_bad) / total * 100, 1) if total else 0,
    }


def main() -> int:
    ap = argparse.ArgumentParser(description="全库标签摸底体检（#474，只读零修改）")
    ap.add_argument("--domain", default=None, help="限定域（L2 对账用），如 decision")
    args = ap.parse_args()

    cards = scan_cards(args.domain)
    r = audit(cards)
    print(f"扫描 {r['total']} 卡")
    print(f"① 脏词: 负向断言 {len(r['dirty'])} + 课程名/来源混入 {len(r['dirty_course'])}（脏词率 {r['dirty_rate']}%）| SOFT 观察: {r['soft_hits']} / 超长短语 {r['long_hits']}")
    print(f"② 来源轴缺失: {len(r['source_missing'])}")
    print(f"③ 域分布: {len(r['domain_counts'])} 个域，词池轴域: {sorted(set(r['domain_counts']) & AXIS_DOMAINS)}")
    print(f"④ 空值/格式异常: {len(r['empty_bad'])}（空值率 {r['empty_rate']}%）")

    if not args.domain:
        _write_report(r)
        print(f"体检报告已写: {REPORT_PATH}")
    return 0


def _write_report(r: dict) -> None:
    from datetime import datetime
    lines = [
        "# 全库标签摸底体检报告（#474 · 2026-08-23）",
        "",
        f"- 生成时间: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}（治理进行中——数字随 #426 批次变动，收官以复扫归零为终态口径）",
        f"- 扫描范围: `30_wiki/` 全部卡（{r['total']} 张，只读零修改）",
        f"- 脏词率: 负向断言 {len(r['dirty'])} + 课程名/来源混入 {len(r['dirty_course'])}（{r['dirty_rate']}%）| SOFT 观察: {r['soft_hits']} / 超长短语 {r['long_hits']}",
        f"- 来源轴缺失: {len(r['source_missing'])} 张",
        f"- 空值/格式异常: {len(r['empty_bad'])} 张（{r['empty_rate']}%）",
        "",
        "## ①a 脏词·负向断言清单（STRONG+PATTERN，三层分档口径）",
    ]
    if not r["dirty"]:
        lines.append("- 无")
    for fp, word, level in r["dirty"][:50]:
        lines.append(f"- `{fp.relative_to(WIKI_ROOT)}` [{level}] `{word}`")
    if len(r["dirty"]) > 50:
        lines.append(f"- …共 {len(r['dirty'])} 条")
    lines += ["", "## ①b 脏词·课程名/来源混入清单（#426 迁移映射口径，按域分组）", ""]
    by_domain = defaultdict(list)
    for fp, tag, reason in r["dirty_course"]:
        fm = read_frontmatter(fp)
        dom = (fm or {}).get("domain") or []
        by_domain[", ".join(dom[:2]) if isinstance(dom, list) else str(dom)].append((fp, tag, reason))
    if not r["dirty_course"]:
        lines.append("- 无")
    for dom, items in sorted(by_domain.items()):
        lines.append(f"### {dom or '未知域'}（{len(items)}）")
        for fp, tag, reason in items[:15]:
            lines.append(f"- `{fp.relative_to(WIKI_ROOT)}` `{tag}` — {reason}")
        if len(items) > 15:
            lines.append(f"- …共 {len(items)} 条")
    lines += ["", "## ② 来源轴缺失清单", ""]
    if not r["source_missing"]:
        lines.append("- 无")
    for fp, sp, sc in r["source_missing"][:50]:
        lines.append(f"- `{fp.relative_to(WIKI_ROOT)}` source_person={sp or '-'} source_context={str(sc or '')[:40]}")
    if len(r["source_missing"]) > 50:
        lines.append(f"- …共 {len(r['source_missing'])} 条")
    lines += ["", "## ③ 域地图（有轴/无轴）", "", "| 域 | 卡数 | 词池轴 |", "|:--|--:|:--|"]
    for dom, n in r["domain_counts"].most_common():
        axis = "✅" if dom in AXIS_DOMAINS else "—"
        lines.append(f"| {dom} | {n} | {axis} |")
    lines += ["", "## ④ 空值/格式异常清单", ""]
    if not r["empty_bad"]:
        lines.append("- 无")
    for fp, reason in r["empty_bad"][:50]:
        lines.append(f"- `{fp.relative_to(WIKI_ROOT)}`: {reason}")
    if len(r["empty_bad"]) > 50:
        lines.append(f"- …共 {len(r['empty_bad'])} 条")
    lines += ["", "## 治理优先级建议", "",
              "- 脏词/空值: 按域分批治理（#426 模式放量，首批已归零的决策域为模板）",
              "- 来源轴缺失: 建议批量补来源词（拆书/Live/开放麦批次）",
              "- 无轴域: 词池轴建设随素材驱动（#426 词表 v0.3 六轴可复用）",
              "",
              "*tags-audit.py 生成 · #474 · 只读扫描零修改*", ""]
    REPORT_PATH.write_text("\n".join(lines), encoding="utf-8")


if __name__ == "__main__":
    sys.exit(main())
