# 微信视频号偶遇采集全自动链路 · 技术文档

> 一句话：**手机复制视频号链接 → 粘贴发送 → 10 分钟内电脑自动完成 解析→下载→转写→知识化 → 进 `00_inbox/wechat-collect/`**，全程零人工、零电脑操作。
> 状态：🟢 生产可用（2026-08-17/18 两次实测闭环）
> 顶层文档：`70_product/projects/proj_20260816_wechat-collect-顶层文档.md`
> 方法论：楚门「偶遇自动采集五通道」通道②（`framework-serendipity-five-channels`）

---

## 一、用户怎么用（唯一操作）

```
手机上：视频号 → 分享 → 复制链接 → 发送到 文件传输助手 / 任意群
        ↑ 就这一个动作，其余全自动
```

> ⚠️ **必须"复制链接"转发**（链接形如 `https://weixin.qq.com/sph/xxxx`）。
> "直接转发卡片"微信不提供解析入口，无法全自动（见 §五 边界）。

---

## 二、系统链路（每 10 分钟自动跑一轮）

```
手机复制链接 → 发送到微信
  ↓（PC 微信在线时消息同步进本地数据库）
[计划任务 wechat-link-monitor · 每 10 分钟]
  ├─ 1. 解密微信 4.x 数据库（SQLCipher 4，密钥复用，约 10 秒）
  ├─ 2. 读新消息（ZSTD 解压）→ 提取链接
  │      · sph 分享链接 → parse_sph 解析直链
  │      · 视频号卡片(XML) → 提取自带直链（加密，需解密，见 §五）
  │      · 公众号链接 → 抓取文章正文
  ├─ 3. 下载（直连不走代理）
  ├─ 4. WSL faster-whisper GPU 转写 → 逐字稿
  └─ 5. LLM 三层次知识化（事实/规律/洞察）→ 研究文档
       ↓ 全部落
00_inbox/wechat-collect/
  ├─ src_wechat_*.md              # 逐字稿
  ├─ src_wechat_article_*.md      # 公众号文章
  └─ knowledge/case-wechat-*.md   # 三层次研究文档（inbox 待转正）
```

**铁律**：产物第一站必须是 `00_inbox/`，未经 ingest/validate 不得入 `10_raw/` 和 `30_wiki/`（用户纠偏）。

---

## 三、组件清单

| 组件 | 路径 | 作用 |
|:--|:--|:--|
| 监控脚本 | `40_outputs/code/scripts/wechat_link_monitor.py`（源：`kdo-tools/`） | 全链路主控：解密→提取→解析→下载→转写→知识化 |
| 知识化脚本 | `40_outputs/code/scripts/wechat_knowledge.py` | LLM 三层次总结（DeepSeek v4-flash），覆盖保护+跳过已知识化+NO_PROXY |
| 定向采集 CLI | `40_outputs/code/scripts/collect_wechat.py` | 方式二博主定向（--author）+ 本地导入（--import-local） |
| Cookie 提取 | `40_outputs/code/scripts/yuanbao_cookie_extract.py` | CDP 从已登录元宝页面提取全量 Cookie（过期后重建） |
| 解析服务 | `C:\Users\Administrator\tools\wx_channels_download_bin\wx_video_download.exe`（ltaoo v260817） | 本地 API 127.0.0.1:2022：parse_sph（链接→直链）+ MCP（fetch_content/download_content 自动解密） |
| 微信解密 | `C:\Users\Administrator\wechat-decrypt\`（段王爷资产复用） | SQLCipher 4 数据库解密（passphrase + PBKDF2） |
| WSL 转写 | `/home/dministrator/wechat-collect/transcribe.py` | faster-whisper（tiny，GPU CUDA，CPU fallback） |
| 计划任务 | `wx-channels-download`（登录自启）+ `wechat-link-monitor`（每 10 分钟） | 无人值守固化 |

---

## 四、部署清单（从零到可用，约 30 分钟）

### 4.1 微信数据库解密（一次性）
```bash
# 依赖：微信 4.x 已登录运行（进程 Weixin.exe）
pip install pycryptodome
# 密钥：复用 C:\Users\Administrator\wechat-decrypt\build_keys.py 的 PASSPHRASE
# 验证（当前账号 19/19 通过）：
cd C:\Users\Administrator\wechat-decrypt && python _build_and_decrypt.py
```

### 4.2 解析服务（一次性）
```bash
# 下载 ltaoo/wx_channels_download v260817 Windows 包（gh-proxy 镜像）
# 解压到 C:\Users\Administrator\tools\wx_channels_download_bin\
# 配置 config.yaml 的 cloudflare.sphCookie（见 4.3）
# 启动（计划任务已配登录自启）：
./wx_video_download.exe   # API 127.0.0.1:2022 / 代理 2023 / MCP /mcp
```

### 4.3 元宝 Cookie（约 1 个月有效，过期重建）
```bash
# ① 启动带调试端口的 Edge，打开元宝（profile 复用登录态）：
msedge --remote-debugging-port=9222 --remote-allow-origins=* \
  --user-data-dir=C:\Users\Administrator\tools\edge-debug-profile https://yuanbao.tencent.com/
