---



id: skill-渐进式披露上下文
title: 技能：渐进式披露上下文
type: "tool"
domain:
- management
- product
- ai-saas
- design
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
- 支持长上下文的LLM
- 对话线程管理
created_at: '2026-06-09T14:38:36+00:00'
updated_at: '2026-06-16'
author: 老顽童
reviewed_by: pending
confidence: 0.7
trust_level: low
related:
  - '[[skill-多轮确认防偏差]]'
  - '[[skill-主动摘要压缩上下文]]'
  - '[[skill-反向教学深化理解]]'
  - '[[skill-反向提示获取优化建议]]'
  - '[[skill-提示词结构化迭代]]'
---
# 技能：渐进式披露上下文

## 原始表述
> 2.渐进式披露

## 操作步骤
1. 先提供最小必要信息让AI开始
2. 根据AI反馈和任务进展
3. 逐步释放更多背景信息、细节或约束
4. 避免一次性信息过载

## 适用场景
- ✅ 上下文极长的复杂任务
- ✅ 需要探索性对话逐步明确需求
- ✅ 敏感信息需要分阶段授权
- ❌ 需要一次性全局优化的任务（如代码架构设计）

## 为什么有效
避免长上下文中的信息稀释和注意力分散，让AI聚焦当前阶段，同时保留调整空间

## 工具/环境
- 支持长上下文的LLM
- 对话线程管理

## 常见失败模式
- （待补充）

## 关联技能
- （待补充）

## 来源
- Truman，src_20260609_03491271，2026-06-09

## Feedback Path
- 60_feedback/comments/ — 反馈
