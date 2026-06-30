import yaml
from pathlib import Path

wiki = Path("30_wiki")
rust_cards = [
    "concepts/rust-domain-overview.md",
    "concepts/rust-ownership-basics.md",
    "concepts/rust-borrowing-references.md",
    "concepts/rust-lifetimes.md",
    "concepts/rust-traits-generics.md",
    "concepts/rust-smart-pointers.md",
    "concepts/rust-concurrency-send-sync.md",
    "concepts/rust-error-handling.md",
]

for card in rust_cards:
    p = wiki / card
    if not p.exists():
        print(f"MISSING: {card}")
        continue
    text = p.read_text(encoding="utf-8", errors="ignore")
    parts = text.split("---", 2)
    fm = yaml.safe_load(parts[1])
    src = fm.get("source_refs", [])
    if not src or src == []:
        # Replace empty source_refs with pending_archive placeholder
        lines = text.split("\n")
        new_lines = []
        in_source = False
        fixed = False
        for i, line in enumerate(lines):
            s = line.strip()
            if s == "source_refs:" or s == "source_refs: []":
                new_lines.append("source_refs:")
                new_lines.append("  - pending_archive")
                fixed = True
                in_source = True
                continue
            if in_source and line.strip().startswith("- ") and not fixed:
                continue  # skip old empty entries
            if in_source and line and line[0] not in (" ", "\t", "-") and ":" in s:
                in_source = False
            new_lines.append(line)
        if fixed:
            new_text = "\n".join(new_lines)
            parts2 = new_text.split("---", 2)
            try:
                yaml.safe_load(parts2[1])
                p.write_text(new_text, encoding="utf-8")
                print(f"  FIXED: {card}")
            except Exception as e:
                print(f"  FAILED: {card}: {e}")
    else:
        print(f"  SKIP (has source_refs): {card}")
