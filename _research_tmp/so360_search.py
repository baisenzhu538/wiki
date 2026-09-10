# -*- coding: utf-8 -*-
"""so.com (360) batch search. Usage: python so360_search.py cfg.json"""
import sys, json, time
import urllib.parse
import requests
from lxml import etree
import urllib3
urllib3.disable_warnings()

UA = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0 Safari/537.36"
S = requests.Session()
S.headers.update({'User-Agent': UA, 'Accept-Language': 'zh-CN,zh;q=0.9', 'Referer': 'https://www.so.com/'})

def so360(q, max_pages=2):
    out = []
    for page in range(1, max_pages + 1):
        url = 'https://www.so.com/s?' + urllib.parse.urlencode({'q': q, 'pn': page})
        r = S.get(url, timeout=25)
        tree = etree.HTML(r.text)
        for li in tree.xpath('//li[contains(@class,"res-list")]'):
            a = li.xpath('.//h3/a')
            if not a:
                continue
            title = ''.join(a[0].xpath('.//text()')).strip()
            link = a[0].get('href') or ''
            if not link.startswith('http'):
                continue
            snip = ' '.join(''.join(li.xpath('.//p[contains(@class,"res-desc")]/text() | .//div[contains(@class,"res-desc")]/text() | .//p[@class="res-rich"]//text() | .//span[contains(@class,"res-desc")]/text()')).split())
            data = ' '.join(''.join(li.xpath('.//p[contains(@class,"source")]/span/text() | .//p[contains(@class,"source")]//span[@class="date"]/text()')).split())
            out.append({'title': title, 'url': link, 'snippet': snip[:320], 'date': data})
    return out

def main():
    cfg = json.load(open(sys.argv[1], encoding='utf-8'))
    out = {}
    for i, q in enumerate(cfg['queries']):
        ok = False
        for attempt in range(3):
            try:
                res = so360(q)
                if not res and attempt < 2:
                    time.sleep(6*(attempt+1)); continue
                out[q] = res
                print(f"[{i+1}/{len(cfg['queries'])}] {q} -> {len(res)}", flush=True)
                ok = True; break
            except Exception as e:
                print(f"[{i+1}] {q} retry{attempt+1} err {e}", flush=True)
                time.sleep(8)
        if not ok:
            out[q] = {'error': 'failed'}
        time.sleep(2.5)
    json.dump(out, open(cfg['out'], 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
    print('saved', cfg['out'])

if __name__ == '__main__':
    main()
