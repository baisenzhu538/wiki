---

id: research_methodology
created_at: 2026-05-03
domain:
- ai-saas
status: superseded
superseded_by: []
title: Kimi 深度调研集群方法论 (Deep-Research-Swarm)
type: concept
updated_at: '2026-06-16'
author: unknown
reviewed_by: pending
confidence: 0.75
trust_level: medium-low
source_refs:
- 10_raw/sources/src_20260502_7d7c1b7c-kimi-深度调研集群方法论-deep-research-swarm.md
source_context: （原 legacy，已从 title/context/filename 推断为 10_raw/sources/src_20260502_7d7c1b7c-kimi-深度调研集群方法论-deep-research-swarm.md）
---
# Kimi 深度调研集群方法论 (Deep-Research-Swarm)

## Summary

> **核心理念**: 多智能体认知三角测量（Epistemic Triangulation）——在不同研究维度上发散、检测重叠与矛盾、深度验证、再收敛为经过验证的综合结论
> **核心创新**: 集群并行服务于认知鲁棒性，而非仅仅追求速度
> **四条自适应路由**: Route A（广域搜索）、Route B（聚焦搜索）、Route C（纯文件研究）、Route D（文件增强研究）
> **规模**: ≥10个子Agent并行，每Agent ≥20次独立搜索，总搜索预算≥200次（Route B）

> **注意**: 本文件内容来自 `src_20260503_5dc58ec8`。相关概念参见 [[kimi-深度调研集群方法论-deep-research-swarm]]（`10_raw/sources/src_20260502_7d7c1b7c-kimi-深度调研集群方法论-deep-research-swarm.md`），二者内容高度相似，可能为同一方法论的不同版本或整理稿。

## Source Refs

- src_unknown
- src_unknown

## Reusable Knowledge

### [Condense] 五条核心结论

1. **自适应路由是方法论的差异化核心**：根据任务特征（是否有文件、主题宽泛度、外部搜索限制）自动选择四条路线之一。Route C（纯文件研究）尊重用户"不上网搜索"的意图，Route D（文件增强研究）平衡文件内容与外部补充。

2. **Phase 2 强制分解≥10个维度**：维度必须相互互补（合起来覆盖完整问题空间）且部分重叠（≥30%重叠用于交叉验证）。维度类型包括：技术图景、市场/商业图景、监管/政策图景、竞争动态、用户视角、供应链、地理差异、历史演进、新兴颠覆、利益相关者视角等。

3. **Phase 3 并行深度挖掘的严格标准**：每个子Agent执行≥20次独立搜索，禁止重复关键词循环；优先原始来源（政府网站、学术期刊、官方备案、主流媒体）；所有发现必须包含 Claim / Source / URL / Date / Excerpt / Context / Confidence 七字段模板。

4. **Phase 4 交叉验证引擎的四级置信度**：高置信度（≥2个Agent从独立来源确认）、中等置信度（1个Agent从权威来源确认）、低置信度（来源薄弱或单一未验证）、冲突区域（Agent间统计分歧或解释分歧）。冲突必须显式记录，从不压制。

5. **Phase 6 洞察提取要求"非显而易见"**：洞察不得重复先前声明，必须来自跨维度比较，至少间接受两个维度证据支持。体裁感知：报告优先战略洞察，学术论文优先研究空白与理论张力。

## Critique

#### 研究者偏差风险——调研者本身是最大的系统性偏差源

**研究者偏差风险**（Researcher Bias——来自科学哲学和方法论）：任何调研报告都是一个"被构建的叙事"——调研者的假设、工具、语言、时间窗口全都在形塑结果。这张卡片告诉你"什么是真的"，但它没告诉你"什么被排除了"。调研报告越详细，排除的东西越多——而那些被排除的，可能正是你最需要的。

> **核心质问**：这个调研报告在哪些关键决策点上排除了反例？调研者为什么选了这个时间点做调研？如果换一个不同背景的人来做同样的调研，结果会不会不同？如果答案是"会不同"——那么这个报告的"普通性"就是虚假的。

### 内部局限
 逐条质疑

**对结论2-5：**
- src_unknown
- src_unknown
- src_unknown

## Synthesis

### 不要用的场景

| 场景 | 为什么失效 | 替代方案 |
|
---|-----------|---------|
| 把调研报告当成绝对真理执行 | 调研报告是时间截面，技术/市场/组织在变 | 每次使用前先验证"这个结论现在还成立吗" |
| 在无专业背景的情况下做出重大决策 | 调研报告是信息输入，不是决策代理 | 结合自身业务场景做二次判断 |

### 关联概念 跨领域对标

**与现有概念的关联：**
- src_unknown
- src_unknown
- src_unknown

**可迁移场景：**
- src_unknown
- src_unknown

## Open Questions

- src_unknown
- src_unknown
- src_unknown

## Output Opportunities

- src_unknown
- src_unknown
- src_unknown

## Action Triggers

| 触发场景 | 第一个动作 | 成功指标 |
|---------|-----------|---------|
| 需要基于这份调研做出关键决策前 | 先问自己"这个报告的结论现在还成立吗？有没有新的反例出现？" | 每次使用前都能说出至少一个可能影响结论有效性的新变化因素 |
