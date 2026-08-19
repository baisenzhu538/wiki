"""用 CDP 驱动无头 Edge 渲染抖音作者主页，提取视频列表（标题/点赞/链接）。

用法: python _tmp_douyin_user.py <sec_uid 或 profile url>
产出: JSON 到 stdout（[{title, likes, url, aweme_id}]）
"""
import json
import subprocess
import sys
import time
import urllib.request

import websocket

sys.stdout.reconfigure(encoding="utf-8", errors="replace")

EDGE = r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe"
PROFILE = r"C:\Users\Administrator\tools\edge-debug-profile"
PORT = 9223  # 避开元宝用的 9222

target = sys.argv[1] if len(sys.argv) > 1 else ""
if not target.startswith("http"):
    target = f"https://www.douyin.com/user/{target}"

# 启动无头 Edge（独立调试 profile，不碰用户日常浏览器）
proc = subprocess.Popen([
    EDGE, "--headless=new", f"--remote-debugging-port={PORT}", "--remote-allow-origins=*",
    f"--user-data-dir={PROFILE}-dy", "--no-first-run", target,
], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

try:
    # 等 CDP 起来
    ws_url = None
    for _ in range(30):
        try:
            pages = json.loads(urllib.request.urlopen(f"http://127.0.0.1:{PORT}/json", timeout=3).read())
            for p in pages:
                if "douyin.com/user" in p.get("url", ""):
                    ws_url = p["webSocketDebuggerUrl"]
                    break
            if ws_url:
                break
        except Exception:
            pass
        time.sleep(1)
    if not ws_url:
        print("❌ CDP 页面未就绪")
        sys.exit(1)

    ws = websocket.create_connection(ws_url, timeout=30)
    mid = 0

    def send(method, params=None):
        global mid
        mid += 1
        ws.send(json.dumps({"id": mid, "method": method, "params": params or {}}))
        while True:
            resp = json.loads(ws.recv())
            if resp.get("id") == mid:
                return resp

    # 等页面渲染（抖音是重 JS 应用，视频列表异步加载）
    time.sleep(12)
    # 多次滚动触发全量加载
    for _ in range(6):
        send("Runtime.evaluate", {"expression": "window.scrollTo(0, document.body.scrollHeight)"})
        time.sleep(2.5)
    send("Runtime.evaluate", {"expression": "window.scrollTo(0, 0)"})
    time.sleep(2)

    # 从 DOM 提取视频卡片：链接含 /video/<id>，点赞数在卡片内
    js = """
(() => {
  const out = [];
  document.querySelectorAll('a[href*="/video/"]').forEach(a => {
    const m = a.href.match(/\\/video\\/(\\d+)/);
    if (!m) return;
    const card = a.closest('li') || a.parentElement;
    const text = (card ? card.innerText : a.innerText) || '';
    // 点赞数通常在卡片文本里（可能带"万"）
    const lm = text.match(/(\\d+(?:\\.\\d+)?)(\\s*万)?\\s*$/m);
    let likes = 0;
    const likeMatch = text.match(/(\\d+(?:\\.\\d+)?)(万)?(?!.*\\d)/);
    if (likeMatch) likes = parseFloat(likeMatch[1]) * (likeMatch[2] ? 10000 : 1);
    const title = (a.getAttribute('title') || text.split('\\n')[0] || '').trim();
    out.push({aweme_id: m[1], url: a.href, title: title.slice(0, 80), likes, raw: text.slice(0, 120)});
  });
  // 去重
  const seen = new Set();
  return out.filter(v => !seen.has(v.aweme_id) && seen.add(v.aweme_id));
})()
"""
    r = send("Runtime.evaluate", {"expression": js, "returnByValue": True})
    videos = r.get("result", {}).get("result", {}).get("value", [])
    print(json.dumps(videos, ensure_ascii=False, indent=1))
    # 页面标题辅助诊断
    t = send("Runtime.evaluate", {"expression": "document.title", "returnByValue": True})
    print("PAGE_TITLE:", t.get("result", {}).get("result", {}).get("value", ""), file=sys.stderr)
    ws.close()
finally:
    proc.terminate()
