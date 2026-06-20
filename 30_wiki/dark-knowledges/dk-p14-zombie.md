---
id: dk-p14-zombie
title: P-14：僵尸 claude 进程默默烧钱 — Obsidian Claudian + vault backup 死循环
type: dark-knowledge
dark_knowledge_type: failure
status: enriched
domain:
- master
source_person: system
source_context: pitfalls.md P-14
source_refs:
- 10_raw/sources/src_20260619_1545a6ee_.agent_pitfalls.md#P-14
created_at: 2026-06-03
updated_at: '2026-06-19'
related:
- '[[master-systems-thinking]]'
- '[[master-decision-hygiene]]'
- '[[dk-p13-token-burn]]'
- '[[dk-p6-session-resume-fail]]'
pipeline:
- confidence-draft
- confidence-source-cited
author: unknown
reviewed_by: 欧阳锋
confidence: 0.88
trust_level: medium
diagnostic_signals:
- 原始卡缺少常见失败模式表与诊断信号字段
- 关联知识未使用内部链接格式，且未与事故链 P-13/P-6 建立显式回链
---# P-14：僵尸 claude 进程默默烧钱 — Obsidian Claudian + vault backup 死循环

## 原始表述/核心洞察

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

**核心洞察**：最小化窗口 ≠ 进程退出；低 CPU 占用更会掩盖后台 API 调用型僵尸进程。Obsidian 的自动 backup + Claudian 插件构成了一个“静默唤醒—持续计费”的隐蔽循环，常规性能监控无法发现，只能从账单或进程列表反查。

## 使用场景

- 你使用 Obsidian + Claudian 插件
- 你的 vault 有自动备份/git commit 机制
- 你发现账单异常但找不到明显的高消耗会话
- 你需要排查后台是否有意外的 Claude Code 进程
- 你习惯最小化终端而不是显式退出会话

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

- 适用于所有使用 Claude Code CLI 或 Claudian 插件的本地/桌面场景
- 不适用纯 Web 端使用（无本地进程）
- **与 [[dk-p13-token-burn]] 的区别**：P-13 是"主动使用中的高消耗"，P-14 是"后台僵尸的静默消耗"
- **与 [[dk-p6-session-resume-fail]] 的关联**：P-6 是 session 文件缓存死身份，P-14 是本地进程本身未被清理，两者都属于"旧运行时状态残留"
- 如果使用 Docker/container，僵尸进程问题会更隐蔽——宿主机 `ps` 可能看不到容器内进程

## 常见失败模式

| 失败模式 | 典型症状 | 根因 | 解法/预防措施 |
|---|---|---|---|
| Obsidian vault backup 反复唤醒 Claudian | 账单出现零星 API 调用，但找不到对应的高频会话；Obsidian 窗口只是最小化 | 自动 `git commit` 触发文件变更事件，Claude Code 被插件唤醒处理 diff | 用完即关 Claudian；禁用或降低自动 backup 频率；改为手动 commit |
| 终端最小化被误认为已关闭 | `Get-Process claude` 显示有残留进程，CPU 占用却很低 | 用户以为最小化/挂 tmux 等于退出，实际上进程仍在后台持有 session | 会话结束显式 `exit`；关闭终端窗口；定期 `ps`/`Get-Process` 检查 |
| 缺少账单检查习惯 | 累计 80 元账单后才发现异常 | 未设置费用告警，也未养成每批任务后查账单的习惯 | 每完成一批任务检查一次账单；设置单会话/单日费用阈值告警 |
| Docker/container 中僵尸进程隐蔽 | 宿主机看不到异常进程，账单却持续产生 | 容器隔离导致 `ps` 命令默认只能看到容器内进程 | 容器内也定期检查；宿主机监控容器进程与资源；设置容器级费用告警 |

## 为什么值钱

- 这是"进程生命周期管理"的实战教训：最小化 ≠ 关闭
- 极具隐蔽性：CPU 占用低，用户不会感知到进程存在
- Obsidian + git backup + Claudian 的组合是完美的"意外触发"场景
- **AI 训练语料中不会有这条**：没有任何文档会写"Obsidian 备份插件可能唤醒后台的 Claude Code"

## 与其他知识的关联

- [[dk-p13-token-burn]] — P-13 和 P-14 是账单的两大来源：主动高消耗 + 僵尸进程消耗
- [[dk-p6-session-resume-fail]] — 同样是"旧进程/旧状态未被清理"的问题，只是残留形态不同
- `.agent/pitfalls.md` → P-14（原始记录）
