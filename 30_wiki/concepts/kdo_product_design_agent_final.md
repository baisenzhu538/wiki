---
id: kdo_product_design_agent_final
created_at: 2026-05-03
domain: ai-saas
source_refs:
- 10_raw/sources/src_20260503_52ae08ba-kdo_product_design_agent_final.md
status: enriched
title: Obsidian + KDO 内容产出工作流 — 产品设计大纲 (v1.0完整版)
type: concept
updated_at: 2026-05-03
pipeline:
- src_unknown
author: unknown
reviewed_by: 欧阳锋
confidence: 0.8
trust_level: medium
related:
- - - ocr-泛产品设计-用户卡片-场景推演
- - - tool-半肥猫-课程Skill化的八步工作流
- - - kdo-input-channel-strategy-2026-06-16
- - - ocr-泛产品设计-落地卡片-攻坚会
- - - kdo-protocol
- - - ocr-泛产品设计落地篇
- - - ocr-泛产品设计者的三大自我修养
- - - ocr-泛产品设计-用户卡片-惊喜公式
- - - ocr-泛产品设计-落地卡片-roi分析
- - - tool-月白-PPT全AI生成工作流
- - - framework-kdo-self-attack
- - - kdo-yaml-frontmatter-safety
- - - tool-泛产品设计-需求工具箱指南
- - - kdo-priority-checklist
- - - ocr-泛产品设计-落地卡片-低成本测试mvp
---

# Obsidian + KDO 内容产出工作流 — 产品设计大纲 (v1.0完整版)

## Summary

> **文档定位**: KDO（Knowledge Delivery Orchestrator）产品设计大纲 v1.0
> **日期**: 2026-05-01
> **核心愿景**: 面向内容创作者和知识工作者的"画布+流水线"双模态内容生产操作系统
> **核心假设**: 创作需要无序的自由（Obsidian画布），产出需要有序的纪律（KDO流水线），现有工具无法同时满足两者
> **差异化**: 流程纪律（八阶段流水线+质量门禁）+ 反馈闭环（SHA-256快照+修订链）+ 人机共享Wiki + 本地优先（零订阅）

> **注意**: 本文件是 `src_20260503_52ae08ba` 对应的完整版产品设计大纲。较早版本参见 obsidian-kdo-内容产出工作流-产品设计大纲。

## Source Refs

- src_unknown
- src_unknown

## Reusable Knowledge

### [Condense] 五条核心结论

1. **KDO 填补了"画布+流水线+本地优先"三角地带的唯一空白**：Notion AI（云端协作/强结构）、Mem.ai（云端/无结构）、Tana（云端/Supertag图谱）、Obsidian+插件（本地/无流程）都无法同时满足"笔记自由+产出纪律+数据本地所有权"。KDO 以 Obsidian 为前台画布、KDO 为后台流水线，通过共享 Markdown 目录实现零摩擦衔接。

2. **八阶段流水线是核心竞争壁垒**：Capture→Ingest→Enrich→Produce→Validate→Ship→Feedback→Improve。每个阶段配备状态追踪和质量门禁，阶段晋升需满足预设检查条件（如 Validate 需通过可读性评分和事实一致性检查）。这是 Tana Supertag 和 Notion 数据库触发器都无法实现的"强制执行"机制。

3. **反馈闭环通过 SHA-256 快照+修订链实现**：Validate 阶段生成密码学哈希基线，后续修订基于不可篡改的基线进行 diff 比对。读者反馈结构化链接到修订记录，形成"原始内容→反馈→修订→新版本"的完整因果链，使知识库随使用愈发准确（"去伪存真"效应）。

4. **人机共享 Wiki 打破 AI 黑盒隔离**：人和 AI 共同读写同一套 Markdown wiki。AI 每次启动通过查询 wiki 恢复上下文，人类在 Obsidian 中的新笔记即时进入 AI 视野。AI 从"外部工具"转变为"协作维护者"。

5. **目标用户是"系统型内容生产者"**：深度 Obsidian 用户（500+笔记、知识囤积但产出滞后）、小型内容团队（3-10人、拒绝 SaaS 锁定）、AI 辅助知识工作者（已用 AI 插件但缺乏流程编排）。单机月运行成本约 0.6 美元。

## Critique

#### 研究者偏差风险——调研者本身是最大的系统性偏差源

**研究者偏差风险**（Researcher Bias——来自科学哲学和方法论）：任何调研报告都是一个"被构建的叙事"——调研者的假设、工具、语言、时间窗口全都在形塑结果。这张卡片告诉你"什么是真的"，但它没告诉你"什么被排除了"。调研报告越详细，排除的东西越多——而那些被排除的，可能正是你最需要的。

> **核心质问**：这个调研报告在哪些关键决策点上排除了反例？调研者为什么选了这个时间点做调研？如果换一个不同背景的人来做同样的调研，结果会不会不同？如果答案是"会不同"——那么这个报告的"普通性"就是虚假的。

### 内部局限
 逐条质疑

**对结论1（三角地带唯一空白）：**
- src_unknown
- src_unknown
- src_unknown

**对结论2（八阶段流水线是壁垒）：**
- src_unknown
- src_unknown
- src_unknown

**对结论3-5**：详见完整源文件。

## Synthesis

### 不要用的场景

| 场景 | 为什么失效 | 替代方案 |
|------|-----------|---------|
| 把调研报告当成绝对真理执行 | 调研报告是时间截面，技术/市场/组织在变 | 每次使用前先验证"这个结论现在还成立吗" |
| 在无专业背景的情况下做出重大决策 | 调研报告是信息输入，不是决策代理 | 结合自身业务场景做二次判断 |

### 关联概念 跨领域对标

**与现有概念的关联：**
- 待补充链接
- 待补充链接
- 待补充链接
**可迁移场景：**
- 待补充链接
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
