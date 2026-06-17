# 微信MCP — 消息提取与查询流水线

## 概述
通过 wechat-decrypt 工具，从本地微信数据库中解密并查询聊天记录。
支持历史消息查询（无需微信在线）和实时消息监听（需微信在线）。

## 架构

```
微信PC客户端 → SQLCipher加密DB → wx_key提取密钥 → PBKDF2派生enc_key
                                                    ↓
                                           wechat-decrypt MCP服务
                                                    ↓
                                          Hermes Agent 调用查询
```

## 环境

| 组件 | 路径 |
|------|------|
| wechat-decrypt | `C:\Users\Administrator\wechat-decrypt\` |
| wx_key (密钥提取) | `C:\Tools\wx_key\wx_key.exe` |
| Python | `C:\Program Files\Python312\python.exe` |
| MCP Web服务 | `http://localhost:5678` |
| 配置文件 | `C:\Users\Administrator\wechat-decrypt\config.json` |
| 密钥文件 | `C:\Users\Administrator\wechat-decrypt\all_keys.json` |
| 解密输出 | `C:\Users\Administrator\wechat-decrypt\decrypted\` |
| 开机自启 | `shell:startup\wechat_mcp_autostart.bat` |

## 当前账号

| 账号 | wxid | 消息库大小 | 密钥状态 |
|------|------|-----------|----------|
| 大号 | baconzhu_5d29 | 20MB (message_0) + 28MB (biz_message_0) | ✅ 已提取 |
| 小号 | wxid_53kdj7ep82rv22_ffd5 | 2.9MB + 1.1MB | ✅ 已提取 |

## 完整操作流程

### 1. 提取密钥（新账号或密钥过期时）

```bash
# 前提：微信PC已登录目标账号
# 运行 wx_key.exe
C:\Tools\wx_key\wx_key.exe
# → 点击「开始提取密钥」→ 复制64位hex passphrase

# 派生enc_key（Python）
python3 << 'EOF'
import hashlib, os, json
passphrase = "<从wx_key获取的64位hex>"
base = "D:\\Backup\\Documents\\xwechat_files\\<wxid>\\db_storage"

keys = {}
for root, dirs, files in os.walk(base):
    for f in files:
        if f.endswith('.db'):
            path = os.path.join(root, f)
            with open(path, 'rb') as fp:
                salt = fp.read(16)
            enc_key = hashlib.pbkdf2_hmac('sha512', passphrase.encode(), salt, 256000, dklen=32).hex()
            rel = os.path.relpath(path, base).replace('\\', '\\\\')
            keys[rel] = {"enc_key": enc_key, "salt": salt.hex(), "size_mb": round(os.path.getsize(path)/(1024*1024),1)}

# 合并到 all_keys.json
with open('C:\\Users\\Administrator\\wechat-decrypt\\all_keys.json', 'r') as f:
    existing = json.load(f)
existing.update(keys)
with open('C:\\Users\\Administrator\\wechat-decrypt\\all_keys.json', 'w') as f:
    json.dump(existing, f, indent=2)
EOF
```

### 2. 解密数据库

```bash
# 更新 config.json 指向目标账号
# db_dir: D:\\Backup\\Documents\\xwechat_files\\<wxid>\\db_storage

# 运行解密
cd C:\Users\Administrator\wechat-decrypt
python main.py decrypt
# 解密后的数据库在 decrypted\message\ 目录
```

### 3. 查询聊天记录

```python
import sqlite3, hashlib

# 使用解密后的数据库
db = 'C:\\Users\\Administrator\\wechat-decrypt\\decrypted\\message\\message_0.db'
conn = sqlite3.connect(f'file:{db}?mode=ro', uri=True)

# 表名 = Msg_ + MD5(wxid)
wxid = 'wxid_pijc2qfirlxe11'  # 目标联系人
table = f'Msg_{hashlib.md5(wxid.encode()).hexdigest()}'

# 查所有文字消息
cur = conn.cursor()
cur.execute(f"""SELECT local_id, real_sender_id, create_time, message_content
    FROM [{table}]
    WHERE message_content IS NOT NULL AND message_content != ''
    ORDER BY create_time""")
for row in cur.fetchall():
    print(row)
```

### 4. biz_message_0.db（企业微信/公众号消息）

同样结构，可能有额外的消息。需单独解密和查询。

---

## 启动MCP服务

```bash
cd C:\Users\Administrator\wechat-decrypt
python main.py web
# 监听 http://localhost:5678
```

**注意**：`main.py web` 需要微信进程在运行，否则会报错退出。
如果只需要查历史数据（微信不在线），可以跳过 `check_wechat_running()` 检查，
或直接使用解密后的数据库文件查询。

---

## 开机自启

已配置：`shell:startup\wechat_mcp_autostart.bat`
启动时会等待微信进程（最多60秒），然后启动MCP服务。

**前提**：微信需设置为开机自动启动并自动登录。

---

## 使用限制

| 场景 | 可用性 |
|------|--------|
| 微信在线 + MCP在线 | ✅ 实时消息 + 历史查询 |
| 微信离线 + MCP在线 | ⚠️ 仅历史查询（用解密后的DB） |
| 微信离线 + MCP离线 | ❌ 不可用 |

**远程访问**：办公室通过飞书 → Hermes 即可调用本机MCP，
前提是本机不关机、不断网、微信保持登录。

**数据同步**：回家登录微信后，新增消息会自动同步到本地数据库，
再次解密即可获取新消息。

---

## 常见问题

**Q: 为什么搜"海浪的声音"只有1条？**
A: "海浪的声音"是微信昵称而非备注名。数据库中联系人存储为 wxid。
需要先确认 wxid → MD5 → Msg_表名，再查内容。

**Q: 为什么私聊只有8条？**
A: 早期使用了 MCP 的 search 工具，但表名匹配逻辑不完整。
正确做法：`表名 = Msg_ + MD5(wxid)`，直接查询整张表。

**Q: 大号私聊399条 vs 小号235条，为什么不一样？**
A: 不同微信账号的消息独立存储。完整画像需要合并两个账号的数据。

**Q: HMAC验证失败怎么办？**
A: wechat-decrypt 的 decrypt_db.py 对 SQLCipher 4 的 HMAC 验证逻辑
可能因页面参数差异而失败。跳过 HMAC 直接解密：
```python
# 跳过 HMAC，直接 AES-256-CBC 解密
# 每页 4096 字节，reserve=80
# IV = 页面倒数第80-96字节
# 第1页加密区 = 字节16 到 4096-80
```

---

## 相关文件

- `海浪袁总_完整对话.txt` — 634条完整记录（桌面）
- `海浪袁总_客户洞察报告.txt` — 五轮分析报告（桌面）
- `wechat_mcp_autostart.bat` — 开机自启脚本
