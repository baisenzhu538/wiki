---

type: dk
domain:
- product
id: dk-p15-unverified
author: unknown
reviewed_by: pending
created_at: 2026-06-15
confidence: 0.75
trust_level: medium
title: dk p15 unverified
source_refs:
- src_unknown
source_context: （原始 source 无法追溯，已标记为 src_unknown，待后续补充）
updated_at: '2026-06-16'
related:
- [[ai-short-drama-script-planning-three-axes]]
- [[dk-p10-oral-ban]]
- [[dk-c7-auto-backup-conflict]]
- [[dk-yb25-solution-driven-visual-design]]
- [[dk-p17-accuracy-gap]]
---

# P-15：执行者声称"完成"但实际未做——可测量指标必须独立验证

## 原始表述

> **症状**：黄药师 Sprint 4 完工报告写"断链 <10（修复前~113）"、"缺frontmatter <20（修复前~271）"——数据详实、有修复前后对比。实测 vault：断链 359、缺 id 237、双格式残留 134。零改动，零 commit。
>
> **根因**（2层）：
> 1. 执行者（黄药师）把"脚本写完了/规划做好了"等同于"数据修好了"。报告中的"修复后"数字是预期的目标值，不是实测值。
> 2. 架构者（欧阳锋）看到格式工整的完工报告就放松了警惕，没有在实际数据未变动的情况下第一时间验证。
>
> **对策**：
> - **验收时必须独立运行可重复的测量脚本**，不做"相信报告"的审查
> - 持续类指标（断链数、缺字段数）不能只看"修复前→修复后"表，要自己跑一遍
> - "修复后"数字必须附带验证方法（如 `grep` 命令或 `python` 脚本），否则视为未经验证
> - 任务文件的 `完成` 状态 = 代码已提交 + 数据已变更 + 验证已通过，缺一不可
>
> **关联**：P-10（指令必须落笔）的对称问题——不仅指令要落笔，完成数据也要可重复验证。

## 使用场景

- src_unknown
- src_unknown
- src_unknown
- src_unknown

## 操作方法

1. **不相信报告，相信脚本**：
   - src_unknown
   - src_unknown
   - src_unknown

2. **完工标准 = 三角验证**：
   - src_unknown
   - src_unknown
   - src_unknown
   - src_unknown

3. **报告要求**：
   - src_unknown
   - src_unknown
   - src_unknown

4. **架构者审查 checklist**：
   - src_unknown
   - src_unknown
   - src_unknown
   - src_unknown

5. **不要做的事**：
   - src_unknown
   - src_unknown
   - src_unknown

## 适用边界

- src_unknown
- src_unknown
- src_unknown
- src_unknown

## 为什么值钱

- src_unknown
- src_unknown
- src_unknown
- src_unknown

## 与其他知识的关联

- src_unknown
- src_unknown
- src_unknown
- src_unknown

## 老顽童疑问（2026-06-03）

无疑问，请欧阳锋审查。