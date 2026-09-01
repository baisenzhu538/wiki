---
id: "592"
title: "wiki 恢复力基建加固——异机备份+快速重建+完整性自检三件套（老朱直令：确保能恢复不会造成大的影响）"
type: infrastructure
status: queued
priority: P0
assignee: 黄药师
created_by: 王语嫣
created_at: 2026-09-01
updated_at: 2026-09-01
source_refs:
- 90_control/scripts/wiki-bundle-backup.bat（#589 已交付的每日 bundle）
- "#589/#590 事故报告"
---

# #592 wiki 恢复力三件套（老朱 09-01 直令「加强基础设施，确保能恢复」）

## 现状与缺口

已有：每日 02:30 bundle 备份（D 盘同机，7 份滚动，#589 交付，实跑 PASS）。
缺口：**备份与 wiki 同机**——目录级删除防住了（08-31 型事故恢复点已证），整机故障/勒索加密/盘坏防不住；且无「恢复演练」——真出事时恢复路径只有 08-31 那次手工经验，无固化脚本。

## 任务（三件套）

### R1 异机备份（最高优先）
每日 bundle 生成成功后，自动复制最新 bundle 到坚果云同步目录（`C:\Users\Administrator\Nutstore\1\我的坚果云\kdo-backup\`，坚果云自动上云=异机副本），保留 3 份滚动。改 wiki-bundle-backup.bat 或加第二步脚本（推荐后加：失败不影响主备份，log 分开）。**自证**：手动 /run 后确认坚果云目录出现 bundle 且 NutstoreClient 日志显示上传事件。

### R2 快速重建脚本固化
把 08-31 手工恢复路径固化为 `90_control/scripts/wiki-vault-restore.py`：输入 bundle 路径+目标目录 → 校验（git bundle verify + HEAD 比对）→ clone/rebuild → 输出文件数+git status 对照报告。**自证**：用最新 bundle 在临时目录（如 D:\_restore_test\）演练一次全流程，输出「恢复后文件数 vs 现仓文件数」对照，演练目录清理。

### R3 完整性自检例行
轻量巡检脚本（挂既有 kdo-health-daily 或独立计划任务，每日 1 次）：①工作树文件数+git status 干净度 ②最新 bundle 存在性+mtime+verify ③异机副本存在性。异常→写 gate-blocked 通道（复用 #472 探针通知面），值班（王语嫣时钟拍）自动消费。**自证**：人为制造一个异常（如临时改名 bundle），确认通知面触发，再还原。

## 验收标准

- 三件全部实跑自证（不接受「已配置」），输出留痕
- R1: 坚果云端可见副本（本地目录出现+上传日志）
- R2: 演练恢复文件数与现仓一致（±untracked 合理范围）
- R3: 异常注入测试触发+还原

## 边界

- 不动 wiki 本体（只读 bundle/clone）
- 坚果云只做「被动接收文件的普通同步目录」，**不把 wiki 加入同步**（#589 铁证：同步机制碰 .git 有前科）
- 勒索防护/访问控制类（ACL 加固、受控文件夹访问）不在本单（等安全排查收敛后老朱拍板，避免影响产线写入）

## 需要谁动作

- 欧阳锋：终审
- 王语嫣：R3 异常通知接入值守消费面（终审 PASS 后编排层配置）

## 执行报告

（完工后填写）
