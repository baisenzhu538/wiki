---
id: task_20260905_huangyaoshi-sysmon-cas-trace
title: C:\Sysmon 59G 内容寻址存储溯源与处置（已冻结改名止血；09-01 11:34 生，正值 #592 备份施工窗口）
seq: 646
status: reviewed
assignee: huangyaoshi
created_by: wangyuyan
created_at: 2026-09-05
decision_source: 老朱确认无印象（非他装）→ 王语嫣冻结止血（改名 Sysmon.frozen-20260905），写入者溯源归黄药师
reviewer: 欧阳锋
instance: huangyaoshi
disposal: true
updated_at: '2026-09-05T17:56:49.268238+00:00'
evidence: 60_feedback/tasks/task_20260905_huangyaoshi-sysmon-cas-trace.md
reviewed_by: 欧阳锋
review_date: '2026-09-05'
grade: A-
---

# #646 C:\Sysmon CAS 溯源与处置（黄药师）

## 背景（王语嫣 forensic 实证）

- C:\Sysmon = 59G 内容寻址存储：64-hex 大写平铺松散对象 + .pack/.idx/.rev（JGit DFS 形态）+ 检索索引快照 json（588MB 级）+ production-queue 锁 + #645 任务文本
- 目录创建于 2026-09-01 11:34——**正值 #592（异机备份三件套）施工窗口**（11:49 claim 起），头号嫌疑=备份/重建工具链的写路径指错
- 增长加速：09-03 起 +14350 文件
- 已冻结（改名 Sysmon.frozen-20260905）——若某工具报错找它，报错者=写入者

## 任务

1. **溯源**：查 #592 三件套脚本（vault-backup/vault-snapshot/vault-integrity-check/wiki-vault-restore）与坚果云同步链的写路径，找到把对象库写到 C:\Sysmon 的调用点（重点：路径变量拼接错误/环境变量默认值）
2. **处置**：确认可弃则删除 Sysmon.frozen-20260905（释放 59G）；若是某机制的"工作状态"，修复写路径指向正确位置后再清
3. 观察哨：冻结后 48h 内有工具报错找 Sysmon=写入者现行，优先走这条路收证据

## 交付

- 写入者结论（含证据）+ 处置结果（释放空间数）+ 执行报告
- claim/complete 走 queue_transition（complete 646）

## 执行报告（黄药师 2026-09-05 04:30）

**交付物**：①写入者结论+铁证链（下述）②Sysmon 修正配置热加载生效（活体 hash 7E41628D…）③仓库配置同步修正 `90_control/scripts/sysmon-kdo-forensics.xml`④处置完成：C:\Sysmon.frozen-20260905（27,714 文件）+ C:\Sysmon 全删，C 盘可用 51G→111G（释放 **60G**，占用 86%→69%）

**完成内容**：
- **写入者 = Sysmon64 自身的 EID23 归档机制，#592 三件套全部排除**。机制链：#591 取证配置 `sysmon-kdo-forensics.xml` 含 `<FileDelete onmatch="include">Desktop\wiki</FileDelete>`——Sysmon EID23 对命中的删除事件会把被删文件按 **SHA256大写+原扩展名** 归档进 ArchiveDir（默认=C:\Sysmon，活体配置 dump 实证 `Archive Directory: -` 即默认值）。vault 高频原子替换写入（git/python/kimi 的 write-tmp-rename）= 持续产生「删除」→ 每次替换留一份归档 → 4 天堆出 59G（内含 2.3GB git pack ×N 版、616MB kdo 索引快照 ×3 版等，每次 rebuild/repack 双倍计费）。
- #592 三件套+wiki-bundle-backup.bat 写路径逐一读码排除：vault-backup→~/kdo-backups、vault-integrity-check→gate-blocked.log、wiki-vault-restore→显式 target、vault-snapshot→90_control/vault-status.md、bundle.bat→D:\KDO-memory+坚果云，无一指向 C:\Sysmon。目录生于 09-01 11:34 是 #591 装 Sysmon+载配置的时点，与 #592（11:49 claim）窗口相邻纯属先后施工。
- 修复：FileDelete(EID23 带归档) → FileDeleteDetected(EID26 只记录不归档)，schema 升 4.90（FileDeleteDetected 在 4.22 下校验静默失败 exit 127——坑已避开）；删除检测能力（Image+TargetFilename）保留。
- 处置：两目录删除，内容全部为 vault 文件的被替换旧版本（git/vault 现行版全覆盖，零独有数据）。

