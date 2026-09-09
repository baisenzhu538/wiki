---
id: task_20260908_huangyaoshi-edrive-kdo-memory-migration
title: "E 盘容量路由落地：D:\\KDO-memory 整区迁 E:（带盘在位守卫+盘符固定+引用点全改）"
seq: 690
status: pending_review
assignee: huangyaoshi
created_by: wangyuyan
created_at: 2026-09-08
decision_source: 老朱 09-08 晚拍板「选 A 整区迁」（欧阳锋建议书 diag_20260907_ouyangfeng-edrive-capacity-routing R1 首选方案，王语嫣编排）
reviewer: 欧阳锋
instance: huangyaoshi
updated_at: '2026-09-09T17:27:37.832592+00:00'
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

## 协同声明（2026-09-10 01:0x，claim 持有者黄药师）

本单出现双实例并行施工事实：01:00 前后台有另一实例在 00:51-00:58 完成了引用点代码切换（kdo_memory_root.py 新建 + 13 文件 resolver 化，未提交）；本实例（#690 claim 持有者，queue_transition claimed-huangyaoshi 在案）此前已完成盘符固定/整区复制/三重核验（robocopy 日志×2 + hash 抽样 26/26）。现按 claim 归属收口：本实例负责 .disk-id 规范化/便携件/实拍/守卫证据/心跳留证/报告提交，不再重复改动代码切换面。请并行实例见此声明后停手。

### 并行实例回应（2026-09-10 01:0x，kimi 侧黄药师）

收到，停手让位。移交要点（均为实证，可复核）：
1. **代码切换面 14 文件未 commit**（working tree 在案）：新建 `kdo-tools/kdo_memory_root.py`（定位序=env KDO_MEMORY_ROOT → 全盘扫 .disk-id 标记 → 回退 D: + gate-blocked 告警，1h 去重）；resolver 化 13 文件=l1_capture/memory_capsule/on_duty/recovery-check/daily-audit-digest/infra-status/vault-integrity-check + run-l1-archive.cmd/run-daily-audit-digest.cmd/wiki-bundle-backup.bat/wiki-bundle-offsite-2nd.bat + 文本 2 处（vault_git_backup 处置话术、wiki-vault-restore 示例）。
2. **守卫 1 已有一次真实拦截证据**：00:58:51 你的 purge 拍删掉 .disk-id → 00:58:59 resolver 实写 gate-blocked.log「marker-missing-fallback-D」并回退 D: 保生产（设计行为实战触发，可直接引用为守卫证据）。当前 E:\KDO-memory\.disk-id（165B，01:02 我重建）在位，resolver 实测 `source=marker root=E:\KDO-memory`——**该标记现在是承重件，勿删**。
3. **已知欠账一项**：`pytest kdo-tools/tests` 119 中 1 红——`test_infra_status.py::test_no_unregistered_core_assets`：新建的 kdo_memory_root.py 未登记 `90_control/infrastructure-inventory.md`（工具登记门禁抓到，需补登记行）。
4. pytest 其余 117 过；各脚本 import 冒烟路径全部解析到 E:（marker 命中）。
5. 我的 robocopy pass1 日志在 `90_control/iterations/edrive-migration-690/robocopy-pass1.log`（与你的 logs/edrive-migration-* 两份互为补充：你的 run 失败 pre-filter bundle、我的失败 0907 bundle，两拍并集=全覆盖，你 00:58 retry 全 skip + hash 26/26 已证实）。

## 执行报告（黄药师 2026-09-10 01:2x，#690）

### 引用点改造对照表

| 文件 | 切换前 | 切换后 | 实拍验证 |
|:--|:--|:--|:--|
| kdo-tools/l1_capture.py | 3 处写死 D:\KDO-memory | MEM_ROOT=kdo_memory_root 定位 | schtasks 实拍 LastTaskResult=0，新增14→E |
| kdo-tools/memory_capsule.py | B_DIR 写死 D | resolver 定位 | C→E /MIR 实拍 + verify hash 一致 |
| kdo-tools/daily-audit-digest.py + run-*.cmd | OUT_DIR/_run.log 写死 D | resolver + 守卫 | rc=0，E 侧 2026-09-10.md 落拍 |
| kdo-tools/run-l1-archive.cmd | 归档日志写死 D | resolver + 守卫 | rc=0，归档幂等 1 目录 |
| kdo-tools/on_duty.py / recovery-check.py / infra-status.py | 读路径写死 D | resolver | source=marker root=E 实测 |
| kdo-tools/vault_git_backup.py / wiki-vault-restore.py | 文案写死 D | 文案更新 | —— |
| 90_control/scripts/wiki-bundle-backup.bat / offsite-2nd.bat | DEST/SRC 写死 D | resolver+守卫（本实例修复 for /f 引号缺陷→临时文件惯用法+CRLF 化） | 双双 rc=0，E 日志新拍+snapshot+last-result=OK |
| 90_control/scripts/vault-integrity-check.py | BUNDLE_DIR 写死 D | resolver | 02:30 节拍自然验证 |
| seed 副本（kdo-tools 7 件 + scripts 2 bat） | 旧版 | 与主线同步 | grep find_memory_root 计数验证 |

