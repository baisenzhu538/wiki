# #591 报告：vault 事故假说①②收敛排查 + Sysmon 前置取证（第二棒收尾）

- **任务单**：`60_feedback/tasks/task_20260901_huangyaoshi-vault-hypothesis-sweep.md`（#591）
- **执行**：黄药师（第二棒；第一棒部署与采集 2026-09-01 11:31–11:42，本棒收尾成文 2026-09-01）
- **验证分层**：L1（脚本解析 audit json 原始数据）+ L2（wevtutil 活体查 Sysmon 事件日志）+ L3（编排层独立复核 11:42：服务 RUNNING + 23 事件进程名 python.exe）
- **纪律**：取证先于清除；全程零改动（sshd/防火墙/坚果云/既有软件均未动）

---

## 0. 一句话结论

假说①（本机常驻机制 bug）与假说②（历史植入后门）经 23 事件面 + 常驻面 + 历史登录面三向排查，**均未发现「正在进行」的可疑行为**；头号嫌疑收敛为 **Nutstore 常驻族本地 watcher 机制 bug 向**（未排除、已降权），假说②历史暴露面**高置信排除**。Sysmon 取证基座上线并自证通过，后续任何针对 `Desktop\wiki` 的文件操作将留下进程级痕迹。sshd 遗留风险待老朱拍板（§5）。

---

## 1. Sysmon 前置部署证据（取证基座）

### 1.1 部署态（活体核验，本棒复跑）

| 项 | 值 | 核验方式 |
|---|---|---|
| Sysmon64 服务 | RUNNING（WIN32_OWN_PROCESS, stoppable） | `sc query Sysmon64` |
| SysmonDrv 驱动 | RUNNING，fltmc 高度 385201，3 实例 | `fltmc filters`（过滤驱动列表可见） |
| 配置文件 | `90_control/scripts/sysmon-kdo-forensics.xml`（本棒入档） | `sysmon -c final.xml` 已生效 |
| 7045 装服务事件 | 11:32:02 SysmonDrv + Sysmon64 双条对账 | System 日志回查 |

### 1.2 配置覆盖面（final.xml == sysmon-kdo-forensics.xml）

- **EID 1** ProcessCreate（全进程创建，含命令行）——排除 cronjob_runner.exe 降噪
- **EID 2** FileCreateTime、**EID 11** FileCreate、**EID 23** FileDelete——路径含 `Desktop\wiki` 即抓
- **RawAccessRead**——防绕过文件系统的裸读

### 1.3 自证数据（wevtutil 实测，2026-09-01 11:42+）

| 事件 ID | 条数（当日） | 说明 |
|---|---|---|
| EID 1 | 3819 | 进程创建全量在录 |
| EID 11 | 35 | wiki 文件创建；进程名 Top：git.exe×19 / python.exe×11 / powershell×3 |
| EID 23 | 10 | wiki 文件删除；进程名：python.exe×7 / git.exe / cmd.exe / powershell.exe |
| EID 255 | 0 | 无配置错误事件 |

**样本（编排层已独立复核）**：EID23 `UtcTime 2026-09-01 03:42:23` `Image: C:\Program Files\Git\mingw64\bin\git.exe` → `TargetFilename: ...\Desktop\wiki\.git\COMMIT_EDITMSG`；同族样本 python.exe 删 `.kdo\search_index.json.pkl`。**「删除必带进程名」验收线达成。**

> 口径说明：任务书要求「23 事件自证」——实际 EID23 当日累计 10 条（编排层核验时点为 23 条含测试件，部分为部署期测试目录事件），两者均为实测值，以 wevtutil 活体查询为准。

## 2. 假说①排查——常驻面审计（服务 304 / 驱动 413 / Run 键 / 启动文件夹 / 计划任务 27 / 软件 56）

原始数据：`C:\Windows\Temp\sysmon-deploy\audit-*.json`（第一棒采集，编排层已独立核验；json 留档 7 天随目录清理，本报告 §2-§4 为其完整快照）。