# ② 用户微信扫码登录（仅首次；profile 保存后免登）
# ③ 提取全量 Cookie 写入 config.yaml：
python 40_outputs/code/scripts/yuanbao_cookie_extract.py
# ④ 重启 wx_video_download 使配置生效（改配置必须重启）
```
**要点**：Cookie 必须全量（含 `.tencent.com` 域的 `hy_token`，共 13 个）。只填主 token 会返回"此内容暂时无法播放"。

### 4.4 计划任务（一次性）
```powershell
# 解析服务登录自启
Register-ScheduledTask -TaskName 'wx-channels-download' -Action (New-ScheduledTaskAction -Execute 'C:\Users\Administrator\tools\wx_channels_download_bin\wx_video_download.exe') -Trigger (New-ScheduledTaskTrigger -AtLogOn) -Principal (New-ScheduledTaskPrincipal -UserId 'Administrator' -LogonType Interactive -RunLevel Highest) -Force
# 监控每 10 分钟
Register-ScheduledTask -TaskName 'wechat-link-monitor' -Action (New-ScheduledTaskAction -Execute 'C:\Program Files\Python312\python.exe' -Argument 'C:\Users\Administrator\Desktop\wiki\kdo-tools\wechat_link_monitor.py') -Trigger (New-ScheduledTaskTrigger -Once -At (Get-Date) -RepetitionInterval (New-TimeSpan -Minutes 10)) -Force
```

### 4.5 验证（端到端冒烟）
```bash
# 手动跑一轮（正常输出：解密→链接→解析→下载→转写→知识化）
python kdo-tools/wechat_link_monitor.py
# 产物检查
ls 00_inbox/wechat-collect/ 00_inbox/wechat-collect/knowledge/
```

---

## 五、边界与已知限制（诚实清单）

| 场景 | 可用性 | 说明 |
|:--|:--|:--|
| 复制链接转发（sph 短链） | ✅ 全自动 | 主链路，两次实测（WorkBuddy 146s/99s） |
| 公众号链接转发 | ✅ 全自动 | 抓文章正文入库（正则已支持 /s/ 与 /s? 两种格式） |
| 直接转发卡片（无链接） | ⚠️ 需电脑播放 | 微信卡片只有加密视频数据，解密密钥仅播放时暴露——wx_channels_download 代理(2023)拦截自动下载，人需在电脑前（非自动化，兜底） |
| 元宝 Cookie 过期 | ⚠️ 每月重建 | 重新扫码 + CDP 提取（4.3） |
| 微信反爬变化 | ⚠️ 随时可能 | parse_sph 自持登录态相对稳定；失效回退播放拦截 |

---

## 六、运维手册

### 6.1 日常检查
- 产物：`00_inbox/wechat-collect/` 有逐字稿 + knowledge/
- 计划任务：`schtasks /query /tn wechat-link-monitor`
- 解析服务：`curl "http://127.0.0.1:2022/api/channels/parse_sph?url=<测试sph链接>"` → code:0

### 6.2 故障排查表

| 症状 | 根因 | 修复 |
|:--|:--|:--|
| "no yuanbao cookie" | Cookie 未配置/清空 | 重配 4.3 全量 Cookie |
| "此内容暂时无法播放" | Cookie 不全（缺 hy_token）或过期 | 重跑 4.3 提取全量 13 个 |
| 下载慢/中断 | MITM 系统代理干扰 | 脚本已无代理直连（ProxyHandler({})），确认下载目录文件大小正常 |
| 转写失败 Invalid data | 下载文件是加密视频（卡片直链） | 该链接走播放拦截（§五）；sph 链接的直链是非加密版 |
| LLM 知识化失败 | 系统代理拦 DeepSeek / 瞬时抖动 | 脚本已 NO_PROXY；重跑 `wechat_knowledge.py <文件>` 即可 |
| 数据库解密失败 | 微信未运行 / 重装微信密钥变 | 微信登录后重跑 `_build_and_decrypt.py` |
| 监控无新链接 | seen_links.txt 已记 / PC 微信未同步 | 查 seen；确认 PC 微信在线（消息实时同步）；微信重启触发 WAL 落盘 |
| WAL 未合并读不到新消息 | 微信运行中 WAL 未 checkpoint | 重启微信（退出→打开）立即合并；或等空闲自动落盘 |

### 6.3 恢复流程（重装/换机）
1. 4.1-4.4 重建（密钥从旧 build_keys.py 带过来）
2. 元宝 Cookie 重新扫码提取（4.3）
3. 冒烟验证（4.5）

---

## 七、相关资产

| 资产 | 路径 |
|:--|:--|
| 顶层文档 | `70_product/projects/proj_20260816_wechat-collect-顶层文档.md` |
| 调研报告 | `00_inbox/视频号逐字稿调研/视频号逐字稿自动化工作流-爆炸式建模.md` |
| 工具卡 | `30_wiki/tools/tool-wechat-transcript-automation-workflow.md` |
| 偶遇框架 | `30_wiki/frameworks/framework-serendipity-five-channels.md` |
| Skill | `.claude/skills/wechat-serendipity-collect/` |
| 复盘 | `桌面/agent复盘/huangyaoshi/daily-context/2026-08-17.md` |

*黄药师 · 2026-08-18 更新（主链路：复制链接转发全自动）*
