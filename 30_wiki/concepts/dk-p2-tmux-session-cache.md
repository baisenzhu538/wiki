---
id: dk-p2-tmux-session-cache
title: "P-2：tmux session 缓存旧配置——改了 .bashrc 但行为不变"
type: dark-knowledge
dark_knowledge_type: failure
status: draft
domain:
  - master
source_person: system
source_context: "pitfalls.md P-2"
source_refs:
  - .agent/pitfalls.md#P-2
tags:
  - "#source_type/error"
  - "#domain/knowledge-management"
  - "#method/evaluation-method"
created_at: 2026-05-31
updated_at: 2026-05-31
related:
  - dk-p1-model-switch-env-var
  - master-decision-hygiene
---

# P-2：tmux session 缓存旧配置——改了 .bashrc 但行为不变

## 原始表述

> **症状**：改了 `.bashrc` 后 `claude` 行为没变。
>
> **根因**：`claude()` 函数包装了 tmux session `claude`，只要 session 活着，用的是 session 创建时的环境，不是最新 `.bashrc`。
>
> **对策**：改完配置后 `tmux kill-session -t claude`，再重新 `claude`。

## 使用场景

- 你修改了 `.bashrc`、`.profile` 或环境变量，但运行 `claude` 后发现旧配置仍然生效
- 你在 tmux 会话中运行长命命令，需要确认环境变量是否为最新值
- 你调试一个"配置已修改但程序行为不变"的问题
- 你在写自动化脚本时，需要了解 tmux session 的环境隔离机制

## 操作方法

1. **改完配置后 kill session**：每次修改 `.bashrc` 或相关配置后，先执行 `tmux kill-session -t claude`
2. **确认 session 已死**：用 `tmux ls` 确认 `claude` session 不在列表中
3. **重新启动**：运行 `claude`（或对应的包装函数），此时新 session 会加载最新的 `.bashrc`
4. **验证变更**：运行 `echo $VAR_NAME` 或测试目标功能，确认配置已生效
5. **建立习惯**：将 `tmux kill-session -t claude` 写入配置变更的后置 check 清单

## 适用边界

- 适用于所有用 tmux 包装长命命令的场景（不仅限于 `claude`）
- 不适用于普通前台进程（不走 tmux）——这些进程每次重启都会加载新配置
- 如果在 tmux session 内运行了多个窗口/面板，kill-session 会清理所有内容——如果有未保存的工作，先保存
- 除了 tmux，screen、byobu 等其他终端复用器也有相同的环境缓存行为
- 在 Docker 容器内，容器启动时的环境变量也不会随 `.bashrc` 修改而更新，需要重新启动容器

## 为什么值钱

- 这是终端多路复用器（tmux/screen）特有的行为：session 是环境的快照，不是实时映射
- **"改了配置但无效"是开发者最常见的困惑之一**：大多数人不会第一时间想到是 tmux session 的缓存
- 暴露了一个常被忽视的级别：终端复用器的环境隔离机制和普通 shell 是不同的概念
- 任何 AI 训练语料中都不会有"tmux session 会缓存创建时的环境变量"这条知识

## 与其他知识的关联

- [[dk-p1-model-switch-env-var]] — 同一模式："配置修改后验证失败"。P-1 是"改了环境变量但全局设置覆盖"，P-2 是"改了 .bashrc 但 tmux session 缓存"——两者都是"配置已变更但实际行为未变"
- [[master-decision-hygiene]] — 决策卫生 Step 2：每次配置修改后，必须有明确的验证步骤来确认变更生效（此处是"kill session 后重启验证"）
- `.agent/pitfalls.md` → P-2（原始记录）

## 老顽童疑问（2026-05-31）

无疑问，请欧阳锋审查。
