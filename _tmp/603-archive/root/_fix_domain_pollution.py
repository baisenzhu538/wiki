"""Batch fix domain pollution in wiki cards.

Two pollution categories:
  1. YAML corruption: domain field concatenated with next field
     e.g. "domain: demand-analysissource_person: truman" → domain: demand-analysis
  2. Status leak: "needs-review" in domain field → remove from domain

Usage:
  python _fix_domain_pollution.py --dry-run   # preview changes only
  python _fix_domain_pollution.py --apply      # apply fixes
"""

import re
import sys
from pathlib import Path
from collections import Counter

ROOT = Path(r"C:\Users\Administrator\Desktop\wiki\30_wiki")

# Pattern 1: domain: <real> + concatenated next field
# Captures the real domain name before the corruption starts
DOMAIN_CORRUPTION_RE = re.compile(
    r"^(domain:\s*\[?)([^\]\n{]*?)(source_person|estimated_tokens|language|author|confidence|source_refs)"
)

# Pattern 2: domain: needs-review (status leaked into domain)
STATUS_LEAK_RE = re.compile(r"^domain:\s*needs-review\s*$", re.MULTILINE)

# Known valid domains to clean the extracted value
KNOWN_DOMAINS = {
    "demand-analysis", "product", "business-model", "growth", "barrier",
    "master", "modeling", "personal-growth", "yitang", "ai-saas",
    "learning-methodology", "healthcare", "entrepreneurship", "decision",
    "design", "strategy", "decision-science", "decision-making",
    "business-strategy", "management", "kdo", "ai-collaboration",
    "content-production", "marketing", "research", "finance-legal",
    "supply-chain", "saas", "b2b", "feishu", "publishing",
    "content-extraction", "e-commerce", "education", "govtech",
    "execution", "architecture", "innovation", "operations", "platform",
    "retail", "product-design", "knowledge-graph", "human-ai-collaboration",
    "kdo-infrastructure", "lean-startup",
}


def fix_card(filepath: Path, dry_run: bool = True) -> tuple[str, str, bool]:
    """Fix a single card. Returns (domain_before, domain_after, changed)."""
    raw = filepath.read_text(encoding="utf-8", errors="replace")
    original = raw
    raw = raw.replace("\r\n", "\n")

    if not raw.startswith("---\n"):
        return ("", "", False)
    end = raw.find("\n---\n", 4)
    if end == -1:
        return ("", "", False)

    fm_text = raw[4:end]
    body = raw[end + 5:]

    # Extract domain line(s) from raw text
    domain_lines = []
    other_lines = []
    in_domain = False
    for line in fm_text.split("\n"):
        stripped = line.strip()
        if stripped.startswith("domain:"):
            domain_lines.append(line)
            in_domain = True
        elif in_domain and (stripped.startswith("- ") or stripped.startswith("  ")):
            domain_lines.append(line)
        else:
            in_domain = False
            other_lines.append(line)

    if not domain_lines:
        return ("", "", False)

    # Check if any domain line is polluted
    polluted = False
    for dl in domain_lines:
        for pattern in [
            "source_person", "estimated_tokens", "language:",
            "author:", "confidence:", "source_refs:"
        ]:
            if pattern in dl:
                polluted = True
                break

    # Also check for needs-review leaked into domain
    has_status_leak = any(
        "needs-review" in dl and "domain:" in dl
        for dl in domain_lines
    )

    if not polluted and not has_status_leak:
        return ("", "", False)

    # Extract real domain value
    domain_before = " | ".join(dl.strip() for dl in domain_lines)
    new_domain_values = []

    for dl in domain_lines:
        content = dl.strip()
        if content.startswith("domain:"):
            content = content[7:].strip()

        # Remove YAML list brackets
        if content.startswith("[") and content.endswith("]"):
            content = content[1:-1]

        # Split on comma if list-like
        parts = [content] if "," not in content else content.split(",")
        for part in parts:
            part = part.strip().strip("'\"")

            if not part or part == "needs-review":
                continue

            # Clean corruption: extract domain before the first concatenated field
            m = DOMAIN_CORRUPTION_RE.match(f"domain: {part}")
            if m:
                raw_domain = m.group(2).strip().rstrip("-").strip()
                if raw_domain and not raw_domain.startswith("{"):
                    new_domain_values.append(raw_domain)
                continue

            # Skip dict repr
            if part.startswith("{"):
                continue

            # Valid domain
            if part.lower() in KNOWN_DOMAINS:
                new_domain_values.append(part.lower())
            elif part and not part.startswith("-"):
                new_domain_values.append(part.lower())

    if not new_domain_values:
        return (domain_before, "(empty)", False)

    unique = list(dict.fromkeys(new_domain_values))
    if len(unique) == 1:
        new_domain_line = f"domain: {unique[0]}"
    else:
        new_domain_line = "domain:\n" + "\n".join(f"  - {d}" for d in unique)

    domain_after = new_domain_line.strip()

    # Rebuild frontmatter
    new_fm_lines = []
    for line in other_lines:
        new_fm_lines.append(line)
    # Insert domain at the top (after any initial fields)
    insert_pos = 0
    for i, line in enumerate(new_fm_lines):
        if line.strip().startswith(("id:", "title:", "aliases:")):
            insert_pos = i + 1
        else:
            break
    new_fm_lines.insert(insert_pos, new_domain_line)

    new_fm = "\n".join(new_fm_lines)
    new_content = "---\n" + new_fm + "\n---" + body

    if dry_run:
        return (domain_before, domain_after, True)

    filepath.write_text(new_content, encoding="utf-8")
    return (domain_before, domain_after, True)


def main():
    dry_run = "--dry-run" in sys.argv or "--apply" not in sys.argv
    apply_mode = "--apply" in sys.argv

    fixes: list[tuple[str, str, str]] = []
    stats = Counter()

    for md in ROOT.rglob("*.md"):
        if ".trash" in md.parts or "decisions" in md.parts:
            continue
        before, after, changed = fix_card(md, dry_run=dry_run)
        if changed:
            rel = md.relative_to(ROOT.parent)
            fixes.append((str(rel), before, after))
            if "(empty)" in after:
                stats["removed"] += 1
            else:
                stats["fixed"] += 1

    mode = "DRY RUN" if dry_run else "APPLIED"
    print(f"\n{'='*70}")
    print(f"  Domain Pollution Fix — {mode}")
    print(f"{'='*70}")
    print(f"  Cards scanned:  {sum(1 for _ in ROOT.rglob('*.md'))}")
    print(f"  Cards fixed:    {len(fixes)}")
    print(f"    Domain fixed: {stats['fixed']}")
    print(f"    Domain removed: {stats['removed']}")
    print()

    if fixes:
        print(f"  Changes ({'preview only' if dry_run else 'applied'}):")
        print(f"  {'File':<55} {'Before':<40} -> After")
        print(f"  {'-'*55} {'-'*40} ---")
        for path, before, after in fixes[:30]:
            b_short = before[:38] + ".." if len(before) > 40 else before
            a_short = after[:50] + ".." if len(after) > 50 else after
            print(f"  {path:<55} {b_short:<40} -> {a_short}")
        if len(fixes) > 30:
            print(f"  ... and {len(fixes) - 30} more")
    else:
        print("  No polluted domains found.")

    print(f"\n{'='*70}")
    if dry_run:
        print("  To apply: python _fix_domain_pollution.py --apply")
    print()


if __name__ == "__main__":
    main()
