# 微信消息AI提取方案 — 全面评估报告

> 调研日期：2026-06-15 | 段王爷（南帝）  
> 决策问题：如何让AI助手（周伯通/段王爷）自动提取微信群重要消息，解决信息过载和遗漏？

---

## 一、底层原理：微信把一切存在你电脑上

微信电脑版（Windows/macOS）在你登录后，会将所有聊天记录存储在**本地加密数据库**中：

```
你的电脑
├── WeChat.exe / WeChat.app          ← 微信进程（内存中含解密密钥）
├── ~/Documents/WeChat Files/
│   ├── wxid_abc123/                  ← 你的大号
│   │   └── db_storage/
│   │       ├── message/message_0.db  ← 聊天记录（SQLCipher 4 加密）
│   │       ├── contact/contact.db    ← 联系人（加密）
│   │       └── session/session.db    ← 会话列表（加密）
│   └── wxid_def456/                  ← 你的小号
│       └── db_storage/               ← 另一套独立数据库
```

**核心事实：微信只在内存中持有解密密钥。** 只要能从微信进程内存中提取密钥，就能用标准 SQLCipher 库读取加密数据库——就像打开一个普通 SQLite 文件。

---

## 二、大号小号怎么处理？

### 登录场景分析

| 场景 | 电脑上的微信状态 | 数据库情况 |
|------|----------------|-----------|
| 手机登录大号 + 电脑登录大号 | 大号在运行，密钥在内存 | 大号的 DB 可解密 ✅ |
| 手机登录小号 + 电脑登录小号 | 小号在运行 | 小号的 DB 可解密 ✅ |
| **电脑同时登录大号+小号** | 两个进程都在运行 | **两个号都一次性解密 ✅** |
| 电脑只登大号，小号只在手机 | 只有大号 | 小号的手机端数据不在此方案范围 ❌ |

### 工具的初始化过程

```
wechat-cli init 的执行过程：
1. 扫描所有正在运行的微信进程
2. 发现 "WeChat.exe" (大号：wxid_abc123)
3. 发现 "WeChat.exe" (小号：wxid_def456) ← 如果有双开
4. 弹出提示："检测到 2 个账号，请选择："
   [1] wxid_abc123 (数据目录: ...)
   [2] wxid_def456 (数据目录: ...)
5. 提取所选账号的加密密钥 → 保存到 ~/.wechat-cli/
6. 后续所有命令自动用该密钥解密数据库

⚠️ 如需切换账号：再跑一次 wechat-cli init 选另一个号
```

**结论：大号小号都能处理，只要在电脑上登录过。**

---

## 三、方案对比：wechat-cli vs WeChat Decrypt

| 维度 | wechat-cli | WeChat Decrypt |
|------|-----------|---------------|
| **定位** | 轻量命令行工具 | 全功能数据工具箱 |
| **安装** | `npm install -g @canghe_ai/wechat-cli` | `git clone` + `pip install` |
| **复杂度** | ⭐ 简单（11条命令） | ⭐⭐⭐ 较复杂（20+个脚本） |
| **核心能力** | 查询聊天记录、搜索、导出 | 解密+导出+实时监听+语音转录+图片解密+MCP |
| **多账号** | 一次选一个号 | 一次提取所有号 |
| **实时监听** | `wechat-cli new-messages` | Web UI SSE + MCP Server |
| **MCP集成** | ❌ 需自己封装 | ✅ 内置 MCP Server |
| **输出格式** | JSON（AI友好） | JSON/CSV/HTML |
| **平台** | macOS arm64 + Windows(pip) + Linux | Windows/macOS/Linux 全平台 |
| **依赖** | Node.js 或 Python 3.10+ | Python 3.10+ + 多种原生库 |
| **Stars** | 新项目（2026年4月） | 3,930 ⭐ (2026年2月) |

---

## 四、风险评估（选项2：WeChat Decrypt MCP）

### 🔴 风险矩阵

| 风险类别 | 风险等级 | 具体描述 | 防范措施 |
|---------|---------|---------|---------|
| **封号风险** | 🟢 极低 | 工具只读本地文件，不经微信服务器、不模拟用户行为、不调用微信协议。技术上微信无法检测。 | 无 |
| **macOS重签名** | 🟡 低 | macOS SIP 禁止其他进程读微信内存，需重新签名添加调试权限。这是苹果开发者正常操作，不违法。 | 微信大版本更新后需重新签名 |
| **密钥泄露** | 🔴 中高 | `all_keys.json` / `~/.wechat-cli/` 明文存储解密密钥。任何拿到这个文件的人都可以解密你的所有聊天记录。 | ①文件权限设为 `chmod 600` ②加密磁盘 ③不备份到云端 |
| **本地数据库泄露** | 🔴 中高 | 解密后的数据库包含所有联系人、消息、文件路径。电脑被入侵时是首要目标。 | 用完即删解密库；不长期保留明文DB |
| **MCP Server 暴露** | 🟡 中 | MCP Server 默认监听 `localhost:5678`。同机其他用户/恶意软件可调用 API 读取消息。 | ①仅监听 127.0.0.1 ②加 token 认证 |
| **微信版本升级** | 🟡 中 | 微信 4.x→5.0 可能改变密钥存储位置或加密算法，导致工具暂时失效。 | 关注项目更新；等待社区适配 |
| **法律/ToS** | 🟡 低 | 微信用户协议可能禁止"逆向工程"。但重签名属于对自己设备上软件的修改，且仅读取个人数据。 | 仅个人使用，不商用 |
| **Windows Defender** | 🟠 中 | Windows 上内存扫描器可能被 Defender 标记为"潜在危险程序"。 | 添加白名单 |

