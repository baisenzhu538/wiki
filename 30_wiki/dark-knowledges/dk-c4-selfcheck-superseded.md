---
id: dk-c4-selfcheck-superseded
title: C-4：自检误报 superseded 页面→终态卡片被标记为未 enrich
type: dk
dark_knowledge_type: failure
status: enriched
domain:
- src_unknown
source_person: Builder
source_context: 2026-05-03
source_refs:
- src_unknown
created_at: 2026-05-31
updated_at: '2026-06-18'
related:
- src_unknown
- src_unknown
- src_unknown
- src_unknown
- src_unknown
- src_unknown
- src_unknown
- src_unknown
pipeline:
- src_unknown
- src_unknown
author: unknown
reviewed_by: 欧阳锋
confidence: 0.88
trust_level: medium
diagnostic_signals:
- signal: src_unknown
  framework_lens: 终态状态被错误地纳入未 enrich 检查：superseded 表示已被替代/废弃，不应参与 enrich 统计
  follow_up_question: 检查 `_check_unenriched_wiki` 函数的 skip 集合是否包含 superseded；确认 schema
    中终态 status 的完整列表
- signal: src_unknown
  framework_lens: skip 集合作为跨函数约定，必须与状态机终态保持同步；复制逻辑会继承缺陷
  follow_up_question: 梳理所有读取 status 做过滤/跳过的函数，统一 skip 集合或抽取公共常量；为新增 status 建立同步 checklist
- signal: src_unknown
  framework_lens: 新增终态 status 时只改 schema 不改 skip 集合，是系统性误报的直接诱因
  follow_up_question: 每新增一个 status，先判定是中间态还是终态；终态必须同步到所有检查函数的 skip 集合
---# C-4：自检误报 superseded 页面→终态卡片被标记为未 enrich

## 原始表述

> `kdo self-check --dry-run` 将 `status: superseded` 的页面报为"未 enrich"。
>
> 根因：`_check_unenriched_wiki` 函数的 skip 集合里没有包含 `superseded`。
>
> 修正：已修复。skip 集合加入 `superseded`。

## 核心洞察

- src_unknown
- src_unknown
- src_unknown
- src_unknown

## 使用场景

- src_unknown
- src_unknown
- src_unknown
- src_unknown

## 操作方法

1. **识别终态页面**：`superseded` 表示"已被新版替代/废弃"，是终态——不需要 enrich，也不应参与未 enrich 统计
2. **检查 skip 集合**：打开 `_check_unenriched_wiki` 函数，确认 skip 列表包含所有终态 status：`superseded`、`draft`（如果 draft 也不需要 enrich）等
3. **确认修复已生效**：运行 `kdo self-check --dry-run`，验证 `superseded` 页面不再出现在报告中
4. **同步更新所有相关函数**：如果项目中有多个检查函数（如 `_check_unenriched_wiki`、`_check_stale_pages`、lint 规则），确保 skip 集合一致
5. **新增 status 时的 checklist**：每新增一个 status 值，自问"这是需要 enrich 的中间态，还是不需要处理的终态？"——终态必须加入所有 skip 集合

## 适用边界

- src_unknown
- src_unknown
- src_unknown
- src_unknown
- src_unknown

## 常见失败模式

| 失败模式 | 真实症状 | 可执行修复 |
|:-----|:-----|:-----|
| skip 集合遗漏 `superseded` | `kdo self-check --dry-run` 将终态页面报为"未 enrich" | 在 `_check_unenriched_wiki` 等函数的 skip 集合中加入 `superseded` |
| 多个检查函数 skip 集合不一致 | 某些工具跳过 superseded，另一些仍误报或漏检 | 统一 skip 集合；抽取公共终态常量；为所有过滤逻辑补单元测试 |
| 新增终态 status 未同步 skip 集合 | 新增 `archived`/`deprecated` 后，self-check 误报率突然上升 | 建立"新增 status → 判定终态 → 更新所有 skip 集合"的 checklist |
| 临时复活旧版本未移出 skip 集合 | 需要重新 enrich 的页面被漏检 | 临时移除或单独标记，完成后再恢复 skip |
| superseded 页面被外部引用且含错误信息 | 自检跳过但错误继续影响下游 | 优先修正引用、添加 redirect 或 frontmatter 警告，而非简单跳过 |

## 为什么值钱

- src_unknown
- src_unknown
- src_unknown
- src_unknown

## 与其他知识的关联

- src_unknown
- src_unknown
- src_unknown

## 老顽童疑问（2026-05-31）

无疑问，请欧阳锋审查。
