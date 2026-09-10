# -*- coding: utf-8 -*-
"""解析 so.com/sogou 跳转链接,拿到真实目标URL"""
import re
import sys
import urllib.request

UA = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) Chrome/120.0'}

def resolve(url):
    try:
        req = urllib.request.Request(url, headers=UA)
        html = urllib.request.urlopen(req, timeout=20).read().decode('utf-8', 'ignore')
        # so.com: URLDecoder('m=...') params; look for window.location.replace / href
        m = re.search(r"window\.location\.(?:replace|href)\s*=\s*[\"']([^\"']+)[\"']", html)
        if m:
            return m.group(1)
        m = re.search(r'URL=\'?([^\'">]+)', html)
        if m:
            return m.group(1)
        m = re.search(r'http[s]?://(?:www\.)?(?:gov\.cn|nmpa\.gov\.cn|samr\.gov\.cn|nhc\.gov\.cn|nhsa\.gov\.cn)[^\s"\'<>]*', html)
        if m:
            return m.group(0)
        return 'NO_TARGET_FOUND len=%d' % len(html)
    except Exception as e:
        return 'ERR %s' % e

for u in sys.argv[1:]:
    print(u[:80])
    print('  ->', resolve(u))
