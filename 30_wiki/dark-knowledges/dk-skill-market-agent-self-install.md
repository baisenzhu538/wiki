---

id: dk-skill-market-agent-self-install
title: 暗知识：Skills Market 不是给人看的说明书，而是给 Agent 自安装的自描述
type: dk
dark_knowledge_type: paradigm-shift
status: reviewed
domain:
- ai-collaboration
- yitang
source_person: 纪浩
source_context: AI俱乐部·AI协作方法论分享，第二十二节批次4精修提炼，2026-06-17
aliases:
  - 不是给人看的说明书
  - 暗知识
  - 纪浩
  - 而是给
  - 自安装的自描述
  - 装的自描述
source_refs:
- pending_archive:src_20260606_6ea91aa8-纪浩-AI协作方法论-口述
- src_20260606_6ea91aa8-纪浩-AI协作方法论-口述
confidence: 0.88
trust_level: medium
discoverable_by:
  - 暗知识：Skills Market 不是给人看的说明书，而是
  - 暗知识
  - 不是给人看的说明书，而是给
  - 自安装的自描述
related:
- - - plan_20260621_skill-iteration-standard
- - - dk-ban-fei-mao-skill-rejection-value
- - - case-半肥猫-course-to-skill
- - - tool-ban-fei-mao-yong-skill-zuo-dui-bi-ce-shi-yan-zheng-xiao-guo
- - - case-ban-fei-mao-conversion-hacker-skill
- - - case-ji-hao-skill-market-problem-validation
- - - concept-纪浩-ai-collaboration-five-layer
- - - case-纪浩-from-zip-to-five-layers
- - - case-纪浩-focus-prompt-design
- - - case-半肥猫-course-to-skill
tags:
- audience:executor
- scene:reference
- skill-level:intermediate
author: 老顽童
reviewed_by: 欧阳锋
review_date: '2026-06-19'
created_at: '2026-06-19'
updated_at: '2026-06-19'
diagnostic_signals:
- signal: src_unknown
  framework_lens: 受众错位——Skill 的消费者是 Agent，不是人
  follow_up_question: 拿一条 Skill 出来，让 Agent 纯读这份 Skill 后独立执行一次任务，能跑通吗？不能的话，缺失了什么？
- signal: src_unknown
  framework_lens: 重心倒置——自描述的核心是协议，不是说明
  follow_up_question: 你的 Skill 里有这些吗：输入格式约束、输出格式约束、评分规则、拒绝条件、边界声明？缺了任何一个，Agent 就是在猜。
- signal: src_unknown
  framework_lens: 更多描述 ≠ 更好的自描述——结构化约束比自然语言描述更有效
  follow_up_question: 与其加文字，不如把当前描述中模糊的部分转化为显式规则（输入类型、输出格式、拒绝条件）。Agent 更尊重规则，不尊重建议。#
    暗知识：Skills Market 不是给人看的说明书，而是给 Agent 自安装的自描述
- 协作方法论
---
> 人的工作从"写说明"降级为"跟 AI 说清楚，让 AI 去补全"。

## 原始表述

> Skills Market 不是给人看的说明书，而是给 Agent 自安装的自描述。人的工作从「写说明」降级为「跟 AI 说清楚，让 AI 去补全」。

——纪浩，AI 协作方法论，提炼自第二十二节批次4精修

## 核心洞察

这个洞察翻转了"Skills Market / Skill 市场"的设计哲学：

**传统思路**：Skill 是给人看的操作手册 → 人读了之后操作 → Skill 市场 = 文档库。

**纪浩的思路**：Skill 是给 Agent 读的**自描述文件** → Agent 读了之后自我配置、自我约束、自我执行 → Skill 市场 = Agent 的能力注册中心。

这个翻转有三个层次：

1. **消费者变了。** Skill 的主要消费者不是人，是 Agent。人只是偶尔看一眼。因此 Skill 的"可读性"标准不是"人类是否觉得清晰"，而是"Agent 能否据此独立完成任务"。

2. **内容重心变了。** 传统说明书写"怎么做"，自描述 Skill 写"约束是什么"。输入格式、输出格式、评分规则、拒绝条件、边界声明——这些结构化约束比任何自然语言描述都更能让 Agent 理解边界。

