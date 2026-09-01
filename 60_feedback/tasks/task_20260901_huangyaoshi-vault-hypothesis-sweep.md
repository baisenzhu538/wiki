---
id: '591'
title: vault 事故假说①②收敛排查+Sysmon 前置取证（取证先于清除）
type: investigation
status: reviewed
reviewed_by: 欧阳锋
review_date: '2026-09-01'
grade: A-
priority: P0
assignee: 黄药师
created_by: 王语嫣
created_at: 2026-09-01
updated_at: '2026-09-01T05:14:00.786328+00:00'
source_refs:
- 60_feedback/tasks/report_20260901_huangyaoshi-vault-incident-candidate-b.md（#590
  PASS A-）
- 90_control/todos/wangyuyan.md 2026-09-01 编排层取证记录
instance: huangyaoshi
evidence: 60_feedback/tasks/report_20260901_huangyaoshi-vault-hypothesis-sweep.md
---

# #591 假说收敛排查+Sysmon 前置取证（老朱 09-01 直令「立项」）

## 背景

#589/#590 已排除：坚果云（本端+配置全量）、计划任务、Windows 调度器、本机 agent 会话、RDP（关闭，3389 无监听）、事故窗口登录面（44 条全为机器账户类型 4/5，零交互/零远程/零失败）。剩余假说（王语嫣 09-01 编排层分析）：

- **假说①（最重）**：本机常驻软件/驱动/服务的「本地同步/清理/杀毒/备份轮换」类机制出 bug——不需要登录、SYSTEM 权限、原生 API 批量能力全吻合
- **假说②（次要）**：历史暴露面（8 月早些时候）植入的持久化后门，自带定时器触发
- **假说③（低）**：系统/磁盘类故障极端形态——两阶段+懂 plumbing 特征过「聪明」，低倾向不排除

## 任务

1. **Sysmon 前置部署（第一优先，取证基座）**：下载 Sysinternals Sysmon（官方 swiftlane 或微软文档配置），安装配置覆盖 Event ID 1（进程创建含命令行）/2（文件时间戳）/11（文件创建）/23（文件删除，含进程名！）+文件删除 SACL 审计（auditpol + 对 Desktop\wiki 配置）——**装完自证**：生成一个测试目录做一次删除，确认 23 事件抓到进程名，随后清理测试痕迹。配置落 90_control/scripts/ 留档
2. **假说①排查——常驻面审计**：全机服务（sc query type= service state= all）+驱动（driverquery）+启动项（HKLM/HKCU Run、启动文件夹）+已装软件清单，按「02:00 整点相关/文件系统过滤驱动/云同步类/清理类/备份轮换类」过筛，列出嫌疑 Top10+每个的排除/存疑依据。重点排查：WPS 云/360 族/各类网盘驱动（云桥式）/系统还原点配置/存储空间/重复文件清理器
3. **假说②排查——历史登录回查**：08-01 以来全部 4624（类型 3 网络/10 远程桌面/8 网络明文）+4625 失败+4720 新建账户+7045 新装服务，异常项逐条给结论
4. **输出**：报告 `60_feedback/tasks/report_20260901_huangyaoshi-vault-hypothesis-sweep.md`——假说①②证据链+嫌疑清单+Sysmon 部署证据（含自证事件）+下一步建议

## 验证分层

- Sysmon 自证必须有实测 23 事件截图/文本输出（含进程名），不接受「已安装」
- 假说①嫌疑清单每项给「三要素符合度」评分（02:00 关联/批量删除能力/git 知识），不列空泛名单
- 历史登录回查给原始事件计数+异常项逐条分析

## 边界

- 不执行杀扫/改密（等 Sysmon 落地+假说收敛后老朱再拍板清除序）
- 不卸载/停用任何既有软件（只查证；确需停服验证的，报告里列建议待拍板）
- #588（Skill 目录机制）排队在本单之后——本单 P0 插队，领单序=本单先

## 需要谁动作

- 欧阳锋：终审
- 老朱：报告出来后拍板清除序（杀扫/改密/卸载嫌疑软件）

## 执行报告

**文件清单**：`60_feedback/tasks/report_20260901_huangyaoshi-vault-hypothesis-sweep.md`（新建，假说①②收敛报告：Sysmon 部署证据+嫌疑 Top3 三要素评分+历史登录对账+sshd 建议）；`90_control/scripts/sysmon-kdo-forensics.xml`（第一棒产出，本棒入档 commit）。

**完成内容**：第一棒已交付 Sysmon64+SysmonDrv 部署与常驻面/登录面原始取证数据；本棒解析成文——假说①嫌疑收敛 Nutstore 本地 watcher 子向（服务端路径 #589 已排除）、假说②历史植入高置信排除（4625=0/4720=0/7045 18 条全对账）、sshd 0.0.0.0:22+密码认证遗留风险三项方案待老朱拍板（本棒零改动）。

**验证**：L1 脚本解析 5 份 audit json（服务 304/驱动 413/任务 27/软件 56）；L2 wevtutil 活体查 Sysmon 日志（EID1=3819/EID11=35/EID23=10，删除事件带进程名）；L3 编排层独立复核（服务 RUNNING+23 事件 python.exe）。

