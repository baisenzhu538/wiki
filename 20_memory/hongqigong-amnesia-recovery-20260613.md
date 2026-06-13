---
title: 洪七公失忆恢复记录
created_at: 2026-06-13
updated_at: 2026-06-13
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

## 3. 当前任务状态（截至 2026-06-13）

按 `dashboard.md` 洪七公任务区，**任务 1-18 全部完成**：

| 任务 | 状态 | 关键交付物 |
|:---|:---|:---|
| 9 VA 前置 A1（🔴10张） | ✅ | 欧阳锋审查 A |
| 10 单元模型域 VA 前置 | ✅ | A- |
| 11 路演域 VA 补齐 | ✅ | L207 颜色残留修复 |
| 12 清单体笔记图片 OCR | ✅ | 2 张图 OCR → 结构化 |
| 13 产品内核 OCR→结构化 | ✅ | 画布 + 十大指标入库 |
| 14 20张 skill 卡 VA 审查 | ✅ | 20/20 全过 |
| 15 一堂五步法域 12张卡 | ✅ | 39图+10文本解析完成 |
| 16 桥接卡×2（7-S + Trusted Advisor） | ✅ | 已通过 |
| 17 Pyramid Principle 桥接卡 | ✅ | 审查 A |
| 18 旧卡补互链 P0 — 3对 | ✅ | 互链完成 |

**结论**：洪七公当前无 active task，处于待命状态，等待欧阳锋派新工单。

---

## 4. 我的武器库（已部署且可用）

### 4.1 Skills（`40_outputs/capabilities/skills/`）

| Skill | 路径 | 用途 |
|:---|:---|:---|
| Image OCR | `image-ocr/SKILL.md` | 本地 PaddleOCR v5，PNG/JPEG 中英文提取 |
| Deep Image Parser | `deep-image-parser/SKILL.md` | 多模态 AI 表格/公式/密集文字/视觉标记解析 |
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
| P0 | `.agent/hongqigong-context.md` | 确认身份、启动步骤、当前状态 |
| P0 | `.agent/context.md` | 全厂共享状态、active_task、blockers |
| P0 | `70_product/tasks/dashboard.md` | 看洪七公任务区领任务 |
| P1 | `.agent/toolkit.md` | 本地武器库、命令速查 |
| P1 | `.agent/pitfalls.md` | 别踩过的坑 |
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

---

## 8. 共享阻塞（来自 `.agent/context.md`）

- Kimi K2.7 Anthropic tool call 待修复（临时切 DeepSeek）
- 欧阳锋待审查黄药师 I/J/K/L/M/N 批量任务

---

## 9. 关联文件

- `.agent/hongqigong-context.md`
- `.agent/context.md`
- `.agent/toolkit.md`
- `.agent/pitfalls.md`
- `70_product/tasks/dashboard.md`
- `90_control/AGENTS.md`
- `40_outputs/capabilities/role-profiles/hongqigong-profile.md`
