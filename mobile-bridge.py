"""Minimal HTTP→WebSocket bridge for mobile access to Hermes agents."""
import json, asyncio, os
from aiohttp import web
import websockets

AGENTS = {
    "老顽童": "laowantong", "王语嫣": "wangyuyan",
    "洪七公": "hongqigong", "段王爷": "duanwangye",
}

async def index(request):
    return web.FileResponse(os.path.join(os.path.dirname(__file__), "mobile-chat.html"))

async def chat(request):
    data = await request.json()
    agent_id = data.get("agent", "laowantong")
    message = data.get("message", "")

    # Forward to Hermes hub WebSocket
    try:
        async with websockets.connect("ws://localhost:8765/ws") as ws:
            await ws.send(json.dumps({
                "type": "chat",
                "agent": agent_id,
                "message": message,
                "platform": "web",
            }))
            resp = await asyncio.wait_for(ws.recv(), timeout=120)
            return web.json_response(json.loads(resp))
    except Exception as e:
        return web.json_response({"response": f"Agent 未响应: {e}"})

app = web.Application()
app.router.add_get("/", index)
app.router.add_post("/chat", chat)
app.router.add_static("/", os.path.dirname(__file__))

if __name__ == "__main__":
    print("Mobile Bridge: http://0.0.0.0:9876")
    web.run_app(app, host="0.0.0.0", port=9876)
