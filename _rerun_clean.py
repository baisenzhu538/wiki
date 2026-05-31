"""Re-run clean_cards with fixed yaml parser on all cards."""
import sys
sys.path.insert(0, "40_outputs/capabilities/skills/data-curator/scripts")
from clean_cards import clean_card
from pathlib import Path

concepts = Path("30_wiki/concepts")
cards = sorted(concepts.glob("*.md"))
written = 0
clean = 0
errors = 0

for card in cards:
    result = clean_card(card, dry_run=False, backup=False)
    status = result["status"]
    if status == "written":
        written += 1
    elif status == "clean":
        clean += 1
    else:
        errors += 1
        print("  {}: {} — {}".format(status, card.stem, result.get("reason", "?")))

print("Written: {}, Clean: {}, Errors: {}, Total: {}".format(written, clean, errors, len(cards)))
