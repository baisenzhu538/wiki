"""Safe string-replacement fix: dict URL -> src_unknown + OCR fuzzy >= 0.90"""
import difflib, re, yaml
from pathlib import Path

ROOT = Path(r"C:\Users\Administrator\Desktop\wiki")

# Build file index (name -> path)
file_index = {}
for d in ["00_inbox", "10_raw"]:
    for f in (ROOT / d).rglob("*"):
        if f.is_file():
            rel = str(f.relative_to(ROOT)).replace("\\", "/")
            file_index[rel] = rel
            file_index[f.name] = rel

n_dict, n_ocr = 0, 0
mid = []

for md in (ROOT / "30_wiki").rglob("*.md"):
    if ".trash" in md.parts: continue
    raw = md.read_text(encoding="utf-8", errors="replace")
    changed = False

    # 1. Dict URL -> src_unknown
    for pattern in re.findall(r"\{'web':\s*'[^']*'\}", raw):
        raw = raw.replace(pattern, "src_unknown")
        n_dict += 1
        changed = True

    # 2. OCR fuzzy match
    for old_ref in re.findall(r"^(\s*-\s+)(.+\.(?:md|txt|png|pdf))", raw, re.MULTILINE):
        prefix, ref = old_ref
        ref_s = ref.strip()
        if ref_s.startswith("src_"): continue
        if (ROOT / ref_s.replace("\\", "/")).exists(): continue

        fn = Path(ref_s).name
        if fn in file_index:
            raw = raw.replace(ref_s, file_index[fn])
            n_ocr += 1
            changed = True
            continue

        stem = Path(ref_s).stem
        clean_stem = re.sub(r'\s+\d+(-\d+)?$', '', stem)
        best, best_r = "", 0.0
        for name, path in file_index.items():
            r = difflib.SequenceMatcher(None, clean_stem, Path(name).stem).ratio()
            if r > best_r:
                best_r = r
                best = path
        if best_r >= 0.90:
            raw = raw.replace(ref_s, best)
            n_ocr += 1
            changed = True
        elif best_r >= 0.85:
            mid.append((str(md.relative_to(ROOT)).replace("\\","/"), ref_s, best, best_r))

    if changed:
        md.write_text(raw, encoding="utf-8")

print(f"dict URL -> src_unknown: {n_dict}")
print(f"OCR fuzzy >= 0.90:   {n_ocr}")
print(f"0.85-0.89 for review: {len(mid)}")
if mid:
    print("\n=== 0.85-0.89 samples ===")
    for card, old, new, conf in mid[:10]:
        print(f"  {card}: {old[:80]} -> {new} ({conf:.0%})")
