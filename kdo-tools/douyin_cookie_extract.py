"""CDP 提取抖音匿名新鲜 Cookie → Netscape cookies.txt（供 yt-dlp 使用）。

用法: python _tmp_douyin_cookie.py [输出路径]
"""
import json
import subprocess
import sys
import time
import urllib.request

import websocket

sys.stdout.reconfigure(encoding="utf-8", errors="replace")

EDGE = r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe"
PROFILE = r"C:\Users\Administrator\tools\edge-debug-profile-dy"  # 复用 dy profile，cookie 可持续累积
PORT = 9223
OUT = sys.argv[1] if len(sys.argv) > 1 else r"C:\Users\Administrator\Desktop\wiki\60_feedback\wechat-collect\douyin-dali\cookies.txt"

proc = subprocess.Popen([
    EDGE, "--headless=new", f"--remote-debugging-port={PORT}", "--remote-allow-origins=*",
    f"--user-data-dir={PROFILE}", "--no-first-run",
    "https://www.douyin.com/video/7654610643165120177",
], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

try:
    ws_url = None
    for _ in range(30):
        try:
            pages = json.loads(urllib.request.urlopen(f"http://127.0.0.1:{PORT}/json", timeout=3).read())
            for p in pages:
                if "douyin.com" in p.get("url", ""):
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

    send("Network.enable")
    time.sleep(10)  # 等页面加载+匿名 cookie 下发
    r = send("Network.getAllCookies")
    cookies = r.get("result", {}).get("cookies", [])
    lines = ["# Netscape HTTP Cookie File"]
    n = 0
    for c in cookies:
        if "douyin" not in c.get("domain", "") and "iesdouyin" not in c.get("domain", ""):
            continue
        domain = c["domain"]
        flag = "TRUE" if domain.startswith(".") else "FALSE"
        secure = "TRUE" if c.get("secure") else "FALSE"
        expires = int(c.get("expires", 0) or 0)
        lines.append("\t".join([domain, flag, c.get("path", "/"), secure, str(expires), c["name"], c["value"]]))
        n += 1
    with open(OUT, "w", encoding="utf-8") as f:
        f.write("\n".join(lines) + "\n")
    print(f"✅ {n} 个 douyin cookie → {OUT}")
    ws.close()
finally:
    proc.terminate()
