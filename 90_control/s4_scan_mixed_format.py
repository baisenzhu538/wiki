"""S4-3: Detect cards with mixed old/new format headings."""
import json
import re
from pathlib import Path

VAULT = Path(r"C:\Users\Administrator\Desktop\wiki")
WIKI_DIR = VAULT / "30_wiki"

# Pairs: (new_format_heading, old_format_heading)
CHECK_PAIRS = [
    ("## Critique", "## Constraints & Boundaries"),
    ("### 不要用的场景", "## dont-use"),
    ("### 不要用的场景", "### dont-use"),
]


def main():
    md_files = list(WIKI_DIR.rglob("*.md"))
    results = []
    stats = {'total': 0, 'mixed': 0, 'old_only': 0}

    for f in sorted(md_files):
        try:
            content = f.read_text(encoding="utf-8")
        except Exception:
            continue

        stats['total'] += 1
        conflicts = []

        for new_h, old_h in CHECK_PAIRS:
            has_new = new_h in content
            has_old = old_h in content
            if has_new and has_old:
                conflicts.append({'new': new_h, 'old': old_h, 'action': 'remove_old'})
            elif has_old and not has_new:
                conflicts.append({'new': new_h, 'old': old_h, 'action': 'rename_to_new'})

        if conflicts:
            stats['mixed' if any(c['action'] == 'remove_old' for c in conflicts) else 'old_only'] += 1
            results.append({
                'file': str(f.relative_to(VAULT)),
                'conflicts': conflicts,
                'has_both': any(c['action'] == 'remove_old' for c in conflicts),
            })

    out_path = VAULT / "90_control" / "s4-mixed-format.json"
    summary = {
        'stats': {**stats, 'mixed': sum(1 for r in results if r['has_both']), 'old_only': sum(1 for r in results if not r['has_both'])},
        'cards': results,
    }
    out_path.write_text(json.dumps(summary, ensure_ascii=False, indent=2), encoding="utf-8")

    print(f"Total cards scanned: {stats['total']}")
    print(f"Mixed format (both old + new): {summary['stats']['mixed']}")
    print(f"Old format only (need rename): {summary['stats']['old_only']}")
    print(f"Total with issues: {len(results)}")
    print(f"Output: {out_path}")

    print(f"\nSample (first 20):")
    for r in results[:20]:
        print(f"  {r['file']}")
        for c in r['conflicts']:
            print(f"    [{c['action']}] old='{c['old']}' new='{c['new']}'")


if __name__ == "__main__":
    main()
