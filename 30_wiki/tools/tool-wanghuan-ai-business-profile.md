---
id: tool-wanghuan-ai-business-profile
title: 王欢AI业务档案5字段工具
type: tool
status: reviewed
domain: src-unknown
created_at: '2026-06-19'
updated_at: '2026-06-28'
author: 王语嫣
reviewed_by: 欧阳锋
confidence: 0.88
trust_level: medium
source_person: 王欢
source_context: 王欢 AI 实战分享（2026-06-18 授课）
aliases:
  - 业务档案
  - 字段工具
  - 王欢
  - 王欢AI业务档案5字段工具
source_refs:
- src_unknown
- src_unknown
- src_unknown
diagnostic_signals:
- lens: context-loss
  follow_up: 检查业务档案是否已固化为 system prompt 或对话开头注入
- lens: standard-drift
  follow_up: 检查"我的风格偏好"与"我的输出标准"是否写了可验证的负面约束
- lens: tacit-rule-gap
  follow_up: 补充"行业暗规则"字段，把"不说但默认"的规矩写成否定句
- lens: role-ambiguity
  follow_up: 把个人/团队业务档案作为共享上下文资产统一注入
discoverable_by:
  - 王欢AI业务档案5字段工具
related:
- '[[concept-wanghuan-tacit-knowledge-examples]]'
- '[[pending_unknown]]'
- '[[pending_unknown]]'
- '[[pending_unknown]]'
- '[[pending_unknown]]'
- '[[tool-ai-critical-reading-three-layers]]'
tags:
- src_unknown
- src_unknown
- src_unknown
- src_unknown
- src_unknown
- audience:executor
- scene:execution
- skill-level:intermediate
---
# 王欢AI业务档案5字段工具

> **Burn line**: 每次新对话，第一步先把你的业务档案粘进去。
>
> **来源**：王欢 AI 实战分享（2026-06-18）

---

## 用一句话讲清楚

AI 业务档案是一个 5 字段模板，用来在每次与 AI 协作前，快速定义**你是谁、你服务谁、你的风格、你的行业暗规则、你的输出标准**，让 AI 从"面对一个陌生人"变成"住在你的业务里"。

---

## 核心要点

1. **上下文工程的第一块砖**：它不是单次提示词技巧，而是跨对话积累的"角色与标准资产"。
2. **暗规则是差异化来源**：通用 AI 知道行业常识，但不知道你组织里"不说但默认"的规矩。
3. **标准是乘数，不是加数**：最终质量 = 你的标准 × AI 的执行力 × 迭代次数。标准为零，结果为零。
4. **可复用 > 一次性**：档案写完后，每次新对话粘贴即可，避免重复交代背景。
5. **与 BTICOE 互补**：档案回答"长期稳定的我"，BTICOE 回答"这次具体任务"。

---

## 五个字段

| 序号 | 字段 | 英文 | 核心问题 | 填写示例 |
|:---|:---|:---|:---|:---|
| 01 | 关于我 | About Me | 你的角色和核心职责是什么？ | 我是知识工厂的质量负责人，负责 wiki 卡片进入和出去的质量把关 |
| 02 | 我服务谁 | Who I Serve | 你的客户/上级在乎什么？ | 内容生产者需要清晰标准，审查者需要可追溯的证据链 |
| 03 | 我的风格偏好 | My Style | 你的表达习惯是什么？ | 简洁、结构化、少修辞、多用表格和 checklist |
| 04 | 行业暗规则 | Tacit Rules | 哪些事不说但默认要遵守？ | 卡片必须有 source_refs；给客户的报价留 8% 谈判空间；收到简历 48 小时内未回复，offer 接受率降 30%（详见 `[[concept-wanghuan-tacit-knowledge-examples]]`） |
| 05 | 我的输出标准 | My Standards | 你的底线是什么？（不是格式） | 事实准确、逻辑自洽、可执行、有明确的 Action Trigger |

> **第 4 个字段"行业暗规则"是王欢标星的重点**——高手和 AI 的差距，往往就在这些"不说但默认"的规则上。

---

## 使用模板

