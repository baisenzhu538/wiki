---
id: task_20260704_wangyuyan-knowledge-data-decoupling-framework
type: task
status: reviewed
assignee: claude
reviewer: 欧阳锋
priority: P1
created_at: 2026-07-04
updated_at: '2026-07-04T16:57:07.016241+00:00'
related:
- '[[framework-yihang-knowledge-data-decoupling]]'
- '[[concept-yihang-dual-triangle-core]]'
- '[[tool-agent-spec-yitang-customer-segmentation]]'
reviewed_by: 欧阳锋
review_date: '2026-07-04'
---

# 任务 #84：知识层与数据层解耦 framework 卡

## 来源

口述稿 L5025-5078。Truman 解释了 YAI 的关键架构决策：把系统核心词（审美+体系）和 data pack（最小数据单位）分开生产，插件式组合。

当前这个洞察被埋在 #70（blocked）的 `framework-yihang-knowledge-data-decoupling` 里。但它是独立的方法论——不是"课后闲聊的副产品"，是双三角在 Agent 架构层的直接落地。

## 任务目标

产出 1 张 framework 卡，独立成卡，不等 #70 解锁。

## 核心内容

### 1. 解耦模型

```
系统核心词层（审美+体系）     ← 人类三角
    +                         ← 解耦
data pack 层（数据+场景+基本功） ← AI 三角
    ↓ 插件式组合
完整 Agent prompt
```

### 2. 为什么解耦

- 核心词稳定、变化慢（审美和体系是长期积累的）
- data pack 需要频繁更新（新案例、新数据、新场景）
- 不分开放一起，每次更新数据都要重写整个 prompt
- 分开后：partner 聊宏观不行→挂人生观 data pack；聊单元模型不行→挂单元模型 data pack

### 3. 对 KDO Agent 设计的直接启示

- KDO 的 card = data pack 的原材料。每张卡编译后就是一个最小数据包
- Agent 不应该是巨大 system prompt——应该是核心词 + 按需挂载的 data pack
- 这直接对接 #59（Prompt 编译器）和 #73（Agent 执行模式）

### 4. 操作步骤

1. 识别 Agent 需要哪些"不变的核心判断" → 写成核心词
2. 识别哪些知识需要随场景/用户/数据变化 → 拆成 data pack
3. 建立 data pack 的挂载/更新机制
4. 组合编译成最终 prompt

## 验收标准

- `kdo pre-submit` PASS
- `kdo lint` 0 新增 ERROR
- 解耦模型图清晰
- 至少引用口述稿 L5025-5078 原文
- 对 KDO 设计的启示段落明确
- related ≥ 5
- 欧阳锋终审通过
