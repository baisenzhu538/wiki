"""Add source_refs: pending_archive to all 8 Rust cards."""
import yaml, re

cards = [
    "30_wiki/concepts/rust-domain-overview.md",
    "30_wiki/concepts/rust-ownership-basics.md",
    "30_wiki/concepts/rust-borrowing-references.md",
    "30_wiki/concepts/rust-lifetimes.md",
    "30_wiki/concepts/rust-traits-generics.md",
    "30_wiki/concepts/rust-smart-pointers.md",
    "30_wiki/concepts/rust-concurrency-send-sync.md",
    "30_wiki/concepts/rust-error-handling.md",
]

for path in cards:
    with open(path, encoding="utf-8") as f:
        text = f.read()

    # Insert source_refs before created_at (or updated_at if no created_at)
    lines = text.split("\n")
    new_lines = []
    inserted = False

    for line in lines:
        s = line.strip()
        # Insert before created_at if found and not yet inserted
        if not inserted and (s.startswith("created_at:") or s.startswith("updated_at:")):
            new_lines.append("source_refs:")
            new_lines.append("  - pending_archive")
            inserted = True
        new_lines.append(line)

    if inserted:
        new_text = "\n".join(new_lines)
        # Verify YAML
        try:
            parts = new_text.split("---", 2)
            yaml.safe_load(parts[1])
            with open(path, "w", encoding="utf-8") as f:
                f.write(new_text)
            print(f"  OK: {path}")
        except Exception as e:
            print(f"  FAIL: {path}: {e}")
    else:
        print(f"  SKIP: {path} (no anchor found)")
