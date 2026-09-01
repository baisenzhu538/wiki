# -*- coding: utf-8 -*-
"""L1 探测 doc2 (yitang fs-doc) + doc3 (yitanger wiki)"""
import json, urllib.request

ENV_PATH = r"C:\Users\Administrator\AppData\Local\hermes\profiles\duanwangye\.env"
DOC2 = "KulEd8ruzoKFxWxrHocc2rXnnEd"          # AI×知识管理 探索营内测Candy
DOC3 = "VUTtwYbs5irOiNk9T3NcQCljn2s"          # yitanger wiki 链接

env = {}
with open(ENV_PATH, "r", encoding="utf-8") as f:
    for line in f:
        line = line.strip()
        if line and "=" in line and not line.startswith("#"):
            k, v = line.split("=", 1)
            env[k.strip()] = v.strip()

app_id = env.get("FEISHU_APP_ID", "")
app_secret = env.get("FEISHU_APP_SECRET", "")

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

r = post("https://open.feishu.cn/open-apis/auth/v3/tenant_access_token/internal",
         {"app_id": app_id, "app_secret": app_secret})
tat = r["tenant_access_token"]
print("TAT_OK")

for name, doc_id in [("DOC2_KulEd", DOC2), ("DOC3_wiki_VUTt", DOC3)]:
    url = f"https://open.feishu.cn/open-apis/docx/v1/documents/{doc_id}/raw_content"
    body, err = get(url, tat)
    if err is None:
        j = json.loads(body.decode("utf-8", errors="replace"))
        if j.get("code") == 0:
            content = j["data"]["content"]
            print(f"{name}: L1_SUCCESS total_chars={len(content)}")
            print("  HEAD:", content[:200].replace("\n", " / "))
            with open(rf"C:\Users\Administrator\Desktop\wiki\kdo-tools\tmp_raw_{name}.txt", "w", encoding="utf-8") as f:
                f.write(content)
        else:
            print(f"{name}: L1_CODE {j.get('code')} {j.get('msg')}")
            # 尝试 wiki node 解析
            try:
                url2 = f"https://open.feishu.cn/open-apis/wiki/v2/spaces/get_node?token={doc_id}"
                req = urllib.request.Request(url2, headers={"Authorization": "Bearer " + tat})
                j2 = json.loads(urllib.request.urlopen(req, timeout=20).read())
                print(f"  wiki_node:", json.dumps(j2.get("data", {}), ensure_ascii=False)[:300])
            except Exception as e2:
                print(f"  wiki_node ERR: {e2}")
    else:
        print(f"{name}: L1_HTTP_ERR {err.code}")
        print("  ", body.decode("utf-8", errors="replace")[:300])
