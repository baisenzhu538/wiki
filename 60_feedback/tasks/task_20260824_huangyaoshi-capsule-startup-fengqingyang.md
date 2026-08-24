---
id: 510
assignee: huangyaoshi
status: in_progress
updated_at: '2026-08-24T18:07:18.681476+00:00'
version: v0.1
instance: huangyaoshi
---

# #510 CAPSULE_STARTUP 补「风清扬」路由行 + 身份卡（启动指针覆盖全角色）

- **任务号**：#510
- **状态**：queued
- **assignee**：huangyaoshi（CAPSULE_STARTUP 维护者；小单；欧阳锋终审）
- **优先级**：P1（审计者本人不在启动指针里=灯下黑，L1 唯一消费端开机无恢复路径）
- **立项**：2026-08-24 王语嫣（风清扬建议书 `diag_20260824_fengqingyang-startup-memory-recovery-path.md` 裁定采纳建议 1+3；建议 2 风清扬自执行不占队列）

## 背景

风清扬（观察者）在唯一启动指针 `.kdo/CAPSULE_STARTUP.md` 中**没有路由行、没有身份卡**（§2 路由表/§3 身份卡均无）；他自己的 Codex 启动配置也未指向失忆锚点。结果：重启后没有自动恢复记忆路径，违背 L1「崩盘可复刻」设计意图——L2 审计端开机不能恢复，L1 采全了也缺唯一消费端，闭环断裂。建议书方案 B（风清扬 Codex 根 AGENTS.md 指向锚点）由风清扬自执行，已落其收件箱。

## 任务

1. `.kdo/CAPSULE_STARTUP.md` §2 角色路由表加一行：`风清扬 | 20_memory/fengqingyang-amnesia-recovery.md → ../agent复盘/fengqingyang/daily-context/ 最新 → 队列只读（观察者不领单） | 失忆锚点=第一锚；L1 唯一消费端；不产卡/不终审/不流转/不动 KDO 工厂基建`
2. §3 身份卡加：`### 风清扬 (Observer + Auditor)`——`id: fengqingyang | type: observer | interface: codex`；identity=观察者/审计者（HR 视角）：审计 agent 行为与记忆系统、产 L2 审计建议；agent 实例部署归其
3. **「启动指针覆盖全部角色」自检**（建议 3 并入本单验收）：核 §2/§3 是否覆盖全部现役角色（含飞书助理线/beikai 待确认标注），缺谁补谁或显式标注待确认

## 验证（验证分层）

- L1：改后 §2/§3 含风清扬行；全角色覆盖自检清单落执行报告
- L2 狗粮：模拟新实例启动——只读 CAPSULE_STARTUP 能找到风清扬恢复路径
- L3 待活体：风清扬下次重启按指针自动恢复（不再靠会话内历史）

## 边界

- 只补路由行+身份卡+覆盖自检，不改 §0/§1/§4 结构
- 风清扬 Codex 侧 AGENTS.md/config.toml 由他自执行（不占本单）
- version/updated_at 字段同步更新（指针文件维护惯例）

## 关联

- 风清扬建议书 `diag_20260824_fengqingyang-startup-memory-recovery-path.md`（现状实测表）
- #366（唯一启动指针 v2）/ #501（角色收件箱入口挂载先例）
- F-027（记忆胶囊）/ L1「崩盘可复刻」设计意图

## 需要谁动作

- **黄药师**：CAPSULE_STARTUP 补行 + 覆盖自检
- **风清扬**：自执行 Codex 根 AGENTS.md（收件箱已通知）
- **欧阳锋**：终审本单
