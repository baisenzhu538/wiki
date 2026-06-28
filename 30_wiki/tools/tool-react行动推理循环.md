---
id: tool-react行动推理循环
title: 技能：ReACT行动推理循环
type: tool
domain:
  - ai-collaboration- ai-saas
  - yitang
status: draft
source_person: Truman
source_context: src_20260609_03491271
source_refs:
- src_20260609_03491271-ocr-一堂-ai学习-truman自用的ai-featureset
definition_of_done:
- src_unknown
- src_unknown
- src_unknown
tools_required:
- src_unknown
- src_unknown
- src_unknown
created_at: '2026-06-09T14:38:36+00:00'
updated_at: '2026-06-16'
author: 老顽童
reviewed_by: pending
confidence: 0.7
trust_level: low
related:
  - [[tool-反向提示获取优化建议]]
  - [[tool-多轮确认防偏差]]
  - [[tool-主动摘要压缩上下文]]
  - [[tool-提示词结构化迭代]]
  - [[tool-渐进式披露上下文]]
---
# 技能：ReACT行动推理循环

## 原始表述
> 6.使用ReACT

## 操作步骤
1. 定义可调用工具集（搜索/计算/代码执行等）
2. 模型循环执行：Thought（思考需要什么）→ Action（调用工具）→ Observation（获取结果）→ ...
3. 直到获得最终答案
4. 显式追踪每一步的推理和工具调用

## 适用场景
- src_unknown
- src_unknown
- src_unknown


## 为什么有效
将推理与行动交织，模型自主决定何时需要外部信息，比纯生成更准确和及时

## 工具/环境
- src_unknown
- src_unknown
- src_unknown

## 常见失败模式
- src_unknown

## 关联技能
- src_unknown

## 来源
- src_unknown

## Feedback Path
- src_unknown