### 🟢 不存在的风险（辟谣）

- ❌ **不会封号** — 没有网络请求，微信服务器完全无感知
- ❌ **不会修改微信数据** — 只读操作，不写数据库
- ❌ **不需要微信密码** — 密钥从内存提取，不涉及登录
- ❌ **不会影响微信正常使用** — 只是另外开一个 SQLite 连接读数据库
- ❌ **不会同步到云端** — 纯本地工具，零网络通信

---

## 五、MCP Server 工作原理（选项2核心）

```
┌─────────────────────────────────────────────┐
│                 你的电脑                      │
│                                              │
│  ┌──────────┐   内存读密钥   ┌─────────────┐ │
│  │ WeChat   │ ◄────────── │ MCP Server   │ │
│  │ 进程     │              │ (Python)     │ │
│  └──────────┘              │              │ │
│       │                    │ ①提取密钥    │ │
│       │ (加密DB文件)       │ ②解密DB      │ │
│       ▼                    │ ③SQL查询     │ │
│  ┌──────────┐              │ ④HTTP API    │ │
│  │ message  │ ◄────────── │ localhost:    │ │
│  │ _0.db    │  SQLCipher   │ 5678         │ │
│  └──────────┘  实时查询     └──────┬──────┘ │
│                                    │        │
└────────────────────────────────────┼────────┘
                                     │ MCP 协议
                                     ▼
                          ┌─────────────────┐
                          │ Claude / 周伯通  │
                          │                  │
                          │ "查一下最近3天   │
                          │  创业群的消息"   │
                          └─────────────────┘
```

**关键：MCP Server 只是 SQL 查询的中转站。** 它接收 Claude 的请求 → 查询本地加密数据库 → 返回结果。全程在你电脑上完成。

---

## 六、推荐实施路径

### 阶段一：快速验证（wechat-cli，30分钟）

```bash
# 1. 安装
npm install -g @canghe_ai/wechat-cli

# 2. 初始化（微信必须正在运行）
sudo wechat-cli init   # macOS
wechat-cli init        # Windows

# 3. 验证
wechat-cli sessions                    # 看能不能列出最近会话
wechat-cli search "精益" --limit 5     # 搜索关键词
wechat-cli history "XX群" --limit 20   # 看群消息

# 风险评估：✅ 零风险。这一步只验证技术可行性。
```

### 阶段二：接入AI（wechat-cli + cron，半天）

```bash
# 定时任务：每2小时扫描重要群的消息
wechat-cli new-messages --format json > /tmp/wechat_new.json

# 段王爷/周伯通读取 JSON → AI 总结 → 发飞书/存wiki
```

### 阶段三：深度集成（WeChat Decrypt MCP，1天）

```
1. pip install wechat-decrypt (或 git clone)
2. 提取密钥 → 解密DB → 启动MCP Server
3. Claude Code 配置: claude mcp add wechat -- python mcp_server.py
4. 周伯通可直接查询微信消息
5. 风险：需要保护 all_keys.json 文件安全
```

---

## 七、安全基线建议

如果选择选项2，必须做到：

```bash
# 1. 密钥文件最严格权限
chmod 600 ~/.wechat-cli/*.json
chmod 600 all_keys.json

# 2. 不备份密钥到云端（iCloud/Dropbox 等）
# 在 .gitignore / .cloudignore 中排除密钥文件

# 3. MCP Server 仅绑定本地
# 确保配置中 host=127.0.0.1（不是 0.0.0.0）

# 4. 定期清理解密缓存
# 解密后的临时数据库用完即删

# 5. 电脑本身安全
# 屏幕锁、全盘加密、系统防火墙
```

---

## 八、最终建议

| 如果你... | 推荐方案 |
|----------|---------|
| 想先试试水，不折腾 | **阶段一**：wechat-cli，30分钟跑通 |
| 希望AI定期总结群消息 | **阶段二**：wechat-cli + cron 定时查询 → 段王爷总结 |
| 想AI深度参与，随时查微信 | **阶段三**：WeChat Decrypt MCP |
| 担心安全风险 | 先用 wechat-cli，感受一下再决定是否升级 |

---

## 九、对比：飞书 vs 微信

| 维度 | 飞书 | 微信 |
|------|------|------|
| API开放性 | ✅ 完整开放API | ❌ 无个人API |
| 数据可编程性 | ✅ tenant_token直接读 | ⚠️ 需内存提取密钥 |
| AI集成 | ✅ 原生支持 | ⚠️ 需本地解密中转 |
| 封号风险 | 无 | 🟢 极低（但需注意重签名） |
| 推荐策略 | 能用飞书的群迁移到飞书 | 微信保留，用本报告方案补充 |

---

> 📎 参考链接:
> - wechat-cli: https://github.com/freestylefly/wechat-cli
> - WeChat Decrypt: https://github.com/ylytdeng/wechat-decrypt
> - WeChat MCP Server: https://github.com/SsssssSynqa/WeChat-ClaudeCode-MCP
