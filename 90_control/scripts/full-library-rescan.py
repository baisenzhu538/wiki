#!/usr/bin/env python3
"""
full-library-rescan.py — 全库复扫标准工具（#399）

消灭"清单口径归零冒充全库归零"（#391/#393 连续复发）：对指定"修复类别"
扫**全库**（30_wiki 全部 md，yaml 级解析），输出剩余清单或确认 =0。

**纪律（#399 固化）**：任务报告/退回意见中任何"全库归零/复扫确认"声明
必须附本脚本输出，否则终审可据此直接 FAIL。

用法：
    python full-library-rescan.py                     # 全检查项全库跑
    python full-library-rescan.py --check missing-tags-dim --domain yitang
    python full-library-rescan.py --check all --json  # JSON 输出（供 health-check/agent 消费）
    python full-library-rescan.py --delta <baseline>  # 增量报警：基线为 0 的项变 >0 才报

退出码：任一项 剩余 N>0 → 1（可被门禁/脚本链调用）；全 0 → 0。

检查项（可插拔，注册于 CHECKS 表）：
- missing-updated-at : frontmatter 缺 updated_at
- missing-tags-dim   : tags 缺 audience/scene 维度（--domain 按 domain 列表精确匹配）
- dead-source-refs   : source_refs 指向不可达路径（文件不存在 / pending_archive）
- body-fm-style-links: body（`---` 之后）行首 `- '[[` 前缀行
- related-asymmetry  : related 单向链（A 链 B 但 B 有 related 却未回链）
- parse-error        : YAML 解析失败的卡（**不得伪装归零**——#393 A- 盲区）

设计口径：
- yaml 级解析，禁正则凑数（E017）
- --domain = domain 列表**精确包含**目标域（#393 P1：只取 domain[0] 漏多 domain 卡）
- 解析失败显式列入 parse-error，不算入其他检查项（#393 A-：解析器口径 ≠ 全库口径）
"""

import argparse
import json
import sys
from pathlib import Path

VAULT_ROOT = Path(__file__).resolve().parent.parent.parent
WIKI_DIR = VAULT_ROOT / "30_wiki"
IGNORE_PARTS = {"_archive", "_tmp", "raw", "_vlm_output", "__pycache__"}

try:
    import yaml
except ImportError:
    yaml = None


def safe_read(path: Path) -> str | None:
    """多编码容错读取（utf-8 优先，历史 GBK/混合编码兜底）。"""
    for enc in ("utf-8", "gbk", "latin-1"):
        try:
            return path.read_text(encoding=enc)
        except (UnicodeDecodeError, OSError):
            continue
    return None


def parse_fm(text: str) -> tuple[dict | None, str | None, str | None, int]:
    """返回 (frontmatter dict, error, body, body_start_line)。body_start_line = body 第 1 行的文件行号。"""
    if not text.startswith("---"):
        return None, "no frontmatter", text, 1
    end = text.find("\n---\n", 4)
    if end == -1:
        return None, "unclosed frontmatter", None, 1
    fm_text = text[4:end]
    body = text[end + 5 :]
    body_start = text[:end].count("\n") + 3  # ---\n...\n---\n → body 首行在文件中的行号
    if yaml is None:
        return None, "PyYAML not installed", body, body_start
    try:
        fm = yaml.safe_load(fm_text)
        if not isinstance(fm, dict):
            return {}, "frontmatter not a dict", body, body_start
        return fm, None, body, body_start
    except Exception as e:
        return None, f"YAML parse error: {e}", body, body_start


def collect_cards() -> list[dict]:
    """全库扫描一次，缓存解析结果。返回卡片列表。"""
    cards = []
    for fp in sorted(WIKI_DIR.rglob("*.md")):
        if any(p in IGNORE_PARTS for p in fp.parts):
            continue
        rel = fp.relative_to(VAULT_ROOT).as_posix()
        text = safe_read(fp)
        if text is None:
            cards.append({"rel": rel, "id": fp.stem, "fm": None, "err": "read error", "body": None, "body_start": 1})
            continue
        fm, err, body, body_start = parse_fm(text)
        card_id = str(fm.get("id", fp.stem)).strip() if fm else fp.stem
        cards.append({"rel": rel, "id": card_id, "fm": fm, "err": err, "body": body, "body_start": body_start})
    return cards


