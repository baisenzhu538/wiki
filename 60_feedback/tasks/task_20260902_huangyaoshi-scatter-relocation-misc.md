---
id: task_20260902_huangyaoshi-scatter-relocation-misc
title: 散点归位杂项（散点审计 R7，P1）：假盘符树 + Harness 重复对 + mp4 归位
seq: 604
status: queued
assignee: huangyaoshi
created_by: wangyuyan
created_at: 2026-09-02
priority: P1
updated_at: '2026-09-02T01:25:00+08:00'
---

# #604 散点归位杂项

## 背景

风清扬审计 P1 三项归位杂项。

## 范围（三件）

1. **`C\uf03a/` 假盘符目录树**：WSL 写 `C:\...` 路径事故产物（`:` 被写成 Unicode PUA 字符）。核查内容是否全为重复垃圾 → 确认无独有内容后删除（有独有内容先归档隔离区）。
2. **Harness 重复对**：`00_inbox/Harness Engineering-….md` vs `00_inbox/Harness Engineering：….md`（md5 相同）——保留文件名规范的一份，另一份移隔离区。
3. **mp4 归位**：`60_feedback/wechat-collect/*.mp4` 6 个约 120MB 移 `10_raw/` 对应素材目录（反馈层不放素材）。若移动影响 wechat 管线脚本的路径假设，先 grep 脚本引用再动；有影响则在任务单执行报告中标注，不硬移。

## 安全栏

- 每件操作前先 grep 引用对账（含 30_wiki source_refs）。
- 假盘符树删除前列出完整文件清单入执行报告（证明无独有内容）。
- 批量三问。

## 交付物

三项处置结果 + 引用对账 + 执行报告五字段。

## 验收

欧阳锋终审：假盘符树清零 + Harness 重复对收敛 + mp4 归位且管线引用未断（或已标注）。
