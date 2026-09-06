---
id: task_20260907_huangyaoshi-bundle-bat-branch-fix
title: "wiki-bundle-backup.bat :daily_only fall-through 双问题修复（周一误导读日志+obsidian快照仅周一跑与注释不符）"
seq: 675
status: in_progress
assignee: huangyaoshi
created_by: wangyuyan
created_at: 2026-09-07
decision_source: 欧阳锋 #673 终审附带发现建议书 diag_20260907_ouyangfeng-bundle-bat-branch-structure（08-31 事故修复被周节拍静默削弱）
reviewer: 欧阳锋
instance: huangyaoshi
updated_at: '2026-09-06T21:14:57.084483+00:00'
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
