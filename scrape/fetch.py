# -*- coding: utf-8 -*-
"""Search (Baidu primary, Sogou fallback) + page fetch via Playwright. Windows-safe."""
import sys, json, re, io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8", errors="replace")

UA = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36"

def _launch(pw):
    try:
        return pw.chromium.launch(headless=True, args=["--disable-blink-features=AutomationControlled"])
    except Exception:
        return pw.chromium.launch(headless=True, channel="msedge", args=["--no-sandbox"])

def _ctx(pw):
    browser = _launch(pw)
    ctx = browser.new_context(user_agent=UA, locale="zh-CN", viewport={"width": 1366, "height": 900}, timezone_id="Asia/Shanghai")
    ctx.add_init_script("Object.defineProperty(navigator,'webdriver',{get:()=>undefined})")
    return browser, ctx

def _baidu(page, q, count):
    page.goto(f"https://www.baidu.com/s?wd={q}&rn={max(count,10)}", timeout=40000, wait_until="domcontentloaded")
    page.wait_for_timeout(3500)
    return page.evaluate("""(n) => {
        const sel = 'div.result.c-container, div.c-container[tpl], div.c-container';
        const els = Array.from(document.querySelectorAll(sel)).slice(0, n*2);
        const out = [];
        const seen = new Set();
        for (const el of els) {
            const a = el.querySelector('h3 a') || el.querySelector('a');
            if (!a) continue;
            const title = (a.innerText||'').trim();
            if (!title || seen.has(title)) continue;
            seen.add(title);
            let snip = '';
            const c = el.querySelector('.c-abstract, [class*=content-right], .c-span-last, div[class*=abstract]');
            if (c) snip = c.innerText.trim();
            const dateM = el.innerText.match(/20(2[3-6])[-年\\/\\.](\\d{1,2})[-月\\/\\.](\\d{1,2})/);
            out.push({title, url: a.href, snippet: snip.slice(0,300), date: dateM?dateM[0]:''});
            if (out.length >= n) break;
        }
        return out;
    }""", count)

def _sogou(page, q, count):
    page.goto(f"https://www.sogou.com/web?query={q}", timeout=40000, wait_until="domcontentloaded")
    page.wait_for_timeout(3500)
    return page.evaluate("""(n) => {
        const els = Array.from(document.querySelectorAll('.vrwrap, .rb, div[class*=result]')).slice(0, n*2);
        const out = [];
        const seen = new Set();
        for (const el of els) {
            const a = el.querySelector('h3 a');
            if (!a) continue;
            const title = (a.innerText||'').trim();
            if (!title || seen.has(title)) continue;
            seen.add(title);
            let snip = '';
            const c = el.querySelector('.str-text-info, .str_info, [class*=space-txt], p');
            if (c) snip = c.innerText.trim();
            const dateM = el.innerText.match(/20(2[3-6])[-年\\/\\.](\\d{1,2})[-月\\/\\.](\\d{1,2})/);
            out.push({title, url: a.href, snippet: snip.slice(0,300), date: dateM?dateM[0]:''});
            if (out.length >= n) break;
        }
        return out;
    }""", count)

def sync_pw():
    from playwright.sync_api import sync_playwright
    return sync_playwright().__enter__()

def do_search(q, count=12):
    from urllib.parse import quote
    qe = quote(q)
    pw = sync_pw()
    browser, ctx = _ctx(pw)
    page = ctx.new_page()
    engine, items = "", []
    try:
        items = _baidu(page, qe, count)
        engine = "baidu"
    except Exception as e:
        items = []
        engine = f"baidu_err:{str(e)[:80]}"
    if not items:
        try:
            items = _sogou(page, qe, count)
            engine += "+sogou"
        except Exception as e:
            engine += f"+sogou_err:{str(e)[:80]}"
    browser.close()
    pw.stop()
    return {"engine": engine, "results": items}

def do_page(url, maxchars=9000):
    pw = sync_pw()
    browser, ctx = _ctx(pw)
    page = ctx.new_page()
    final_url, status, title, text = url, None, "", ""
    try:
        resp = page.goto(url, timeout=45000, wait_until="domcontentloaded")
        status = resp.status if resp else None
        page.wait_for_timeout(3000)
        final_url = page.url
        title = page.title()
        page.evaluate("() => {document.querySelectorAll('script,style,noscript,svg,iframe').forEach(e=>e.remove())}")
        text = page.evaluate("() => document.body ? document.body.innerText : ''")
    except Exception as e:
        text = f"__ERROR__ {type(e).__name__}: {str(e)[:200]}"
    browser.close()
    pw.stop()
    if text and not text.startswith("__ERROR__"):
        text = re.sub(r"\n{3,}", "\n\n", text)
        text = re.sub(r"[ \t]{2,}", " ", text)
        if len(text) > maxchars:
            text = text[:maxchars] + f"\n...[TRUNCATED total {len(text)}]"
    return {"status": status, "final_url": final_url, "title": title, "text": text}

if __name__ == "__main__":
    mode = sys.argv[1]
    if mode == "search":
        q = sys.argv[2]
        cnt = int(sys.argv[3]) if len(sys.argv) > 3 else 12
        print(json.dumps(do_search(q, cnt), ensure_ascii=False, indent=1))
    elif mode == "page":
        url = sys.argv[2]
        mc = int(sys.argv[3]) if len(sys.argv) > 3 else 9000
        print(json.dumps(do_page(url, mc), ensure_ascii=False))
