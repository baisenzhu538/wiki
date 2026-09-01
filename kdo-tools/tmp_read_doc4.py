# -*- coding: utf-8 -*-
"""读取 DOC4 wiki (KzXwwSWmMiAKJzkPnIBcvTpdnhf) 内容"""
import json, urllib.request

ENV_PATH = r"C:\Users\Administrator\AppData\Local\hermes\profiles\duanwangye\.env"
DOC4 = "KzXwwSWmMiAKJzkPnIBcvTpdnhf"

env = {}
with open(ENV_PATH, "r", encoding="utf-8") as f:
    for line in f:
        line = line.strip()
        if line and "=" in line and not line.startswith("#"):
            k, v = line.split("=", 1)
            env[k.strip()] = v.strip()

def post(url, body):
    data = json.dumps(body).encode()
    req = urllib.request.Request(url, data=data, headers={"Content-Type": "application/json"}, method="POST")
    return json.loads(urllib.request.urlopen(req, timeout=20).read())

def get(url, token):
    req = urllib.request.Request(url, headers={"Authorization": "Bearer " + token})
    try:
        return urllib.request.urlopen(req, timeout=30).read(), None
    except urllib.error.HTTPError as e:
        return e.read() if hasattr(e, "read") else b"", e

r = post("https://open.feishu.cn/open-apis/auth/v3/tenant_access_token/internal",
         {"app_id": env["FEISHU_APP_ID"], "app_secret": env["FEISHU_APP_SECRET"]})
tat = r["tenant_access_token"]

url = f"https://open.feishu.cn/open-apis/docx/v1/documents/{DOC4}/raw_content"
body, err = get(url, tat)
if err is None:
    j = json.loads(body.decode("utf-8", errors="replace"))
    if j.get("code") == 0:
        content = j["data"]["content"]
        print(f"DOC4 L1_SUCCESS total_chars={len(content)}")
        print("==== FULL CONTENT ====")
        print(content)
    else:
        print(f"DOC4 CODE {j.get('code')} {j.get('msg')}")
else:
    print(f"DOC4 HTTP_ERR {err.code}", body.decode("utf-8", errors="replace")[:300])
