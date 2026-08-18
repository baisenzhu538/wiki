"""通过 CDP 从已登录的元宝页面提取 Cookie（无需用户手动复制）。"""
import json
import sys
import urllib.request
import websocket

sys.stdout.reconfigure(encoding="utf-8", errors="replace")

# 找元宝页面
pages = json.loads(urllib.request.urlopen("http://127.0.0.1:9222/json", timeout=10).read())
ws_url = None
for p in pages:
    if "yuanbao.tencent.com" in p.get("url", ""):
        ws_url = p["webSocketDebuggerUrl"]
        break
if not ws_url:
    print("❌ 未找到元宝页面")
    sys.exit(1)

ws = websocket.create_connection(ws_url, timeout=30)
msg_id = 1

def send(method, params=None):
    global msg_id
    ws.send(json.dumps({"id": msg_id, "method": method, "params": params or {}}))
    msg_id += 1
    while True:
        resp = json.loads(ws.recv())
        if resp.get("id") == msg_id - 1:
            return resp

send("Network.enable")
resp = send("Network.getAllCookies")
cookies = resp.get("result", {}).get("cookies", [])
target = [c for c in cookies if "yuanbao.tencent.com" in c.get("domain", "")]
print(f"找到 {len(target)} 个元宝 Cookie")
if target:
    cookie_str = "; ".join(f"{c['name']}={c['value']}" for c in target)
    print("COOKIE_START")
    print(cookie_str)
    print("COOKIE_END")
else:
    print("⚠️ 无元宝 Cookie——可能未登录或登录已过期")
ws.close()
