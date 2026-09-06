#!/usr/bin/env python3
"""
review-mark -- Ouyang Feng review mark CLI.
Usage:
  python review_mark.py card.md --reviewer OuyangFeng
  python review_mark.py card.md --reviewer OuyangFeng --confidence 0.92 --dry-run

#670：翻转核心抽为 mark_card()——queue_transition 终审 PASS 钩子与手工批收口
共用同一实现（翻转逻辑单写一面，避免两处副本漂移）。
"""
import argparse, re, sys
from pathlib import Path
from datetime import datetime, timezone, timedelta

VAULT_ROOT = Path(__file__).resolve().parent.parent.parent
FM_RE = re.compile(r"^---\s*\n(.*?)\n---\s*\n", re.DOTALL)
CST = timezone(timedelta(hours=8))

def parse_yaml_fm(text):
    try:
        import yaml
        return yaml.safe_load(text) or {}
    except ImportError:
        result = {}
        for line in text.splitlines():
            s = line.strip()
            if not s or s.startswith("#"): continue
            if ":" in s:
                k, v = s.split(":", 1)
                result[k.strip()] = v.strip().strip('"').strip("'")
        return result

def _fm_value(fm_text: str, key: str) -> str:
    """取 frontmatter 单行标量值（找不到返回空串）——status 门控用，不依赖 yaml。"""
    for line in fm_text.splitlines():
        s = line.strip()
        if s.startswith(key + ":"):
            return s.split(":", 1)[1].strip().strip('"').strip("'")
    return ""

def mark_card(cp: Path, reviewer: str = "OuyangFeng", confidence: float | None = None,
              dry_run: bool = False,
              only_flip_from: tuple[str, ...] | None = None) -> tuple[bool, str]:
    """把一张卡 frontmatter 翻成 reviewed（status/reviewed_by/review_date，可选 confidence）。

    返回 (ok, message)。only_flip_from 给定时（#670 钩子传 ("draft",)），当前 status
    不在集合内 → 不写盘，返回 (False, "skip: status=...")——防钩子误翻 stable/needs-review。
    """
    if not cp.exists():
        return False, f"not found: {cp}"

    content = cp.read_text(encoding="utf-8")
    m = FM_RE.match(content)
    if not m:
        return False, "no frontmatter"

    fm_text = m.group(1)
    body = content[m.end():]

    if only_flip_from is not None:
        cur = _fm_value(fm_text, "status")
        if cur not in only_flip_from:
            return False, f"skip: status={cur or '缺失'} 不在 {'/'.join(only_flip_from)}"

    now = datetime.now(CST).strftime("%Y-%m-%d")
    updates = {"status": "reviewed", "reviewed_by": reviewer, "review_date": now}
    if confidence is not None:
        updates["confidence"] = confidence

    new_lines = []
    updated = set()
    for line in fm_text.splitlines():
        s = line.strip()
        matched = False
        for key, val in updates.items():
            if s.startswith(key + ":") or s.startswith(key + " "):
                new_lines.append(f"{key}: {val}")
                updated.add(key)
                matched = True
                break
        if not matched:
            new_lines.append(line)
    for key in updates:
        if key not in updated:
            new_lines.append(f"{key}: {updates[key]}")

    new_fm = "---\n" + "\n".join(new_lines) + "\n---\n"
    new_content = new_fm + body
    rel = cp.relative_to(VAULT_ROOT).as_posix() if cp.is_relative_to(VAULT_ROOT) else str(cp)

    lines = [f"[DRY RUN] {rel}:" if dry_run else f"OK {rel}"]
    lines += [f"  {k}: {v}" for k, v in updates.items()]
    if not dry_run:
        cp.write_text(new_content, encoding="utf-8")
    return True, "\n".join(lines)

def main():
    parser = argparse.ArgumentParser(description="Mark card as reviewed")
    parser.add_argument("card", help="Card path relative to vault root")
    parser.add_argument("--reviewer", default="OuyangFeng")
    parser.add_argument("--confidence", type=float, default=None)
    parser.add_argument("--dry-run", action="store_true")
    args = parser.parse_args()

    cp = Path(args.card)
    if not cp.is_absolute():
        cp = VAULT_ROOT / cp
    ok, msg = mark_card(cp, reviewer=args.reviewer, confidence=args.confidence,
                        dry_run=args.dry_run)
    if not ok:
        print(f"ERROR: {msg}", file=sys.stderr)
        sys.exit(1)
    print(msg)

if __name__ == "__main__":
    main()
