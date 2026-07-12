#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""#161 域外桥接指标复测：域外出链占比 / 零域外出链卡数 / 零域外入链卡数"""
import os, re, sys, io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

ROOT = r'C:/Users/Administrator/Desktop/wiki'
WIKI = os.path.join(ROOT, '30_wiki')
SPEC = os.path.join(ROOT, '.agent/prompts/agent-一堂-业务公式教练.md')

def read(p):
    with open(p, 'r', encoding='utf-8', errors='replace') as f:
        return f.read()

def parse_fm(txt):
    m = re.match(r'^---\n(.*?)\n---', txt, re.S)
    return m.group(1) if m else ''

def get_domain(fm):
    m = re.search(r'^domain:\s*\n((?:\s*-\s+.*\n)+)', fm, re.M)
    if m:
        return ' '.join(x.strip().lstrip('-').strip() for x in m.group(1).splitlines())
    m = re.search(r'^domain:\s*(.*)$', fm, re.M)
    return m.group(1).strip().strip('"\'') if m else ''

def get_related(fm):
    m = re.search(r'^related:\s*\n((?:\s*-\s+.*\n)+)', fm, re.M)
    if not m:
        m2 = re.search(r'^related:\s*\[(.*?)\]', fm, re.S)
        if m2:
            return [x.strip().strip('[]"\'') for x in m2.group(1).split(',') if x.strip()]
        return []
    ids = []
    for line in m.group(1).splitlines():
        s = line.strip().lstrip('-').strip()
        s = s.strip('[]').strip('"\'')
        s = re.sub(r'\[\[(.*?)\]\]', r'\1', s)
        if s:
            ids.append(s)
    return ids

# build card index: id -> (path, domain)
cards = {}
for dp, _, fns in os.walk(WIKI):
    for fn in fns:
        if not fn.endswith('.md'):
            continue
        p = os.path.join(dp, fn)
        txt = read(p)
        fm = parse_fm(txt)
        cid = fn[:-3]
        cards[cid] = (p, get_domain(fm), get_related(fm))

def is_bf(domain):
    return 'business-formula' in domain

# C-domain set: cards whose domain contains business-formula + spec
cset = {cid for cid, (p, d, r) in cards.items() if is_bf(d)}
cset.add('agent-一堂-业务公式教练')

# spec related
spec_txt = read(SPEC)
spec_fm = parse_fm(spec_txt)
spec_related = get_related(spec_fm)

out_total = 0
out_cross = 0
zero_out = []   # cards with zero cross-domain outbound
inbound_cross = {cid: 0 for cid in cset}

def resolve(tid):
    tid = tid.split('#')[0].split('|')[0].strip()
    return tid

for cid in cset:
    if cid == 'agent-一堂-业务公式教练':
        rel = spec_related
    else:
        rel = cards[cid][2]
    cross = 0
    for t in rel:
        t = resolve(t)
        if not t:
            continue
        out_total += 1
        tdom = cards[t][1] if t in cards else None
        # out-of-domain if target not in cset (or unknown id -> count as cross? unknown treated cross)
        if t not in cset:
            cross += 1
            if t in cards:
                inbound_cross.setdefault(t, 0)
        else:
            pass
    out_cross += cross
    if cross == 0:
        zero_out.append(cid)

# inbound cross: for every card outside cset, count links into cset
for cid, (p, d, rel) in cards.items():
    if cid in cset:
        continue
    for t in rel:
        t = resolve(t)
        if t in cset:
            inbound_cross[t] = inbound_cross.get(t, 0) + 1

zero_in = [cid for cid in cset if inbound_cross.get(cid, 0) == 0]

print(f"C域卡数(含spec): {len(cset)}")
print(f"出链总数: {out_total}")
print(f"域外出链: {out_cross}")
print(f"域外占比: {out_cross/out_total*100:.1f}%")
print(f"零域外出链卡: {len(zero_out)} -> {sorted(zero_out)}")
print(f"零域外入链卡: {len(zero_in)} -> {sorted(zero_in)}")
