# -*- coding: utf-8 -*-
"""解析 so.com 跳转,拿到真实目标URL"""
import re
import sys
import urllib.parse
import urllib.request

UA = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) Chrome/120.0',
      'Referer': 'https://www.so.com/'}

def resolve(url):
    try:
        req = urllib.request.Request(url, headers=UA)
        html = urllib.request.urlopen(req, timeout=25).read().decode('utf-8', 'ignore')
        pats = [
            r"window\.location\.(?:replace|href)\s*=\s*[\"']([^\"']+)[\"']",
            r"location\.replace\([\"']([^\"']+)[\"']\)",
            r'URL=\'?([^\'">]+)',
            r'(https?://[^\s"\'<>]*(?:gov\.cn|nmpa\.gov\.cn|samr\.gov\.cn|nhc\.gov\.cn|nhsa\.gov\.cn)[^\s"\'<>]*)',
        ]
        for p in pats:
            m = re.search(p, html)
            if m:
                return m.group(1)
        return 'NO_TARGET len=%d head=%s' % (len(html), html[:200])
    except Exception as e:
        return 'ERR %s' % e

for u in sys.argv[1:]:
    print('->', resolve(u))
