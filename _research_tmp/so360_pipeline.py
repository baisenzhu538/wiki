# -*- coding: utf-8 -*-
"""so.com search + in-session resolve + fetch pages, one pipeline.
cfg: {"tasks": [{"q": "...", "fetch": ["kw1","kw2"], "max": 2}], "out": "out.json"}
"""
import sys, json, time, re
import urllib.parse
import requests
from lxml import etree
import urllib3
urllib3.disable_warnings()

UA = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0 Safari/537.36"
S = requests.Session()
S.headers.update({'User-Agent': UA, 'Accept-Language': 'zh-CN,zh;q=0.9', 'Referer': 'https://www.so.com/'})

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

def search(q):
    url = 'https://www.so.com/s?' + urllib.parse.urlencode({'q': q, 'pn': 1})
    r = S.get(url, timeout=25)
    tree = etree.HTML(r.text)
    out = []
    for li in tree.xpath('//li[contains(@class,"res-list")]'):
        a = li.xpath('.//h3/a')
        if not a:
            continue
        title = ''.join(a[0].xpath('.//text()')).strip()
        link = a[0].get('href') or ''
        snip = ' '.join(''.join(li.xpath('.//p[contains(@class,"res-desc")]/text() | .//div[contains(@class,"res-desc")]/text() | .//span[contains(@class,"res-desc")]/text()')).split())
        out.append({'title': title, 'link': link, 'snippet': snip[:350]})
    return out

def resolve_fetch(link):
    r = S.get(link, timeout=25, allow_redirects=True)
    real = r.url
    if 'so.com/link' in real:
        m = re.search(r'window\.location\.replace\("([^"]+)"\)', r.text)
        if not m:
            m = re.search(r"window\.location\.href\s*=\s*'([^']+)'", r.text)
        if not m:
            m = re.search(r'URL=\'?([^\'">]+)\'?"?', r.text)
        if m:
            real = m.group(1)
            r = S.get(real, timeout=25)
    enc = r.apparent_encoding or 'utf-8'
    if enc and enc.lower() in ('gbk', 'gb2312'):
        r.encoding = 'gb18030'
    else:
        r.encoding = r.encoding or 'utf-8'
    return real, clean_text(r.text)[:16000]

def main():
    cfg = json.load(open(sys.argv[1], encoding='utf-8'))
    out = {'search': {}, 'pages': {}}
    for i, task in enumerate(cfg['tasks']):
        q = task['q']
        try:
            res = search(q)
            out['search'][q] = res
            print(f"[{i+1}/{len(cfg['tasks'])}] {q} -> {len(res)}", flush=True)
            kws = task.get('fetch', [])
            fetched = 0
            for item in res:
                if fetched >= task.get('max', 2):
                    break
                if kws and not any(k in item['title'] for k in kws):
                    continue
                try:
                    real, text = resolve_fetch(item['link'])
                    out['pages'][real] = text
                    print(f"    FETCH len={len(text)} {real[:90]}", flush=True)
                    fetched += 1
                    time.sleep(1.5)
                except Exception as e:
                    print(f"    fetch err {e}", flush=True)
        except Exception as e:
            out['search'][q] = {'error': str(e)}
            print(f"[{i+1}] {q} ERROR {e}", flush=True)
        time.sleep(2.5)
    json.dump(out, open(cfg['out'], 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
    print('saved', cfg['out'])

if __name__ == '__main__':
    main()
