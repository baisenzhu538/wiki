---

id: dk-c4-selfcheck-superseded
title: C-4：自检误报 superseded 页面→终态卡片被标记为未 enrich
type: dark-knowledge
dark_knowledge_type: failure
status: enriched
domain:
- master
source_person: Builder
source_context: 2026-05-03
source_refs:
- 10_raw/sources/src_20260619_f35cd8b6_20_memory_corrections.md#C-4
created_at: 2026-05-31
updated_at: '2026-06-18'
related:
  - '[[dk-f1-regex-on-cjk]]'
  - '[[sprint-2-gate-enrich-evidence]]'
  - '[[dk-c2-dual-status-machine]]'
  - '[[plan_20260503_f3e9a2b1-improvement-plan]]'
  - '[[sprint-2-门禁举证验收]]'
  - '[[dk-c5-todo-false-positive]]'
  - '[[dk-c2-dual-status-machine]]'
  - '[[master-cognitive-bias-checklist]]'
pipeline:
- confidence-draft
- confidence-source-cited
author: unknown
reviewed_by: 欧阳锋
confidence: 0.88
trust_level: medium
diagnostic_signals:
- signal: '`kdo self-check --dry-run` 报告中出现 `status: superseded` 的页面，且被标记为"未 enrich"'
  framework_lens: '终态状态被错误地纳入未 enrich 检查：superseded 表示已被替代/废弃，不应参与 enrich 统计'
  follow_up_question: '检查 `_check_unenriched_wiki` 函数的 skip 集合是否包含 superseded；确认 schema 中终态 status 的完整列表'
- signal: '多个检查函数或自定义脚本的 skip 集合不一致，部分工具误报而终态页面被其他工具漏检'
  framework_lens: 'skip 集合作为跨函数约定，必须与状态机终态保持同步；复制逻辑会继承缺陷'
  follow_up_question: '梳理所有读取 status 做过滤/跳过的函数，统一 skip 集合或抽取公共常量；为新增 status 建立同步 checklist'
- signal: '新增 status 值（如 archived、deprecated）后，self-check 误报率突然上升'
  framework_lens: '新增终态 status 时只改 schema 不改 skip 集合，是系统性误报的直接诱因'
  follow_up_question: '每新增一个 status，先判定是中间态还是终态；终态必须同步到所有检查函数的 skip 集合'
---# C-4：自检误报 superseded 页面→终态卡片被标记为未 enrich

## 原始表述

> `kdo self-check --dry-run` 将 `status: superseded` 的页面报为"未 enrich"。
>
> 根因：`_check_unenriched_wiki` 函数的 skip 集合里没有包含 `superseded`。
>
> 修正：已修复。skip 集合加入 `superseded`。

## 核心洞察

- **误报的本质是"状态机终态"和"检查范围"不同步。** `superseded` 在 KDO 编译状态机中代表"已被新版替代/废弃"，是终态；但 `_check_unenriched_wiki` 的 skip 集合没把它识别为终态，导致检查范围越界。
- **"狼来了"效应会摧毁整个自检机制的可信度。** 当报告里充斥 superseded 这类假阳性，审查者会系统性脱敏，真正的未 enrich 页面反而被忽略。
- **skip 集合不是局部实现细节，而是跨函数的约定。** 一旦新增终态 status，所有读取 `status` 做过滤的函数（`_check_unenriched_wiki`、lint 规则、自定义脚本）都必须同步更新，否则一处遗漏会处处传染。
- **通用软件工程知识不会告诉你 superseded 应该被跳过。** 这是 KDO 具体实现层面的暗知识：终态页面不需要 enrich，也不应参与未 enrich 统计。

## 使用场景

- 你运行 `kdo self-check --dry-run` 检查 vault 中未 enrich 的页面，发现报告里出现了大量已废弃/被替代的卡片
- 你审查 self-check 输出时，看到 `status: superseded` 的卡片被标红，需要判断这是真问题还是误报
- 你修改 `_check_unenriched_wiki` 函数或自定义自检规则时，需要确定哪些终态 status 应该被排除在检查之外
- 你设计新的 status 值（如 `archived`、`deprecated`），需要同步更新所有 skip 集合

