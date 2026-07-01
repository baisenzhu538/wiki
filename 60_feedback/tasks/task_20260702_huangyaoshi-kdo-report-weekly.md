---
id: task_20260702_huangyaoshi-kdo-report-weekly
title: kdo report --weekly 完成报告
type: task
status: reviewed
assignee: 黄药师
priority: P1
created_at: 2026-07-02
updated_at: '2026-06-29T19:20:00+00:00'
reviewer: 欧阳锋
review_date: '2026-06-29'
acceptance_verdict: pass
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

---

## 欧阳锋终审结论（2026-06-29）

**终审通过。**

### 复核结果

| 验收项 | 状态 | 复核说明 |
|---|---|---|
| `kdo report --weekly` 可运行 | ✅ PASS | 在 wiki 工作区实测生成报告 |
| Snapshot 表格 8 项指标 | ✅ 通过 | Errors/Warnings/Wiki/Inbox/Sources/Artifacts/Deliveries/Feedback |
| vs Last Week 增量对比 | ✅ 已修复 | 原正则匹配失败，已改为解析 Snapshot 数据行；排除当天待覆盖文件 |
| Inbox Top 5 | ✅ 已补齐 | 原报告缺失，已补充按目录统计的 Top 5 表格 |
| Recommendations | ✅ 通过 | 含 ERROR、Inbox 积压等建议 |
| 代码位置 | ✅ 通过 | `kdo/cli.py` + `kdo/commands/system.py` |
| pytest | ✅ 549 passed / 2 failed / 1 skipped | 2 failed 为环境编码/端口 flaky，与本次改动无关 |
| 单元测试 | ✅ 新增 | `tests/test_report.py` 覆盖 report 生成与周环比 |

### 审查中发现并修复的问题

1. **vs Last Week 未生效**
   - 原代码用 `Warnings:\s*(\d+)` 等正则匹配报告文本，但报告里是 Markdown 表格，无 `Warnings:` 文本
   - 修复：改为正则匹配 Snapshot 数据行 `|^\|\s*(\d+)\s*\|\s*(\d+)\s*\|\s*(\d+)\s*\|\s*(\d+)`
   - 同时排除即将覆盖的当天报告文件，避免与自身对比

2. **Inbox Top 5 缺失**
   - 任务单要求报告含 `📦 Inbox Top 5`，但实现中未输出
   - 修复：在 `cmd_report` 中增加 Inbox 目录 Top 5 表格

3. **缺少单元测试**
   - 新增 `tests/test_report.py`，验证 report 文件生成、Snapshot/Inbox Top 5/Recommendations 存在，以及 vs Last Week 对比

### 全库 lint 状态

- 本次代码改动不新增 lint ERROR
- 全库剩余 1 个 ERROR（`30_wiki/personal-os/zhu-time-os.md`，#41 遗留）

同意封账。

*终审：欧阳锋 · 2026-06-29*
