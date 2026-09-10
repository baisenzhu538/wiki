# -*- coding: utf-8 -*-
"""Refetch specific pages with forced encoding."""
import re, json, time
import requests
from lxml import etree
import urllib3
urllib3.disable_warnings()

UA = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0 Safari/537.36"
S = requests.Session()
S.headers.update({'User-Agent': UA, 'Accept-Language': 'zh-CN,zh;q=0.9'})

def clean(html):
    tree = etree.HTML(html)
    if tree is None: return ''
    for tag in tree.xpath('//script|//style|//noscript|//iframe'):
        p = tag.getparent()
        if p is not None: p.remove(tag)
    t = tree.xpath('string(//body)')
    t = re.sub(r'[ \t\r\xa0]+', ' ', t)
    t = re.sub(r'\n\s*\n+', '\n', t)
    return t.strip()

targets = [
    ('http://business.sohu.com/20120420/n341080130.shtml', 'gb18030'),
    ('https://www.xianjichina.com/news/details_55202.html', 'utf-8'),
]
out = {}
for url, enc in targets:
    try:
        r = S.get(url, timeout=25)
        r.encoding = enc
        out[url] = clean(r.text)[:15000]
        print(url, '->', len(out[url]), flush=True)
    except Exception as e:
        print(url, 'ERR', e, flush=True)
    time.sleep(1.5)
json.dump(out, open('p3_refetch.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print('saved p3_refetch.json')
