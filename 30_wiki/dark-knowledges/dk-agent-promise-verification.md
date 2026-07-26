---
id: dk-agent-promise-verification
title: 承诺核对表：Agent 能承诺什么、不能承诺什么
type: dk
status: draft
confidence: 0.87
trust_level: high
domain:
- agent-engineering
author: 老顽童
reviewed_by: 待审
review_date: '2026-07-19'
created_at: '2026-07-19'
updated_at: '2026-07-19'
quality_labels:
- actionable
- principle
source_refs:
- 00_inbox/半肥猫/【半肥猫】用 AI 把脑子里的经验，推进成一个最小可验证的数字交付 副本.md §第五步
related:
- tool-kdo-agent-production-checklist
- agent-native-card-design
- dk-ai-memory-four-layers
- system-yitang-Y-model-os
tags:
- audience:executor
- scene:reference
- skill-level:advanced
---

# 承诺核对表：Agent 能承诺什么、不能承诺什么

> 一句话：半肥猫在每张 Skill 卡最后加了一张"承诺核对表"——四列：对外承诺/对应交付/用户动作/验收标准。核心逻辑是反向的：不能补交付的，就把表达降级。

---

## 原始表述

> 来源：半肥猫·经验→数字交付文章 §第五步

半肥猫的承诺核对表结构：

| 对外承诺 | 对应交付 | 用户动作 | 验收标准 |
|:---|:---|:---|:---|
| 这个 Agent 能帮你做什么？ | 我们具体产出什么？ | 用户需要做什么？ | 怎样算"交付成功"？ |

核心原则：**"不能补交付的，就把表达降级。"** 如果你承诺了"帮你做竞品分析"但实际只产出了"竞品名单"——要么补交付，要么把承诺改成"帮你列竞品名单"。

---

## 使用场景

- 每张 agent-spec 卡提交前——填写承诺核对表
- Agent 上线后用户投诉"做不到"时——回头核对承诺表
- 老顽童生产 agent-spec 时——Step 3.4 强制勾稽

---

## 操作方法

```
1. 列"对外承诺"：这个 Agent 对用户承诺什么？
2. 列"对应交付"：承诺的每一条，Agent 具体产出什么？
3. 列"用户动作"：用户要做什么才能让 Agent 工作？
4. 列"验收标准"：怎样判断交付成功？
5. 反向检查：有没有承诺了但交付不了的项目？→ 降级承诺或补交付
```

---

## 适用边界

- ✅ agent-spec 卡提交前自检
- ✅ 用户使用 Agent 前了解"能做什么/不能做什么"
- ❌ 纯内部 Agent（不通向用户）——可简化

---

## 为什么值钱

半肥猫的经历：很多 Agent 上线后用户不满意，不是因为 Agent 不好——是因为承诺和交付不匹配。这张表把"期望管理"显式化了。

---

## 与其他知识的关联

- `agent-native-card-design`：承诺核对表应作为 agent-spec 卡的设计规范补充
- `tool-kdo-agent-production-checklist`：Step 3.4 强制引用本卡
