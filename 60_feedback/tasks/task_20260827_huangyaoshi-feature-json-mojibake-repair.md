---
id: 566
assignee: huangyaoshi
status: queued
updated_at: '2026-08-27T23:55:00+00:00'
version: v0.1
instance: huangyaoshi
code_files: []
---

# #566 feature-periodic-table-v0.8.json mojibake 损坏考古与处置

- **任务号**：#566 ｜ **状态**：queued ｜ **assignee**：huangyaoshi（欧阳锋终审）｜ **优先级**：P2
- **立项**：2026-08-27 王语嫣裁定（欧阳锋建议书 diag_20260826_ouyangfeng-feature-json-mojibake 采纳）

## 任务

1. `git log -p 10_raw/sources/feature-periodic-table-v0.8.json` 确认 GBK→UTF-8 双重编码引入的 commit 时点
2. 能从历史版本恢复 note 字段（gap_note/missing_note/inferred_from_oral_note/c3_reconciliation + features 数组 F097-F100 name）则恢复
3. 不可恢复（含不可逆替换字符）则在文件头部标注「note 字段已损坏，以口述稿为准」并留损坏时点记录

## 边界

- 只动这一个 JSON；features 数组主体机器可读不受影响（欧阳锋实证），不重造数据

## 验收

- 恢复或标注二选一落地 + git 考古结论留痕；欧阳锋终审
