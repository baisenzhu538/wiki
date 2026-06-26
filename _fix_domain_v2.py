"""Fix domain pollution — v2: safe, incremental, git-backed.

Strategy: find every card whose parsed domain contains a dict repr
(e.g. "{'mastersource_person': 'truman'}") or status-leaked value
(e.g. "needs-review"). Extract the real domain from the raw frontmatter
text, rebuild the frontmatter, and write back.

Safety: git repo allows revert if anything goes wrong.
"""

import re
import sys
from pathlib import Path
from collections import Counter

ROOT = Path(r"C:\Users\Administrator\Desktop\wiki\30_wiki")
DRY_RUN = "--apply" not in sys.argv


def extract_real_domain(raw_fm_text: str) -> list[str]:
    """Extract real domain values from raw frontmatter text.

    Uses the same fallback approach as KDO workspace.parse_frontmatter.
    """
    domains: list[str] = []
    in_domain = False
    domain_indent = ""

    for line in raw_fm_text.split("\n"):
        stripped = line.strip()

        if stripped.startswith("domain:"):
            in_domain = True
            val = stripped[7:].strip()
            if val and not val.startswith("-"):
                # single-line domain: value
                domains.append(val.strip("'\"").strip("[]").strip())
                in_domain = False
            elif val.startswith("- "):
                domains.append(val[2:].strip("'\"").strip())
            # else: multi-line, continue
            continue

        if in_domain:
            if stripped.startswith("- "):
                domains.append(stripped[2:].strip("'\"").strip())
            elif not stripped or stripped.startswith(("id:", "title:", "type:",
                "status:", "source_refs:", "source_context:", "created_at:",
                "updated_at:", "author:", "reviewed_by:", "review_date:",
                "confidence:", "trust_level:", "related:", "tags:", "aliases:",
                "component_of:", "---")):
                in_domain = False
            # else: continuation of multi-line domain value (unusual but possible)

    return domains


def clean_domain_value(val: str) -> str:
    """Clean a single domain value. Remove corruption artifacts."""
    val = val.strip().strip("'\"").strip()

    # Skip obviously corrupted values
    if not val or val == "needs-review":
        return ""
    if val.startswith("{") and "}" in val:
        return ""  # dict repr — can't extract
    if val.startswith("[") and "]" in val:
        return ""  # list repr — can't extract

    # Remove corruption suffixes
    corruption_markers = [
        "source_person:", "estimated_tokens:", "language:",
        "author:", "confidence:", "source_refs:",
        "  source_person", "  estimated_tokens",
    ]
    for marker in corruption_markers:
        idx = val.find(marker)
        if idx > 0:
            val = val[:idx].rstrip("-").rstrip()

    return val.strip()


def rebuild_frontmatter(raw_text: str, new_domain_line: str) -> str:
    """Replace the domain section in raw frontmatter text."""
    lines = raw_text.split("\n")
    new_lines = []
    in_domain = False
    replaced = False

    for line in lines:
        stripped = line.strip()

        if stripped.startswith("domain:") and not replaced:
            new_lines.append(new_domain_line)
            in_domain = True
            replaced = True
            # Check if single-line
            val = stripped[7:].strip()
            if val and not val.startswith("-"):
                in_domain = False
            continue

        if in_domain:
            if stripped.startswith("- "):
                continue  # skip old domain list items
            elif not stripped or stripped.startswith(("id:", "title:", "type:",
                "status:", "source_refs:", "source_context:", "created_at:",
                "updated_at:", "author:", "reviewed_by:", "review_date:",
                "confidence:", "trust_level:", "related:", "tags:", "aliases:",
                "component_of:", "---")):
                in_domain = False
                new_lines.append(line)
            # else: skip continuation lines of corrupted domain
            continue

        new_lines.append(line)

    return "\n".join(new_lines)


def main():
    stats = Counter()
    fixes: list[tuple[str, str, str]] = []

    for md in ROOT.rglob("*.md"):
        if ".trash" in md.parts or "decisions" in md.parts:
            continue

        raw = md.read_text(encoding="utf-8", errors="replace")
        raw_unix = raw.replace("\r\n", "\n")

        if not raw_unix.startswith("---\n"):
            continue
        end = raw_unix.find("\n---\n", 4)
        if end == -1:
            continue

        fm_text = raw_unix[4:end]
        body = raw_unix[end + 5:]

        # Extract real domains from raw text
        raw_domains = extract_real_domain(fm_text)
        cleaned = [d for d in (clean_domain_value(d) for d in raw_domains) if d]

        # Skip if no issues
        if cleaned == raw_domains:
            continue

        if not cleaned:
            stats["emptied"] += 1
            continue

        # Deduplicate
        unique = list(dict.fromkeys(cleaned))

        rel = md.relative_to(ROOT.parent)

        if len(unique) == 1:
            new_domain_line = f"domain: {unique[0]}"
        else:
            new_domain_line = "domain:\n" + "\n".join(f"  - {d}" for d in unique)

        old_repr = " | ".join(raw_domains[:2])
        if len(raw_domains) > 2:
            old_repr += f" ...({len(raw_domains)})"
        new_repr = " | ".join(unique)

        if not DRY_RUN:
            new_fm = rebuild_frontmatter(fm_text, new_domain_line)
            new_content = "---\n" + new_fm + "\n---" + body
            md.write_text(new_content, encoding="utf-8")

        fixes.append((str(rel), old_repr, new_repr))
        stats["fixed"] += 1

    mode = "DRY RUN" if DRY_RUN else "APPLIED"
    print(f"\n{'='*70}")
    print(f"  Domain Fix v2 — {mode}")
    print(f"{'='*70}")
    print(f"  Cards fixed:  {len(fixes)}")
    print(f"  Emptied:      {stats['emptied']}")
    print()

    if fixes:
        print(f"  {'File':<55} Before -> After")
        print(f"  {'-'*55} ---")
        for path, before, after in fixes[:25]:
            b = before[:55] + ".." if len(before) > 57 else before
            print(f"  {path:<55} {b} -> {after}")
        if len(fixes) > 25:
            print(f"  ... and {len(fixes) - 25} more")
    else:
        print("  No changes needed.")

    print(f"\n{'='*70}")
    if DRY_RUN:
        print("  To apply: python _fix_domain_v2.py --apply")
    print()


if __name__ == "__main__":
    main()
