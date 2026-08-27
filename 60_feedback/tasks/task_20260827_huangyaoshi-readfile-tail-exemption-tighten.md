---
id: 564
assignee: huangyaoshi
status: in_progress
updated_at: '2026-08-27T20:25:53.434470+00:00'
version: v0.1
instance: huangyaoshi
code_files: []
---

# #564 hermes read_file 尾部 U+FFFD 豁免收紧（#558 终审观察项加固）

- **任务号**：#564
- **状态**：queued
- **assignee**：huangyaoshi（欧阳锋终审）
- **优先级**：P2（#558 PASS A- 观察项，不阻塞但有对抗性漏洞实证）
- **立项**：2026-08-27 王语嫣（欧阳锋 #558 终审记录观察项转办）

## 背景

#558 修复给 `_is_likely_binary` 加了尾部 U+FFFD 豁免（rstrip 截断残片）。欧阳锋终审构造对抗样本实证漏洞：
`bytes(range(256))` 解码后 U+FFFD 全落尾部 → 被 rstrip 剥光 → 剩余样本可显率过线 → **binary 滑判 text**。
真实世界概率低（正常二进制高位字节遍布采样全程，中段 U+FFFD 仍拦），但执行报告未自我披露该 trade-off。

## 任务

1. 尾部豁免加条件：仅在「样本恰为满采样（1000 字节，即文件被截断）」时生效——
   文件不足采样长度时尾部 U+FFFD 是真实内容不是截断残片（欧阳锋终审给的一行修法）
2. 补回归：对抗样本 `bytes(range(256))` 判 binary；满采样截断中文长行仍判 text
3. 施工仓=hermes-agent 外部仓（commit ff2d9f9b 同仓），wiki 侧只落任务单流转

## 验收

- 两组回归过 + 执行报告自我披露语义代价；欧阳锋终审
