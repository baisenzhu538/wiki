---
id: dk-ai-does-not-question-your-mistake
title: 「暗知识：AI不质疑你的口误——它只会工整地扩散出去」
type: dk
status: reviewed
confidence: 0.85
trust_level: observed
domain:
  - ai-basic
author: 老顽童
source_refs:
  - 00_inbox/AI基本功/Live258：AI基本功第一课优秀作业.md
source_person: 王鹏飞（Live258 学员）
source_context: Live258 AI基本功第一课优秀作业·王鹏飞「桥之旅」一进多出复盘（L2859-L2887），学员二手自述
reviewed_by: 欧阳锋
aliases:
  - AI不质疑口误
  - 事实扩散
  - DataPack
  - 错误输入放大
  - AI基本功
  - Live258
discoverable_by:
  - 事实扩散
  - 口误扩散
  - DataPack
  - 事实约束
  - AI不质疑
  - 错误放大
related:
  - framework-truman-feature-thinking-core
  - framework-truman-feature-layered-system
  - dk-demand-feature-stacking
  - dk-feature-not-learned-but-used
  - ai-basic-domain-digest
  - case-live258-fact-spread-18-bridges
  - case-live258-zhihu-content-acquisition
  - case-live258-livestream-prompt-v1-v5
  - case-live258-europe-cold-email
tags:
  - method:feature-thinking
  - method:fact-control
  - scene:ai-usage
  - audience:practitioner
  - content-format:dk
  - source-person:student
  - evidence:observed
created_at: 2026-08-12
updated_at: 2026-08-12
quality_labels:
  - insight
  - quotable
  - actionable
diagnostic_signals:
  - signal: "AI输出的数字/事实错了但自己没发现"
    lens: 输入错误被AI无差别放大——人喂的错，AI工整扩散
    follow_up: 关键事实建只读DataPack+负面约束+强制核对，生成前引用、禁止推断
  - signal: "一进多出类任务（1份内容N种交付物）出错后返工量巨大"
    lens: 产线越高效，错误扩散越广——输入保真没跟上
    follow_up: 放量前先做一次事实核对演练，确认输入无错再进产线
review_date: 2026-08-13
---
> 本卡属于 [[framework-truman-feature-thinking-core]] 的暗知识——"事实约束/DataPack"类 Feature 缺失的真实代价（Feature 周期表 2B 格）。实证见 `[[case-live258-fact-spread-18-bridges]]`；与 E020（回答前先检索验证）同构：KDO 铁律"不检索=瞎说"的 AI 侧对应物。

# AI不质疑你的口误——它只会工整地扩散出去

> 一句话：人喂给 AI 的错误输入（口误/笔误/记错），AI 不会质疑，只会以高执行力无差别放大——错误数字被写进全部交付物，返工成本远大于当初做一次核对（实测 L2861）。

---

## 原始表述

王鹏飞（L2861，翻车实录）：

> "桥的数量，我一开始口误说成18座。AI完全顺着我往下写，18这个数字被写进了课程结构、周计划、家长长图。等到要出正式物料时才回溯核对：景区一共24座桥，孩子实际徒步的是17座。18是错的。错误数字在四份物料之间流了一圈，返工成本远大于当初做一次核对。"

> "对照课上，我缺的正是'给DataPack'和'负面约束/输出限制'这两格。AI不会质疑我口误的事实，它只会把它工整地扩散出去。"（L2861）

## 使用场景

| 场景 | 典型症状 | 案例 |
|:---|:---|:---|
| 事实性数字进 prompt | 数量/日期/名单/金额口误或记错，AI 原样采用 | 王鹏飞 18 桥（实测 L2861） |
| 一进多出（1 份内容 N 种交付物） | 错误随产线放大到所有交付物 | 18 扩散进 docx/PDF/长图/任务卡四份物料（实测 L2861） |
| 多轮迭代/长链任务 | 早期错误被后续轮次继承并加固 | jeffgirl 类迭代链（推演，机制同构） |
| 高效产线（组合/自动化） | 产线效率越高，错误扩散越快越广 | 王鹏飞 1C 组合（实测 L2841-L2849） |

## 操作方法

1. **建只读 DataPack（事实包）**：把任务涉及的关键事实（完整名单/数量/里程/位置）建成独立事实包，生成前强制引用、禁止推断（王鹏飞假设 1，L2877-L2879）
2. **负面约束/输出限制**：明确告诉 AI"不得推断、不得补充未提供的数字，缺失则省略"（王鹏飞缺的第二格，L2861）
3. **强制核对节点**：出正式物料前先回溯核对关键数字与事实源（王鹏飞是"等到要出正式物料时才回溯核对"——太晚，L2861）
4. **生成标准内置自检**：让 AI 输出前复述关键事实（类似"反向确认"），人确认后再继续
5. **放量前事实演练**：高效产线（组合/一进多出）上线前，先用小样跑一遍核对流程（预防产线放大效应）

