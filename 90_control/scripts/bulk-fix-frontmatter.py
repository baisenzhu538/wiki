"""
Bulk fix frontmatter fields: related, status, author, reviewed_by, confidence.

Usage:
    python bulk-fix-frontmatter.py --dry-run              # Preview issues
    python bulk-fix-frontmatter.py --fix                  # Apply fixes
    python bulk-fix-frontmatter.py --fix --card <id>      # Fix single card
    python bulk-fix-frontmatter.py --stats                # Show stats only

Only writes safe defaults. Never overwrites existing data.
"""
import argparse, re, sys
from pathlib import Path
from collections import Counter

WIKI = Path(r"C:\Users\Administrator\Desktop\wiki\30_wiki")
IGNORE = ["_archive", "index.md", "log.md"]

DEFAULTS = {
    "status": "draft",
    "author": "老顽童",
    "reviewed_by": "待审",
    "confidence": "0.75",
    "type": "concept",
}

def safe_read(f):
    for enc in ['utf-8', 'gbk', 'latin-1']:
        try: return f.read_text(encoding=enc)
        except: continue
    return None

def parse_frontmatter(text):
    if not text.startswith("---"): return {}, text
    end = text.find("---", 3)
    if end == -1: return {}, text
    fm, body = {}, text[3:end]
    for line in body.split("\n"):
        if ":" in line:
            k, _, v = line.partition(":")
            k, v = k.strip(), v.strip().strip('"').strip("'")
            if v.startswith("[") and v.endswith("]"):
                fm[k] = [it.strip().strip('"').strip("'") for it in v[1:-1].split(",") if it.strip()]
            else:
                fm[k] = v
    for lk in ["related", "domain", "source_refs", "tags"]:
        if lk in fm and (fm[lk] == [] or fm[lk] == ""):
            pat = re.compile(rf"^{lk}:\n((?:\s+-.+\n?)*)", re.MULTILINE)
            m = pat.search(body)
            if m:
                items = re.findall(r"^\s*-\s+(.+)$", m.group(1), re.MULTILINE)
                fm[lk] = [it.strip().strip('"').strip("'") for it in items]
    return fm, text[end+3:]

def count_related(fm):
    rel = fm.get("related", [])
    if isinstance(rel, str): rel = [rel] if rel else []
    return len([r for r in rel if r.strip()])

def scan():
    issues = []
    stats = Counter()
    for f in sorted(WIKI.rglob("*.md")):
        if any(p in str(f) for p in IGNORE): continue
        text = safe_read(f)
        if not text: continue
        fm, body = parse_frontmatter(text)
        if "id" not in fm: continue

        card_id = fm["id"]
        rel_path = str(f.relative_to(WIKI))
        problems = []

        # Required fields check
        for field in ["title", "type", "status", "author"]:
            if field not in fm or not fm[field]:
                problems.append(f"missing:{field}")
                stats[f"missing_{field}"] += 1

        # Related check
        rel_count = count_related(fm)
        if rel_count < 5:
            problems.append(f"related={rel_count}")
            stats["low_related"] += 1

        # Source refs check
        src = fm.get("source_refs", [])
        if isinstance(src, str): src = [src] if src else []
        if not src:
            # Check if type warrants source_refs
            if fm.get("type") not in ["index", "system", "improvement-plan"]:
                problems.append("no_source_refs")
                stats["no_source_refs"] += 1

        # Status check
        if fm.get("status") in [None, "", "draft"]:
            stats["status_draft"] += 1

        if problems:
            issues.append({"id": card_id, "path": rel_path, "problems": problems, "fm": fm, "file": f})

        stats["total"] += 1

    return issues, stats

def apply_fix(issue, dry_run=False):
    f = issue["file"]
    fm = issue["fm"]
    problems = issue["problems"]
    text = safe_read(f)
    if not text: return

    fm_raw = text[3:text.find("---", 3)]
    patches = []

    for p in problems:
        if p.startswith("missing:"):
            field = p.split(":")[1]
            if field in DEFAULTS:
                patches.append(f"{field}: {DEFAULTS[field]}")

    if patches and not dry_run:
        new_fm = fm_raw.rstrip() + "\n" + "\n".join(patches) + "\n"
        new_text = "---\n" + new_fm + "---" + text[text.find("---", 3)+3:]
        f.write_text(new_text, encoding="utf-8")
        return f"PATCHED: {', '.join(patches)}"
    elif patches:
        return f"[DRY-RUN] would add: {', '.join(patches)}"
    return None

def main():
    p = argparse.ArgumentParser()
    p.add_argument("--dry-run", action="store_true")
    p.add_argument("--fix", action="store_true")
    p.add_argument("--card")
    p.add_argument("--stats", action="store_true")
    args = p.parse_args()

    issues, stats = scan()

    if args.stats:
        print(f"Total cards: {stats['total']}")
        for k, v in sorted(stats.items()):
            if k != "total": print(f"  {k}: {v}")
        return

    if args.card:
        issues = [i for i in issues if i["id"] == args.card]
        if not issues:
            print(f"Card '{args.card}' not found or no issues.")
            return

    fixed = 0
    for issue in issues:
        problems_str = ", ".join(issue["problems"])
        result = apply_fix(issue, dry_run=args.dry_run)
        if result:
            print(f"  {issue['id']} ({issue['path']})")
            print(f"    Issues: {problems_str}")
            print(f"    {result}")
            fixed += 1

    mode = "[DRY-RUN] " if args.dry_run else ""
    print(f"\n{mode}{fixed} cards with issues out of {stats['total']} total.")

if __name__ == "__main__":
    main()
