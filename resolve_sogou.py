# -*- coding: utf-8 -*-
"""解析 sogou 跳转链接 -> 真实URL"""
import re
import sys
import urllib.request

UA = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) Chrome/120.0',
      'Referer': 'https://www.sogou.com/'}

def resolve(url):
    try:
        req = urllib.request.Request(url, headers=UA)
        html = urllib.request.urlopen(req, timeout=25).read().decode('utf-8', 'ignore')
        pats = [
            r'window\.location\.replace\(["\']([^"\']+)["\']\)',
            r'window\.location\.href\s*=\s*["\']([^"\']+)["\']',
            r'URL=\'?([^\'">]+)',
            r'(https?://[^\s"\'<>]+)',
        ]
        for p in pats:
            m = re.search(p, html)
            if m:
                return m.group(1)
        return 'NO_TARGET len=%d' % len(html)
    except Exception as e:
        return 'ERR %s' % e

for u in sys.argv[1:]:
    u = u.replace('&amp;', '&')
    print('->', resolve(u))
