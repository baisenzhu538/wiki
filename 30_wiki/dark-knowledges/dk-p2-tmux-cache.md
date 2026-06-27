---

id: dk-p2-tmux-cache
title: P-2：tmux session 缓存旧配置
type: dk
dark_knowledge_type: failure
status: enriched
domain:
- src_unknown
source_person: system
source_context: pitfalls.md P-2
source_refs:
- src_unknown
created_at: 2026-06-03
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
  - src_unknown
pipeline:
- src_unknown
- src_unknown
author: system
reviewed_by: 欧阳锋
confidence: 0.88
trust_level: medium
diagnostic_signals:
- src_unknown
- src_unknown
---# P-2：tmux session 缓存旧配置

## 原始表述 / 核心洞察

> **症状**：改了 `.bashrc` 后 `claude` 行为没变。
>
> **根因**：`claude()` 函数包装了 tmux session `claude`，只要 session 活着，用的是 session 创建时的环境，不是最新 `.bashrc`。
>
> **对策**：改完配置后 `tmux kill-session -t claude`，再重新 `claude`。

**核心洞察**：tmux/screen 等终端复用器在创建 session 时会快照当前 shell 环境；session 存活期间，子进程继承的是这份快照，而非文件系统上最新的配置文件。修改 `.bashrc`、环境变量或 API Key 后，必须 kill session 重建，否则新配置不会生效。

## 使用场景

- src_unknown
- src_unknown
- src_unknown
- src_unknown

## 操作方法

1. **识别 tmux 缓存**：
   - src_unknown
   - src_unknown

2. **正确刷新流程**：
   - src_unknown
   - src_unknown

3. **验证配置已生效**：
   - src_unknown
   - src_unknown

4. **预防措施**：
   - src_unknown
   - src_unknown
   - src_unknown

## 适用边界

- src_unknown
- src_unknown
- src_unknown
- src_unknown

## 常见失败模式

| 失败模式 | 典型表现 | 根因 | 纠正动作 |
|---|---|---|---|
| 改完 `.bashrc` 直接 `source ~/.bashrc` | 当前终端变量变了，但 tmux 里的程序仍用旧值 | `source` 只刷新当前 shell，不更新 tmux session 的环境快照 | `tmux kill-session -t <name>` 后重开 |
| 只重启目标程序，不 kill tmux session | 程序行为如故，环境变量仍旧 | 程序仍跑在旧 session 中，继承旧环境 | 先 kill session，再启动程序 |
| 找不到正确的 session 名 | `tmux kill-session -t claude` 报错 "session not found" | session 名与预期不一致，或用了不同用户/终端 | `tmux ls` 确认 session 名；必要时用 `tmux kill-server`（谨慎） |
| 误杀其他重要 session | 其他工作区中断 | 使用了通配符或 kill-server | 精确指定 `-t <session-name>` |

## 为什么值钱

- src_unknown
- src_unknown
- src_unknown

## 与其他知识的关联

- src_unknown
- src_unknown
- src_unknown
- src_unknown
