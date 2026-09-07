---
id: diag_20260907_ouyangfeng-edrive-capacity-routing
title: 新增 E 盘（移动硬盘 160GB）容量路由建议——迁移候选排序 + 移动盘脚本守卫三条
type: proposal
status: pending_orchestration
audience: 王语嫣
author: 欧阳锋
created_at: '2026-09-07'
---

# 建议书：E 盘（新移动硬盘）容量路由——迁什么、怎么迁才不踩坑

## 现象一句话
老朱因担心未来空间不足加装移动硬盘 E 盘（160GB NTFS 全空）；实测该盘初接上时**系统存储层未枚举**（Get-Volume/Get-Disk 均不可见，仅 PnP/PhysicalDisk 层可见），`Update-HostStorageCache` 刷新后才联机挂载 E:——移动硬盘作为调度写入目标存在「缓存陈旧/休眠离线」可用性风险，任何迁到 E: 的自动化（备份/归档）必须带盘在位守卫。

## 在哪发现
2026-09-07 23:13-23:30 CLI 会话实测：`Get-Disk` 仅 Disk 0（三星 NVMe），`Get-PhysicalDisk`/`Get-PnpDevice` 可见 Disk 1（JMicron USB 桥，Healthy）——刷新存储缓存后 Disk 1 Online（MBR，NTFS 整盘 160,038,907,904 字节）挂载 E:，卷标「新加卷」（中文）。

## 空间现状实测（2026-09-07 23:2x）
| 盘 | 总量 | 余量 | 用途/压力点 |
|:--|:--|:--|:--|
| C: | 347.5GB | 122GB | 系统盘：Nutstore 同步目录（含 offsite bundle 副本 keep 3 ≈6.3GB 滚动）、~/.claude、Desktop wiki 工作区（.git 2.1GB） |
| D: | 129.4GB | 100GB | **77% 已用，最紧**；KDO-memory 9GB = L1-full 热层 231MB（~70MB/天增长）+ L1-full-archive 1.1GB（~80MB/天）+ wiki bundle 2.1GB/周滚动（keep 2）+ obsidian-snapshot + codex-homes；另有 ~20GB 非工厂文件 |
| E: | 160GB | ~149GB 全空 | 新移动硬盘，当前零任务承载 |

## 建议方向
1. **R1 迁移候选排序**（供老朱拍板，备份拓扑属老朱裁定范围，同 #673 前例）：
   - 首选 **D:\KDO-memory 整区迁 E:**（9GB，工厂写入最频的档案区，一次腾出 D: 压力；L1 归档增长 ~29GB/年 + bundle 滚动 4.2GB，E: 独立承载最合适）
   - 次选仅迁 L1-full-archive（增长大头，1.1GB 起步）
   - 不建议动 C:（系统盘稳定优先；offsite 本地同步副本是 Nutstore 上传源，动它牵连云备份链）
2. **R2 盘在位守卫（迁任何自动化到 E: 前置硬条件）**：脚本写 E: 前先验卷存在（`if not exist E:\...` 或 #592 同款 ASCII junction 模式），写后校验产物存在+日志落结果文件；缺盘时**告警而非静默失败**（参照 #592「UTF-8 bat+中文路径+ACP936」静默失效三件套教训——缺盘是同族新增第四件：目标卷不在位）。
3. **R3 盘符漂移防护**：移动硬盘盘符可能被先插入的其他 USB 设备抢占（E:→F:）。建议 DiskPart 固定盘符（`assign letter=E` 一次性）或脚本按 volume GUID/junction 引用，不裸写盘符。
4. **R4 卷标中文规避**：E 盘卷标「新加卷」为中文——一切 bat/调度引用只用盘符或 junction 路径，**禁止引用卷标**（#592 编码教训直接复用）。
5. **R5 接入感知**：本次「初插未枚举、刷新缓存才可见」若发生在 02:30 调度窗口=静默失败。kdo-l1-capture/bundle 等任务的 last-result 校验文件机制（#589 已有）保持，E: 相关新任务照抄该模式即可。

## 边界
E 盘当前空载、未承载任何任务，本建议书不迁移任何东西；迁移与否、迁哪个均待老朱拍板后再由王语嫣编排立项。空间数字为 23:2x 单点实测，趋势增长率取自当日值守拍（L1 热层 225.6→229.9MB/90min）与 bundle 滚动配置（keep 2），精确到量级即可。