3. **人的角色变了。** 人不再需要"把操作步骤写清楚"（Agent 自己能推理步骤），人需要做的是"把判断标准说清楚"——什么算好、什么算坏、什么情况下该拒绝。这是从"操作者"到"评判者"的角色升级。

更深一层：**这也是 AI 时代知识管理范式的变化**——知识不再被"归档"给人看，而是被"封装"给 Agent 调用。

## 使用场景

- src_unknown
- src_unknown
- src_unknown
- src_unknown
- src_unknown

## 诊断信号

| 信号 Signal | 透镜 Lens | 跟进 Follow-up |
|:
|:---|:---|
| Skill 写给人看但 Agent 读不懂 | 受众错位——Skill 的消费者是 Agent | 拿一条 Skill 让 Agent 独立执行一次任务，测试能否跑通 |
| 建 Skill 花 80% 时间写说明，20% 写协议 | 重心倒置——自描述的核心是协议 | 补齐输入约束、输出约束、评分规则、拒绝条件、边界声明 |
| 一遇到问题就加更多文字描述 | 多描述 ≠ 更好的自描述——Agent 尊重规则 | 把模糊描述转化为显式结构化约束 |
| Agent 从不拒绝任务，哪怕明显超出了 Skill 的适用范围 | 缺失边界声明——Agent 需要知道"什么时候停" | 在 Skill 中显式列出不适用场景和拒绝触发条件 |

## 操作方法

1. **用"Agent 独立执行测试"代替"人审阅"**
   写完一条 Skill 后，不让人类审阅者打分。直接把 Skill 文档 + 一个测试任务扔给 Agent，看它能不能独立完成。不能 → Skill 不合格。

2. **Skill 的必含五要素**
   每条 Skill 必须包含：
   - src_unknown
   - src_unknown
   - src_unknown
   - src_unknown
   - src_unknown

3. **人写"判断"，Agent 推"操作"**
   人不再写操作步骤。人写：好的输出长什么样、坏的输出长什么样、边界在哪里。Agent 自己推理怎么操作。

4. **Skill 质量 = 被 Agent 成功调用的次数**
   衡量一个 Skill 好不好的指标，不是"文档写了多少字"，而是"过去一个月 Agent 成功调用它完成了多少次任务，其中多少次无需人工干预"。

## 适用边界

| 边界 | 说明 |
|:-----|:-----|
| **适用于 Agent-native 系统** | 如果你的系统没有 Agent 自动调用 Skill 的能力，这条暗知识暂时用不上（但不代表不重要）。 |
| **不适用安全/合规关键操作** | 涉及资金、法律、安全的操作，Agent 不能独立执行，必须有人的签字节点。 |
| **需要 Skill 生态已具雏形** | 如果只有 3 条 Skill 且没有 Agent 自动调用机制，先建机制，再谈自描述。 |
| **人的判断力不会被替代** | 自描述让 Agent 能执行，但执行结果的终审仍然需要人。 |

| 失败模式 | 典型症状 | 修复方法 |
|---|---|---|
| 说明书式 Skill | Skill 很长但全是自然语言操作步骤，Agent 执行时因缺少约束而"自由发挥" | 把操作步骤改为结构化约束 |
| 无拒绝条件 | Agent 无论什么场景都尝试执行，在不可执行的任务上浪费 Token 或产生错误输出 | 为每条 Skill 加显式拒绝触发条件 |
| 自描述 ≠ 自测试 | 写完约束但没有配测试用例，不知道 Agent 能否正确执行 | 每条 Skill 配至少 2 条测试用例（1 好场景 + 1 边界场景） |
| 人机混用不区分 | 同一条 Skill 既给人看又给 Agent 读，两边都不满意 | 人读的说明文字放 `description` 字段，Agent 读的约束放 `constraints` 字段 |
| 只写"怎么做"，不写"怎么判" | Agent 执行了但无法自评质量，结果全靠人复核 | 加评分规则和好坏示例 |

## 为什么值钱

- src_unknown
- src_unknown
- src_unknown
- src_unknown

## 与其他知识的关联

- src_unknown
- src_unknown
- src_unknown
- src_unknown
- src_unknown
