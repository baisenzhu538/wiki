import yaml
samples = [
    "30_wiki/frameworks/framework-kdo-self-attack.md",
    "30_wiki/tools/tool-yitang-channel-scan-cheat-sheet.md",
    "30_wiki/cases/case-yitang-goat-milk-channel-partnership.md",
]
for s in samples:
    with open(s, encoding="utf-8") as f:
        text = f.read()
    parts = text.split("---", 2)
    fm = yaml.safe_load(parts[1])
    ql = fm.get("quality_labels", "MISSING!")
    print(f"{s}: {ql}")
