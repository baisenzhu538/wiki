import pathlib, re

dir = pathlib.Path("30_wiki/concepts")

for f in sorted(dir.glob("*.md")):
    content = f.read_text(encoding="utf-8")
    lines = content.splitlines()
    
    # Check if pan-product
    h2s = [l[3:].strip() for l in lines if l.startswith("## ")]
    has_cb = "Constraints & Boundaries" in h2s
    has_fg = "Framework Gallery" in h2s
    has_critique = any("Critique" in h for h in h2s)
    
    if not (has_cb and has_fg):
        continue
    if has_critique:
        continue  # Already has Critique
    
    # Find external attack H3 in Framework Gallery
    attack_line_idx = None
    for i, l in enumerate(lines):
        if l.startswith("### ") and ("外部攻击" in l or "攻击" in l):
            attack_line_idx = i
            break
    
    if attack_line_idx is None:
        continue
    
    # Find the end of attack section (next ## or ### that is not part of attack)
    end_idx = len(lines)
    for i in range(attack_line_idx + 1, len(lines)):
        if lines[i].startswith("## "):
            end_idx = i
            break
        # Also stop at next ### if it's not part of the attack content
        # Attack content usually starts with **Name**
        if lines[i].startswith("### ") and not lines[i].startswith("### 外部攻击"):
            end_idx = i
            break
    
    attack_content = lines[attack_line_idx:end_idx]
    
    # Parse attack title
    attack_title = attack_content[0][4:].strip()  # Remove "### "
    
    # Extract attacker names and convert to H4
    new_content = ["## Critique", "", "### 外部攻击", ""]
    
    for line in attack_content[1:]:
        # Check if line starts with **Name**(...)
        m = re.match(r'^\*\*([^*]+)\*\*\uff08', line)
        if m:
            name = m.group(1).strip()
            # Try to extract title from attack_title
            # Format: "外部攻击：X的'Y' + Z的'W'"
            new_content.append(f"#### {name}：批判")
            new_content.append("")
        elif line.strip():
            new_content.append(line)
    
    if len(new_content) <= 4:
        continue  # No attackers found
    
    # Build new file content
    new_lines = lines[:attack_line_idx] + new_content + lines[end_idx:]
    
    # Write back
    f.write_text("\n".join(new_lines), encoding="utf-8")
    print(f"Fixed: {f.stem}")
