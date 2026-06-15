---
id: "skill-react行动推理循环"
title: "技能：ReACT行动推理循环"
type: skill
domain:
  - ai-saas
  - yitang
status: draft
source_person: Truman
source_context: src_20260609_03491271
source_refs:
  - src_20260609_03491271
definition_of_done:
  - "操作步骤清晰可执行"
  - "适用场景有正反例"
  - "工具要求明确"
tools_required:
  - "支持Function Calling的LLM"
  - "工具API（搜索/数据库/计算等）"
  - "ReACT框架实现"
created_at: "2026-06-09T14:38:36+00:00"
updated_at: "2026-06-09T14:38:36+00:00"
author: legacy
reviewed_by: pending
confidence: 0.7
trust_level: low
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
- ✅ 需要实时信息的问题
- ✅ 多步骤工具调用任务
- ✅ 需要与外部系统交互的自动化


## 为什么有效
将推理与行动交织，模型自主决定何时需要外部信息，比纯生成更准确和及时

## 工具/环境
- 支持Function Calling的LLM
- 工具API（搜索/数据库/计算等）
- ReACT框架实现

## 常见失败模式
- （待补充）

## 关联技能
- （待补充）

## 来源
- Truman，src_20260609_03491271，2026-06-09

## Feedback Path
- 60_feedback/comments/ — 反馈
