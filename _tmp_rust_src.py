import yaml
for c in ['rust-borrowing-references.md','rust-domain-overview.md','rust-error-handling.md']:
    with open("30_wiki/concepts/"+c, encoding="utf-8") as f:
        text = f.read()
    fm = yaml.safe_load(text.split("---",2)[1])
    src = fm.get("source_refs", "MISSING")
    print(f"{c}: source_refs = {src}")
