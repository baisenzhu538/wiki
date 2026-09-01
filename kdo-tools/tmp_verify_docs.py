# -*- coding: utf-8 -*-
"""回读验证已发布飞书文档首尾"""
import json, urllib.request

ENV_PATH = r"C:\Users\Administrator\AppData\Local\hermes\profiles\duanwangye\.env"
DOCS = {
    "DOC1_Live260": "QdcBd2T8ho84nFxrkb3c2EaDnEf",
    "DOC2_AI知识管理": "OT9IdsioQopTVRxKLmHcrqWtn4f",
    "DOC5_Live257": "IlYfdaY3Uos4TAxkzchc22OEntg",
}

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

for name, doc_id in DOCS.items():
    url = f"https://open.feishu.cn/open-apis/docx/v1/documents/{doc_id}/raw_content"
    body, err = get(url, tat)
    if err is None:
        j = json.loads(body.decode("utf-8", errors="replace"))
        if j.get("code") == 0:
            c = j["data"]["content"]
            print(f"{name}: OK chars={len(c)}")
            print("  HEAD:", c[:100].replace("\n", " / "))
            print("  TAIL:", c[-100:].replace("\n", " / "))
        else:
            print(f"{name}: CODE {j.get('code')} {j.get('msg')}")
    else:
        print(f"{name}: HTTP_ERR {err.code}")