## 操作方法

1. **识别终态页面**：`superseded` 表示"已被新版替代/废弃"，是终态——不需要 enrich，也不应参与未 enrich 统计
2. **检查 skip 集合**：打开 `_check_unenriched_wiki` 函数，确认 skip 列表包含所有终态 status：`superseded`、`draft`（如果 draft 也不需要 enrich）等
3. **确认修复已生效**：运行 `kdo self-check --dry-run`，验证 `superseded` 页面不再出现在报告中
4. **同步更新所有相关函数**：如果项目中有多个检查函数（如 `_check_unenriched_wiki`、`_check_stale_pages`、lint 规则），确保 skip 集合一致
5. **新增 status 时的 checklist**：每新增一个 status 值，自问"这是需要 enrich 的中间态，还是不需要处理的终态？"——终态必须加入所有 skip 集合

## 适用边界

- 适用于所有运行 `kdo self-check` 或类似自检工具的场景
- **不适用于你希望 superseded 页面被重新 enrich 的特殊情况**：如复活旧版本、做历史对比分析时，可能需要临时移出 skip 集合
- skip 集合需要随 schema 演进而更新：如果新增终态 status（如 `archived`），必须同步到所有检查函数
- 如果 superseded 页面本身含有错误信息且被外部引用，可能需要保留 enrich 而非跳过——但这属于异常流程，非常态
- 自定义自检脚本如果复制了 `_check_unenriched_wiki` 的逻辑，会继承这个缺陷，需要逐行审查

## 常见失败模式

| 失败模式 | 真实症状 | 可执行修复 |
|:-----|:-----|:-----|
| skip 集合遗漏 `superseded` | `kdo self-check --dry-run` 将终态页面报为"未 enrich" | 在 `_check_unenriched_wiki` 等函数的 skip 集合中加入 `superseded` |
| 多个检查函数 skip 集合不一致 | 某些工具跳过 superseded，另一些仍误报或漏检 | 统一 skip 集合；抽取公共终态常量；为所有过滤逻辑补单元测试 |
| 新增终态 status 未同步 skip 集合 | 新增 `archived`/`deprecated` 后，self-check 误报率突然上升 | 建立"新增 status → 判定终态 → 更新所有 skip 集合"的 checklist |
| 临时复活旧版本未移出 skip 集合 | 需要重新 enrich 的页面被漏检 | 临时移除或单独标记，完成后再恢复 skip |
| superseded 页面被外部引用且含错误信息 | 自检跳过但错误继续影响下游 | 优先修正引用、添加 redirect 或 frontmatter 警告，而非简单跳过 |

## 为什么值钱

- self-check 的误报会产生**"狼来了"效应**：如果报告里充斥假阳性，审查者会对整个报告脱敏，真正的未 enrich 页面会被忽略
- 这是 KDO 特有的工具行为组合：`superseded` 作为编译进度状态机的终态，和 `self-check` 的 skip 集合之间缺少同步——这个具体知识不在任何通用软件测试教材中
- 揭示了维护自检工具的核心原则：**skip 集合必须与状态机终态保持同步**。新增 status 时只改 schema 不改 skip 集合，是系统性错误的温床
- 通用编程知识会告诉你"写测试要覆盖边界情况"，但不会告诉你"KDO 的 self-check 需要跳过 superseded"

## 与其他知识的关联

- [[dk-c5-todo-false-positive]] — 同一模式：自检工具的字符串/规则匹配误报。C-4 是 skip 集合缺失导致的误报，C-5 是字符串匹配过宽导致的误报——两者都会降低自检报告的可信度
- [[master-cognitive-bias-checklist]] — 认知偏差中的"告警疲劳"：当假阳性率高时，人类会系统性忽略所有告警，包括真阳性。C-4 和 C-5 如果不修复，会摧毁整个 self-check 机制的有效性
- `20_memory/corrections.md` → C-4（原始记录）

## 老顽童疑问（2026-05-31）

无疑问，请欧阳锋审查。
