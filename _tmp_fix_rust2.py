import yaml

rust_cards = [
    "30_wiki/concepts/rust-domain-overview.md",
    "30_wiki/concepts/rust-ownership-basics.md",
    "30_wiki/concepts/rust-borrowing-references.md",
    "30_wiki/concepts/rust-lifetimes.md",
    "30_wiki/concepts/rust-traits-generics.md",
    "30_wiki/concepts/rust-smart-pointers.md",
    "30_wiki/concepts/rust-concurrency-send-sync.md",
    "30_wiki/concepts/rust-error-handling.md",
]

for card in rust_cards:
    with open(card, encoding="utf-8") as f:
        text = f.read()
    parts = text.split("---", 2)
    fm = yaml.safe_load(parts[1])
    src = fm.get("source_refs", [])
    if not src:
        lines = text.split("\n")
        new_lines = []
        fixed = False
        skip_next = False
        for i, line in enumerate(lines):
            s = line.strip()
            if s == "source_refs:" or s == "source_refs: []":
                new_lines.append("source_refs:")
                new_lines.append("  - pending_archive")
                fixed = True
                skip_next = True
                continue
            if skip_next and s.startswith("- "):
                continue
            skip_next = False
            new_lines.append(line)
        new_text = "\n".join(new_lines)
        parts2 = new_text.split("---", 2)
        try:
            yaml.safe_load(parts2[1])
            with open(card, "w", encoding="utf-8") as f:
                f.write(new_text)
            print(f"  FIXED: {card}")
        except Exception as e:
            print(f"  FAIL: {card}: {e}")
    else:
        print(f"  SKIP: {card}")
