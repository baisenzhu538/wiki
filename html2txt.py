# -*- coding: utf-8 -*-
"""HTML -> 纯文本(去script/style/标签),保存为 .txt"""
import re
import sys

def html2txt(f):
    html = open(f, encoding='utf-8', errors='ignore').read()
    t = re.sub(r'<script[\s\S]*?</script>|<style[\s\S]*?</style>|<!--[\s\S]*?-->', ' ', html)
    t = re.sub(r'<br\s*/?>', '\n', t)
    t = re.sub(r'</p>|</div>|</li>|</h\d>', '\n', t)
    t = re.sub(r'<[^>]+>', ' ', t)
    t = t.replace('&nbsp;', ' ').replace('&amp;', '&').replace('&lt;', '<').replace('&gt;', '>').replace('&quot;', '"').replace('&ldquo;', '“').replace('&rdquo;', '”')
    t = re.sub(r'[ \t\r]+', ' ', t)
    t = re.sub(r'\n\s*\n+', '\n', t)
    out = f.rsplit('.', 1)[0] + '.txt'
    open(out, 'w', encoding='utf-8').write(t)
    print(out, len(t))

for f in sys.argv[1:]:
    html2txt(f)
