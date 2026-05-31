---
id: dk-p6-session-cache-resume-fail
title: "P-6：cc-connect 修好配置后仍然空响应——session 缓存了失效的 Claude Code session ID"
type: dark-knowledge
dark_knowledge_type: failure
status: draft
domain:
  - master
source_person: system
source_context: "pitfalls.md P-6"
source_refs:
  - .agent/pitfalls.md#P-6
tags:
  - "#source_type/error"
  - "#domain/knowledge-management"
  - "#method/evaluation-method"
created_at: 2026-05-31
updated_at: 2026-05-31
related:
  - dk-p5-cc-connect-config-cascade
  - master-systems-thinking
---

# P-6：cc-connect 修好配置后仍然空响应——session 缓存了失效的 Claude Code session ID

## 原始表述

> **症状**：cc-connect 的 `work_dir` 和 `env.conf` 都已修正（→ wiki vault + DeepSeek），飞书发消息后 bot 返回空。日志显示 `is_resume=true`，紧接着 `exit status 1: No conversation found with session ID: cb687591...`。
>
> **根因**：cc-connect 的 session 文件（`~/.cc-connect/sessions/huangyaoshi_53de3c3f.json`）里存了 `agent_session_id`，指向 Claude Code 在**旧 work_dir**（`/home/dministrator`）下创建的 session。work_dir 已改为 wiki vault 后，Claude Code 的 wiki 项目里不存在这个 session ID，resume 失败，返回空。
>
> **为什么之前的 401 错误也写入了同一个 session**：这个 session 是在 Kimi 配置期间创建的，所有 401 错误都被写入了 session history。修好 API Key 后 session 里仍有 `agent_session_id` 指向不存在的位置，所以 Claude Code 启动即失败。
>
> **对策**：修改 cc-connect 的 `work_dir` 后，**必须同时删除对应的 session 文件**（`~/.cc-connect/sessions/<project>_<hash>.json`），否则旧 session ID 无法 resume。删除后重启 cc-connect，下次消息自动创建全新 session。
>
> **2026-05-17 复现**：P-6 的精确复现。昨晚 21:37 修 P-5 时重启了 cc-connect，旧 Claude Code 进程被杀，但 session 文件保留着死进程的 `agent_session_id`。用户睡觉期间没人发消息，WebSocket 在 00:05 和 02:17 两次超时重连后进入僵尸状态（TCP 连着但应用层不收消息）。早上用户发消息 → cc-connect 尝试 resume 死 session → 静默失败 → 空响应。飞书端 3 小时零条日志。修复：删 session 文件 + 重启 cc-connect。
>
> **复现条件**：cc-connect 重启 + 存在旧 session 文件 + 重启后第一次发消息。复现率 100%。
>
> **设计层根因**：cc-connect 启动时不做 session 有效性检测——不检查 `agent_session_id` 是否指向活着的 Claude Code 进程，也不自动清理。这个 bug 每次重启 cc-connect 都会触发。
>
> **关联**：P-5（同一事故链的第三环：work_dir 错 → env.conf 错 → session 缓存错）。Config Cascade Debug skill 的 Layer 0（运行时缓存）又一次成为最后一层漏网之鱼。

## 使用场景

- 你修改了 cc-connect 的 `work_dir` 后，飞书 bot 返回空响应或无法 resume
- 你重启了 cc-connect 服务，发现第一次消息总是失败
- 你在排查"配置已修复但仍然不工作"的问题
- 你设计带状态持久化的系统时，需要考虑 session 有效性检测和自动清理机制

## 操作方法

1. **修改 work_dir 时清理 session**：每次修改 `work_dir` 后，立即删除 `~/.cc-connect/sessions/<project>_<hash>.json`
2. **重启前 kill 旧进程**：确保旧的 Claude Code 进程已经被杀死，否则新进程和旧进程会冲突
3. **重启后发测试消息**：cc-connect 重启后立即发一条测试消息，确认新 session 能正常创建
4. **监控日志**：用 `journalctl --user -u cc-connect --no-pager -n 50` 检查是否有 `No conversation found with session ID` 错误
5. **建立检查单**：将"删除 session 文件"写入 cc-connect 配置变更的必须步骤

## 适用边界

- 适用于所有使用 cc-connect 且修改了 `work_dir` 或重启了服务的场景
- 不适用于从未修改过 work_dir 的稳定运行环境——在稳定环境中 session 文件不会失效
- 如果使用的不是 cc-connect 而是其他桥接器（如自己写的 WebSocket 代理），同样需要关注 session 持久化和有效性检测的问题
- 删除 session 文件会丢失该会话的历史记录——如果历史记录重要，需要先备份
- 这是一个设计层 bug（cc-connect 不做 session 有效性检测），而非配置错误——即使配置正确，重启也会触发

## 为什么值钱

- 这是运行时缓存（runtime cache）特有的调试难题：**配置已经对了，但缓存里的状态还是旧的**
- P-6 极其迷惑人——用户会花很长时间排查配置，但配置完全没问题，问题在缓存里
- 揭示了状态管理中的一个经典漏洞：**系统不做运行时缓存的有效性检测和自动清理**——这不是用户的错，是设计缺陷
- 任何 AI 训练语料中都不会有"cc-connect 的 session 文件会缓存旧 Claude Code session ID 导致 resume 失败"这条知识

## 与其他知识的关联

- [[dk-p5-cc-connect-config-cascade]] — 同一事故链的第三环。P-5 是"work_dir 错 + env.conf 错"，P-6 是"session 文件缓存了旧 session ID"——三者共同构成了一个完整的 Config Cascade 调试案例
- [[master-systems-thinking]] — 系统思维中的"状态一致性"和"缓存失效"：当系统的运行时状态（session 文件）与配置状态（work_dir）失去一致性时，系统会进入未定义行为
- `.agent/pitfalls.md` → P-6（原始记录）

## 老顽童疑问（2026-05-31）

无疑问，请欧阳锋审查。
