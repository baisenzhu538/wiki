import pathlib

dir = pathlib.Path("30_wiki/concepts")
bullet_at = []

for f in sorted(dir.glob("*.md")):
    content = f.read_text(encoding="utf-8")
    lines = content.splitlines()
    
    # Check if has Action Triggers heading
    has_at = any("action triggers" in l.lower() for l in lines if l.startswith("## ") or l.startswith("### "))
    if not has_at:
        continue
    
    # Check AT format
    in_at = False
    has_table = False
    has_bullet = False
    for l in lines:
        if l.startswith("## ") or l.startswith("### "):
            in_at = "action triggers" in l.lower()
        if in_at:
            if l.strip().startswith("|") and l.strip().count("|") >= 3:
                has_table = True
            if l.strip().startswith("- ") or l.strip().startswith("* "):
                has_bullet = True
    
    if has_bullet and not has_table:
        bullet_at.append(f.stem)

print(f"Cards with bullet AT: {len(bullet_at)}")
for name in bullet_at[:20]:
    print(f"  {name}")
