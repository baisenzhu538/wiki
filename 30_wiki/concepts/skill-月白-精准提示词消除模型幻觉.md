---



id: skill-月白-精准提示词消除模型幻觉
title: 技能：精准提示词消除模型幻觉
type: "tool"
status: draft
domain:
  - design- design
source_person: 月白
source_context: 文创案例 （原始 source 无法追溯，已标记为 source_unknown，待后续补充）
source_refs:
- source_unknown
wiki_refs: null
definition_of_done:
- 操作步骤清晰可执行
- 适用场景有正反例
- 工具要求明确
tools_required: null
prerequisite_skills: null
created_at: 2026-06-07
updated_at: '2026-06-16'
pipeline:
- confidence-draft
author: 月白
reviewed_by: pending
confidence: 0.6
trust_level: low
related:
  - '[[skill-月白-AI生图与图生图决策法]]'
  - '[[skill-月白-关键要素提取改图法]]'
  - '[[skill-月白-分层自洽海报生成法]]'
  - '[[skill-月白-多语言提示词精准法]]'
  - '[[skill-月白-AI设计严苛批评法]]'

---
# 技能：精准提示词消除模型幻觉

## 原始表述

精准提示词消除模型幻觉是月白在文创案例中提出的实操方法。

## 操作步骤

1. 确保提示词足够精准
2. 增加约束条件限定输出范围
3. 同一套提示词跨模型测试（GPT/Midjourney/DALL·E/Stable Diffusion）
4. 验证标准：主体信息一致、画面呈现类似、风格偏差在可接受范围

## 适用场景

- 需要稳定复现特定画面
- 跨平台/跨工具保持输出一致
- 对画面内容有严格要求不能出错

## 不适用场景

- 创意探索阶段需要随机性
- 艺术风格实验
- 提示词工程能力不足时强行复杂化

## 工具/环境

- 多种AIGC模型
- 提示词模板库

## 常见失败模式

- 步骤跳过或省略 → 结果不完整 → **严格按步骤执行**
- 未确认场景是否匹配 → 方法失效 → **先对照"适用场景"确认**

## 为什么有效

模型幻觉源于提示词模糊和约束不足；当提示词精准且约束到位时，不同模型的输出会收敛，降低随机性风险

## 关联技能

- 待补充

## 来源

- 月白，文创案例

## Feedback Path

- 60_feedback/comments/ — 使用此技能后有任何反馈，提交到这里
