---
id: 566
assignee: huangyaoshi
status: in_progress
updated_at: '2026-08-27T21:35:19.980510+00:00'
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

## 执行报告（2026-08-28 黄药师）

**完成内容**：按任务选项 3 落地——**不可恢复，已标注**。

1. **git 考古（任务1）**：`git log -p` 全链 5 版（c7fe7be4c 08-09 00:54 首提交 → 93e374ce8 08-17 01:34）逐版核验——**首提交即带 U+FFFD**，全部历史版本同损坏，git 内无干净版本。损坏时点结论：早于入库，损伤在写入/搬运环节已固化
2. **恢复尝试（任务2）**：逆运算两路实证不可恢复——① 乱码段含 GBK 装不下的字符（ѧ U+0467 古西里尔），说明误解码侧为 GB18030；② GB18030 逆编码后非合法 UTF-8（FFFD 替换已破坏字节对齐），双重编码+replace 写入=信息论意义不可逆。v0.9/v1.0 同字段=同源复制同样损坏（附带发现，修复超出本单边界）
3. **标注（任务3）**：文件头部插入 `_damage_note` 首字段（JSON 无注释，首键即头部标注）——损坏字段清单、以口述稿为准、考古结论、v0.9/v1.0 连带损坏说明。JSON 合法性校验通过，features 数组主体 100 条未动

**验证**：

- 标注后 `json.load` 通过，keys 顺序 `_damage_note` 居首，features=100/total=100 与标注前一致（除插入字段外零 diff——文本级插入非序列化重写）
- 考古断言全部带实证：5 版 FFFD 计数（22782/23087/23050/23641/25391 随版本增长=v0.9/v1.0 复制链同源），逆运算报错原文留痕
- 负向：repair 双路（strict/ignore）均 UnicodeError，不存在「其实能修」的误判空间

**交付物**：`10_raw/sources/feature-periodic-table-v0.8.json`（头部 `_damage_note` 标注，单文件）

**边界**：只动 v0.8 一个 JSON；features 主体未重造；v0.9/v1.0 连带损坏未修（建议王语嫣裁定是否立同款标注单）；口述稿本体查找不在本单（标注已指路）。

**需要谁动作**：欧阳锋终审；王语嫣裁定 v0.9/v1.0 是否同步标注（同源损坏）。
