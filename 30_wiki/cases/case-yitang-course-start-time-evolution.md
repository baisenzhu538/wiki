---
id: case-yitang-course-start-time-evolution
title: 案例：一堂开课时间——从"同行七八点"到"用户真正需要九点"
type: case
status: reviewed
author: 老顽童
reviewed_by: 欧阳锋
confidence: 0.85
trust_level: high
language: zh-CN
created_at: 2026-07-04
updated_at: '2026-07-04'
domain:
- yitang
source_refs:
- 00_inbox/解放思想/解放思想-truman-口述.txt
- 60_feedback/extractions/extraction-jiefang-sixiang-truman.md
related:
- "[[framework-yitang-jiefang-sixiang]]"
- "[[case-yitang-yitang-transcript-strategy]]"
---

# 案例：一堂开课时间——从"同行七八点"到"用户真正需要九点"

> **一句话定义**：Truman 面对同行普遍 19:00-20:00 开课的行业常识，没有直接照搬，而是回归"用户时间协调"底层逻辑，测试 20:00 后发现请假率上升，最终长期坚持 21:00。行业常识被底层用户行为数据推翻。

## 一、背景

- **行业惯例**：在线教育课一般在 19:00-20:00 开始
- **惯例的假设**：用户下班后吃完饭正好听课
- **Truman 的测试**：试过 20:00 → 请假率上升（用户还没忙完）；试过 21:00 → 出勤率和完课率最优

## 二、决策逻辑

没有盲目遵循行业惯例，也没有为了"不一样"而故意不一样。而是回到底层逻辑——用户在什么时间最可能完整听完一节课？——用数据回答。

## 三、与解放思想的关系

行业常识（L2）是"在线教育应该七八点开课"。Truman 用底层用户行为数据推翻了它。关键不是"七八点对不对"，而是"七八点在你的用户身上对不对"。

## Action Triggers

| 触发场景 | 第一个动作 |
|:---|:---|
| 发现团队在照搬行业惯例而没有验证 | 问：这个惯例在我们的用户/场景下成立吗？上一次验证是什么时候？ |
