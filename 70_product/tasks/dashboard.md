---
title: 任务仪表盘
updated: 2026-05-19
---

# 任务仪表盘

> **用法**：Agent 自己来看进度、领任务。批次全部完成后通知欧阳锋统一审查。
> **图例**：✅ 完成 · 🔨 进行中 · ⏳ 排队 · ⚠️ 阻塞

---

## 老顽童（Producer · 飞书 Hermes）

| # | 任务 | 批次 | 状态 | 备注 |
|---|------|------|------|------|
| ① | 补 related 边 | — | ⏳ | 3 条 wikilink + frontmatter relation |
| ② | 双三角文章 v2 | — | ✅ | 用户已通过，关闭 |
| ③ | 管理工具箱 Batch 1（F1+T1+T2） | 工具箱 | ✅ | 全 A。T1 typo 已修 ✅ |
| ④ | 管理工具箱 Batch 2（T3+T4+T5） | 工具箱 | ✅ | T3 A / T4 A+ / T5 A。T3 typo 已修 ✅ |
| 🔍 | 双三角卡结构修复 | — | ⏳ | H3→H4 攻击者标题 + 删重复 related（审查 A-） |
| 🆕 | Anthropic AI 原生初创手册 | 素材编译 | ⏳ | ingest ✅，骨架已生成，三步编译未开始 |
| ⑤ | 设计域 S1+S2+S3 skill | 洪七公+段王爷 | 🔨 | 内容 A，3 命名/格式 Bug 待修（详见表下执行顺序 #2） |
| 🆕 | 科学决策域 35 PNG 增强消化 | 增强 | ⏳ | OCR+交叉比对，老顽童自闭环 |
| ⑥ | v1.5 全库修复（89 FAILED） | 质量 | ⏳ | 等 scaffold 工具 + 设计域完成后启动 |
| ⑦ | 管理工具箱 Batch 3（T6+T7+T8） | 工具箱 | ⏳ | 穿插在 89 卡修复间隙 |

### 老顽童 — 执行顺序（从上到下，做完一个再看下一个）

