---
session_id: duanwangye-2026-08-24
agent_id: duanwangye
date: 2026-08-24
created_at: 2026-08-24T01:23:22.329169+00:00
updated_at: 2026-08-24T01:23:22.329169+00:00
git_head: 8151d7726
content_hash: e31d4a317770
---

# duanwangye · 2026-08-24

---
session_id: duanwangye-2026-08-24
agent_id: duanwangye
date: 2026-08-24
created_at: 2026-08-23T16:30:31.669965+00:00
updated_at: 2026-08-23T16:30:31.669965+00:00
git_head: df050a803
content_hash: 5a3f8dc84934
---

# duanwangye · 2026-08-24

## 差异栏（第1章）
本次 vs 上次：上次是 L1 直达纯 API 提取（3秒），本次是 L3 全链路（OAuth 403→CDP→扫码→单章节逐节点提取→清理→发布）。新视角：同一类任务（Live 逐字稿）不同文档权限天差地别——Live84/86 可 TAT 直读，Live260 必须扫码，不能因上次成功就默认下次简单。复发模式：headless Chrome 微信 iframe 不渲染二维码（上次 Live259 是 WSL 无此问题，本次 Windows headless 踩坑）。

## 概要
直播Live260《AI口喷必修课》逐字稿：TAT/UAT/MCP 全 403 → L3 严格模式（有头 Chrome CDP + 微信扫码）→ 单章节渲染 45 目录节点逐节点原生点击 → 803 blocks 合并 → 清理 37,877 字 → 发布飞书 241 blocks 零失败 → 回读验证完整。

## 关键决策
| 决策 | 理由 | 结果 |
|------|------|------|
| TAT/UAT/MCP 全 403 后直接切 L3 | 决策树顺序：先试所有 API 通道再进浏览器 | ✅ 避免浪费时间重试 |
| headless→有头模式切换 | 微信 qrconnect 在 headless 下 iframe 不渲染二维码（canvas 一直 false） | ✅ 有头模式可渲染，但 iframe 截图仍空 → 用页面内 fetch 拿二维码 img |
| 二维码获取用页面内 fetch（带 cookie）而非 curl | curl 直接下载返回 size 0（需要 referer/cookie） | ✅ 470x470 二维码成功 |
| 逐节点提取用 playwright 原生 click | JS dispatchEvent / el.click() 对 Vue 无效（技能陷阱），首次循环 cur 始终 531 不变 | ✅ 原生 click 后内容增长 |
| 去重 key 用 (type, text[:150]) | 外层容器+内层 text 重复（288 重复） | ✅ 803 合并成功 |
| callout 与 text 重复单独清理 | callout 大段（518字）与后续 text 完全重复 | ✅ 发布 241 blocks 干净 |

## 思维盲点
1. 盲点：headless Chrome 微信 iframe 不渲染二维码——第一次截图发给用户是空白，用户反馈后才排查。为什么漏掉？技能里 WSL 场景（Live259）没有此问题，Windows headless 是新环境坑。下次：Windows 下微信扫码登录直接用有头模式+页面内 fetch 二维码，不要先 headless 截图。
2. 盲点：第一次提取循环用 JS click 静默失败（cur 始终 531，+0 累积），浪费一整轮。为什么漏掉？技能已写明'JS dispatchEvent 对 Vue 无效，必须原生 click'，但写成 .cjs 脚本时用了 evaluate click。下次：提取脚本直接上 playwright locator.click()。
3. 盲点：二维码发给用户后未确认用户是否就绪，第一张码发出时用户离开。为什么漏掉？技能有'发码前先确认用户就绪'警示，但急着推进忘了。下次：发码前问一句。

## 顿悟
1. 微信 qrconnect 页面可以直接打开（open.weixin.qq.com/connect/qrconnect?appid=...），iframe 渲染不了时绕开 iframe 直接访问二维码页面拿 img src（open.weixin.qq.com/connect/qrcode/xxx），这是 Windows L3 扫码的稳定通道。
2. 单章节渲染文档的'目录点击'不一定需要逐个点完——先滚动测试判断模式（滚动收缩=单章节），再决定用原生点击累积，节省无效尝试。

