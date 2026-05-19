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
| ⑤ | 设计域 S1+S2 skill | 洪七公+段王爷 | 🔨 | 老顽童已提交，待欧阳锋审查 |
| ⑥ | v1.5 全库修复（89 FAILED） | 质量 | ⏳ | 等 scaffold 工具 + 设计域完成后启动 |
| ⑦ | 管理工具箱 Batch 3（T6+T7+T8） | 工具箱 | ⏳ | 穿插在 89 卡修复间隙 |

### 老顽童 — 执行顺序（从上到下，做完一个再看下一个）

| 顺序 | 任务 | 内容 | 估时 | 备注 |
|:----:|------|------|:--:|------|
| **1** | 🔍 双三角卡结构修复 | H3→H4 攻击者标题 + 删重复 related | 5min | 审查 A-，修完跑 `kdo validate --v15 --card yt-model-dual-triangle-competitiveness` 验证 |
| **2** | 🆕 Anthropic 创始人手册 | 三步编译法 → concept 卡 | 2h | 详见 [[70_product/tasks/laowantong-next-tasks#⑧ Anthropic AI 原生初创公司手册]] |
| **3** | ⑤ 设计域 S1+S2 | AI 生图模型选型 + Prompt 工程 skill | 🔨 老顽童已提交 | 待欧阳锋审查，文件位置待确认 |
| **4** | ⑤ 设计域 S3 | `设计资产管理规范` skill | 1h | S1+S2 审查通过后启动 |

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
| 10 | Quality Gate v2（article+skill） | P1 | ⏳ | validate 扩展到文章/skill 类型 |

### 黄药师 — 当前任务

**Task 10**：Quality Gate v2（详见 [[70_product/tasks/huangyaoshi-next-tasks.md]]）

---

## 洪七公（Multimodal · 飞书 Hermes）

| # | 任务 | 状态 | 备注 |
|---|------|------|------|
| 1 | 角色自我定义 | ✅ | `20_memory/beikai-role-positioning.md`（296行，85技能×18领域，4个待决策问题） |
| 2 | 双三角 Visual Analysis | ✅ | `40_outputs/content/images/infographics/dual-triangle-visual-analysis.md`（158行五维分析） |
| 3 | 双三角 Excalidraw 重绘 | ✅ | `40_outputs/content/images/infographics/dual-triangle-competitiveness.excalidraw` |
| 4 | wiki 勘误（归属错位） | ✅ | 发现原图 vs 卡片子项归属错位，已写入 Visual Analysis + 卡片注释 |
| 5 | 角色边界决策 | ⏳ | 4 个待欧阳锋决策的问题（见角色定位文件） |

### 洪七公 — 待欧阳锋决策

详见 [[20_memory/beikai-role-positioning.md]]，4 个问题：
1. 角色边界：AGENTS.md 是"最小职责集"还是"最大边界墙"？
2. 执行接口标准化：触发机制是否需要统一？
3. 归属错位处理原则：原图 vs wiki 卡片不一致时用哪个？
4. 技能升级权限：85 个技能中哪些正式注册？

## 段王爷（Publisher）

| # | 任务 | 状态 | 备注 |
|---|------|------|------|
| — | 待激活 | ⚠️ | 任务派发协议待定义 |

---

## 阻塞项

| 谁 | 什么事 | 卡在哪 |
|----|--------|--------|
| 老顽童 | 双三角卡 H3→H4 + 删重复 related | 审查发现，等老顽童修 |
| 洪七公 | 4 个角色决策待欧阳锋拍板 | 见 `beikai-role-positioning.md` |
| 欧阳锋 | 需审阅洪七公角色定位 + 双三角 VA | 两份文件均已就位 |

---

## 最近完成

| 日期 | 谁 | 任务 | 结果 |
|------|-----|------|------|
| 05-19 | 黄药师 | Task 9 Graph RAG 深化 | ✅ graph path + 跨域标注 + --health, 9 tests |
| 05-19 | 洪七公 | 双三角 VA + Excalidraw 重绘 | ✅ VA 158行 + `.excalidraw` 源文件 |
| 05-19 | 洪七公 | 角色自我定义 | ✅ `beikai-role-positioning.md`（296行，85技能×18领域） |
| 05-19 | 洪七公 | wiki 勘误 | ✅ 发现双三角归属错位，已记录 |
| 05-19 | 老顽童 | 双三角卡 Visual Analysis 节引用 | ✅ 引用洪七公 VA 产出 + 归属错位注释 |
| 05-19 | 欧阳锋 | 老顽童工作审查 | T1/T3 typo ✅，双三角卡 A-（2 结构问题），Anthropic 未开工 |
| 05-19 | 黄药师 | Task 8 graph stats | ✅ 4 tests, --json |
| 05-19 | 黄药师 | Task 7 graph rebuild --incremental | ✅ 5 tests, --full + incremental |
| 05-19 | 黄药师 | Task 6 kdo task 自动化 | ✅ 5 子命令 + 6 tests |
