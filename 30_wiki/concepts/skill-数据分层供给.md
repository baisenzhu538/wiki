---


id: skill-数据分层供给
title: 技能：数据分层供给
type: "tool"
domain:
- kdo
- product
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
- RAG系统
- 向量数据库
- 知识图谱
created_at: '2026-06-09T14:38:36+00:00'
updated_at: '2026-06-16'
author: 老顽童
reviewed_by: pending
confidence: 0.7
trust_level: low
---
# 技能：数据分层供给

## 原始表述
> 8.数据分层

## 操作步骤
1. 将数据按重要性/时效性/敏感度分层
2. 设计不同层级的接入策略（核心层直接注入、扩展层RAG检索、公开层联网搜索）
3. 根据任务需求动态组合数据层

## 适用场景
- ✅ 企业级知识库构建
- ✅ 数据量大且更新频率不同
- ✅ 需要平衡成本与效果


## 为什么有效
优化token使用效率，保证核心信息优先触达，灵活扩展信息边界

## 工具/环境
- RAG系统
- 向量数据库
- 知识图谱

## 常见失败模式
- （待补充）

## 关联技能
- （待补充）

## 来源
- Truman，src_20260609_03491271，2026-06-09

## Feedback Path
- 60_feedback/comments/ — 反馈