def in_domain(card: dict, domain: str) -> bool:
    """domain 列表精确包含目标域（列表化后精确匹配）。"""
    fm = card["fm"]
    if not fm:
        return False
    d = fm.get("domain", [])
    if isinstance(d, str):
        d = [d]
    if not isinstance(d, list):
        return False
    return domain in [str(x).strip() for x in d]


def norm_tag_list(fm: dict) -> list[str]:
    tags = fm.get("tags", [])
    if isinstance(tags, str):
        tags = [tags]
    if not isinstance(tags, list):
        return []
    return [str(t).strip() for t in tags if str(t).strip()]


# ── 检查项实现（签名：fn(cards) -> list[str] 违规行）───────────────────


def check_missing_updated_at(cards):
    out = []
    for c in cards:
        if c["err"] or not c["fm"]:
            continue
        ua = c["fm"].get("updated_at")
        if not ua or not str(ua).strip().strip("'\""):
            out.append(f"{c['rel']} (缺 updated_at)")
    return out


def check_missing_tags_dim(cards):
    out = []
    for c in cards:
        if c["err"] or not c["fm"]:
            continue
        tags = norm_tag_list(c["fm"])
        has_audience = any(t.startswith("audience:") for t in tags)
        has_scene = any(t.startswith("scene:") for t in tags)
        if not has_audience or not has_scene:
            missing = [x for x, ok in (("audience", has_audience), ("scene", has_scene)) if not ok]
            out.append(f"{c['rel']} (tags 缺 {'/'.join(missing)} 维度)")
    return out


def is_file_path(ref: str) -> bool:
    s = ref.strip()
    if s.startswith("[["):
        return False
    if s.startswith(("http://", "https://")):
        return False  # URL 不是文件 source，由他类管理
    if s.startswith("src_") and "/" not in s:
        return False
    return "/" in s or s.endswith(".md") or s.endswith(".txt") or s.endswith(".pdf")


def _strip_locator(s: str) -> str:
    """剥尾部定位后缀：'path L14' / 'path L946-1278' / 'path §一' / 'path - src_unknown'。"""
    import re
    s = re.sub(r"\s+- src_unknown$", "", s.strip())
    s = re.sub(r"\s+L\d+(-\d+)?$", "", s)
    s = re.sub(r"\s+§\S+$", "", s)
    s = re.sub(r"\s+第[一二三四五六七八九十0-9]+[章节条]$", "", s)
    return s.strip()


def _resolve_ref(s: str) -> list[Path]:
    """source_ref → 候选路径列表。相对路径先试 vault 根、再试桌面级（复盘目录）。"""
    s = _strip_locator(s)
    if "*" in s or "?" in s:
        if ":" in s:  # 绝对路径带通配符
            return list(Path(s).parent.glob(Path(s).name))
        hits = list(VAULT_ROOT.glob(s))
        if not hits:
            hits = list(VAULT_ROOT.parent.glob(s))
        return hits
    if ":" in s:  # 绝对路径
        return [Path(s)]
    candidates = [VAULT_ROOT / s, VAULT_ROOT.parent / s]
    return candidates


def check_dead_source_refs(cards):
    out = []
    for c in cards:
        if c["err"] or not c["fm"]:
            continue
        refs = c["fm"].get("source_refs", [])
        if isinstance(refs, str):
            refs = [refs]
        if not isinstance(refs, list):
            continue
        for ref in refs:
            s = str(ref).strip()
            if not s:
                continue
            if "pending_archive" in s:
                out.append(f"{c['rel']} (source_refs 指向 pending_archive: {s[:80]})")
                continue
            if "src_unknown" in s:
                continue  # #391 合法占位标记
            if is_file_path(s):
                hits = _resolve_ref(s)
                if not any(p.exists() for p in hits):
                    out.append(f"{c['rel']} (source_refs 死路径: {_strip_locator(s)[:80]})")
    return out


