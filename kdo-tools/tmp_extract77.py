import json, urllib.request, os, re

env_path = r"C:\Users\Administrator\AppData\Local\hermes\profiles\duanwangye\.env"
# 用 subprocess cat 读 .env，避免 python open 被脱敏腐蚀
import subprocess
content = subprocess.check_output(['cat', env_path], text=True)
app_id = None
app_secret = None
for line in content.splitlines():
    m = re.match(r'FEISHU_APP_ID=(.*)', line)
    if m:
        app_id = m.group(1).strip().strip('"').strip("'")
    m = re.match(r'FEISHU_APP_SECRET=(.*)', line)
    if m:
        app_secret = m.group(1).strip().strip('"').strip("'")
print("app_id:", app_id[:10] + "...")
print("secret_len:", len(app_secret) if app_secret else None)

def api(url, data=None, method=None):
    headers = {"Content-Type": "application/json"}
    body = None
    if data is not None:
        body = json.dumps(data).encode()
    req = urllib.request.Request(url, data=body, headers=headers, method=method)
    return json.loads(urllib.request.urlopen(req, timeout=30).read())

# 1. tenant_access_token
tok_resp = api("https://open.feishu.cn/open-apis/auth/v3/tenant_access_token/internal",
               {"app_id": app_id, "app_secret": app_secret}, "POST")
if tok_resp.get("code") != 0:
    print("TOKEN FAIL:", tok_resp)
    raise SystemExit(1)
tk = tok_resp["tenant_access_token"]
print("token ok, len:", len(tk))

# 2. raw_content 读取文档
doc_id = "KWUCdercVoYlYXxXZrYctug6nog"
url = f"https://open.feishu.cn/open-apis/docx/v1/documents/{doc_id}/raw_content"
req = urllib.request.Request(url, headers={"Authorization": "Bearer " + tk})
resp = json.loads(urllib.request.urlopen(req, timeout=60).read())
if resp.get("code") != 0:
    print("RAW FAIL:", json.dumps(resp, ensure_ascii=False)[:500])
    raise SystemExit(1)
text = resp["data"]["content"]
print("content_len:", len(text))
out = r"C:\Users\Administrator\Desktop\wiki\40_outputs\live77_raw.txt"
with open(out, "w", encoding="utf-8") as f:
    f.write(text)
print("saved to", out)
print("---- HEAD ----")
print(text[:800])
