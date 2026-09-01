import pathlib

dir = pathlib.Path("30_wiki/concepts")
needs_fix = []

for f in sorted(dir.glob("*.md")):
    content = f.read_text(encoding="utf-8")
    lines = content.splitlines()
    h2s = [l[3:].strip() for l in lines if l.startswith("## ")]
    h4_count = sum(1 for l in lines if l.startswith("#### "))
    
    # Classify
    has_cb = "Constraints & Boundaries" in h2s
    has_fg = "Framework Gallery" in h2s
    has_critique = any("Critique" in h for h in h2s)
    has_rk = "Reusable Knowledge" in h2s
    has_oq = "Open Questions" in h2s
    
    if has_rk or has_oq:
        structure = "research"
    elif has_cb and has_fg:
        structure = "pan-product-upgraded" if has_critique else "pan-product"
    elif len(h2s) <= 3 and any(h in h2s for h in ["Summary", "Index", "内容"]):
        structure = "catalog-index"
    elif "Condense" in h2s or "Critique" in h2s or ("Constraints" in h2s and has_critique):
        structure = "standard-concept"
    else:
        structure = "other"
    
    if structure in ("pan-product", "pan-product-upgraded", "standard-concept", "research"):
        required_h4 = 2 if structure in ("pan-product", "pan-product-upgraded", "standard-concept") else 1
        if h4_count < required_h4:
            needs_fix.append((f.stem, structure, h4_count, required_h4))

print(f"Cards needing H4 fix: {len(needs_fix)}")
for name, st, h4, req in needs_fix[:30]:
    print(f"  {name} ({st}) H4={h4}/{req}")
