"""Recover domain fields corrupted by batch script — restore from git history."""
import re, yaml, subprocess
from pathlib import Path

root = Path(r"C:\Users\Administrator\Desktop\wiki")
wiki = root / "30_wiki"

# Find cards where domain is [src_unknown] but wasn't before
affected = []
for md in wiki.rglob("*.md"):
    if ".trash" in md.parts or "decisions" in md.parts:
        continue
    text = md.read_text(encoding="utf-8", errors="replace")
    text_u = text.replace("\r\n", "\n")
    end = text_u.find("\n---\n", 4)
    if end == -1: continue
    try: fm = yaml.safe_load(text_u[4:end])
    except: continue
    if not isinstance(fm, dict): continue
    dv = fm.get("domain", [])
    if isinstance(dv, str): dv = [dv]
    if not dv: continue
    if all(str(d).strip() == "src_unknown" for d in dv):
        affected.append(md)

print(f"Domain corrupted to src_unknown: {len(affected)}")

restored = 0
for md in affected:
    rel = str(md.relative_to(root)).replace("\\", "/")
    # Try git show with encoding
    try:
        result = subprocess.run(
            ["git", "show", f"HEAD~20:{rel}"],
            capture_output=True, text=True, cwd=str(root),
            encoding="utf-8", errors="replace",
        )
    except Exception:
        continue
    if result.returncode != 0 or not result.stdout:
        continue
    old_text = result.stdout.replace("\r\n", "\n")
    old_end = old_text.find("\n---\n", 4)
    if old_end == -1: continue
    try: old_fm = yaml.safe_load(old_text[4:old_end])
    except: continue
    if not isinstance(old_fm, dict): continue
    old_dv = old_fm.get("domain", [])
    if isinstance(old_dv, str): old_dv = [old_dv]
    if not old_dv: continue
    if all(str(d).strip() == "src_unknown" for d in old_dv):
        continue  # was already polluted

    # Restore
    text = md.read_text(encoding="utf-8", errors="replace")
    text_u = text.replace("\r\n", "\n")
    if len(old_dv) == 1:
        new_line = f"domain: {old_dv[0]}"
        text_u = re.sub(r"domain:\s*src_unknown", new_line, text_u)
    else:
        new_block = "domain:\n" + "\n".join(f"  - {d}" for d in old_dv)
        text_u = re.sub(r"domain:\s*\n(\s*-\s*src_unknown\s*\n?)+", new_block + "\n", text_u)
    md.write_text(text_u, encoding="utf-8")
    restored += 1
    if restored <= 10:
        print(f"  {rel}: {old_dv}")

print(f"\nRestored: {restored}")
