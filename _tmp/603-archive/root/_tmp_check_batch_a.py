import pathlib

batch_a = [
    "yt-composite-pan-product-methodology",
    "yt-model-pan-product-36-strategies",
    "yt-model-pan-product-aesthetic-toolkit",
    "yt-model-pan-product-climbing-map",
    "yt-model-pan-product-demand-toolkit",
    "yt-model-pan-product-execution-toolkit",
    "yt-model-pan-product-three-virtues",
    "yt-personal-knowledge-extraction",
    "yt-prompt-anti-flattery",
    "yt-prompt-brainstorming",
    "yt-prompt-engineering-andrew-ng",
    "yt-prompt-iterative-prompting",
    "yt-prompt-writing-workflow",
]

dir = pathlib.Path("30_wiki/concepts")
for name in batch_a:
    f = dir / f"{name}.md"
    if not f.exists():
        print(f"{name}: FILE NOT FOUND")
        continue
    content = f.read_text(encoding="utf-8")
    lines = content.splitlines()
    
    has_at = any("action triggers" in l.lower() for l in lines if l.startswith("## ") or l.startswith("### "))
    has_dontuse = any("don't use" in l.lower() or "dont use" in l.lower() or "不用" in l for l in lines if l.startswith("### "))
    h4_count = sum(1 for l in lines if l.startswith("#### "))
    
    print(f"{name}: AT={has_at} DU={has_dontuse} H4={h4_count}")
