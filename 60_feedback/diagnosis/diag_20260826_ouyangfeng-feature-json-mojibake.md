---
id: diag_20260826_ouyangfeng-feature-json-mojibake
title: feature-periodic-table-v0.8.json 元数据字段 mojibake 不可逆损坏
type: proposal
status: orchestrated
author: 欧阳锋（审查）
audience: 王语嫣
date: 2026-08-26
orchestration: 已裁定（08-27 王语嫣）：采纳立项 #566（黄药师 P2 考古恢复或标注）
---

# 建议书：feature-periodic-table-v0.8.json 元数据字段 mojibake 损坏

- **日期**：2026-08-26
- **作者**：欧阳锋
- **来源**：#544 批次过审 framework-truman-feature-thinking-core 时取证发现

## 现象

`10_raw/sources/feature-periodic-table-v0.8.json` 的 `gap_note` / `missing_note` / `inferred_from_oral_note` / `c3_reconciliation` 字段为 GBK→UTF-8 双重编码乱码，且含不可逆替换字符（），无法还原。features 数组内部分 name 字段同样受损（如 F097/F098/F099/F100 的 name）。

## 影响

该 JSON 是 Feature 周期表的单一真相源（被 framework 卡 source_refs 引用、被 feature_menu.py 数据链消费）。note 字段损坏不影响机器读 features 数组主体，但人读审计（gap  reconcile 依据）已不可取证。

## 建议方向

黄药师确认损坏时点（git log 该文件，看哪次 commit 引入双重编码），能从历史版本恢复则恢复；不能恢复则在文件内标注"note 字段已损坏，以口述稿为准"。P2 级。
