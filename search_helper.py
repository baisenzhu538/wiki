# -*- coding: utf-8 -*-
"""搜索助手: 用 so.com / sogou 检索并解析结果标题+链接"""
import re
import sys
import urllib.parse
import urllib.request

UA = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) Chrome/120.0',
      'Accept': 'text/html,application/xhtml+xml',
      'Accept-Language': 'zh-CN,zh;q=0.9'}

def fetch(url):
    req = urllib.request.Request(url, headers=UA)
    return urllib.request.urlopen(req, timeout=30).read().decode('utf-8', 'ignore')

def search_so(query, out):
    q = urllib.parse.quote(query)
    html = fetch('https://www.so.com/s?q=' + q)
    open(out, 'w', encoding='utf-8').write(html)
    items = re.findall(r'<a[^>]+href="([^"]+)"[^>]*(?:data-mdurl="([^"]*)")?[^>]*>(.*?)</a>', html)
    seen = set()
    n = 0
    for url, mdurl, txt in items:
        txt = re.sub(r'<[^>]+>', '', txt)
        txt = re.sub(r'\s+', ' ', txt).strip()
        if len(txt) < 14:
            continue
        # 直接目标
        if mdurl:
            target = mdurl
        elif 'so.com/link' in url:
            target = 'REDIR:' + (url if url.startswith('http') else 'https://www.so.com' + url)
        else:
            target = url
        key = txt[:30]
        if key in seen:
            continue
        seen.add(key)
        print(txt[:85])
        print('   ', target[:200])
        n += 1
        if n >= 12:
            break

def search_sogou(query, out):
    q = urllib.parse.quote(query)
    html = fetch('https://www.sogou.com/web?query=' + q)
    open(out, 'w', encoding='utf-8').write(html)
    items = re.findall(r'<a[^>]+href="([^"]+)"[^>]*>(.*?)</a>', html)
    seen = set()
    n = 0
    for url, txt in items:
        txt = re.sub(r'<[^>]+>', '', txt)
        txt = re.sub(r'\s+', ' ', txt).strip()
        if len(txt) < 14:
            continue
        if 'sogou.com/web' in url or 'weixin' in url and 'mp.' not in url:
            continue
        target = url if url.startswith('http') else 'https://www.sogou.com' + url
        key = txt[:30]
        if key in seen:
            continue
        seen.add(key)
        print(txt[:85])
        print('   ', target[:200])
        n += 1
        if n >= 12:
            break

if __name__ == '__main__':
    engine, query, out = sys.argv[1], sys.argv[2], sys.argv[3]
    if engine == 'so':
        search_so(query, out)
    else:
        search_sogou(query, out)
