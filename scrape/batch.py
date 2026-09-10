# -*- coding: utf-8 -*-
"""Batch runner v2: searches with rate-limit-safe intervals + resolve baidu redirects."""
import sys, json, io, os, re, time
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8", errors="replace")
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from urllib.parse import quote
from playwright.sync_api import sync_playwright
import fetch as F

def resolve_baidu_link(page, url):
    """Navigate a baidu redirect link and return the real final URL."""
    try:
        page.goto(url, timeout=25000, wait_until="domcontentloaded")
        page.wait_for_timeout(2500)
        return page.url
    except Exception:
        try:
            return page.url
        except Exception:
            return url

def run(tasks_path, out_dir, search_interval=18, resolve_top=6):
    with open(tasks_path, encoding="utf-8") as f:
        tasks = json.load(f)
    os.makedirs(out_dir, exist_ok=True)
    pw = sync_playwright().__enter__()
    browser, ctx = F._ctx(pw)
    log = []
    for i, t in enumerate(tasks.get("searches", [])):
        if i > 0:
            time.sleep(search_interval)
        tid, q = t["id"], t["q"]
        page = ctx.new_page()
        items, engine = [], ""
        try:
            items = F._baidu(page, quote(q), t.get("count", 10))
            engine = "baidu"
        except Exception as e:
            engine = f"baidu_err:{str(e)[:50]}"
        if not items:
            time.sleep(search_interval)
            try:
                items = F._sogou(page, quote(q), t.get("count", 10))
                engine += "+sogou"
            except Exception as e:
                engine += f"+sogou_err:{str(e)[:50]}"
        # resolve baidu redirects for top results
        for it in items[:resolve_top]:
            u = it.get("url", "")
            if "baidu.com/link" in u:
                it["real_url"] = resolve_baidu_link(page, u)
            else:
                it["real_url"] = u
        page.close()
        with open(os.path.join(out_dir, f"search_{tid}.json"), "w", encoding="utf-8") as f:
            json.dump({"id": tid, "q": q, "engine": engine, "results": items}, f, ensure_ascii=False, indent=1)
        log.append(f"SEARCH {tid}: engine={engine} n={len(items)}")
    for t in tasks.get("pages", []):
        tid, url = t["id"], t["url"]
        page = ctx.new_page()
        final_url, status, title, text = url, None, "", ""
        try:
            resp = page.goto(url, timeout=45000, wait_until="domcontentloaded")
            status = resp.status if resp else None
            page.wait_for_timeout(int(t.get("wait", 3000)))
            final_url = page.url
            title = page.title()
            page.evaluate("() => {document.querySelectorAll('script,style,noscript,svg,iframe').forEach(e=>e.remove())}")
            text = page.evaluate("() => document.body ? document.body.innerText : ''")
        except Exception as e:
            text = f"__ERROR__ {type(e).__name__}: {str(e)[:150]}"
        page.close()
        if text and not text.startswith("__ERROR__"):
            text = re.sub(r"\n{3,}", "\n\n", text)
            text = re.sub(r"[ \t]{2,}", " ", text)
        with open(os.path.join(out_dir, f"page_{tid}.txt"), "w", encoding="utf-8") as f:
            f.write(f"URL: {url}\nFINAL_URL: {final_url}\nSTATUS: {status}\nTITLE: {title}\n{'='*60}\n{text}")
        log.append(f"PAGE {tid}: status={status} len={len(text)} final={final_url[:80]}")
    browser.close()
    pw.stop()
    with open(os.path.join(out_dir, "_run.log"), "w", encoding="utf-8") as f:
        f.write("\n".join(log) + "\n")

if __name__ == "__main__":
    run(sys.argv[1], sys.argv[2])
