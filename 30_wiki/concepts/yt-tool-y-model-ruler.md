---
id: yt-tool-y-model-ruler
component_of:
- src_unknown
confidence: 0.85
created_at: 2026-06-06
difficulty: advanced
domain:
- src_unknown
estimated_tokens: 3400
language: zh-CN
prerequisites:
- src_unknown
- src_unknown
query_triggers:
- src_unknown
- src_unknown
- src_unknown
- src_unknown
- src_unknown基准权重
- src_unknown
- src_unknown
- src_unknown
- src_unknown
- src_unknown
related:
- "[[yt-tool-best-practice-learning]]"
- "[[yt-tool-fab-persuasion]]"
- "[[yt-tool-foresight-canvas]]"
review_by: 2026-12-06
reviewed_by: 黄药师
source_refs:
- 10_raw/sources/src_20260613_96e45c45-qishijian-business-model.md
status: enriched
title: Y模型尺子刻度法：从模糊经验到可复用评估模型
type: tool
version: 1
pipeline:
- src_unknown
- src_unknown
- src_unknown
diagnostic_signals:
- framework_lens: 因果规律 / 维度有效性
  follow_up_question: 评估维度是否覆盖了结果的真实驱动因素？
- framework_lens: 可操作化 / 去模糊
  follow_up_question: '''不错''''很好''等描述是否被替换为具体阈值？'
- framework_lens: 风险管理 / 非线性
  follow_up_question: 总分最高但存在致命缺陷的选项是否仍被选中？
- framework_lens: 系统配置 / 资源匹配
  follow_up_question: 均衡型与偏科型选项是否被差异化决策？
updated_at: '2026-06-16'
author: 老顽童
trust_level: medium-high
---

## Summary

> **一句话**：“我觉得这个人不错”不是评估，是猜测。真正的评估是：**用一套“尺子”量化每个维度，用“刻度”确定打分标准，用“基准”找到参照系，用“权重”告诉你哪些维度值得花更多时间”。

Y 模型尺子刻度法是一堂在投资、招聘、选品等高风险决策场景中反复验证的定量评估框架。它从“模糊的经验”中提炼出四层结构：**尺子（评估维度）→ 刻度（打分标准）→ 基准（参照系）→ 权重（重要性分配）**。核心洞见：Y 模型的“因果规律”不仅是“理解了因果”，更是“能用一套定量工具预测结果”——**没有刻度的尺子不是尺子，是棍子。

## Claims

### claim:01 [conf=0.90][src: Y模型实操口述版] 四层评估框架：尺子 → 刻度 → 基准 → 权重

| 层级 | 问题 | 例子（招聘场景） | 常见错误 |
|------|------|----------------|---------|
| **尺子** | 我评估什么？ | 领导力、创始人韧性、单元模型 | 尺子太多（10+个）或太少（1-2个），没有覆盖关键维度 |
| **刻度** | 每个尺子怎么打分？ | 领导力=1-5分：1分=只能管自己，5分=能管理100+人团队 | 刻度模糊（"还行“"一般“"不好“），不同评估者打分差异大 |
| **基准** | 打出的分相当于什么水平？ | 创始人韧性的基准 = “能在公司倒闭前夜睡着觉” | 没有基准，打分变成"和自己比“而非"和行业比“ |
| **权重** | 哪些尺子对最终结果影响最大？ | 团队占30%、市场占30%、产品占20%、财务占20% | 所有尺子权重相同，或权重出自主观感觉而非数据验证 |

> **关键原则**：每个尺子必须可**单独打分、单独改变**——如果两个尺子总是同时变化（如"团队能力“和"领导力“总是一起高一起低），说明它们是同一个尺子的两个面，应合并。

### claim:02 [conf=0.88][src: Y模型实操口述版] 三种常见应用场景

- src_unknown
  - src_unknown
  - src_unknown
  - src_unknown
  - src_unknown
  - src_unknown

- src_unknown
  - src_unknown
  - src_unknown
  - src_unknown
  - src_unknown
  - src_unknown

- src_unknown
  - src_unknown
  - src_unknown
  - src_unknown
  - src_unknown
  - src_unknown

### claim:03 [conf=0.85][src: Y模型实操口述版] “风险红线”比“总分”更重要

- src_unknown
- src_unknown
  - src_unknown
  - src_unknown
  - src_unknown
- src_unknown
- src_unknown

## Critique

### Constraints

