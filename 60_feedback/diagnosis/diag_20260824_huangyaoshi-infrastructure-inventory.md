---
id: diag-infrastructure-inventory
title: 基建资产总表建议书（infrastructure-inventory.md——识别靠表不靠记忆）
type: proposal
doc_id: D-20260824-001
version: v1.0
author: huangyaoshi
created_at: '2026-08-24T00:30:00+08:00'
updated_at: '2026-08-24T00:30:00+08:00'
audience: 王语嫣
status: pending_orchestration
---

# 基建资产总表建议书（识别靠表不靠记忆）

## 现象一句话

全厂基建（130+ 脚本/计划任务/服务/数据资产/台账）没有一张总表——任何角色（含新 Builder 替代者）识别"基建有哪些、谁健康、哪里断、谁维护"靠记忆+翻目录拼图。

## 在哪发现

2026-08-24 黄药师实战 15 单后自我盘点：对"接触过的"清晰、对"全貌"仍模糊——①90_control/scripts ~80 个脚本中约一半是一次性修复批（fix-*/repair-*/migrate-*），有用/历史遗留无账；②KDO CLI 源码侧（47 文件）vs wiki 侧脚本的分工边界无文档；③计划任务（conveyor-probe/l1-capture/inbox-watch/health-daily）+ 服务（hermes gateway/wx_video_download）+ 数据资产（L1 库+镜像/索引/台账/基线）散落各文档无总览。现有机制（cap_hub 26 Feature/README 登记/memory-registry）各管一段，互不隶属——与 08-23 三路由讨论同构（路由层=导航，本表=资产地图）。

## 建议方向

①**建 `90_control/infrastructure-inventory.md`**（基建资产总表）：按域分类（门禁族/工具族/服务/计划任务/数据资产/基线台账/一次性批标记）+ 每项登记（位置/职责/维护人/最近验证状态/关联），一次性修复批标注"历史遗留待归档"；②**配 `--status` 快照**（一条命令输出各资产健康态，与 health-check 联动）；③**挂路由层附录**（D-018 附录 A 待补项就此结清），CAPSULE_STARTUP 指向；④**维护权**=黄药师（基建单一实例），新增基建组件登记入表=登记纪律（与 40_outputs README 同构但不重复——README 记"存在"，本表记"状态+职责+关联"）。

## 边界

- 只建总表+快照，不动任何组件本体；存量一次性修复批只标注不清理（清理另立项）
- 与 memory-registry（记忆真相源）/cap_hub（能力注册）/README（工具登记）并存分层，不合并不替代
