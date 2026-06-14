---
id: "skill-模型组合调用"
title: "技能：模型组合调用"
type: "skill"
status: "draft"
domain:
source_person: "Truman"
source_context: "src_20260609_03491271"
source_refs:
  - "src_20260609_03491271"
wiki_refs:
definition_of_done:
  - "操作步骤清晰可执行"
  - "适用场景有正反例"
  - "工具要求明确"
tools_required:
  - "多个模型API"
  - "编排工具如Dify/n8n/自研脚本"
prerequisite_skills:
related:
created_at: "2026-06-09T14:38:36+00:00"
updated_at: "2026-06-09T14:38:36+00:00"
pipeline:
  - None
author: "legacy"
reviewed_by: "pending"
confidence: 0.7
trust_level: "low"
---

# 技能：模型组合调用

## 原始表述
> 5.模型组合

## 操作步骤
1. 分析任务链条，识别各环节所需能力
2. 为每个环节匹配最适合的模型
3. 设计模型间的数据传递格式
4. 串联或并联执行

## 适用场景
- ✅ 复杂多步骤任务
- ✅ 各环节需要不同专长（如代码+创意+分析）
- ❌ 单一步骤的简单任务

## 为什么有效
没有单一模型在所有维度最优，组合调用发挥各模型比较优势

## 工具/环境
- 多个模型API
- 编排工具如Dify/n8n/自研脚本

## 常见失败模式
- （待补充）

## 关联技能
- （待补充）

## 来源
- Truman，src_20260609_03491271，2026-06-09

## Feedback Path
- 60_feedback/comments/ — 反馈
