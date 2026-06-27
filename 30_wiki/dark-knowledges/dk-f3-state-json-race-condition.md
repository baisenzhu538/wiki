---
id: dk-f3-state-json-race-condition
title: F-KDO-003：state.json 覆盖写竞态→improve 执行后 revision 记录丢失
type: dk
dark_knowledge_type: failure
status: enriched
domain:
- src_unknown
source_person: system
source_context: failure-modes.md F-KDO-003
source_refs:
- src_unknown
created_at: 2026-05-31
updated_at: '2026-06-19'
related:
- src_unknown
- src_unknown
- src_unknown
- src_unknown
- src_unknown
- src_unknown
- src_unknown
pipeline:
- src_unknown
- src_unknown
author: unknown
reviewed_by: 欧阳锋
confidence: 0.88
trust_level: medium
diagnostic_signals:
- src_unknown
- src_unknown
- src_unknown
---# F-KDO-003：state.json 覆盖写竞态→improve 执行后 revision 记录丢失

## 原始表述

> **触发命令**：`kdo improve --apply`
>
> **表现**：improve 执行后 wiki_snapshots 为空，revision 记录丢失。无报错。
>
> **根因**：`snapshot_wiki_page()` 内部独立调用 `load_state()` + `save_state()`，但调用方 `cmd_improve()` 之后也用自己持有的旧 state dict 写回磁盘，覆盖了 snapshot 的写入
>
> **触发信号**：`kdo improve --apply` 成功但 `.kdo/state.json` 中 `wiki_snapshots` 为空
>
> **防御措施**：① 代码修复：`snapshot_wiki_page()` 接受调用方的 state dict 参数，不独立读写 ② 所有写 state.json 的函数统一走一个 save 入口
>
> **状态**：代码已修复（2026-05-01），但问题模式未记录入库
>
> **关联文件**：`kdo/commands/feedback.py`, `kdo/workspace.py`

## 使用场景

- src_unknown
- src_unknown
- src_unknown
- src_unknown

## 操作方法

1. **检查并发进程**：执行 improve 前，先 `ps aux | grep kdo` 确认没有其他 kdo 进程正在写 state.json
2. **备份 state.json**：在执行 improve 前，先 `cp .kdo/state.json .kdo/state.json.bak`，防止数据丢失
3. **执行 improve**：`kdo improve --apply`
4. **验证 wiki_snapshots**：执行完后立即检查 `.kdo/state.json`，确认 `wiki_snapshots` 字段非空且包含正确的 revision 记录
5. **代码层修复（开发者）**：所有写 state.json 的函数必须统一走一个 save 入口，禁止多个函数各自独立读写 state.json

## 适用边界

- src_unknown
- src_unknown
- src_unknown
- src_unknown
- src_unknown

## 常见失败模式

| 失败模式 | 触发条件 | 表面症状 | 后果 |
|---|---|---|---|
| 并发覆盖写 | `snapshot_wiki_page()` 与 `cmd_improve()` 各自独立保存 state | improve 成功但 wiki_snapshots 为空 | revision 历史丢失，无法回滚 |
| 旧 state dict 写回 | 调用方持有旧 state，子函数写入后被覆盖 | state 字段值回退到执行前 | 反馈状态、快照数据不一致 |
| 多进程同时写 state | 自动化管线中多个 kdo 实例并行 | 无报错但 state.json 损坏或丢失 | 系统状态不可恢复 |

## 为什么值钱

- src_unknown
- src_unknown
- src_unknown
- src_unknown

## 与其他知识的关联

- src_unknown
- src_unknown-systems-thinking — 系统思维中的"涌现性"原则：单个组件各自工作时没问题，但组件间交互时产生意想不到的故障。F-KDO-003 是这一原则在 state 管理中的具体体现
- src_unknown
- src_unknown

## 老顽童疑问（2026-05-31）

无疑问，请欧阳锋审查。
