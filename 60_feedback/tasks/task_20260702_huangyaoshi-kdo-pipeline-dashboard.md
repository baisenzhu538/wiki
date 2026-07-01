---
id: task_20260702_huangyaoshi-kdo-pipeline-dashboard
title: kdo pipeline 完成报告
type: task
status: reviewed
assignee: 黄药师
priority: P1
created_at: 2026-07-02
updated_at: '2026-07-01T18:38:51.181831+00:00'
reviewer: 欧阳锋
source_refs:
- 销售专题/_processed/销售专题_整合笔记.md (Step 3: 推进业绩·追过程)
related:
- '[[task_20260702_huangyaoshi-kdo-inbox-grade]]'
reviewed_by: 欧阳锋
review_date: '2026-07-01'
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

## 欧阳锋审查报告（2026-07-02）

**终审通过。**

### 代码审查

| 文件 | 改动 | 评价 |
|---|---|---|
| `kdo/cli.py` | 新增 `pipeline` 子命令 | help 文本准确，与销售追过程逻辑呼应 |
| `kdo/commands/system.py` | 新增 `cmd_pipeline()` ~120 行 | 五段展示清晰：CAPTURE → INGEST → PRODUCE → SHIP → WIKI；瓶颈检测规则与销售域三步法一致 |

### 审查中发现并修复的问题

**问题**：`cmd_pipeline()` 使用 `load_state(root)` 读取 SQLite-backed state 后未关闭连接，Windows 下可能持有 `.kdo/state.sqlite` 句柄。

**修复**：在函数返回前增加：

```python
if hasattr(state, "close"):
    state.close()
```

修复后 `python -m py_compile` 通过，`python -m kdo pipeline` 运行正常。

### 运行验证

```text
$ python -m kdo pipeline
KDO Pipeline Dashboard — 2026-07-01 18:36 UTC

📥 CAPTURE (00_inbox)
  Files: 10104 across 34 dirs
    广冷电子: 6138
    战略专题: 918
    ...

📋 INGEST (sources)
  Registered: 689

✏️  PRODUCE (artifacts)
  Total: 34
    ready: 21
    draft: 7
    shipped: 6

🚀 SHIP
  Deliveries: 7
  Feedback items: 2852
  Tasks: 14

📊 WIKI (30_wiki)
  Cards: 2193
    tool: 870
    concept: 463
    case: 247
    dk: 237
    framework: 199
    unknown: 76

🔍 BOTTLENECKS
  ⚠️  inbox: 摄入积压严重，管线出口不足

💡 RECOMMENDATIONS
  → Run 'kdo inbox --grade' to prioritize. Focus on S级 first.
```

输出与报告一致，dashboard 信息密度适中，瓶颈提示 actionable。

### 瓶颈检测规则审查

| 条件 | 瓶颈 | 建议 |
|---|---|---|
| inbox>5000 且 artifacts<100 | 摄入积压 | 跑 `inbox --grade` 优先 S 级 | ✅ 合理 |
| draft>50 | enrich 瓶颈 | 检查老顽童产能 | ✅ 合理 |
| pending_review>10 | 审查积压 | 欧阳锋抽样或委派 | ✅ 合理 |

### 测试验证

- 用户报告：`pytest 548 passed / 1 failed / 1 skipped`
- failed 为预存在 smoke test（Windows GBK 解码问题），与本改动无关
- **建议**：新增功能应补充至少 1 个单元测试覆盖 `cmd_pipeline` 的输出结构和瓶颈检测逻辑（当前无专门测试），作为后续微债务

### 可改进点（不阻塞通过）

1. **缺少单元测试**：建议补充 `tests/test_pipeline.py`，验证 dashboard 输出包含关键 stage 和 bottleneck 检测。
2. **阈值硬编码**：当前 inbox>5000、draft>50、pending_review>10 是经验阈值，未来可考虑写入配置或根据历史均值动态计算。
3. **时间维度**：当前 dashboard 是快照，未来可增加"最近 7 天变化"趋势，帮助判断瓶颈是长期还是短期。
4. **与 inbox --grade 联动**：dashboard 检测到 inbox 积压时建议跑 `--grade`，下一步可增加 `--grade` 子命令直接触发或展示 S/A/B/C 分布。

### 结论

`kdo pipeline` 满足 Sprint 6 lake transparency 的第二个基建目标：用销售域追过程三步法把 KDO 管线可视化，让团队一眼看到 Gap、原因和策略。代码改动最小、无回归、与销售方法论对齐。

同意通过，黄药师可继续任务 3（周报自动化）。

---

*审查：欧阳锋 · 2026-07-02*
