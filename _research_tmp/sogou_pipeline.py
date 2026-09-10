# -*- coding: utf-8 -*-
"""Sogou mobile-UA search + in-session resolve + fetch. Same cfg format as so360_pipeline."""
import sys, json, time, re
import urllib.parse
import requests
from lxml import etree
import urllib3
urllib3.disable_warnings()

MOB_UA = "Mozilla/5.0 (iPhone; CPU iPhone OS 17_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.0 Mobile/15E148 Safari/604.1"
S = requests.Session()
S.headers.update({'User-Agent': MOB_UA, 'Accept-Language': 'zh-CN,zh;q=0.9'})

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
    url = 'https://www.sogou.com/web?' + urllib.parse.urlencode({'query': q})
    r = S.get(url, timeout=25)
    tree = etree.HTML(r.text)
    out = []
    for div in tree.xpath('//div[contains(@class,"vrwrap")] | //div[contains(@class,"rb")]'):
        a = div.xpath('.//h3/a')
        if not a:
            continue
        title = ''.join(a[0].xpath('.//text()')).strip()
        link = a[0].get('href') or ''
        if link.startswith('/'):
            link = 'https://www.sogou.com' + link
        snip = ' '.join(''.join(div.xpath('.//p//text() | .//div[contains(@class,"str_info")]/text() | .//div[contains(@class,"text-layout")]//text()')).split())
        out.append({'title': title, 'link': link, 'snippet': snip[:350]})
    return out

def resolve_fetch(link):
    r = S.get(link, timeout=25, allow_redirects=True)
    real = r.url
    if 'sogou.com/link' in real:
        m = re.search(r'window\.location\.replace\("([^"]+)"\)', r.text)
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
                if fetched >= task.get('max', 1):
                    break
                if kws and not any(k in item['title'] for k in kws):
                    continue
                try:
                    real, text = resolve_fetch(item['link'])
                    out['pages'][real] = text
                    print(f"    FETCH len={len(text)} {real[:90]}", flush=True)
                    fetched += 1
                    time.sleep(2)
                except Exception as e:
                    print(f"    fetch err {e}", flush=True)
        except Exception as e:
            out['search'][q] = {'error': str(e)}
            print(f"[{i+1}] {q} ERROR {e}", flush=True)
        time.sleep(4)
    json.dump(out, open(cfg['out'], 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
    print('saved', cfg['out'])

if __name__ == '__main__':
    main()
