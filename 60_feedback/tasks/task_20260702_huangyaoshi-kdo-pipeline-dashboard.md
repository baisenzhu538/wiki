---
id: task_20260702_huangyaoshi-kdo-pipeline-dashboard
title: kdo pipeline 完成报告
type: task
status: pending_review
assignee: 黄药师
priority: P1
created_at: 2026-07-02
updated_at: 2026-07-02
reviewer: 欧阳锋
source_refs:
  - 销售专题/_processed/销售专题_整合笔记.md (Step 3: 推进业绩·追过程)
related:
  - "[[task_20260702_huangyaoshi-kdo-inbox-grade]]"
---

# kdo pipeline 完成报告

## 做了什么

新增 `kdo pipeline` 命令——KDO管线可视化Dashboard。用销售域**追过程三步法**（看Gap→找原因→定策略）作为底层逻辑。

## 展示内容

```
📥 CAPTURE  — inbox文件数/目录分布
📋 INGEST   — sources注册数
✏️  PRODUCE  — artifacts按status分布
🚀 SHIP     — deliveries/feedback/tasks
📊 WIKI     — 卡片按type分布
🔍 BOTTLENECKS — 自动检测管线瓶颈
💡 RECOMMENDATIONS — 基于瓶颈给建议
```

## 瓶颈检测规则

| 条件 | 瓶颈 | 建议 |
|:---|:---|:---|
| inbox>5000 且 artifacts<100 | 摄入积压 | 跑 inbox --grade 优先S级 |
| draft>50 | enrich瓶颈 | 检查老顽童产能 |
| pending_review>10 | 审查积压 | 欧阳锋抽样或委派 |

## 当前运行结果

```
Inbox: 10104 files (34 dirs, 广冷电子占60%)
Sources: 689
Artifacts: 34 (ready:21 draft:7 shipped:6)
Wiki: 2189 cards (tool:868 concept:463 case:246)
⚠️ Bottleneck: inbox积压严重
```

## 代码改动

| 文件 | 改动 |
|:---|:---|
| `kdo/cli.py` | `p_pipeline` 子命令 |
| `kdo/commands/system.py` | `cmd_pipeline()` ~120行 |

## pytest

548 passed / 1 failed / 1 skipped（failed为预存在）

---

*黄药师 2026-07-02*
