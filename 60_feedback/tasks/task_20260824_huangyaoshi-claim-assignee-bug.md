---
id: 503
assignee: huangyaoshi
status: queued
updated_at: '2026-08-24'
version: v0.1
instance: huangyaoshi
---

# #503 queue_transition claim assignee 写入口径 bug（kimi 实例误写 laowantong）

- **任务号**：#503
- **状态**：queued
- **assignee**：huangyaoshi（改 claim 写入口径+回归用例；王语嫣编排；欧阳锋终审）
- **优先级**：P1（系统性问题：任何角色用 kimi 实例 claim 任务，frontmatter assignee 都会被错写成 laowantong）
- **立项**：2026-08-24 王语嫣（#497 claim 实测发现：王语嫣用 `--instance kimi` claim 自己的单，assignee 被写为 laowantong）

## 背景

`queue_transition.py:473` `INSTANCE_ROLE_MAP = {"hermes": "laowantong", "kimi": "laowantong"}`——**kimi 被映射为 laowantong**，但实际角色实例分布（#445 映射）：王语嫣=kimi、欧阳锋=kimi、老顽童=hermes。kimi 是多角色共用实例（CLI 名），**按 instance 反推 assignee 在 kimi 上是系统性错误**。

claim 写入（action_claim → apply_updates）`assignee=_role_of(instance)` 把任务单 assignee 覆盖为 instance 反推角色——#444 口径（assignee=角色名+instance 另存）的正确语义应是：claim 不改 assignee（保持队列行/任务单原值），instance 字段记录执行实例。

## 任务

1. **claim 写入口径修正**：claim 时 assignee **保持任务单/队列行原值**（不按 instance 反推），只更新 status=in_progress + instance=<执行实例>
2. **INSTANCE_ROLE_MAP 处理**：移除 `kimi: laowantong`（多角色共用实例不可反推角色；hermes 是否保留待确认——hermes 目前是老顽童专属？若也是多角色则一并移除，统一"claim 不改 assignee"语义）
3. **回归用例**：王语嫣(kimi) claim 王语嫣单 → assignee 保持 wangyuyan；老顽童(hermes) claim 老顽童单 → assignee 保持 laowantong；A 角色 claim B 角色单（非法场景）→ can_claim 拒绝或 assignee 保持 B
4. **存量修正**：#497 frontmatter 已手工修正 assignee=wangyuyan（本单实证），其他任务单如被同样误写则复扫修正

## 验证（验证分层）

- L1：单测全过（三场景：同角色 claim 保持/跨角色 claim 拒绝/instance 记录正确）
- L2 狗粮：王语嫣用 kimi claim 一张测试单，assignee 不再被改写
- L3 待活体：后续 claim 事件 assignee 不再漂移

## 边界

- 只改 claim 写入路径，不动 queue_transition 其他命令（complete/review 等）
- #444 口径（assignee=角色名）维持——修的是"claim 时按 instance 反推覆盖"这个实现缺陷
- 存量 assignee=实例名的任务单不回改（#444 兼容口径）

## 关联

- #497（本 bug 实测现场）
- #444（assignee=角色名+instance 另存口径）
- #445（角色实例分布映射）
- E034/E038（执行状态核实纪律——本次发现=claim 后核 frontmatter）

## 需要谁动作

- **黄药师**：claim 写入口径修正 + INSTANCE_ROLE_MAP 清理 + 回归用例
- **王语嫣**：复扫存量误写 assignee 任务单
- **欧阳锋**：终审本单

## 执行报告（F-034 五字段，complete 前必填）
