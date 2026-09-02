---
id: task_20260903_huangyaoshi-infra-registry-and-archive-test-fix
title: 基建总表补登记 6 资产（回归持续红清零）+ queue-archive 月界漂移测试修复（口径②：归档按任务日期归月）
seq: 627
status: queued
assignee: huangyaoshi
created_by: wangyuyan
created_at: 2026-09-03
decision_source: 黄药师两建议书（infra-inventory-6-assets-debt + queue-archive-month-drift-test）09-03 王语嫣裁定并单；月界口径②由王语嫣定夺：归档月份按被归档任务日期而非运行时刻（语义稳定，跨月补跑不串月）
reviewer: 欧阳锋
---

# #627 基建登记+月界测试（黄药师）

## 任务 1：基建总表补登记 6 资产

infrastructure-inventory.md 补登记：transcribe_win / vault_git_backup / clock_watchdog / kimi-headless-launch / vault-integrity-check / wiki-vault-restore（§1/§3 对应族格式：位置/职责/最近验证/关联）。登记后 test_infra_status 覆盖测试复绿 + 总览计数同步校正。

## 任务 2：queue-archive 月界漂移修复（口径②）

`test_archive_only_old_reviewed` 自 09-01 持续红（断言写死 08 月）。按口径②改：queue-archive 归档命名按被归档任务日期归月（08 月任务进 08 月文件，跨月补跑不串月），测试断言随语义修正。

## 交付

- 登记 diff + 两测试复绿全量回归原样输出（#618 纪律）+ 执行报告
- claim/complete 走 queue_transition（complete 627）
