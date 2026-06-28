---

id: tool-ban-fei-mao-yong-skill-zuo-dui-bi-ce-shi-yan-zheng-xiao-guo
title: 技能：用 Skill 做对比测试验证效果
type: tool
status: enriched
domain:
- src_unknown
- yitang- src_unknown
source_person: 半肥猫
source_context: AI俱乐部-AI学习落地 分享
source_refs:
- 10_raw/sources/src_20260619_08606b41_00_inbox_半肥猫_AI学习落地_口述.md
tools_required:
- src_unknown
prerequisite_skills:
- src_unknown
related:
  - [[tool-ban-fei-mao-she-ji-skill-de-ping-fen-gui-ze-yu-feng-xian-bian-jie]]
  - [[tool-半肥猫-课程Skill化的八步工作流]]
  - [[case-ban-fei-mao-skill-ab-test]]
  - [[dk-ban-fei-mao-skill-rejection-value]]
  - [[pending_unknown]]
created_at: '2026-06-07'
updated_at: '2026-06-28'
pipeline:
- src_unknown
- src_unknown
- src_unknown
- src_unknown
author: 半肥猫
reviewed_by: 欧阳锋
confidence: 0.88
trust_level: medium
diagnostic_signals:
- framework_lens: 效果验证缺口
  follow_up_question: 能否设计一组有/无 Skill 的对照测试，用同一套评分标准量化差距？
- framework_lens: 边界盲区
  follow_up_question: 是否已经设计反向/越界测试集，验证 Skill 在边界和高风险场景下的拒绝能力？
- framework_lens: 共识缺失
  follow_up_question: 能否把评价标准事先和 AI/团队约定，用结构化评分替代主观争论？

---

# 技能：用 Skill 做对比测试验证效果

## 用一句话讲清楚

半肥猫提出的 A/B 测试方法：通过"有 Skill"与"没 Skill"的对照测试，用结构化评分验证 Skill 的真实价值，避免把信仰当工具。

## 核心要点

- src_unknown
- src_unknown
- src_unknown
- src_unknown
- src_unknown

## 操作步骤

1. **设计多维度评分标准**——触发范围、结论明确性、场景拆解、技术路径、风险识别、拒绝能力、证据纪律、评分构架、MVP 建议、不夸大承诺、合规性、可观测性
2. **设计正向测试集**——典型适用场景，验证 Skill 在"正常情况下"的表现
3. **设计反向/越界测试集**——故意提交边界或无关场景，验证 Skill 能否正确拒绝
4. **设计高风险场景测试集**——敏感行业或低容错场景，验证 Skill 在压力下的表现
5. **对比两组得分**——方案 A（用 Skill）vs 方案 B（不用 Skill），结构化评分
6. **分析差距来源**——哪些维度的差距最大？为什么？如何改进？

## 边界

### 适用边界

| 边界 | 说明 |
|:-----|:-----|
| ✅ 适合 | 任何需要验证效果的 AI Skill 发布前 |
| ✅ 适合 | 需要证明 Skill 价值的团队内部沟通 |
| ✅ 适合 | 需要比较不同 Skill 版本优劣的迭代优化 |
| ✅ 适合 | 诊断+分析+决策型 Skill 的效果验证 |

### 不适用边界

| 边界 | 说明 |
|:-----|:-----|
| ❌ 不适合 | 纯执行型任务（如写文案、翻译、格式调整）——这套评估维度是为诊断+分析+决策型 Skill 设计的 |
| ❌ 不适合 | 没有明确的"不用 Skill"对照组 ——A/B 测试的前提是有两个可比的组 |
| ❌ 不适合 | 评分者自己对评分维度的定义不清楚 ——评分标准需要在测试前先和 AI 约定好 |

## 失败模式

| 模式 | 症状 | 修复 |
|:-----|:-----|:-----|
| **只做正向测试** | 边界问题被隐藏，上线后用户一越界就崩溃 | 反向测试和正向测试同等重要，必须同时设计 |
| **测试场景不具体** | 评分标准模糊，不同评分者打分差异大 | 每个测试场景都需要具体的业务描述 |
| **评分者不独立** | 评分者带着"希望 Skill 好"的偏见打分 | 如果可能，让第三方独立评分，或先约定标准再盲评 |
| **对照组不可比** | "不用 Skill"的基线太弱或太强，导致差距失真 | 基线必须是同一模型在同一提示下的默认表现 |
| **忽视高风险场景** | 正向测试全过，但医疗/金融/合规场景出错 | 对低容错行业单独设计高风险测试集 |
| **测试结果不迭代** | 测完一次就定论，不再验证改进效果 | 把 A/B 测试作为每次迭代的门禁，重复跑 |

## 行动 Checklist

- src_unknown
- src_unknown
- src_unknown
- src_unknown
- src_unknown
- src_unknown
- src_unknown
- src_unknown

## 工具/环境

- src_unknown
- src_unknown

## 为什么有效

A/B 测试是唯一能分离"技能效果"和"其他因素"的方法。没有对照组，你就无法确定是 Skill 让 AI 变得更好了，还是只是这个场景本身就简单。

## Critique

### 内部局限

- src_unknown

- src_unknown

- src_unknown

### 外部攻击

#### Herbert Simon 的"有限理性"与"评估的成本"

**Herbert Simon**（诺贝尔经济学奖得主，"有限理性"理论提出者）对 A/B 测试方法提出了系统性质疑：

- src_unknown

- src_unknown

- src_unknown

> **Simon 的拷问**："你说 A/B 测试是验证 Skill 的唯一可靠方式。但你知道你的测试成本有多高吗？12 个维度、每个维度 0-3 分、每个测试场景都要两组对比。一个小型团队可能根本没有资源做这种测试。你让 A/B 测试成为了 Skill 的必需项，但这个必需项本身就是一道门槛，把很多人拦在了外面。"

#### Don Norman 的"自动化悖论"与"测试的局限性"

**Don Norman**（*The Design of Everyday Things* 作者，认知心理学家、设计思维专家）从人机交互角度质疑：

- src_unknown

- src_unknown

- src_unknown

> **Norman 的拷问**："你说 A/B 测试是唯一可靠的验证方式。但你知道什么是唯一真正可靠的验证方式吗？是用户在真实世界中的使用。你的测试是在模拟环境中进行的，你用的测试场景是你自己设计的。你在用'你以为用户会怎么用'来替代'用户真的怎么用'。这不是验证，这是假设。"

## Synthesis

| 关系 | 目标节点 | 说明 |
|------|----------|------|
| 上位 | [[tool-ban-fei-mao-she-ji-skill-de-ping-fen-gui-ze-yu-feng-xian-bian-jie]] | 测试需要基于评分规则——两者配套使用 |
| 上位 | [[tool-半肥猫-课程Skill化的八步工作流]] | 八步中的第7步——测试验证 |
| 案例 | [[case-ban-fei-mao-skill-ab-test]] | A/B 测试的完整实例 |
| 暗知识 | [[dk-ban-fei-mao-skill-rejection-value]] | "Skill 的最大价值是拒绝"——测试反向场景是核心 |

## 相关卡/互链

- src_unknown
- src_unknown
- src_unknown
- src_unknown

## 来源

- src_unknown
- 10_raw/sources/src_20260619_08606b41_00_inbox_半肥猫_AI学习落地_口述.md

## Feedback Path

- src_unknown

## 目的

> 待补充：这个工具解决什么问题？适用于什么场景？

## 不要用的场景

> 待补充：什么情况下这个工具效果有限或不应该使用？
