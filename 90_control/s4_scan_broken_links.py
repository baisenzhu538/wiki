"""S4-1: Scan vault for broken wikilinks."""
import json
import os
import re
import sys
from pathlib import Path

VAULT = Path(r"C:\Users\Administrator\Desktop\wiki")
WIKI_DIR = VAULT / "30_wiki"
OUTPUT_DIR = VAULT / "90_control"

WIKILINK_RE = re.compile(r'\[\[([^\]|#]+)(?:[#|][^\]]+)?\]\]')

def find_md_files(root: Path) -> list[Path]:
    files = []
    for path in root.rglob("*.md"):
        if path.is_file():
            files.append(path)
    return files

def resolve_target(link_target: str, source_file: Path) -> Path | None:
    """Try to resolve a wikilink target to a real file."""
    target = link_target.strip()

    # Try exact match
    exact = WIKI_DIR / "concepts" / f"{target}.md"
    if exact.exists():
        return exact

    # Try tools
    exact = WIKI_DIR / "tools" / f"{target}.md"
    if exact.exists():
        return exact

    # Try systems
    exact = WIKI_DIR / "systems" / f"{target}.md"
    if exact.exists():
        return exact

    # Try in all wiki subdirs
    for subdir in WIKI_DIR.rglob("*"):
        if subdir.is_dir():
            candidate = subdir / f"{target}.md"
            if candidate.exists():
                return candidate

    # Try relative to source file
    candidate = source_file.parent / f"{target}.md"
    if candidate.exists():
        return candidate

    return None

def main():
    md_files = find_md_files(WIKI_DIR)
    broken_links = []
    total_links = 0

    for f in sorted(md_files):
        try:
            content = f.read_text(encoding="utf-8")
        except Exception:
            continue

        for match in WIKILINK_RE.finditer(content):
            total_links += 1
            target = match.group(1).strip()
            resolved = resolve_target(target, f)
            if resolved is None:
                broken_links.append({
                    "source": str(f.relative_to(VAULT)),
                    "line": content[:match.start()].count('\n') + 1,
                    "target": target,
                })

    # Write output
    output = {
        "total_links_scanned": total_links,
        "broken_count": len(broken_links),
        "broken_links": broken_links,
    }

    out_path = OUTPUT_DIR / "s4-broken-links.json"
    out_path.write_text(json.dumps(output, ensure_ascii=False, indent=2), encoding="utf-8")

    print(f"Scanned {len(md_files)} files, {total_links} total links")
    print(f"Broken: {len(broken_links)}")
    print(f"Output: {out_path}")

    # Print first 20 for quick review
    for bl in broken_links[:20]:
        print(f"  {bl['source']}:{bl['line']} -> [[{bl['target']}]]")

if __name__ == "__main__":
    main()
