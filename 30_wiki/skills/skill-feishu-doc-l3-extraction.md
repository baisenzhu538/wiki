---
id: skill-feishu-doc-l3-extraction
title: 飞书文档 L3 严格模式提取 — SSO破墙+逐节点击+DOM提取
type: skill
status: reviewed
confidence: 0.95
trust_level: high
domain:
- feishu
- extraction
- browser-automation
- yitang
source_refs:
- capability/duanwangye/feishu-doc-l3-extraction
author: 段王爷（南帝）
reviewed_by: 欧阳锋
review_date: '2026-08-15'
related:
- '[[skill-duanwangye-feishu-publishing]]'
- '[[skill-duanwangye-wechat-extraction]]'
- '[[concept-feishu-api-pagination-trap]]'
- '[[concept-streaming-extraction-pattern]]'
tags:
- audience:executor
- scene:execution
- skill-level:advanced
discoverable_by:
- 飞书文档提取
- L3提取
- SSO登录
- 逐字稿提取
- yitang提取
- 微信扫码登录
- 单章节渲染
- CDP提取
---

# 飞书文档 L3 严格模式提取 — SSO破墙+逐节点击+DOM提取

> **一句话**：当飞书文档 TAT/UAT/MCP/API 全被 403 拦截（跨企业+文档级权限+SSO 登录墙）时，用 headless Chrome + 微信扫码登录获得登录态，再逐节点击目录 + DOM 提取，全自动拿到全文。

## 其他 Agent 何时调用我

| 场景 | 触发条件 | 示例 |
|------|---------|------|
| 直播逐字稿提取 | yitang.top/fs-doc 链接，需提取全文 | "提取Live259逐字稿存飞书" |
| 跨企业飞书文档 | 应用 token 403，OAuth 后仍 403 | "把这篇一堂文档抓下来" |
| SSO 登录墙文档 | 页面跳转 sso.yitang.top 登录 | 任何需要登录才能看的文档 |
| 单章节渲染文档 | 滚动不加载，点击目录才渲染 | 分段渲染的飞书富文档 |

## 我的核心能力

| 能力 | 状态 | 说明 |
|------|------|------|
| SSO 破墙 | ✅ | headless Chrome 微信扫码登录，agent 获得完整登录态 |
| 单章节渲染提取 | ✅ | 逐 ref 原生 click + DOM 提取 + 去重累积 |
| 混合提取 | ✅ | 初始 SSR + 逐节提取合并去重 |
| 发布 | ✅ | 合并后经 markdown_to_feishu 模板发布飞书 |

## 使用步骤（浓缩版）

### Step 0: 判定 —— 四连拒即切 L3

```
TAT + raw_content → 403
OAuth UAT + raw_content → 403（用户授权也绕不过 = 文档级权限）
TAT/UAT + MCP fetch-doc → forBidden / NETWORK:5002
SPA 内部 API → code:10 未登录
→ 🔴 切 L3，不要死磕 API
```

### Step 1: 启动 Chrome CDP

```bash
google-chrome --headless=new --disable-gpu --remote-debugging-port=9222 --no-sandbox \
  --user-data-dir=/tmp/chrome-yitang --window-size=1400,3000 about:blank
BIN=~/.hermes/hermes-agent/node_modules/agent-browser/bin/agent-browser-linux-x64
"$BIN" --cdp 9222 open "https://yitang.top/fs-doc/{ns}/{doc_id}"
```

### ⚠️ 跨平台适配（2026-08-16：WSL ↔ Windows 双轨）

**技能知识在 KDO 共享，执行层按平台适配：**

