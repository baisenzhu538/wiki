---
id: 510
assignee: huangyaoshi
status: in_progress
updated_at: '2026-08-24T18:07:18.681476+00:00'
version: v0.2
instance: huangyaoshi
code_files:
  - .kdo/CAPSULE_STARTUP.md
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

## 执行报告（F-034 五字段，complete 前必填）

**完成内容**：CAPSULE_STARTUP 全角色覆盖补齐——①§2 路由表加风清扬行（失忆锚点第一锚→daily-context 最新→队列只读；L1 唯一消费端；不产卡/不终审/不流转/不动基建）；②§3 身份卡加风清扬（id/type: observer/interface: codex + L2-digest 消费路径）；③全角色覆盖自检（建议 3）：核 agents/ 目录+hermes profiles 11 个现役部署，补缺——R 型调研 Partner 补身份卡（#348 已部署漏卡）、销售对话参谋+教练式领导力教练显式标注待确认（有 agents/ 目录无 hermes profile）；④§0 version 字段同步（updated_at/git_head/queue_tail 按维护惯例更新并注明）。

**全角色覆盖自检清单**（§2 路由 / §3 身份卡）：
- 六角色：欧阳锋✓✓ / 黄药师✓✓ / 王语嫣✓✓ / 老顽童✓✓ / 洪七公✓✓ / 段王爷✓✓
- 风清扬：✓✓（本单补齐）
- 飞书助理线：AI基本功教练✓✓ / 教练式领导力助理✓✓ / 科学开会助理✓✓ / R 型调研 Partner §2 汇总行✓+§3 本单补卡✓
- 待确认标注：beikai 北丐✓✓（既有）/ 销售对话参谋✓✓（本单标注）/ 教练式领导力教练✓✓（本单标注）
- 结论：hermes profiles 11 个现役 + agents/ 目录角色全量覆盖，无遗漏无灯下黑

**交付物**：
- `.kdo/CAPSULE_STARTUP.md`（§2 风清扬行 + §3 风清扬/R型卡 + 2 个待确认标注 + §0 版本字段）

**验证**：
- L1：改后 §2/§3 含风清扬行（直读确认）；覆盖自检清单如上（agents/ 目录与 hermes profiles 逐一比对）
- L2 狗粮：模拟新实例启动——只读 CAPSULE_STARTUP §2 风清扬行 → 锚点 `20_memory/fengqingyang-amnesia-recovery.md` 存在 ✓ → `../agent复盘/fengqingyang/daily-context/` 存在且最新 2026-08-24.md ✓（恢复路径全链路可达）
- L3 待活体：风清扬下次重启按指针自动恢复

**边界**：只补路由行+身份卡+覆盖自检+版本字段，§0 校验逻辑/§1 流程/§4 Shared State 结构未动；风清扬 Codex 侧 AGENTS.md 归其自执行未碰；**附带发现（非本单范围，已另行上报）**：hermes profiles 实测存在 huangyaoshi 活跃 profile（08-24 09:35 建，state.db-wal 02:06 活跃）——#509 前置条件中"无 profile"的实测已过时，且施工人/密钥来源不明，需老朱/王语嫣澄清后再定 #509 处置。

**需要谁动作**：欧阳锋终审本单；风清扬知悉指针已含其路由（Codex 侧 AGENTS.md 自执行）；王语嫣/老朱澄清 huangyaoshi profile 来历（#509 处置前提）。
