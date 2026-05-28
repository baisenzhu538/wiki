"""S4-2: Scan vault for missing frontmatter fields (id/type/status)."""
import json
import re
from pathlib import Path

VAULT = Path(r"C:\Users\Administrator\Desktop\wiki")
WIKI_DIR = VAULT / "30_wiki"

FM_RE = re.compile(r'^---\s*\n(.*?)\n---', re.DOTALL)


def parse_frontmatter(text: str) -> dict[str, str] | None:
    m = FM_RE.match(text)
    if not m:
        return None
    fm = {}
    for line in m.group(1).split('\n'):
        line = line.strip()
        if ':' in line:
            key, _, val = line.partition(':')
            fm[key.strip()] = val.strip().strip('"\'')
    return fm


def infer_type(filename: str) -> str:
    stem = filename.lower()
    if stem.startswith('ocr-') or stem.startswith('ocr_'):
        return 'concept'
    return 'concept'


def infer_status(fm: dict | None, content: str) -> str:
    if fm and fm.get('status', '').strip():
        return fm['status']
    has_critique = '## Critique' in content or '## 质疑' in content
    has_synthesis = '## Synthesis' in content or '## 对标' in content or '## Synthesize' in content
    if has_critique and has_synthesis:
        return 'enriched'
    return 'draft'


def generate_id(filepath: Path) -> str:
    return filepath.stem


def main():
    md_files = list(WIKI_DIR.rglob("*.md"))
    results = []
    missing_stats = {'id': 0, 'type': 0, 'status': 0, 'any': 0, 'no_frontmatter': 0}
    total = 0

    for f in sorted(md_files):
        total += 1
        try:
            content = f.read_text(encoding="utf-8")
        except Exception:
            continue

        fm = parse_frontmatter(content)
        issues = []

        if fm is None:
            missing_stats['no_frontmatter'] += 1
            issues.append('no_frontmatter')
        else:
            if not fm.get('id', '').strip():
                issues.append('id')
                missing_stats['id'] += 1
            if not fm.get('type', '').strip():
                issues.append('type')
                missing_stats['type'] += 1
            if not fm.get('status', '').strip():
                issues.append('status')
                missing_stats['status'] += 1

        if issues:
            missing_stats['any'] += 1
            # Generate suggested fixes
            fix = {}
            rel = str(f.relative_to(VAULT))
            if 'no_frontmatter' in issues or 'id' in issues:
                fix['id'] = generate_id(f)
            if 'no_frontmatter' in issues or 'type' in issues:
                fix['type'] = infer_type(f.name)
            if 'no_frontmatter' in issues or 'status' in issues:
                fix['status'] = infer_status(fm, content)

            results.append({
                'file': rel,
                'issues': issues,
                'suggested_fix': fix,
            })

    # Write output
    summary = {
        'total_cards': total,
        'missing_stats': missing_stats,
        'cards_with_issues': results,
    }
    out_path = VAULT / "90_control" / "s4-frontmatter-missing.json"
    out_path.write_text(json.dumps(summary, ensure_ascii=False, indent=2), encoding="utf-8")

    print(f"Total cards: {total}")
    print(f"No frontmatter: {missing_stats['no_frontmatter']}")
    print(f"Missing id: {missing_stats['id']}")
    print(f"Missing type: {missing_stats['type']}")
    print(f"Missing status: {missing_stats['status']}")
    print(f"Cards with any issue: {missing_stats['any']}")
    print(f"Output: {out_path}")

    # Show top offenders
    print(f"\nSample cards (first 15):")
    for r in results[:15]:
        print(f"  {r['file']}")
        print(f"    issues: {r['issues']}")
        print(f"    fix: {r['suggested_fix']}")


if __name__ == "__main__":
    main()
