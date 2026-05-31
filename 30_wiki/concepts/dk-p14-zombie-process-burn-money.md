---
id: dk-p14-zombie-process-burn-money
title: "P-14：僵尸 claude 进程默默烧钱 — Obsidian Claudian + vault backup 死循环"
type: dark-knowledge
dark_knowledge_type: failure
status: draft
domain:
  - master
source_person: system
source_context: "pitfalls.md P-14"
source_refs:
  - .agent/pitfalls.md#P-14
tags:
  - "#source_type/error"
  - "#domain/knowledge-management"
  - "#method/evaluation-method"
created_at: 2026-05-31
updated_at: 2026-05-31
related:
  - dk-p13-long-session-token-blackhole
  - master-systems-thinking
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

- 你完成一个 Claude Code 会话后，需要确认进程真的已经终止
- 你发现 API 账单异常高昂，需要排查是否有僵尸进程在后台运行
- 你使用 Obsidian + Claudian 插件，需要了解 vault backup 可能触发的副作用
- 你在管理多个 AI 工具时，需要建立进程检查的习惯

## 操作方法

1. **会话结束时关终端**：每次 Claude Code 会话结束后，确认终端窗口已关闭，不是最小化或挂在 tmux 里
2. **定期检查进程**：每天至少一次运行 `Get-Process claude` （PowerShell）或 `ps aux | grep claude` （WSL），查看是否有意外残留
3. **关闭 Claudian**：如果使用 Obsidian Claudian 插件，用完后明确关闭，而不是让它继续运行
4. **定期检查账单**：每周（或每天）检查 API 提供商的账单，如果发现异常增长，立即排查
5. **设置预算告警**：如果可能，在 API 提供商处设置消费上限或预算告警

## 适用边界

- 适用于所有使用按 token 计费的 LLM API 的场景
- 不适用于本地部署的模型（如 llama.cpp）——这些不涉及 API 费用
- Obsidian Claudian 只是一个具体案例，任何后台运行的 AI 工具都可能有相同问题
- 即使没有使用 Claudian，普通的 Claude Code 会话也可能因为意外而留下僵尸进程
- 进程检查应该是日常习惯而非"出了事才查"——僵尸进程的成本是积累的

## 为什么值钱

- 这是 AI 工具使用中最隐蔽的成本泄漏：**僵尸进程不会产生任何可见的错误，只会默默消耗 API 费用**
- "80元账单不全是黄药师消耗"是关键发现：排查时只看主要使用者，忽视了后台的僵尸进程
- 揭示了资源管理中的一个核心原理：**任何持续运行的进程都必须有明确的存在理由和结束条件**
- 任何 AI 训练语料中都不会有"Obsidian Claudian 会被 vault backup 反复唤醒并消耗 API 费用"这条知识

## 与其他知识的关联

- [[dk-p13-long-session-token-blackhole]] — 同一模式："资源泄漏导致财务损失"。P-13 是"长会话导致 token 爆炸"，P-14 是"僵尸进程导致 API 费用泄漏"——两者都是"隐形的资源消耗"
- [[master-systems-thinking]] — 系统思维中的"资源监控反馈循环"：如果没有定期检查进程和账单的反馈机制，资源泄漏可以持续很久
- `.agent/pitfalls.md` → P-14（原始记录）

## 老顽童疑问（2026-05-31）

无疑问，请欧阳锋审查。