**验证**（全部实跑）：
- 铁证1 USN：rename 对 `60_feedback\tasks\task_20260904_laowantong-transcript-to-qingdanti-skill.md`（父 FRN …0d7571=该目录实测）→ `C:\Sysmon\<SHA256>.md`（_tmp/646-usn-dump.csv 留档），vault 侧同名文件秒级重建（FRN …08f654=现行文件实测一致）
- 铁证2 EID23 活体：04:11-04:13 删除事件 Image=kimi.exe/git.exe/python.exe 与 CAS blob 落盘时刻逐条对齐
- 铁证3 内容：blob 文件名==内容 SHA256 大写（多文件实测）；blob=任务文件历史版本（sha 对账）
- 修复验证：配置热载后 vault 内造删测试文件 → EID26 抓到（rm.exe 带路径）、C:\Sysmon blob 计数 118→118 零增长
- 释放验证：df 51G→111G

**边界**：①Sysmon 日志只留 ~28min 窗口（EID 量大滚动快），历史 EID1 不可回查，靠 USN+活体陷阱补位；②EID26 不归档=被删文件内容不再留底，检测能力不变；若终审认为归档有价值可另议 ArchiveDir 指 D 盘；③冻结期观察哨无工具报错找 Sysmon，与「Sysmon 自身归档、无业务依赖」结论互洽；④老朱 PROTOCOL §7：本次删除对象=取证工具自身归档垃圾（非 vault 内容，git 全覆盖），任务单已授权「确认可弃则删除」，执行留痕于此。

**需要谁动作**：①欧阳锋终审本单；②王语嫣知会：后续查删除事件用 EID26 不再是 EID23（EID23 已随归档关闭归零）；③口径提示（不阻塞）：grep 全库无自动化消费 Sysmon 日志（仅报告文本提及 EID23），无改动面。

## 内容价值判断（#457 处置标记配套）

删除对象 = C:\Sysmon.frozen-20260905 + C:\Sysmon 内全部 blob：Sysmon EID23 归档的 vault 文件被替换旧版本。内容价值=零独有数据——逐类对账：md/py/json 等=vault 文件历史版本（git 全覆盖）；.pack/.idx/.rev=vault .git 对象旧版（现行 .git 在位）；616MB 索引快照=kdo 索引可再生中间产物；lock=瞬态锁。任务单决策源已含「老朱确认无印象+确认可弃则删除」授权。

## 机器预审报告

> 🤖 机器预审参考层（#515）：仅供欧阳锋终审参考，不构成结论、不放行不拦截

### ① 声称-交付差集

✅ 1 个声明路径全部存在+已跟踪+无脏改动
### ② lint

✅ frontmatter 可解析 + F-034 五字段在位
### ③ 负向判词 / ④ 存在性核查

✅ 执行报告无负向断言词（检查面=执行报告节）

## 终审记录（欧阳锋 2026-09-06 01:53）

methodology_version: v2.3
verdict: PASS A-（写入者溯源 + 处置闭环）
blocking: 无阻断
residual_risks:
- 🟠 Medium（不阻塞，待王语嫣知会）：EID23 已关归档 → 后续删除事件取证改用 EID26；EID26 只记录不归档，被删文件内容不再留底。若日后需保留归档价值，可另议 ArchiveDir 指 D 盘（本单已声明）。
scores: 溯源完整 24/25 · 逻辑骨架 24/25 · 暗知识密度 16/20 · 可操作性 14/15 · 表达质量 13/15（合计 91/100）

**存在性核查**
- 写入者结论读码复核：sysmon-kdo-forensics.xml 现为 FileDeleteDetected(EID26)、schemaversion=4.90，FileDelete(EID23) 归档已移除 ✅
- 处置：C:\Sysmon 与 C:\Sysmon.frozen-20260905 均不存在（已删）✅
- 释放：C 盘 Free 实测 109.4GB（报告 51G→111G、占用 69% 一致）✅
- 证据：_tmp/646-usn-dump.csv 在场（137MB USN dump；抽样见 Microsoft-Windows-Sysmon%4Operational.evtx「存档」操作行，佐证 Sysmon 归档行为）✅
- 交付物已入仓 commit（f125535f2）
- 内容价值判断（#457）：删除对象=Sysmon EID23 归档的 vault 被替换旧版本（git/vault 现行版全覆盖，零独有数据），授权链完整（老朱确认无印象 + 任务单「确认可弃则删除」）