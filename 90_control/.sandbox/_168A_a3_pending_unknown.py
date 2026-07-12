"""#168A A-3: AI簇 pending_unknown/src_unknown处置 dry-run/apply"""
import re, sys, json
from pathlib import Path
from collections import defaultdict

VAULT = Path(__file__).resolve().parent.parent.parent
DRY = "--apply" not in sys.argv
MANIFEST = []

# Find AI簇 cards (domain contains ai-saas, ai-collaboration, or ai- prefix)
def is_ai_cluster(fm_text):
    domains = re.findall(r'-\s+(\S+)', fm_text[fm_text.find("domain:"):fm_text.find("\n\n", fm_text.find("domain:"))] if "domain:" in fm_text else "")
    return any(d in ["ai-saas", "ai-collaboration"] or d.startswith("ai-") for d in domains)

frontmatter_fixed = 0
related_fixed = 0

for d in ["concepts","frameworks","tools","cases","systems","methods","dark-knowledges","dk","domains","decisions","skills"]:
    dpath = VAULT / "30_wiki" / d
    if not dpath.is_dir(): continue
    for f in dpath.rglob("*.md"):
        try: c = f.read_text(encoding="utf-8", errors="replace")
        except: continue
        fm_match = re.match(r"^(---\s*\n.*?\n---)", c, re.DOTALL)
        if not fm_match: continue
        fm = fm_match.group(1)
        rest = c[len(fm):]
        if not is_ai_cluster(fm): continue

        original_fm = fm
        rel_path = str(f.relative_to(VAULT))

        # ── Frontmatter: remove src_unknown entries ──
        new_fm = re.sub(r'\s*-\s*src_unknown\s*\n', '\n', fm)
        if new_fm != fm:
            frontmatter_fixed += 1

        # ── Related: classify [[pending_unknown]] ──
        for m in re.finditer(r'-\s*["\']?\[\[pending_unknown\]\]["\']?', new_fm):
            # All pending_unknown in AI cluster →摘 (no real target card exists for pending_unknown)
            new_fm = new_fm.replace(m.group(0), "")
            related_fixed += 1
            MANIFEST.append({"card": rel_path, "action": "摘", "target": "pending_unknown", "reason": "AI簇占位符，无对应真实卡片"})

        if new_fm == original_fm: continue

        new_content = new_fm + rest
        if not DRY:
            f.write_text(new_content, encoding="utf-8")

mode = "DRY-RUN" if DRY else "APPLY"
print(f"A-3 {mode}")
print(f"  Frontmatter src_unknown removed: {frontmatter_fixed} cards")
print(f"  Related [[pending_unknown]] removed: {related_fixed} entries")
print(f"  Manifest: {len(MANIFEST)} entries")

if MANIFEST:
    mpath = VAULT / "90_control/.sandbox/a3_pending_unknown_manifest.json"
    if not DRY:
        mpath.write_text(json.dumps(MANIFEST, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"  Manifest -> {mpath}")
if not DRY: print("Done.")
