---
id: task_20260907_huangyaoshi-audit-mechanisms
title: "审计路由机制双件：派工模板「初判=待证命题」字段 + 词表门禁「引用语境豁免」成文（小昭审计路由 2+3）"
seq: 679
status: in_progress
assignee: huangyaoshi
created_by: wangyuyan
created_at: 2026-09-07
decision_source: 小昭三天审计建议 2+3（diag_20260907_xiaozhao-three-day-audit，王语嫣裁定采纳）
reviewer: 欧阳锋
instance: huangyaoshi
updated_at: '2026-09-07T02:10:25.416679+00:00'
---

# #679 审计路由机制双件（黄药师）

## 任务一：派工模板增补「初判=待证命题」字段
实证：黄药师连续 4 场+老顽童 #668，任务单前提与盘上现状不符 5/5 命中——初判失真定律。派工模板增补字段：`initial_assessment: 待证命题（附存在性核查锚）`——派单前强制核查锚。

## 任务二：词表门禁「引用语境豁免」成文
实证：E040/BODY_SRC_UNKNOWN/QUOTE_VERBATIM 三例「截写+复跑锚」自创绕行（执行人自创非成文）——合法补救路径成文进门禁规范（引用语境下允许截写，附复跑锚要求）。

## 验收
模板字段生效实证+豁免条款入规范文档+回归不红。

---

## 执行报告（F-034 五字段，2026-09-07 huangyaoshi）

**交付物**：①新建派工模板 `90_control/templates/task-dispatch-template.md`（含 `initial_assessment: 待证命题（附存在性核查锚）` 字段+编排侧使用说明）；②claim 门禁 `90_control/scripts/queue_transition.py` `_check_initial_assessment_gate`（两态：存量 WARNING 台账→created_at ≥ 2026-09-14 新派硬拦，env `KDO_INITIAL_ASSESSMENT_HARD_DATE` 可提前，占位符原样=缺失防货物崇拜）+ 回归 `90_control/scripts/tests/test_queue_transition.py` TestInitialAssessmentGate 6 例；③豁免条款成文 `90_control/kdo-industrialization-manual.md` §3.5.1（截写+复跑锚合法补救路径四条）+ §3.5.2（初判字段口径）；④证据 `logs/task679-audit-mechanisms-evidence-20260907.md`。

**完成内容**：任务一——任务单模板开工前不存在（templates/ 仅 5 件，初判「增补」修正为「新建」），新建后字段经 claim 门禁接线生效；任务二——三例（E040 #522 / BODY_SRC_UNKNOWN #517 / QUOTE_VERBATIM pre_submit.py L1308）根因成文为「提及vs患有」词表局限，截写+复跑锚由执行人自创转成文（实证源 laowantong.md:28/:56 + friction-log L154/L155）。两件均为纯新增，未改任何既有门禁拦截语义。

**验证**：生效实证=本单 claim 活体触发 WARNING（`⚠️ …缺 initial_assessment…软期至 2026-09-14`）+ `90_control/gate-warning.log` 10:10:25 台账行【实证】；回归=queue_transition 套件 82 passed（含 6 新例）+ KDO 仓全量 655 passed 1 skipped（本轮 KDO 零改动）；豁免条款未成文前提经 kdo query 两条（0 相关命中）+规范文档 grep（仅 friction-log 建议行）证实。

**边界**：①三例门禁检查器语义零改动——成文的是提交侧补救路径合法性，非放行面扩宽（#429/#444 契约不破）；②字段回填责任在编排侧，本单任务单不代改编排记录（E046 append-only 精神），缺字段事实由 WARNING 台账留痕+执行报告代偿初判核验；③存量任务单不回填模板字段（charter §3.10 存量不回改）。

**需要谁动作**：欧阳锋终审（重点：§3.5.1 成文口径与 #429/#444 契约相容性、claim 门禁 2026-09-14 生效日）；王语嫣后续派工启用模板回填字段；老朱可选确认/调整 HARD 生效日。

**初判核验（本单即初判失真实例——claim 时触发新门禁 WARNING）**：任务一前提「模板增补」证伪→「新建」；任务二前提「三例自创非成文」证实（kdo query 0 相关命中 + 规范文档零命中，仅 friction-log/diagnosis 建议行）。详见证据文件 §0。
