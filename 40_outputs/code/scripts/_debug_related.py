"""Temp debug script — delete after use."""
import sys, re, json
from pathlib import Path

WIKI = Path(r"C:\Users\Administrator\Desktop\wiki\30_wiki")

def extract_text(fpath):
    try:
        raw = fpath.read_text(encoding="utf-8")
    except Exception:
        return ""
    if raw.startswith("---"):
        end = raw.find("---", 3)
        if end != -1:
            raw = raw[end + 3:]
    raw = re.sub(r'\[\[([^\]]+)\]\]', r'\1', raw[:3000])
    return raw

def parse_frontmatter(text):
    if not text.startswith("---"):
        return None
    end = text.find("---", 3)
    if end == -1:
        return None
    fm = {}
    for line in text[3:end].split("\n"):
        if ":" in line:
            k, _, v = line.partition(":")
            k, v = k.strip(), v.strip().strip('"').strip("'")
            if v.startswith("[") and v.endswith("]"):
                fm[k] = [it.strip().strip('"').strip("'") for it in v[1:-1].split(",") if it.strip()]
            else:
                fm[k] = v
    for lk in ["related", "domain", "source_refs", "tags"]:
        if lk in fm and fm[lk] == []:
            pat = re.compile(rf"^{lk}:\n((?:\s+-.+\n?)*)", re.MULTILINE)
            m = pat.search(text[3:end])
            if m:
                items = re.findall(r"^\s*-\s+(.+)$", m.group(1), re.MULTILINE)
                fm[lk] = [it.strip().strip('"').strip("'") for it in items]
    return fm

def get_related(fm):
    rel = fm.get("related", [])
    if isinstance(rel, str):
        rel = [rel]
    ids = set()
    for r in rel:
        if not r or not r.strip():
            continue
        m = re.search(r'\[\[([^\]|]+)', r)
        if m:
            ids.add(m.group(1).strip())
        else:
            ids.add(r.strip())
    return ids

# Find one target card
import glob
for f in glob.glob(str(WIKI / "**" / "*.md"), recursive=True):
    fpath = Path(f)
    text = fpath.read_text(encoding="utf-8")
    fm = parse_frontmatter(text)
    if not fm or "id" not in fm:
        continue
    cid = fm["id"]
    if cid == "plan_20260621_kdo-quality-harness-upgrade":
        print(f"FILE: {fpath}")
        rel_raw = fm.get("related", "KEY NOT FOUND")
        print(f"related type: {type(rel_raw).__name__}")
        print(f"related value: {repr(rel_raw)[:500]}")
        print(f"related == []: {rel_raw == []}")
        print(f"related == '': {rel_raw == ''}")
        rel_parsed = get_related(fm)
        print(f"get_related(): {rel_parsed}")
        # Show actual lines around 'related:' in the raw text
        idx = text.find("related:")
        print(f"\nRaw text around 'related:':")
        print(text[max(0,idx-20):idx+300])
        break
