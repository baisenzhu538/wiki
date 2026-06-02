---
title: "飞轮反馈汇总：老顽童 6 篇文章 × 18 条系统级 Feedback"
assigned_to: "黄药师（Builder）+ 欧阳锋（Architect）"
priority: "P0"
created_at: "2026-06-02"
reviewer: "欧阳锋"
status: "pending"
source: "老顽童飞轮第一圈 — 6 篇深度合成文章"
---

# 飞轮反馈汇总

> 老顽童的第一圈飞轮产出了 6 篇文章、18 条系统级 Feedback。以下按可修复的系统问题分类。

## A. 缺 CLI 命令（黄药师，P0，估 4h）

| # | 文章 | Feedback | 建议命令 |
|:--:|------|------|------|
| A1 | rag_judgment | 看不到系统层查询统计 | `kdo query --stats` |
| A2 | inbox_lake | 无法确认素材在不在 inbox | `kdo inbox --search "关键词"` |
| A3 | inbox_lake | 不知道湖里有多少素材 | `kdo inbox --count` |
| A4 | recursive_deepen | 看不到自己的生产数据 | `kdo produce --stats` |

## B. 缺自动化机制（黄药师，P1，估 3h）

| # | 文章 | Feedback | 建议机制 |
|:--:|------|------|------|
| B1 | feedback_fuel | Feedback 写在文章末尾没人看 | 自动提取文章 Feedback 段 → 归类 → 写入工单 |
| B2 | inbox_lake | 消费状态靠人记不靠谱 | 自动消费状态跟踪 |
| B3 | directory_friction | 使用频率靠人判断 | 自动使用频率分析 |
| B4 | oral_digestion | 跳读习惯靠人自律 | 每次打开口述稿时系统提示打猎目标 |
| B5 | feedback_fuel | Feedback 消费后无确认回路 | Feedback → 动作 → 通知回路 |

## C. 缺角色/流程（欧阳锋，P1）

| # | 文章 | Feedback | 建议 |
|:--:|------|------|------|
| C1 | feedback_fuel | 不确定汇聚者是谁 | 明确"飞轮管理者"角色（欧阳锋 or 新角色？） |
| C2 | feedback_fuel | 无法验证 Feedback 是否被看了 | 文章审查状态查看器 |

## D. 缺数据/评测（黄药师，P2，估 6h）

| # | 文章 | Feedback | 建议工具 |
|:--:|------|------|------|
| D1 | rag_judgment | 不了解 LightRAG 内部实现 | Graph RAG 技术白皮书 |
| D2 | rag_judgment | "向量 vs 图"只有感觉没有数据 | 标准化检索评测工具 |
| D3 | recursive_deepen | 分不清"累了"还是"方法论缺陷" | 文章独立判断密度自动评分 |
| D4 | oral_digestion | 跳读效率无法验证 | `kdo digest --benchmark` |
| D5 | directory_friction | 没有 A/B 测试数据 | 层次影响量化测量 |

## E. Feedback 本身的问题（黄药师，P0 — 本次修复）

| # | 文章 | Feedback | 修复 |
|:--:|------|------|------|
| E1 | feedback_fuel | "Feedback 被写下后就没有下文了" | `kdo feedback --scan` 自动提取 + 汇总 |
| E2 | feedback_fuel | "习惯解不是技术解" | 本文档就是技术解的第一步：Feedback → 工单 |

---

## 执行优先级

```
P0 本次: E1+E2 (Feedback 自动提取) + A1-A4 (4 个 CLI 命令)
P1 下次: B1-B5 (5 个自动化机制) + C1-C2 (角色/流程)
P2 后续: D1-D5 (5 个评测/数据工具)
```

---

*黄药师 · 2026-06-02 · 基于老顽童飞轮第一圈 Feedback 自动汇总*
