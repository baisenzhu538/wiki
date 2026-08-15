---
title: 洪七公失忆恢复记录
created_at: 2026-06-13
updated_at: 2026-08-15
type: memory/role-recovery
---

# 洪七公失忆恢复记录

> 触发：用户说"你是洪七公，你去桌面的wiki文件夹里面去熟悉你的任务，你又失忆了"
> 恢复时间：2026-06-13
> 工作目录：`C:\Users\Administrator\Desktop\wiki\`

---

## 1. 我是谁（已恢复）

**洪七公（Multimodal Arbiter）**——知识工厂的多模态知识仲裁者。

- **主业**：知识→视觉资产（信息图、Excalidraw、SVG、视频、音频、AI 出图 prompt）
- **副业**：VA 过程中发现源文件与编译物归属错位/不一致，写纠偏记录，不改卡片主体
- **运行接口**：Hermes agent → 飞书
- **任务来源**：`70_product/tasks/dashboard.md` 洪七公任务区
- **协调节点**：欧阳锋是唯一派活人，角色之间不互相派活

---

## 2. 本次恢复读了哪些文件

按 `CLAUDE.md` 启动顺序：

1. `.agent/hongqigong-context.md` — 角色专属指令
2. `.agent/context.md` — 共享状态、当前任务
3. `.agent/pitfalls.md` — 踩坑记录
4. `.agent/toolkit.md` — 可用工具
5. `70_product/tasks/dashboard.md` — 任务仪表盘
6. `70_product/tasks/hongqigong-next-tasks.md` — 我的后续任务
7. `90_control/AGENTS.md` — 角色分工、禁止清单
8. `40_outputs/capabilities/role-profiles/hongqigong-profile.md` — 我的角色画像

---

## 3. 当前状态（截至 2026-08-15，以目录内最新为准）

> 任务 1-18（VA 前置 A1、单元模型域 VA、OCR 系列）已于 2026-06-13 前全部完成，历史从略。
> 最新状态以 `桌面/agent复盘/洪七公/每日复盘/` + `桌面/agent复盘/洪七公/索引.md` 为准，本文件只保留最近锚点。

- **2026-07-12**：C 域（业务公式）101 图、D 域（转化率）484 文件（155 图+329 PDF 页）OCR+VLM 收官，整合笔记+任务编排建议书交付王语嫣；报告在各素材 `_vlm_output/`。沉淀错误模式 E013-E017
- **2026-07-21**：王欢《无限画布》教程 22 图识别+md 交叉验证收官（报告在素材旁 `_vlm_output/识别报告_无限画布教程.md`）；认领新武器 `infinite-canvas-prezi`（见第 4 节）
- **2026-08-09（最新一轮）**：
  - AI基本功：69 次 VLM 调用（92.8%），产出位置曾被纠正为"直接落素材目录、Obsidian 可见"；周期表 4 个被化学元素皮肤遮蔽的 Feature 待人工对照补齐
  - 教练式领导力：79 图全量 OCR+VLM 覆盖，双引擎补跑（M3 55/68），8 卡任务编排建议书交付
  - 科学开会：27 图全量 OCR+VLM（83/86，96% 一次通过），十大原则武器库 + 8 卡建议书交付
  - `long-image-ocr` skill 迭代到 **v2.0**（M3 铁律 + 断点续跑 + 双路径密钥）并完成 KDO 注册
  - 错误模式库累计 **E001-E024**（新增 E021-E024）
  - 固化铁律：①产出=OCR 原文而非分析总结，直接写素材目录；②顺序=先 OCR+VLM→理解→最后写建议书；③脚本运行前三查（import/变量/路径）；④密钥放家目录，`/tmp` 会被清
  - 模型铁律：**只用 MiniMax-M3**，`abab6.5s-chat` 禁用（7% 随机失败）
- **当前**：AI基本功 / 教练式领导力 / 科学开会三个专题已收官，待命；遗留"周期表 4 个 Feature"人工对照。任务由欧阳锋派（看 `70_product/tasks/production-queue.md` + `.agent/context.md`）

---

## 4. 我的武器库（已部署且可用）

> ⚠️ **2026-08-09 起，武器以活注册表为准**：`.agent/hongqigong-context.md`「武器路由」表（分析/渲染/质检/交接四类）+ `40_outputs/capabilities/workflows/multimodal-production.md` 决策树。下方静态清单仅作历史参考。
> 🆕 **新武器**：`infinite-canvas-prezi`——内容→无限画布空间叙事（impress.js 单文件 HTML，镜头缩放/平移/旋转叙事）。登记：路由表渲染类 / 决策树 Pipeline E / skill 卡 `30_wiki/skills/skill-duanwangye-prezi.md`（draft）。**生产归我，发布归段王爷。**
> 🆕 **long-image-ocr v2.0（2026-08-09）**——长图/截图批量 OCR+VLM 主力流程：MiniMax-M3 铁律、断点续跑、双路径密钥。注册卡 `40_outputs/capabilities/skills/long-image-ocr/SKILL.md`，可执行技能 `~/.hermes/profiles/beikai/skills/creative/long-image-ocr/SKILL.md`。

### 4.1 Skills（`40_outputs/capabilities/skills/`）

| Skill | 路径 | 用途 |
|:---|:---|:---|
| Image OCR | `image-ocr/SKILL.md` | 本地 PaddleOCR v5，PNG/JPEG 中英文提取 |
| Deep Image Parser | `deep-image-parser/SKILL.md` | 多模态 AI 表格/公式/密集文字/视觉标记解析 |
| Long Image OCR | `long-image-ocr/SKILL.md` | 长图/截图切分 + VLM 识别，原始 OCR 文本直出 |
| Design Prompt Iteration | `design-prompt-iteration/SKILL.md` | 设计师反馈 → AI 图像 prompt 翻译 |
| Visual Prompt System | `visual-prompt-system/SKILL.md` | SROM Visual OS：视角+美学宪章+拼贴海报 |
| AI Design Assets | `ai-design-assets/SKILL.md` | 设计资产管理规范（8要素命名+PS四层+Moodboard） |
| AI Design Fundamentals | `ai-design-fundamentals/SKILL.md` | 模型选型与提示词基本功 |
| AI Design Prompts | `ai-design-prompts/SKILL.md` | AI 设计提示词技法 |
| Document Parsing Toolkit | `document-parsing-toolkit/SKILL.md` | PDF/图片→结构化 Markdown 引擎选型 |
| AI Image Prompt Engineering | `ai-image-prompt-engineering/SKILL.md` | 通用 AI 图像生成 prompt 工程 |
| Markdown to Presentation | `markdown-to-presentation/SKILL.md` | Markdown → 幻灯片 |
| Audio Production Pipeline | `audio-production-pipeline/SKILL.md` | TTS / 配音 / 音乐 / 音频后期 |

### 4.2 实际产出（已有肉身）

- **信息图**：`40_outputs/content/images/infographics/`
  - `dual-triangle-competitiveness.excalidraw`
  - `dual-triangle-*.png/svg`
  - `va-report-scientific-decision-2026-05-21.md`
- **视频**：`40_outputs/content/videos/`
  - `kdo-quickstart-video/index.html`
  - `knowledge-delivery-os-快速上手指南把散落知识变成可交付资产/`（含脚本、分镜、音频、final）

### 4.3 已有 skill 但无实际产出的领域

- `40_outputs/content/images/generative/` — AI 生图：有 `ai-image-prompt-engineering` skill，但无直接产出
- `40_outputs/content/audio/` — 音频：有 `audio-production-pipeline` skill，但无实际作品
- `40_outputs/content/presentations/` — PPT/幻灯片：有 `markdown-to-presentation` skill，但无实际作品

---

## 5. 记忆锚点（下次失忆直接按这个顺序读）

| 优先级 | 文件 | 作用 |
|:---|:---|:---|
| P0 | `.agent/hongqigong-context.md` | 确认身份、启动步骤、武器路由表（活注册表）、行为牌组 H1-H6、当前状态 |
| P0 | `.agent/context.md` | 全厂共享状态、active_task、blockers |
| P0 | `70_product/tasks/dashboard.md` | 看洪七公任务区领任务 |
| P1 | `.agent/toolkit.md` | 本地武器库、命令速查 |
| P1 | `.agent/pitfalls.md` | 别踩过的坑 |
| P1 | `桌面/agent复盘/洪七公/`（错误模式库 E001-E024 / 技能进化日志 / 每日复盘 / 索引，以目录内最新为准） | 我个人的错误模式与技能进化史 |
| P1 | `桌面/agent复盘/hongqigong/daily-context/`（以目录内最新日期为准） | 最近 Truman 10章复盘 |
| P1 | `40_outputs/capabilities/role-profiles/hongqigong-profile.md` | 角色画像快照 |
| P2 | `90_control/AGENTS.md` | 全厂角色分工、禁止清单 |
| P2 | `20_memory/hongqigong-amnesia-recovery-20260613.md` | 本文件：完整恢复记录 |

---

## 6. Skill 迭代存放规则

- **新增/修改 skill**：`40_outputs/capabilities/skills/<skill-name>/SKILL.md`
- **新增本地工具/命令**：同步更新 `.agent/toolkit.md`
- **新增坑/教训**：同步追加 `.agent/pitfalls.md`
- **职责/接口变化**：同步更新 `.agent/hongqigong-context.md`
- **角色画像变化**：同步更新 `40_outputs/capabilities/role-profiles/hongqigong-profile.md`
- **成为全厂内置 skill**：同步更新 `CLAUDE.md` + `90_control/AGENTS.md`

---

## 7. 我现在的待命能力

用户/欧阳锋可以直接派：

1. 给图 → OCR / 深度解析
2. 给知识卡片 → 信息图 / Excalidraw / SVG
3. 给文章 → 视频脚本 + 分镜
4. 给 AI 出图反馈 → prompt 迭代
5. 给设计团队 → 资产管理规范
6. 发现图文错位 → 写 `60_feedback/corrections/` 记录
7. 给长图/截图批量素材 → `long-image-ocr v2.0`：切分→M3 VLM→原始 OCR 文本直出素材目录

---

## 8. 共享阻塞（以 `.agent/context.md` 最新为准）

- 本文件不再复制阻塞清单——失忆恢复时读 `.agent/context.md` 的 blockers 节。
- 历史阻塞（供追溯）：Kimi K2.7 Anthropic tool call 待修复（临时切 DeepSeek）；欧阳锋待审查黄药师 I/J/K/L/M/N 批量任务。

---

## 9. 关联文件

- `.agent/hongqigong-context.md`
- `.agent/context.md`
- `.agent/toolkit.md`
- `.agent/pitfalls.md`
- `70_product/tasks/dashboard.md`
- `90_control/AGENTS.md`
- `40_outputs/capabilities/role-profiles/hongqigong-profile.md`
- `40_outputs/capabilities/skills/long-image-ocr/SKILL.md`