---
id: task_20260907_huangyaoshi-activate-tags-gate
title: "激活 pre-submit _check_tags 门禁（检查器已存在未接线 L821）+ dk 1-3 词维度规则"
seq: 677
status: queued
assignee: huangyaoshi
created_by: wangyuyan
created_at: 2026-09-07
decision_source: 老朱三连问（标签有门禁吗/欧阳锋为何没查/其他角色呢）——检查器在未接线实锤（pre_submit.py L821 注释）
reviewer: 欧阳锋
instance: huangyaoshi
updated_at: '2026-09-07T09:00:00+08:00'
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
