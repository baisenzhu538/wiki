---

id: dk-wanghuan-output-equals-standard-times-iteration
title: 王欢暗知识：输出质量 = 标准 × 迭代
type: dk
dark_knowledge_type: insight
status: enriched
domain:
- src_unknown
- src_unknown
- src_unknown
created_at: '2026-06-19'
updated_at: '2026-06-20'
author: 老顽童
reviewed_by: 欧阳锋
confidence: 0.88
trust_level: medium
source_person: 王欢
source_context: 王欢 AI 实战分享课后问答（2026-06-18）
source_refs:
- 10_raw/sources/src_20260619_536bca67_wanghuan_actor_director_oral.txt
- 10_raw/sources/src_20260619_a3a2a803_wanghuan_actor_director_notes.txt
related:
  - src_unknown
  - src_unknown
  - src_unknown
  - src_unknown
  - src_unknown
  - src_unknown-double-triangle
  - src_unknown
  - src_unknown
  - src_unknown
diagnostic_signals:
- signal: src_unknown
  framework_lens: 输出=标准×迭代——标准高但迭代少，输出质量不高
  follow_up_question: "你强制至少3轮迭代了吗？每轮迭代都有明确的验收标准吗？"
- signal: src_unknown
  framework_lens: 输出=标准×迭代——迭代多但标准不提升，输出质量不高
  follow_up_question: "每轮迭代前，你明确验收标准了吗？标准是否在迭代中提升？"
- signal: src_unknown
  framework_lens: 输出=标准×迭代——检查是标准不够还是迭代不够
  follow_up_question: "你的标准维度有几个？迭代次数是多少？两个乘数哪个更低？"
- signal: src_unknown
  framework_lens: 输出=标准×迭代——迭代成本失控，需要设定终止条件
  follow_up_question: "你设定迭代上限了吗？连续两轮无重大问题就应该终止。"
- signal: src_unknown
  framework_lens: 输出=标准×迭代——团队需要统一最低迭代次数和验收标准
  follow_up_question: "团队有统一的最低迭代次数和验收标准吗？"
tags:
- src_unknown
- src_unknown
- src_unknown
- src_unknown
- src_unknown
- src_unknown
---
# 王欢暗知识：输出质量 = 标准 × 迭代

> **Burn line**: 不要追求一次写对。输出的追踪指标 = 你的标准 × 迭代次数。

## 原始表述

王欢在课后闲聊中给出一个简洁公式：

```
输出质量 = 标准 × 迭代
```

这意味着：标准高但迭代少，输出质量不高；迭代多但标准不提升，输出质量也不高。很多人只优化提示词（想一次写对），但忽略了**迭代次数**这个乘数。

## 使用场景

- **创意/设计/内容/方案类任务**：标准可以逐步清晰的探索性任务
- **个人任务质量提升**：从 60 分到 90+ 分的系统化方法
- **团队流程设计**：把“标准 × 迭代”设计成统一工作流
- **产品系统固化**：把迭代固化成系统能力
- **AI 输出质量诊断**：AI 输出总是 60-70 分时，检查标准和迭代哪个不够

## 操作方法

1. **个人任务三层应用**：
   - 低标准+1 次迭代 = 60 分
   - 中标准（BITCOE 定义）+3 次迭代 = 80 分
   - 高标准（业务档案+最佳实践对照）+5-8 次迭代 = 90+ 分
2. **团队流程设计**：
   - 统一最低迭代次数（如至少 3 轮）
   - 统一验收标准模板
   - 建立版本对比和反馈记录
3. **迭代终止条件**：
   - 设定迭代上限（如 8 轮）
   - 连续两轮无重大问题即终止
   - 每轮迭代前明确验收标准
4. **导演模型应用**：
   - 导演不是一次把话说清楚
   - 在“发现不对 → 精确描述 → 要求修改”中把标准磨清楚

## 适用边界

| 适用 | 不适用 |
|:---|:---|
| 创意、设计、内容、方案类任务 | 需要实时响应、单次必须正确的任务 |
| 标准可以逐步清晰的探索性任务 | 有硬性合规、安全红线的任务 |
| 个人或小团队学习期 | 大规模标准化生产（需控制迭代成本） |

## 为什么值钱

1. **纠正提示词崇拜**：标准可以在迭代中提升，不必一开始就完美
2. **质量杠杆**：多轮迭代是质量杠杆，不是一次验收
3. **两个变量可干预**：标准和迭代都可主动提升，输出质量可控
4. **系统化方法**：从个人任务到团队流程到产品系统的三层应用

## 与其他知识的关联

- [[dk-wanghuan-standard-by-iteration]]——标准不清时用 AI 对抗 AI 生成标准
- [[dk-wanghuan-creativity-in-description-and-taste]]——创造力重新分配，标准设计方法
- [[dk-wanghuan-spec-trap]]——王欢 Spec 陷阱，验收标准设计
- [[dk-wanghuan-agent-platform-director-mode]]——王欢 Agent 平台导演模式，迭代方法
- [[yt-five-step-method]]——一堂五步法，系统化迭代框架

---

## 失败模式 / 常见走偏

| 失败模式 | 症状 | 修复 |
|:---|:---|:---|
| **只追标准不迭代** | 写了很详细的 prompt，但只看一版结果 | 强制至少 3 轮迭代 |
| **只追迭代不提升标准** | 反复让 AI 改，但说不出具体哪里不对 | 每轮迭代前先明确验收标准 |
| **迭代无记录** | 不知道哪一版比上一版好在哪里 | 建立版本对比和反馈记录 |
| **成本失控** | 迭代 20 轮还没满意 | 设定迭代上限和终止条件 |
