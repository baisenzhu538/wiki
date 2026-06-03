---
id: dk-p2-tmux-cache
title: "P-2：tmux session 缓存旧配置"
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
  - "#domain/system-operations"
  - "#method/debugging"
created_at: 2026-06-03
updated_at: 2026-06-03
related:
  - dk-p1-model-switch-env
  - dk-p5-cc-connect-config-cascade
  - dk-p6-session-resume-fail
contradicts:
---

# P-2：tmux session 缓存旧配置

## 原始表述

> **症状**：改了 `.bashrc` 后 `claude` 行为没变。
>
> **根因**：`claude()` 函数包装了 tmux session `claude`，只要 session 活着，用的是 session 创建时的环境，不是最新 `.bashrc`。
>
> **对策**：改完配置后 `tmux kill-session -t claude`，再重新 `claude`。

## 使用场景

- 你刚在 `.bashrc` 里改了环境变量/别名/函数定义，但终端行为完全没变
- 你重连 tmux 后以为会加载最新 `.bashrc`，但实际上还是旧 session
- 你发现"同样的命令，新终端正常，tmux 里不正常"
- 你在排查"配置改了却不生效"，已经排除了文件权限和语法错误

## 操作方法

1. **确认症状**：新开一个普通终端（非 tmux），运行同样命令 → 如果新终端正常，tmux 异常 → 99% 是 tmux session 缓存
2. **查看活着的 session**：`tmux ls`，确认目标 session 存在且状态为 `(attached)` 或 `(detached)`
3. **杀掉旧 session**：`tmux kill-session -t <session_name>`（示例中为 `claude`）
4. **重新启动**：运行包装命令（如 `claude`），让脚本自动创建新 session
5. **验证**：检查环境变量是否已更新（`echo $VAR_NAME`）
6. **如果还有残留**：`tmux kill-server` 杀掉所有 session（注意：会丢失所有未保存的工作）

## 适用边界

- 仅适用于被 tmux 包装的命令——如果命令不走 tmux，此模式不适用
- 不适用于 screen、zellij 等其他终端复用器（但原理相同：session 创建时的环境快照不会自动更新）
- **与 P-1 的区分**：P-1 是"静态配置优先级问题"（改了低优先级层），P-2 是"动态运行时缓存问题"（改了文件但进程没重载）
- 如果 `.bashrc` 本身有语法错误，tmux 新 session 也会加载失败——先跑 `bash -n ~/.bashrc` 确认语法无误

## 为什么值钱

- 最隐蔽的"改了不生效"类型之一：文件确实改了、语法也对、路径也正确——但运行时环境是旧快照
- 新手容易在".bashrc → source → 为什么没变"的循环里浪费 30 分钟，本质原因是没意识到 tmux session 是持久进程
- 任何文档都不会写"改完 .bashrc 记得 kill tmux session"——这是运行时的隐性知识

## 与其他知识的关联

- [[dk-p1-model-switch-env]] — 同样是"改了配置不生效"：P-1 是静态配置层优先级问题，P-2 是动态 session 缓存问题。两者常被同时遇到，debug 时应先确认是哪一类
- [[dk-p5-cc-connect-config-cascade]] — P-5 的 systemd drop-in 也涉及服务重启后才能生效，与 tmux session 缓存同属"运行时环境不随配置文件自动更新"的大家族
- [[dk-p6-session-resume-fail]] — P-6 的 cc-connect session 缓存失效是另一种 session 问题：不是环境缓存，而是 session ID 指向了不存在的进程。两者都说明"session 机制需要显式管理"
- `.agent/pitfalls.md` → P-2（原始记录）