1. **尺子刻度法假设维度独立**：实际上大多数评估维度高度相关（如"团队能力“和"领导力“），简单加权重会重复计算相关维度，导致“某些方面被过度加权”
2. **刻度的主观性**：即使有明确刻度，不同评估者打分差异仍然很大（如“领导力”到底是3分还是4分），需要多人打分取平均
3. **权重难以验证**：权重通常出自主观判断，缺少数据验证“这个权重是否真的对结果预测最准”
4. **静态模型难以应对动态环境**：尺子刻度法建立的是静态模型，但市场、团队、产品都在变化，模型需要定期更新

### External Attackers

> **攻击者A：统计学家 / 数据科学家（数据范式）**
> 
> 「尺子刻度法是一种‘加权线性模型’，但这种模型有三个严重缺陷：(1) 假设维度独立——实际上维度高度相关，简单加权会重复计算；(2) 假设线性关系——实际上某些维度在低分时对结果的负面影响远大于高分时的正面影响（非线性）；(3) 没有置信区间——你给一个人打了 3.5 分，但这个 3.5 分的不确定性是多少？如果换一个评估者可能是 2.5 分，这个区间你考虑了吗？一个没有置信区间的‘定量’模型，比一个有置信区间的‘定性’判断更危险——因为它给了你一种‘精确的错误’。”
> 
> **回应**：统计学家的批评是精准的。本卡的回应是：尺子刻度法**不是“精确的定量模型”**，而是““模糊经验的结构化”**——它的价值不在于“打出精确的 3.5 分”，而在于“让评估者意识到自己在哪些维度上存在偏差”。对于需要更高精度的场景，应该在尺子刻度法之上叠加统计方法（如 A/B 测试、回归分析），而非用本卡替代统计方法。

> **攻击者B：认知偏差研究者（心理学范式）**
> 
> 「人类打分本身就带有系统性偏差。光环效应：一个人在A维度上表现得好，你会自动给他B维度也打高分。锚定效应：第一个打分的人的分数会锚定后面所有人的判断。可得性偏差：你会给那些你能轻松想起来的例子打更高分。你们的‘尺子刻度法’建立在‘人类打分是可靠的’这个假设上，但这个假设本身就是假的。更危险的是，当你有了一套‘看似科学的’评估工具，你会更加确信自己的偏差是正确的——这种‘工具加持的自信’比‘没有工具的自信’更危险。”
> 
> **回应**：认知偏差研究者的批评是有力的——**尺子刻度法并不能消除偏差，只能“暴露偏差”**。本卡的回应是：(1) 强制要求多人独立打分后取平均，减少个人偏差；(2) 每次打分后要求打分人写下"为什么给这个分数“，让隐性偏差显性化；(3) 最重要的——定期回顾“打分和实际结果的差距“，让偏差自己暴露自己。

## Cases

### 成功案例：一堂投资评估从“感觉”到“模型”

- src_unknown
- src_unknown
- src_unknown
  - src_unknown
  - src_unknown
  - src_unknown
  - src_unknown
- src_unknown
- src_unknown

### 失败/边界案例：“模型”变成“榴子”

- src_unknown
- src_unknown
- src_unknown
- src_unknown

### 反常识案例：“分布形状”比“总分”更重要

- src_unknown
- src_unknown
  - src_unknown
  - src_unknown
- src_unknown
- src_unknown

## Constraints & Boundaries

| 边界 | 适用 | 不适用 |
|---|---|---|
| 决策类型 | 高风险、多维度评估 | 低 stakes、单一维度 |
| 信息状态 | 维度可定义、可获取基准 | 完全无基准、无数据 |
| 目标 | 选择/排序/淘汰 | 创造性发散 |
| 组织阶段 | 需要团队对齐决策标准 | 决策者个人偏好即可 |

### Common Failure Modes
1. **尺子维度拍脑袋** → 症状：评估维度遗漏关键驱动因素；原因：未先做需求分析；修复：尺子维度必须来自需求分析或因果规律
2. **刻度模糊无基准** → 症状：评分变成'不错''很好'；原因：缺少具体阈值和参照系；修复：每个维度定义 1-5 分具体刻度
3. **只看总分不看分布** → 症状：选了总分高但有致命缺陷的选项；原因：未用风险红线；修复：设定并执行一票否决红线
4. **忽视分布形状** → 症状：均衡型与偏科型被同样决策；原因：只看总分；修复：根据资源能力匹配分布形状
5. **权重缺失或平均** → 症状：所有维度同等重要；原因：未区分杠杆维度；修复：强制权重差异 ≥2 倍
## Synthesis

### Wikilinks

- 待补充链接
- 待补充链接
- 待补充链接
- 待补充链接
### Contradictions

- 待补充链接
- 待补充链接
## Feedback

### 摩擦记录

- src_unknown
- src_unknown
- src_unknown
- src_unknown
