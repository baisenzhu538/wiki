---

id: dk-p14-zombie
title: P-14：僵尸 claude 进程默默烧钱 — Obsidian Claudian + vault backup 死循环
type: dk
dark_knowledge_type: failure
status: enriched
domain:
- master
source_person: system
source_context: pitfalls.md P-14
source_refs:
- src_unknown
created_at: 2026-06-03
updated_at: '2026-06-19'
related:
  - [[obsidian-kdo-内容产出工作流-产品设计大纲]]
  - [[dk-c7-auto-backup-conflict]]
  - [[obsidian-git-sync-protocol]]
  - [[pending_unknown]]
  - [[pending_unknown]]
pipeline:
- src_unknown
- src_unknown
author: unknown
reviewed_by: 欧阳锋
confidence: 0.88
trust_level: medium
diagnostic_signals:
- src_unknown
- src_unknown# P-14：僵尸 claude 进程默默烧钱 — Obsidian Claudian + vault backup 死循环

---

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

- src_unknown
- src_unknown
- src_unknown
- src_unknown
- src_unknown

## 操作方法

1. **会话结束时确认关闭**：
   - src_unknown
   - src_unknown
   - src_unknown

2. **定期检查进程**：
   - src_unknown
   - src_unknown
   - src_unknown

3. **管理 Obsidian Claudian**：
   - src_unknown
   - src_unknown
   - src_unknown

4. **账单监控**：
   - src_unknown
   - src_unknown
   - src_unknown

5. **不要做的事**：
   - src_unknown
   - src_unknown
   - src_unknown

## 适用边界

- src_unknown
- src_unknown
- src_unknown
- src_unknown
- src_unknown

| 失败模式 | 典型症状 | 根因 | 解法/预防措施 |
|
|---|---|---|
| Obsidian vault backup 反复唤醒 Claudian | 账单出现零星 API 调用，但找不到对应的高频会话；Obsidian 窗口只是最小化 | 自动 `git commit` 触发文件变更事件，Claude Code 被插件唤醒处理 diff | 用完即关 Claudian；禁用或降低自动 backup 频率；改为手动 commit |
| 终端最小化被误认为已关闭 | `Get-Process claude` 显示有残留进程，CPU 占用却很低 | 用户以为最小化/挂 tmux 等于退出，实际上进程仍在后台持有 session | 会话结束显式 `exit`；关闭终端窗口；定期 `ps`/`Get-Process` 检查 |
| 缺少账单检查习惯 | 累计 80 元账单后才发现异常 | 未设置费用告警，也未养成每批任务后查账单的习惯 | 每完成一批任务检查一次账单；设置单会话/单日费用阈值告警 |
| Docker/container 中僵尸进程隐蔽 | 宿主机看不到异常进程，账单却持续产生 | 容器隔离导致 `ps` 命令默认只能看到容器内进程 | 容器内也定期检查；宿主机监控容器进程与资源；设置容器级费用告警 |

## 为什么值钱

- src_unknown
- src_unknown
- src_unknown
- src_unknown

## 与其他知识的关联

- src_unknown
- src_unknown
- src_unknown
