---
id: dk-p6-session-resume-fail
title: P-6：cc-connect 修好 work_dir + API Key 后仍然空响应 — session 缓存了失效的 Claude Code session
  ID
type: dk
dark_knowledge_type: failure
status: enriched
domain:
- master
source_person: system
source_context: pitfalls.md P-6
source_refs:
- src_unknown
created_at: 2026-06-03
updated_at: '2026-06-19'
related:
- '[[framework-strategy-pyramid]]'
- '[[framework-yitang-channel-exploration-4step]]'
- '[[framework-lean-four-principles]]'
- '[[framework-lean-pivot-decision]]'
- '[[framework-doris-industry-report-4step]]'
- '[[framework-kdo-self-attack]]'
- '[[dk-modeling-timely-review-session-window]]'
- '[[framework-yitang-deliberate-practice-1plus4]]'
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
- src_unknown# P-6：cc-connect 修好 work_dir + API Key 后仍然空响应 — session 缓存了失效的 Claude
  Code session ID
---

## 原始表述/核心洞察

> **症状**：cc-connect 的 `work_dir` 和 `env.conf` 都已修正（→ wiki vault + DeepSeek），飞书发消息后 bot 返回空。日志显示 `is_resume=true`，紧接着 `exit status 1: No conversation found with session ID: cb687591...`。
>
> **根因**：cc-connect 的 session 文件（`~/.cc-connect/sessions/huangyaoshi_53de3c3f.json`）里存了 `agent_session_id`，指向 Claude Code 在**旧 work_dir**（`/home/dministrator`）下创建的 session。work_dir 已改为 wiki vault 后，Claude Code 的 wiki 项目里不存在这个 session ID，resume 失败，返回空。
>
> **对策**：修改 cc-connect 的 `work_dir` 后，必须同时删除对应的 session 文件（`~/.cc-connect/sessions/<project>_<hash>.json`），否则旧 session ID 无法 resume。删除后重启 cc-connect，下次消息自动创建全新 session。
>
> **复现**（2026-05-17）：修 P-5 时重启了 cc-connect，旧 Claude Code 进程被杀，但 session 文件保留着死进程的 `agent_session_id`。用户睡觉期间没人发消息，WebSocket 进入僵尸状态。早上用户发消息 → cc-connect 尝试 resume 死 session → 静默失败 → 空响应。飞书端 3 小时零条日志。
>
> **复现条件**：cc-connect 重启 + 存在旧 session 文件 + 重启后第一次发消息。复现率 100%。
>
> **设计层根因**：cc-connect 启动时不做 session 有效性检测——不检查 `agent_session_id` 是否指向活着的 Claude Code 进程，也不自动清理。这个 bug 每次重启 cc-connect 都会触发。

## 使用场景

- src_unknown
- src_unknown
- src_unknown
- src_unknown

## 操作方法

1. **识别 session 缓存问题**：
   - src_unknown
   - src_unknown

2. **删除旧 session 文件**：
   - src_unknown
   - src_unknown

3. **重启服务**：
   - src_unknown
   - src_unknown

4. **验证修复**：
   - src_unknown
   - src_unknown
   - src_unknown

5. **预防措施**：
   - src_unknown
   - src_unknown
   - src_unknown

## 适用边界

- src_unknown
- src_unknown
- src_unknown
- src_unknown
- src_unknown

## 常见失败模式

| 失败模式 | 典型症状 | 根因 | 解法/预防措施 |
|
|---|---|---|
| 旧 session ID 指向已销毁的 Claude Code 进程 | `is_resume=true` 后 `No conversation found with session ID` | 服务重启杀掉了旧进程，但 session 文件仍保留旧 `agent_session_id` | 重启 cc-connect 前删除 `~/.cc-connect/sessions/<project>_<hash>.json` |
| work_dir 修改后 resume 旧项目 session | 配置已修正，bot 仍返回空响应 | 旧 session 是在错误 work_dir 下创建的，新 work_dir 下无此 session | 改 work_dir 时同步清空 sessions 目录 |
| 首次发消息触发静默失败 | 重启后长时间无日志，随后空响应 | WebSocket 处于僵尸状态，直到有新消息才尝试 resume 死 session | 重启后立即发测试消息验证；把 session 清理写进启动脚本 |
| 依赖自动恢复但未校验 session 有效性 | 每次重启都复现空响应 | cc-connect 启动时不检查 `agent_session_id` 是否有效 | 在启动脚本中加入 session 有效性探测，无效则自动清理 |

## 为什么值钱

- src_unknown
- src_unknown
- src_unknown
- src_unknown

## 与其他知识的关联

- src_unknown
- src_unknown
- src_unknown
- src_unknown
