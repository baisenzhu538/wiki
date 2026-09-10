# -*- coding: utf-8 -*-
"""Multi-engine search test: baidu / bing-global / sogou."""
import sys, json, time, re, base64
import urllib.parse
import requests
from lxml import etree

UA = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0 Safari/537.36"

def baidu(q):
    url = 'https://www.baidu.com/s?' + urllib.parse.urlencode({'wd': q, 'rn': 15})
    r = requests.get(url, headers={'User-Agent': UA, 'Accept-Language': 'zh-CN,zh;q=0.9'}, timeout=25)
    tree = etree.HTML(r.text)
    out = []
    for div in tree.xpath('//div[contains(@class,"result") and contains(@class,"c-container")]'):
        a = div.xpath('.//h3/a')
        if not a: continue
        title = ''.join(a[0].xpath('.//text()')).strip()
        link = a[0].get('href') or ''
        snip = ''.join(div.xpath('.//span[contains(@class,"content-right")]/text() | .//div[contains(@class,"c-abstract")]/text() | .//div[contains(@class,"c-span-last")]//text()'))
        out.append({'title': title, 'url': link, 'snippet': snip.strip()[:300]})
    return out

def bing_global(q):
    url = 'https://www.bing.com/search?' + urllib.parse.urlencode({'q': q, 'count': 15})
    r = requests.get(url, headers={'User-Agent': UA, 'Accept-Language': 'zh-CN,zh;q=0.9'}, timeout=25)
    tree = etree.HTML(r.text)
    out = []
    for li in tree.xpath('//li[@class="b_algo"]'):
        a = li.xpath('.//h2/a')
        if not a: continue
        title = ''.join(a[0].xpath('.//text()')).strip()
        href = a[0].get('href') or ''
        m = re.search(r'[?&]u=a1([^&]+)', href)
        link = href
        if m:
            try:
                b = m.group(1); b += '=' * (-len(b) % 4)
                link = base64.urlsafe_b64decode(b).decode('utf-8', 'replace')
            except Exception: pass
        snip = ' '.join(li.xpath('.//div[contains(@class,"b_caption")]//p//text() | .//p[contains(@class,"b_algoSlug")]//text()'))
        out.append({'title': title, 'url': link, 'snippet': ' '.join(snip.split())[:300]})
    return out

def sogou(q):
    url = 'https://www.sogou.com/web?' + urllib.parse.urlencode({'query': q})
    r = requests.get(url, headers={'User-Agent': UA}, timeout=25)
    tree = etree.HTML(r.text)
    out = []
    for div in tree.xpath('//div[contains(@class,"vrwrap")] | //div[contains(@class,"rb")]'):
        a = div.xpath('.//h3/a')
        if not a: continue
        title = ''.join(a[0].xpath('.//text()')).strip()
        link = a[0].get('href') or ''
        if link.startswith('/'): link = 'https://www.sogou.com' + link
        snip = ''.join(div.xpath('.//div[contains(@class,"str_info")]/text() | .//p[contains(@class,"str-text-info")]/text() | .//div[contains(@class,"ft")]//text()'))
        out.append({'title': title, 'url': link, 'snippet': snip.strip()[:300]})
    return out

q = sys.argv[1]
for name, fn in [('BAIDU', baidu), ('BING_GLOBAL', bing_global), ('SOGOU', sogou)]:
    print('#'*70)
    print(name, '->', q)
    try:
        res = fn(q)
        for it in res[:8]:
            print('-', it['title'][:60], '|', it['url'][:90])
            print('  ', it['snippet'][:130])
    except Exception as e:
        print('ERROR', e)
    time.sleep(1)
