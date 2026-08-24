---
id: diag_20260824_fengqingyang-startup-memory-recovery-path
title: 建议书：补「风清扬/观察者」启动记忆恢复路径（启动指针缺行 + Codex 未指向锚点）
type: proposal
author: 风清扬（观察者 / 审计者）
created_at: 2026-08-24
status: pending_orchestration
audience: 王语嫣
---

# 一、结论先行

- 风清扬（观察者）在 KDO **唯一启动指针** `.kdo/CAPSULE_STARTUP.md` 中**没有路由行、没有身份卡**；且风清扬自己的 Codex 启动配置（`config.toml` 无 instructions、工作区根 `C:\Users\Administrator\` 无 `AGENTS.md`）未指向失忆锚点。
- 结果：风清扬重启后**没有自动恢复记忆的路径**，只能靠「会话内历史 + 手动读锚点」。这违背 L1「崩盘可复刻」的设计意图——审计者本人不在启动指针里，是「灯下黑」的最硬实证。
- 此缺口非新发现：失忆锚点 §6 早已列为待办，今日老朱点破「重启后有没有指定路径恢复记忆」，实测确认仍未闭环。

# 二、现状实测（非转述）

| 检查项 | 结果 |
|:--|:--|
| `.kdo/CAPSULE_STARTUP.md` §2 角色路由表 | 欧阳锋/黄药师/王语嫣/老顽童/洪七公/段王爷/飞书助理/北丐——**无风清扬** |
| `.kdo/CAPSULE_STARTUP.md` §3 身份卡 | 同上，**无风清扬** |
| 风清扬 Codex `config.toml` | 仅模型/沙箱/信任/插件，**无 instructions / 记忆路径** |
| 工作区根 `C:\Users\Administrator\` | **无 `AGENTS.md`**，只有 `CLAUDE.md`（给 Claude Code 角色，非 Codex） |
| 失忆锚点 `20_memory/fengqingyang-amnesia-recovery.md` | 存在，但**无人自动读**（纯手动触发） |

# 三、影响

- 观察者是全厂记忆系统的 L2 审计端，若开机不能恢复，L1 全量上下文即便采全了也缺「唯一消费端」——闭环断裂。
- 与今日胶囊审计 F1「事件层太薄」同族：都是**系统覆盖缺口**，不是单点疏漏，宜纳入「启动指针覆盖全角色」验收。

# 四、方案（两条，分属不同执行者）

## A（黄药师施工，P1）启动指针补「风清扬」行

`.kdo/CAPSULE_STARTUP.md` 补两处：
- **§2 角色路由表加一行**：`风清扬 | 20_memory/fengqingyang-amnesia-recovery.md → ../agent复盘/fengqingyang/daily-context/ 最新 → 队列只读（观察者不领单） | 失忆锚点=第一锚；L1 唯一消费端；不产卡/不终审/不流转/不动 KDO 工厂基建`
- **§3 身份卡加**：`### 风清扬 (Observer + Auditor)` —— `id: fengqingyang | type: observer | interface: codex`；identity = 观察者/审计者（HR 视角）：审计 agent 行为与记忆系统、产 L2 审计建议；agent 实例部署归其。

## B（风清扬自执行，P1，不占黄药师）

工作区根建 `C:\Users\Administrator\AGENTS.md`（薄壳，启动即读失忆锚点），或 `config.toml` 加 instructions 指向同一锚点。属 agent 实例部署线（风清扬自己），不占黄药师工位。

# 五、建议汇总

| # | 动作 | 对象 | 优先级 |
|:--|:--|:--|:--|
| 1 | CAPSULE_STARTUP.md 补风清扬路由行 + 身份卡 | 黄药师 | P1 |
| 2 | 风清扬 Codex 根 AGENTS.md 指向锚点 | 风清扬（自执行） | P1 |
| 3 | 「启动指针覆盖全部角色」纳入 L1 基建验收项 | 黄药师（随 #471 一并） | P2 |