import pathlib

f = pathlib.Path("30_wiki/concepts/master-ai-info-literacy.md")
content = f.read_text(encoding="utf-8")
lines = content.splitlines()
h2s = [l[3:].strip() for l in lines if l.startswith("## ")]
print("H2s:", h2s)
print("has_rk:", "Reusable Knowledge" in h2s)
print("has_oq:", "Open Questions" in h2s)
print("has_cb:", "Constraints & Boundaries" in h2s)
print("has_fg:", "Framework Gallery" in h2s)
print("has_critique:", any("Critique" in h for h in h2s))
