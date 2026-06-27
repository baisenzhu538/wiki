"""Scan source_refs across the vault and check disk existence.

Output: 4-column table for欧阳锋 review.
"""
import difflib
import sys
from pathlib import Path
from collections import Counter

ROOT = Path(r"C:\Users\Administrator\Desktop\wiki")
WIKI = ROOT / "30_wiki"


def find_best_match(target: str, candidates: list[str]) -> str:
    """Return the closest-matching file in candidates, or '' if no good match."""
    best, best_r = "", 0.0
    tn = Path(target).name
    for c in candidates:
        cn = Path(c).name
        r = difflib.SequenceMatcher(None, tn, cn).ratio()
        if r > best_r:
            best_r = r
            best = c
    return best if best_r >= 0.75 else ""


def scan():
    # Build disk file index
    all_files: set[str] = set()
    for f in ROOT.rglob("*"):
        if ".trash" in f.parts or ".obsidian" in f.parts or ".git" in f.parts:
            continue
        if f.is_file():
            rel = str(f.relative_to(ROOT)).replace("\\", "/")
            all_files.add(rel)

    results: list[dict] = []

    for md in WIKI.rglob("*.md"):
        if ".trash" in md.parts or "decisions" in md.parts:
            continue
        text = md.read_text(encoding="utf-8", errors="replace")
        text = text.replace("\r\n", "\n")
        if not text.startswith("---\n"):
            continue
        end = text.find("\n---\n", 4)
        if end == -1:
            continue
        import yaml
        try:
            fm = yaml.safe_load(text[4:end])
        except:
            continue
        if not isinstance(fm, dict):
            continue
        refs = fm.get("source_refs", [])
        if not isinstance(refs, list):
            continue

        rel_md = str(md.relative_to(ROOT)).replace("\\", "/")
        for ref in refs:
            ref = str(ref).strip()
            if not ref or ref.startswith("src_"):
                continue
            if ref in all_files:
                continue
            # Try as-is
            if (ROOT / ref).exists():
                continue
            # Check without .md suffix
            if ref.endswith(".md"):
                alt = ref[:-3]
                if alt in all_files or (ROOT / alt).exists():
                    continue

            suggestion = find_best_match(ref, list(all_files))
            cat = "typo" if suggestion else "missing"
            results.append({
                "card": rel_md,
                "source_ref": ref,
                "category": cat,
                "suggestion": suggestion,
            })

    return results


def main():
    results = scan()
    cats = Counter(r["category"] for r in results)
    print(f"Total broken source_refs: {len(results)}")
    print(f"  typo (has suggestion): {cats['typo']}")
    print(f"  missing (no file found): {cats['missing']}")
    print()

    # Print full table
    print(f"{'Card':<55} {'Source Ref':<65} {'Category':<8} Suggestion")
    print("-" * 160)
    for r in results[:100]:
        print(f"{r['card']:<55} {r['source_ref']:<65} {r['category']:<8} {r['suggestion']}")
    if len(results) > 100:
        print(f"\n... and {len(results) - 100} more (full output: _scan_source_refs_output.txt)")

    # Write full output
    out = ROOT / "_scan_source_refs_output.txt"
    with open(out, "w", encoding="utf-8") as f:
        f.write(f"Total broken source_refs: {len(results)}\n")
        f.write(f"typo: {cats['typo']}, missing: {cats['missing']}\n\n")
        f.write(f"{'Card':<55} {'Source Ref':<65} {'Category':<8} Suggestion\n")
        f.write("-" * 160 + "\n")
        for r in results:
            f.write(f"{r['card']:<55} {r['source_ref']:<65} {r['category']:<8} {r['suggestion']}\n")
    print(f"\nFull list written to: _scan_source_refs_output.txt")


if __name__ == "__main__":
    main()
