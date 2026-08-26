---
id: 539
assignee: laowantong
status: pending_review
updated_at: '2026-08-26T12:58:26.360905+00:00'
version: v0.1
instance: kimi-cli
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

---

## 执行报告（F-034 五字段 · 2026-08-26 老顽童 kimi-cli）

**文件清单**：30_wiki/concepts/concept-aducit-six-step.md（新建）/ 30_wiki/cases/case-yihang-dual-triangle-AI三角-数据.md（警示+conflict_with）/ 30_wiki/concepts/concept-yihang-dual-triangle-core.md（双链回填）；commit `a9ac29e45`。

**完成内容**：
1. **ADUCIT 概念卡（P0 卡级三方法）**：官方全称逐字母对账 plan_20260531_data-curator-v1.3.md:81——Anticipate 预判/Detect 识别/Unearth 收集/Clean 处理/Implement 使用/Track 反馈 + Governance 贯穿；KDO 本土演绎（art_20260602:91——D/U 鸡生蛋循环、U=升仓决策）分层标注「官方版 vs 本土版」不混写；卡内嵌考证警示（小昭「全库零命中」断言证伪过程+推断版 6 错 4 不得引用）；与 concept-yihang-dual-triangle-core 双链（本卡 ADUCIT→core 定位行+core related 回填本卡）
2. **case 卡臆测表处置**：L145 表正上方挂显式警示（⚠️ AI 推断与权威卡冲突，以 concept-yihang-dual-triangle-core 为准——权威版=场景/数据/基本功）+ 注明「保留作事故化石不得引用」；frontmatter 加 `conflict_with: [[concept-yihang-dual-triangle-core]]`；表未删（按任务书留化石）
3. **源债登记**：itingnao 7685126 全文未拉取——已写入概念卡「源债登记（停车场）」节，拉到后补时间戳

**验证**：`kdo index` 重建（4169 docs）→ pre-submit 3 文件 **Passed 3 / Failed 0**（WARNING 存量级）；全称对账=plan:81 直读逐字母比对（A/D/U/C/I/T+G 全中）；三方法：来源层（plan/art 双锚直读）+逻辑层（官方 vs 本土分层自洽）+外部考证层（小昭推断版与官方版逐字母 diff=6 错 4 属实）。

**未做项**：结构层两段式 schema 改造（按边界走 #540）；itingnao 全文拉取（源债已登记）。

**需要谁动作**：欧阳锋终审（重点核英文全称与 plan 文档逐字母对账——对账记录见上）。

## 机器预审报告

> 🤖 机器预审参考层（#515）：仅供欧阳锋终审参考，不构成结论、不放行不拦截

### ① 声称-交付差集

✅ 2 个声明路径全部存在+已跟踪+无脏改动
### ② lint

✅ frontmatter 可解析 + F-034 五字段在位
### ③ 负向判词 / ④ 存在性核查

✅ 执行报告无负向断言词（检查面=执行报告节）
