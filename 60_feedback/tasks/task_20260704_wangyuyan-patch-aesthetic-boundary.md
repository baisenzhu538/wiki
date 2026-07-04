---
id: task_20260704_wangyuyan-patch-aesthetic-boundary
type: task
status: queued
assignee: 老顽童
reviewer: 欧阳锋
priority: P2
created_at: 2026-07-04
updated_at: 2026-07-04
source_task: task_20260704_laowantong-aesthetic-library-method-tool-cards
related:
- '[[method-yihang-aesthetic-fast-build]]'
- '[[tool-aesthetic-library-builder]]'
- '[[case-yihang-truman-aesthetic-library-practices]]'
---

# 任务 #82：#72 修补——审美三约束

## 修补目标

#72 产出 3 张审美域卡片后，对 method 卡和 tool 卡追加审美边界条件。

## 原始素材

口述稿课后闲聊 L4098-4144 Truman 讲了三个审美约束：

1. **审美带着起点和终点，带着目标和人群**（L4098-4099）——不能脱离"为谁做、要达到什么目的"谈审美
2. **审美带着成本线**（L4100-4104）——真正的审美判断是在预算规模线下找到最优解。Truman："你无限看什么没有意义……我们拿苹果借鉴审美之后，其实还是在基于成本线下去考虑"
3. **不能只看最贵的**（L4136-4143）——"要去看最贵的，但很多东西是学不会的。它最后成本也是你的限制条件，你做不出来"

## 修补内容

**method-yihang-aesthetic-fast-build**：在操作步骤中增加一步"声明成本约束"——拉到什么水平取决于能投入多少资源。加一句 Truman 原话。

**tool-aesthetic-library-builder**：支持按成本线分级输出（预算无限版 / 商业交付版 / MVP 版）。如果工具已交付不支持，则在 tool 卡中标注为"未来迭代方向"。

## 验收标准

- method 卡和 tool 卡更新后 `kdo pre-submit` PASS
- method 卡含审美三约束（至少含 Truman 一句原话引用）
- tool 卡含成本线分级的说明（已实现或未来方向均可）
- 欧阳锋终审通过

## 依赖

- #72 完成（3 张审美卡已交付）