def check_body_fm_style_links(cards):
    out = []
    for c in cards:
        if c["err"] or not c["body"]:
            continue
        for i, line in enumerate(c["body"].splitlines(), 1):
            stripped = line.strip()
            if stripped.startswith("- '[[") or stripped.startswith('- "[['):
                out.append(f"{c['rel']}:{c['body_start'] + i - 1} (body 行首 `- '[['` 前缀)")
    return out


def _norm_link(raw: str) -> str:
    """归一化 related 值 → 纯 id 候选：[[x]] / [[x|别名]] / "x" → x"""
    s = str(raw).strip().strip("'\"").strip()
    if s.startswith("[[") and s.endswith("]]"):
        s = s[2:-2]
    return s.split("|")[0].strip()


def check_related_asymmetry(cards):
    """A 链 B 但 B 有 related 却未回链 A。B 无 related 字段 → 系统页/不回链型，跳过。"""
    by_id = {}
    for c in cards:
        for k in {c["id"], c["rel"].rsplit("/", 1)[-1].removesuffix(".md")}:
            lst = by_id.setdefault(k, [])
            if c not in lst:
                lst.append(c)

    related_of = {}
    for c in cards:
        if c["err"] or not c["fm"]:
            continue
        rel = c["fm"].get("related", [])
        if isinstance(rel, str):
            rel = [rel]
        if not isinstance(rel, list):
            continue
        related_of[c["rel"]] = {_norm_link(x) for x in rel if str(x).strip() and not str(x).strip().startswith("<<<")}

    out = []
    seen = set()
    for c in cards:
        targets = related_of.get(c["rel"])
        if not targets:
            continue
        for t in targets:
            if t == c["id"]:
                continue
            for b in by_id.get(t, []):
                if b["rel"] == c["rel"]:
                    continue
                if "/60_feedback/" in c["rel"] or "/60_feedback/" in b["rel"]:
                    continue  # 会话记录/usage-log 非正式卡，不要求回链
                b_related = related_of.get(b["rel"])
                if b_related is None:  # B 无 related 字段：不回链型页面，不算违规
                    continue
                pair = (c["rel"], b["rel"])
                if pair in seen:
                    continue
                if c["id"] not in b_related and c["rel"].rsplit("/", 1)[-1].removesuffix(".md") not in b_related:
                    seen.add(pair)
                    out.append(f"{c['rel']} → {b['rel']} (单向链，缺回链)")
    return out


def check_parse_error(cards):
    out = []
    for c in cards:
        if c["err"]:
            out.append(f"{c['rel']} ({c['err']})")
    return out


# 注册表：可插拔，新增类别在此注册即可
CHECKS = {
    "missing-updated-at": ("frontmatter 缺 updated_at", check_missing_updated_at),
    "missing-tags-dim": ("tags 缺 audience/scene 维度", check_missing_tags_dim),
    "dead-source-refs": ("source_refs 不可达路径", check_dead_source_refs),
    "body-fm-style-links": ("body 行首 - '[[' 前缀行", check_body_fm_style_links),
    "related-asymmetry": ("related 单向链", check_related_asymmetry),
    "parse-error": ("YAML 解析失败（不得伪装归零）", check_parse_error),
}


