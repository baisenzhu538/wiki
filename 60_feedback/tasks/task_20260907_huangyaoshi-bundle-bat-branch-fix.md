---
id: task_20260907_huangyaoshi-bundle-bat-branch-fix
title: "wiki-bundle-backup.bat :daily_only fall-through 双问题修复（周一误导读日志+obsidian快照仅周一跑与注释不符）"
seq: 675
status: reviewed
assignee: huangyaoshi
created_by: wangyuyan
created_at: 2026-09-07
decision_source: 欧阳锋 #673 终审附带发现建议书 diag_20260907_ouyangfeng-bundle-bat-branch-structure（08-31 事故修复被周节拍静默削弱）
reviewer: 欧阳锋
instance: huangyaoshi
updated_at: '2026-09-06T21:53:28.690725+00:00'
evidence: logs/sim-bundle-bat-675-20260907.log
reviewed_by: 欧阳锋
review_date: '2026-09-06'
grade: A-
---

# #675 bundle bat 结构双问题修复（黄药师）

## 实证（欧阳锋 #673 终审独立读 bat 源码+daily.log）
1. `:daily_only` 标签双角色：周一产完 bundle 后仍无条件 echo「skip: not Monday」误导读日志（09-07 L143→L145 实证）
2. **obsidian 快照仅周一执行**，与头注释「Obsidian snapshot 仍每日跑」不符——08-31 事故的 .obsidian 盲点修复被周节拍静默削弱（非周一 09-06 无 snapshot 行实证）

## 修法
拆分标签职责（周一全量路径/每日路径各归各）+ obsidian 快照节拍按注释意图对齐（或改注释如实声明节拍，二选一给依据）+ 日志行修正。

## 验收
周一/非周一两天模拟：日志行如实+快照行为与文档声明一致；回归不红。

## 执行报告（黄药师 2026-09-07 05:40）

**交付物**：`90_control/scripts/wiki-bundle-backup.bat` 重构（标签拆分+快照节拍对齐+日志行修正）；文档层 `90_control/infrastructure-inventory.md` L186 节拍声明 + bundle 判读口径收口；证据 `logs/sim-bundle-bat-675-20260907.log`（红→绿两段）；模拟 harness `_tmp/bat675-sim/sim_bundle_bat_675.py`（_tmp 不进 git，可复跑复核）。

**完成内容**：①标签拆分——`:monday_full`（周一全量 bundle+verify+HEAD 比对+offsite）/`:daily_tasks`（.obsidian 快照+rolling cleanup+done）各归各，周一走 `goto :daily_tasks` 前无任何 skip 行出口【实证】修后 Monday 段 0 条 skip 行；②快照节拍二选一取「按注释意图对齐=每日跑」，依据：08-31 盲点兜底意图（.obsidian 不进 git，快照是唯一恢复路径，周拍=最多丢 6 天配置）+快照 KB-MB 级成本不适用 2GB/天磁盘闸门理由+头注释与 skip 行两处既有声明均为每日【推断→模拟实证】；③skip 行改如实措辞「(.obsidian snapshot + cleanup still run)」；④附带声明真实性修正（超出双问题最小集，欧阳锋可裁）：头注释「Keeps rolling >=4 bundles」→「2 weekly bundles」（09-02 老朱 7→4、09-05 再改 2，注释停在旧值，与问题②同类「注释与行为不符」）；⑤WD 探测失败 fail-safe 保持（空值≠Monday→skip 分支，每日尾段仍执行）。

**验证**：TDD 红→绿——自建两天沙盒模拟（fakewiki git 仓+假 DEST，4 个声明 seam：路径×2/星期参数注入/offsite call stub 防 real 坚果云写入+keep-2 误删【实证】offsite-2nd.bat 硬编码 D:\KDO-memory→C:\kdo-offsite 真路径）14 断言：修前 RED 10/14（恰两目标缺陷失败：Sunday 快照 S3/S4/S5+Monday 假行 M3，其余语义全过），修后 GREEN 14/14（含 Monday 快照内容 day2 新鲜度、cleanup keep-2、bundle verify rc0）；回归=vault-integrity-check.py OK exit 0（vault 26172 files+bundle+offsite 三查全过）+ 90_control/scripts/tests pytest 296 passed 无红；真实 D:\KDO-memory 未被模拟触碰（全沙盒隔离）。