业界印证（诊断报告 §一 组4，2026 共识）：citation-grounded outputs 是最强幻觉抑制器——"模型找不到来源就必须省略或承认缺口"，自纠正闭环；fail-closed（低于阈值拒绝回答而非猜测）也是同一原理。

## 适用边界

| 场景 | 适用？ | 说明 |
|:---|:---|:---|
| 事实性内容（数字/名单/流程） | ✅ 核心场景 | 错误扩散成本最高 |
| 创意类内容（风格/表达） | ⚠️ 部分适用 | 负面约束有用，DataPack 不适用 |
| 纯推演/假设类任务 | ❌ 不适用 | 本来就没事实可核对 |
| 已建立人工核对流程的单件任务 | ⚠️ 边际价值低 | DataPack 主要是防"扩散"而非防"错误" |

> ⚠️ 边界警示（反例）：DataPack 只约束"引用时"，不防"引用前没核对"——王鹏飞的根因链条是"口误（人因）→AI 无差别执行→出正式物料才核对（流程缺位）"。加 DataPack 不等于不会犯错，仍需人工核对节点。正面做法参照农夫三拳的 R/E/S/X 事实分级（L817-L831）：每张图建事实卡并标记来源等级，S 级（AI 场景延展）明确禁止事实性表述——防扩散的完整工程方案。

## 为什么值钱

1. **错误扩散是隐形成本**："返工成本远大于当初做一次核对"（L2861）——一次核对几分钟，四份物料返工数小时到数天
2. **产线放大效应是反直觉的**：高效 Feature（组合/一进多出）放大正确也放大错误——效率越高越需要输入保真配套
3. **这是 Feature 周期表的真实缺口**：诊断确认 DataPack/事实约束类 Feature 在周期表缺失或学员未认识（诊断报告 §二 L2）——本 dk 是该 Feature 家族的证据锚点
4. **AI 的"不质疑"是默认行为不是缺陷**：理解了这一点才能设计"让 AI 自我纠错"的机制（引用约束/强制核对/自检复述），而不是抱怨 AI

## 与其他知识的关联

- `[[case-live258-fact-spread-18-bridges]]`：本 dk 的证据链（翻车实录+40→65 分+5 个 Feature 假设）
- `[[dk-demand-feature-stacking]]`：产线放大效应的机制层——叠加的正向（维度覆盖）与负向（错误放大）并存
- `[[framework-truman-feature-layered-system]]`：DataPack/负面约束属于 2B 格（上下文/生成标准）
- E020（KDO 错误模式库）：回答前先检索验证——本 dk 是同一纪律在 AI 使用侧的映射
- `[[dk-feature-not-learned-but-used]]`：同源暗知识——"用会的"与"防扩散"都是把 Feature 落到真实操作

## Critique

**内部局限**：单案例（王鹏飞一进多出）。"返工成本远大于一次核对"没有量化数字；翻车链条是"口误+AI 扩散+无核对机制"三因素叠加，归因到单一 Feature 缺口是对复杂失败的简化。

**外部攻击者 1（Kahneman 式——事后归因偏差）**：复盘叙事把翻车整齐归因为"缺 DataPack 和负面约束"，但把责任归于"缺 Feature"可能让操作者误以为"加了 DataPack 就不会犯错"——实际 DataPack 只约束"引用时"，不防"引用前没核对"。真正有效的预防是流程节点（核对），而非单一 Feature。

**外部攻击者 2（Taleb 式——幸存者偏差）**：这是"优秀作业"——课程最终做成了，翻车被写成有教育意义的插曲。真实世界中大量同类失败（口误扩散）可能直接导致项目报废而无人复盘——本 dk 提炼的"规律"来自一个幸存案例的失败插曲，样本代表性有限。

**业界反方**：citation-grounded 约束有成本——强制引用/省略会让 AI 在低置信场景拒绝回答或产出缩水内容；过度约束可能降低产出完整性。约束强度需要按任务风险分级，而非一刀切全开。

## 常见失败模式

| 失败模式 | 症状 | 修复 |
|:---|:---|:---|
| 只建 DataPack 不建核对节点 | 事实包建了但错误仍进产线 | DataPack 必须配强制核对节点（生成前+出物料前） |
| 负面约束写得太宽 | AI 连合理推断都不敢做，产出缩水 | 负面约束按任务分级：事实类严格、创意类宽松 |
| 口误直接进 prompt 不核来源 | 18 桥型翻车 | 关键数字先核来源再入 prompt；引用时强制标注来源 |
| 产线放量前无事实演练 | 错误随高效产线瞬间扩散 | 放量前小样核对演练；DataPack 与产线配套上线 |
