#!/usr/bin/env python3
"""#227 final pass — �?key pattern + unicode cleanup"""
import re, yaml
from pathlib import Path

root = Path(r'C:\Users\Administrator\Desktop\wiki')
KEYS = ['title:', 'type:', 'reviewed_by:', 'source_refs:', 'related:',
        'status:', 'confidence:', 'domain:', 'created_at:', 'updated_at:',
        'author:', 'aliases:', 'tags:', 'discoverable_by:', 'diagnostic_signals:',
        'bridges_to:', 'review_date:', 'trust_level:', 'review_notes:']
fixed = 0

for fp in root.rglob("30_wiki/**/*.md"):
    if "_archive" in str(fp): continue
    t = fp.read_text(encoding="utf-8", errors="replace")
    m = re.match(r'^---\s*\n(.*?)\n---\s*\n', t, re.DOTALL)
    if not m: continue
    fm, body = m.group(1), t[m.end():]
    try: yaml.safe_load(fm); continue
    except: pass

    for key in KEYS:
        fm = fm.replace('\ufffd?' + key, '\n' + key)
        fm = fm.replace('\ufffd' + key, '\n' + key)
    fm = fm.replace('\ufffd?', '')
    while '\ufffd' in fm:
        fm = fm.replace('\ufffd', '')
    fm = re.sub(r'[\x00-\x08\x0b\x0c\x0e-\x1f\xad]', '', fm)
    fm = re.sub(r'(\S)  +([a-zA-Z_]\w*\s*:)', r'\1\n\2', fm)
    nf = '\n'.join(l.rstrip() for l in fm.splitlines() if l.rstrip())
    try:
        yaml.safe_load(nf)
        fp.write_text('---\n' + nf + '\n---\n' + body, encoding="utf-8")
        fixed += 1
    except: pass

rem = 0
for fp in root.rglob("30_wiki/**/*.md"):
    if "_archive" in str(fp): continue
    t = fp.read_text(encoding="utf-8", errors="replace")
    m2 = re.match(r'^---\s*\n(.*?)\n---\s*\n', t, re.DOTALL)
    if not m2: continue
    try: yaml.safe_load(m2.group(1))
    except: rem += 1

double = sum(1 for fp in root.rglob("30_wiki/**/*.md")
    if "_archive" not in str(fp)
    and len(re.findall(r'^aliases:\s*$', fp.read_text(encoding="utf-8", errors="replace"), re.MULTILINE)) > 1)

print(f"Fixed: {fixed} | YAML broken: {rem} | Double aliases: {double}")
