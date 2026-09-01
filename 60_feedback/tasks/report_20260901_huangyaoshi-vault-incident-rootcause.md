---
id: report_20260901_huangyaoshi-vault-incident-rootcause
title: '#589 vault 整树消失事故根因排查报告（两棒证据链合并）'
type: investigation-report
status: submitted
author: 黄药师（Builder）
reviewed_by: ''
created_at: 2026-09-01
task_ref: 60_feedback/tasks/task_20260901_huangyaoshi-vault-incident-rootcause.md
---

# #589 vault 整树消失事故根因排查报告

> 08-31 02:00 前后 `Desktop\wiki` 整树消失（24811 跟踪文件+.git 元数据被掏空，仅剩 4503 loose objects），02:15 王语嫣发现并手工全量恢复，数据零损失。本报告合并两棒（USN 考古棒 + 坚果云深挖棒）全部证据，给出根因定性、排除清单、防再发交付物与剩余取证空白。

## 一、结论速览

1. **坚果云（头号嫌疑）高置信排除**：四沙箱全量穷尽无 wiki；本地 event.db 41393 条服务端事件镜像全史（05-17~09-01）零 wiki 路径、事故窗口（01:30-02:15）零事件零删除；客户端主日志事故窗口完全静默（仅 3 小时心跳）。**「同步盘机制」定性降级为低概率。**
2. **02:00 操作者是 git-plumbing 感知的定向掏空**：双仓同型（主仓 + 嵌套影子仓 `wiki\wiki\.git` 都只剩 objects、mtime 同为 02:00），精准保留 objects、销毁 refs/HEAD/config/index——傻子删除/杀毒隔离不会按 git 对象模型区分保留。
3. **时间点非任何调度器特异性**：Windows 计划任务 223 个全量无 02:00 精确触发、Hermes 全部 11 profile cron 无 02:00 表达式、工具链自删路径全 grep 零命中。02:00 更可能是**手工/交互式操作时刻**，而非定时器。
4. **唯一证据空白 = 操作者进程名**：NTFS USN 记录了完整的两阶段删除序列但不含进程归属（USN 机制本身不记进程），云端回收站需老朱登录确认（本地无凭据）。

## 二、证据链（两棒合并，原始命令+输出逐条）

### 第一棒（USN 考古，2026-09-01 上午）

| # | 证据 | 命令/来源 | 关键输出 |
|---|------|----------|---------|
| 1 | 两阶段删除序列 | `C:\Windows\TEMP\usn_full.txt`（1.15GB dump，fsutil usn readjournal） | 08-31 02:00-02:01：先 `.git` 元数据（HEAD/refs/config/index），后工作树顶层；单秒 264 项删除中**精确保留 objects** |
| 2 | Windows 计划任务全量排除 | `schtasks /query /fo csv /v` 全量 | 223 个任务 0 个 02:00:00 精确触发（02:00:00 行仅系统杂项） |
| 3 | 事件日志排除 | System/Application 08-30+08-31 02:00 前后 | 0 事件（无杀软扫描、无服务异常启动） |
| 4 | 08-30 凌晨双阴 | 事件日志+当时可知日志源 | 08-30 凌晨零同类事件（老朱印象的「前天」事故待其提供现象再对齐） |
| 5 | 恢复基线 | 王语嫣手工恢复 | commit 2764248716（01:31:49 时钟 v4.1 诊断交付提交），bundle 20260831-0215 verify PASS |

### 第二棒（坚果云深挖+防再发，2026-09-01 09:30-10:00）

