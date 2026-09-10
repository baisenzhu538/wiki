# -*- coding: utf-8 -*-
"""Sogou batch search v2 with session, antispider backoff. Usage: python sogou_search.py cfg.json"""
import sys, json, time
import urllib.parse
import requests
from lxml import etree

UA = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0 Safari/537.36"
S = requests.Session()
S.headers.update({'User-Agent': UA, 'Accept-Language': 'zh-CN,zh;q=0.9', 'Referer': 'https://www.sogou.com/'})

def sogou(q):
    url = 'https://www.sogou.com/web?' + urllib.parse.urlencode({'query': q})
    r = S.get(url, timeout=25, verify=False)
    tree = etree.HTML(r.text)
    if tree is None or tree.xpath('//title[contains(text(),"验证")]|//*[@id="seccodeImage"]'):
        raise RuntimeError('antispider')
    out = []
    for div in tree.xpath('//div[contains(@class,"vrwrap")] | //div[contains(@class,"rb")]'):
        a = div.xpath('.//h3/a')
        if not a:
            continue
        title = ''.join(a[0].xpath('.//text()')).strip()
        link = a[0].get('href') or ''
        if link.startswith('/'):
            link = 'https://www.sogou.com' + link
        snip = ''.join(div.xpath('.//div[contains(@class,"str_info")]/text() | .//p[contains(@class,"str-text-info")]/text() | .//div[contains(@class,"text-layout")]//text() | .//div[contains(@class,"ft")]//text()'))
        out.append({'title': title, 'url': link, 'snippet': snip.strip()[:300]})
    return out

def main():
    cfg = json.load(open(sys.argv[1], encoding='utf-8'))
    out = {}
    for i, q in enumerate(cfg['queries']):
        ok = False
        for attempt in range(4):
            try:
                res = sogou(q)
                if not res and attempt < 3:
                    print(f"[{i+1}] {q} empty, backoff {8*(attempt+1)}s", flush=True)
                    time.sleep(8*(attempt+1))
                    continue
                out[q] = res
                print(f"[{i+1}/{len(cfg['queries'])}] {q} -> {len(res)}", flush=True)
                ok = True
                break
            except Exception as e:
                print(f"[{i+1}] {q} retry {attempt+1} err {e}", flush=True)
                time.sleep(10*(attempt+1))
        if not ok:
            out[q] = {'error': 'failed'}
        time.sleep(3)
    json.dump(out, open(cfg['out'], 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
    print('saved', cfg['out'])

if __name__ == '__main__':
    main()
