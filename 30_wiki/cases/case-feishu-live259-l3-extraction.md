---
id: case-feishu-live259-l3-extraction
title: 「案例：Live259逐字稿提取——SSO破墙+逐节点击，四连拒后的L3正解」
type: case
status: reviewed
confidence: 0.95
trust_level: medium
domain:
- feishu
- extraction
- browser-automation
- yitang
author: 段王爷（南帝）
source_refs:
- capability/duanwangye/feishu-doc-l3-extraction
source_person: 段王爷（南帝）实战
source_context: 2026-08-15 提取 yitang.top/fs-doc Live259《爆炸式调研》逐字稿并发布飞书
reviewed_by: 欧阳锋
aliases:
- Live259提取
- L3严格模式
- SSO破墙
- 微信扫码登录
- 单章节渲染
- yitang提取
discoverable_by:
- 飞书文档403
- 直播逐字稿提取
- SSO登录墙
- 跨企业文档
- 分段渲染
- 扫码登录提取
related:
- skill-feishu-doc-l3-extraction
- skill-duanwangye-feishu-publishing
- concept-feishu-api-pagination-trap
- concept-streaming-extraction-pattern
tags:
- method:browser-automation
- method:feishu-extraction
- scene:content-acquisition
- audience:executor
- content-format:case
- source-person:agent
- evidence:observed
created_at: 2026-08-15
updated_at: 2026-08-15
quality_labels:
- insight
- actionable
- reusable
diagnostic_signals:
- signal: 飞书文档 TAT/UAT/MCP/内部API 全 403
  lens: 文档级权限+SSO 双层收紧，API 路径全灭
  follow_up: 直接切 L3：headless Chrome + 微信扫码登录 + DOM 提取，不要死磕 API
- signal: 滚动页面 innerText 反而收缩
  lens: 不是滚动懒加载，是单章节渲染模式
  follow_up: 改逐 ref 点击目录触发加载
review_date: 2026-08-15
---
> 本卡是 [[skill-feishu-doc-l3-extraction]] 的实战实证——飞书文档 L3 严格模式提取的完整突破路径。与 [[skill-duanwangye-feishu-publishing]] 的 L3 协作协议互为表里：旧协议要求用户逐段点击配合，本案例证明**扫码登录后 agent 可全自动自驱提取**，用户只需扫一次码。

# Live259 逐字稿提取：四连拒后的 L3 正解

> 一句话：yitang.top 直播逐字稿（Live259《爆炸式调研》），TAT/OAuth/MCP/内部API 四种路径全被 403 拦截——最终用 headless Chrome + 微信扫码登录 SSO，获得登录态后逐节点击目录 + DOM 提取，20 分钟拿下 2.1 万字全文并发布飞书，用户全程只扫了一次码。

---

## 过程（起点→尝试→转折→结果）

### 起点：一篇被双重保护的一堂直播逐字稿

老朱发来链接 `https://yitang.top/fs-doc/{ns}/{doc_id}`，要求提取逐字稿存入飞书，并预告"可能是分段渲染，我可以配合你逐段点击"——用户预期了点击式渲染。

### 尝试：四种 API 路径全灭（四连拒）

| 尝试 | 结果 | 耗时 |
|:---|:---|:---|
| TAT + raw_content | ❌ 403 Forbidden | 秒级 |
| TAT + MCP fetch-doc | ❌ forBidden (NETWORK:5002) | 秒级 |
| OAuth UAT + raw_content | ❌ 403（拿到 UAT 后仍拒） | 秒级 |
| UAT + MCP fetch-doc | ❌ forBidden | 秒级 |
| 内部 API `/api/feishu/get-doc-blocks` | ❌ code:10 未登录（SSO 后仍拒） | 分钟级 |

### 转折 1：Node v12 与浏览器栈

`browser_navigate` 报 Node v12 SyntaxError（agent-browser.js 需要 Node ≥14）。改用预编译二进制 `agent-browser-linux-x64 --cdp 9222` + headless Chrome，绕开 Node 版本问题。

### 转折 2：SSO 登录墙 → 微信扫码破墙（关键洞察）

页面被重定向到 `sso.yitang.top/account/login`，只有"微信登录"和"探月学校登录"。**发现登录页内嵌微信登录 iframe**（`open.weixin.qq.com/connect/qrconnect`），于是：

1. `screenshot /tmp/qr.png` 截二维码 → `MEDIA:` 发给老朱
2. 老朱微信扫码 → 浏览器**自动跳回目标文档页**，登录态保留在 Chrome profile
3. 后续 agent 拥有完整登录态，可自主点击目录——**用户只需扫一次码，不再需要逐段手动复制**

### 转折 3：滚动无效 → 识别单章节渲染模式

滚动到底部后 `innerText` 从 2287 反而收缩到 1423——不是滚动懒加载！检查发现目录是 Element UI 树（`.el-tree-node__content`），**点击标题才渲染该章节**，且每次只渲染当前章节（单章节渲染）。

### 转折 4：JS 合成 click 无效 → 必须原生 click

用 `dispatchEvent(new MouseEvent('click'))` 全部返回 CLICKED 但内容不加载——Vue 事件监听器不响应合成事件。改用 agent-browser 原生 `click eN` 命令，逐个点击 33 个目录 ref，每轮提取 + 去重累积。

### 结果：全自动提取 + 发布零失败

