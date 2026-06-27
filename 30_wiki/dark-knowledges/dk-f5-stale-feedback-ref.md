---

id: dk-f5-stale-feedback-ref
title: F-KDO-005：过期 feedback 引用残留→kdo lint 报错但文件已不存在
type: dark-knowledge
dark_knowledge_type: failure
status: enriched
domain:
- src_unknown
source_person: system
source_context: failure-modes.md F-KDO-005
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
---# F-KDO-005：过期 feedback 引用残留→kdo lint 报错但文件已不存在

## 原始表述/核心洞察

### 原始表述

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

### 核心洞察

这是 KDO 中"元数据与实体分离存储"导致的经典幽灵引用问题。feedback 文件是实体数据，存在 `60_feedback/` 或 `.kdo/feedback/` 下；而 state.json 中的 `feedback` 列表是元数据索引。两者没有事务性保证，删除文件时若未同步清理索引，系统就会对着不存在的实体报错。更危险的是，这类报错呈现为 ERROR 级别，容易让人误以为是程序 bug，而实则是前期清理操作不完整留下的尾巴。

## 使用场景

- src_unknown
- src_unknown
- src_unknown
- src_unknown

## 操作方法

1. **定位 stale 引用**：运行 `kdo lint`，记录报错中的 feedback ID（如 `fb_xxx`）
2. **确认文件已删除**：`ls 60_feedback/` 或 `ls .kdo/feedback/` 确认该文件确实不存在
3. **手动清理 state.json**：打开 `.kdo/state.json`，从 `feedback` 列表中移除该 ID 对应的对象
4. **验证修复**：再次运行 `kdo lint`，确认 "Feedback path does not exist" 错误消失
5. **建立同步习惯**：以后删除 feedback 文件时，**同步**从 state.json 的 `feedback` 列表中移除对应条目

## 适用边界

- src_unknown
- src_unknown
- src_unknown
- src_unknown
- src_unknown

## 常见失败模式

| 失败模式 | 触发条件 | 表面症状 | 修复方法 |
|---|---|---|---|
| 手动删文件未清 state | 删除 `60_feedback/` 中的 `.md` 文件但未同步编辑 state.json | `kdo lint` 报 "Feedback path does not exist" | 从 state.json 的 `feedback` 列表移除对应 ID |
| Obsidian/工具自动清理 | 第三方工具或插件自动删除孤立文件 | lint 忽然出现大量 stale feedback 错误 | 批量运行清理脚本或手动过滤 feedback 列表 |
| 路径变更当作删除 | feedback 文件被移动或重命名 | lint 报原路径不存在 | 更新 state.json 中的路径为新路径，而非删除引用 |
| 并发删除竞态 | 脚本批量删除文件与更新 state.json 不同步 | 部分引用残留或 state.json 损坏 | 先备份 state.json，批量更新后再删除文件 |

## 为什么值钱

- src_unknown
- src_unknown
- src_unknown
- src_unknown

## 与其他知识的关联

- src_unknown
- src_unknown-systems-thinking — 系统思维中的"状态一致性"原则：当元数据（state.json）与实体数据（文件系统）分离存储时，任何清理操作都必须同步更新两边，否则会产生不一致
- src_unknown
- src_unknown
- src_unknown

## 老顽童疑问（2026-05-31）

无疑问，请欧阳锋审查。
