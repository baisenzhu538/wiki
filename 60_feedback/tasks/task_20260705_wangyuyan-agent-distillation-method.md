---
id: task_20260705_wangyuyan-agent-distillation-method
type: task
status: queued
assignee: 王语嫣
reviewer: 欧阳锋
priority: P1
created_at: 2026-07-05
updated_at: 2026-07-05
source_refs:
- 00_inbox/人机协作双三角/一堂双三角-人机协作模型-口述.txt L2118-2136
- 00_inbox/人机协作双三角/一堂双三角-人机协作模型-口述.txt L2220-2312
related:
- '[[method-yihang-ai-self-xray-iteration]]'
- '[[method-yihang-dual-triangle-ai-review]]'
- '[[concept-yihang-dual-triangle-core]]'
---

# 任务 #104：Agent 蒸馏方法——从对话中提取系统提示词的工程框架

## 背景

明天老朱会学习 YAI Agent，对话上下文需要被蒸馏为 KDO Agent 的系统提示词。课程中 Truman 演示了"让 AI 学双三角→拆自己设计过程→复盘→迭代"的闭环。外部调研确认了蒸馏的精度边界和工程化路径。

**本任务是王语嫣自己执行的调研+设计任务，不等老顽童。**

## 蒸馏框架：三层精度模型

| 层级 | 类型 | 可蒸馏性 | KDO 对应 |
|:---|:---|:---|:---|
| L1 | 结构化规则/框架/约束 | ✅ 精确 | 双三角六要素、7步配置法、画布填充逻辑 |
| L1.5 | 风格/语气/判断偏好 | ⚠️ 方向正确 | 人格画像、Truman 的沟通习惯 |
| L2 | 直觉/效用判断 | ❌ 不可编码 | 保持人在环 |

## 蒸馏流程（缝合课程+外部调研）

```
对话上下文输入
  → 第1步：Cite——标注关键决策点和框架调用
  → 第2步：Compress——将标注段压缩为结构化规则
  → 第3步：Connect——映射到已有 KDO 卡片（用双三角六要素对齐）
  → 第4步：Codify——输出为 agent-spec 格式的 system prompt 段落
  → 第5步：Evaluate——用双三角自复盘验证蒸馏质量
```

## 明天执行计划

1. 老朱提供 YAI Agent 对话上下文
2. 王语嫣按 5 步蒸馏流程提取
3. 产出一个可直接使用的 system prompt 段落
4. 同时归入 KDO 卡片作为新 domain knowledge

## 输出物

- 蒸馏后的 system prompt 片段（可直接挂载到 Agent）
- 蒸馏过程中识别的新框架/方法 → 标注为后续任务
- 整个过程存入 `60_feedback/diagnosis/diag_20260705_yai-agent-distillation.md`