## 过程资产
- C:\Users\Administrator\Desktop\wiki\00_inbox\直播Live260-AI口喷必修课-逐字稿.md（本地归档）
- 飞书文档 https://yitanger.feishu.cn/docx/S7NWdp9HgoV7xoxjhfqcwov0nzc（已发布，anyone_readable）
- 00_inbox 去重：删除连字符版成瘾文件，保留冒号版

## 元反思
下次 Live 提取：①先 API 三通道探测（TAT/UAT/MCP）②全 403 → L3 ③Windows 下扫码直接有头 Chrome + 页面内 fetch 二维码（不要 headless 截图）④确认用户就绪再发码 ⑤单章节渲染用 playwright 原生 click 累积。知识检索审视：本次全程依赖技能 feishu-doc-l3-extraction，检索了其 references/third-party-feishu-viewers.md 确认 doc_id 提取方式，纠正了'第二段是 doc_id'的认知（实际第三段才是）。

## Truman复盘
### 逐轮映射
| 轮次 | 人做什么 | 双三角 | AI做什么 | 双三角 |
|------|---------|--------|---------|--------|
| 1 | 发文档链接 | 场景 | API 三通道探测 | 基本功 |
| 2 | OAuth 授权 | 信任 | UAT 读取 | 数据 |
| 3 | 微信扫码 | 信任/场景 | CDP 提取 | 基本功 |
| 4 | 反馈二维码空白 | 审美/校验 | 排查+有头模式+fetch 二维码 | 场景 |
| 5 | 反馈失效重来 | 校验 | 重新生成 | 执行 |
| 6 | 确认已扫 | 场景 | 检测登录+提取+发布+验证 | 执行 |

### 飞轮效应
加速了 L3 提取闭环：Windows 扫码路径（有头+fetch 二维码）沉淀后，下次 Live 提取从 30+ 分钟压缩到 10 分钟以内；技能更新让飞轮更快。

### 对照实验
无AI：用户手动复制逐字稿需 40 分钟+（43 章节逐个复制）；无用户：AI 无法扫码登录（文档权限硬墙）；合在一起：约 15 分钟全自动提取发布，用户仅扫码 2 次。

### 下次改进
Agent自身：Windows 扫码 L3 流程已踩通（有头 Chrome + fetch 二维码 + 原生 click），应立即 patch 进技能 feishu-doc-l3-extraction；方法论卡更新：技能 references/third-party-feishu-viewers.md 的 URL 结构说明已确认（第三段是 doc_id），无需改。

---

## 追加：每周一自我进化巡检（cron 2026-08-24）

### 四阶段闭环结果

**Phase 1 — Memory 自检 ✅**
- 当前 80%（1,761/2,200 chars），未超 92% 红线，无需精简
- 逐条核对：WSL 不可用 / 凭据路径 / 检索铁律 / 微信三账号 全部仍为当前事实，无过时条目

**Phase 2 — Skills 自检 ✅**
- 4 核心技能全部可加载（readiness: available）：feishu-publishing / duanwangye-review / duanwangye-prezi / duanwangye-knowledge-collision
- 路径均为 Windows 侧（C:\Users\Administrator\AppData\Local\hermes\profiles\duanwangye\skills\），无 /mnt/c 残留
- feishu-doc-l3-extraction 08-23 已 patch（Windows 扫码 + 原生 click 陷阱），无未记录 pitfalls

**Phase 3 — Error-to-Skill 闭环 ✅**
- 本周（08-18~08-24）会话盘点：08-19 Live86 发布 / 08-22 待命 / 08-23 Live260 提取
- 08-23 两个坑（headless 微信二维码不渲染、Vue 原生 click 陷阱）→ 已沉淀进 feishu-doc-l3-extraction skill（session 799/801）
- **08-18 MCP 检索诊断（diag_20260818）**：#350/#351 黄药师已修复——本次实测 `kdo_search("飞书发布 反馈追踪 最佳实践")` 中文正常返回 3 卡（hybrid RRF，无乱码）✅ 检索铁律生效
- 无需新建 corrections / dk 卡

**Phase 4 — 复盘检查 ✅**
- daily-context 最近复盘 2026-08-24.md（本日 00:30，Live260 提取，🟡 B级），无断档（<7天）
- 六文件在拼音轨（agent复盘/duanwangye/）健康，旧目录已冻结（#367）
