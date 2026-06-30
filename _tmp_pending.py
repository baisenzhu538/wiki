import yaml
from pathlib import Path

wiki = Path("30_wiki")
pending_cards = []

for p in wiki.rglob("*.md"):
    if "_archive" in str(p) or "raw/ocr" in str(p):
        continue
    try:
        text = p.read_text(encoding="utf-8", errors="ignore")
    except:
        continue
    if not text.startswith("---"):
        continue
    parts = text.split("---", 2)
    if len(parts) < 3:
        continue
    try:
        fm = yaml.safe_load(parts[1])
    except:
        continue
    if not fm or not isinstance(fm, dict):
        continue
    related = fm.get("related", [])
    if not isinstance(related, list) or not related:
        continue
    # Check if ALL entries are pending_unknown
    all_pending = all(isinstance(r, str) and "pending_unknown" in r.lower() for r in related)
    if all_pending:
        pending_cards.append(p.stem)

print(f"Cards with ONLY pending_unknown in related: {len(pending_cards)}")
for c in pending_cards[:30]:
    print(f"  {c}")
if len(pending_cards) > 30:
    print(f"  ... and {len(pending_cards) - 30} more")
