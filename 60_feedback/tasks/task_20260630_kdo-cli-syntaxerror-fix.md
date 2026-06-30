---
id: task_20260630_kdo-cli-syntaxerror-fix
type: task
status: queued
assignee: 黄药师
priority: P1
created_at: 2026-06-30
updated_at: 2026-06-30
reviewer: 欧阳锋
source_refs:
- 90_control/plan-state-json-to-sqlite-migration.md
related:
- task_20260630_kdo-query-label-filter
- task_20260630_community-knowledge-failure-modes
---

# 修复 kdo CLI SyntaxError（kdo/commands/delivery.py:686）

## 问题来源

老顽童在执行 #34 `task_20260630_community-knowledge-failure-modes` 时，调用 `python -m kdo pre-submit` 触发 `SyntaxError: expected 'except' or 'finally' block`，报错位置为 `kdo/commands/delivery.py:686`。

## 目标

定位并修复 `kdo/commands/delivery.py` 第 686 行附近的语法错误，使 `python -m kdo <command>` 不再触发 `SyntaxError`。

## 复现步骤

```bash
cd C:/Users/Administrator/Desktop/wiki/
python -m kdo pre-submit -f <任意卡片路径>
```

报错信息：
```text
SyntaxError: expected 'except' or 'finally' block
  File ".../kdo/commands/delivery.py", line 686
```

## 验收标准

- [ ] `python -m kdo --help` 正常输出
- [ ] `python -m kdo pre-submit -f <卡片路径>` 不再报 SyntaxError
- [ ] `python -m kdo lint` 能正常启动（不因此 SyntaxError 退出）
- [ ] 回归测试：跑 `kdo lint --summary` 不因此问题失败

## 备注

- 本任务与 #35 state.json → SQLite MVP、#36 `kdo query --label` 同为基础设施类任务，可并行处理。
- 修复后通知老顽童和各实例，恢复直接使用 `python -m kdo` CLI，不再需要绕过。
