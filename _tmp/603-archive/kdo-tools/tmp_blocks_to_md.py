#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""通用 blocks JSON → Markdown 逐字稿转换：python tmp_blocks_to_md.py <json_path> <md_out> <title>"""
import json, re, sys

SRC = sys.argv[1]
OUT = sys.argv[2]
DOC_TITLE = sys.argv[3]

with open(SRC, 'r', encoding='utf-8') as f:
    data = json.load(f)
blocks = data['allBlocks']

def clean(text):
    t = text.replace('\u200b', '').strip()
    t = re.sub(r'\s+', ' ', t)
    return t

md_lines = [DOC_TITLE, '', '> 一堂课程逐字稿 | 提取时间：2026-09-01', '', '---', '']
seen_exact = set()

for b in blocks:
    t = clean(b['text'])
    if not t:
        continue
    ctype = b['type']
    if ctype.startswith('heading'):
        lv = int(ctype.replace('heading', ''))
        md_lines.append('#' * lv + ' ' + t)
        md_lines.append('')
        seen_exact.add(t)
    elif ctype == 'bullet':
        line = t if re.match(r'^[-•]\s', t) else '- ' + t
        if line.strip() in ('-', '•', '—', '———', '----'):
            continue
        if t in seen_exact:
            continue
        seen_exact.add(t)
        md_lines.append(line)
    elif ctype == 'ordered':
        line = t if re.match(r'^\d+[\.、]', t) else '1. ' + t
        if t in seen_exact:
            continue
        seen_exact.add(t)
        md_lines.append(line)
    elif ctype == 'callout':
        if t in seen_exact:
            continue
        seen_exact.add(t)
        md_lines.append('> ' + t); md_lines.append('')
    elif ctype == 'grid':
        if t in seen_exact:
            continue
        seen_exact.add(t)
        md_lines.append(t); md_lines.append('')
    elif ctype == 'image':
        md_lines.append('_[图片]_'); md_lines.append('')
    else:
        if t in ('-', '—', '———', '——', '----'):
            md_lines.append('---'); md_lines.append('')
            continue
        if t in seen_exact:
            continue
        seen_exact.add(t)
        md_lines.append(t); md_lines.append('')

md = '\n'.join(md_lines)
md = re.sub(r'\n{3,}', '\n\n', md)
md = re.sub(r'^[-•]\s*[-•]\s*', '- ', md, flags=re.M)
lines = md.split('\n')
md = '\n'.join(l for l in lines if not (re.search(r'1\.\s.*\s2\.\s', l) and len(l) > 100))
md = re.sub(r'[ \t]+$', '', md, flags=re.M)

with open(OUT, 'w', encoding='utf-8') as f:
    f.write(md)
print(f'MD_SAVED: {OUT}')
print(f'MD_CHARS: {len(md)}  MD_LINES: {len(md.splitlines())}')
