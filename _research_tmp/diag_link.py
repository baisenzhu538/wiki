# -*- coding: utf-8 -*-
"""Diagnose so.com /link redirect mechanism."""
import requests

UA = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0 Safari/537.36'}
url = 'https://www.so.com/link?m=uuSUgmbTh%2BEWnr9L1JY20%2Fq3WcJnxVvv%2FqK50AA%2BBzkOulY6TtXzKFreVYcE7TuZGo'
r = requests.get(url, headers=UA, timeout=20, allow_redirects=False)
print('status', r.status_code)
print('location:', r.headers.get('Location'))
print('---body first 500---')
print(r.text[:500])
