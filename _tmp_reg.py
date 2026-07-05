import importlib.util, sys
from pathlib import Path

spec = importlib.util.spec_from_file_location("transcript_registry", "kdo-tools/transcript-registry.py")
mod = importlib.util.module_from_spec(spec)
spec.loader.exec_module(mod)

mod.register(Path("C:/Users/Administrator/Desktop/wiki/00_inbox/人机协作双三角/一堂双三角-人机协作模型-口述.txt").resolve())

data = mod.load_registry()
print(f"Registered: {len(data['transcripts'])} transcript(s)")
for path, info in data["transcripts"].items():
    print(f"  {path}")
    for a in info["assets"]:
        print(f"    -> {a}")
