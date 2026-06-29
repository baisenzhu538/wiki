import yaml, re
from pathlib import Path

wiki = Path("30_wiki")
fixed = 0
failed = 0

for p in wiki.rglob("*.md"):
    if "_archive" in str(p):
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
    
    # Try to parse - if it succeeds, skip
    try:
        yaml.safe_load(parts[1])
        continue
    except:
        pass
    
    # Parse failed - fix indentation
    lines = text.split("\n")
    new_lines = []
    section_indent = None  # expected indent for list items in current section
    in_section = False
    section_name = None
    
    for i, line in enumerate(lines):
        stripped = line.strip()
        
        # Detect list-valued fields
        if re.match(r'^(related|source_refs|domain|tags|diagnostic_signals|bridges_to|aliases|query_triggers|pipeline|wiki_refs):\s*$', stripped):
            section_name = stripped.split(":")[0]
            in_section = True
            # Determine expected indent from the line itself
            section_indent = len(line) - len(line.lstrip())
            new_lines.append(line)
            continue
        
        # Detect next top-level field (end of list section)
        if in_section and line and line[0] not in (" ", "\t", "-") and ":" in stripped:
            in_section = False
            section_indent = None
            new_lines.append(line)
            continue
        
        # Fix list item indent in current section
        if in_section and stripped.startswith("- ") and section_indent is not None:
            # Ensure list items are indented section_indent + 2
            expected_indent = section_indent + 2
            # Rebuild the line with correct indent
            item_content = stripped[2:]  # remove "- "
            new_line = " " * expected_indent + "- " + item_content
            new_lines.append(new_line)
            continue
        
        new_lines.append(line)
    
    new_text = "\n".join(new_lines)
    parts2 = new_text.split("---", 2)
    if len(parts2) >= 3:
        try:
            yaml.safe_load(parts2[1])
            p.write_text(new_text, encoding="utf-8")
            fixed += 1
        except:
            failed += 1
    else:
        failed += 1

print(f"YAML indent fixes applied: {fixed}")
print(f"Still failing after fix: {failed}")