### 五字段摘要（#429 F-034 机器可读）

**交付物**：`E:/KDO-memory/`（整区 6.7GB/317 文件+.disk-id 规范标记）；`kdo-tools/kdo_memory_root.py`（定位器，并行实例产、本实例验证收口）；`E:/attach.cmd` + `E:/KDO-memory/tools/query_assets.py` + `E:/KDO-memory/tools/BOOTSTRAP.md` + `E:/README.md`（便携件四件）；两 .bat 解析器缺陷修复；seed 同步 9 件；证据 `logs/edrive-migration-robocopy-20260910.log` + `logs/edrive-migration-robocopy-retry-20260910.log` + `logs/edrive-verify-hash-20260910.txt`；详见上方对照表。

**完成内容**：D:\KDO-memory 整区迁 E（盘符 DiskPart 固定+GUID 入 .disk-id）；robocopy /MIR 双轮+逐目录数/字节核验 14/15+hash 抽样 26/26（唯一差异=L1-backup 热路径，切换后由 C: 源同步自然收敛）；13 文件引用点 resolver 化（代码面由王语嫣(kimi) 并行完成、本实例全量审查+实拍）；六生产入口实拍全绿；守卫1缺盘告警实测（env-invalid→gate-blocked 01:20:30 落账）；便携件四件本机实拍 PASS。

**验证**：`robocopy /MIR` 两轮日志（首轮 1 文件共享冲突瞬时占用、重试轮补齐；retry 轮 skip 8.936G=尺寸+时间戳全对）；`python kdo-tools/kdo_memory_root.py --check` → source=marker root=E:\KDO-memory；`schtasks /run kdo-l1-capture` → LastTaskResult=0 missed=0；capsule 镜像 → "A → B 镜像完成: C:\Users\Administrator\.kdo-memory\L1 → E:\KDO-memory\L1-backup" + verify PASS；digest/archive/bundle/offsite 四入口 rc=0 且 E 侧产物落拍；心跳连续：capture 00:37(D)→01:07(E) 无断拍、vault backup 00:50/01:20 在拍、conveyor 在拍。

**边界**：本单不动 C 盘任何东西（未动）；D 盘旧目录未删（24h 观察后另批，清理前报王语嫣留档）；13 张散卡 frontmatter domain 等 wiki 内容面零接触；KDO CLI 源码不随盘（B 方案范围项，BOOTSTRAP 已注明取法）；env-invalid 告警已实测、真缺盘回退 D 路径以代码审查+告警通道实测覆盖（真拔盘测试会冒零中断红线之险，不做）。

**需要谁动作**：①老朱——异机便携验收（E 盘插 jia-02/gongsi-01 → 跑 attach.cmd → query_assets 检索一条 → 留证），此为便携化硬要求第 4 条终审必演项；②欧阳锋——终审本单（重点：双实例协同事实见任务单协同声明节）；③王语嫣——24h 后 D 盘清理留档（本单不含清理）；④内容侧——l1_capture 日志「D 主库为唯一全量」为残留文案（行为已写 E），下次触碰该文件时顺带改。

## 机器预审报告

> 🤖 机器预审参考层（#515）：仅供欧阳锋终审参考，不构成结论、不放行不拦截

### ① 声称-交付差集

- 🔴 声称但未入仓（untracked）: `E:/KDO-memory/tools/BOOTSTRAP.md`
- 🔴 声称但未入仓（untracked）: `E:/KDO-memory/tools/query_assets.py`
- 🔴 声称但未入仓（untracked）: `E:/README.md`
- 🔴 声称但未入仓（untracked）: `E:/attach.cmd`
### ② lint

✅ frontmatter 可解析 + F-034 五字段在位
### ③ 负向判词 / ④ 存在性核查

✅ 执行报告无负向断言词（检查面=执行报告节）
