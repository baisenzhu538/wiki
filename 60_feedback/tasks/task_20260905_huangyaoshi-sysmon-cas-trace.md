---
id: task_20260905_huangyaoshi-sysmon-cas-trace
title: C:\Sysmon 59G 内容寻址存储溯源与处置（已冻结改名止血；09-01 11:34 生，正值 #592 备份施工窗口）
seq: 646
status: in_progress
assignee: huangyaoshi
created_by: wangyuyan
created_at: 2026-09-05
decision_source: 老朱确认无印象（非他装）→ 王语嫣冻结止血（改名 Sysmon.frozen-20260905），写入者溯源归黄药师
reviewer: 欧阳锋
instance: huangyaoshi
updated_at: '2026-09-04T19:46:27.738569+00:00'
---

# #646 C:\Sysmon CAS 溯源与处置（黄药师）

## 背景（王语嫣 forensic 实证）

- C:\Sysmon = 59G 内容寻址存储：64-hex 大写平铺松散对象 + .pack/.idx/.rev（JGit DFS 形态）+ 检索索引快照 json（588MB 级）+ production-queue 锁 + #645 任务文本
- 目录创建于 2026-09-01 11:34——**正值 #592（异机备份三件套）施工窗口**（11:49 claim 起），头号嫌疑=备份/重建工具链的写路径指错
- 增长加速：09-03 起 +14350 文件
- 已冻结（改名 Sysmon.frozen-20260905）——若某工具报错找它，报错者=写入者

## 任务

1. **溯源**：查 #592 三件套脚本（vault-backup/vault-snapshot/vault-integrity-check/wiki-vault-restore）与坚果云同步链的写路径，找到把对象库写到 C:\Sysmon 的调用点（重点：路径变量拼接错误/环境变量默认值）
2. **处置**：确认可弃则删除 Sysmon.frozen-20260905（释放 59G）；若是某机制的"工作状态"，修复写路径指向正确位置后再清
3. 观察哨：冻结后 48h 内有工具报错找 Sysmon=写入者现行，优先走这条路收证据

## 交付

- 写入者结论（含证据）+ 处置结果（释放空间数）+ 执行报告
- claim/complete 走 queue_transition（complete 646）
