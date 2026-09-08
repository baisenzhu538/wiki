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
> 🆕 老朱 09-08 深夜追加要求：**E 盘要建成即插即用的便携基础设施盘——拿到其他电脑上马上就能用**（见「便携化硬要求」节，优先级高于一切实现细节）。

## 迁移范围

`D:\KDO-memory\` 整区（~9GB：L1-full 热层 + L1-full-archive + L2-digest + L1-backup 镜像 + obsidian-snapshot + wiki bundle 滚动 + codex-homes）→ `E:\KDO-memory\`。

## 四条守卫（建议书 R2-R5，全部硬要求）

1. **盘在位守卫**：所有写 E: 的脚本先验卷存在（`if not exist E:\...` 或 #592 同款 ASCII junction 模式）；缺盘时**告警而非静默失败**——写 90_control/gate-blocked.log（#472 格式）
2. **盘符漂移防护**：先 DiskPart `assign letter=E` 一次性固定（或按 volume GUID 引用），脚本不裸写可能漂移的盘符
3. **禁引中文卷标**：E 盘卷标「新加卷」为中文——一切 bat/调度只用盘符或 junction 路径，禁止引用卷标（#592 编码教训复用）
4. **last-result 校验**：E: 相关任务照抄 #589 校验文件机制

## 引用点改造清单（先全面 grep 再动手）

l1-capture（采集目标 D:\KDO-memory\L1-full）/ kdo-l1-archive（归档）/ kdo-daily-audit-digest（L2-digest）/ wiki-bundle 备份（D:\KDO-memory 下 bundle 滚动）/ memory_capsule（L1-backup 镜像）/ obsidian-snapshot / 任何写死 D:\KDO-memory 的脚本——全量 grep `KDO-memory` 找出所有引用点，逐点改，改完列对照表。

## 便携化硬要求（老朱追加：拿到其他电脑上马上就能用）

目标形态：E 盘拔下来插到 mesh 内任意一台机器（jia-01/jia-02/gongsi-01/gongsi-02），**一条命令以内完成接入并使用**，不依赖原机的盘符/注册表/环境。

1. **自定位，不锁盘符**：盘根放标记文件（如 `\KDO-memory\.disk-id`，内容=卷 GUID+建设日期）；所有脚本定位顺序=标记文件识别卷 → 动态取当前盘符。盘符在别的机器上是 F:/G: 也必须能跑（与守卫 2 的「固定盘符」关系：本机固定 E: 是为了调度稳定，便携要求是指**离了本机不抓瞎**——两者都要）
2. **自包含读取工具链**：盘上除数据外带最小读取工具（`tools/`：query_assets 类检索脚本 + README + 依赖说明），不依赖目标机装有 wiki 仓
3. **attach 引导脚本**：盘根一个 `attach.cmd`——在新机器上跑一次，完成：识别卷→打印数据位置与可用命令→（可选）注册只读检索入口。全程只读目标机，不写注册表不改系统
4. **即插即用验收场景**（终审必演）：E 盘插到另一台机器（建议 jia-02 或 gongsi-01 实测），跑 attach → 检索一条素材成功 → 全程录像/日志留证

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
- **便携验收：异机插盘 → attach → 检索成功，日志留证（便携化硬要求第 4 条）**
- 欧阳锋终审

## 边界

- E 盘当前空载零任务承载；本单不动 C 盘任何东西
- D 盘旧目录清理在 24h 观察后做，不与迁移同批
- 黄药师单实例，本单与在队其他基建单不并行

## ⛔ 红线：本机工厂零中断（老朱 09-08 深夜追加，最高优先级）

本机的看懂工厂与 KDO 基础设施**正常运转不能受任何影响**：

1. **不断拍**：迁移/切换全程，l1-capture（30min 拍）、conveyor-probe/inbox-watch/role-clock（10min 拍）、vault-git-backup、每日复盘拉起、各 gateway——任何一项不许因本单断拍
2. **切换要瞬时**：引用点切换用「先双写/先指向新址验证→再切读」的过渡法，不允许出现"旧路径已废、新路径未通"的真空窗口
3. **回滚随时在**：每一步切换保留指回 D 盘的能力，任何一项验证不过→立即切回→报告，不硬闯
4. **验收加一条硬证据**：迁移窗口期内的 l1-size.log / conveyor-probe.log 心跳连续无断档（终审时附窗口期日志段）
