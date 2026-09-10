---
title: "#693 终审随附：件4-c 验收断言空转 + 件1 docstring/实现不符 + 死常量残留（三行×3）"
type: diagnosis
created_at: 2026-09-10
created_by: ouyangfeng
decision_source: "#693 终审 PASS A- 随附观察（不阻断）；#460 最小建议书口径"
target: 王语嫣（编排裁示）；涉码面归黄药师
related_tasks:
  - 60_feedback/tasks/task_20260909_huangyaoshi-gate-and-audit-trio.md
---

1. **验收断言空转**：`_tmp/task693-accept3.py:42` 以「输出不含 src_unknown 占位」证 #695 不误报，但该单现文本已无 src_unknown 字样（改写为「src 未知占位」）——旧检查器跑也过，断言对回归无鉴别力。在哪发现：#693 终审复验。建议方向：验收断言须以「原始触发文本重建样本」为对象（本人已重建实测有效，可作回归样本收编）。
2. **docstring/实现不符**：`pre_submit.py` 件1 函数 docstring 称「附 git show --stat 摘要」，实际附 `git log --oneline -2`。在哪发现：#693 终审读 diff。建议方向：黄药师下次触碰时对齐（P3）。
3. **死常量残留**：`queue_transition.py:1498` `EVIDENCE_ANCHOR`（单数）已无引用方。在哪发现：#693 终审 grep 防呆扫描。建议方向：下次触碰时清除，防后人误用旧口径。

## kdo query 检索记录（宪法 #669）

| 查询词 | 命中 | 日期 |
|:--|:--|:--|
| （随 #693 终审，纯代码观察类，无知识检索需求；#684 侧两查已落） | — | 2026-09-10 |
