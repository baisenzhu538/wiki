#!/usr/bin/env python3
"""#237 — standardize 6 dirty domain names. Second pass with while-loop."""
import re, yaml
from pathlib import Path

root = Path(r'C:\Users\Administrator\Desktop\wiki')
wiki = root / '30_wiki'

MIGRATIONS = {
    'design- design': 'design',
    'yitang- yitang': 'yitang',
    'ai_collaboration': 'ai-collaboration',
    'learning-methodology- product': 'learning-methodology',
    'critical_thinking': 'critical-thinking',
    'business_judgment': 'business-judgment',
}

fixed = failed = 0
for fp in wiki.rglob("*.md"):
    if "_archive" in str(fp) or "raw" in str(fp): continue
    try: t = fp.read_text(encoding='utf-8')
    except: continue
    m = re.match(r'^---\s*\n(.*?)\n---\s*\n', t, re.DOTALL)
    if not m: continue
    fm_text, body = m.group(1), t[m.end():]
    try: fm = yaml.safe_load(fm_text)
    except: continue
    if not fm: continue
    d = fm.get('domain', [])
    if isinstance(d, str): d = [d]
    if not d: continue
    new_d = [MIGRATIONS.get(v, v) for v in d]
    if new_d == d: continue

    lines = fm_text.splitlines()
    new_lines, i = [], 0
    while i < len(lines):
        s = lines[i].rstrip()
        if re.match(r'^domain\s*:', s):
            new_lines.append(f'domain: {new_d[0]}' if len(new_d) == 1 else 'domain:')
            if len(new_d) > 1:
                for v in new_d: new_lines.append(f'  - {v}')
            i += 1
            while i < len(lines) and re.match(r'^\s*-\s+', lines[i]):
                i += 1
            continue
        new_lines.append(lines[i])
        i += 1

    new_text = '---\n' + '\n'.join(new_lines) + '\n---\n' + body
    m2 = re.match(r'^---\s*\n(.*?)\n---\s*\n', new_text, re.DOTALL)
    try:
        yaml.safe_load(m2.group(1))
        fp.write_text(new_text, encoding='utf-8')
        fixed += 1
    except Exception as e:
        failed += 1

print(f'Fixed: {fixed}, Failed: {failed}')

# Verify
dirty = {d: 0 for d in MIGRATIONS}
for fp in wiki.rglob("*.md"):
    if "_archive" in str(fp) or "raw" in str(fp): continue
    try:
        t = fp.read_text(encoding='utf-8', errors='replace')
        m = re.match(r'^---\s*\n(.*?)\n---\s*\n', t, re.DOTALL)
        if not m: continue
        fm = yaml.safe_load(m.group(1))
        if not fm: continue
        d = fm.get('domain', [])
        if isinstance(d, str): d = [d]
        for v in d:
            if v in MIGRATIONS: dirty[v] += 1
    except: pass
rem = sum(dirty.values())
print(f'Dirty remaining: {rem}')
for d, c in dirty.items():
    if c: print(f'  {d}: {c}')
