"""Scan domain vs tags mismatch across all cards."""
import re
from pathlib import Path
from collections import Counter

d = Path(r"C:\Users\Administrator\Desktop\wiki\30_wiki\concepts")

TAG_TO_DOMAIN = {
    "#yitang": "yitang",
    "#domain/AI": "ai",
    "#domain/design": "design",
    "#domain/product": "product",
    "#domain/entrepreneurship": "entrepreneur",
    "#domain/decision-making": "decision-making",
    "#domain/knowledge-management": "knowledge-management",
    "#domain/electronics": "electronics",
    "#domain/note-taking": "note-taking",
    "#domain/creative": "creative",
    "#domain/collaboration": "collaboration",
    "#domain/scene-analysis": "scene-analysis",
    "#domain/business-strategy": "business-strategy",
    "#domain/innovation": "innovation",
    "#domain/ai-collaboration": "ai-collaboration",
    "#domain/ai-implementation": "ai",
    "#domain/ai-ethics": "ai",
    "#domain/learning": "learning",
    "#scene/entrepreneurship": "entrepreneur",
    "#scene/business-analysis": "business-strategy",
    "#scene/ai-collaboration": "ai-collaboration",
    "#scene/product-design": "product",
    "#scene/strategy": "business-strategy",
    "#scene/note-taking": "note-taking",
}

total = 0
mismatch = 0
mismatch_by_file = []

for f in sorted(d.glob("*.md")):
    total += 1
    text = f.read_text(encoding="utf-8", errors="replace")
    m = re.search(r"^---\s*\n(.*?)\n---", text, re.DOTALL)
    if not m:
        continue
    fm = m.group(1)

    domains = set()
    in_domain = False
    for line in fm.split("\n"):
        s = line.strip()
        if s.startswith("domain:"):
            in_domain = True
            rest = s.split(":", 1)[1].strip()
            if rest.startswith("[") and "]" in rest:
                for x in rest.strip("[]").split(","):
                    x = x.strip().strip('"').strip("'")
                    if x:
                        domains.add(x.lower())
                in_domain = False
            elif rest and not rest.startswith("["):
                domains.add(rest.strip('"').strip("'").lower())
                in_domain = False
        elif in_domain and s.startswith("- "):
            dom = s[2:].strip().strip('"').strip("'")
            if dom:
                domains.add(dom.lower())
        elif in_domain and not s.startswith("- ") and s:
            in_domain = False

    tags = set()
    in_tags = False
    for line in fm.split("\n"):
        s = line.strip()
        if s.startswith("tags:"):
            in_tags = True
            rest = s.split(":", 1)[1].strip()
            if rest.startswith("[") and "]" in rest:
                for x in rest.strip("[]").split(","):
                    x = x.strip().strip('"').strip("'")
                    if x:
                        tags.add(x)
                in_tags = False
        elif in_tags and s.startswith("- "):
            t = s[2:].strip().strip('"').strip("'")
            if t:
                tags.add(t)
        elif in_tags and not s.startswith("- ") and s:
            in_tags = False

    suggested = set()
    for tag in tags:
        if tag in TAG_TO_DOMAIN:
            suggested.add(TAG_TO_DOMAIN[tag])
        if tag.startswith("#domain/"):
            dom = tag.replace("#domain/", "")
            if dom not in TAG_TO_DOMAIN:
                suggested.add(dom)

    missing = suggested - domains
    if missing:
        mismatch += 1
        mismatch_by_file.append((f.stem, sorted(domains), sorted(missing)))

print(f"Total cards: {total}")
print(f"Mismatch: {mismatch} ({mismatch * 100 // total}%)")
print()

pattern_count = Counter()
for stem, doms, miss in mismatch_by_file:
    for m_item in miss:
        pattern_count[m_item] += 1
print("Top 10 missing domain patterns:")
for pat, cnt in pattern_count.most_common(10):
    print(f"  {pat}: {cnt}")

print()
print("Examples:")
for stem, doms, miss in mismatch_by_file[:20]:
    print(f"  {stem}: domain={doms}  missing={miss}")
