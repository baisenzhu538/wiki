# -*- coding: utf-8 -*-
"""Resolve so.com /link URLs with session warmup. Reads links from cfg json, fetches pages."""
import sys, json, time, re
import requests
from lxml import etree
import urllib3
urllib3.disable_warnings()

UA = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0 Safari/537.36"
S = requests.Session()
S.headers.update({'User-Agent': UA, 'Accept-Language': 'zh-CN,zh;q=0.9', 'Referer': 'https://www.so.com/'})

def warmup():
    S.get('https://www.so.com/s', params={'q': '医药电商'}, timeout=20)

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

def resolve(link):
    r = S.get(link, timeout=25, allow_redirects=True)
    if r.url and 'so.com/link' not in r.url and r.status_code == 200:
        return r.url, r
    # parse JS/meta refresh
    m = re.search(r'window\.location\.replace\("([^"]+)"\)', r.text)
    if not m:
        m = re.search(r"window\.location\.href\s*=\s*'([^']+)'", r.text)
    if not m:
        m = re.search(r'URL=\'?([^\'">]+)\'?"?', r.text)
    if m:
        target = m.group(1)
        r2 = S.get(target, timeout=25)
        return target, r2
    return None, r

def main():
    cfg = json.load(open(sys.argv[1], encoding='utf-8'))
    out = {}
    warmup()
    for i, u in enumerate(cfg['urls']):
        try:
            real, r = resolve(u)
            if real is None:
                out[u] = {'error': 'resolve failed', 'status': r.status_code}
                print(f"[{i+1}] resolve FAILED {r.status_code}", flush=True)
            else:
                enc = r.apparent_encoding or 'utf-8'
                if enc and enc.lower() in ('gbk', 'gb2312'):
                    r.encoding = 'gb18030'
                else:
                    r.encoding = r.encoding or 'utf-8'
                out[u] = {'status': r.status_code, 'text': clean_text(r.text)[:18000], 'url': real}
                print(f"[{i+1}/{len(cfg['urls'])}] len={len(out[u]['text'])} {real[:95]}", flush=True)
        except Exception as e:
            out[u] = {'error': str(e)}
            print(f"[{i+1}] ERROR {e}", flush=True)
        time.sleep(1.5)
    json.dump(out, open(cfg['out'], 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
    print('saved', cfg['out'])

if __name__ == '__main__':
    main()
