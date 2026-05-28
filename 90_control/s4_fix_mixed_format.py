"""S4-3: Unify old/new format headings — remove or rename ## Constraints & Boundaries."""
import json
import re
from pathlib import Path

VAULT = Path(r"C:\Users\Administrator\Desktop\wiki")

with open(VAULT / "90_control" / "s4-mixed-format.json", "r", encoding="utf-8") as f:
    data = json.load(f)

OLD_HEADING = "## Constraints & Boundaries"
NEW_HEADING = "## Critique"


def get_section_content(content, heading):
    """Return (start, end, body) of a ## heading section, or None."""
    idx = content.find(heading)
    if idx == -1:
        return None
    body_start = idx + len(heading)
    # Find next ## heading after this one
    next_h = re.search(r'^## ', content[body_start:], re.MULTILINE)
    if next_h:
        body_end = body_start + next_h.start()
    else:
        body_end = len(content)
    body = content[body_start:body_end].strip()
    return idx, body_end, body


fixed_remove = 0
fixed_rename = 0
fixed_migrate = 0

for card in data["cards"]:
    fpath = VAULT / card["file"]
    if not fpath.exists():
        print(f"MISSING: {card['file']}")
        continue

    content = fpath.read_text(encoding="utf-8")

    for c in card["conflicts"]:
        if c["action"] == "rename_to_new":
            content = content.replace(OLD_HEADING, NEW_HEADING, 1)
            fixed_rename += 1

        elif c["action"] == "remove_old":
            old_sec = get_section_content(content, OLD_HEADING)
            new_sec = get_section_content(content, NEW_HEADING)

            if old_sec is None:
                continue

            old_start, old_end, old_body = old_sec

            # Check if new section is empty and old has content → migrate
            if new_sec and old_body and not new_sec[2]:
                # Migrate: insert old body into new section, remove old section
                new_idx = new_sec[0] + len(NEW_HEADING)
                content = content[:new_idx] + "\n\n" + old_body + content[new_idx:]
                # Remove old section (adjusted for potential offset if old is after new)
                old_start2 = content.find(OLD_HEADING)
                if old_start2 != -1:
                    old_end2 = old_start2 + len(OLD_HEADING)
                    next_h2 = re.search(r'^## ', content[old_end2:], re.MULTILINE)
                    if next_h2:
                        old_end2 += next_h2.start()
                    else:
                        old_end2 = len(content)
                    content = content[:old_start2] + content[old_end2:]
                fixed_migrate += 1
            else:
                # Simple removal: delete old heading + content until next ##
                content = content[:old_start] + content[old_end:]
                fixed_remove += 1

    fpath.write_text(content, encoding="utf-8")

print(f"remove_old (delete): {fixed_remove}")
print(f"remove_old (migrate): {fixed_migrate}")
print(f"rename_to_new: {fixed_rename}")
print(f"Total: {fixed_remove + fixed_migrate + fixed_rename}")