**未做项**：sshd/防火墙/坚果云零改动（全走建议）；Nutstore watcher 压测验证待另单拍板；#588 解封建议已写入报告 §6。

**边界**：取证先于清除——未执行杀扫/改密/卸载；sshd/防火墙/坚果云配置零改动。

**需要谁动作**：欧阳锋终审本单；老朱拍板 sshd 加固方案（报告 §5 三选一）与 Nutstore watcher 压测验证立项（报告 §6.2）。

## 机器预审报告

> 🤖 机器预审参考层（#515）：仅供欧阳锋终审参考，不构成结论、不放行不拦截

### ① 声称-交付差集

✅ 2 个声明路径全部存在+已跟踪+无脏改动
### ② lint

✅ frontmatter 可解析 + F-034 五字段在位
### ③ 负向判词 / ④ 存在性核查

✅ 执行报告无负向断言词（检查面=执行报告节）

## 终审记录（2026-09-01 欧阳锋 · PASS A-）

**结论**：PASS A-。取证链全部 O3 独立复跑成立，边界纪律（零改动）守住，假说收敛判断方向正确。

**独立复跑清单（全部亲跑，非采信报告）**：

| 验收点 | 报告声称 | 我侧实测 | 判定 |
|---|---|---|---|
| Sysmon 服务/驱动 | 双 RUNNING | sc query Sysmon64=RUNNING、fltmc 驱动在册 | ✅ |
| 配置一致性 | final.xml==sysmon-kdo-forensics.xml | 活体 `sysmon64 -c` SHA256=D15D516E…2ACF == 入库 xml 哈希 == final.xml 哈希，三者字节同源 | ✅ |
| EID23 带进程名 | 10 条（git/python 白名单族） | 亲抓：git.exe→COMMIT_EDITMSG、python.exe→production-queue.md 等样本；当日计数 EID1=7773/EID11=249/EID23=55/EID255=0（较报告 11:42 时点持续增长=常驻采集中） | ✅ |
| 7045 对账 | 18 条零未知 | 全量导出逐条：Sysmon×2(11:32)+OpenSSH(03:06)+Tailscale(01:54)+hermes-gateway×10(08-16~24)+Tencent Marvis 族×5(08-17)=18，与 role-registry/用户自装窗口吻合 | ✅ |
| 4625/4720 | 0/0 | PowerShell Security 日志 08-01 起实测均 0 | ✅ |
| 4624 type3 | 3 条 sshd-session | 逐条 XML 字段：03:26:34/03:26:43/03:27:00，ProcessName=C:\Program Files\OpenSSH\sshd-session.exe，用户 Administrator | ✅ |
| 常驻面计数 | 服务304/驱动413/任务27/软件56 | audit json（utf-8-sig 解码亲数）304/413/27/56 一致；413 驱动 PathName 全 Windows 体系、非标位置 .sys=0；HKLM Run=Realtek×3、启动文件夹 Tailscale/codex-relay/ShareX/Snipaste/wechat×2 与报告逐条对上 | ✅ |
| Nutstore 头号嫌疑面 | DriverSvc+USN RUNNING | Get-Service 双 Running+5 进程活体（bin-7.2.12） | ✅ |

**口径区分裁定（核验要点②）**：成立。#589 排除的是**服务端事件面**（event.db 零 wiki 事件+同步沙箱不含 wiki→服务端同步路径死），而 NutstoreUSN/minifilter 的**本地引擎误判**不产生服务端事件记录，属未被排除的独立向量——报告把两者分开、头号嫌疑收敛到本地 watcher 子向且降权不排除，逻辑严密。Sysmon 上线后复发可归因，是正确的收敛姿态。

**缺陷记档（🟡 1 项，不阻塞但须修正认知）**：

**落点**：sshd 前提失实的正确执行序已并入终审汇报「给老朱的清除序最终建议」——待老朱拍板（先装公钥→验证密钥登录→再关密码认证）；#592 终审记录 P1-1 同款警示互链；EID23 口径以报告 §1.3 口径说明自洽收口，无需另单。

- §5 建议方案 1 的前提失实：「最小改 PasswordAuthentication no（现有 tailnet 密钥流不受影响）」——**存在性核查**：`C:\ProgramData\ssh\` 无 administrators_authorized_keys、`~/.ssh\` 无 authorized_keys（ls 实测均不存在）、known_hosts 仅为客户端侧；服务端信任公钥为空集 → 现有 type3 访问实际走的就是密码认证。直接执行方案 1 = SSH 锁死。正确序：先装公钥→密钥登录验证通过→再关密码认证。已并入给老朱的清除序最终建议。

**🟡 小疵**：EID23 计数口径（编排层 23 vs 本棒 10）已自附口径说明，以 wevtutil 活体为准，不降级。

**残余风险**：假说①未排除（Nutstore watcher 压测验证待另单）；观察期 7 天内 Sysmon 配置勿动。#588 解封建议成立（P0 插队关系已终结）。

**流转**：queue_transition review pass / A-。
