---
id: task_20260704_wangyuyan-patch-canvas-risk-judgment
type: task
status: queued
assignee: 黄药师
reviewer: 欧阳锋
priority: P2
created_at: 2026-07-04
updated_at: 2026-07-04
source_task: task_20260704_wangyuyan-dual-triangle-canvas-agent-cli
related:
- '[[tool-yihang-dual-triangle-canvas]]'
---

# 任务 #81：#69 修补——画布 Agent 加风险判断输出

## 修补目标

#69 产出画布 Agent CLI 后，追加一个功能：画布填充完成后输出风险判断。

## 原始素材

口述稿 L4595-4604 Truman 原话：

> "只要他能把双三角画布画出来，我们就敢对外承诺。过去是从来没有过的，就胆子达到这种程度了。"

**核心洞察**：画布填满 ≠ 计划完成。画布填满 = 风险可控。知道每个角有什么牌可打，即使现在没做出来，也知道缺什么、怎么补。

## 修补内容

在 `canvas-agent.py` 和 agent-spec 中增加：

1. 画布输出时，每个格标注置信度：`[确认]` / `[假设]` / `[空白]`
2. 会话结束时输出风险摘要：哪些格是空白（高风险），哪些是假设（需验证）
3. agent-spec 增加一条行为规则："如果用户对某个格的内容含糊，追问直到确认或标记为假设"

## 验收标准

- agent-spec 更新后 `kdo pre-submit` PASS
- `canvas-agent.py` 输出包含置信度标注
- 欧阳锋终审通过

## 依赖

- #69 完成（画布 Agent CLI 已交付）
