---



id: skill-思维链显化推理
title: 技能：思维链显化推理
type: "tool"
domain:
- ai-saas
- decision-making
- yitang
status: draft
source_person: Truman
source_context: src_20260609_03491271
source_refs:
  - src_20260609_03491271-ocr-一堂-ai学习-truman自用的ai-featureset
definition_of_done:
- 操作步骤清晰可执行
- 适用场景有正反例
- 工具要求明确
tools_required:
- 支持CoT的LLM
- 提示词模板
created_at: '2026-06-09T14:38:36+00:00'
updated_at: '2026-06-16'
author: 老顽童
reviewed_by: pending
confidence: 0.7
trust_level: low
related:
  - '[[skill-多轮确认防偏差]]'
  - '[[skill-主动摘要压缩上下文]]'
  - '[[skill-反向提示获取优化建议]]'
  - '[[skill-渐进式披露上下文]]'
  - '[[skill-提示词结构化迭代]]'
---
# 技能：思维链显化推理

## 原始表述
> 4.使用CoT

## 操作步骤
1. 在提示中明确要求'请逐步思考'
2. 或示例展示分步推理格式
3. 让AI显式输出中间推理步骤
4. 基于完整推理链评估最终答案

## 适用场景
- ✅ 数学/逻辑/复杂决策问题
- ✅ 需要可解释性的场景
- ✅ 答案经常出错需要诊断原因时


## 为什么有效
强制模型分配更多计算资源到推理过程，减少跳步错误，提高复杂问题准确率

## 工具/环境
- 支持CoT的LLM
- 提示词模板

## 常见失败模式
- （待补充）

## 关联技能
- （待补充）

## 来源
- Truman，src_20260609_03491271，2026-06-09

## Feedback Path
- 60_feedback/comments/ — 反馈
