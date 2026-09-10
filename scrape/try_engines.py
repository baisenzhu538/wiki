# -*- coding: utf-8 -*-
"""Try multiple search engines via playwright."""
import sys, io, json
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8", errors="replace")
from urllib.parse import quote
from playwright.sync_api import sync_playwright

UA = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36"

def try_engine(name, url, wait, extract_js):
    try:
        with sync_playwright() as pw:
            try:
                browser = pw.chromium.launch(headless=True)
            except Exception:
                browser = pw.chromium.launch(headless=True, channel="msedge")
            ctx = browser.new_context(user_agent=UA, locale="zh-CN", timezone_id="Asia/Shanghai")
            ctx.add_init_script("Object.defineProperty(navigator,'webdriver',{get:()=>undefined})")
            page = ctx.new_page()
            page.goto(url, timeout=40000, wait_until="domcontentloaded")
            page.wait_for_timeout(wait)
            n = page.evaluate(extract_js["count"])
            items = page.evaluate(extract_js["items"]) if n else []
            title = page.title()
            body_head = ""
            if n == 0:
                body_head = page.evaluate("() => document.body ? document.body.innerText.slice(0,300) : ''")
            browser.close()
            print(f"=== {name}: title={title!r} results={len(items)}")
            if items:
                for it in items[:5]:
                    print("  -", it.get("title","")[:50], "|", it.get("url","")[:90])
            if body_head:
                print("  body:", body_head.replace("\n"," / ")[:200])
    except Exception as e:
        print(f"=== {name}: EXCEPTION {type(e).__name__}: {str(e)[:200]}")

q = "京东健康 2025年全年业绩 收入"
E = {}
E["ddg_html"] = dict(
    url=f"https://html.duckduckgo.com/html/?q={quote(q)}", wait=4000,
    extract_js={"count": "() => document.querySelectorAll('.result').length",
                "items": "() => Array.from(document.querySelectorAll('.result')).slice(0,8).map(r=>{const a=r.querySelector('a.result__a');return {title:a?a.innerText:'',url:a?a.href:''}})"})
E["baidu"] = dict(
    url=f"https://www.baidu.com/s?wd={quote(q)}&rn=15", wait=4500,
    extract_js={"count": "() => document.querySelectorAll('div.result, div.c-container[tpl]').length",
                "items": "() => Array.from(document.querySelectorAll('div.result h3 a, div.c-container h3 a')).slice(0,10).map(a=>({title:a.innerText,url:a.href}))"})
E["sogou"] = dict(
    url=f"https://www.sogou.com/web?query={quote(q)}", wait=4500,
    extract_js={"count": "() => document.querySelectorAll('.vrwrap, .rb').length",
                "items": "() => Array.from(document.querySelectorAll('.vrwrap h3 a, .rb h3 a')).slice(0,10).map(a=>({title:a.innerText,url:a.href}))"})

for name, cfg in E.items():
    try_engine(name, cfg["url"], cfg["wait"], cfg["extract_js"])
