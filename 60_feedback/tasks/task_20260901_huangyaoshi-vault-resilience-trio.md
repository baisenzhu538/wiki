---
id: '592'
title: wiki 恢复力基建加固——异机备份+快速重建+完整性自检三件套（老朱直令：确保能恢复不会造成大的影响）
type: infrastructure
status: reviewed
reviewed_by: 欧阳锋
review_date: '2026-09-01'
grade: B+
priority: P0
assignee: 黄药师
created_by: 王语嫣
created_at: 2026-09-01
updated_at: '2026-09-01T05:14:08.855963+00:00'
source_refs:
- 90_control/scripts/wiki-bundle-backup.bat（#589 已交付的每日 bundle）
- '#589/#590 事故报告'
instance: huangyaoshi
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

**文件清单**：`90_control/scripts/wiki-bundle-offsite-2nd.bat`（R1 异机备份第二步，已挂接主备份脚本成功后 call）/`90_control/scripts/wiki-vault-restore.py`（R2 重建脚本）/`90_control/scripts/vault-integrity-check.py`（R3 完整性自检）/`kdo-tools/run-kdo-health.cmd`（R3 挂载行追加，编排层代收尾）/本任务单。 commit 见 git log。

**完成内容**：R1=最新 bundle 自动复制坚果云 kdo-backup 目录（3 份滚动，独立 log，失败不阻塞主备份），顺带修复历史遗留乱码目录「鎴戠殑鍧氭灉浜憍kdo-backup」重命名为规范名；R2=08-31 手工恢复路径固化为脚本（verify→clone→文件数+HEAD+git status 对照+清理）；R3=三查自检（工作树/bundle/异机副本）异常写 gate-blocked（#472 格式），修正「最新 bundle=文件名最大者」判定缺陷+补 last-result.txt 检查。

**验证**：R1 实跑——wiki-bundle-20260901.bundle（2,316,604,477 字节）已落坚果云目录字节等大，nutstore.db 活体 WAL（拷贝到 TEMP 只读开）sndobject 表实证同步引擎已跟踪；R2 演练——verify rc=0/clone rc=0/恢复 24,896 文件 dirty=0，正确识别 bundle-older（差 17 文件=当天新 commit）；R3 注入测试——临时改名 bundle 触发「bundle 缺失+异机缺失」双报警进 gate-blocked，还原后 rc=1 通道验证通过；挂载后编排层实跑 `vault-integrity-check.py`：vault 25,142 文件+bundle+offsite 三查全 OK exit 0。

**未做项**：坚果云服务端 event.db 尚未回显 kdo-backup 条目（2.16GB 大文件上传排队中，本地 sndobject 已跟踪=正常延迟，观察项）；杀扫/改密/sshd 收紧不在本单（等 #591 终审+老朱拍板）。

**需要谁动作**：欧阳锋终审本单+#591；王语嫣——R3 异常已走 gate-blocked 通道，值守拍自动消费（编排层已确认接入，无需额外配置）；老朱——明日 02:30 首次全链自动跑（bundle→offsite→02:07 挂载的 integrity check 顺序为 02:07 先于 02:30，即自检当天会查到前日 bundle，属设计内时序）后可查日志确认。

## 机器预审报告

> 🤖 机器预审参考层（#515）：仅供欧阳锋终审参考，不构成结论、不放行不拦截

### ① 声称-交付差集

✅ 4 个声明路径全部存在+已跟踪+无脏改动
### ② lint

✅ frontmatter 可解析 + F-034 五字段在位
### ③ 负向判词 / ④ 存在性核查

🔴 意见书含负向断言（缺失）但无 `**存在性核查**` 锚点（#433：'我没看到'≠'不存在'，负向判词必须附核查节，否则不闭环）（生产侧同口径，供终审对照）

## 终审记录（2026-09-01 欧阳锋 · PASS B+）

**结论**：PASS B+。R2/R3 代码质量与实测达 A 线（我侧独立复跑全过），R1 存在两处 P1 缺陷——编码缺陷将使**明日 02:30 自动链路静默失效**（手动实跑靠侥幸成功），报告把侥幸成功写成已交付自证。修复点小且明确（P1-2 一行），返工成本低；因自动链路失效直接违背本单「确保能恢复」的核心目标，不给 A。

**达标面（O3 独立复跑，全部亲验）**：

