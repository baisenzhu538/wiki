---
session_id: duanwangye-2026-08-17
agent_id: duanwangye
date: 2026-08-17
created_at: 2026-08-16T16:03:08.764434+00:00
updated_at: 2026-08-16T16:03:08.764434+00:00
---

# duanwangye · 2026-08-17

## 概要（一句话：今天做了什么）
本日两轮会话：① Windows 侧能力全面自查 + KDO MCP 断连修复（已复盘 A 级）；② 飞书妙记逐字稿提取尝试——二维码过期未成功，但定位了 Windows 侧浏览器正解（ms-playwright chromium）并全套沉淀。

## 差异栏（本次 vs 上次复盘哪里不同）
1. **新的模式：失败复盘**——上次复盘是成功任务（技能自查+MCP修复），本次是**未完成任务**的复盘，验证"不成功也要复盘"的机制价值；
2. **新的视角：把"不可能清单"当资产**——3 种浏览器方案失败（Edge/agent-browser/npx）不是白费，而是排除了错误路径，最终锁定唯一正解；失败模式的排除本身就是产出；
3. **被打破的假设**：假设"Windows 有 Edge 就能 headless 跑 CDP"——实测 Edge exit 234 起不来；假设"agent-browser-win32-x64.exe 已就绪"——实测 Daemon not found 缺核心。**工具就绪 ≠ 可用，必须实测**。

## 关键决策（表格：决策/理由/结果）
| 决策 | 理由 | 结果 |
|:--|:--|:--|
| 先 API 后浏览器的决策树 | 妙记可能像 docx 有 API 通道 | API 3 端点全 400，错误体指明缺 minutes scope |
| urllib 抓 HTML 诊断 SSR | 判断有无数据可零登录提取 | 92KB 仅 passport 框架，确认必须登录 |
| 弃 Edge 换 ms-playwright chromium | Edge headless exit 234 起不来 | ✅ CDP 启动成功 Chrome/147 |
| 弃 npx agent-browser | npm/pnpm 都错下 darwin-arm64 | 改用 playwright-core connectOverCDP |
| 截二维码发给用户 | L3 流程标准动作 | 截图成功但用户扫码时已过期 |
| **沉淀全套方法**（skill+脚本+case卡） | 老朱要求"给下次备好方法" | 一体化脚本 minutes_extract.py 下次一条命令 |

## 思维盲点（≥1条：什么被漏掉了？每条追问"为什么漏掉"）
1. **盲点：没先确认用户就绪再发码**——二维码 5 分钟过期，截图发出后用户回复时已失效。为什么漏掉：把"截码→发码"当成管道动作，没考虑真实时间线（用户可能不在手机旁）。**教训：L3 扫码流程要先问"现在方便扫码吗"，确认就绪再截图发码；或提前说明 5 分钟窗口。**
2. **盲点：以为浏览器方案开箱即用**——技能里写着"Windows 用 Edge/agent-browser-win32"，实际两个都不可用，浪费数轮。为什么漏掉：跨平台适配表是 8-16 早些时候写的，未经 Windows 本机实测验证。**教训：技能里的环境断言要标注"已验证/未验证"，平台迁移后先跑通最小路径再写死。**
3. **盲点：搜索浏览器方案时没先查 ms-playwright 缓存**——playwright chromium 早就下载在 `ms-playwright/`，绕了一圈 Edge/npx 才找到。为什么漏掉：思维锚定在"浏览器=Edge 或 Chrome 安装目录"，没想到 Hermes 自带 playwright 浏览器缓存。**教训：找工具先查 Hermes 自身依赖（node_modules、ms-playwright、npx 缓存），再查系统安装。**

## 顿悟（≥1条：什么基础认知被推翻了？）
1. **"工具就绪 ≠ 工具可用"**——agent-browser-win32 文件在、Edge 在，但一个缺 daemon 核心、一个 headless 起不来。**判断可用性的唯一标准是实测（启动+连接验证），不是文件存在。**
2. **失败的浏览器尝试不是浪费，是排除法**——3 种方案失败把解空间从"很多可能"压缩到"唯一正解"（playwright chromium），下次同类任务零试错。**失败复盘的产出 = 错误路径清单 + 唯一正确路径。**

