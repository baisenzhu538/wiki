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
    
    lines = original_text.split("\n")
    in_related = False
    fixed_count = 0
    new_lines = []
    
    for i, line in enumerate(lines):
        stripped = line.strip()
        
        if stripped == "related:" or stripped.startswith("related:"):
            in_related = True
            new_lines.append(line)
            continue
        
        if in_related and line and line[0] not in (" ", "\t", "-"):
            if ":" in stripped:
                in_related = False
        
        if in_related and stripped.startswith("- - - "):
            # Triple-nested: "- - - card-name" → '- "[[card-name]]"'
            indent = line[:len(line) - len(line.lstrip())]
            card_name = stripped[6:].strip()  # remove "- - - "
            # Remove any trailing spaces or comments
            card_name = card_name.split("#")[0].strip()
            if card_name:
                new_line = f'{indent}- "[[{card_name}]]"'
                new_lines.append(new_line)
                fixed_count += 1
                continue
        elif in_related and stripped.startswith("- - "):
            # Double-nested: "- - card-name" → '- "[[card-name]]"'
            indent = line[:len(line) - len(line.lstrip())]
            card_name = stripped[4:].strip()
            card_name = card_name.split("#")[0].strip()
            if card_name:
                new_line = f'{indent}- "[[{card_name}]]"'
                new_lines.append(new_line)
                fixed_count += 1
                continue
        
        new_lines.append(line)
    
    if fixed_count > 0:
        new_text = "\n".join(new_lines)
        try:
            parts2 = new_text.split("---", 2)
            fm2 = yaml.safe_load(parts2[1])
            related2 = fm2.get("related", [])
            if isinstance(related2, list) and related2:
                first = related2[0]
                if isinstance(first, str):
                    p.write_text(new_text, encoding="utf-8")
                    total_files += 1
                    total_fixes += fixed_count
                else:
                    errors.append(f"Still nested after fix: {p.relative_to(wiki)}: {type(first).__name__} = {str(first)[:80]}")
        except Exception as e:
            errors.append(f"VERIFY ERROR: {p.relative_to(wiki)}: {e}")

print(f"Files fixed (round 2): {total_files}")
print(f"Entries fixed (round 2): {total_fixes}")
print(f"Errors: {len(errors)}")
for e in errors[:15]:
    print(f"  {e}")