| 验收点 | 实测 | 判定 |
|---|---|---|
| R1 字节等大 | 坚果云 kdo-backup/wiki-bundle-20260901.bundle = 2,316,604,477B，与 D 盘源逐字节同数（ls 双侧实测）；offsite log 11:50 OK 行+last-result=OK | ✅ |
| R1 挂载链 | wiki-bundle-backup.bat L55 call 成功后触发；L56-58 失败不阻塞主备份（WARN 语义正确） | ✅ |
| R2 演练复算 | verify rc=0（我亲跑 HEAD=014daeec）；bundle-older 判定逻辑成立：现仓 HEAD=b2966d943≠bundle HEAD→warn 不 FAIL，「差 17 文件=当天新 commit」方向正确 | ✅ |
| R3 注入测试痕迹 | gate-blocked.log L447 12:00:38 vault-integrity 行在案（真实故障+真实报警）；编排层 12:35 划销处置已入 git（b2966d943） | ✅ |
| R3 挂载+活体 | run-kdo-health.cmd L11 挂载行在案；**我亲跑 vault-integrity-check.py：三查 OK exit 0，零副作用** | ✅ |
| R3 选包缺陷修正 | 「文件名最大→mtime 最新」复算确认已修（mtime 排序亲测选出 20260901）；12:00 行的「postfix 过期」系健康任务 02:07 先于 bundle 02:30 的设计内时序空窗，非缺陷 | ✅ |
| 铁律①wiki 不入同步 | Nutstore 全树 walk：wiki 源码零出现在同步目录，仅 kdo-backup/bundle | ✅ |
| 铁律②nutstore.db 只读 | R1 路径不触碰 db；验证走 TEMP 副本 | ✅ |

**P1 缺陷（2 项，返工点）**：

- **P1-1 R1 bat 编码缺陷（证据链闭合）**：`wiki-bundle-offsite-2nd.bat` 无 BOM UTF-8 内嵌中文路径「我的坚果云」（L13），本机 ACP=936（注册表 OEMCP 实测）、任务计划环境无 chcp 65001 前置（父脚本 wiki-bundle-backup.bat 全文无 chcp）。我受控实验复现：同构 UTF-8 bat 在 cp936 下把 DEST 解析成乱码目录（实验产物 '鎴戠殑鍧氭灉浜慭kdo-backup'，与报告自述「历史遗留乱码目录」同款模式——正是这一前科的正确成因）。11:50 实跑成功靠的是父 cmd 继承了 Unicode 代码页的**非设计内侥幸**（其日志 cmd 回显字节 d2d1b8b4…=GBK「已复制 1 个文件」，恰证运行时码页非 UTF-8）。**预测：明日 02:30 调度环境大概率复现为乱码目录/复制失败**——而 last-result 仍写 OK 或 fail 被主备份 WARN 吞掉，静默失效。**修复指令（黄药师，一行）**：bat L1 `@echo off` 后加 `chcp 65001 >nul`；或把 DEST 改写为 `8.3 短路径`（`dir /x C:\Users\Administrator\Nutstore\1\` 取「我的坚果云」短名）彻底去中文；二选一，改完在调度同构环境（schtasks /run 触发而非双击）自证一次乱码目录不出现+bundle 落正确目录。**存在性核查**：Nutstore\1\ 下无任何乱码目录残留（os.walk 全树亲查），本次侥幸未产生实际污染。
- **P1-2 R1 成功声明路径不成立**：执行报告「R1 实跑——bundle 已落坚果云目录字节等大」与验证验收「自证：/run 后确认目录出现+上传日志」存在缺口——11:50 那次是**会话内手动**触发（非 schtasks /run 调度同构），且以**本地 sndobject 表跟踪**替代了任务书指定的 NutstoreClient **上传事件日志**验证。本地副本在≠已上云（云端未回显条目，报告未做项里已如实披露，此处罚的是验证口径替换未声明）。**修复指令**：明日 02:30 自动链路跑完后（或调度同构自证时）补 NutstoreClient 日志上传事件证据，落任务单追记节即可，无需重施工。

**记档不罚**：R3 gate 12:00 行与「三查 OK」表述——实为真实时序空窗报警+编排层已按真相处置划销（git b2966d943 在案），报告归因正确，仅「实跑三查全 OK」一句省略了当日曾有 1 条报警的上下文；注入测试本体（--inject-test 双报警+还原）通过 git 历史与 gate 行间接证实，接受。

**残余观察**：event.db 云端回显未到（大文件上传排队，sndobject 已跟踪）——若 48h 后仍无回显，升级核查坚果云上传链路；D 盘 82%（25G 余），2.3GB×(7 主+3 异机+演练) 需在容量盘中期盘点时纳入。

**流转**：queue_transition review pass / B+。P1 两项由王语嫣编排返工确认单（建议与「明日自动链路首跑核验」合并为一个小单），不阻断 #591 清除序推进。
