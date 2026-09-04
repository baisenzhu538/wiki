---
id: task_20260904_huangyaoshi-qingdanti-into-production-spec
title: 生产规范补清单体标准：工业化手册/卡产出规范引用清单体分层标准（知行断裂规范层修复）
seq: 639
status: in_progress
assignee: huangyaoshi
created_by: wangyuyan
created_at: 2026-09-04
decision_source: 老朱 09-04 直令立项（90_control/40_outputs 规范面零引用清单体实证）
reviewer: 欧阳锋
instance: huangyaoshi
updated_at: '2026-09-04T13:20:37.043916+00:00'
---

# #639 清单体标准入生产规范（黄药师）

## 任务

1. `90_control/kdo-industrialization-manual.md` 卡产出规范节补「清单体结构标准」：分层≤3 层/编号序列/重点前置/提出-展开-回收/一分钟扫完——引用 yt-note 卡族为方法论锚（不复制内容只链接）
2. pre-submit 或质检词表加轻量提示（WARNING 档）：超长无分层段落提醒
3. 归 regression 一则

## 交付

- 手册 diff + 门禁提示 + 回归 + 执行报告
- claim/complete 走 queue_transition（complete 639）

## 执行报告（黄药师 2026-09-04）

**交付物**
- `90_control/kdo-industrialization-manual.md` §12.2.1「清单体结构标准」（分层≤3层/编号序列/重点前置/提出-展开-回收/一分钟扫完；方法论锚 yt-note 卡族五链只链不抄；含门禁落点说明）
- `Knowledge Delivery OS 0.0.1/kdo/pre_submit.py` 新门禁 `_check_qingdanti_structure`（WARNING 档：连续散文化段落 ≥8 行 / 单段 ≥400 字提醒重组；跳过代码围栏；只向前生效）+ run_pre_submit 注册 + listed_gates 登记
- `Knowledge Delivery OS 0.0.1/tests/test_pre_submit_qingdanti_structure.py` 回归 7 例（命中/清单体结构不命中/代码围栏豁免/单段超长/非 30_wiki 不查/短散文不误伤/CLI 渲染）
- `90_control/notification-coverage-matrix.md` 行 29 登记（§3.19 总账同步）

**完成内容**
- 规范层：手册 §12.2 质量标准下新增 §12.2.1，引用 [[yt-note-checklist-concept]]/[[yt-note-fact-pattern-insight]]/[[yt-note-five-levels-training]]/[[yt-note-live-field-skill]]/[[concept-提升笔记阅读舒适度]] 为方法论锚（不复制内容只链接）
- 门禁层：pre-submit 加轻量 WARNING 提示（任务书「pre-submit 或质检词表」二选一——取 pre-submit，同 #542/#616 WARNING 提示制哲学：机器做存在性，人做正确性）

**验证**
- 新回归 7 例 + 邻近 #542/#540 回归 11 例全绿；CLI 全量 pytest 621 passed / 1 skipped，零回归
- 真实 vault 实测：30_wiki 2960 卡扫描，62 卡会触发提醒（只统计不回扫，WARNING 只向前生效于提交中的卡）；3 张已终审 yt-note/案例卡实测零误报
- wikilink 锚五链逐一核对卡片存在

**边界**
- WARNING 提示制不拦截，升阻断与否待观察期后另行裁定（同 #616 口径）
- 阈值（8 行/400 字）为首版经验值，误报多再调；存量 62 卡治理不在本单范围
- 清单体生产 skill（口述稿→清单体笔记）= #638 老顽童在建，本单只补规范层不碰 skill

**需要谁动作**
- 欧阳锋终审（手册 diff + 门禁 + 回归 + 矩阵行 29）
- 无其他角色动作；存量 62 卡是否治理由王语嫣裁定另立项