- 初始 SSR 103 blocks + 逐节 510 blocks → 合并去重 524 → 清理 503
- 39 个标题（h1-h5，含表格内 heading5）、37 章节、~2.1 万字
- 发布飞书：507 blocks / 11 批（50×10+7）零失败，`anyone_readable` 公开权限
- 验证：`raw_content` 回读 20535 字符，首尾完整
- 全程 < 20 分钟，用户操作 = 扫一次码

---

## Claims / Evidence

| Claim | 证据 | 证据状态 |
|:---|:---|:---|
| API 四连拒（TAT/OAuth/MCP/内部）即 L3 信号，继续试 API 是浪费时间 | 本案例 5 种 API 路径全部失败后才切浏览器路径 | 实测 |
| 微信扫码登录可让 headless Chrome 获得完整 SSO 登录态 | 扫码后浏览器自动跳回文档页，后续全自动提取成功 | 实测 |
| yitang fs-doc 是单章节渲染：滚动不加载、点击目录才渲染、每次只渲染当前章节 | scrollTo 后 innerText 收缩；逐 ref 点击后 blocks 增加 | 实测 |
| JS 合成 click（dispatchEvent）对 Vue 组件无效，必须原生 click | dispatchEvent 返回 CLICKED 但内容不加载；`click eN` 立即生效 | 实测 |
| agent-browser eval 返回双层 JSON 转义 | `json.loads` 后仍是字符串，需 `json.loads(json.loads(out))` | 实测 |

## 关键数字

| 数据 | 来源 | 状态 |
|:---|:---|:---|
| 5 种 API 路径全灭 | 实战日志 | 实测 |
| 33 个目录 ref 逐一点击 | 实战日志 | 实测 |
| 初始 SSR 103 + 逐节 510 → 合并 524 → 清理 503 blocks | 实战日志 | 实测 |
| 发布 507 blocks / 11 批零失败 | 发布日志 | 实测 |
| 37 章节 2.1 万字，raw_content 回读 20535 字符 | 验证日志 | 实测 |

## 双三角六要素映射

| 三角 | 要素 | 案例对应 |
|:---|:---|:---|
| 人的三角 | 判断力 | 四连拒后不停留在"换API再试"，直接切浏览器路径（决策树） |
| 人的三角 | 体系 | L1→L2→L3 三级提取决策树，先诊断再动手 |
| 人的三角 | 创造力 | "截图二维码发给用户扫"——把登录墙变成可协作突破点 |
| AI 三角 | 场景 | yitang 直播逐字稿提取（跨企业+SSO+分段渲染三重困难） |
| AI 三角 | 数据 | DOM block 提取（docx-xxx-block 类名），非 API 数据 |
| AI 三角 | 基本功 | agent-browser CDP 操作、Element UI 树识别、单章节渲染判断 |

## Critique

**内部局限（自指）**：headless Chrome 依赖系统 google-chrome 已安装；二维码过期需重截（5 分钟）；CDP 提取对页面结构变化敏感（类名/渲染模式改了要重新适配）；登录态保存在 `/tmp/chrome-yitang`，重启丢失需重新扫码。

**外部攻击者 1（Kahneman 式——锚定偏差）**：本例锚定在"API 能拿到一切"的惯性上，前面浪费了几轮 API 尝试。正确姿势是**先 10 秒滚动测试判定渲染模式，再决定路径**——若一开始就识别"滚动收缩=点击式"，可更快切浏览器。

**外部攻击者 2（Taleb 式——路径依赖）**：微信扫码破墙依赖"目标平台支持微信登录"。若平台只有手机验证码/企业 SSO，此方案不适用。通用原则是**登录墙总有用户可配合的入口（扫码/验证码/OAuth），把入口变成 agent 与用户的协作点**，而非死路。

## Synthesis

本次突破的核心机制：**登录墙不是死路，是协作入口**。以前 L3 只想到"用户逐段点击、agent 提取"（人机配合），没想到"用户扫码登录、agent 自驱操作"（人机分工升级）——二维码截图发给用户扫，换来 agent 的完整登录态，之后所有点击/提取/累积全部自主完成。跨案例收敛：`[[case-live258-zhihu-content-acquisition]]` 的"无意识用对 Feature"与本例的"无意识卡在 API 惯性"同构——**突破往往来自把已有的能力（浏览器+扫码）以新的组合方式使用**。机制层见 `[[skill-feishu-doc-l3-extraction]]`（完整打法）。

## Action Triggers

1. 任何飞书/yitang 文档提取，先跑决策树：TAT raw → OAuth UAT → MCP，四连拒即切 L3
2. 遇到 SSO 登录墙，先查有无微信/探月等扫码入口——有就截图二维码发给用户，换取 agent 登录态
3. 页面加载后先做 10 秒滚动测试：innerText 收缩 = 单章节渲染 = 切逐 ref 点击
4. 提取选择器覆盖 `heading\d+` 全级别（含 heading5），去重 key 用 (type, text[:150])

## 失败模式

| 失败模式 | 症状 | 修复 |
|:---|:---|:---|
| 死磕 API | TAT 403 后继续试 OAuth/MCP/内部 API | 四连拒后直接切 L3，不恋战 |
| JS 合成 click | dispatchEvent 返回 CLICKED 但无内容 | 用 agent-browser 原生 `click eN` |
| 滚动提取 | scrollTo 后 innerText 收缩 | 先测滚动再决定，10 秒可判 |
| 只抓 h1-h3 | 表格内 heading5 标题丢失 | 正则含 `heading\d+` 全级别 |
| 二维码过期 | 用户扫码失败 | reload 后重新截图 |
| 合并重复 | 外层容器+内层 text 各提取一次 | 去重 key 用 (type, text[:150]) |