| 项 | WSL（Linux） | Windows |
|----|------------|---------|
| 浏览器 | `google-chrome`（系统已装） | **Edge** `"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe"`（Windows 无 Chrome） |
| agent-browser | `agent-browser-linux-x64` | `agent-browser-win32-x64.exe`（已复制到 `C:\Users\Administrator\AppData\Local\hermes\agent-browser\bin\`） |
| 临时目录 | `/tmp/` | `%TEMP%` 或自建 `C:\Users\Administrator\.hermes\tmp\` |
| 脚本 | bash | Git Bash（`C:\Program Files\Git\bin\bash.exe`）或 PowerShell |

Windows 启动 Edge CDP：
```powershell
# PowerShell
$Edge = "C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe"
& $Edge --headless=new --disable-gpu --remote-debugging-port=9222 --no-sandbox --user-data-dir="$env:TEMP\chrome-yitang" about:blank
# Git Bash 版
"/mnt/c/Program Files (x86)/Microsoft/Edge/Application/msedge.exe" --headless=new --disable-gpu --remote-debugging-port=9222 --no-sandbox --user-data-dir=/tmp/chrome-yitang about:blank &
```

### Step 2: 微信扫码破 SSO

1. 登录页含微信 iframe（`open.weixin.qq.com/connect/qrconnect`）
2. `"$BIN" --cdp 9222 screenshot /tmp/qr.png` → `MEDIA:/tmp/qr.png` 发给用户
3. 用户扫码 → 自动跳回文档页，登录态保留
4. ⚠️ 二维码 5 分钟过期 → `eval "window.location.reload()"` 重截

### Step 3: 判定渲染模式（10秒）

```bash
"$BIN" --cdp 9222 eval "window.scrollTo(0, document.body.scrollHeight); 'scrolled'"
sleep 2; # 对比 innerText.length
```
- 长度收缩 → **单章节渲染**（点击目录才加载），见 Step 4
- 长度增长 → 滚动懒加载，直接滚动提取

### Step 4: 逐节点击提取（单章节渲染）

```bash
"$BIN" --cdp 9222 snapshot -i   # → treeitem [ref=e3]~[ref=e36]
"$BIN" --cdp 9222 click e3; sleep 1.5   # ⚠️ 必须原生 click，JS dispatchEvent 对 Vue 无效
# 每轮点击后执行提取 JS（见模板），去重 key = (type, text[:150])
```

提取选择器要点：
- block 级元素：`[class*="docx-"]` 且 `className.indexOf('block docx-') >= 0`
- 类型正则含 `heading\d+`（**含 heading5**，表格内标题）
- 初始 SSR（打开页面后立即提取）+ 逐节提取合并去重

### Step 5: 合并清理发布

1. 合并去重 → 清理空白/重复/`- •` 双重符号
2. `markdown_to_feishu.py` 模板发布（50块/批，失败逐块重试）
3. `raw_content` 回读验证首尾 + 章节数

## 关键陷阱（P0）

| 陷阱 | 症状 | 解法 |
|------|------|------|
| JS 合成 click 对 Vue 无效 | dispatchEvent 静默不触发 | 必须用 agent-browser 原生 `click eN` |
| 滚动触发收缩 | scrollTo 后 innerText 变短 | 切点击模式 |
| eval 双层 JSON 转义 | json.loads 后仍是字符串 | `json.loads(json.loads(out))` |
| 只抓 h1-h3 漏内容 | 表格内 heading5 丢失 | 正则含 `heading\d+` 全级别 |
| 二维码 5 分钟过期 | 用户扫码失败 | reload 后重新截图 |
| 合并时重复 | 外层容器+内层 text 各提取一次 | 去重 key 用 (type, text[:150]) |

## 实战验证

- **Live259《爆炸式调研》逐字稿（2026-08-15）**：TAT/UAT/MCP/内部API 全 403 → 微信扫码登录 → 逐 ref 点击 33 标题 → 初始 SSR 103 + 逐节 510 → 合并 524 → 清理 503 → 发布飞书 507 blocks 零失败，37 章节 2.1 万字零遗漏
- 完整日志：`references/yitang-live259-session.md`

## 与其他技能分工

| 技能 | 范围 |
|------|------|
| skill-duanwangye-feishu-publishing | L1 SSR / L2 raw_content / 发布管线 |
| skill-duanwangye-wechat-extraction | 微信本地库提取 |
| **本技能** | **L3 严格模式：SSO + 单章节渲染 + CDP DOM 提取** |
