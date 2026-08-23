---
id: diag_20260823_fengqingyang-memory-capsule-backup-stale
title: 记忆胶囊审计建议：B 镜像过期，可恢复声明已失效（P1）
type: proposal
author: 风清扬（观察者 / 审计者）
created_at: 2026-08-23
status: resolved
audience: 王语嫣
---

# 记忆胶囊审计建议：B 镜像过期，可恢复声明已失效

> 触发：老朱 2026-08-23 指令「提取记忆胶囊审计，并写建议书」→ 风清扬实库提取 + 复跑 status/verify 后出本建议。
> 定位：观察者审计/建议（B2-2① 只交王语嫣）。我只审计、定口径、产建议；**不跑 mirror、不注册计划任务、不改代码、不产卡**。

## 0. 一句话结论

#434 自动写入端已上线且真实在记（A 主库 5 条，含 3 条真实角色复盘）；但 **B 镜像还停在 #432 时点，落后 4 条真实事件，`verify` 已 FAIL**。当前「A+B 双层可恢复」的声明是假的——此刻 A 崩，最近 4 条全丢。这是 P1，建议黄药师立即手动 mirror 补缺 + 老朱拍板镜像计划任务时间锚。

## 1. 审计事实（实库提取，非转述）

- 时点：2026-08-23（本次会话）。
- A 主库：`C:\Users\Administrator\.kdo-memory\L0\activity_log.db`，**5 行**，最新 ts `2026-08-23T04:03:59Z`，integrity ok。
- B 镜像：`D:\KDO-memory\L0-backup\activity_log.db`，**1 行**，最新 ts `2026-08-22T16:34:51Z`，integrity ok。
- `memory_capsule.py verify`：**FAIL —— `activity_log.db: hash 不一致`**（B 落后 4 条）。
- `schtasks`：查无 `kdo-memory-mirror` 常驻任务（镜像仍为手动）。

事件明细：

| # | agent_id | event_type | 性质 |
|:--|:--|:--|:--|
| 1 | huangyaoshi | capsule_test | #432 狗粮 |
| 2 | `__test434__` | review_saved | #434 测试残留 |
| 3 | fengqingyang | review_saved | 真实 |
| 4 | wangyuyan | review_saved | 真实 |
| 5 | `老顽童` | review_saved | 真实（agent_id 中文） |

## 2. 核心问题：备份侧没跟上写入侧

- #434（自动写入端）已 `reviewed A-` 并真实落库，写入侧「活」了。
- 但镜像仍是手动（#432/#434 边界「老朱确认前不注册常驻计划任务」），#434 上线后无人补跑 `mirror`，于是 A 在涨、B 冻结。
- 结论：**「自动记账」现在只是「单点记账」，没有第二盘兜底**。这正好撞上我们刚立的健康度纪律——「可恢复」声明必须附 verify 输出；现在 verify 输出就是 FAIL。

## 3. 建议

### 建议 1 · 黄药师立即手动补一次 mirror（P0 动作，关闭缺口）

不注册任何计划任务，只跑一次 `python kdo-tools/memory_capsule.py mirror`，随即 `verify` 并附 PASS 输出。先把当前 4 条缺口关掉。

### 建议 2 · 老朱拍板镜像计划任务时间锚

命令早已备好（#434 编排补充）：`schtasks /create /tn kdo-memory-mirror /tr "python kdo-tools/memory_capsule.py mirror" /sc daily /st 03:00`。建议**不晚于本次会话**给出确认或改点；在此之前不得擅自注册。

### 建议 3 · 计划任务注册前的临时纪律

在常驻任务生效前，把「写入后同日至少跑一次 mirror + verify」定为临时收尾动作（或挂到当日复盘收尾），禁止「只写不备」。否则每天的真实复盘事件都在裸奔。

### 建议 4 · 「B 落后于 A」纳入健康度巡检（#425 家族）

`status/verify` 已具备 hash 对比能力；建议巡检项增加「verify PASS 才算备份有效」，FAIL 即告警，而不是等下一次审计才被发现。

## 4. 需要谁动作

| 角色 | 动作 |
|:--|:--|
| 黄药师 | 立即手动 mirror + verify 补缺（建议 1） |
| 老朱 | 拍板镜像计划任务时间锚（建议 2） |
| 王语嫣 | 吸收本建议；若立项则编排 P1；临时纪律落地（建议 3） |
| 欧阳锋 | 终审本建议留痕 |
| 风清扬 | 已出本建议；后续只审计 verify 状态，不实施 |

## 5. 边界声明

- 风清扬只审计、定口径、产建议；不跑 mirror、不注册计划任务、不改 `memory_capsule.py`、不产卡。
- 测试残留 `__test434__` 与中文 `老顽童` 的 agent_id 清理已在 #456 承接，本文不重复。

---

*风清扬（观察者 / 审计者）· 2026-08-23 · 只审计、不实施*