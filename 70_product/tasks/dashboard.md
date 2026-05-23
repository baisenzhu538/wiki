---
title: 任务仪表盘
updated: 2026-05-24
---

# 任务仪表盘

> **用法**：Agent 自己来看进度、领任务。批次全部完成后通知欧阳锋统一审查。
> **图例**：✅ 完成 · 🔨 进行中 · ⏳ 排队 · ⚠️ 阻塞

---

## 老顽童（Producer · 飞书 Hermes）

| # | 任务 | 状态 | 备注 |
|---|------|:--:|------|
| 1-9 | 补related边 / 双三角文章 / 工具箱B1-B3 / 设计域Skill / Anthropic手册 / 科学决策PNG / v1.5全库修复 / Truman知识地图 | ✅ | 全部完成 |
| 10 | 🆕 **单元模型域编译 + VA 修复** ← 当前 | 🔨 | 5口述稿+31图→7卡（Part A ✅）。Part B 14条修复中 10/14（剩余3条）。详见 [[task-20260524-laowantong-unit-model-plus-va-repair]] |
| 11 | OCR Batch 4（50张视觉卡） | ⚠️ | 阻塞：等洪七公 VA 前置交付 |

> **规则**：顺序执行，不跳。每完成一个 → 跑验证 → 通知欧阳锋审查。

---

## 黄药师（Builder · WSL tmux claude）

| # | 任务 | 状态 |
|---|------|:--:|
| 1-17 | scaffold / clean-transcript / validate-watch / watch解耦 / 插入位置修正 / task自动化 / graph增量 / graph-stats / Graph RAG深化 / Quality Gate v2 / validate-skill-dir / Build系统 / scaffold四缺陷 / validator空H4 / video CLI / video render修复 / render遗留缺陷 | ✅ |
| 18-20 | Batch 7 基础设施债（index.md wikilink / 源注册表垃圾 / auto-feedback洪水） | ✅ |
| 19 | Sprint 12 回溯升级 v1.5（110/110 卡 PASS） | ✅ |
| 🍽️ | Dogfood：AI学习域全管线 → 2篇文章 + 体验笔记 | ✅ |

### 当前队列（按优先级）

| # | 任务 | 估时 | 状态 |
|:--:|------|:--:|:--:|
| 24 | 🔥 produce 自动预填结构性信息（P0） | ~1.5h | ⏳ |
| 25 | validate 以 frontmatter 为真相源（P1） | ~1h | ⏳ |
| 21 | 断链批量修复（~113个） | ~45min | ⏳ |
| 22 | frontmatter 批量补全（~271张） | ~30min | ⏳ |
| 23 | 新旧格式统一（~166张） | ~20min | ⏳ |
| 26 | clean-transcript 会话式规则集（P1） | ~1.5h | ⏳ |
| 27 | ocr 失败提示（P2） | ~15min | ⏳ |
| 28 | produce→validate 快捷循环（P2） | ~20min | ⏳ |

> ⚡ 未等工单已自修 2 个 P0。详见 [[huangyaoshi-next-tasks]]。

---

## 洪七公（Multimodal Arbiter · 飞书 Hermes）

| # | 任务 | 状态 | 备注 |
|---|------|:--:|------|
| 1-7 | 角色定义 / 双三角VA / Excalidraw / wiki勘误 / 通道就绪 / 文章审计 / KDO视频试点（7a-7g 全部✅ 已 ship） | ✅ | 视频管线关闭 🎉 |
| 8 | 科学决策域 VA 交叉审查 | ✅ | 35张图逐图审查，通过率~71% |
| 9 | VA 前置（A1 🔴10张） | ✅ | A。10/10 四维法，欧阳锋审查通过。🟡🟢16张后续穿插 |
| 10 | 🔥 **单元模型域 VA 前置** ← 当前 | 🔨 | 原任务书图名与 inbox 不匹配。已更正：7 张 yt-unit-model 卡逐张写 VA。详见 [[task-20260524-hongqigong-unit-model-va]] |
| — | 文章重启（B 部分，≥3篇） | ⏳ | A 全部完成后再做 |

> **洪七公定位**：多模态知识仲裁者。主业=知识→视觉资产。原图优先于卡片文字。不自行修改卡片主体结构。

---

## 段王爷（Publisher · 飞书 Hermes）

| # | 任务 | 状态 | 备注 |
|---|------|:--:|------|
| 1 | 🎬 KDO 视频试点 ship | ⚠️ 待补记录 | final.mp4 已就绪（11810 KB, 500.08s, H.264/AAC）。需补全交付记录 JSON（审批链+门禁+贡献者） |

---

## ⚠️ 阻塞项

| 谁 | 什么事 | 卡在哪 |
|----|--------|--------|
| 老顽童 | OCR Batch 4（50张视觉卡） | 等洪七公 VA 前置交付 |
| 老顽童 | 单元模型域编译（卡片写作阶段） | 等洪七公单元模型域 VA 完成 |

---

## 最近完成

| 日期 | 谁 | 任务 | 结果 |
|------|-----|------|------|
| 05-24 | 老顽童 | Part A 单元模型域 7卡编译 | ✅ A。全部 v1.5 三要件（Critique≥2攻击者 + 不要用≥2 + AT≥3） |
| 05-24 | 洪七公 | Task 9 VA 前置 A1（10张🔴卡） | ✅ A。10/10 四维法，欧阳锋审查通过 |
| 05-24 | 黄药师 | Batch 7 基础设施债（Task 18-20） | ✅ A。index.md wikilink + 源注册表垃圾 + auto-feedback cooldown。379 tests |
| 05-24 | 老顽童 | OCR Batch 2+3 格式调整 | ✅ A。31张卡统一 `## Critique` + `### 不要用的场景` |
| 05-24 | 洪七公 | 科学决策域 VA 交叉审查 Batch 1 | ✅ 18张图逐图审查 |
| 05-23 | 黄药师 | P0+P1 整改令全部关闭 | ✅ 6 项全部通过 |
| 05-23 | 老顽童 | OCR Batch 1（5张视觉框架卡） | ✅ A+ |
| 05-21 | 段王爷 | 🎬 KDO 视频试点 ship | ✅ final.mp4 shipped。管道关闭 |
| 05-21 | 老顽童 | v1.5 全库修复 + 工具箱 Batch 3 | ✅ 215 cards: 211 pass / 0 fail / 4 warn |
