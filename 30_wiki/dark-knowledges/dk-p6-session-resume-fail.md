---

id: dk-p6-session-resume-fail
title: P-6：cc-connect 修好 work_dir + API Key 后仍然空响应 — session 缓存了失效的 Claude Code session ID
type: dark-knowledge
dark_knowledge_type: failure
status: enriched
domain:
- master
source_person: system
source_context: pitfalls.md P-6
source_refs:
- 10_raw/sources/src_20260619_1545a6ee_.agent_pitfalls.md#P-6
created_at: 2026-06-03
updated_at: '2026-06-19'
related:
  - '[[dk-p2-tmux-cache]]'
  - '[[dk-p1-model-switch-env]]'
  - '[[dk-c6-large-source-overflow]]'
  - '[[dk-state-residue-is-the-silent-killer]]'
  - '[[dk-p5-cc-connect-config]]'
- '[[master-systems-thinking]]'
- '[[master-first-principles]]'
- '[[dk-p5-cc-connect-config]]'
- '[[dk-p2-tmux-cache]]'
pipeline:
- confidence-draft
- confidence-source-cited
author: unknown
reviewed_by: 欧阳锋
confidence: 0.88
trust_level: medium
diagnostic_signals:
- 日志出现 is_resume=true 后紧跟 No conversation found with session ID
- 配置已修正（work_dir/API Key）但 bot 仍返回空响应
- 服务重启后首次发消息即复现
---# P-6：cc-connect 修好 work_dir + API Key 后仍然空响应 — session 缓存了失效的 Claude Code session ID

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

- 你修改了 cc-connect 的 `work_dir` 后发现飞书 bot 空响应
- 你重启了一个长期运行的 Agent wrapper 服务
- 你的应用有"resume session"机制，但 session 可能已经过期或无效
- 你排查"为什么配置修好了但程序还是不工作"——可能是旧运行时状态在作祖

## 操作方法

1. **识别 session 缓存问题**：
   - 检查日志里是否有 `is_resume=true` 后跟着 session 相关错误
   - 检查 `~/.cc-connect/sessions/` 目录下的 session 文件时间戳（是否比服务重启时间更早）

2. **删除旧 session 文件**：
   - `rm ~/.cc-connect/sessions/<project>_<hash>.json`
   - 如果不确定哪个是旧的，安全做法是清空整个 sessions 目录

3. **重启服务**：
   - `systemctl --user restart cc-connect`
   - 下次消息会自动创建新 session

4. **验证修复**：
   - 发一条测试消息
   - 确认日志里没有 `No conversation found with session ID`
   - 确认 bot 有正常响应

5. **预防措施**：
   - 将"删 session 文件"加入 cc-connect 重启 SOP
   - 考虑在 cc-connect 启动脚本中自动检查 session 有效性，无效时自动删除
   - 记录每次服务重启的原因和时间，便于追踪

## 适用边界

- 适用于所有使用 session 恢复机制的应用（不限于 cc-connect）
- 不适用于无状态的一次性进程（如 cron job、批量脚本）——那些没有 session 缓存
- **与 P-2 的区别**：P-2 是 tmux session 的环境变量缓存，P-6 是 Claude Code session ID 的应用层缓存。两者是同一模式在不同层的复现
- **与 P-5 的关系**：P-5 是事故链的第一环（配置错），P-6 是第三环（session 缓存）。中间的第二环是 API Key 修复
- 如果应用在启动时自动检测并清理无效 session，P-6 不触发——但这需要额外的工程实现

## 常见失败模式

| 失败模式 | 典型症状 | 根因 | 解法/预防措施 |
|---|---|---|---|
| 旧 session ID 指向已销毁的 Claude Code 进程 | `is_resume=true` 后 `No conversation found with session ID` | 服务重启杀掉了旧进程，但 session 文件仍保留旧 `agent_session_id` | 重启 cc-connect 前删除 `~/.cc-connect/sessions/<project>_<hash>.json` |
| work_dir 修改后 resume 旧项目 session | 配置已修正，bot 仍返回空响应 | 旧 session 是在错误 work_dir 下创建的，新 work_dir 下无此 session | 改 work_dir 时同步清空 sessions 目录 |
| 首次发消息触发静默失败 | 重启后长时间无日志，随后空响应 | WebSocket 处于僵尸状态，直到有新消息才尝试 resume 死 session | 重启后立即发测试消息验证；把 session 清理写进启动脚本 |
| 依赖自动恢复但未校验 session 有效性 | 每次重启都复现空响应 | cc-connect 启动时不检查 `agent_session_id` 是否有效 | 在启动脚本中加入 session 有效性探测，无效则自动清理 |

## 为什么值钱

- 这是**运行时缓存 vs 新配置**的实战教训：修复配置不等于修复状态。旧状态可能以多种形式隐藏（session 文件、缓存、旧进程的内存等）
- 极其幽默：配置修完了，重启了服务，但旧 session 文件保留着死进程的状态。新进程试图 resume 一个已经消亡的身份
- 揭示了"Layer 0 缓存"的威力：配置层（Layer 3）和运行时缓存（Layer 0）是独立的。改了 Layer 3 不等于 Layer 0 也被更新
- **AI 训练语料中不会有这条**：没有任何文档会写"修改 work_dir 后要删掉 session 文件——否则旧 session ID 会导致空响应"

## 与其他知识的关联

- [[dk-p5-cc-connect-config]] — P-6 是 P-5 的事故链延伸：工作目录错 → env.conf 错 → API Key 修复 → work_dir 修正 → session 缓存 → 空响应。完整的五环事故链
- [[dk-p2-tmux-cache]] — 同一模式在不同工具上的复现：tmux session 缓存环境 vs cc-connect session 缓存 Claude Code 身份
- [[dk-p1-model-switch-env]] — 事故链的起点：切换模型配置
- `.agent/pitfalls.md` → P-6（原始记录）
