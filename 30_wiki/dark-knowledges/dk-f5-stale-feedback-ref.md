---
id: dk-f5-stale-feedback-ref
title: F-KDO-005：过期 feedback 引用残留→kdo lint 报错但文件已不存在
type: dark-knowledge
dark_knowledge_type: failure
status: draft
domain:
- master
source_person: system
source_context: failure-modes.md F-KDO-005
source_refs:
- 90_control/failure-modes.md#F-KDO-005
created_at: 2026-05-31
updated_at: '2026-06-16'
related:
- '[[dk-c4-selfcheck-superseded]]'
- '[[master-systems-thinking]]'
pipeline:
- confidence-draft
- confidence-source-cited
author: unknown
reviewed_by: pending
confidence: 0.7
trust_level: low
---
# F-KDO-005：过期 feedback 引用残留→kdo lint 报错但文件已不存在

## 原始表述

> **触发命令**：`kdo lint`
>
> **表现**：`ERROR: Feedback 'fb_xxx' path does not exist` —— lint 报告一个磁盘上已不存在的文件
>
> **根因**：feedback 的 .md 文件被删除（如 Obsidian 清理），但 state.json 的 `feedback` 列表中仍保留该文件路径
>
> **触发信号**：`kdo lint` 输出 "Feedback path does not exist"
>
> **防御措施**：① `kdo lint` 自动检测并清理 stale feedback 引用（当前只报错不修复）② 定期运行 `kdo self-check` ③ 删除 feedback 文件时同时从 state.json 移除
>
> **清理方法**：`python3 -c "import json; state=json.load(open('.kdo/state.json')); state['feedback']=[f for f in state['feedback'] if 'DEAD_ID' not in str(f)]; json.dump(state, open('.kdo/state.json','w'), indent=2)"`
>
> **关联文件**：`.kdo/state.json` → `feedback` 列表

## 使用场景

- 你运行 `kdo lint` 时看到 "Feedback path does not exist" 错误，需要定位和清理残留引用
- 你手动删除了 `60_feedback/` 目录下的 feedback 文件，但忘记同步更新 state.json
- 你使用 Obsidian 或其他工具清理 vault 中的废弃文件，担心是否破坏了 kdo 的内部状态
- 你写自动化清理脚本时，需要确保"删文件"和"删 state 引用"是原子操作

## 操作方法

1. **定位 stale 引用**：运行 `kdo lint`，记录报错中的 feedback ID（如 `fb_xxx`）
2. **确认文件已删除**：`ls 60_feedback/` 或 `ls .kdo/feedback/` 确认该文件确实不存在
3. **手动清理 state.json**：打开 `.kdo/state.json`，从 `feedback` 列表中移除该 ID 对应的对象
4. **验证修复**：再次运行 `kdo lint`，确认 "Feedback path does not exist" 错误消失
5. **建立同步习惯**：以后删除 feedback 文件时，**同步**从 state.json 的 `feedback` 列表中移除对应条目

## 适用边界

- 适用于所有手动删除 feedback 文件的场景
- 不适用于 feedback 文件仍然存在但路径变更的情况——此时应更新路径而非删除引用
- 如果 feedback 文件是被外部工具（如 Obsidian 的 auto-cleanup）自动删除的，你可能无法提前同步——需要依赖 `kdo lint` 的事后检测
- `kdo lint` 当前**只报错不自动修复**，所以必须人工介入清理
- 批量删除 feedback 文件时，建议先用脚本批量更新 state.json，再执行文件删除

## 为什么值钱

- 这是 KDO 特有的状态管理问题：feedback 的元数据存储在 state.json 中，而文件本身存储在文件系统中——两者是分离的
- **"文件已删但引用残留"是分布式状态的经典问题**：state.json 和文件系统之间没有事务性保证，删除操作不是原子的
- 症状极具迷惑性：`kdo lint` 报告的是 ERROR 级别，但问题根因不是"代码错了"而是"清理操作不完整"
- 任何 AI 训练语料中都不会有"KDO 的 state.json feedback 列表需要与 60_feedback/ 目录保持同步"这条知识

## 与其他知识的关联

- dk-c4-selfcheck-superseded — 同一模式：自检工具报告的状态与实际情况不一致。C-4 是"self-check 误报 superseded 为未 enrich"，F-KDO-005 是"lint 报错已删除的 feedback"——两者都是"内部状态与实际文件系统不同步"
- master-systems-thinking — 系统思维中的"状态一致性"原则：当元数据（state.json）与实体数据（文件系统）分离存储时，任何清理操作都必须同步更新两边，否则会产生不一致
- `90_control/failure-modes.md` → F-KDO-005（原始记录）
- `90_control/AGENTS.md` → 禁止清单 #4（不准删除 feedback 文件不同步清理 state.json）

## 老顽童疑问（2026-05-31）

无疑问，请欧阳锋审查。
