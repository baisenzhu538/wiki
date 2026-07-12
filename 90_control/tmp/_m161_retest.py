#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""#161 域外桥接指标复测（终版）：域外出链占比 / 零域外出链卡数 / 零域外入链卡数
口径：frontmatter domain 含 business-formula 的卡 + .agent/prompts/agent-一堂-业务公式教练.md spec = 50 卡集
用法：cd wiki && python 90_control/tmp/_m161_retest.py
"""
import os, re, sys, io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

WIKI = '30_wiki'
SPEC = '.agent/prompts/agent-一堂-业务公式教练.md'
SPECID = 'agent-一堂-业务公式教练'

def read(p):
    with open(p, 'r', encoding='utf-8', errors='replace') as f:
        return f.read()

def fm_of(t):
    m = re.match(r'^---\n(.*?)\n---', t, re.S)
    return m.group(1) if m else ''

def list_field(fm, key):
    # YAML 列表：首项可与 key 同行（related: - '[[x]]'），列表项零缩进或缩进均可
    m = re.search(rf'^{key}:[ \t]*(.*(?:\n[ \t]*-[ \t].*)*)', fm, re.M)
    if not m:
        return []
    first = m.group(1).splitlines()[0].strip()
    if first.startswith('['):  # flow style [a, b]
        return [x.strip().strip('"\'') for x in first.strip('[]').split(',') if x.strip()]
    items = []
    for line in m.group(1).splitlines():
        s = line.strip()
        if not s.startswith('-'):
            continue
        s = s[1:].strip().strip('"\'')
        mm = re.search(r'\[\[(.*?)\]\]', s)
        if mm:
            s = mm.group(1)
        s = s.split('|')[0].split('#')[0].strip()
        if s:
            items.append(s)
    return items

def domain_of(fm):
    d = list_field(fm, 'domain')
    if d:
        return ' '.join(d)
    m = re.search(r'^domain:\s*(\S.*)$', fm, re.M)
    return m.group(1).strip() if m else ''

cards = {}
for dp, _, fns in os.walk(WIKI):
    for fn in fns:
        if fn.endswith('.md'):
            p = os.path.join(dp, fn)
            fm = fm_of(read(p))
            cards[fn[:-3]] = (domain_of(fm), list_field(fm, 'related'))

cset = {c for c, (d, r) in cards.items() if 'business-formula' in d}
cset.add(SPECID)
spec_rel = list_field(fm_of(read(SPEC)), 'related')

out_total = out_cross = 0
zero_out = []
for c in cset:
    rel = spec_rel if c == SPECID else cards[c][1]
    cr = sum(1 for t in rel if t not in cset)
    out_total += len(rel)
    out_cross += cr
    if cr == 0:
        zero_out.append(c)

inb = {c: 0 for c in cset}
for c, (d, rels) in cards.items():
    if c in cset:
        continue
    for t in rels:
        if t in cset:
            inb[t] += 1
zero_in = [c for c in cset if inb[c] == 0]

print(f"C域卡数(含spec): {len(cset)}")
print(f"出链总数: {out_total}")
print(f"域外出链: {out_cross}")
print(f"域外占比: {out_cross/out_total*100:.1f}%")
print(f"零域外出链卡: {len(zero_out)} {sorted(zero_out)}")
print(f"零域外入链卡: {len(zero_in)} {sorted(zero_in)}")
