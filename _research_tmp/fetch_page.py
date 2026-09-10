# -*- coding: utf-8 -*-
"""Fetch article text, resolving sogou /link redirects. Usage: python fetch_page.py cfg.json"""
import sys, json, time, re
import requests
from lxml import etree
import urllib3
urllib3.disable_warnings()

UA = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0 Safari/537.36"
SESSION = requests.Session()
SESSION.headers.update({'User-Agent': UA, 'Accept-Language': 'zh-CN,zh;q=0.9'})

def clean_text(html):
    tree = etree.HTML(html)
    if tree is None:
        return ''
    for tag in tree.xpath('//script|//style|//noscript|//iframe'):
        p = tag.getparent()
        if p is not None:
            p.remove(tag)
    text = tree.xpath('string(//body)')
    text = re.sub(r'[ \t\r\xa0]+', ' ', text)
    text = re.sub(r'\n\s*\n+', '\n', text)
    return text.strip()

def resolve_sogou(url):
    r = SESSION.get(url, timeout=25, verify=False)
    html = r.text
    # JS redirect
    m = re.search(r'window\.location\.replace\("([^"]+)"\)', html)
    if not m:
        m = re.search(r'URL=\'?([^\'">]+)\'?"?\s*/?>', html)  # meta refresh
    if m:
        return m.group(1)
    return None

def fetch(url):
    real = url
    if 'sogou.com/link' in url:
        target = resolve_sogou(url)
        if target:
            real = target
        else:
            return {'status': 0, 'text': '[SOGOU_REDIRECT_FAILED]', 'url': url}
    r = SESSION.get(real, timeout=25, verify=False)
    enc = r.apparent_encoding or 'utf-8'
    if enc and enc.lower() in ('gbk', 'gb2312'):
        r.encoding = 'gb18030'
    else:
        r.encoding = r.encoding or 'utf-8'
    return {'status': r.status_code, 'text': clean_text(r.text)[:18000], 'url': real}

def main():
    cfg = json.load(open(sys.argv[1], encoding='utf-8'))
    out = {}
    for i, u in enumerate(cfg['urls']):
        try:
            res = fetch(u)
            out[u] = res
            real = res.get('url', u)
            print(f"[{i+1}/{len(cfg['urls'])}] len={len(res['text'])} {real[:90]}", flush=True)
        except Exception as e:
            out[u] = {'error': str(e)}
            print(f"[{i+1}] {u[:60]} -> ERROR {e}", flush=True)
        time.sleep(2)
    json.dump(out, open(cfg['out'], 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
    print('saved', cfg['out'])

if __name__ == '__main__':
    main()
