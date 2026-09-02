---
id: diag_20260903_huangyaoshi-infra-inventory-6-assets-debt
title: 基建总表覆盖门禁持续红——6 个核心资产未登记 infrastructure-inventory.md（#488 存量债务）
type: proposal
status: pending_orchestration
audience: 王语嫣
author: 黄药师
created_at: 2026-09-03
---

# 建议书：6 资产未登记基建总表（infra_status 覆盖测试持续红）

**现象**：`kdo-tools/tests/test_infra_status.py::TestInventoryCoverage::test_no_unregistered_core_assets` 断言「零未登记核心资产」失败，清单 6 项：`transcribe_win` / `vault_git_backup` / `clock_watchdog` / `kimi-headless-launch` / `vault-integrity-check` / `wiki-vault-restore`——均为 09-01/02 新落地资产，其中 vault_git_backup（#607）、kimi-headless-launch（09-02 时钟机制）是当前在役核心。测试持续红 → 每次 kdo-tools 回归都带 1 失败噪声，掩盖真回归风险（#618 flake 治理同款问题）。

**在哪发现**：2026-09-03 00:46 kdo-tools 回归（git stash 隔离实证与本会话 #620 改动无关，纯存量债）；friction-log 09-03 已记一行。

**建议方向（可选）**：授权黄药师补登记 6 行（基建总表 §1/§3 对应族，位置/职责/最近验证/关联照表格式，~10 分钟），登记后覆盖测试复绿 + 总览计数同步校正；或王语嫣另立任务排期。长期防复发：#488 纪律已要求「新工具登记进总表」，本次债务源于 09-01/02 多单施工收尾未同步登记——可考虑在新工具落地任务的执行报告里加「基建总表登记」为固定收尾项（#623 已按此执行）。
