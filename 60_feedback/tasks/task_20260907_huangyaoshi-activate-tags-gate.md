---
id: task_20260907_huangyaoshi-activate-tags-gate
title: "激活 pre-submit _check_tags 门禁（检查器已存在未接线 L821）+ dk 1-3 词维度规则"
seq: 677
status: pending_review
assignee: huangyaoshi
created_by: wangyuyan
created_at: 2026-09-07
decision_source: 老朱三连问（标签有门禁吗/欧阳锋为何没查/其他角色呢）——检查器在未接线实锤（pre_submit.py L821 注释）
reviewer: 欧阳锋
instance: huangyaoshi
updated_at: '2026-09-07T01:01:16.986303+00:00'
evidence: logs/task677-tags-gate-evidence-20260907.md
---

# #677 激活 tags 门禁（黄药师，一行接线+规则扩展）

## 实证
`pre_submit.py` L821-852：`_check_tags` 检查器完整存在（空 tags/缺 audience:scene 判定逻辑齐备），注释自证"To activate: add '_check_tags(root, target_files)' to run_pre_submit"——**未接线**。15 个 check 在跑，tags 不在其中。

## 任务
1. run_pre_submit 激活 `_check_tags`（一行）
2. 规则扩展：dk 卡 tags 1-3 词核心维度（#498）/普通卡 5-8 词/空串残渣清理
3. 两态：先 WARNING 一周→升 HARD（与 #669 检索记录同节奏）

## 验收
- 用今天 2 张零 tags 卡复现→WARNING 实证
- 合规卡（标杆卡 meeting-iceberg）通过实证
- 回归不红

## 执行报告（F-034 五字段，2026-09-07 huangyaoshi）

**交付物**：KDO 仓 commit `0c44c12`——`Knowledge Delivery OS 0.0.1/kdo/pre_submit.py`（死代码提取为真函数 `_check_tags` + 接线 `run_pre_submit` + #498 词量口径 + 两态 `TAGS_HARD_DATE=2026-09-14`/env `KDO_TAGS_HARD_DATE`）+ 新增回归 `Knowledge Delivery OS 0.0.1/tests/test_pre_submit_tags_gate.py` 15 例；验证证据 `logs/task677-tags-gate-evidence-20260907.md`。

**完成内容**：①接线激活——【实证】"检查器完整存在"与实际不符：`def _check_tags(...)` 行在 8bc5645 批量提交时丢失，检查器主体是困在 `_check_aliases_has_source_name` 的 `return`（L817）之后的死代码，按注释直接加调用会 NameError；本轮提取成真函数后接线。②规则扩展——普通卡全部条目 5-8、dk 卡核心词（非 `:` 条目）1-3、空串残渣清理（剥离后计数）；原死代码 framework→method 检查不接线（registry `method` 为 layer:chunk+labeling:auto 非卡作者职责，实证 309 张 framework 仅 19 张带且标杆卡无）；dk source-person/source-context-type 维度接受 tags 标签或 frontmatter `source_person`/`source_context` 字段双通道（新式卡实证承载）。③两态 WARNING 软一周（至 2026-09-14）→HARD，env 可提前，与 #669 同节奏。

**验证**：TDD 先红（ImportError=函数未成形，失败原因正确）后绿（15/15）；全量回归 654 passed 1 skipped 零红；缺陷态活体复现——两 dk 卡 09-06 18:31 前版本（git `4179de376^`，`^tags:` 计数 0/0）双双 WARNING；标杆卡 meeting-iceberg 走 `run_pre_submit` 接线路径 tags 门禁 0 issue、passed=1 failed=0（另 3 条 issue 属 quote_verbatim/concept_crosscheck/quality_score 其他门禁）；HARD 态 env 翻转 severity=error failed=2。

**边界**：【实证·验收前提已失真】"今天 2 张零 tags 卡"在抽检时点为真，但两卡 tags 已于 09-06 18:31/18:42（vault backup `4179de376`/`d941b99a1`，早于本单立项）补齐——缺陷复现改用 git 历史版本完成；现行态 0 误报。词量计数口径存在解释空间（维度标签是否计词）：普通卡计全部条目（标杆卡 6 条合规的唯一读法）、dk 卡只计核心词（否则与 registry dk 必备维度 ≥4 数学冲突），不对称裁定详见证据文件「口径裁定」节，请欧阳锋终审。

**需要谁动作**：欧阳锋终审（重点：词量计数不对称口径 + framework→method 不接线两处裁定）；2026-09-14 软期结束前 dk/普通卡不合规存量由内容侧（老顽童/王语嫣）治理，逾期 tags WARNING 升 HARD 拦截。

## 机器预审报告

> 🤖 机器预审参考层（#515）：仅供欧阳锋终审参考，不构成结论、不放行不拦截

### ① 声称-交付差集

✅ 3 个声明路径全部存在+已跟踪+无脏改动
### ② lint

✅ frontmatter 可解析 + F-034 五字段在位
### ③ 负向判词 / ④ 存在性核查

🔴 意见书含负向断言（丢失）但无 `**存在性核查**` 锚点（#433：'我没看到'≠'不存在'，负向判词必须附核查节，否则不闭环）（生产侧同口径，供终审对照）
