---
id: case-feishu-minutes-extraction-attempt
title: 「案例：飞书妙记逐字稿提取尝试——二维码过期未成，但定位了 Windows 侧浏览器正解」
type: case
status: draft
reviewed_by: 待审（欧阳锋）
confidence: 0.85
trust_level: observed
language: zh-CN
created_at: 2026-08-16
updated_at: 2026-08-16
domain:
- feishu
- extraction
- browser-automation
- infrastructure
aliases:
- 妙记提取
- minutes提取
- 二维码过期
- 飞书扫码登录
- Windows CDP
- playwright chromium
source_person: 段王爷（南帝）实战
source_context: 2026-08-16 尝试提取 yitanger.feishu.cn 妙记逐字稿 obcnetutt68o4r42697igyye，登录二维码过期未完成，但完整验证了 Windows 侧浏览器方案
source_refs:
- capability/duanwangye/feishu-doc-l3-extraction
related:
- '[[skill-feishu-doc-l3-extraction]]'
- '[[case-feishu-live259-l3-extraction]]'
- '[[dk-mcp-pythonpath-pollution]]'
tags:
- method:browser-automation
- method:feishu-extraction
- scene:content-acquisition
- audience:executor
- source-person:agent
- evidence:observed
discoverable_by:
- 飞书妙记提取
- minutes逐字稿
- 二维码过期
- Windows浏览器方案
- playwright chromium CDP
---

# 飞书妙记逐字稿提取：二维码过期未成，但 Windows 侧浏览器正解已定位

> 一句话：尝试提取飞书妙记（minutes）逐字稿，API 缺 scope、页面有登录墙，二维码截图发给用户后 5 分钟内过期，本次未提取成功——但完整验证了 **ms-playwright chromium + playwright-core connectOverCDP** 是 Windows 侧唯一可靠浏览器路径，为下次备好了全套方法。

## 过程（起点→尝试→转折→结果）

### 起点：妙记链接
老朱发来 `https://yitanger.feishu.cn/minutes/obcnetutt68o4r42697igyye`，要求提取逐字稿。

### 尝试 1：API 路径 → 缺 scope
- TAT 获取成功 → `/open-apis/minutes/v1/minutes/{token}` 全部 400
- 错误体明确：需 `minutes:minutes:readonly` / `minutes:minutes.transcript:export` 等 scope，应用未开通
- **结论：API 不可用（缺权限，非绕过可解）**

### 尝试 2：诊断页面 → 确认登录墙
- urllib 抓 HTML：92KB，含 `suite-passport` meta + login JS，无 SSR transcript 数据
- **结论：妙记无 SSR，必须登录态**

### 尝试 3：浏览器路径 → 连踩三坑后找到正解
| 尝试 | 结果 |
|:--|:--|
| Edge headless (`msedge.exe --headless`) | ❌ exit 234，CDP 端口拒连，仅 webview2 进程 |
| agent-browser npx 安装 | ❌ npm/pnpm 都下载 `agent-browser-darwin-arm64`（平台检测错） |
| agent-browser-win32-x64.exe（已复制副本） | ❌ 报 `Daemon not found`（缺 daemon 核心） |
| **ms-playwright chromium-1217 + playwright-core** | ✅ **成功启动 CDP**（Chrome/147），打开登录页，截到二维码 |

### 转折：二维码截图成功，但用户扫码时已过期
- 登录页确认：飞书移动端扫码（canvas 184x184，容器 `new-scan-qrcode-container`）
- 二维码 clip 截图成功 → `MEDIA:` 发给老朱
- 老朱回复"过期了，算了下次再试"——**未提取成功**

### 结果：失败但有全套方法沉淀
- skill `feishu-doc-l3-extraction` 更新：Windows 首选 CDP 方案 + `references/feishu-minutes-extraction.md`
- 脚本沉淀：`scripts/start_chrome.py` + `scripts/minutes_extract.py`（一体化）
- 本 case 卡注册 KDO

## Claims / Evidence

| Claim | 证据 | 证据状态 |
|:--|:--|:--|
| 飞书妙记 API 需要专属 scope（元数据与 transcript 两组不同） | 99991672 错误体列出两组 scope | 实测 |
| 妙记页面无 SSR transcript，未登录必 302 到 accounts.feishu.cn | urllib 抓包 92KB 仅 passport 框架 | 实测 |
| Edge headless 在本机起不来（exit 234） | 多次尝试 CDP 端口均拒连 | 实测 |
| agent-browser npm 安装平台检测错（下载 darwin-arm64） | npm/pnpm 两次安装均为 darwin | 实测 |
| **ms-playwright chromium-1217 是 Windows 侧可靠浏览器** | subprocess.Popen 启动成功，CDP 返回 Chrome/147 | 实测 |
| 飞书登录页用 canvas 画二维码（非 img），clip 截图需取 canvas rect | canvas 184x184 定位成功 | 实测 |

## 关键数字

| 数据 | 来源 |
|:--|:--|
| 妙记 API 3 个端点全部 400 | 实测 |
| HTML 92KB 无 transcript | 实测 |
| chromium Chrome/147.0.7727.15 | CDP 返回 |
| 二维码 184x184 | DOM |
| 尝试 3 种浏览器方案后才成功 | 实测 |

## 失败模式

| 失败模式 | 症状 | 修复 |
|:--|:--|:--|
| API 缺 scope 仍死磕 | 反复 400 | 看错误体的 scope 列表，直接放弃 API 走浏览器 |
| 用 Edge headless | exit 234 | 直接用 ms-playwright chromium |
| npx 装 agent-browser | 下载 darwin-arm64 | 不要用 npx，用 playwright-core |
| 二维码截图用容器元素 | clip 尺寸异常 | 用 `document.querySelector('canvas')` 的 rect |
| **二维码 5 分钟过期** | 用户来不及时扫 | 下次先确认用户就绪再发码；或用 `--user-data-dir` 保留登录态，扫码一次长期复用 |

## Synthesis

失败案例的隐藏价值：**把"不可能"清单走完了**。Edge 不行、agent-browser 不行、npx 不行——最终确认 `ms-playwright chromium` 是 Windows 侧唯一可用路径。下次同类任务（任何需要浏览器登录的飞书内容）直接复用，无需再踩三坑。登录态复用机制（`--user-data-dir` 保留）意味着扫码成功一次后，同域文档长期免扫码。

## Action Triggers

1. 遇到飞书妙记 → 先 API（看 scope 错误）→ 直接切浏览器，不恋战
2. Windows 侧浏览器 = ms-playwright chromium + playwright-core connectOverCDP（不用 Edge/agent-browser）
3. 发二维码前先确认用户在线就绪，避免 5 分钟过期
4. 扫码成功后保留 `--user-data-dir` profile，同域复用登录态
