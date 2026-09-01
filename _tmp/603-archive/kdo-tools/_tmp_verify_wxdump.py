import sys
sys.stdout.reconfigure(encoding="utf-8", errors="replace")

from pywxdump import get_wx_info, get_wx_db

# 1. 获取微信信息 + 密钥
info = get_wx_info()
if not info:
    print("❌ 未获取到微信信息——请确认微信 PC 版已登录运行")
    sys.exit(1)

for acc in info:
    print(f"✅ 微信账号: {acc.get('name')} / {acc.get('wxid')} / key={acc.get('key')[:8]}...")
    print(f"   msg_dir: {acc.get('msg_dir')}")
