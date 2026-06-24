import re, sys
sys.path.insert(0, "90_control/scripts")
from cross_domain_audit import parse_frontmatter, extract_related_ids
from pathlib import Path

fp = Path("30_wiki/frameworks/framework-strategy-lean-validation.md")
text = fp.read_text(encoding="utf-8")
fm = parse_frontmatter(text)
if fm:
    print("id:", fm.get("id"))
    rel = fm.get("related")
    print("related raw:", repr(rel))
    ids = extract_related_ids(fm)
    print("extracted IDs:", ids)
else:
    print("parse_frontmatter returned None")
    end = text.find("---", 3)
    fm_text = text[3:end]
    # Show related section
    idx = fm_text.find("related:")
    if idx >= 0:
        print("FM section around related:")
        print(repr(fm_text[idx:idx+300]))
