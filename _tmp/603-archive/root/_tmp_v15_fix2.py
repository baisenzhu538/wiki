import pathlib

dir = pathlib.Path("30_wiki/concepts")
pan_product_fix = []
standard_fix = []

for f in sorted(dir.glob("*.md")):
    content = f.read_text(encoding="utf-8")
    lines = content.splitlines()
    h2s = [l[3:].strip() for l in lines if l.startswith("## ")]
    h4_count = sum(1 for l in lines if l.startswith("#### "))
    
    has_cb = "Constraints & Boundaries" in h2s
    has_fg = "Framework Gallery" in h2s
    has_critique = any("Critique" in h for h in h2s)
    has_rk = "Reusable Knowledge" in h2s
    has_oq = "Open Questions" in h2s
    
    if has_rk or has_oq:
        continue  # research - skip
    elif has_cb and has_fg:
        structure = "pan-product-upgraded" if has_critique else "pan-product"
        if h4_count < 2:
            pan_product_fix.append((f.stem, structure, h4_count))
    elif len(h2s) <= 3 and any(h in h2s for h in ["Summary", "Index", "内容"]):
        continue  # catalog-index - skip
    elif "Condense" in h2s or "Critique" in h2s or ("Constraints" in h2s and has_critique):
        if h4_count < 2:
            standard_fix.append((f.stem, "standard-concept", h4_count))
    else:
        continue  # other - skip

print(f"Pan-product needing H4 fix: {len(pan_product_fix)}")
for name, st, h4 in pan_product_fix[:20]:
    print(f"  {name} ({st}) H4={h4}")

print(f"\nStandard-concept needing H4 fix: {len(standard_fix)}")
for name, st, h4 in standard_fix[:20]:
    print(f"  {name} ({st}) H4={h4}")
