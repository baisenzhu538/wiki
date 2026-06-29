import re
from pathlib import Path

wiki = Path("30_wiki")
total_files = 0
total_fixes = 0
sample_output = []

for p in wiki.rglob("*.md"):
    if "_archive" in str(p) or "raw/ocr" in str(p):
        continue
    try:
        text = p.read_text(encoding="utf-8", errors="ignore")
    except:
        continue
    if not text.startswith("---"):
        continue
    
    # Find the frontmatter
    parts = text.split("---", 2)
    if len(parts) < 3:
        continue
    fm_text = parts[1]
    body_and_rest = "---" + parts[2]
    
    # Find related section and fix bare [[...]] entries (not already quoted)
    # Pattern: on a line in related section, match "  - [[" not preceded by '"'
    # We need to be careful to only fix entries that look like YAML inline lists
    # but NOT already-quoted ones
    
    lines = text.split("\n")
    in_related = False
    fixed_count = 0
    new_lines = []
    
    for i, line in enumerate(lines):
        # Track if we're in the related section
        if line.strip().startswith("related:"):
            in_related = True
            new_lines.append(line)
            continue
        elif in_related and line and not line.startswith(" ") and not line.startswith("\t") and ":" not in line.strip():
            in_related = False
        elif in_related and line.strip() and ":" in line.strip() and not line.startswith(" ") and not line.startswith("-"):
            in_related = False
        
        if in_related and line.strip().startswith("- [["):
            # This is a bare [[...]] entry - wrap in quotes
            indent = line[:len(line) - len(line.lstrip())]
            content = line.strip()
            entry = content[2:]  # remove "- "
            # Only fix if not already quoted and is a wikilink
            if not entry.startswith('"') and entry.startswith('[['):
                # Check it looks like a wikilink
                if entry.endswith(']]') or ']]' in entry:
                    new_line = f'{indent}- "{entry}"'
                    new_lines.append(new_line)
                    fixed_count += 1
                    continue
        new_lines.append(line)
    
    if fixed_count > 0:
        total_files += 1
        total_fixes += fixed_count
        if len(sample_output) < 10:
            sample_output.append(f"  {p.relative_to(wiki)}: {fixed_count} entries fixed")

print(f"Files needing fix: {total_files}")
print(f"Total entries to fix: {total_fixes}")
print()
print("Sample files:")
for s in sample_output:
    print(s)
