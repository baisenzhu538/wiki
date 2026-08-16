---
reviewed_by: 欧阳锋
review_date: 2026-08-09
id: task_20260809_huangyaoshi-dashboard-grade-badges
assignee: huangyaoshi
status: reviewed
updated_at: 2026-08-09
priority: P1
wsjf: 3.0
---

# dashboard 终审等级标注（#302 · 用户要求看板一目了然）

## 任务目标

看板（dashboard.html）标注每个任务的终审等级（A/A-/B+/B/B-/C）——用户要求"看板要一目了然，需要标注 A 还是 A- 还是 B+ 等等状态"。

## 规格

1. **等级解析**：generate-dashboard.py 从队列行终审记录提取等级——匹配模式 `PASS A` / `PASS A-` / `PASS B+` / `PASS（条件）B+` / `PASS(条件)A-` 等（含条件标注）；解析函数 `parse_grade(row)`
2. **每任务标注**：已完成（reviewed）任务行显示等级徽章（A / A- / B+ / B / B- / C）；条件 PASS 显示"条件"标记
3. **等级分布统计**：看板顶部汇总（A×N / A-×M / B+×K / …）
4. **着色规则**：A 绿 / A- 浅绿 / B+ 黄 / B 橙 / B- 橙红 / C 红（与首交率阈值色系一致）
5. **无等级任务**：queued/claimed/pending_review 不显示徽章（显示"进行中/待审"）

## 验收标准

- 生成后 dashboard.html 每个 reviewed 任务可见等级徽章
- 分布统计与队列行终审记录对账一致（抽查 10 个）
- 条件 PASS 正确标注（如 #282 PASS(条件)B+）
- 无等级任务不误标

## 参考

- `60_feedback/tasks/task_20260809_huangyaoshi-dashboard-first-submit-rate.md`（#269 首交率——同脚本扩展）
- 队列行终审记录格式：`✅欧阳锋终审PASS A(2026-08-09)` / `PASS（条件）B+`

## 边界

- 只改 generate-dashboard.py 展示层，不动队列状态机
- 不修改已 reviewed 任务（只读解析）
