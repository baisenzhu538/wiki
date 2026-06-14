---
id: "skill-思维验证交叉检验"
title: "技能：思维验证交叉检验"
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
  - "单一模型多轮对话"
  - "或两个实例对话"
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

# 技能：思维验证交叉检验

## 原始表述
> 5.使用CoV

## 操作步骤
1. 让AI先给出初始答案（CoT）
2. 再让AI扮演批评者验证该答案
3. 识别潜在错误、假设、遗漏
4. 基于验证结果修正答案
5. 可多次迭代

## 适用场景
- ✅ 高 stakes 决策
- ✅ 已知模型容易出错的领域
- ✅ 需要极高可靠性的分析


## 为什么有效
利用模型自我修正能力，通过角色分离实现内部交叉验证，减少确认偏误

## 工具/环境
- 单一模型多轮对话
- 或两个实例对话

## 常见失败模式
- （待补充）

## 关联技能
- （待补充）

## 来源
- Truman，src_20260609_03491271，2026-06-09

## Feedback Path
- 60_feedback/comments/ — 反馈