def fmt_list(items: list[str], limit: int = 50) -> str:
    """N≤50 全列，>50 列前后各 25 + 总数。"""
    n = len(items)
    if n == 0:
        return "剩余 0"
    if n <= limit:
        listing = "\n".join(f"    {x}" for x in items)
        return f"剩余 {n}\n{listing}"
    head = "\n".join(f"    {x}" for x in items[: limit // 2])
    tail = "\n".join(f"    {x}" for x in items[-(limit // 2):])
    return f"剩余 {n}（共 {n} 条，列前后各 {limit // 2}）\n{head}\n    ...（中间 {n - limit} 条省略）...\n{tail}"


def run_checks(cards, names, domain) -> dict[str, list[str]]:
    scoped = cards
    if domain:
        scoped = [c for c in cards if in_domain(c, domain)]
    results = {}
    for name in names:
        _, fn = CHECKS[name]
        if name == "parse-error":
            # 解析失败卡的 domain 不可知——永不全库列出，不被域过滤藏起来
            #（#393 A-：yihang/一堂 因解析失败被跳过 = 归零是"解析器口径"）
            results[name] = fn(cards)
        else:
            results[name] = fn(scoped)
    return results


def load_baseline(path: Path) -> dict | None:
    if not path.exists():
        return None
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except Exception:
        return None


def save_baseline(path: Path, results: dict[str, list[str]]):
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(
        json.dumps({k: v for k, v in results.items()}, ensure_ascii=False, separators=(",", ":")),
        encoding="utf-8",
    )


def main() -> int:
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")

    p = argparse.ArgumentParser(description="KDO 全库复扫标准工具（#399）")
    p.add_argument("--check", default="all", help="逗号分隔检查项名，默认 all")
    p.add_argument("--domain", help="仅扫 domain 列表精确包含该域的卡（#393 口径）")
    p.add_argument("--json", action="store_true", help="JSON 输出")
    p.add_argument("--baseline", type=Path, help="保存当前各检查项计数为基线（json）")
    p.add_argument("--delta", type=Path, help="增量报警：只报基线为 0 的项现在 >0 的（0→N）")
    args = p.parse_args()

    if yaml is None:
        print("ERROR: PyYAML is required. Install with: pip install pyyaml", file=sys.stderr)
        return 1

    names = [x.strip() for x in args.check.split(",") if x.strip()]
    if names == ["all"] or "all" in names:
        names = list(CHECKS.keys())
    unknown = [n for n in names if n not in CHECKS]
    if unknown:
        print(f"未知检查项: {', '.join(unknown)}。可选: {', '.join(CHECKS)}", file=sys.stderr)
        return 1

    cards = collect_cards()
    results = run_checks(cards, names, args.domain)
    nonzero = {k: v for k, v in results.items() if v}

    if args.baseline:
        save_baseline(args.baseline, results)
        print(f"基线已保存: {args.baseline}")
        for k, v in results.items():
            print(f"  {k}: 剩余 {len(v)}")

    if args.delta:
        base = load_baseline(args.delta)
        if base is None:
            save_baseline(args.delta, results)
            print(f"[full-library-rescan] 首次建档（无基线），已保存: {args.delta}")
            return 0
        # 文件级增量报警：当前违规文件不在基线清单 → 新增违规（覆盖 0→N 语义）
        alarms = {}
        for k, v in results.items():
            base_files = set(base.get(k, []))
            fresh = [f for f in v if f not in base_files]
            if fresh:
                alarms[k] = fresh
        if not alarms:
            print("[full-library-rescan] 增量检查: 无新增违规（PASS）")
            return 0
        print("[full-library-rescan] 增量检查: 存在新增违规（FAIL）")
        for k, v in alarms.items():
            print(f"  [{k}]")
            print(fmt_list(v))
        return 1

    if args.json:
        print(json.dumps({k: {"count": len(v), "files": v} for k, v in results.items()}, ensure_ascii=False, indent=2))
        return 1 if nonzero else 0

    scope = f" --domain={args.domain}" if args.domain else ""
    print(f"[full-library-rescan] 全库复扫（{len(cards)} 文件{scope}）")
    has_fail = False
    for name in names:
        items = results[name]
        block = fmt_list(items)
        has_fail = has_fail or bool(items)
        print(f"  {name:<22}: {block.splitlines()[0]}")
        if len(block.splitlines()) > 1:
            print("\n".join("    " + l if not l.startswith("  ") else l for l in block.splitlines()[1:]))
    print()
    print("归零声明纪律（#399）：任何「全库归零/复扫确认」声明必须附本脚本输出。")
    print("Status:", "FAIL" if has_fail else "PASS")
    return 1 if has_fail else 0


if __name__ == "__main__":
    sys.exit(main())
