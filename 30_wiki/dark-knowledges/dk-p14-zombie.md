---
id: dk-p14-zombie
title: P-14：僵尸 claude 进程默默烧钱 — Obsidian Claudian + vault backup 死循环
type: dark-knowledge
dark_knowledge_type: failure
status: draft
domain:
- master
source_person: system
source_context: pitfalls.md P-14
source_refs:
- .agent/pitfalls.md#P-14
created_at: 2026-06-03
updated_at: '2026-06-16'
related:
- '[[master-systems-thinking]]'
- '[[master-decision-hygiene]]'
pipeline:
- confidence-draft
- confidence-source-cited
author: legacy
reviewed_by: pending
confidence: 0.7
trust_level: low
---
# P-14：僵尸 claude 进程默默烧钱 — Obsidian Claudian + vault backup 死循环

## 原始表述

> **症状**：PID 17916 `claude` 从 5月19日跑到今天（5天），CPU 仅 502 秒但可能烧了大量 API 费用。另外 PID 15540（hermes）从 5月16日跑了 8 天。80元账单不全是黄药师消耗。
>
> **根因**：
> 1. Obsidian vault backup 插件每隔几分钟自动 `git commit`，文件变更可能触发 Obsidian 内的 Claudian 插件调用
> 2. 用户不知道那个 Obsidian 窗口里的 Claudian 一直在后台活着
> 3. 没有定期检查进程的习惯——僵尸会话默默积累
>
> **对策**：
> - 每次 Claude Code 会话结束**确认终端已关**——不是最小化、不是挂 tmux
> - 定期 `Get-Process claude` 检查是否有意外残留
> - Obsidian Claudian 用完即关——不要让它在后台被 vault backup 反复唤醒
> - **每完成一批任务就检查一次账单**——不要等积累了 80元才发现

## 使用场景

- 你使用 Obsidian + Claudian 插件
- 你的 vault 有自动备份/git commit 机制
- 你发现账单异常但找不到明显的高消耗会话
- 你需要排查后台是否有意外的 Claude Code 进程

## 操作方法

1. **会话结束时确认关闭**：
   - 不是最小化窗口
   - 不是挂 tmux detach
   - 是真正退出进程（`exit` 或关闭终端）

2. **定期检查进程**：
   - PowerShell：`Get-Process claude`
   - WSL：`ps aux | grep claude`
   - 发现意外残留立即 `kill`

3. **管理 Obsidian Claudian**：
   - 用完即关，不要让它在后台运行
   - 如果 vault backup 频繁触发，考虑禁用自动 backup 或调整频率
   - 将 Claudian 设置为手动触发而非自动

4. **账单监控**：
   - 每完成一批任务检查一次账单
   - 设置费用告警阈值
   - 发现异常立即排查进程

5. **不要做的事**：
   - 不要以为最小化 = 关闭
   - 不要让 Obsidian 插件在后台自动调用 API
   - 不要等账单爆炸才发现问题

## 适用边界

- 适用于所有使用 Claude Code CLI 或 Claudian 插件的场景
- 不适用纯 Web 端使用（无本地进程）
- **与 P-13 的区别**：P-13 是"主动使用中的高消耗"，P-14 是"后台僵尸的静默消耗"
- 如果使用 Docker/container，僵尸进程问题会更隐蔽

## 为什么值钱

- 这是"进程生命周期管理"的实战教训：最小化 ≠ 关闭
- 极具隐蔽性：CPU 占用低，用户不会感知到进程存在
- Obsidian + git backup + Claudian 的组合是完美的"意外触发"场景
- **AI 训练语料中不会有这条**：没有任何文档会写"Obsidian 备份插件可能唤醒后台的 Claude Code"

## 与其他知识的关联

- dk-p13-token-burn — P-13 和 P-14 是账单的两大来源
- dk-p6-session-resume-fail — 同样是"旧进程/旧状态未被清理"的问题
- `.agent/pitfalls.md` → P-14（原始记录）

## 老顽童疑问（2026-06-03）

无疑问，请欧阳锋审查。
