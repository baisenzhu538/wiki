# -*- coding: utf-8 -*-
"""Bing search scraper for research. Usage: python bing_search.py config.json
config: {"queries": [...], "out": "results_x.json"}
"""
import sys, json, time, base64, re
import urllib.parse
import requests
from lxml import etree

UA = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0 Safari/537.36"

def decode_bing_url(href):
    # Bing wraps results in /ck/a?...&u=a1<base64>
    m = re.search(r'[?&]u=a1([^&]+)', href)
    if m:
        b = m.group(1)
        try:
            pad = b + '=' * (-len(b) % 4)
            return base64.urlsafe_b64decode(pad).decode('utf-8', 'replace')
        except Exception:
            return href
    if href.startswith('http'):
        return href
    return 'https://cn.bing.com' + href

def bing_search(query, count=15):
    url = 'https://cn.bing.com/search?' + urllib.parse.urlencode({'q': query, 'count': count, 'setlang': 'zh-hans', 'mkt': 'zh-CN'})
    r = requests.get(url, headers={'User-Agent': UA, 'Accept-Language': 'zh-CN,zh;q=0.9'}, timeout=25)
    r.raise_for_status()
    tree = etree.HTML(r.text)
    results = []
    for li in tree.xpath('//li[@class="b_algo"]'):
        a = li.xpath('.//h2/a')
        if not a:
            continue
        a = a[0]
        title = ''.join(a.xpath('.//text()')).strip()
        href = a.get('href') or ''
        link = decode_bing_url(href)
        snips = li.xpath('.//div[contains(@class,"b_caption")]//p//text() | .//p[@class="b_lineclamp4 b_algoSlug"]//text() | .//p[contains(@class,"b_algoSlug")]//text()')
        snippet = ' '.join(s.strip() for s in snips if s.strip())[:400]
        # capture date hint if present
        span = li.xpath('.//span[contains(@class,"news_dt")]/text()')
        date = span[0].strip() if span else ''
        if title and link:
            results.append({'title': title, 'url': link, 'snippet': snippet, 'date': date})
    return results

def main():
    cfg = json.load(open(sys.argv[1], encoding='utf-8'))
    out = {}
    for i, q in enumerate(cfg['queries']):
        try:
            res = bing_search(q)
            out[q] = res
            print(f"[{i+1}/{len(cfg['queries'])}] {q} -> {len(res)} results", flush=True)
        except Exception as e:
            out[q] = {'error': str(e)}
            print(f"[{i+1}] {q} -> ERROR {e}", flush=True)
        time.sleep(1.5)
    json.dump(out, open(cfg['out'], 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
    print("saved", cfg['out'])

if __name__ == '__main__':
    main()
