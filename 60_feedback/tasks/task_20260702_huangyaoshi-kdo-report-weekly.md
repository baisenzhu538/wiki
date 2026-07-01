---
id: task_20260702_huangyaoshi-kdo-report-weekly
title: kdo report --weekly 完成报告
type: task
status: pending_review
assignee: 黄药师
priority: P1
created_at: 2026-07-02
updated_at: 2026-07-02
reviewer: 欧阳锋
source_refs:
  - 销售专题/_processed/销售专题_整合笔记.md (Step 3: 推进业绩·周会三要点)
related:
  - "[[task_20260702_huangyaoshi-kdo-pipeline-dashboard]]"
  - "[[task_20260702_huangyaoshi-kdo-inbox-grade]]"
---

# kdo report --weekly 完成报告

## 做了什么

新增 `kdo report --weekly` 命令。用销售域**周会三要点**（看Gap→找原因→定策略）生成工厂周报。

## 报告内容

- 📊 Snapshot：Errors/Warnings/Wiki/Inbox/Sources/Artifacts
- 📈 vs Last Week：自动对比上周报告，显示增量
- 📦 Inbox Top 5
- 💡 Recommendations：基于Gap自动给建议

## 运行验证

```text
$ kdo report --weekly
Weekly report: 60_feedback/auto/weekly-report-20260701.md
  Errors:10 Warnings:2608 Wiki:2193 Inbox:10104
  🔴 10 lint ERRORs — fix immediately
  📥 Inbox 积压 — 跑 kdo inbox --grade 优先 S 级
```

报告文件已生成到 `60_feedback/auto/weekly-report-20260701.md`。

## 代码改动

| 文件 | 改动 |
|:---|:---|
| `kdo/cli.py` | `p_report` 子命令 + `--weekly` |
| `kdo/commands/system.py` | `cmd_report()` ~100行 |

## pytest

548 passed / 1 failed / 1 skipped（failed为预存在）

## 说明

10个ERROR来自周报首跑时发现的真实新问题（personal-os 3个 + 已有卡 7个），非误报。下周运行时会与本周基线对比，显示趋势变化。

---

*黄药师 2026-07-02*