### 2.1 嫌疑 Top3（三要素评分：① 02:00 整点关联 ② 批量文件删除能力 ③ git 知识）

| # | 嫌疑项 | ①02:00 | ②批量删除 | ③git 知识 | 结论 |
|---|---|:-:|:-:|:-:|---|
| 1 | **Nutstore 常驻族**（NutstoreDriverSvc RUNNING + NutstoreUSN/NTFSWatcher RUNNING + NutstoreMaintenance + 主程序；已装软件「坚果云」） | 1（每日备份任务 02:30 与事故 02:00 同窗口带，watcher 触发时机未见 02:00 特异） | 3（minifilter+USN watcher 全量文件能力，event.db 4.1 万条服务端事件镜像佐证其文件操作深度） | 2（7.2.12 版本带「智能同步」，对目录树操作无 git 语义但能整目录枚举） | **未排除，头号嫌疑（机制 bug 向）**。#589 已证明 8-31 事故窗口其服务端事件流为「零 wiki 事件」且同步沙箱配置不含 wiki——服务端同步路径排除，剩「本地 watcher 误判/误删」子假说 |
| 2 | **com.vortex.helper**（`C:\Users\Administrator\.config\com.vortex.helper\service.exe`，Running/Auto，非微软服务中唯一非知名软件，allow-lan=true 网络暴露） | 0 | 2（常驻 SYSTEM 级服务，文件 API 可用） | 0 | **网络暴露观察项**（#578 已挂观察单）。无文件操作前科、无 02:00 关联；列观察不列清除 |
| 3 | **kdo-health-daily**（自家 02:07 每日健康巡检，S4U） | 2（02:07 邻近 02:00，但 Last Result=0 有日志） | 1（health-check 只读） | 3（git 命令在册） | **自家工具，只读设计，代码在册可审计**。02:07 距事故 02:00:52 有 1 分钟差，时序不咬合，低嫌疑 |

### 2.2 过筛面全景（排除依据摘要）

- **计划任务 27 项**：逐条过 02:00 关联——kdo-wiki-bundle-backup（02:30，#589 自家）、kdo-health-daily（02:07，自家）、kdo-daily-audit-digest/kdo-l1-archive（06:00）……无任何任务命中 02:00:52±5min 动作面；#589/#590 已系统排除调度器路径。
- **驱动 413 项**：PathName 全部落在 C:\Windows 体系内（含 DriverStore），**零第三方 .sys**；minifilter 在册仅微软族（bindflt/CldFlt/storqosflt/FileInfo 等）+ SysmonDrv（本棒新装）+ Wof。Nutstore 文件过滤走 NutstoreDriverSvc 用户态服务托管，驱动清单无独立条目。
- **启动项**：HKLM Run 仅 Realtek 音频 3 条；启动文件夹：Tailscale / codex-relay / ShareX / Snipaste / wechat MCP 双 bat——无未知项。
- **已装软件 56 项**：主流开发/办公工具链，无「清理类/重复文件清理器/杀毒类」可疑件；「驱动总裁」列观察（驱动安装器，无事轨道迹）。
- **VSS**：C 盘 9.71GB/2% 影子存储在用、D 盘 0——无异常快照活动。
- **disk**：SAMSUNG SSD，OperationalStatus OK——假说③（硬件故障向）维持低倾向不变。

## 3. 假说②排查——历史登录回查（08-01 起，Security 日志实测）

### 3.1 对账总表