**边界**：①`wiki-bundle-offsite-2nd.bat` 自身未动（其 SRC/DEST 是真备份副本目录，行为与注释一致，无同款缺陷）；②真实节拍验证只能到「模拟等价」——真实生效看 09-08（周二）02:30 首拍：日志应出现 skip+「OK .obsidian snapshot updated」两行（此前周二无快照行）；③LightRAG/kdo CLI 侧无涉；④harness 未晋升正式 pytest（有副作用：建仓+跑 cmd，需 marker 隔离，是否收编待欧阳锋裁）。

**需要谁动作**：欧阳锋终审（重点核：快照节拍二选一依据是否成立、附带头注释修正是否接受、09-08 首拍后可抽查 D:\KDO-memory\wiki-bundle-daily.log 尾 4 行）；无需老朱动作（#673 挂的「待老朱拍板补日拍或改注释」已按对齐方案执行，inventory 判读口径已同步收口）。

## kdo query 检索记录（宪法第六条，#669）

| 检索词 | 命中 | 日期 |
|---|---|---|
| `kdo query "备份 周节拍 bundle obsidian 快照" --limit 5` | 5 chunks（25 entities/35 relations） | 2026-09-07 |
| `kdo query "wiki bundle backup daily weekly cadence" --limit 5` | 5 chunks（26 entities/47 relations） | 2026-09-07 |

判定：库内无 bundle bat 结构/快照节拍专题卡；本任务为非知识类代码修复，权威证据源=bat 源码+`D:\KDO-memory\wiki-bundle-daily.log`+inventory 判读口径（grep/Read 属非知识类检索合规口径②）。

## 机器预审报告

> 🤖 机器预审参考层（#515）：仅供欧阳锋终审参考，不构成结论、不放行不拦截

### ①-补 划痕路径提示

- ⚠️ 交付物节含划痕路径 `_tmp/bat675-sim/sim_bundle_bat_675.py`（中间产物非交付物，按约定豁免三态检查；如属误写请清理交付物节）
### ① 声称-交付差集

✅ 3 个声明路径全部存在+已跟踪+无脏改动
### ② lint

✅ frontmatter 可解析 + F-034 五字段在位
### ③ 负向判词 / ④ 存在性核查

✅ 执行报告无负向断言词（检查面=执行报告节）


## 终审记录

methodology_version: v2.3
verdict: PASS
grade: A-
blocking: 无
reviewed_by: 欧阳锋
review_date: 2026-09-07

**审查结论**：三项重点核全过，准予通过。

①标签职责拆分后周一/非一路径日志如实——bat 现逻辑 `if /i "%WD%"=="Monday" goto :monday_full`：非周一先 echo skip（措辞 `.obsidian snapshot + cleanup still run`）再 `goto :daily_tasks`；周一进 `:monday_full` 产完 bundle/verify/HEAD/offsite 后自然 fall-through 到 `:daily_tasks`（中间无 goto 出口），周一不再出现 skip 行【实证，本端读 bat 全文】。沙盒模拟 S1/S2/S5（周日 skip 恰一次+无 start/OK bundle+措辞如实）、M1/M3（周一 start/OK bundle 且无 skip）全过【实证，本端在 git 仓库 CWD 下独立重跑 harness，GREEN 14/14】。修复前真实日志双缺陷均被 D:\KDO-memory\wiki-bundle-daily.log 证实：09-07（周一）段「OK .obsidian snapshot updated」后紧跟「skip: not Monday」假行；09-06（周六）段「skip…(obsidian snapshot still runs)」却无「OK .obsidian snapshot updated」行【实证】。

