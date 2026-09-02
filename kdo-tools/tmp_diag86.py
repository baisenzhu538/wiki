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
            return {"http_error": e.code}

tok = api("https://open.feishu.cn/open-apis/auth/v3/tenant_access_token/internal",
          {"app_id": app_id, "app_secret": app_secret}, "POST")
tk = tok["tenant_access_token"]

# 新86场 doc_id
for label, doc_id in [("new86", "StDWdSUVRo0r1RxVc0ncKFz7nUh"),
                      ("old86", "YVu2dGr6HoH7PlxhLG4c42JInoh")]:
    r = api(f"https://open.feishu.cn/open-apis/docx/v1/documents/{doc_id}/raw_content", token=tk)
    if r.get("code") == 0:
        c = r["data"]["content"]
        print(f"[{label}] OK len={len(c)}")
        print("  HEAD:", c[:200].replace("\n", " | "))
    else:
        print(f"[{label}] FAIL code={r.get('code')} msg={r.get('msg')}")
