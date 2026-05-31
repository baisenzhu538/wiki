"""Debug Gold Standard text parsing."""
import re
from pathlib import Path

text = Path(r"C:\Users\Administrator\Desktop\wiki\30_wiki\decisions\gold-standard-manual-labels.md").read_text(encoding="utf-8")

sections = re.split(r'\n## Chunk (\d+)', text)
print("Sections found: {}".format((len(sections)-1)//2))

# Show first chunk raw
for i in range(1, min(5, len(sections)), 2):
    cid = sections[i]
    body = sections[i+1] if i+1 < len(sections) else ""
    print("\n=== Chunk {} ===".format(cid))
    # Find chunk content
    cm = re.search(r'\*\*chunk 内容\*\*\s*\|\s*(.+?)(?=\n\|\s*\n\||\n\n)', body, re.DOTALL)
    if cm:
        txt = cm.group(1).strip().strip('"').strip("'")
        print("Content ({} chars): {}".format(len(txt), txt[:100]))
    else:
        # Try simpler pattern
        lines = body.split("\n")
        for j, l in enumerate(lines[:15]):
            print("L{}: {}".format(j, l[:100]))
        break
