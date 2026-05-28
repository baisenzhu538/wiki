"""S4-2: Fix missing frontmatter fields (id/type/status)."""
import json
import re
from pathlib import Path

VAULT = Path(r"C:\Users\Administrator\Desktop\wiki")

with open(VAULT / "90_control" / "s4-frontmatter-missing.json", "r", encoding="utf-8") as f:
    data = json.load(f)

FM_RE = re.compile(r'^---\s*\n(.*?)\n---', re.DOTALL)

fixed = 0
errors = 0

def add_or_fill_field(fm_text, key, value):
    """Add key: value if missing, fill if key exists but empty."""
    if re.search(rf'^{key}:\s*\S', fm_text, re.MULTILINE):
        return fm_text  # already has non-empty value
    if re.search(rf'^{key}:\s*$', fm_text, re.MULTILINE):
        return re.sub(rf'^{key}:\s*$', f'{key}: {value}', fm_text, flags=re.MULTILINE)
    # Key not present — add after the first line or at start
    lines = fm_text.split('\n')
    inserted = False
    for i, line in enumerate(lines):
        if ':' in line:
            continue
        if not inserted:
            lines.insert(i, f'{key}: {value}')
            inserted = True
            break
    if not inserted:
        lines.append(f'{key}: {value}')
    return '\n'.join(lines)


for card in data["cards_with_issues"]:
    fpath = VAULT / card["file"]
    if not fpath.exists():
        print(f"MISSING: {card['file']}")
        errors += 1
        continue

    content = fpath.read_text(encoding="utf-8")
    fix = card["suggested_fix"]

    if "no_frontmatter" in card["issues"]:
        fm_block = "---\n"
        if "id" in fix:
            fm_block += f"id: {fix['id']}\n"
        if "type" in fix:
            fm_block += f"type: {fix['type']}\n"
        if "status" in fix:
            fm_block += f"status: {fix['status']}\n"
        fm_block += "title: \ncreated_at: \nupdated_at: \n---\n\n"
        content = fm_block + content
    else:
        m = FM_RE.match(content)
        if not m:
            print(f"NO FM: {card['file']}")
            errors += 1
            continue

        old_fm = m.group(0)
        fm_inner = m.group(1)

        if "id" in card["issues"] and "id" in fix:
            fm_inner = add_or_fill_field(fm_inner, "id", fix["id"])
        if "type" in card["issues"] and "type" in fix:
            fm_inner = add_or_fill_field(fm_inner, "type", fix["type"])
        if "status" in card["issues"] and "status" in fix:
            fm_inner = add_or_fill_field(fm_inner, "status", fix["status"])

        new_fm = f"---\n{fm_inner}\n---"
        content = content.replace(old_fm, new_fm, 1)

    fpath.write_text(content, encoding="utf-8")
    fixed += 1

print(f"Fixed: {fixed}, Errors: {errors}")
