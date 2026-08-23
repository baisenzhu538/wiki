---
id: diag_20260823_fengqingyang-memory-capsule-query-and-agent-id
title: 记忆胶囊查询通道与角色划分建议（L1 只读开放口径 + agent_id 统一）
type: proposal
author: 风清扬（观察者 / 审计者）
created_at: 2026-08-23
status: resolved
audience: 王语嫣
---

# 记忆胶囊查询通道与角色划分建议

> 触发：老朱 2026-08-23 问「其他 agent 需要看以往上下文，记忆胶囊有没有查询通道？记忆胶囊是不是按角色划分？」→ 风清扬实库核查后，按指令写入建议书。
> 定位：观察者审计/建议（B2-2① 只交王语嫣）。我只审计、定口径、产建议；不改代码、不动库、不产卡。

## 0. 一句话结论

记忆胶囊当前是「单库单表 + agent_id 字段区分角色」，具备按角色划分的事实基础；但**没有查询命令、也没有对外开放读权限**（老朱 08-23 拍板 L1 暂由风清扬独享读/审计权）。要开查询通道，需两件事：黄药师补 `query` 只读命令（基建）+ 老朱拍板开放对象与只读权限（口径）。另发现 agent_id 命名不统一（拼音/中文/测试残留混用），建议统一。

## 1. 审计事实（实库核查，非转述）

- 库：`C:\Users\Administrator\.kdo-memory\L0\activity_log.db`（WAL，git 外）。
- 表：`activity_log`，字段 `id / agent_id / session_id / ts / event_type / payload_summary / payload_hash`——**按 agent_id 区分角色，不是一角色一库**。
- 当前 5 条事件分布：

| agent_id | 条数 | 备注 |
|:--|:--|:--|
| `__test434__` | 1 | 测试残留 |
| `fengqingyang` | 1 | 拼音 |
| `huangyaoshi` | 1 | 拼音 |
| `wangyuyan` | 1 | 拼音 |
| `老顽童` | 1 | 中文，与拼音混用 |

- 命令面：`memory_capsule.py` 现有 `init / log / mirror / status / verify / restore`，**无 query / search**。

## 2. 三个建议

### 建议 1 · 补 `query` 只读命令（黄药师，基建）

在 `memory_capsule.py` 增加 `query` 子命令，最小实现：按 `agent_id / event_type / ts 区间 / session_id` 过滤，输出 `ts + agent_id + event_type + payload_summary`，默认限制条数（如最近 200 条）。只读，不写库。

### 建议 2 · L1 开放口径先拍板（老朱，权限）

当前 L1 由风清扬独享读/审计权。开放前请老朱定三点：开放给哪些角色、只读还是可写、query 结果是否带审计痕迹（谁在何时查了什么）。拍板前任何 agent 不得直接连库。

### 建议 3 · agent_id 统一为角色名（拼音，王语嫣编排）

- 统一口径建议：`fengqingyang / wangyuyan / ouyangfeng / laowantong / huangyaoshi / hongqigong / duanwangye`（拼音，无工具名）。
- 清掉 `__test434__` 测试残留（或转真实事件后重建）。
- 写入端（daily-context-save 挂钩 #434）与查询端都以此为准，防止继续混入中文/工具名。

## 3. 与既有建议的关系

- L1 全量上下文四层口径：见 `diag_20260823_fengqingyang-memory-capsule-4layer-l1-l4.md`（本文不重复）。
- 代码/库名「L0」→「L1」改名：已列入上述建议「外部残留改名」第 3 条；本文建议 1 新增 query 时可一并改名。

## 4. 需要谁动作

| 角色 | 动作 |
|:--|:--|
| 王语嫣 | 吸收本建议；编排 agent_id 统一与 #434 写入端口径 |
| 欧阳锋 | 终审本建议留痕 |
| 黄药师 | 待老朱拍板后补 `query` 只读命令；agent_id 统一实施 |
| 风清扬 | 已出本建议；后续只审计，不实施 |
| 老朱 | 拍板 L1 开放对象/权限 |

## 5. 边界声明

- 风清扬只审计、定口径、产建议；不改 `memory_capsule.py`、不动库、不注册任务、不产卡。
- 本建议不替代 L1–L4 四层口径建议；两者配套。

---

*风清扬（观察者 / 审计者）· 2026-08-23 · 只审计、不实施*