import sys
sys.path.insert(0, "90_control/scripts")
from cross_domain_audit import load_cards, domain_of, extract_related_ids
from pathlib import Path

vault = Path(".")
cards = load_cards(vault)
cid = "framework-strategy-lean-validation"
fm = cards.get(cid, {})
print(f"{cid} in cards: {cid in cards}")
rel_ids = extract_related_ids(fm)
print(f"related IDs: {rel_ids}")
for rid in rel_ids:
    d = domain_of(rid, cards)
    print(f"  {rid} -> domain={d} (in cards: {rid in cards})")
print(f"")
target = {"strategy", "lean-startup"}
domains = {domain_of(r, cards) for r in rel_ids if r}
print(f"Computed domains: {sorted(domains)}")
print(f"Target: {sorted(target)}")
print(f"Covered: {sorted(domains & target)}")
