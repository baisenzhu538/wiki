# -*- coding: utf-8 -*-
"""Debug bing search."""
import sys, io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8", errors="replace")
from urllib.parse import quote
from playwright.sync_api import sync_playwright

q = "京东健康 2025年全年业绩 收入"
with sync_playwright() as pw:
    try:
        browser = pw.chromium.launch(headless=True, args=["--disable-blink-features=AutomationControlled"])
    except Exception:
        browser = pw.chromium.launch(headless=True, channel="msedge")
    ctx = browser.new_context(
        user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36",
        locale="zh-CN", viewport={"width": 1366, "height": 900}, timezone_id="Asia/Shanghai")
    ctx.add_init_script("Object.defineProperty(navigator,'webdriver',{get:()=>undefined})")
    page = ctx.new_page()
    url = f"https://www.bing.com/search?q={quote(q)}&mkt=zh-CN&setlang=zh-hans"
    print("URL:", url)
    page.goto(url, timeout=45000, wait_until="domcontentloaded")
    page.wait_for_timeout(3500)
    print("TITLE:", page.title())
    try:
        val = page.eval_on_selector("textarea#sb_form_q, input#sb_form_q", "el => el.value")
        print("QUERYBOX:", val)
    except Exception as e:
        print("no query box", e)
    n = page.locator("li.b_algo").count()
    print("RESULTS:", n)
    if n == 0:
        body = page.evaluate("() => document.body.innerText")
        print("BODYHEAD:", body[:600])
    browser.close()
