import re, yaml
from pathlib import Path

wiki = Path("30_wiki")
total_files = 0
total_fixes = 0
errors = []

for p in wiki.rglob("*.md"):
    if "_archive" in str(p) or "raw/ocr" in str(p):
        continue
    try:
        original_text = p.read_text(encoding="utf-8", errors="ignore")
    except:
        continue
    if not original_text.startswith("---"):
        continue
    
    parts = original_text.split("---", 2)
    if len(parts) < 3:
        continue
    
    lines = original_text.split("\n")
    in_related = False
    fixed_count = 0
    new_lines = []
    
    for i, line in enumerate(lines):
        stripped = line.strip()
        
        # Detect entering related section
        if stripped == "related:" or stripped.startswith("related:"):
            in_related = True
            new_lines.append(line)
            continue
        
        # Detect leaving related section (non-indented, non-list field with colon)
        if in_related and line and not line[0] in (" ", "\t", "-"):
            if ":" in stripped:
                in_related = False
                new_lines.append(line)
                continue
        
        # Detect next top-level field
        if in_related and line and line[0] not in (" ", "\t", "-"):
            in_related = False
        
        if in_related and stripped.startswith("- [["):
            indent = line[:len(line) - len(line.lstrip())]
            entry = stripped[2:]  # remove "- "
            # Only wrap bare wikilinks (not already quoted)
            if not entry.startswith('"') and entry.startswith('[['):
                # Verify it looks like a complete wikilink
                if entry.endswith(']]'):
                    new_line = f'{indent}- "{entry}"'
                    new_lines.append(new_line)
                    fixed_count += 1
                    continue
                elif ']]' in entry:
                    # Partial match - still fix what we can
                    new_line = f'{indent}- "{entry}"'
                    new_lines.append(new_line)
                    fixed_count += 1
                    continue
        
        new_lines.append(line)
    
    if fixed_count > 0:
        new_text = "\n".join(new_lines)
        
        # Verify the fix: yaml.safe_load should now parse related as strings
        try:
            parts2 = new_text.split("---", 2)
            fm2 = yaml.safe_load(parts2[1])
            related2 = fm2.get("related", [])
            if isinstance(related2, list) and related2:
                # Check first entry is now a string
                if isinstance(related2[0], str):
                    # Fix verified, write back
                    p.write_text(new_text, encoding="utf-8")
                    total_files += 1
                    total_fixes += fixed_count
                else:
                    errors.append(f"FIX FAILED (still nested list): {p.relative_to(wiki)}")
            else:
                # Empty or no related - still write
                p.write_text(new_text, encoding="utf-8")
                total_files += 1
                total_fixes += fixed_count
        except Exception as e:
            errors.append(f"VERIFY ERROR: {p.relative_to(wiki)}: {e}")

print(f"Files fixed: {total_files}")
print(f"Entries fixed: {total_fixes}")
print(f"Errors: {len(errors)}")
for e in errors[:10]:
    print(f"  {e}")
