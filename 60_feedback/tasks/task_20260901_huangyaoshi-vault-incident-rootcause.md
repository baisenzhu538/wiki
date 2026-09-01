---
id: '589'
title: vault 整树消失事故根因排查+防再发（08-31 02:00 目录级清空）
type: investigation
status: in_progress
priority: P0
assignee: 黄药师
created_by: 王语嫣
created_at: 2026-09-01
updated_at: '2026-09-01T01:03:35.944738+00:00'
source_refs:
- 90_control/todos/wangyuyan.md 08-31 02:15 事故记录
- 90_control/scripts/queue_transition.py 旁证链
instance: huangyaoshi
---

# #589 vault 整树消失事故根因排查+防再发

## 背景（事故已恢复，数据无损失）

08-31 02:00 前后，`C:\Users\Administrator\Desktop\wiki`（24811 跟踪文件）整树消失，根 git 元数据（HEAD/refs/config/index）被掏空，仅剩 4503 个 loose objects；`.git/objects/info` 目录 mtime=08-31 02:00（目录级重建痕迹，内部 commit-graph 文件还是 08-25 22:20 的老文件）。王语嫣值守拍 02:15 发现，纯 Python 扫 loose objects 定位 commit 2764248716（01:31:49），手工重建 HEAD/refs + read-tree/checkout-index 全量恢复，git status 干净。bundle 备份 verify PASS（D:\KDO-memory\wiki-bundle-20260831-0215.bundle，HEAD=2764248716）。

**老朱 09-01 线索：前天（08-30）可能也发生过同类事故——是否同源待查。**

## 编排层已查的初步证据（2026-09-01 08:45-09:00 王语嫣，供接单参考）

1. **git 层无 08-30 事故痕迹**：todos 链 08-30 全天连续（11:11→22:57）；reflog 无 08-30 凌晨活动；全史 >3h commit 空洞清单里 08-30 00:37→13:24 有 12.8h 空洞，但当时（08-29 停时钟架构生效后）凌晨静默属正常，空洞≠消失。前天是否真发生，需非 git 证据源对齐。
2. **坚果云（Nutstore）头号嫌疑**：本机正在运行（NutstoreClient/nutstore_watchdog 等全家族进程，日志写至 09-01 06:57）。同步沙箱含 `Desktop\agent复盘`（id=30178085）和 `Knowledge Delivery OS 0.0.1`；日志实证它连 git 内部都碰（`OS 0.0.1\.git\refs\heads\main.lock` set-in-sync 报错、rm.exe 删除 agent复盘文件被 UpstreamDeleteProcessor 上传同步）。wiki 本体**未出现在**已知沙箱清单（NsConfig.json grep 无 wiki 命中），但沙箱全量清单只核了两个日志样本+部分配置，未穷尽。
3. **事故操作模式与同步盘处理 .git 冲突高度同型**：掏空 .git 元数据+目录级重建 objects/info，正是同步盘处理 git 仓冲突/锁文件的典型行为面。
4. **时间点规律待证**：02:00 是否为某计划任务/同步任务触发点，未定位到确切触发源（计划任务 CSV 全量含 02:00:00 的行只有系统杂项；git maintenance 无配置；无 git 类系统任务）。

## 任务

1. **证据考古**（按优先级）：
   a. NTFS USN Journal：`fsutil usn readjournal C:` 查 08-31 01:50-02:15 对 `Desktop\wiki` 的删除/改名记录（USN 保留期可能已过，尽力而为）
   b. 事件查看器：System/Application 日志 08-30 与 08-31 的 02:00 前后（杀软扫描、服务启动、计划任务触发事件）
   c. 坚果云深挖：沙箱全量清单（NsConfig.json + db1 + 服务端）、历史滚动日志（当前 log 仅覆盖 08-27 23:25 后）、**坚果云云端回收站/文件历史**（若 wiki 曾在同步范围，云端可能有快照）、08-30/08-31 凌晨它在本机干了什么
   d. Windows 计划任务全量筛查（「下次运行时间」列精确=02:00 的任务）
   e. 回收站（$RECYCLE.BIN）08-31 02:00 前后删除记录
   f. File History 是否启用及其备份范围
2. **前天对齐**：用 b/c/f 的日志回查 08-30 凌晨是否有同类事件；结果无论阴阳都记录（阳=同源实锤；阴=老朱印象的现象另行对齐，编排层会向老朱要当时现象）
3. **根因定性**：谁/什么机制/为什么 02:00/是否与前天同源。可复现给复现路径；不可复现给排除清单（每个候选附排除证据）
4. **防再发方案落地**（本单必交付，不等根因）：
   - wiki 每日自动 bundle 备份计划任务（参照 wiki-bundle-20260831-0215.bundle 打法，S4U 无窗，存 D:\KDO-memory\，建议保留 ≥7 份滚动）
   - 若根因锁定同步盘类机制：给出 wiki 防护建议（移出风险区/白名单/监控）

## 验证分层

- **实跑验证**：每条证据链给出原始命令+输出摘录（USN/事件ID/日志行号），不接受「查过了没有」式结论
- **备份验证**：bundle 计划任务注册后手动 /run 实跑一次，产物 verify 通过（git bundle verify + HEAD 比对）

## 边界

- 不改 30_wiki/60_feedback 内容；不重装/卸载坚果云（查证优先，处置方案另报老朱拍板）
- 数据恢复已完成，本单不重复恢复动作

## 关联

- #584/#585/#586 均在事故后恢复的树上施工，全链闭环
- 停车场 O-18（黄药师名下既有待办）不阻塞本单

## 需要谁动作

- 老朱：前天（08-30）事故的现象/大概时间点（若记得）——供「前天对齐」交叉验证
- 欧阳锋：排查报告+防再发交付后终审

## 执行报告

（完工后填写）

## 编排层补充（2026-09-01 09:40 老朱反馈）

老朱原话：「前天或者大前天了，不记得具体时间」——即嫌疑窗口放宽为 **08-29 或 08-30**。任务第 2 条「前天对齐」的回查范围相应扩为 08-29+08-30 两个凌晨（事件日志/坚果云历史/File History 同样双日回查），阴阳结果都记录。
