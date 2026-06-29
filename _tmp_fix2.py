import yaml

def fix_file(path):
    with open(path, encoding="utf-8") as f:
        text = f.read()
    lines = text.split("\n")
    new_lines = []
    in_source = False
    source_indent = None

    for i, line in enumerate(lines):
        s = line.strip()
        if s == "source_refs:":
            in_source = True
            source_indent = len(line) - len(line.lstrip())
            new_lines.append(line)
            continue
        if in_source and line and line[0] not in (" ", "\t", "-") and ":" in s:
            in_source = False
        if in_source and s.startswith("- ") and source_indent is not None:
            expected = source_indent + 2
            current = len(line) - len(line.lstrip())
            if current == 0:  # broken indent - fix it
                new_lines.append(" " * expected + "-" + line.lstrip()[1:])
                continue
        new_lines.append(line)

    new_text = "\n".join(new_lines)
    parts = new_text.split("---", 2)
    if len(parts) >= 3:
        try:
            yaml.safe_load(parts[1])
            with open(path, "w", encoding="utf-8") as f:
                f.write(new_text)
            return True, "OK"
        except Exception as e:
            return False, str(e)
    return False, "No frontmatter found"

# Fix both files
for p in ["30_wiki/concepts/yitang-qualitative-to-quantitative.md",
          "30_wiki/dark-knowledges/dk-skill-market-agent-self-install.md"]:
    ok, msg = fix_file(p)
    print(f"{'FIXED' if ok else 'FAILED'}: {p} - {msg}")
