---
id: diag_20260823_fengqingyang-codex-instance-isolation
title: Codex 实例隔离与 L1 采集面补全建议（CODEX_HOME 分家 + sessions 采集）
type: proposal
author: 风清扬（观察者 / 审计者）
created_at: 2026-08-23
status: pending_orchestration
audience: 王语嫣
---

# Codex 实例隔离与 L1 采集面补全建议

> 触发：老朱问「Codex 每个实例是否单独记忆 / 空间 / profile」→ 风清扬实测审计 → 老朱令「写建议书」。
> 定位：观察者审计建议（只交王语嫣）。我只审计、定口径、产建议；不实施。

## 0. 一句话结论

本机 Codex 当前是**单实例共享**（单 config.toml / 单 memory / 单 sessions / CODEX_HOME 未设），不满足「每个角色全量上下文必须独立」；且 L1 全量采集面漏掉 Codex sessions。需两件事：①若 Codex 作为角色 CLI，用 `CODEX_HOME` 按角色分家；②采集面补 Codex sessions。

## 1. 审计事实（实测，非转述）

- 单 profile：`C:\Users\Administrator\.codex\config.toml` 无 `[profiles.*]`，仅一份默认配置（model=deepseek-v4-pro，relay 127.0.0.1:4444）。
- 单记忆：`~\.codex\memory\context.md` 一份 + `memories_1.sqlite` 一个。
- 单会话：`~\.codex\sessions\` 单一库 + `history.jsonl` 一份。
- 环境变量：`CODEX_HOME` 未设 → 所有 codex 进程落同一个 `~\.codex\`。
- 现状角色工具映射（#445）：黄药师=claude / 欧阳锋=kimi / 王语嫣=kimi / 老顽童=hermes / 风清扬·洪七公·段王爷=飞书类——**当前无角色用 codex**，但本机 `.codex\` 有活跃使用（sqlite 今日有写）。
- L1 采集面（#463）：只采 claude / kimi-code / hermes，**未采 Codex sessions**。

## 2. 建议

### 建议 1 · Codex 实例隔离：CODEX_HOME 按角色分家（黄药师，经王语嫣）

- 每个需用 Codex 的角色给独立目录：`D:\KDO-memory\codex-homes\<角色>\`（config / memory / sessions 全分离）。
- 启动时注入 `CODEX_HOME`；若未来把某角色切到 codex，同步登记进 #445 一键启动脚本角色表。
- 迁移口径：现有共享 `~\.codex\sessions\` 与 `memory\context.md` 是否按角色拆分，由王语嫣 / 黄药师定；默认**不迁移**——新角色新家起新档，旧档只读留存备查。

### 建议 2 · L1 采集面补 Codex sessions（黄药师，经王语嫣）

- `l1_capture.py` 增补 `~\.codex\sessions\`（分家后改为 `codex-homes\<角色>\sessions\`）。
- 与既有 claude / kimi-code / hermes 采集同口径：mtime 增量、幂等、失败可见、体积红线。

### 建议 3 · 通用纪律（可选，王语嫣裁定）

- 把「每个角色的 CLI 实例必须独立 HOME / 记忆 / 会话，且 L1 采集面必须覆盖该工具」写成通用纪律，不只针对 Codex——防未来再冒出新工具实例共享的坑。是否入 charter / spec 由王语嫣编排、老朱拍板。

## 3. 需要谁动作

| 角色 | 动作 | 经谁 |
|:--|:--|:--|
| 王语嫣 | 吸收本建议，编排立项 | — |
| 黄药师 | CODEX_HOME 分家 + l1_capture 补面 | 经王语嫣 |
| 欧阳锋 | 终审留痕 | 经王语嫣编排 |
| 老朱 | 拍板是否启用 Codex 作为角色 CLI、目录位置 | — |
| 风清扬 | 已出本建议；后续只审计 | 对接老朱 + 王语嫣 |

## 4. 边界声明

- 风清扬只审计、定口径、产建议；不改 Codex 配置、不改脚本、不产卡、不动队列。
- 风清扬唯一直接对接 = 老朱 + 王语嫣；实施一律经王语嫣编排转达。

---

*风清扬（观察者 / 审计者）· 2026-08-23 · 只审计、不实施*