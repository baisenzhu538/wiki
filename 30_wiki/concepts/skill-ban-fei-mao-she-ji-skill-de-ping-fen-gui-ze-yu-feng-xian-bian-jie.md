---
id: skill-ban-fei-mao-she-ji-skill-de-ping-fen-gui-ze-yu-feng-xian-bian-jie
title: '技能：设计 Skill 的评分规则与风险边界'
type: "tool"
status: enriched
domain:
- ai-collaboration
source_person: 半肥猫
source_context: AI俱乐部-AI学习落地 分享
source_refs:
- 10_raw/sources/src_20260617_f1830fa6-半肥猫-ai学习落地-口述.md
tools_required:
- AIGC大模型
- 文档编辑工具
prerequisite_skills:
- skill-半肥猫-课程Skill化的八步工作流
- skill-ban-fei-mao-pan-duan-ke-cheng-shi-fou-zhi-de-zuo-cheng-skill
related:
- '[[concept-半肥猫-ai-learning-toolification-methodology]]'
- '[[case-ban-fei-mao-skill-ab-test]]'
- '[[dk-ban-fei-mao-skill-rejection-value]]'
created_at: 2026-06-07
reviewed_by: 欧阳锋
updated_at: '2026-06-19'
pipeline:
- confidence-draft
- confidence-source-cited
- confidence-verified-by-case
- confidence-verified-by-test
author: 半肥猫
confidence: 0.88
trust_level: medium
diagnostic_signals:
- signal: Skill 在边界场景仍然输出"做吧做吧"式鼓励
  lens: 拒绝能力与风险边界
  follow_up: 检查评分规则与风险边界是否写入 Skill 主体并被自动执行
- signal: 不同用户对同一 Skill 输出给出差异极大的"好坏"判断
  lens: 量化评分维度
  follow_up: 核对是否每个维度都有 0-3 四级标准和可复现的评分示例
- signal: 高风险场景下 Skill 没有触发额外审查或降级输出
  lens: 风险分级映射
  follow_up: 验证高/中/低容错场景是否对应不同的约束强度与评分权重
---
# 技能：设计 Skill 的评分规则与风险边界

## 用一句话讲清楚

通过量化评分规则与分级风险边界，把 Skill 从"好意的建议"变成"有约束、可评估、知道该拒绝"的协议。

## 核心要点

- **Skill 的最大价值是"拒绝"**。A/B 测试中差距最大的地方往往不在生成能力，而在"拒绝能力"——能在场景不适合时说"暂时别做"的 Skill，比一味讨好用户的通用模型更可靠。
- **评分规则要量化、多维度、分级**。以 12 维度为例，每个维度按 0-3 打分（无能力、弱、可接受、强），满分 36 分，把"好不好"从感觉变成数据。
- **风险边界要分级映射到评分规则**。高容错、中容错、低容错场景对应不同的约束强度与审查环节；高风险场景（如保险、医疗、金融）必须有更严格的边界。
- **规则要写入 Skill 主体**。评分规则和风险边界不能只在文档里，要变成 Skill 每次执行时自动检查的约束条件。

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

- [ ] 确定 Skill 的核心目标与关键失败代价
- [ ] 设计 3-5 个核心评分维度，并给出 0-3 四级标准
- [ ] 定义适用场景、不适用场景与灰色地带示例
- [ ] 建立高/中/低容错风险分级，并映射到评分权重与约束条件
- [ ] 将评分规则和风险边界写入 Skill 主体提示词
- [ ] 针对边界场景设计测试用例，验证 Skill 能否正确拒绝
- [ ] 收集真实使用反馈，迭代评分标准与边界定义

## 相关卡/互链

- [[skill-半肥猫-课程Skill化的八步工作流]] — 八步中的第 4 步（诊断协议设计）的上位流程
- [[skill-ban-fei-mao-yong-skill-zuo-dui-bi-ce-shi-yan-zheng-xiao-guo]] — 评分规则是测试的基础，没有评分规则就无法验证效果
- [[case-ban-fei-mao-skill-ab-test]] — 评分规则在 A/B 测试中的实际应用
- [[dk-ban-fei-mao-skill-rejection-value]] — "Skill 的最大价值是拒绝"，这是设计风险边界的核心理念

## 来源

- 半肥猫，AI 俱乐部 AI 学习落地分享

## Feedback Path

- 60_feedback/comments/ — 使用此技能后有任何反馈，提交到这里
