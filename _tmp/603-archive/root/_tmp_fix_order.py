import pathlib

dir = pathlib.Path("30_wiki/concepts")

for f in sorted(dir.glob("*.md")):
    content = f.read_text(encoding="utf-8")
    lines = content.splitlines()
    
    # Find ## Critique and ## Framework Gallery positions
    critique_idx = None
    fg_idx = None
    cb_idx = None
    for i, l in enumerate(lines):
        if l.startswith("## Critique"):
            critique_idx = i
        elif l.startswith("## Framework Gallery"):
            fg_idx = i
        elif l.startswith("## Constraints & Boundaries"):
            cb_idx = i
    
    if critique_idx is None or fg_idx is None or cb_idx is None:
        continue
    
    if critique_idx > fg_idx:
        # Critique is after Framework Gallery, need to fix order
        # Find end of Critique section (next ## after critique_idx)
        critique_end = len(lines)
        for i in range(critique_idx + 1, len(lines)):
            if lines[i].startswith("## "):
                critique_end = i
                break
        
        # Extract Critique section
        critique_section = lines[critique_idx:critique_end]
        
        # Find end of Constraints & Boundaries section
        cb_end = len(lines)
        for i in range(cb_idx + 1, len(lines)):
            if lines[i].startswith("## "):
                cb_end = i
                break
        
        # Build new content: lines before cb_end + critique + lines from cb_end to critique_idx + lines after critique_end
        new_lines = lines[:cb_end] + critique_section + lines[cb_end:critique_idx] + lines[critique_end:]
        
        f.write_text("\n".join(new_lines), encoding="utf-8")
        print(f"Fixed order: {f.stem}")
