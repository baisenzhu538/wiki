#!/usr/bin/env python3
"""
卡片复审自检——提交欧阳锋审查前必须跑，漏一项不交。

用法:
  python card_review_checklist.py <card_path> [card_path ...]

检查项: YAML / TITLE / TYPE / DS / RELATED(>=5) / RELATED_DEAD(全解析) / POSITION / REVIEW_DATE / 类型专属段
退出码: 0 = 全部通过, 1 = 有缺口
"""
import argparse, re, sys, yaml
from pathlib import Path

VAULT_ROOT = Path(__file__).resolve().parent.parent.parent
FM_RE = re.compile(r"^---\s*\n(.*?)\n---\s*\n", re.DOTALL)


def build_all_ids():
    ids = set()
    for fp in VAULT_ROOT.rglob("30_wiki/**/*.md"):
        if "_archive" in str(fp) or "raw" in str(fp):
            continue
        try:
            t = fp.read_text(encoding="utf-8", errors="replace")
            m = FM_RE.match(t)
            if not m:
                continue
            fm = yaml.safe_load(m.group(1))
            if fm:
                cid = fm.get("id", "")
                if cid:
                    ids.add(cid)
            ids.add(fp.stem)
        except:
            pass
    return ids


def clean_wikilink(raw):
    """Extract card ID from a wikilink like [[target]] or [[target|alias]] or quoted variants."""
    s = str(raw).strip()
    s = s.replace('"', '').replace("'", "")
    s = s.removeprefix("[[").removesuffix("]]")
    if "|" in s:
        s = s.split("|")[0]
    return s.strip()


def check_card(fp, all_ids):
    results = {}
    text = fp.read_text(encoding="utf-8", errors="replace")
    m = FM_RE.match(text)
    if not m:
        return {"YAML": (False, "no frontmatter")}
    fm_text, body = m.group(1), text[m.end():]

    try:
        yaml.safe_load(fm_text)
        results["YAML"] = (True, "")
    except Exception as e:
        results["YAML"] = (False, str(e)[:80])
        return results

    fm = yaml.safe_load(fm_text) or {}

    title = str(fm.get("title", "")).strip()
    results["TITLE"] = (bool(title), "empty" if not title else title[:60])

    ctype = str(fm.get("type", "")).strip()
    results["TYPE"] = (bool(ctype), ctype)

    ds = fm.get("diagnostic_signals", [])
    if isinstance(ds, str):
        ds = [ds]
    has_ds = bool(ds and len(ds) >= 1)
    results["DS"] = (has_ds, f"{len(ds) if isinstance(ds, list) else 0} signals")

    related = fm.get("related", [])
    if isinstance(related, str):
        related = [r for r in related.split(",") if r.strip()]
    has_rel = len(related) >= 5
    results["RELATED"] = (has_rel, f"{len(related)} links (need >=5)")

    if all_ids and related:
        dead = []
        for r in related:
            target = clean_wikilink(r)
            if target and target not in all_ids:
                dead.append(target)
        results["RELATED_DEAD"] = (
            len(dead) == 0,
            f"{len(dead)} dead: {dead[:3]}" if dead else "all resolve",
        )

    has_pos = bool(re.search(r'> \*\*定位\*\*', body))
    results["POSITION"] = (has_pos, "" if has_pos else "missing O8 positioning block")

    rd = str(fm.get("review_date", "")).strip()
    results["REVIEW_DATE"] = (bool(rd), rd if rd else "missing")

    if ctype == "dk":
        has = "## 与其他知识的关联" in body
        results["DK_EXTRA"] = (has, "" if has else "missing ## 与其他知识的关联")
    elif ctype == "tool":
        has_c = "## Critique" in body
        has_f = "## 失败模式" in body
        results["TOOL_EXTRA"] = (
            has_c and has_f,
            f"Critique={'YES' if has_c else 'NO'}, 失败模式={'YES' if has_f else 'NO'}",
        )
    elif ctype == "workflow":
        sections = ["使用场景", "操作步骤", "适用边界", "为什么值钱", "与其他知识的关联", "Critique"]
        missing = [s for s in sections if f"## {s}" not in body]
        results["WORKFLOW_EXTRA"] = (
            len(missing) == 0,
            f"missing: {missing}" if missing else "all 6 present",
        )

    return results


def main():
    p = argparse.ArgumentParser(description="Card review readiness self-check")
    p.add_argument("cards", nargs="+", help="Card paths to check")
    args = p.parse_args()
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")

    all_ids = build_all_ids()
    all_pass = True
    for path in args.cards:
        fp = Path(path)
        if not fp.is_absolute():
            fp = VAULT_ROOT / path
        if not fp.exists():
            print(f"MISSING: {path}")
            all_pass = False
            continue

        results = check_card(fp, all_ids)
        fails = [k for k, (ok, _) in results.items() if not ok]
        status = "PASS" if not fails else f"FAIL ({', '.join(fails)})"

        print(f"\n{'='*50}")
        print(f"  {fp.name}")
        print(f"{'='*50}")
        for check, (ok, detail) in results.items():
            icon = "[PASS]" if ok else "[FAIL]"
            detail_str = f" — {detail}" if detail else ""
            print(f"  {icon} {check}{detail_str}")
        print(f"  STATUS: {status}")

        if fails:
            all_pass = False

    print(f"\n{'='*50}")
    print(f"OVERALL: {'PASS — ready for review' if all_pass else 'FAIL — fix gaps before submitting'}")

    sys.exit(0 if all_pass else 1)


if __name__ == "__main__":
    main()
