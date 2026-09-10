# -*- coding: utf-8 -*-
"""从 so360.html 提取完整的跳转链接(不截断)"""
import re

html = open('so360.html', encoding='utf-8', errors='ignore').read()
items = re.findall(r'<a[^>]+href="((?:https?://www\.so\.com/link|/link)\?[^"]+)"[^>]*>(.*?)</a>', html)
seen = set()
for url, txt in items:
    txt = re.sub(r'<[^>]+>', '', txt)
    txt = re.sub(r'\s+', ' ', txt).strip()
    if url in seen:
        continue
    seen.add(url)
    full = url if url.startswith('http') else 'https://www.so.com' + url
    print(txt[:60], '\n   FULL:', full, '\n')
