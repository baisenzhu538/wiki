# -*- coding: utf-8 -*-
"""一体化: so搜索 -> 解析重定向 -> 抓正文存txt"""
import re
import sys
import time
import urllib.parse
import urllib.request

UA = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) Chrome/120.0',
      'Accept-Language': 'zh-CN,zh;q=0.9'}

def fetch(url, referer=None):
    h = dict(UA)
    if referer:
        h['Referer'] = referer
    req = urllib.request.Request(url, headers=h)
    return urllib.request.urlopen(req, timeout=30).read().decode('utf-8', 'ignore')

def resolve_so(url):
    html = fetch(url, referer='https://www.so.com/')
    for p in [r'window\.location\.(?:replace|href)\s*=\s*["\']([^"\']+)["\']',
              r'URL=\'?([^\'">]+)',
              r'(https?://[^\s"\'<>]+)']:
        m = re.search(p, html)
        if m:
            return m.group(1)
    return None

def search(query, top=6):
    q = urllib.parse.quote(query)
    html = fetch('https://www.so.com/s?q=' + q)
    items = re.findall(r'<h3[^>]*>\s*<a[^>]+href="([^"]+)"[^>]*>(.*?)</a>', html)
    out, seen = [], set()
    for url, txt in items:
        txt = re.sub(r'\s+', ' ', re.sub(r'<[^>]+>', '', txt)).strip()
        if len(txt) < 14 or url in seen:
            continue
        seen.add(url)
        real = url
        if 'so.com/link' in url:
            full = url if url.startswith('http') else 'https://www.so.com' + url
            try:
                real = resolve_so(full) or full
            except Exception as e:
                real = 'RESOLVE_ERR:%s' % e
            time.sleep(2)
        out.append((txt, real))
        if len(out) >= top:
            break
    return out

def save_page(url, name):
    try:
        html = fetch(url)
        open(name + '.html', 'w', encoding='utf-8').write(html)
        t = re.sub(r'<script[\s\S]*?</script>|<style[\s\S]*?</style>', ' ', html)
        t = re.sub(r'<[^>]+>', ' ', t)
        t = re.sub(r'[ \t\r]+', ' ', t)
        t = re.sub(r'\n\s*\n+', '\n', t)
        open(name + '.txt', 'w', encoding='utf-8').write(t)
        return '%s saved %d chars' % (name, len(t))
    except Exception as e:
        return '%s FAILED %s' % (name, e)

if __name__ == '__main__':
    query = sys.argv[1]
    for txt, url in search(query):
        print(txt[:90])
        print('   ', url[:150])
