#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""通用 MD → 飞书 Docx 发布：python tmp_publish_md.py <md_path> <doc_title>"""
import json, urllib.request, os, time, re, sys

ENV_PATH = r"C:\Users\Administrator\AppData\Local\hermes\profiles\duanwangye\.env"
MD_PATH = sys.argv[1]
DOC_TITLE = sys.argv[2]

env = {}
with open(ENV_PATH, "r", encoding="utf-8") as f:
    for line in f:
        line = line.strip()
        if line and "=" in line and not line.startswith("#"):
            k, v = line.split("=", 1)
            env[k.strip()] = v.strip()
app_id = env.get("FEISHU_APP_ID", "")
secret = env.get("FEISHU_APP_SECRET", "")

def get_token():
    url = 'https://open.feishu.cn/open-apis/auth/v3/tenant_access_token/internal'
    data = json.dumps({'app_id': app_id, 'app_secret': secret}).encode()
    req = urllib.request.Request(url, data=data, headers={'Content-Type': 'application/json'}, method='POST')
    return json.loads(urllib.request.urlopen(req, timeout=15).read())['tenant_access_token']

TOKEN = get_token()
print("Token OK")

def api(method, path, body=None, query=''):
    url = f'https://open.feishu.cn/open-apis{path}{query}'
    headers = {'Authorization': f'Bearer {TOKEN}', 'Content-Type': 'application/json'}
    data = json.dumps(body).encode() if body else None
    req = urllib.request.Request(url, data=data, headers=headers, method=method)
    return json.loads(urllib.request.urlopen(req, timeout=30).read())

def tr(content, bold=False):
    return {"text_run": {"content": content, "text_element_style": {"bold": bold}}}

def h(level, content):
    return {"block_type": 2 + level, f"heading{level}": {"elements": [tr(content)]}}

def pg(*elements):
    elems = [tr(e) if isinstance(e, str) else e for e in elements]
    return {"block_type": 2, "text": {"elements": elems}}

def bullet(content):
    return {"block_type": 12, "bullet": {"elements": [tr(content)]}}

def divider():
    return {"block_type": 22, "divider": {}}

def parse_inline(text):
    parts = []
    pos = 0
    for m in re.finditer(r'\*\*(.+?)\*\*', text):
        if m.start() > pos:
            parts.append(tr(text[pos:m.start()]))
        parts.append(tr(m.group(1), bold=True))
        pos = m.end()
    if pos < len(text):
        parts.append(tr(text[pos:]))
    return parts if parts else [tr(text)]

def md_to_blocks(md):
    blocks = []
    lines = md.split('\n')
    i = 0
    in_code = False
    code_buf = []
    while i < len(lines):
        line = lines[i]
        stripped = line.strip()
        if stripped.startswith('```'):
            if in_code:
                blocks.append({"block_type": 14, "code": {"elements": [tr('\n'.join(code_buf))], "language": 0, "wrap": True}})
                code_buf = []
                in_code = False
            else:
                in_code = True
            i += 1
            continue
        if in_code:
            code_buf.append(line)
            i += 1
            continue
        if not stripped:
            i += 1
            continue
        m = re.match(r'^(#{1,4})\s+(.+)$', line)
        if m:
            level = len(m.group(1))
            blocks.append(h(level, m.group(2).strip()))
        elif line.startswith('> '):
            blocks.append({"block_type": 15, "quote": {"elements": [tr(stripped[2:])]}})
        elif line.startswith('- '):
            content = stripped[2:]
            if content and content not in ('-', '•', '—', '———', '----'):
                blocks.append(bullet(content))
        elif stripped == '---':
            blocks.append(divider())
        elif re.match(r'^[-•]\s*[-•]', stripped):
            # 双重列表符号清理
            content = re.sub(r'^[-•]\s*[-•]\s*', '', stripped)
            blocks.append(bullet(content))
        else:
            blocks.append(pg(*parse_inline(stripped)))
        i += 1
    return blocks

def create_doc(title):
    r = api('POST', '/docx/v1/documents', {"title": title})
    if r.get('code') != 0:
        print("CREATE_FAIL:", r)
        raise SystemExit(1)
    return r['data']['document']['document_id']

def append_batch(doc_id, children, index=-1):
    r = api('POST', f'/docx/v1/documents/{doc_id}/blocks/{doc_id}/children',
            {"children": children, "index": index})
    return r

def set_public(doc_id):
    try:
        r = api('PATCH', f'/drive/v1/permissions/{doc_id}/public?type=docx',
                {"link_share_entity": "anyone_readable", "external_access": True})
        print("PERM:", r.get('code'), r.get('msg'))
    except Exception as e:
        print("PERM_ERR:", e)

with open(MD_PATH, 'r', encoding='utf-8') as f:
    md = f.read()

print("MD_CHARS:", len(md))
blocks = md_to_blocks(md)
print("BLOCKS:", len(blocks))

doc_id = create_doc(DOC_TITLE)
print("DOC_ID:", doc_id)

batch_size = 50
for i in range(0, len(blocks), batch_size):
    batch = blocks[i:i+batch_size]
    r = append_batch(doc_id, batch)
    if r.get('code') != 0:
        print(f"  BATCH {i//batch_size} FAIL: {r.get('code')} {r.get('msg')}")
        # 逐块重试
        for blk in batch:
            r2 = append_batch(doc_id, [blk])
            if r2.get('code') != 0:
                print(f"    BLOCK FAIL: {r2.get('code')} {str(blk)[:100]}")
        time.sleep(0.3)
    else:
        print(f"  BATCH {i//batch_size} OK ({len(batch)} blocks)")
    time.sleep(0.3)

set_public(doc_id)
print("DONE_URL:", f"https://yitanger.feishu.cn/docx/{doc_id}")
