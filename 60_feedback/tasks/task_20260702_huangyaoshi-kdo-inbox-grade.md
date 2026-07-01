---
id: task_20260702_huangyaoshi-kdo-inbox-grade
title: kdo inbox --grade 完成报告
type: task
status: reviewed
assignee: 黄药师
priority: P1
created_at: 2026-07-02
updated_at: '2026-07-01T18:17:34.989997+00:00'
reviewer: 欧阳锋
source_refs:
- 销售专题/_processed/销售专题_整合笔记.md
related:
- '[[task_20260702_huangyaoshi-proposal-dark-knowledge-pilot]]'
reviewed_by: 欧阳锋
review_date: '2026-07-01'
---

# kdo inbox --grade 完成报告

## 做了什么

新增 `kdo inbox --grade` 命令，用销售域 SABC 分层逻辑自动给 `00_inbox/` 素材打分级。

## 分级规则

| 等级 | 判定逻辑 | 示例 |
|:---|:---|:---|
| **S** | 来源含一堂/Truman/免检作者信号 + 正文>500字 | 一堂AI学习口述稿、科学决策笔记 |
| **A** | 含群聊精华/案例/行业报告信号 + 正文>300字 | Vikki战队精华提炼、纪浩提示词案例 |
| **B** | 已处理的VLM/OCR产物、一般参考 | _vlm_reprocess下的文件 |
| **C** | 临时文件、脚本、锁文件、JSON/ZIP/PY | run_ocr.py, vlm_summary.json |

## 当前 inbox 状态

```
10104 files
  S: 2832 — AI学习口述稿、AI数据课、战略域图片等
  A:   40 — Vikki/大馨精华、纪浩案例、设计课口述
  B: 6559 — 大量已处理的VLM产物和图片
  C:  673 — 临时脚本和JSON
```

## 代码改动

| 文件 | 改动 |
|:---|:---|
| `kdo/cli.py:319` | `--grade` 参数 |
| `kdo/commands/system.py` | `_cmd_inbox_grade()` 函数（约80行） |

## pytest

548 passed / 1 failed / 1 skipped（failed为预存在smoke test）

## 给欧阳锋的建议

1. **S级2832个文件是真实的**——大多是.png图片+OCR文本对。建议下一步加 `--grade --ready` 过滤出可直接ingest的文本文件（跳过图片）。
2. **C级673个文件可以考虑清理**——脚本和JSON不应该留在inbox里。
3. **A级40个文件很少**——说明中间档次的素材在inbox里偏少，大部分要么是S级课程素材要么是B级处理产物。

---

*黄药师 2026-07-02*

## 欧阳锋审查报告（2026-07-02）

**终审通过。**

### 代码审查

| 文件 | 改动 | 评价 |
|---|---|---|
| `kdo/cli.py` | `p_inbox.add_argument("--grade", ...)` | 参数命名清晰，help 文本准确 |
| `kdo/commands/system.py` | 新增 `_cmd_inbox_grade()` 约 120 行 | 逻辑分层清晰：C 级判定 → B 级判定 → S 级判定 → A 级判定 → 默认 B；输出包含分级统计、S/A 示例列表、C 级归档建议 |

### 分级规则审查

| 等级 | 规则 | 合理性 |
|---|---|---|
| **S** | 来源含一堂/Truman/免检作者信号 + 正文>500字 | 合理，但英文信号（Diamandis/Kotler/Ries）仅在文件名小写匹配时生效，符合当前实现 |
| **A** | 含群聊精华/案例/行业报告信号 + 正文>300字 | 合理；A 级仅 40 个文件，说明中间档素材确实偏少 |
| **B** | 已处理的 VLM/OCR 产物、一般参考 | 合理；6559 个文件占 inbox 主体，符合当前 inbox 以处理产物为主的现状 |
| **C** | 临时文件、脚本、锁文件、JSON/ZIP/PY | 合理；673 个文件可考虑归档清理 |

### 运行验证

```text
$ python -m kdo inbox --grade
Inbox Grading Report — 10104 files

Grade  Count    Priority
────── ──────── ────────────────────────────────────────
  S    2832     立即处理 — 高价值源/框架密度高
  A    40       排队处理 — 群聊精华/案例/行业报告
  B    6559     低优先级 — 一般参考/重复概念
  C    673      建议归档 — 临时文件/处理产物/脚本
```

输出与报告一致，命令可稳定运行。

### 测试验证

- 用户报告：`pytest 548 passed / 1 failed / 1 skipped`
- failed 为预存在 smoke test（Windows GBK 解码问题），与本改动无关
- **建议**：新增功能应补充至少 1 个单元测试覆盖 `_cmd_inbox_grade` 的分级逻辑（当前无专门测试），作为后续微债务

### 可改进点（不阻塞通过）

1. **S 级中图片占比高**：2832 个 S 级文件包含大量 `.png` + OCR 文本对，建议下一步按黄药师建议增加 `--grade --ready` 过滤，仅输出可直接 ingest 的文本文件。
2. **缺少单元测试**：建议补充 `tests/test_inbox_grade.py`，覆盖：
   - 文件名/目录命中 S/A/C 信号的分级
   - 内容长度不足时降级行为
   - 未知文件默认 B 级
3. **C 级清理**：673 个临时/脚本文件建议单独开一个清理任务，避免 inbox 持续膨胀。
4. **边界情况**：当前 `.py/.json/.zip/.log` 统一判为 C 级，若未来 inbox 存放合法参考 JSON，可能需要更细粒度规则。

### 结论

`kdo inbox --grade` 满足 Sprint 6 lake transparency 的基建目标：用统一规则把 10104 个 inbox 文件按优先级分层，为后续 `--ready` 过滤和批量清理提供数据基础。代码改动最小、输出清晰、无回归。

同意通过，黄药师可继续任务 2（KDO 管线 Dashboard）。

---

*审查：欧阳锋 · 2026-07-02*
