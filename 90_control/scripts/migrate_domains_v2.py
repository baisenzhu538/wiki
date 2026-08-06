#!/usr/bin/env python3
"""#239 — second batch domain cleanup: spaces, dedup, lowercase, underscores"""
import re, yaml
from pathlib import Path

root = Path(r'C:\Users\Administrator\Desktop\wiki')
wiki = root / '30_wiki'

# Known valid domains (from #237 scan, kebab-case English)
VALID_DOMAINS = {
    'yitang', 'ai-collaboration', 'research', 'design', 'strategy', 'decision-science',
    'master', 'business-strategy', 'management', 'ai-saas', 'product', 'business-formula',
    'kdo', 'conversion-rate', 'five-step-method', 'modeling', 'personal-os',
    'decision-making', 'healthcare', 'personal-growth', 'panproduct', 'entrepreneurship',
    'innovation', 'demand-analysis', 'growth', 'sales', 'content-production',
    'learning-methodology', 'critical-thinking', 'business-judgment', 'finance-legal',
    'marketing', 'saas', 'human-ai-collaboration', 'competitive-analysis',
    'problem-solving', 'business-design', 'market-positioning', 'video-production',
    'reading-methodology',
}

def fix_value(v):
    """Fix one domain value. Returns (new_value, changed)."""
    orig = v

    # 1. Strip spaces around hyphens
    v = re.sub(r'\s*-\s*', '-', v)
    v = v.strip()

    # 2. Lowercase (but preserve Chinese)
    if not re.search(r'[\u4e00-\u9fff]', v):
        v = v.lower()

    # 3. Replace underscores with hyphens
    v = v.replace('_', '-')

    # 4. Remove semicolons (treat as separator → keep first valid part)
    if ';' in v:
        parts = [p.strip() for p in v.split(';')]
        v = parts[0]  # Keep first

    # 5. Deduplicate repeated segments (e.g. healthcare-healthcare -> healthcare)
    parts = v.split('-')
    if len(parts) >= 2 and len(parts) % 2 == 0:
        mid = len(parts) // 2
        if parts[:mid] == parts[mid:]:
            v = '-'.join(parts[:mid])

    # 6. For Chinese values, leave as-is
    if re.search(r'[\u4e00-\u9fff]', v):
        return v, False  # Don't touch Chinese

    # 7. Remove leading/trailing hyphens
    v = v.strip('-')

    return v, (v != orig)


fixed = 0
skipped_chinese = []

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

    new_d = []
    changed = False
    for v in d:
        nv, ch = fix_value(v)
        new_d.append(nv)
        if ch: changed = True

    if not changed: continue

    # Track Chinese values
    for v in new_d:
        if re.search(r'[\u4e00-\u9fff]', v) and v != 'src_unknown':
            skipped_chinese.append((fp.name, v))

    # Rebuild frontmatter
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
        print(f'FAIL: {fp.name}: {e}')

print(f'Fixed: {fixed}')
if skipped_chinese:
    print(f'\nChinese values left as-is ({len(set(v for _,v in skipped_chinese))} unique):')
    for v in sorted(set(v for _,v in skipped_chinese)):
        count = sum(1 for _,x in skipped_chinese if x == v)
        print(f'  {v}: {count}')

# Final scan
from collections import Counter
remaining = Counter()
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
            if v and v != 'src_unknown':
                is_std = re.match(r'^[a-z][a-z0-9-]*$', v) and ' ' not in v and '_' not in v and v == v.lower()
                if not is_std:
                    remaining[v] += 1
    except: pass
print(f'\nNon-standard remaining: {sum(remaining.values())}')
for v, c in remaining.most_common(10):
    print(f'  {v}: {c}')