| 顺序 | 任务 | 内容 | 估时 | 备注 |
|:----:|------|------|:--:|------|
| **1** | 🔍 双三角卡结构修复 | H3→H4 攻击者标题 + 删重复 related | 5min | 审查 A-，修完跑 `kdo validate --v15 --card yt-model-dual-triangle-competitiveness` 验证 |
| **2** | 🔧 设计域 Skill 命名+格式修复 | 目录重命名 + frontmatter name 去重 + 加五段式标准结构 | 15min | 审查发现 3 Bug：目录名错位、name 重复、缺标准段。详见 [[70_product/tasks/laowantong-next-tasks#⑤-B 设计域 Skill 命名与格式修复（欧阳锋审查反馈）]] |
| **3** | 🆕 Anthropic 创始人手册 | 三步编译法 → concept 卡 | 2h | 详见 [[70_product/tasks/laowantong-next-tasks#⑧ Anthropic AI 原生初创公司手册]] |
| **4** | ⑤ 设计域 S1+S2+S3 复审 | 命名+格式修完后欧阳锋复审 | — | S1/S2/S3 内容已完成（A），等格式修复后复议 |
| **5** | 🆕 科学决策域 35 PNG 增强消化 | OCR+交叉比对→查漏补缺 | 3h | 老顽童自闭环（含 OCR）。详见 [[70_product/tasks/laowantong-next-tasks#⑨ 科学决策域 35 PNG 增强消化]] |
| **6** | ⑥ v1.5 全库修复（89 FAILED） | scaffold 分批修 + 穿插 ⑦ Batch 3 | 分批 | `kdo validate --v15` FAILED → 0 |

> **规则**：顺序执行，不跳。每完成一个 → 跑验证 → 通知欧阳锋审查。不要等批次全部完成。

---

## 黄药师（Builder · WSL tmux claude）

| # | 任务 | 优先级 | 状态 | 备注 |
|---|------|--------|------|------|
| 1 | `kdo scaffold` | P0 | ✅ | A，17 tests |
| 2 | `kdo clean-transcript` | P1 | ✅ | A，7 tests |
| 3 | `kdo validate --v15 --watch` | P2 | ✅ | A，纯标准库 |
| 4 | `kdo watch` 依赖解耦 | P1 | ✅ | 4 tests |
| 5 | scaffold 插入位置修正 | P2 | ✅ | Critique→CB/Synthesis 间 |
| 6 | `kdo task` 自动化 + dashboard | **P0** | ✅ | 6 tests, 5 子命令, 向后兼容 |
| 7 | graph rebuild --incremental | P2 | ✅ | 5 tests, --full + incremental |
| 8 | `kdo graph stats` | P3 | ✅ | 4 tests, --json, NOT BUILT |
| 9 | Graph RAG 深化 | P1 | ✅ | graph path + 跨域标注 + --health, 9 tests |
| 10 | Quality Gate v2（article+skill） | P1 | ✅ | --article + --skill + --all, 9 tests |
| 11 | `kdo validate --skill-dir` 审查流水线 | P1 | ✅ | batch 扫描 + L1 5节检查, 5 tests |
| 12 | KDO Build 系统 | P2 | ✅ | `kdo build` + CHANGELOG + build_state, 11 tests |

### 黄药师 — 当前任务

**全部完成，无待办**。等待欧阳锋分配新任务。

---

## 洪七公（Multimodal Arbiter · 飞书 Hermes）

> **定位**：多模态知识仲裁者。主业=知识→视觉资产。副业=VA 过程中发现归属错位。
> **输入**：`dashboard` 任务 + `30_wiki/concepts/` 卡片 + `10_raw/assets/` 原图
> **输出**：静态视觉 → `40_outputs/content/images/` · 动态视觉 → `videos/` · 音频 → `audio/` · 演示 → `presentations/` · 网页 → `code/templates/` · 勘误 → `60_feedback/corrections/`
> **规则**：不自行修改卡片主体结构。原图优先于卡片文字。详细 → [[20_memory/beikai-role-positioning.md]]

| # | 任务 | 状态 | 备注 |
|---|------|------|------|
| 1 | 角色自我定义 | ✅ | 已获欧阳锋确认为"多模态仲裁者" |
| 2 | 双三角 Visual Analysis | ✅ | `40_outputs/content/images/infographics/dual-triangle-visual-analysis.md` |
| 3 | 双三角 Excalidraw 重绘 | ✅ | `40_outputs/content/images/infographics/dual-triangle-competitiveness.excalidraw` |
| 4 | wiki 勘误（归属错位） | ✅ | 已反馈 → `60_feedback/corrections/`，卡片修正由老顽童执行 |
| 5 | 通道就绪确认 | ⏳ | 确认能读写上述输入/输出路径 |

## 段王爷（Publisher）

| # | 任务 | 状态 | 备注 |
|---|------|------|------|
| — | 待激活 | ⚠️ | 任务派发协议待定义 |

---

## 阻塞项

| 谁 | 什么事 | 卡在哪 |
|----|--------|--------|
| 老顽童 | 双三角卡 H3→H4 + 删重复 related | 审查发现，等老顽童修 |
| 老顽童 | 设计域 3 Skill 命名/格式修复 | 目录名错位+name 重复+缺标准段，修复清单已写入 [[70_product/tasks/laowantong-next-tasks#⑤-B 设计域 Skill 命名与格式修复（欧阳锋审查反馈）]] |
| 洪七公 | 通道就绪确认 | 确认能读写输入/输出路径 |
| 欧阳锋 | 待审查黄药师 Task 11+12 | Task 11 开发中，Task 12 排队 |

---

## 最近完成

| 日期 | 谁 | 任务 | 结果 |
|------|-----|------|------|
| 05-19 | 欧阳锋 | 老顽童设计域 3 Skill 审查 | ✅ 内容全 A，3 Bug（命名+格式），修复清单已写入任务文件 |
| 05-19 | 黄药师 | Task 10 Quality Gate v2 | ✅ --article + --skill + --all, 9 tests |
| 05-19 | 黄药师 | Task 9 Graph RAG 深化 | ✅ graph path + 跨域标注 + --health, 9 tests |
| 05-19 | 洪七公 | 双三角 VA + Excalidraw 重绘 | ✅ VA 158行 + `.excalidraw` 源文件 |
| 05-19 | 洪七公 | 角色自我定义 | ✅ `beikai-role-positioning.md`（296行，85技能×18领域） |
| 05-19 | 洪七公 | wiki 勘误 | ✅ 发现双三角归属错位，已记录 |
| 05-19 | 老顽童 | 双三角卡 Visual Analysis 节引用 | ✅ 引用洪七公 VA 产出 + 归属错位注释 |
| 05-19 | 欧阳锋 | 老顽童工作审查 | T1/T3 typo ✅，双三角卡 A-（2 结构问题），Anthropic 未开工 |
| 05-19 | 黄药师 | Task 8 graph stats | ✅ 4 tests, --json |
| 05-19 | 黄药师 | Task 7 graph rebuild --incremental | ✅ 5 tests, --full + incremental |
| 05-19 | 黄药师 | Task 6 kdo task 自动化 | ✅ 5 子命令 + 6 tests |
