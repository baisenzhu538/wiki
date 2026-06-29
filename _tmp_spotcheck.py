import yaml

samples = [
    "30_wiki/cases/case-ai-agent-milestone-design.md",
    "30_wiki/cases/case-apple-card-gender-bias.md",
    "30_wiki/frameworks/framework-kdo-self-attack.md",
]

for s in samples:
    try:
        with open(s, encoding="utf-8") as f:
            text = f.read()
        parts = text.split("---", 2)
        fm = yaml.safe_load(parts[1])
        related = fm.get("related", [])
        first = related[0] if related else None
        status = "STRING" if isinstance(first, str) else f"NESTED LIST ({type(first).__name__})" if isinstance(first, list) else f"OTHER ({type(first).__name__})"
        print(f"{s}: related[0] type = {status}")
        if isinstance(first, str):
            print(f"  First entry: {first[:80]}")
        elif isinstance(first, list):
            print(f"  First entry (nested): {first}")
    except Exception as e:
        print(f"{s}: ERROR - {e}")