```markdown
## AI 业务档案

### 01 · 关于我 / About Me
- src_unknown
- src_unknown
- src_unknown

### 02 · 我服务谁 / Who I Serve
- src_unknown
- src_unknown
- src_unknown

### 03 · 我的风格偏好 / My Style
- src_unknown
- src_unknown
- src_unknown

### 04 · 行业暗规则 / Tacit Rules ⭐
- src_unknown
- src_unknown
- src_unknown

> 参考示例：`[[concept-wanghuan-tacit-knowledge-examples]]`（招聘 48 小时回复规则、招投标 95% 报价规则、报价 8% 谈判空间等）

### 05 · 我的输出标准 / My Standards
- src_unknown
- src_unknown
- src_unknown
```

---

## 边界

| 适用 | 不适用 |
|:---|:---|
| 与 AI 建立长期、重复协作关系前，先做一次角色注入 | 一次性、临时性的问答（用 BTICOE 更轻量） |
| 个人或团队需要统一 AI 输出风格和标准 | 完全没有行业经验、写不出暗规则的新手首次尝试 |
| 设计 agent/skill 的角色定义和 system prompt | 把档案当作"万能咒语"，以为填完就无需验收 |
| 高频复用的工作流、产品化工具 | 低频、一次性任务，写档案的成本高于收益 |
| 有明确红线和质量底线的专业领域 | 追求创意发散、不需要固定约束的头脑风暴 |

---

## 失败模式 / 常见走偏

| 走偏模式 | 表现 | 纠偏动作 |
|:---|:---|:---|
| **暗规则缺失** | AI 输出违反行业常识 | 把"不说但默认"的规则写出来 |
| **标准太泛** | "输出要高质量" | 把高质量拆成可检查的标准 |
| **角色标签化** | "你是一个专家" | 用场景和职责替代标签 |
| **档案不更新** | 业务变了但档案没变 | 每季度复盘一次 |
| **只写正面要求** | AI 不断加你不想要的内容 | 补充"不要做什么"的负面约束 |
| **把格式当标准** | "用表格输出"当作底线 | 区分格式偏好与质量红线 |

---

## 行动 Checklist

- src_unknown
- src_unknown
- src_unknown
- src_unknown
- src_unknown
- src_unknown

---

## 相关卡 / 互链

- src_unknown
- src_unknown
- src_unknown
- src_unknown

---

## Critique


**Herbert Simon**（诺贝尔经济学奖得主）会质疑：所有模型都是对现实的简化——模型越精确，它对边缘情况的失效就越突然。
**攻击者 1：提示词工程师**
> "每次对话开头粘一大段档案，太啰嗦。直接把要求写进单次 prompt 就够了，效率更高。"
>
> **回应**：单次 prompt 适合一次性任务。当你面对高频、重复、多人协作的场景时，重复交代背景的成本远高于一次性写好档案。提示词工程师关注"这一次怎么写好"，上下文工程关注"长期怎么让 AI 住进来"。

**攻击者 2：组织变革怀疑者**
> "团队每个人写一份档案，标准不统一，反而更乱。而且暗规则写出来，新人也未必能遵守。"
>
> **回应**：这正是需要把个人档案升级为"团队共享上下文资产"的原因。暗规则不是写一次就完，而是要在真实使用中迭代。初期允许不一致，通过验收反馈收敛到团队标准。

**不要用**：
- src_unknown
- src_unknown
- src_unknown
- src_unknown

---

## Synthesis

AI 业务档案的本质，是把"你的判断力"外化成结构，让 AI 和其他协作者可以复用。它不是提示词工程的一部分，而是上下文工程的起点。王欢在课程中反复强调，真正拉开 AI 输出质量差距的，不是工具，而是"你愿不愿意先把你是谁、你的规矩、你的标准说清楚"。当档案写得足够具体时，AI 会从"面对一个抽象用户"变成"面对一个有明确判断力的协作者"，输出质量会稳定提升。

这套工具最适合作为个人或团队的"AI 协作基础设施"来建设：先用 5 字段把长期稳定的角色和标准固定下来，再用 BTICOE 处理每一次具体任务，最后通过验收清单和迭代把隐性经验持续沉淀回档案。它的边界也很清楚——如果你只是临时问一个问题，不需要它；但如果你要做出一个"下周还会用"的产品、设计一个 agent、或者让团队 AI 输出风格一致，那么它就是第一步。

---

*基于王欢 2026-06-18 AI 实战分享整理。*

## 目的

> 待补充：这个工具解决什么问题？适用于什么场景？

## 操作步骤

1. **步骤一**：待补充
2. **步骤二**：待补充
3. **步骤三**：待补充

## 不要用的场景

> 待补充：什么情况下这个工具效果有限或不应该使用？
