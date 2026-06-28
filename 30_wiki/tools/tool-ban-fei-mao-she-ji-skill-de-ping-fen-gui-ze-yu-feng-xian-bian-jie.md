---

id: tool-ban-fei-mao-she-ji-skill-de-ping-fen-gui-ze-yu-feng-xian-bian-jie
title: 技能：设计 Skill 的评分规则与风险边界
type: tool
status: enriched
domain:
- src_unknown
- yitang- src_unknown
source_person: 半肥猫
source_context: AI俱乐部-AI学习落地 分享
source_refs:
- 10_raw/sources/src_20260617_f1830fa6-半肥猫-ai学习落地-口述.md
tools_required:
- src_unknown
- src_unknown
prerequisite_skills:
- src_unknown
- src_unknown
related:
- src_unknown
- src_unknown
- src_unknown
- src_unknown
- src_unknown
- src_unknown
- src_unknown
- src_unknown
created_at: 2026-06-07
reviewed_by: 欧阳锋
updated_at: '2026-06-19'
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
