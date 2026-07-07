---

id: tool-ban-fei-mao-zhui-wen-ai-zheng-ju-bing-biao-zhu-xin-yuan
title: 技能：追问 AI 证据并标注信源
type: tool
status: reviewed
domain:
- src_unknown
- yitang- src_unknown
source_person: 半肥猫
source_context: AI俱乐部-AI学习落地 分享
source_refs:
- 10_raw/sources/src_20260617_f1830fa6-半肥猫-ai学习落地-口述.md
tools_required:
- src_unknown
prerequisite_skills:
- src_unknown
related:
  - "[[tool-纪浩-Agent技能市场设计法]]"
  - "[[tool-三阶追问法穷尽决策要素]]"
  - "[[pending_unknown]]"
  - "[[pending_unknown]]"
  - "[[pending_unknown]]"
created_at: 2026-06-07
reviewed_by: 欧阳锋
updated_at: '2026-06-28'
pipeline:
- src_unknown
- src_unknown
- src_unknown
author: 半肥猫
confidence: 0.88
trust_level: medium
diagnostic_signals:
- lens: 证据 vs 推理
  follow_up: 这是 AI 的推理还是证据？如果是证据，具体来源、时间、样本量、方法是什么？
- lens: 可验证性
  follow_up: 这个信源能否通过搜索引擎、数据库或报告原文独立核实？
- lens: 风险分级
  follow_up: 这个场景的错误代价是什么？是否已经验证信源并标注不确定性？

---

# 技能：追问 AI 证据并标注信源

## 用一句话讲清楚

在采信 AI 回答前，先用结构化追问把它从"讨好型回答机"逼成"证据型分析师"，并验证、标注可核实的信源。

## 核心要点

- src_unknown
- src_unknown
- src_unknown
- src_unknown

## 边界

| 维度 | 适用 | 不适用 |
|------|------|--------|
| 任务性质 | AI 帮助做调研、分析、决策支持 | 纯创意发散、脑暴、思维导图 |
| 输出用途 | 需要将 AI 回答转化为可执行方案 | 只需要"灵感"而非"准确" |
| 容错要求 | 低容错场景（金融、医疗、法律、保险） | 假设性讨论、无后果的随意尝试 |
| 时间资源 | 有足够时间验证关键信源 | 时间极度紧张、无法做任何验证 |

## 失败模式

| 失败模式 | 典型症状 | 对策 |
|----------|----------|------|
| 追问不深入 | AI 给出模糊信源或泛泛而谈 | 使用结构化问题清单逐层推进 |
| 盲目相信 AI 信源标注 | 信源是编造的或链接失效 | 用搜索引擎、数据库、报告原文快速检验 |
| 只追问一次 | AI"编得更好看"但未验证 | 多轮迭代追问，直到可验证或明确存疑 |
| 证据仪式感 | 追问的证据不影响决策结果 | 先判断该证据是否改变最终决策 |
| 迷信权威信源 | 权威机构数据也可能有叙事包装 | 结合小数据、一手体感和可验证预测能力评估 |
| 过度追问触发防御性编造 | AI 生成更精致、更像真的假证据 | 明确底线："不要扩写、不要营销话术、不要过度推断" |

## 行动 Checklist

- src_unknown
- src_unknown
- src_unknown
- src_unknown
- src_unknown
- src_unknown
- src_unknown

## 相关卡/互链

- src_unknown
- src_unknown
- src_unknown
- src_unknown
- src_unknown

## 来源

- src_unknown
- 10_raw/sources/src_20260617_f1830fa6-半肥猫-ai学习落地-口述.md

## Feedback Path

- src_unknown

## 目的

> 待补充：这个工具解决什么问题？适用于什么场景？

## 操作步骤

1. **步骤一**：待补充
2. **步骤二**：待补充
3. **步骤三**：待补充

## 不要用的场景

> 待补充：什么情况下这个工具效果有限或不应该使用？

## 质疑

- **具体假设**：该工具假设"追问能让 AI 从'讨好型回答机'变成'证据型分析师'"，但追问本身可能触发 AI 的"防御性编造"——当 AI 被逼问证据时，它会生成更精致、更像真的假证据，而非承认"我不知道"。
- **边界**：在时效性极强的场景中（如突发事件分析），AI 训练数据中没有相关信息，追问只会产生幻觉——此时应转向人工搜索而非持续追问。
- **前提**：该工具的前提是"追问者能判断证据的真伪"，但如果追问者本身缺乏领域知识，就无法区分"真实证据"和"编造的证据"——两者的格式可以完全一样。

**Hugo Mercier**（认知科学家，《The Enigma of Reason》作者）会质疑：人类的"推理"能力本质上不是用来"追求真理"的，而是用来"说服他人"的（论证理论）。当 AI 被追问时，它的行为模式不是"寻找真相"，而是"生成有说服力的回答"——这与追问者的目标完全错位。追问得越深，AI 生产的"伪论证"越精致，追问者越容易被误导。真正的防御不是"追问"，而是"交叉验证"——从独立信源获取同一信息。
