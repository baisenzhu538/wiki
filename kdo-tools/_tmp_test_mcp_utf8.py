"""#350 回归：kdo MCP server 中文 query 5 例 + 英文回归（协议级 stdio 实测）。"""
import json
import subprocess
import sys

sys.stdout.reconfigure(encoding="utf-8", errors="replace")

SERVER = r"C:\Users\Administrator\Desktop\wiki\kdo-tools\mcp\server.py"
QUERIES = [
    ("中文1", "偶遇自动采集", "framework-serendipity|偶遇"),
    ("中文2", "视频号 逐字稿", "wechat|视频号"),
    ("中文3", "科学决策", "decision|决策"),
    ("中文4", "知识库 检索", "检索|query"),
    ("中文5", "Y模型", "Y模型|y-model"),
    ("英文", "knowledge delivery", "kdo|knowledge"),
]

p = subprocess.Popen(
    [sys.executable, SERVER],
    stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE,
    env={"PYTHONIOENCODING": "utf-8", **__import__("os").environ},
)
# 初始化
init = {"jsonrpc": "2.0", "id": 1, "method": "initialize", "params": {
    "protocolVersion": "2024-11-05", "capabilities": {}, "clientInfo": {"name": "test", "version": "1"}}}
p.stdin.write((json.dumps(init) + "\n").encode("utf-8"))
p.stdin.flush()
line = p.stdout.readline()
print("init:", "OK" if "result" in line.decode("utf-8", errors="replace") else line[:80])

ok = fail = 0
for i, (tag, query, expect) in enumerate(QUERIES, start=10):
    msg = {"jsonrpc": "2.0", "id": i, "method": "tools/call", "params": {
        "name": "kdo_search", "arguments": {"query": query, "limit": 3}}}
    p.stdin.write((json.dumps(msg) + "\n").encode("utf-8"))
    p.stdin.flush()
    resp = p.stdout.readline().decode("utf-8", errors="replace")
    clean = query in resp or not any(bad in resp for bad in ["\ufffd", "\\u00"])
    hit = any(k in resp for k in ["result", "content"])
    if clean and hit:
        ok += 1
        print(f"  ✅ [{tag}] {query}")
    else:
        fail += 1
        print(f"  ❌ [{tag}] {query} -> {resp[:100]}")
p.stdin.close()
p.terminate()
print(f"\n结果: {ok} 通过 / {fail} 失败")
sys.exit(1 if fail else 0)
