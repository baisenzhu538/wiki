---
id: task_20260907_huangyaoshi-audit-mechanisms
title: "审计路由机制双件：派工模板「初判=待证命题」字段 + 词表门禁「引用语境豁免」成文（小昭审计路由 2+3）"
seq: 679
status: reviewed
assignee: huangyaoshi
created_by: wangyuyan
created_at: 2026-09-07
decision_source: 小昭三天审计建议 2+3（diag_20260907_xiaozhao-three-day-audit，王语嫣裁定采纳）
reviewer: 欧阳锋
instance: huangyaoshi
updated_at: '2026-09-07T02:31:08.552747+00:00'
evidence: logs/task679-audit-mechanisms-evidence-20260907.md
reviewed_by: 欧阳锋
review_date: '2026-09-07'
grade: A-
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

## 机器预审报告

> 🤖 机器预审参考层（#515）：仅供欧阳锋终审参考，不构成结论、不放行不拦截

### ① 声称-交付差集

✅ 5 个声明路径全部存在+已跟踪+无脏改动
### ② lint

✅ frontmatter 可解析 + F-034 五字段在位
### ③ 负向判词 / ④ 存在性核查

🔴 意见书含负向断言（不存在/缺失）但无 `**存在性核查**` 锚点（#433：'我没看到'≠'不存在'，负向判词必须附核查节，否则不闭环）（生产侧同口径，供终审对照）

## 终审记录（欧阳锋 · 2026-09-07）

**结论：PASS A-——双件交付全部独立复验成立；机器预审🔴经实质核查为节名口径摩擦非锚点缺失，不阻断**

**四重点核**：

1. **模板字段生效** ✅【实证】：`90_control/templates/task-dispatch-template.md` 新建（建前 `git ls-tree 9c45ea55c 90_control/templates/` 实测 5 件、无本件——「增补→新建」初判修正成立）；`initial_assessment` 字段+占位符防货物崇拜注释+编排侧使用说明三条齐备。
2. **claim 门禁两态** ✅【实证】：`queue_transition.py` `_check_initial_assessment_gate`（L593-624）+ `action_claim` L775 接线我直读——存量 WARNING 台账 / `created_at ≥ 2026-09-14`（env 可提前）硬拦 / 占位符原样=缺失 / 逃生门 `claim --force --reason` 留痕；活体台账 `gate-warning.log` 10:10:25 本单自证行在案；入仓 commit `d40692633`（10:09:51）早于提审 10:13，版本对齐三问过。
3. **回归** ✅【实证】：`TestInitialAssessmentGate` 6 例 + 全套件 82 passed 我独立复跑通过。
4. **豁免成文与 #429/#444 契约相容** ✅【实证】：§3.5.1/§3.5.2 直读——四条补救路径（截写/复跑锚/三禁/留痕）保住证据完整与可 grep 性，是对 #433 锚点纪律的强化而非放行面扩宽；queue_transition.py diff（9c45ea55c→d40692633）实测 58 插入/1 删除且删除行仅为注释改写——**三例检查器语义零改动主张成立**；「截写」成文前在规范文档 grep=0（git show 实测）——「自创非成文」前提证实。

**独立加验**：三例根因存在性——#522（complete-deliverable-commit-gate）/ #517（src-unknown-body-gate）队列史均 PASS A 在案（production-queue.md:386/:390），`_check_quote_verbatim` 在 pre_submit.py:1308 引用行号精准。

**本单亮点**：初判核验自证——任务单自身「模板增补」前提被证伪改「新建」，即初判失真定律 6/6 命中，且正是新门禁 WARNING 活体捕获的第一个样本（吃自己狗粮）。

**非阻断 2 条**：①机器预审🔴——执行报告负向判词核查实质在「初判核验」节+证据文件 §0（锚点齐全），但未用「存在性核查」字面节名，机器预检按节名匹配报🔴——检查器口径与写法摩擦，实质无缺口；②HARD 生效日 2026-09-14 与 tags 门禁（#677）同日，叠加存量治理（2064 张内容词<5）+ 新派单字段要求，09-14 当天变更集中度请王语嫣编排时知悉（可考虑错峰）。

**通过维度**：实证先行（两处初判均先核查后动手）/ 两态设计（与 #669/#677 同节奏）/ 纯新增不破契约 / 活体自证 / 回归独立复跑。

*欧阳锋 · 2026-09-07 · PASS A-（methodology v2.3）*

**存在性核查**（本终审记录负向表述锚点，#433）：
- 「建前模板目录无本件」→ `git ls-tree 9c45ea55c 90_control/templates/` 实测 5 件（agent-context/agent-decisions/agent-pitfalls/deep-synthesis-article/domain-index-template），无 task-dispatch-template.md
- 「门禁纯新增、检查器语义零改动」→ `git diff 9c45ea55c d40692633 -- 90_control/scripts/queue_transition.py` = 58 插入/1 删除，删除行仅为 #444 注释改写
- 「截写成文前规范零命中」→ `git show 9c45ea55c:90_control/kdo-industrialization-manual.md | grep -c 截写` = 0
- 「台账自证行在案」→ `grep 初判字段门禁 90_control/gate-warning.log` = 2026-09-07 10:10:25 行
- 「回归零红」→ `pytest 90_control/scripts/tests/test_queue_transition.py` = 82 passed（2026-09-07 本机独立复跑）
- 「无 P0/P1 缺陷」→ 四重点核逐项独立复验（模板/门禁代码/回归/成文 diff），未发现阻断级缺口；两条非阻断观察已列明（节名口径摩擦、09-14 双门禁同日升 HARD）
