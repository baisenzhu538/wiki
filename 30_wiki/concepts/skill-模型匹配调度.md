---

id: "skill-模型匹配调度"
title: "技能：模型匹配调度"
type: skill
domain:
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
  - "模型路由层/网关"
  - "负载均衡器"
  - "多模型API密钥"
created_at: "2026-06-09T14:38:36+00:00"
updated_at: "2026-06-09T14:38:36+00:00"
author: legacy
reviewed_by: pending
confidence: 0.7
trust_level: low
---

# 技能：模型匹配调度

## 原始表述
> 1.楼型正配 2.并行调度

## 操作步骤
1. 建立任务特征与模型能力的匹配矩阵
2. 根据任务类型（速度/质量/成本/专长）自动路由到最优模型
3. 对独立子任务并行调度多个模型
4. 聚合结果

## 适用场景
- ✅ 大规模API调用需要成本控制
- ✅ 响应速度敏感的场景
- ✅ 多模型基础设施已建立


## 为什么有效
优化成本-效果-延迟的帕累托前沿，避免对所有任务使用最贵模型

## 工具/环境
- 模型路由层/网关
- 负载均衡器
- 多模型API密钥

## 常见失败模式
- （待补充）

## 关联技能
- （待补充）

## 来源
- Truman，src_20260609_03491271，2026-06-09

## Feedback Path
- 60_feedback/comments/ — 反馈
