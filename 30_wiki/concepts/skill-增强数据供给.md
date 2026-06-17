---


id: skill-增强数据供给
title: 技能：增强数据供给
type: "tool"
domain:
- design
- yitang
- decision-making
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
- 向量数据库
- 搜索API
- RAG框架
- 多模态模型
created_at: '2026-06-09T14:38:36+00:00'
updated_at: '2026-06-16'
author: 老顽童
reviewed_by: pending
confidence: 0.7
trust_level: low
---
# 技能：增强数据供给

## 原始表述
> 1.给案例集 2.专家资料 3.用多模态 4.联网搜索 5.接入API 6.使用RAG

## 操作步骤
1. 识别任务所需的外部知识类型
2. 选择供给方式：案例集（few-shot）、专家资料（角色注入）、多模态（图文音视频）、实时搜索、私有API、RAG检索
3. 将数据格式化接入模型上下文
4. 评估效果调整供给策略

## 适用场景
- ✅ 模型预训练知识不足或过时
- ✅ 需要特定风格或专业深度
- ✅ 私有数据不可直接训练


## 为什么有效
在不对模型微调的情况下，通过上下文学习注入特定能力和知识，灵活且成本低

## 工具/环境
- 向量数据库
- 搜索API
- RAG框架
- 多模态模型

## 常见失败模式
- （待补充）

## 关联技能
- （待补充）

## 来源
- Truman，src_20260609_03491271，2026-06-09

## Feedback Path
- 60_feedback/comments/ — 反馈
