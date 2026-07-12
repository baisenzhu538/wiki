"""#159 阶段 2 放量 apply — 同类型 F2 缺回链分批修复"""
import subprocess, sys, re, json
from pathlib import Path
from collections import defaultdict

VAULT = Path(__file__).resolve().parent.parent.parent
DRY = "--apply" not in sys.argv

# 1. Get all F2 MISSING BACKLINK from full lint
r = subprocess.run([sys.executable, str(VAULT/"90_control/scripts/kdo_lint.py"), str(VAULT/"30_wiki")],
    capture_output=True, text=True, timeout=120, encoding="utf-8", errors="replace")
lines = (r.stdout + r.stderr).splitlines()

pairs = []
for l in lines:
    m = re.search(r"F2 MISSING BACKLINK:\s*(\S+)\s*→\s*(\S+)", l)
    if m: pairs.append((m.group(1), m.group(2)))

def typ(cid):
    for p in ['concept-','framework-','tool-','case-','dk-','method-','system-']:
        if cid.startswith(p): return p.rstrip('-')
    return 'other'

# Filter same-type
same_type = [(f,t) for f,t in pairs if typ(f)==typ(t) and typ(f)!='other']
by_type = defaultdict(list)
for f,t in same_type: by_type[typ(f)].append((f,t))

# Batch order
batches = [
    ("concept", by_type.get("concept",[])),
    ("framework", by_type.get("framework",[])),
    ("case", by_type.get("case",[])),
    ("method", by_type.get("method",[])),
    ("tool", by_type.get("tool",[])),
]

def find_card_file(card_id):
    for d in ["concepts","frameworks","tools","cases","methods","systems","dark-knowledges","dk","domains","skills"]:
        dpath = VAULT / "30_wiki" / d
        if not dpath.is_dir(): continue
        for f in dpath.rglob("*.md"):
            if f.stem == card_id:
                return f
    return None

def add_backlink(filepath, backlink_id):
    """Add [[backlink_id]] to related list in frontmatter. Returns True if changed."""
    content = filepath.read_text(encoding="utf-8")
    fm_match = re.match(r"^(---\s*\n.*?\n---)", content, re.DOTALL)
    if not fm_match: return False, content
    fm = fm_match.group(1)
    rest = content[len(fm):]
    if backlink_id in fm: return False, content

    lines = fm.splitlines()
    # Find last related line
    last = -1
    for i, l in enumerate(lines):
        if l.strip().startswith("-") and ("[[" in l or "[[" in l):
            last = i
    if last < 0: return False, content

    # Match quote style
    quote = "'" if "'" in lines[last] else '"'
    new_entry = f"  - {quote}[[{backlink_id}]]{quote}"
    lines.insert(last+1, new_entry)
    new_fm = "\n".join(lines)
    new_content = new_fm + rest
    return True, new_content

total_applied = 0
total_files = set()

for batch_name, batch_pairs in batches:
    if not batch_pairs:
        print(f"\n[{batch_name}] 0 pairs — skip")
        continue

    print(f"\n{'='*50}")
    print(f"Batch: {batch_name}↔{batch_name} ({len(batch_pairs)} pairs)")
    print(f"{'='*50}")

    # Group by target (to-card gets the backlink)
    by_target = defaultdict(set)
    for frm, to in batch_pairs:
        by_target[to].add(frm)

    batch_applied = 0
    for to_id, from_ids in sorted(by_target.items()):
        to_file = find_card_file(to_id)
        if not to_file:
            print(f"  SKIP {to_id}: file not found (from: {', '.join(sorted(from_ids)[:3])})")
            continue

        for from_id in sorted(from_ids):
            changed, new_content = add_backlink(to_file, from_id)
            if not changed:
                continue

            if DRY:
                print(f"  DRY {to_id} ← {from_id}")
            else:
                to_file.write_text(new_content, encoding="utf-8")
                total_files.add(str(to_file.relative_to(VAULT)))
            batch_applied += 1

    print(f"  {batch_name}: {'would apply' if DRY else 'applied'} {batch_applied} backlinks to {len(by_target)} files")
    total_applied += batch_applied

print(f"\n{'='*50}")
mode = "DRY-RUN" if DRY else "APPLY"
print(f"{mode} complete: {total_applied} backlinks, {len(total_files)} files")
if not DRY:
    print("Run: python 90_control/scripts/kdo_lint.py --baseline")
