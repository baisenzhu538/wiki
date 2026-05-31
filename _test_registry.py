from kdo.commands.label import load_tag_registry, flatten_dimensions, prescreen_chunk
from pathlib import Path

root = Path(r"C:\Users\Administrator\Desktop\wiki")
registry = load_tag_registry(root)
dims = flatten_dimensions(registry)
print(f"Dimensions loaded: {len(dims)}")
for name, vals in dims.items():
    print(f"  {name}: {len(vals)} values")
total = sum(len(v) for v in dims.values())
print(f"Total values: {total}")

chunk = "When evaluating a startup idea, use ROI analysis and prioritization frameworks to make decisions."
candidates = prescreen_chunk(chunk, dims, top_k=10)
print(f"\nPre-screen for 'startup ROI': {len(candidates)} candidates")
for c in candidates[:5]:
    print(f"  {c['dimension']}/{c['value']} score={c['score']}")

chunk2 = "LLM prompt engineering for RAG knowledge management with OCR quality scoring"
candidates2 = prescreen_chunk(chunk2, dims, top_k=10)
print(f"\nPre-screen for 'LLM RAG': {len(candidates2)} candidates")
for c in candidates2[:5]:
    print(f"  {c['dimension']}/{c['value']} score={c['score']}")
