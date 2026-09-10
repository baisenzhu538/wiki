# -*- coding: utf-8 -*-
"""Try fallback engines for Chinese search."""
import re, time
import urllib.parse
import requests
from lxml import etree
import urllib3
urllib3.disable_warnings()

PC_UA = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0 Safari/537.36"
MOB_UA = "Mozilla/5.0 (iPhone; CPU iPhone OS 17_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.0 Mobile/15E148 Safari/604.1"

q = "叮当快药 三年亏损 28亿"

# 1) baidu with session warmup
try:
    S = requests.Session()
    S.headers.update({'User-Agent': PC_UA, 'Accept-Language': 'zh-CN,zh;q=0.9'})
    S.get('https://www.baidu.com/', timeout=15)
    time.sleep(1)
    r = S.get('https://www.baidu.com/s', params={'wd': q, 'rn': 10}, timeout=20)
    t = etree.HTML(r.text)
    res = t.xpath('//h3/a')
    print('BAIDU(session):', r.status_code, 'title:', (t.xpath('//title/text()') or [''])[0][:40], 'h3:', len(res))
    for a in res[:5]:
        print('   -', ''.join(a.xpath('.//text()'))[:60])
except Exception as e:
    print('BAIDU err', e)

time.sleep(2)

# 2) duckduckgo html
try:
    r = requests.get('https://html.duckduckgo.com/html/', params={'q': q}, headers={'User-Agent': PC_UA}, timeout=25)
    t = etree.HTML(r.text)
    res = t.xpath('//a[contains(@class,"result__a")]')
    print('DDG(html):', r.status_code, 'results:', len(res))
    for a in res[:5]:
        print('   -', ''.join(a.xpath('.//text()'))[:60])
except Exception as e:
    print('DDG err', e)

time.sleep(2)

# 3) bing mobile UA
try:
    r = requests.get('https://www.bing.com/search', params={'q': '"叮当快药" 亏损 28亿'}, headers={'User-Agent': MOB_UA}, timeout=25)
    t = etree.HTML(r.text)
    res = t.xpath('//li[@class="b_algo"]//h2/a')
    print('BING(mobile):', r.status_code, 'results:', len(res))
    for a in res[:5]:
        print('   -', ''.join(a.xpath('.//text()'))[:60])
except Exception as e:
    print('BING err', e)

time.sleep(2)

# 4) sogou retest with mobile UA
try:
    r = requests.get('https://www.sogou.com/web', params={'query': q}, headers={'User-Agent': MOB_UA}, timeout=25)
    t = etree.HTML(r.text)
    res = t.xpath('//h3/a')
    print('SOGOU(mobile):', r.status_code, 'results:', len(res), 'title:', (t.xpath('//title/text()') or [''])[0][:30])
except Exception as e:
    print('SOGOU err', e)
