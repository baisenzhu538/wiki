---
id: task_20260705_wangyuyan-multi-ai-cross-validation-dk
type: task
status: pending_review
assignee: claude
reviewer: 欧阳锋
priority: P2
created_at: 2026-07-05
updated_at: '2026-07-05T12:48:49.145554+00:00'
source_refs:
- 00_inbox/人机协作双三角/一堂双三角partner的对话记录20260705.md
related:
- '[[dk-yitang-over-abstraction]]'
- '[[concept-yihang-dual-triangle-core]]'
---

# 任务 #112：多 AI 交叉比对验证法 dk 卡

## 来源

老朱在与 YAI Partner 对话中提出的实战验证策略——没有文档、不懂代码的情况下，用多个 AI 相互校验。

## 核心方法论

```
同一任务 → 多个 AI 分别分析
  → 分歧结果互喂
  → 多轮辩经直到收敛
  → 仍未收敛的标记为"待人工确认"
```

## 为什么有效

"AI 比较实事求是，不太像人会有立场和情绪，很多情况下他们会达成一致的。"

## 适用场景

- 用户自己不懂该领域，无法直接判断 AI 输出质量
- 没有文档/标准答案做参照
- 有多个可用 AI 工具

## 验收

- dk 卡含方法论描述 + 至少 1 个实战案例
- `kdo pre-submit` PASS
