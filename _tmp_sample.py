import yaml
from pathlib import Path

wiki = Path("30_wiki")
# Sample some cards to understand related format
samples = [
    "concepts/yt-decision-y-model.md",
    "frameworks/framework-kdo-self-attack.md", 
    "cases/case-five-step-growth-first-lever.md",
    "concepts/yt-five-step-method.md",
    "concepts/concept-five-step-growth-to-barrier-transition.md",
]
for s in samples:
    p = wiki / s
    if not p.exists():
        print(f"MISSING: {s}")
        continue
    try:
        text = p.read_text(encoding="utf-8", errors="ignore")
        parts = text.split("---", 2)
        fm = yaml.safe_load(parts[1])
        related = fm.get("related", "NO FIELD")
        print(f"\n=== {s} ===")
        print(f"related ({len(related) if isinstance(related, list) else 'N/A'} items): {related}")
    except Exception as e:
        print(f"ERROR {s}: {e}")
