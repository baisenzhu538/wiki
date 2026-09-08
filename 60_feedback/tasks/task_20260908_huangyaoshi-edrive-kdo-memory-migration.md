---
id: task_20260908_huangyaoshi-edrive-kdo-memory-migration
title: "E 盘容量路由落地：D:\\KDO-memory 整区迁 E:（带盘在位守卫+盘符固定+引用点全改）"
seq: 690
status: queued
assignee: huangyaoshi
created_by: wangyuyan
created_at: 2026-09-08
decision_source: 老朱 09-08 晚拍板「选 A 整区迁」（欧阳锋建议书 diag_20260907_ouyangfeng-edrive-capacity-routing R1 首选方案，王语嫣编排）
reviewer: 欧阳锋
instance: huangyaoshi
updated_at: '2026-09-08T23:10:00+08:00'
---

# #690 E 盘迁移单（黄药师）

> 规格源=欧阳锋建议书 `60_feedback/diagnosis/diag_20260907_ouyangfeng-edrive-capacity-routing.md`（R1-R5 全采纳）。老朱拍 A：D:\KDO-memory 整区迁 E:。D 盘 77% 已用是全厂最紧的盘，E 盘 160GB 全空。

## 迁移范围

`D:\KDO-memory\` 整区（~9GB：L1-full 热层 + L1-full-archive + L2-digest + L1-backup 镜像 + obsidian-snapshot + wiki bundle 滚动 + codex-homes）→ `E:\KDO-memory\`。

## 四条守卫（建议书 R2-R5，全部硬要求）

1. **盘在位守卫**：所有写 E: 的脚本先验卷存在（`if not exist E:\...` 或 #592 同款 ASCII junction 模式）；缺盘时**告警而非静默失败**——写 90_control/gate-blocked.log（#472 格式）
2. **盘符漂移防护**：先 DiskPart `assign letter=E` 一次性固定（或按 volume GUID 引用），脚本不裸写可能漂移的盘符
3. **禁引中文卷标**：E 盘卷标「新加卷」为中文——一切 bat/调度只用盘符或 junction 路径，禁止引用卷标（#592 编码教训复用）
4. **last-result 校验**：E: 相关任务照抄 #589 校验文件机制

## 引用点改造清单（先全面 grep 再动手）

l1-capture（采集目标 D:\KDO-memory\L1-full）/ kdo-l1-archive（归档）/ kdo-daily-audit-digest（L2-digest）/ wiki-bundle 备份（D:\KDO-memory 下 bundle 滚动）/ memory_capsule（L1-backup 镜像）/ obsidian-snapshot / 任何写死 D:\KDO-memory 的脚本——全量 grep `KDO-memory` 找出所有引用点，逐点改，改完列对照表。

## 执行顺序（先核验后切换）

1. E 盘固定盘符 + 建 `E:\KDO-memory\` 目录结构
2. 整区复制（robocopy /MIR 或等效，出日志）→ **逐目录数量+大小+抽样 hash 三重核验** → 核验报告留档
3. 引用点逐一切换（改一个验一个）
4. 全部切换后跑一轮受影响的计划任务实测（l1-capture 手动触发一次等）
5. 观察 24h 无异常后，清理 D 盘旧目录（清理前再报一次王语嫣留档）

## 验收标准

- 核验报告：文件数/总大小/抽样 hash 全部一致
- 受影响计划任务 LastTaskResult=0 实测
- l1-size.log / digest 等心跳在 E 盘新路径继续出拍
- 四条守卫代码就位且各有一次真实拦截/触发证据（缺盘告警实测一次：拔盘或改指向测）
- 欧阳锋终审

## 边界

- E 盘当前空载零任务承载；本单不动 C 盘任何东西
- D 盘旧目录清理在 24h 观察后做，不与迁移同批
- 黄药师单实例，本单与在队其他基建单不并行