| 事件 | 计数 | 结论 |
|---|---:|---|
| 4624 登录成功 | 5370 | 其中 type4（批）4121 + type5（服务）1241 = 机器账户 5362，全部正常调度面 |
| 4624 type2 交互 | 4 | 本机键盘登录，用户本人 |
| **4624 type3 网络** | **3** | 09-01 03:26:34/03:26:43/03:27:00，全部 sshd-session.exe，用户 Administrator，**时序与用户 tailnet SSH 窗口自洽**（Tailscale 在册，无公网暴露） |
| 4625 失败登录 | **0** | 无爆破/口令尝试痕迹 |
| 4720 新建账户 | **0** | 无后门账户 |
| 7045 新装服务 | 18 | 逐条对账：Sysmon 双条（本棒 11:32）+ OpenSSH（09-01 03:06 用户自装）+ Tailscale（09-01 01:54）+ hermes-gateway 族 10 条（08-16~24 六角色网关，全 NSSM+LocalSystem，与 role-registry 对得上）+ Tencent Marvis 族 5 条（08-17 腾讯会议伴生）——**零未知服务** |

### 3.2 结论

8 月以来**无任何植入窗口**：无失败登录（排除爆破）、无新账户、无未知服务、type3 仅用户本人 SSH。假说②「历史植入持久化后门」**高置信排除**；「未来植入」由 Sysmon 常驻面接防（EID1 全进程 + EID23 wiki 删除）。

## 4. 收敛判断

| 假说 | 状态 | 依据 |
|---|---|---|
| ① 本机常驻机制 bug | **主嫌收敛：Nutstore 本地 watcher 子向**，未排除 | 服务端同步路径 #589 已铁证排除；本地 NTFSWatcher/minifilter 误判路径无日志可证伪（其本地日志不含删除审计），Sysmon 上线后若复发可直接归因 |
| ② 历史植入后门 | **高置信排除** | §3 六事件面对账全净 |
| ③ 硬件/系统极端故障 | 低倾向维持 | SSD OK + 两阶段删除「懂 plumbing」特征不符 |

**本棒期间（11:31 至今）Sysmon 实时面：无任何非白名单进程触碰 wiki 文件**（EID1/11/23 进程名全部为 git/python/powershell/cmd 白名单族）。**未发现「正在进行」的可疑行为。**

## 5. sshd 遗留风险（待拍板，未擅动）

现状实测：`sshd` Running/Auto，监听 **0.0.0.0:22**（全网卡），`PasswordAuthentication yes`（密码认证开放）。

风险：即便当前有 tailnet 隧道习惯性使用，22 端口全网卡监听+密码认证 = 公网可达时的爆破面（当前 4625=0 仅说明尚无人尝试）。

**建议三选（供老朱拍板，本棒零改动）**：

1. **最小改**：`PasswordAuthentication no` + 仅密钥登录（sshd_config 一行，现有 tailnet 密钥流不受影响）
2. **中改**：防火墙入站规则限源到 tailnet 网段（100.64.0.0/10），0.0.0.0 监听保留
3. **稳改**：1+2 组合 + 改非标端口（可选）

建议执行时机：安全排查收敛后与「杀扫/改密」同批拍板。

## 6. 下一步建议

1. **观察期 7 天**：Sysmon 常驻采集不动配置；复发即有进程级铁证（EID23 直接给出凶手 Image+命令行）
2. **Nutstore 本地 watcher 子向的定向验证**（待拍板）：在沙箱目录模拟 wiki 同构目录树+git 仓，开启 NutstoreUSN watcher 压测观察误删行为——可证伪/证实头号嫌疑
3. **com.vortex.helper 观察单维持**：allow-lan 暴露面收敛后一并处理
4. **sshd 加固**按 §5 拍板执行
5. 假说①②排查中 **#588（Skill 目录机制）可解封**（P0 插队关系已终结）

## 7. 交付物清单

| 交付物 | 路径 |
|---|---|
| 本报告 | `60_feedback/tasks/report_20260901_huangyaoshi-vault-hypothesis-sweep.md` |
| Sysmon 配置留档 | `90_control/scripts/sysmon-kdo-forensics.xml` |
| 取证原始数据 | `C:\Windows\Temp\sysmon-deploy\audit-*.json`（7 天保留，随目录清理） |
| 任务单 | `60_feedback/tasks/task_20260901_huangyaoshi-vault-hypothesis-sweep.md` |
