---
id: 539
assignee: laowantong
status: queued
updated_at: '2026-08-26T11:00:00+00:00'
version: v0.1
instance: laowantong
code_files:
  - 30_wiki/concepts/concept-aducit-six-step.md
  - 30_wiki/cases/case-yihang-dual-triangle-AI三角-数据.md
---

# #539 ADUCIT 概念卡 + 双三角 case 卡 VLM 臆测表处置（小昭误诊事故内容层修复）

- **任务号**：#539
- **状态**：queued
- **assignee**：laowantong（欧阳锋终审）
- **优先级**：P1（错误事实已传播到老朱面前一次，内容层止血优先）
- **立项**：2026-08-26 王语嫣（小昭复盘《双三角误诊复盘与 ADUCIT 考证》改进 4 裁定采纳+修正）

## 背景

小昭把 VLM 臆测的「数据/算法/算力」当双三角 AI 三角回答老朱（正确=场景/数据/基本功）；且她断言 ADUCIT 英文全称全库零命中，实际 `30_wiki/decisions/plan_20260531_data-curator-v1.3.md:81` 有官方版：**Anticipate/Detect/Unearth/Clean/Implement/Track + Governance 贯穿**（她的推断 6 错 4）。

## 任务

1. **产 `concept-aducit-six-step.md`**（P0 卡级三方法）：六步英文全称+中文+定义，source 锚 plan_20260531_data-curator-v1.3.md:81 与 art_20260602_three_deep_questions.md:91；与 `concept-yihang-dual-triangle-core` 双链（ADUCIT=AI 三角「数据」顶点展开方法，数据顶点四阶进化第四阶=飞轮闭环）
2. **处置 case 卡臆测表**（`case-yihang-dual-triangle-AI三角-数据.md:145`）：VLM 臆测的「数据/算法/算力」表挂显式警示（`> ⚠️ AI 推断，与权威卡冲突，以 concept-yihang-dual-triangle-core 为准`）并 frontmatter 加 `conflict_with: [[concept-yihang-dual-triangle-core]]`——不删（留事故化石），但要让任何读者一眼知道不能信
3. 结构层改造（两段式 schema）不在本单，走 #540

## 边界

- 只动这两张卡；itingnao 7685126 全文拉取=源债，随单登记停车场，拉到后补时间戳进概念卡
- 小昭推断表（U/C/I/T 错误版本）不得进任何卡——进复盘当反面教材

## 验收

- 概念卡过 lint+三方法；case 卡警示挂好；欧阳锋终审（重点核英文全称与 plan 文档逐字母对账）
