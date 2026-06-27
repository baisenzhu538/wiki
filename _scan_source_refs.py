"""Scan source_refs across the vault and check disk existence.

Output: 4-column table for欧阳锋 review.
"""
import difflib
import sys
from pathlib import Path
from collections import Counter

ROOT = Path(r"C:\Users\Administrator\Desktop\wiki")
WIKI = ROOT / "30_wiki"


def scan():
    # Build fast index — only source directories where source_refs point
    src_files: set[str] = set()
    src_dir_index: dict[str, str] = {}  # filename -> full path
    for d in ["00_inbox", "10_raw"]:
        for f in (ROOT / d).rglob("*"):
            if f.is_file() and ".trash" not in f.parts:
                rel = str(f.relative_to(ROOT)).replace("\\", "/")
                src_files.add(rel)
                src_dir_index[f.name] = rel
    # Also index vault itself for source_refs that point within wiki
    vault_files: set[str] = set()
    for f in ROOT.rglob("*"):
        if ".trash" in f.parts or ".obsidian" in f.parts or ".git" in f.parts:
            continue
        if f.is_file():
            vault_files.add(str(f.relative_to(ROOT)).replace("\\", "/"))

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
            ref_norm = ref.replace("\\", "/")

            # Check exact match
            if ref_norm in vault_files or (ROOT / ref_norm).exists():
                continue

            # Check filename match in source dirs
            fn = Path(ref_norm).name
            if fn in src_dir_index:
                actual = src_dir_index[fn]
                results.append({
                    "card": rel_md, "source_ref": ref,
                    "category": "typo", "suggestion": actual,
                })
                continue

            # Check without .md extension
            if ref_norm.endswith(".md"):
                fn2 = fn[:-3]
                if fn2 in src_dir_index:
                    actual = src_dir_index[fn2]
                    results.append({
                        "card": rel_md, "source_ref": ref,
                        "category": "typo", "suggestion": actual,
                    })
                    continue

            # No match found
            results.append({
                "card": rel_md, "source_ref": ref,
                "category": "missing", "suggestion": "",
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
