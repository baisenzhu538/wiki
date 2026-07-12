#!/usr/bin/env python3
"""
KDO Quality Label Migration — First 50 cards.
Heuristic auto-labeling based on frontmatter signals.
Usage:
  python 90_control/scripts/label-quality-migrate.py --dry-run   # Preview
  python 90_control/scripts/label-quality-migrate.py --apply     # Apply labels
"""
import argparse
import yaml
from pathlib import Path
from collections import Counter

WIKI = Path("30_wiki")


def analyze_card(fm: dict) -> list[str] | None:
    """Apply heuristics to determine quality_labels for a card.
    Returns None if the card already has quality_labels."""
    existing = fm.get("quality_labels")
    if existing:
        return None

    labels = []

    related = fm.get("related", [])
    if isinstance(related, list):
        real_links = [r for r in related if isinstance(r, str) and r.startswith("[[") and "unknown" not in r.lower()]
        # cited: at least 3 real wikilinks
        if len(real_links) >= 3:
            labels.append("cited")

    status = fm.get("status", "")
    confidence = fm.get("confidence", 0)
    # quality: reviewed/stable with high confidence
    if status in ("reviewed", "stable") and confidence >= 0.80:
        labels.append("quality")

    source_refs = fm.get("source_refs", [])
    if isinstance(source_refs, list):
        real_sources = [s for s in source_refs if isinstance(s, str) and "pending" not in s.lower() and "unknown" not in s.lower()]
        # validated: has at least 1 real source
        if real_sources:
            labels.append("validated")

    card_type = fm.get("type", "")
    # actionable: tool/case cards usually have action triggers
    if card_type in ("tool", "case"):
        labels.append("actionable")

    # principle: framework/concept cards are usually principles
    if card_type in ("framework", "concept"):
        labels.append("principle")

    # hypothesis: low-confidence cards with draft status
    if status == "draft" and confidence <= 0.70:
        labels.append("hypothesis")

    # insight: reviewed framework cards with external attackers
    if card_type == "framework" and status == "reviewed":
        labels.append("insight")

    # quotable: not auto-assigned — needs human judgment
    return sorted(set(labels))


def select_candidates(limit: int = 50) -> list[Path]:
    """Select high-quality cards for first batch."""
    candidates = []
    for p in WIKI.rglob("*.md"):
        if "_archive" in str(p) or "10_raw" in str(p):
            continue
        try:
            text = p.read_text(encoding="utf-8", errors="ignore")
        except:
            continue
        if not text.startswith("---"):
            continue
        parts = text.split("---", 2)
        if len(parts) < 3:
            continue
        try:
            fm = yaml.safe_load(parts[1])
        except:
            continue
        if not fm or not isinstance(fm, dict):
            continue

        # Prioritize: reviewed/stable, has real related links, has source_refs
        status = fm.get("status", "")
        related = fm.get("related", [])
        src = fm.get("source_refs", [])

        # Skip cards that already have quality_labels
        if fm.get("quality_labels"):
            continue

        # Score for selection
        score = 0
        if status in ("reviewed", "stable"):
            score += 3
        elif status == "enriched":
            score += 1

        if isinstance(related, list):
            real = [r for r in related if isinstance(r, str) and r.startswith("[[")]
            score += min(len(real), 5)

        if isinstance(src, list):
            real_src = [s for s in src if isinstance(s, str) and "pending" not in s.lower() and "unknown" not in s.lower()]
            score += min(len(real_src), 3)

        candidates.append((p, score, fm))

    # Sort by score descending, pick top N
    candidates.sort(key=lambda x: -x[1])
    return candidates[:limit]


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--dry-run", action="store_true", default=True, help="Preview only")
    parser.add_argument("--apply", action="store_true", help="Actually write changes")
    args = parser.parse_args()

    candidates = select_candidates(50)
    print(f"Selected {len(candidates)} candidates for quality label migration\n")

    stats = Counter()
    results = []

    for p, score, fm in candidates:
        labels = analyze_card(fm)
        if labels is None:
            continue
        if not labels:
            continue
        for lb in labels:
            stats[lb] += 1
        rel_path = str(p.relative_to(WIKI))
        results.append((rel_path, labels, score))
        print(f"  [{score:2d}] {rel_path}")
        print(f"        labels: {labels}")

    print(f"\n--- Summary ---")
    print(f"Cards to label: {len(results)}")
    print(f"Label distribution:")
    for lb, count in stats.most_common():
        print(f"  {lb}: {count}")

    if args.apply:
        applied = 0
        skipped = 0
        for rel_path, labels, _ in results:
            p = WIKI / rel_path
            text = p.read_text(encoding="utf-8", errors="ignore")

            # Defensive: skip if frontmatter already contains quality_labels
            parts = text.split("---", 2)
            if len(parts) >= 2 and "quality_labels:" in parts[1]:
                skipped += 1
                print(f"  SKIP {rel_path}: already has quality_labels in frontmatter")
                continue

            # Build quality_labels YAML block
            label_lines = "\n".join([f"  - {lb}" for lb in labels])
            quality_block = f"quality_labels:\n{label_lines}"

            # Insert into frontmatter. Try created_at -> updated_at -> end of frontmatter.
            lines = text.split("\n")
            new_lines = []
            inserted = False
            frontmatter_closed = False
            for idx, line in enumerate(lines):
                s = line.strip()
                # First try: insert before created_at
                if s.startswith("created_at:") and not inserted:
                    new_lines.append(quality_block)
                    inserted = True
                # Second try: insert before updated_at
                elif s.startswith("updated_at:") and not inserted:
                    new_lines.append(quality_block)
                    inserted = True
                # Third try: insert before the closing '---' of frontmatter
                elif line == "---" and not inserted and idx > 0 and not frontmatter_closed:
                    # Make sure this is the closing delimiter (we are still inside frontmatter)
                    new_lines.append(quality_block)
                    inserted = True
                    frontmatter_closed = True
                new_lines.append(line)

            if not inserted:
                skipped += 1
                print(f"  SKIP {rel_path}: could not locate frontmatter insertion point")
                continue

            new_text = "\n".join(new_lines)

            # Verify YAML round-trip
            try:
                parts2 = new_text.split("---", 2)
                yaml.safe_load(parts2[1])
                p.write_text(new_text, encoding="utf-8")
                applied += 1
            except Exception as e:
                skipped += 1
                print(f"  SKIP {rel_path}: YAML verify failed: {e}")

        print(f"\nApplied: {applied} cards")
        if skipped:
            print(f"Skipped: {skipped} cards")

    if not args.apply:
        print("\n(Dry-run — use --apply to write changes)")


if __name__ == "__main__":
    main()
