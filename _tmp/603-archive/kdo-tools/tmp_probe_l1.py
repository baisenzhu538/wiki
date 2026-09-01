# -*- coding: utf-8 -*-
"""L1 探测：TAT + raw_content 提取 yitang fs-doc 逐字稿"""
import json, urllib.request, os, re

ENV_PATH = r"C:\Users\Administrator\AppData\Local\hermes\profiles\duanwangye\.env"
DOC_ID = "YTJgdq3idoRKwExETDqc5JlfnNd"

# 读取 .env
env = {}
with open(ENV_PATH, "r", encoding="utf-8") as f:
    for line in f:
        line = line.strip()
        if line and "=" in line and not line.startswith("#"):
            k, v = line.split("=", 1)
            env[k.strip()] = v.strip()

app_id = env.get("FEISHU_APP_ID", "")
app_secret = env.get("FEISHU_APP_SECRET", "")
print("APP_ID:", app_id[:10], "len_secret:", len(app_secret))

def post(url, body, token=None):
    data = json.dumps(body).encode()
    headers = {"Content-Type": "application/json"}
    if token:
        headers["Authorization"] = "Bearer " + token
    req = urllib.request.Request(url, data=data, headers=headers, method="POST")
    return json.loads(urllib.request.urlopen(req, timeout=20).read())

def get(url, token):
    req = urllib.request.Request(url, headers={"Authorization": "Bearer " + token})
    try:
        return urllib.request.urlopen(req, timeout=30).read(), None
    except urllib.error.HTTPError as e:
        return e.read() if hasattr(e, "read") else b"", e

# 1. 换 TAT
r = post("https://open.feishu.cn/open-apis/auth/v3/tenant_access_token/internal",
         {"app_id": app_id, "app_secret": app_secret})
if r.get("code") != 0:
    print("TAT_FAIL:", r)
    raise SystemExit(1)
tat = r["tenant_access_token"]
print("TAT_OK, len:", len(tat))

# 2. raw_content
url = f"https://open.feishu.cn/open-apis/docx/v1/documents/{DOC_ID}/raw_content"
body, err = get(url, tat)
if err is None:
    j = json.loads(body.decode("utf-8", errors="replace"))
    if j.get("code") == 0:
        content = j["data"]["content"]
        print("L1_SUCCESS total_chars:", len(content))
        print("---HEAD---")
        print(content[:800])
        with open(r"C:\Users\Administrator\Desktop\wiki\kdo-tools\tmp_rawcontent.txt", "w", encoding="utf-8") as f:
            f.write(content)
        print("SAVED")
    else:
        print("L1_CODE:", j.get("code"), j.get("msg"))
else:
    print("L1_HTTP_ERR:", err.code)
    try:
        print(body.decode("utf-8", errors="replace")[:500])
    except Exception:
        print(body[:500])
