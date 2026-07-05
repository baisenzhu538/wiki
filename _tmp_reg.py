import sys; sys.path.insert(0, "kdo-tools")
from transcript_registry import register, load_registry
from pathlib import Path
register(Path("C:/Users/Administrator/Desktop/wiki/00_inbox/人机协作双三角/一堂双三角-人机协作模型-口述.txt"))
data = load_registry()
print(f"Registered: {len(data['transcripts'])} transcript(s)")
for path, info in data["transcripts"].items():
    print(f"  {path}")
    for a in info["assets"]:
        print(f"    → {a}")
