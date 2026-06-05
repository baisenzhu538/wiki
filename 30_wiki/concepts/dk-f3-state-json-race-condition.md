---
id: dk-f3-state-json-race-condition
title: "F-KDO-003：state.json 覆盖写竞态→improve 执行后 revision 记录丢失"
type: dark-knowledge
dark_knowledge_type: failure
status: draft
domain:
  - master
source_person: system
source_context: "failure-modes.md F-KDO-003"
source_refs:
  - 90_control/failure-modes.md#F-KDO-003
tags:
  - "#source_type/error"
  - "#domain/knowledge-management"
  - "#method/evaluation-method"
created_at: 2026-05-31
updated_at: 2026-05-31
related:
  - dk-c10-batch-tool-no-dry-run
  - master-systems-thinking
contradicts:
  - [[dk-c10-batch-tool-no-dry-run]]
  - [[master-systems-thinking]]
---

# F-KDO-003：state.json 覆盖写竞态→improve 执行后 revision 记录丢失

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

- 你准备运行 `kdo improve --apply` 将反馈应用到 wiki 页面
- 你发现 improve 执行后 `state.json` 中的 `wiki_snapshots` 为空，需要判断是数据本就为空还是被覆盖了
- 你在编写新的 KDO 命令时，需要设计 state 的读写机制，避免多个函数同时写磁盘
- 你在调试 `kdo improve` 相关 bug 时，需要理解 state.json 的写入流程

## 操作方法

1. **检查并发进程**：执行 improve 前，先 `ps aux | grep kdo` 确认没有其他 kdo 进程正在写 state.json
2. **备份 state.json**：在执行 improve 前，先 `cp .kdo/state.json .kdo/state.json.bak`，防止数据丢失
3. **执行 improve**：`kdo improve --apply`
4. **验证 wiki_snapshots**：执行完后立即检查 `.kdo/state.json`，确认 `wiki_snapshots` 字段非空且包含正确的 revision 记录
5. **代码层修复（开发者）**：所有写 state.json 的函数必须统一走一个 save 入口，禁止多个函数各自独立读写 state.json

## 适用边界

- 适用于所有会写入 `state.json` 的 KDO 命令，尤其是 `kdo improve --apply`
- 不适用于只读操作（如 `kdo lint`、`kdo validate`、`kdo query`），这些操作不会触发竞态
- **代码已修复（2026-05-01）**，但模式未入库——修了 bug 不等于消除了失败模式，同样的竞态逻辑可能存在于其他命令中
- 如果你在自定义扩展 kdo 时写了新的 state 写入逻辑，必须遵循"单一 save 入口"原则
- 在多用户/多进程环境下，即使单一函数内部也需要加文件锁（file lock），而不仅仅是"统一入口"

## 为什么值钱

- 这是 KDO 特有的 state 管理机制：所有操作状态都存储在单一的 `state.json` 中，多个函数同时写入就会产生竞态
- 在单用户交互式环境下难以触发，但在**自动化管线或快速连续执行命令**时，这个竞态会被放大——和 C-10 的"批量操作风险"是同一模式
- 揭示了软件设计中的经典陷阱：**"每个函数自己管自己的 IO"→数据丢失**。通用软件工程不会告诉你"KDO 的 state.json 为什么需要统一 save 入口"
- 任何 AI 训练语料中都不会有"KDO 的 snapshot_wiki_page 会被 cmd_improve 的旧 state dict 覆盖"这条知识——这是具体工具实现层面的暗知证

## 与其他知识的关联

- [[dk-c10-batch-tool-no-dry-run]] — 同一深层模式：自动化/批量操作中的隐蔽风险。C-10 是"批量写入导致内容被覆盖"，F-KDO-003 是"多个写入点导致 state 记录丢失"——两者都是"自动化操作中的写入风险"
- [[master-systems-thinking]] — 系统思维中的"涌现性"原则：单个组件各自工作时没问题，但组件间交互时产生意想不到的故障。F-KDO-003 是这一原则在 state 管理中的具体体现
- `90_control/failure-modes.md` → F-KDO-003（原始记录）
- `90_control/AGENTS.md` → 禁止清单 #5（不准在 state.json 被其他进程持有时执行写操作）

## 老顽童疑问（2026-05-31）

无疑问，请欧阳锋审查。
