---

id: yt-foresight-model-taxonomy
confidence: 0.85
created_at: 2026-06-10
difficulty: beginner
domain:
  - yitang
estimated_tokens: 1200
language: zh-CN
query_triggers:
  - "预判模型"
  - "N要素"
  - "雷达图"
  - Checklist
  - "模型分类"
  - "创业工具"
review_date: 2026-06-10
reviewed_by: "洪七公"
source_refs:
  - src_20260613_96e45c45-qishijian-business-model
source_refs:
  - src_20260613_96e45c45-qishijian-business-model
status: enriched
title: "预判模型分类"
trust_level: medium
type: tool
version: 1
yitang:
  map: entrepreneur
  module: "机会预判"
  course_id: yt-foresight-model-taxonomy
  course_type: tool
  level: core
diagnostic_signals:
  - {'signal': '能根据信息完备度和决策 stakes 快速判断该用 N要素 / 雷达图 / Checklist', 'framework_lens': '模型复杂度要与决策成本匹配', 'follow_up_question': '如果给这个决策限定10分钟，你会降到哪个层级？'}
  - {'signal': '使用每种模型时都配套具体案例，而不是空跑维度', 'framework_lens': '预判模型需要锚定在真实商业案例上', 'follow_up_question': '你最近一次用 Checklist 做尽调时，案例库中是否有≥3个可比案例？'}
  - {'signal': '团队对‘什么时候该升级模型复杂度’有共同约定', 'framework_lens': '工具分层需要决策规则，否则因人而异', 'follow_up_question': '如果两个人分别用 N要素 和 Checklist 评估同一机会，你们会如何裁决？'}
updated_at: 2026-06-13
author: "老顽童"
---

# 预判模型分类

> 来源：一堂课程体系 | [[yt-foresight-business-spectrum]] | [[yt-entrepreneur-opportunity-selection]]

## Summary

一堂将商业预判中常用的分析工具按精细化程度和复杂度分为三个层级：N要素（最糙版）→ 雷达图（常用版）→ Checklist（复杂版）。不同复杂度对应不同的决策场景和信息完备度。

## Claims

### 三层预判工具

| 层级 | 名称 | 特征 | 适用场景 | 典型案例 |
|:---:|:---|:---|:---|:---|
| L1 | **N要素（最糙版）** | 2-3个基本要素，极简归纳 | 快速筛选、初期 brainstorm | 爆款文案三要素、共学活动三原则 |
| L2 | **雷达图（常用版）** | 5-7个清晰完备的维度，可打分 | 中等复杂度决策、团队共识 | 五维雷达图评估、机会评估矩阵 |
| L3 | **Checklist（复杂版）** | 数十条级别的核查清单，配套案例库 | 深度尽职调查、规模化复制前 | 优秀BP黄金27条、投资尽调清单 |

#### L1: N要素（最糙版）

- **一般范式**：2-3个基本要素
- **常见角度**：成功要素 / 必备要素 / 原则
- **典型案例**：爆款文案三要素、海报三要素、共学活动三原则

**使用要点**：追求"少即是多"——用最少的变量抓住核心矛盾。风险在于过度简化导致遗漏关键维度。

#### L2: 雷达图（常用版）

- **基础版本**：5-7个清晰完备的维度
- **加分项1**：每个维度配套案例解读
- **加分项2**：每个维度进行打分评估

**使用要点**：维度选择比打分更重要。5-7个维度应满足MECE（ mutually exclusive, collectively exhaustive）原则。常见错误：维度之间高度相关（如"团队能力"和"执行力"），导致评估失真。

#### L3: Checklist（复杂版）

- **检查清单**：数十条级别的核查条目
- **加分项**：配套范式库 / 模版库 / 案例库

**使用要点**：Checklist的价值不在于"检查"，而在于"防止遗漏"。最佳实践是每条Checklist条目都附带"如果此项不通过，会发生什么"的反面案例。

## Critique

### Atul Gawande（《清单革命》作者）

Gawande的研究表明，Checklist的有效性不取决于条目的多少，而取决于**关键节点的识别**——在复杂系统中，80%的错误可以通过20%的关键检查项预防。一堂的L3 Checklist若不加筛选地堆砌条目，可能陷入" checklist fatigue"（清单疲劳），使用者因条目过多而敷衍了事。

### 建议

预判模型的选择应遵循**"够用即可"原则**：
- 信息极度匮乏 → L1 N要素（快速定位）
- 信息中等、需要团队共识 → L2 雷达图（结构化讨论）
- 信息充分、需要规避风险 → L3 Checklist（系统化排查）

切忌在信息匮乏时用L3（过度工程化），或在信息充分时仍用L1（遗漏关键风险）。

## Constraints & Boundaries

| 边界 | 说明 |
|------|------|
| **适合** | 机会预判、方案筛选、投资决策等需要在不确定下做判断的场景 |
| **适合** | 团队需要统一语言、降低沟通成本的评估流程 |
| **不适合** | 信息完全确定、只需执行的标准化决策 |
| **不适合** | 纯粹创意发散阶段——过早结构化会抑制想法产生 |

### 失败模式

1. **快速筛选也用 Checklist，导致小决策被过度分析**
   - **原因**：模型复杂度与决策重要性不匹配
   - **修复**：给决策 stakes 分级：日常筛选用 N要素，重要决策用雷达图，尽调/复制前用 Checklist

2. **用 N要素 做深度尽调，遗漏关键风险**
   - **原因**：过度简化导致盲区
   - **修复**：当涉及资金/资源投入≥阈值时，强制升级到雷达图或 Checklist

3. **雷达图维度很多，但打分全凭感觉**
   - **原因**：维度缺少锚定案例和评分标准
   - **修复**：每个维度配0/5/10分的具体样例，并让至少两人独立打分后校准

4. **把模型复杂度当成专业度，越复杂越好**
   - **原因**：形式替代了实质
   - **修复**：做完评估后反问：‘如果删掉两个维度，结论会变吗？’不会变的维度应删除

## Synthesis

| 关系 | 目标节点 | 说明 |
|------|---------|------|
| 关联框架 | [[yt-foresight-business-spectrum]] | 终局光谱图——预判规模的L2工具 |
| 关联工具 | [[yt-entrepreneur-opportunity-selection]] | 机会选择——L2雷达图的具体应用 |
| 关联工具 | [[yt-ai-startup-20-risky-hypotheses]] | 20个高风险假设——L3 Checklist的实例 |

## Action Triggers

| 触发场景 | 第一个动作 | 成功指标 |
|---------|-----------|---------|
| 需要快速评估一个创业想法 | 先用L1 N要素（3个核心要素）快速定位 | 5分钟内确定该想法的核心矛盾 |
| 团队对机会评估有分歧 | 升级到L2雷达图，让每个成员独立打分后对比 | 识别分歧集中在哪些维度 |
| 准备融资/重大投入前 | 使用L3 Checklist逐项排查 | 关键风险项全部标注并通过 |

> 视觉标记语义：原图为纵向三层递进结构，左侧模型名称、右侧版本定位标签、下方具体要点。绿色雷达图图标标注L2层级。