②obsidian 快照节拍与文档声明一致——bat 头注释与 `:daily_tasks` 注释均明示「EVERY day」+ inventory L186「obsidian 快照**每日** #675」+ L190 判读口径收口（周一=start/OK bundle/快照/cleanup/done，非周一=skip/快照/cleanup/done）三处声明一致【实证】。沙盒 S3/S4（周日快照行+快照目录真实写入）、M4/M5（周一快照行+内容 day2 新鲜）全过【实证】。决策「对齐为每日」依据成立：08-31 .obsidian 盲点兜底意图 + 快照 KB-MB 级成本不适用 2GB/天磁盘闸门 + 修复前头注释与 skip 行两处旧声明本就写每日【推断→模拟实证】。

③回归不红——vault-integrity-check.py 本端独立实跑 exit=0（[1] files=26173 issues=0 / [2] bundle issues=0 / [3] offsite issues=0 / RESULT OK）【实证】；`pytest 90_control/scripts/tests` 本端独立实跑 296 passed in 51.65s，exit=0【实证】。

**五维评分**：溯源完整 24/25、逻辑骨架 24/25、暗知识密度 17/20、可操作性 14/15、表达质量 14/15（总分 93）。

**非阻断观察**：
1. harness M8 `git bundle verify` 断言依赖运行 CWD 为 git 仓库——`git bundle verify` 需 repo 上下文。本端实测：从 `$TEMP`（非 git 目录）跑 13/14 RED、唯一 FAIL=M8（stderr `error: need a repository to verify a bundle`）；切到 git 仓库 CWD 后复跑 14/14 GREEN。harness 未晋升 pytest、`_tmp` 不进 git 已由执行者边界④ 如实声明；若日后收编，须在 M8 补 `-C FAKEWIKI` 或写明「须在 git 仓库内运行」前置。属证据层鲁棒性提示，非修复缺陷【实证】。
2. 交付物节把未进 git 的划痕路径 `_tmp/bat675-sim/sim_bundle_bat_675.py` 列为交付物（机器预审已提示）——执行者显式标注「_tmp 不进 git，可复跑复核」，接受【实证】。
3. 附带头注释 rolling >=4→2 weekly 声明真实性修正（超出双问题最小集）——依据充分（09-02 老朱 7→4、09-05 再改 2，注释停在旧值），与问题②同类「注释与行为不符」，接受【实证，git log 2df85f297 见 09-05 rolling 留 2 份改动】。
4. 执行报告称 vault files=26172，本端实测 26173（+1 为 09-07 05:45 后新增 headless 日志等合法漂移），非缺陷【实证】。
5. 真实节拍生效待 09-08（周二）02:30 首拍闭环（执行者边界② 已声明）——本次验证到「模拟等价」级，真实环境由明日首拍确认。

**存在性核查**（#433，本端逐条）：「周一假 skip 行（修复前）」→ daily.log 09-07 段可见「OK .obsidian snapshot updated」后紧跟「skip: not Monday」（2026-09-07 本端读 D:\KDO-memory\wiki-bundle-daily.log）；「非周一无快照行（修复前）」→ daily.log 09-06 段仅「skip…(obsidian snapshot still runs)」+「done」，无「OK .obsidian snapshot updated」（2026-09-07 本端）；「回归不红」→ vault-integrity-check exit=0 + pytest 296 passed（2026-09-07 本端独立）；「快照节拍三处声明一致」→ bat 头注释/inventory L186/L190（2026-09-07 本端）。

**kdo query 检索记录**（宪法第六条 #669，本端终审侧）：查询词 `kdo query "备份 bundle obsidian 快照 节拍" --limit 5`，命中 5 chunks（24 entities/34 relations），首条 framework-dual-center-feishu-obsidian（与 bundle bat 结构/快照节拍无直接卡），确认库内无 bundle bat 结构/快照节拍专题卡，属代码/日志层核查（2026-09-07）。

**需要谁动作**：无回退项。王语嫣知悉——#675 终审 PASS A-；黄药师边界③「真实节拍生效看 09-08 02:30 首拍」→ 明日首拍后抽查 D:\KDO-memory\wiki-bundle-daily.log 尾 4 行（非周一应为 skip + `OK .obsidian snapshot updated` 两行，周一假行不再出现）。若 harness 收编 pytest，建议 M8 补 `-C FAKEWIKI`（非阻塞，随收编一并处理）。