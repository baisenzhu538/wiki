#!/usr/bin/env python3
"""
review-mark -- Ouyang Feng review mark CLI.
Usage:
  python review_mark.py card.md --reviewer OuyangFeng
  python review_mark.py card.md --reviewer OuyangFeng --confidence 0.92 --dry-run
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
    if not cp.exists():
        print(f"ERROR: not found: {cp}", file=sys.stderr)
        sys.exit(1)

    content = cp.read_text(encoding="utf-8")
    m = FM_RE.match(content)
    if not m:
        print("ERROR: no frontmatter", file=sys.stderr)
        sys.exit(1)

    fm_text = m.group(1)
    body = content[m.end():]

    now = datetime.now(CST).strftime("%Y-%m-%d")
    updates = {"status": "reviewed", "reviewed_by": args.reviewer, "review_date": now}
    if args.confidence is not None:
        updates["confidence"] = args.confidence

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
    rel = cp.relative_to(VAULT_ROOT).as_posix()

    if args.dry_run:
        print(f"[DRY RUN] {rel}:")
        for k, v in updates.items():
            print(f"  {k}: {v}")
    else:
        cp.write_text(new_content, encoding="utf-8")
        print(f"OK {rel}")
        for k, v in updates.items():
            print(f"  {k}: {v}")

if __name__ == "__main__":
    main()
