---
id: tool-ban-fei-mao-she-ji-skill-de-ping-fen-gui-ze-yu-feng-xian-bian-jie
title: 技能：设计 Skill 的评分规则与风险边界
type: tool
status: reviewed
domain:
- src_unknown
- yitang- src_unknown
source_person: 半肥猫
source_context: AI俱乐部-AI学习落地 分享
aliases:
  - 分规则与风险边界
  - 半肥猫
  - 技能
  - 技能：设计Skill的评分规则与风险边界
  - 的评分规则与风险边界
  - 设计
source_refs:
- 10_raw/sources/src_20260617_f1830fa6-半肥猫-ai学习落地-口述.md
tools_required:
- src_unknown
- src_unknown
prerequisite_skills:
- src_unknown
- src_unknown
related:
- '[[tool-半肥猫-课程Skill化的八步工作流]]'
- '[[tool-ai-skill-engineering-method]]'
- '[[tool-月白-AI设计底层逻辑：从设计到作图到改图]]'
- '[[tool-月白-口述作图法（口喷设计）]]'
- '[[tool-Truman-Skill全生命周期管理]]'
- '[[tool-月白-设计能力蒸馏封装法]]'
- '[[tool-马易-AI搜索公网数据增强（合规边界）]]'
- '[[tool-月白-设计文件八要素命名法]]'
- '[[tool-月白-设计项目MVP拆解法]]'
- '[[tool-ban-fei-mao-yong-skill-zuo-dui-bi-ce-shi-yan-zheng-xiao-guo]]'
- '[[tool-马易-业务问题AI化拆解-餐饮设计案例法]]'
- '[[tool-泛产品设计-需求工具箱指南]]'
- '[[tool-demand-iceberg-l5-forces]]'
created_at: 2026-06-07
reviewed_by: 欧阳锋
updated_at: '2026-06-28'
pipeline:
- src_unknown
- src_unknown
- src_unknown
- src_unknown
author: 半肥猫
confidence: 0.88
trust_level: medium
diagnostic_signals:
- lens: 拒绝能力与风险边界
  follow_up: 检查评分规则与风险边界是否写入 Skill 主体并被自动执行
- lens: 量化评分维度
  follow_up: 核对是否每个维度都有 0-3 四级标准和可复现的评分示例
- lens: 风险分级映射
  follow_up: 验证高/中/低容错场景是否对应不同的约束强度与评分权重
tags:
- audience:executor
- scene:execution
- skill-level:intermediate
- 半肥猫
- 学习落地
---

# 技能：设计 Skill 的评分规则与风险边界

## 用一句话讲清楚

通过量化评分规则与分级风险边界，把 Skill 从"好意的建议"变成"有约束、可评估、知道该拒绝"的协议。

## 核心要点

- src_unknown
- src_unknown
- src_unknown
- src_unknown

## 边界

| 维度 | 适用 | 不适用 |
|------|------|--------|
| 使用对象 | 需要被他人复用、需要质量承诺的 AI Skill | 个人一次性使用、不需要共享的 prompt |
| 任务类型 | 需要重复评估、输出质量可量化的任务 | 创意发散、脑暴、集思广益等开放性任务 |
| 容错要求 | 低容错或中容错场景的 AI 协助决策 | 完全娱乐、无后果的随意尝试 |
| 迭代需求 | 需要持续追踪、比较、改进的 Skill | 一次性任务、不需要重复评估 |

## 失败模式

| 失败模式 | 典型症状 | 对策 |
|----------|----------|------|
| 评分规则过于复杂 | 实际使用时难以执行，评分流于形式 | 保持简洁，聚焦 3-5 个核心维度 |
| 边界定义模糊 | Skill 在灰色地带行为不一致 | 用具体例子说明边界，明确"做/不做/谨慎做" |
| 风险分级与评分规则脱节 | 高风险场景下没有额外保护 | 风险分级要直接映射到评分规则与约束条件 |
| 量化给人伪安全感 | 分数高不等于真的好 | 评分规则需定期用真实案例校准，并保留人工复核 |

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

## 来源

- src_unknown

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

- **具体假设**：该工具假设"量化评分能客观衡量 Skill 质量"，但量化体系最大的陷阱是"可量化的不等于重要的"——评分规则天然偏向"容易打分的维度"（如格式规范、步骤完整性），而忽视"难以打分但更重要"的维度（如洞察深度、场景适配度）。
- **边界**：在创意型 Skill（如写作风格指导、设计灵感生成）中，量化评分不仅无效，还可能有害——它会引导创作者"优化分数"而非"优化效果"。
- **前提**：该工具的前提是"评分者能公正执行评分规则"，但评分者本身也有认知偏差——同一个 Skill，不同评分者的分数可能差 30%。

**Cass Sunstein**（哈佛大学法学院教授，《Nudge》合著者）会质疑：评分规则本质是一种"行为助推"（nudge），它会改变被评估者的行为模式。当 Skill 设计者知道自己的工作要按"3-5 个维度"打分时，他们会把精力集中在"那些维度"上——而被排除在评分之外的维度（即使更重要）会被系统性忽视。这种"可测性偏差"（metric bias）会让整个 Skill 库的质量结构变得扭曲。
