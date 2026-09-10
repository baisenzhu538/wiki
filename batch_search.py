# -*- coding: utf-8 -*-
"""多主题搜索(so.com,带延时)+解析"""
import re
import sys
import time
import urllib.parse
import urllib.request

UA = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) Chrome/120.0',
      'Accept': 'text/html,application/xhtml+xml',
      'Accept-Language': 'zh-CN,zh;q=0.9',
      'Referer': 'https://www.so.com/'}

def fetch(url):
    req = urllib.request.Request(url, headers=UA)
    return urllib.request.urlopen(req, timeout=30).read().decode('utf-8', 'ignore')

def clean(t):
    t = re.sub(r'<[^>]+>', '', t)
    return re.sub(r'\s+', ' ', t).strip()

def search_so(query):
    q = urllib.parse.quote(query)
    html = fetch('https://www.so.com/s?q=' + q)
    items = re.findall(r'<h3[^>]*>\s*<a[^>]+href="([^"]+)"[^>]*(?:data-mdurl="([^"]*)")?[^>]*>(.*?)</a>', html)
    if not items:
        items = re.findall(r'<a[^>]+href="([^"]+)"[^>]*(?:data-mdurl="([^"]*)")?[^>]*>(.*?)</a>', html)
    seen = set()
    n = 0
    for url, mdurl, txt in items:
        txt = clean(txt)
        if len(txt) < 14:
            continue
        if mdurl:
            target = mdurl
        elif 'so.com/link' in url:
            target = 'REDIR:' + (url if url.startswith('http') else 'https://www.so.com' + url)
        else:
            target = url
        key = txt[:25]
        if key in seen:
            continue
        seen.add(key)
        print(txt[:90])
        print('   ', target[:180])
        n += 1
        if n >= 8:
            break
    if n == 0:
        print('(no results / captcha) len=%d' % len(html))

queries = [
    '药品管理法实施条例 2026 修订 第三方平台 备案',
    '美团买药 平台 处罚 药品监管 罚款',
    '饿了么 送药 违规 处罚 药监局',
    '医保个人账户 线上支付 互联网 定点零售药店',
    '国家医保局 互联网医疗 医保在线支付 政策 2025',
    '药品网络销售 专项整治 2025 药监局 通知',
]
only = sys.argv[1] if len(sys.argv) > 1 else None
for qq in queries:
    if only and only not in qq:
        continue
    print('\n########', qq)
    try:
        search_so(qq)
    except Exception as e:
        print('ERR', e)
    time.sleep(6)
