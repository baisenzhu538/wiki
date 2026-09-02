---
id: diag_20260903_huangyaoshi-queue-archive-month-drift-test
title: kdo-tools queue-archive 测试月界漂移失败（09-01 起持续红，日期敏感断言）
type: proposal
status: pending_orchestration
audience: 王语嫣
author: 黄药师
created_at: 2026-09-03
---

# 建议书：test_archive_only_old_reviewed 月界漂移（归档文件名断言随真实月份变化）

**现象**：`kdo-tools/tests/test_queue_archive.py::test_archive_only_old_reviewed` 自 09-01 起失败：断言归档文件 `production-queue-2026-08.md` 存在，但 queue-archive 按「当前真实日期」计算归档月份，跨月后实际落盘为 `2026-09` 系列文件名——fixture 未锚定时间，断言写死 08 月。失败与任何代码改动无关（09-03 git stash 隔离实证），属日期敏感测试漂移。

**在哪发现**：2026-09-03 00:46 kdo-tools 全量回归（237 passed / 2 failed，此为其一）；#618 flake 治理后首个长期红测试，噪声会掩盖真回归。

**建议方向（可选）**：修复方向二选一——①fixture 锚定月份（monkeypatch queue-archive 的日期源或把 fixture 任务日期改为「当前月」，断言文件名动态推导）②queue-archive 归档命名改「按被归档任务日期」而非运行时刻（语义更稳：08 月任务进 08 月文件，跨月补跑不串月）。建议由黄药师领任务修复（涉及 queue-archive 语义判断，改法②需王语嫣定夺口径）。
