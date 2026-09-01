---
id: '589'
title: vault 整树消失事故根因排查+防再发（08-31 02:00 目录级清空）
type: investigation
status: pending_review
priority: P0
assignee: 黄药师
created_by: 王语嫣
created_at: 2026-09-01
updated_at: '2026-09-01T01:55:29.049923+00:00'
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

> 详情见 `60_feedback/tasks/report_20260901_huangyaoshi-vault-incident-rootcause.md`（两棒证据链合并）

- **文件清单**：
  - `60_feedback/tasks/report_20260901_huangyaoshi-vault-incident-rootcause.md`（根因报告，本棒新增）
  - `90_control/scripts/wiki-bundle-backup.bat`（每日 bundle 备份脚本，本棒新增）
  - 计划任务 `kdo-wiki-bundle-backup`（SYSTEM 身份注册，非文件，注册于任务计划程序库）
  - 运行留痕 `D:\KDO-memory\wiki-bundle-daily.log` + `wiki-bundle-daily.last-result.txt`（脚本产出，不入库）
  - 只读副本 `C:\Windows\TEMP\ns_probe\`（坚果云 nutstore.db/event.db 副本+探查脚本，原件未动）
- **完成内容**：
  1. 坚果云铁证收口：沙箱全量穷尽=4 个（无 wiki）+ event.db 41393 条服务端事件镜像全史零 wiki、事故窗口（08-31 01:30-02:15）零事件零删除 + 客户端主日志窗口静默——「同步盘机制」头号嫌疑高置信排除，定性降级；
  2. 影子仓同型掏空实锤（`wiki\wiki\.git` 只剩 objects、mtime 同为 02:00）——操作者 git-plumbing 感知的第二物证；
  3. 02:00 特异性排除：Windows 计划任务（第一棒 223 个）+ Hermes 全部 11 profile cron（无 02:00 表达式）+ 工具链自删路径 grep 零命中；
  4. 前天对齐扩展：event.db 08-29/08-30 双凌晨零事件（老朱线索窗口一并覆盖）；
  5. 防再发交付：每日 02:30 bundle 备份计划任务注册并 `schtasks /run` 实跑验证（Last Result=0，bundle verify PASS，HEAD=014daeec1 一致，滚动保留 7 份）；
  6. 债务汇总：Desktop 6 个 lint 基线孤儿 worktree + 影子仓路径清单入报告待拍板。
- **验证**：L1 证据链每条附原始命令+输出（报告第二节 16 条）；备份脚本前台实跑 EXIT=0 + 计划任务调度器实跑 Last Result=0（Last Run 09-01 09:47:34）+ `git bundle verify` "complete history" + HEAD 比对一致；回收站 `$Recycle.Bin` 08-31 窗口 0 文件实查补齐；L2 脚本为可恢复品标准（verify+HEAD 比对+FAIL 结果文件）；L3 明日 02:30 首次定时实跑待 log 留痕复核。
- **未做项**：
  1. 操作者进程名铁证（USN 机制不记进程，本机无文件删除审计/Sysmon——取证能力空白，非本单可补）；
  2. 坚果云云端回收站查询（本地无凭据，待老朱登录网页版确认，操作指引在报告七.1）；
  3. 债务清理（6 个孤儿 worktree+影子仓）——编排层留档待老朱拍板，本单不执行；
  4. Sysmon/删除审计加固建议——是否立项待编排层拍板。
- **需要谁动作**：
  - 老朱：登录坚果云网页版查云端回收站 08-31 01:30-02:30 有无 wiki 删除记录（指引：报告七.1，一行操作）；前天（08-29/08-30）印象中事故的现象/时间点仍待提供；
  - 欧阳锋：根因报告+防再发交付终审；
  - 编排层：USN dump 归档决策、影子仓取证 vs 清理拍板、审计加固是否立项。

## 编排层补充（2026-09-01 09:40 老朱反馈）

老朱原话：「前天或者大前天了，不记得具体时间」——即嫌疑窗口放宽为 **08-29 或 08-30**。任务第 2 条「前天对齐」的回查范围相应扩为 08-29+08-30 两个凌晨（事件日志/坚果云历史/File History 同样双日回查），阴阳结果都记录。

## 机器预审报告

> 🤖 机器预审参考层（#515）：仅供欧阳锋终审参考，不构成结论、不放行不拦截

### ① 声称-交付差集

- 🔴 声称但未入仓（untracked）: `D:/KDO-memory/wiki-bundle-daily.log`
### ② lint

✅ frontmatter 可解析 + F-034 五字段在位
### ③ 负向判词 / ④ 存在性核查

✅ 执行报告无负向断言词（检查面=执行报告节）
