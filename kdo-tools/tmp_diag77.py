import json, urllib.request, re, subprocess

env_path = r"C:\Users\Administrator\AppData\Local\hermes\profiles\duanwangye\.env"
content = subprocess.check_output(['cat', env_path], text=True)
app_id = app_secret = None
for line in content.splitlines():
    m = re.match(r'FEISHU_APP_ID=(.*)', line)
    if m: app_id = m.group(1).strip().strip('"').strip("'")
    m = re.match(r'FEISHU_APP_SECRET=(.*)', line)
    if m: app_secret = m.group(1).strip().strip('"').strip("'")

def api(url, data=None, method=None, token=None):
    headers = {"Content-Type": "application/json"}
    if token: headers["Authorization"] = "Bearer " + token
    body = json.dumps(data).encode() if data is not None else None
    req = urllib.request.Request(url, data=body, headers=headers, method=method)
    try:
        return json.loads(urllib.request.urlopen(req, timeout=30).read())
    except urllib.error.HTTPError as e:
        try:
            return json.loads(e.read().decode())
        except Exception:
            return {"http_error": e.code, "msg": e.reason}

tok = api("https://open.feishu.cn/open-apis/auth/v3/tenant_access_token/internal",
          {"app_id": app_id, "app_secret": app_secret}, "POST")
tk = tok["tenant_access_token"]
doc_id = "KWUCdercVoYlYXxXZrYctug6nog"

# 诊断1: 文档元数据
r1 = api(f"https://open.feishu.cn/open-apis/docx/v1/documents/{doc_id}", token=tk)
print("meta:", json.dumps(r1, ensure_ascii=False)[:400])

# 诊断2: blocks children
r2 = api(f"https://open.feishu.cn/open-apis/docx/v1/documents/{doc_id}/blocks/{doc_id}/children?page_size=10", token=tk)
print("children:", json.dumps(r2, ensure_ascii=False)[:400])

# 诊断3: raw_content
r3 = api(f"https://open.feishu.cn/open-apis/docx/v1/documents/{doc_id}/raw_content", token=tk)
print("raw:", json.dumps(r3, ensure_ascii=False)[:400])
