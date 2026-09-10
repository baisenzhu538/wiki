# -*- coding: utf-8 -*-
"""解析搜索结果HTML,提取标题+链接"""
import re
import sys

def clean(txt):
    txt = re.sub(r'<[^>]+>', '', txt)
    return re.sub(r'\s+', ' ', txt).strip()

def parse(f, keywords):
    print('=' * 20, f)
    try:
        html = open(f, encoding='utf-8', errors='ignore').read()
    except Exception as e:
        print('ERR', e)
        return
    items = re.findall(r'<a[^>]+href="([^"]+)"[^>]*>(.*?)</a>', html)
    seen = set()
    n = 0
    for url, txt in items:
        txt = clean(txt)
        if len(txt) > 12 and any(k in txt for k in keywords):
            key = txt[:40]
            if key in seen:
                continue
            seen.add(key)
            print(txt[:90], '||', url[:150])
            n += 1
            if n > 25:
                break

if __name__ == '__main__':
    kws = ['药品', '药监局', '监管', '平台', '处方', '医保', '网售']
    for f in sys.argv[1:]:
        parse(f, kws)