| # | 证据 | 命令/来源 | 关键输出 |
|---|------|----------|---------|
| 6 | 沙箱全量穷尽 | `nutstore.db`（拷贝到 `C:\Windows\TEMP\ns_probe\` 只读查，原件未动）`config.all_sandbox_list` + 4×`sndobject*` 表 | **恰 4 个沙箱**：`Nutstore\1\我的坚果云`(29888283)、`Nutstore\1\共享文档`(30292216)、`Knowledge Delivery OS 0.0.1`(29888290)、`Desktop\agent复盘`(30178085)——**无 wiki** |
| 7 | 服务端事件镜像全史零 wiki | `event.db` event 表 41393 条（05-17~09-01），base64 path 全解码 grep | "wiki/desktop" 命中 47 条全部为 KDO0.0.1 沙箱内文件名（wikimedia.pyc、kdo-wiki-synthesis 等），**路径级 wiki 同步记录 0** |
| 8 | 事故窗口零事件 | event.db WHERE time BETWEEN 08-31 01:30 AND 02:15 | **0 条**（四沙箱均无任何服务端下发动作） |
| 9 | 客户端日志静默 | `Nutstore.Client.Wpf.log`（覆盖 08-27 23:25~09-01） | 08-31 全天仅 40 行：3 小时心跳（SQLOperator 备份/升级检查）+19:01 网络重连，**00:57→02:57 两小时空档** |
| 10 | NTFSWatcher 旁证 | `ProgramData\Nutstore\logs\nutstore_usn.log` | 08-26 22:57 起 watch C: 全盘，日志止于启动行（无 08-31 记录=无异常动作） |
| 11 | 前天对齐双阴扩展 | event.db 08-29/08-30 00:00-04:00 | 各 0 事件（08-29 老朱线索窗口一并覆盖） |
| 12 | Hermes cron 全扫 | 11 个 profile `cron/jobs.json` schedule_display 全列 | `*/15`（huangyaoshi/laowantong/laowantong-feishu）、`*/30`（wangyuyan/ouyangfeng）、周日/周一 9 点（其余 5 个）——**无 02:00 表达式** |
| 13 | 时钟活跃性确认 | todos 三角色 08-31 01:12-02:37 记录 | 01:31:49 时钟 v4.1 提交、02:11 王语嫣素材诊断、02:15 事故发现——**时钟拍在跑，事故发生在两拍之间** |
| 14 | 工具链自删排除 | vault+kdo-tools grep `rmtree/rm -rf/worktree`；KDO CLI `system.py:98-143` lint worktree 路径核读 | vault 内脚本零删除代码；`kdo_lint_baseline_*` worktree 建删路径都在仓库内部，**从不指向 Desktop 顶层** |
| 15 | 其他同步盘排除 | tasklist grep + HKLM/HKCU Run 键 | OneDrive/Dropbox/百度网盘/Seafile 等**零进程零自启**（全机唯一同步客户端=坚果云） |
| 16 | 影子仓同型掏空（新发现） | `Desktop\wiki\wiki\.git\` 实地查看 | 仅剩 `objects\` 目录，mtime=08-31 02:00——与主仓完全同型的掏空，**证明操作者按 .git 目录逐仓处理且懂 objects 价值** |

## 三、排除清单（每候选附排除证据）

| 候选 | 结论 | 排除证据 |
|------|------|---------|
| 坚果云同步删除 | **排除** | 证据 #6/#7/#8/#9：无沙箱、无事件、无日志 |
| 杀软/磁盘清理类计划任务 | **排除** | 证据 #2/#3：223 任务无 02:00 触发、事件日志零记录 |
| 其他同步盘 | **排除** | 证据 #15：本机无第二同步客户端 |
| Hermes/工具链定时器 | **排除** | 证据 #12/#14：无 02:00 cron；代码无指向 Desktop 的删除路径 |
| git 自身（maintenance/gc） | **排除** | 第一棒：无 maintenance 配置、无 git 类系统任务（gc 也不删工作树） |
| 误删（人工 Explorer/命令行误操作） | **部分排除** | 纯误删不会两阶段执行+跨仓精准保留 objects；但「知情者手工 git 命令序列」无法用本地证据排除（见四.3） |
| 回收站途径 | **排除** | 第一棒：$RECYCLE.BIN 无 08-31 02:00 记录（USN 直接 delete 语义，非回收站 rename 语义） |

## 四、根因定性（判定+置信度+差什么）

1. **判定**：08-31 02:00 的操作是一个**知晓 git 对象模型的进程/脚本/命令序列**，按「先元数据后工作树、逐仓保留 objects」的两阶段模式执行了目录级清空。**同步盘机制类成因被本棒证据高置信排除**（原头号嫌疑降级）。
2. **置信度声明**：行为画像（git 感知、两阶段、跨仓一致）置信度高（USN+双仓物证）；操作者身份置信度不足——USN Journal 机制不记录进程归属，本机又无文件删除审计（Sysmon/审核策略未开），**操作者进程名是当前唯一取不到的铁证**。
3. **三个候选残余**（按可能性排序）：
   - a. 未知的第三方进程（杀软误判 git objects 批处理/系统工具 bug）——但 02:00 触发点无任何调度器解释，且 264 项/秒的精准保留不像误判；
   - b. 本机某个 agent 会话执行了危险命令序列（02:00 恰在时钟活跃窗口内，02:11/02:15 都有 agent 活动）——**无法用本地日志排除，hermes 会话记录不落盘命令全文**；
   - c. 远程/共享访问（本机暴露面）——无证据，未深查。
4. **差一步铁证**：① 老朱登录坚果云云端回收站确认 wiki 是否曾在云端范围（服务端视角补刀，操作指引见七.1）；② 下次若再发，Sysmon Event ID 1（进程创建）+ 审核策略「删除文件」审计可直接给出进程名——建议作为独立加固单（不在本单范围）。

## 五、防再发交付物（已生效，实跑验证）

| 交付物 | 位置/标识 | 验证结果 |
|--------|----------|---------|
| 备份脚本 | `90_control/scripts/wiki-bundle-backup.bat` | 前台实跑 EXIT=0；bundle create+verify+HEAD 比对三步全过，任一步失败写 FAIL 结果文件+退出码 1 |
| 计划任务 | `kdo-wiki-bundle-backup`（每日 02:30 错开高危时段，SYSTEM 身份，StartWhenAvailable 错过补跑，ExecutionTimeLimit 2h） | `schtasks /run` 实跑：Last Run 2026/9/1 9:47:34、**Last Result 0**；产物 `D:\KDO-memory\wiki-bundle-20260901.bundle`（2.32GB）verify "complete history"、HEAD=014daeec1 与仓一致 |
| 滚动保留 | 脚本内置：按日期名倒序保留最新 7 份，超额删除并留痕 | 逻辑在脚本尾部 cleanup 段（当前 3 份未触发删除分支） |
| 运行留痕 | `D:\KDO-memory\wiki-bundle-daily.log` + `wiki-bundle-daily.last-result.txt` | 每次运行追加 OK/ERROR 行+结果文件，值守可巡检 |

> 注册说明：本会话令牌为 SYSTEM，向 Administrator 注册 S4U 任务被系统拒绝（含 PowerShell Register-ScheduledTask 同拒），任务改以 SYSTEM 身份注册——纯本地 git bundle 不需要用户上下文，行为等价。

## 六、债务登记（汇总路径清单，待老朱拍板，本单不执行清理）

1. **Desktop 6 个 `.kdo_lint_baseline_*` 残留工作树**（KDO CLI `kdo/commands/system.py` lint 基线检出实体，`git worktree` 管理元数据已随事故删除，实体成孤儿）：
   - `C:\Users\Administrator\Desktop\.kdo_lint_baseline_13664`
   - `C:\Users\Administrator\Desktop\.kdo_lint_baseline_23196`
   - `C:\Users\Administrator\Desktop\.kdo_lint_baseline_23756`
   - `C:\Users\Administrator\Desktop\.kdo_lint_baseline_24760`
   - `C:\Users\Administrator\Desktop\.kdo_lint_baseline_25092`
   - `C:\Users\Administrator\Desktop\.kdo_lint_baseline_37556`
2. **wiki 内嵌套影子仓 `Desktop\wiki\wiki\`**（仅 `index.md`/`log.md` + `.git\objects`）：`.git` 同样只剩 objects（mtime=08-31 02:00）——**同时是事故第二物证，取证价值高于清理价值**，建议归档取证后随 O-18 处置。

## 七、需要谁动作

1. **老朱（一行操作）**：浏览器登录坚果云网页版 → 右下角「回收站」→ 按时间倒序看 08-31 01:30-02:30 有无 `wiki` 相关删除记录；再查「我的坚果云/共享文档」目录树中有无 `wiki` 或 `Desktop` 字样目录（确认 wiki 是否曾在云端范围）。结果回填本单评论即可（有无都是关键证据）。
2. **欧阳锋**：本报告+防再发交付终审。
3. **编排层**：USN dump（`C:\Windows\TEMP\usn_full.txt` 1.15GB）归档决策；影子仓取证归档 vs 清理拍板；「开启 Sysmon/文件删除审计」加固建议是否立项。
4. **老朱（前天对齐）**：08-29/08-30「印象中事故」的现象/时间点仍缺——编排层已记录追问，拿到后可再对齐一轮（当前 event.db 双凌晨零事件已是阴性证据）。

## 八、验证分层声明

- L1（命令级）：本报告第二节每条证据附原始命令与输出，可独立复跑；备份脚本实跑 EXIT=0、schtasks Last Result=0。
- L2（狗粮级）：bundle 备份脚本本身以「恢复可用品」标准写（verify+HEAD 比对+结果文件），非一次性命令拼接；下次事故可用任一 bundle 一条命令重建。
- L3（活体级）：计划任务已由调度器真实触发一次（非仅前台手跑），明日 02:30 首次定时实跑后可在 log 留痕复核。