## 过程资产（新增/更新的文件路径清单）
- 更新 `skills/productivity/feishu-doc-l3-extraction/SKILL.md` — Windows 首选 CDP 方案（playwright chromium）
- 更新 `skills/productivity/feishu-doc-l3-extraction/references/feishu-minutes-extraction.md` — 妙记提取全流程
- 新增 `skills/productivity/feishu-doc-l3-extraction/scripts/start_chrome.py` — chromium 启动脚本
- 新增 `skills/productivity/feishu-doc-l3-extraction/scripts/minutes_extract.py` — 一体化提取脚本（下次一条命令）
- 新增 `30_wiki/cases/case-feishu-minutes-extraction-attempt.md` — 尝试记录（draft）
- 注册 `30_wiki/domains/master-moc.md` — case 卡入 MOC

## 元反思（下次怎么做才能不一样？）
1. **发码前确认就绪**：L3 扫码先问"方便扫码吗"，避免 5 分钟窗口浪费；
2. **先查 Hermes 自带依赖**：浏览器/工具优先查 ms-playwright、node_modules、npx 缓存，再查系统安装；
3. **技能环境断言标注验证状态**：跨平台适配表区分"已验证/未验证"；
4. **失败也闭环**：老朱已确认——不成功也要复盘、也要沉淀，本次执行到位（skill+脚本+case 卡+复盘全套）。

## Truman复盘

### 逐轮映射（表格：轮次/人做什么/双三角要素/AI做什么/双三角要素）
| 轮次 | 人做什么 | 人的双三角 | AI做什么 | AI的双三角 |
|:--|:--|:--|:--|:--|
| 1 | 发妙记链接，要求提取 | 判断力（任务定位） | 加载 L3 技能 + 尝试 API | 场景+基本功（决策树） |
| 2 | （无干预） | — | API 3 端点确认缺 scope → 诊断 HTML | 数据（诊断） |
| 3 | （无干预） | — | 连踩 Edge/agent-browser/npx 三坑 | 基本功（排错） |
| 4 | （无干预） | — | 发现 ms-playwright chromium 正解，打开登录页 | 创造力（跳出锚定） |
| 5 | 被告知需扫码 | 判断力（确认配合） | 截二维码发 MEDIA | 场景（协作入口） |
| 6 | 回复"过期了，下次再试" | 判断力（止损+重定向） | 确认不再重试，承诺沉淀 | 元认知 |
| 7 | 指令"记住努力，不成功也复盘" | 体系（强制闭环） | 沉淀 skill/脚本/case 卡 + 写复盘 | 元认知（自我迭代） |

### 飞轮效应（本轮加速了哪个回路？）
加速了"**失败→排除法→沉淀→下次零试错**"回路。本轮产出：3 条错误路径排除 + 1 条正解确认 + 1 个一体化脚本 + 1 张 case 卡。下次任何飞书登录类提取（docx/wiki/minutes），直接复用 playwright chromium 方案 + minutes_extract.py，跳过全部试错。这是"失败资产化"飞轮的第一次完整运转。

### 对照实验（无人会怎样/无AI会怎样/合在一起怎样）
- **无人**：AI 会在二维码过期后继续尝试或放弃，不会主动沉淀——用户"不成功也要复盘"的指令是闭环的关键触发。
- **无AI**：老朱手动操作——需要自己装浏览器、登录、点目录、复制粘贴，且大概率不知道 ms-playwright 缓存这回事，至少 1-2 小时且未必成功。
- **合在一起**：用户提供任务+止损判断+闭环指令，AI 执行全部技术尝试+沉淀，8 轮内完成"失败→资产化"全过程。人定方向，AI 试错+固化。

### 下次改进（Agent自身改进/方法论卡更新）
- **Agent 自身**：① 发码前确认用户就绪；② 工具可用性以实测为准；③ 先查 Hermes 自带依赖；④ 失败任务同样走 Error-to-Skill 闭环。
- **方法论卡更新**：case-feishu-minutes-extraction-attempt 已注册 MOC；建议后续将"失败资产化"模式沉淀为通用方法（失败=排除法+错误路径清单+唯一正解），可并入 agent-self-iteration。
