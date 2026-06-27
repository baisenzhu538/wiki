---


id: yt-research-user-jtbd
title: 用户JTBD访谈工具：区分"说的"和"真正要的"
type: tool
status: enriched
domain:
  - src_unknown
language: zh-CN
version: 1
confidence: 0.88
source_refs:
  - 10_raw/sources/src_20260606_f6cb0868-一堂-机会预判课-Truman-口述.md
  - 00_inbox/调研专题/一堂-用户调研实操课-口述.docx
  - 00_inbox/调研专题/一堂-用户调研实操课-笔记.txt
related:
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
query_triggers:
- src_unknown
- src_unknown
- src_unknown
- src_unknown
created_at: '2026-06-10'
updated_at: '2026-06-18'
estimated_tokens: 2600
tags:
- src_unknown
- src_unknown
- src_unknown
pipeline:
- src_unknown
diagnostic_signals:
- src_unknown
  framework_lens: JTBD = 任务视角
  follow_up_question: 用户最近一次使用类似产品时，想解决什么任务？
- src_unknown
  framework_lens: 任务地图完整画像
  follow_up_question: 如果不解决这个任务，用户会怎样？
- src_unknown
  framework_lens: JTBD的输出是任务陈述
  follow_up_question: 你能用"当我想要____，以便____"描述用户任务吗？
author: unknown
reviewed_by: 欧阳锋
trust_level: medium

---

# 用户JTBD访谈工具：区分"说的"和"真正要的"

> 一句话：JTBD用户访谈是一套基于"用户雇佣产品完成任务"视角的深度访谈工具，通过区分"用户说的"和"真正要的"，帮你在产品早期发现真实需求、避免被功能请求误导。

## 用一句话讲清楚

用户不是因为"喜欢某个功能"而买产品，而是因为要"完成某个任务"才"雇佣"产品；JTBD访谈通过追问场景、任务、动力、阻力与代理品，把"用户嘴上说的功能需求"还原成"用户真正想解决的任务"。

## 核心要点

- src_unknown
- src_unknown
- src_unknown
  1. 用户分层与场景拆解（Who / When/Where / Job / Outcome）
  2. JTBD访谈提纲（任务探索、代理品追问、动力追问、阻力追问、结果追问、演变追问）
  3. 代理品分析（什么都不做、现有产品、DIY/人工等替代方案）
  4. 需求优先级排序（频率 × 痛苦程度 × 现有方案缺陷）
- src_unknown
- src_unknown

## 边界

| 维度 | 适合 | 不适合 |
|------|------|--------|
| **阶段** | 产品早期、创新阶段、需求尚未明确 | 需求已明确、只需执行迭代的成熟产品 |
| **目标** | 理解用户真实动机、避免被功能请求误导 | 快速验证已知功能或收集满意度反馈 |
| **资源** | 能接触到真实用户，具备基础访谈能力 | 无法接触真实用户或团队无访谈能力 |
| **决策类型** | 任务可被用户用语言相对清晰地描述 | 情感驱动、冲动消费或高度无意识决策 |

## 失败模式

| 失败模式 | 常见症状 | 原因 | 修复方法 |
|----------|----------|------|----------|
| **用户说要什么功能就记录什么** | 需求列表全是"加XX功能" | 把愿望当需求 | 每个功能请求后追问："你想用这个完成什么任务？" |
| **忽视用户实际行为，只听口头回答** | 访谈结论与实际使用数据矛盾 | stated preference bias | 要求用户描述最近一次相关场景的具体行为 |
| **任务陈述过于宽泛，无法指导设计** | Jobs Statement 写不出或太抽象 | 颗粒度不足 | 加入具体场景、触发条件和期望结果 |
| **访谈了很多用户但没有提炼出优先级** | 团队仍然争论"做什么" | 缺少收敛 | 按任务频率、重要性、现有方案满意度排序 |
| **把JTBD当成唯一真理** | 忽略情感、社会结构、无意识动机 | 过度理性化 | 搭配情感场景测试、ZMET 或利益相关方映射 |

## 行动 Checklist

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

## 相关卡/互链

| 关系 | 目标节点 | 说明 |
|------|----------|------|
| 上位框架 | [[yt-research-osl-framework]] | JTBD 是 OSL 第 4 步"获取情报"的用户端工具 |
| 关联工具 | [[yt-research-expert-interview]] | 专家访谈技巧可用于 JTBD 访谈 |
| 关联工具 | [[yt-research-hypothesis-test]] | JTBD 结论需要转化为可验证的假设 |
| 关联框架 | [[yt-entrepreneur-key-hypotheses]] | 关键假设验证中的需求假设 |
| 关联工具 | [[yt-research-intelligence-map]] | 13+ 渠道穷尽手段 |
| 关联工具 | [[yt-panproduct-demand-need-discovery]] | 需求发现与泛产品视角 |

---

## 附录：详细组件参考（保留）

### 组件一：用户分层与场景拆解

| 维度 | 问题 | 示例 |
|------|------|------|
| **用户**（Who） | 谁是你的目标用户？ | 年轻白领、二胎家庭、创业老板 |
| **场景**（When/Where） | 什么时候/地点触发需求？ | 早晨通勤路上、睡前床上、周末家庭聚会 |
| **任务**（Job） | 用户想完成什么任务？ | 打发时间、解决饥饿、建立社交连接 |
| **结果**（Outcome） | 完成任务后想达到什么状态？ | 不无聊、不饿、不孤独 |

操作流程：
1. 列出所有可能的用户群体；
2. 对每个群体，列出 3-5 个典型使用场景；
3. 对每个场景，描述用户想完成的"任务"和想达到的"结果"。

### 组件二：JTBD 访谈提纲

| 问题类型 | 具体问题 | 目的 |
|----------|----------|------|
| 任务探索 | 那时候你想解决什么问题？为什么是这个问题？ | 探索真实任务 |
| 代理品追问 | 如果没有这个产品，你会怎么做？ | 理解真正的替代品 |
| 动力追问 | 你为什么想解决这个问题？不解决会怎么样？ | 探索内在动机 |
| 阻力追问 | 你用这个产品时遇到什么困难？有什么不满意？ | 找到现有解决方案的缺陷 |
| 结果追问 | 解决之后你想达到什么状态？ | 明确成功标准 |
| 演变追问 | 如果有一个产品能更好解决这个问题，它应该是什么样的？ | 探索未被满足的需求 |

关键原则：
- src_unknown
- src_unknown
- src_unknown

### 组件三：代理品分析

| 代理品 | 优点 | 缺点 | 启示 |
|--------|------|------|------|
| 什么都不做 | 成本为 0 | 问题没解决 | 这个需求是否真的存在？ |
| 现有产品 A | 已有习惯 | 有某些缺陷 | 用户为什么没有转到更好的产品？ |
| 现有产品 B | 功能更多 | 使用更复杂 | 简单性 vs 功能性的权衡点在哪里？ |
| DIY/人工 | 完全自定义 | 时间成本高 | 用户愿意为什么付出额外努力？ |

### 组件四：需求优先级排序

| 维度 | 问题 | 排序标准 |
|------|------|----------|
| 频率 | 用户多久遇到一次这个任务？ | 频率越高越重要 |
| 痛苦程度 | 任务失败的后果多严重？ | 痛苦越大越重要 |
| 现有解决方案缺陷 | 现有产品解决得多好？ | 解决得越差越重要 |
