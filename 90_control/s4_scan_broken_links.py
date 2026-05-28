"""S4-1: Scan vault for broken wikilinks. V2 with proper path handling."""
import json
import re
from pathlib import Path

VAULT = Path(r"C:\Users\Administrator\Desktop\wiki")
WIKI_DIR = VAULT / "30_wiki"

WIKILINK_RE = re.compile(r'\[\[([^\]|#]+?)(?:[#|][^\]]+)?\]\]')

def find_all_md() -> dict[str, Path]:
    """Return {stem: path, relative_path: path} for all .md files in vault."""
    index = {}
    for f in VAULT.rglob("*.md"):
        if f.is_file():
            rel = str(f.relative_to(VAULT)).replace('\\', '/')
            stem = f.stem
            index[rel.lower()] = f
            index[stem.lower()] = f
            # Also index by path without leading dirs
            parts = rel.split('/')
            if len(parts) > 1:
                shorter = '/'.join(parts[1:])
                index[shorter.lower()] = f
    return index

def is_garbled(s: str) -> bool:
    """Check if string contains encoding-garbled CJK characters."""
    for ch in s:
        cp = ord(ch)
        if cp > 0x4e00 and cp < 0x9fff:
            continue  # valid CJK
        if cp > 0x3000 and cp < 0x303f:
            continue  # CJK punctuation
        if cp > 0xff00 and cp < 0xffef:
            continue  # fullwidth forms
        if cp > 0x2000 and cp < 0x206f:
            continue  # general punctuation
        if cp > 0x80 and cp < 0x2000:
            return True  # garbled latin-1 range for CJK
    return False

def resolve(target_raw: str, file_index: dict[str, Path]) -> tuple[str | None, str]:
    """Try to resolve a wikilink target.
    Returns (resolved_path, category).
    Category: 'found' | 'path-fixable' | 'not-exist' | 'encoding-garbled' | 'external'
    """
    target = target_raw.strip()

    if is_garbled(target):
        return None, 'encoding-garbled'

    # Normalize: replace backslash with forward slash
    normalized = target.replace('\\', '/').lower()

    # Try direct lookup
    if normalized in file_index:
        return str(file_index[normalized].relative_to(VAULT)), 'found'

    # Try with .md extension stripped (in case link has .md)
    if normalized.endswith('.md'):
        without_ext = normalized[:-3]
        if without_ext in file_index:
            return str(file_index[without_ext].relative_to(VAULT)), 'found'

    # Try as stem only (last component without extension)
    stem = Path(target).stem.lower()
    if stem in file_index:
        return str(file_index[stem].relative_to(VAULT)), 'found'

    # Path-fixable: target might exist with slightly different path
    # e.g. "30_wiki/concepts/xxx" vs "xxx"
    for key, val in file_index.items():
        if key.endswith('/' + stem + '.md') or key.endswith('\\' + stem + '.md'):
            return str(val.relative_to(VAULT)), 'path-fixable'

    return None, 'not-exist'


def main():
    file_index = find_all_md()
    print(f"Indexed {len(file_index)} filename variants")

    md_files = list(WIKI_DIR.rglob("*.md"))
    broken: list[dict] = []
    fixable: list[dict] = []
    garbled: list[dict] = []
    stats = {'total': 0, 'found': 0, 'fixable': 0, 'not-exist': 0, 'garbled': 0}

    for f in sorted(md_files):
        try:
            content = f.read_text(encoding="utf-8")
        except Exception:
            continue

        for match in WIKILINK_RE.finditer(content):
            stats['total'] += 1
            target = match.group(1).strip()
            if not target or target.startswith('http'):
                stats['found'] += 1
                continue

            resolved, category = resolve(target, file_index)
            entry = {
                "source": str(f.relative_to(VAULT)),
                "line": content[:match.start()].count('\n') + 1,
                "target": target,
                "resolved": resolved,
            }

            if category == 'found':
                stats['found'] += 1
            elif category == 'path-fixable':
                stats['fixable'] += 1
                fixable.append(entry)
            elif category == 'not-exist':
                stats['not-exist'] += 1
                broken.append(entry)
            elif category == 'encoding-garbled':
                stats['garbled'] += 1
                garbled.append(entry)

    print(f"\nResults:")
    print(f"  Total links scanned:   {stats['total']}")
    print(f"  Found (valid):         {stats['found']}")
    print(f"  Path-fixable (auto):   {stats['fixable']}")
    print(f"  Broken (not exist):    {stats['not-exist']}")
    print(f"  Encoding garbled:      {stats['garbled']}")

    # Write outputs
    out_dir = VAULT / "90_control"

    summary = {
        "stats": stats,
        "fixable_links": fixable,
        "broken_links": broken,
        "garbled_links": garbled,
    }
    (out_dir / "s4-broken-links.json").write_text(
        json.dumps(summary, ensure_ascii=False, indent=2), encoding="utf-8")

    # Write fixable list for auto-repair
    with open(out_dir / "s4-fixable-links.txt", "w", encoding="utf-8") as fh:
        for fl in fixable:
            fh.write(f"{fl['source']}:{fl['line']}:{fl['target']} -> {fl['resolved']}\n")

    # Show top broken not-exist targets
    from collections import Counter
    top_broken = Counter(b['target'] for b in broken).most_common(30)
    print(f"\nTop 30 broken targets (not exist):")
    for t, c in top_broken:
        print(f"  {c:4d}x [[{t[:90]}]]")

    print(f"\nOutput: {out_dir / 's4-broken-links.json'}")
    print(f"Fixable list: {out_dir / 's4-fixable-links.txt'}")

if __name__ == "__main__":
    main()
