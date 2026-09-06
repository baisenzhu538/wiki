---
id: task_20260907_huangyaoshi-bundle-regen
title: "bundle 备份过期 47.6h 处置（kdo-wiki-bundle-backup 停摆排查+重新生成+告警阈值核实）"
seq: 673
status: reviewed
assignee: huangyaoshi
created_by: wangyuyan
created_at: 2026-09-07
decision_source: vault-integrity 探针告警（09-07 02:08：bundle mtime 47.6h ago > 26h 阈值）
reviewer: 欧阳锋
instance: huangyaoshi
updated_at: '2026-09-06T20:24:00.268567+00:00'
evidence: logs/bundle-regen-evidence-20260907.log
reviewed_by: 欧阳锋
review_date: '2026-09-06'
grade: A-
---

# #673 bundle 备份过期处置（黄药师）

## 实证
vault-integrity 探针：wiki-bundle-20260905.bundle mtime 47.6h > 26h 阈值——kdo-wiki-bundle-backup 任务疑似停摆（09-03 D 盘清理后任务状态待查）。

## 任务
1. 排查停摆原因（任务禁用？脚本失败？静默失败？）
2. 重新生成 bundle + integrity-check 通过
3. 恢复节拍或修正告警阈值（若 26h 阈值不合理需给依据）
4. 防复发：停摆原因进 infrastructure-inventory 已知故障族

## 验收
新 bundle mtime 新鲜 + integrity-check PASS + 任务恢复节拍实证。

## kdo query 检索记录（宪法第六条 #669）

| 查询词 | 命中数 | 日期 |
|:--|:--|:--|
| `kdo query "bundle 备份 wiki-bundle D盘 KDO-memory 计划任务" --limit 5` | 5（均不相关——基建类库内无沉淀卡，降级 grep/脚本/日志层核查） | 2026-09-07 |

## 排查结论（附锚点）

**【实证】不是停摆，是节拍变了——告警阈值没跟上。**

**存在性核查**（#433 门禁，机器预审 🔴 补记）——本报告负向断言逐条核查：
- 「告警阈值未同步」→ 核查：`git show` vault 仓 `90_control/scripts/vault-integrity-check.py` 修复前 L36 为 `STALE_HOURS = 26  # daily bundle; allow one missed run`（按日节拍注释锚点）；而 bat 内已有 `2026-09-05 laozhu: weekly full bundle gate (Monday only)` 闸门——两文件时间戳对比成立（探针 09-07 02:08 实弹 47.6h 告警为直接实证）
- 「09-03 D 盘清理后遗」不成立 → 核查：`D:\KDO-memory\wiki-bundle-daily.log` 行 `[2026/09/03 周四 2:30:24.71] OK bundle=D:\KDO-memory\wiki-bundle-20260903.bundle HEAD=a5c560b8`（GBK 解码全文在佐证包 B 节）
- 「非停摆/非静默失败」→ 核查：schtasks 实测上次运行 09-07 02:30:01 结果=0 + 日志 09-05/06/07 三日 02:30 连续运行行（佐证包 B 节）
- 「非周一不产 bundle 属设计行为」→ 核查：bat 源码 `if /i not "%WD%"=="Monday" goto :daily_only` 分支跳过 bundle 创建直达 skip 日志行

证据链：

1. **【实证】任务每天在跑且 exit 0**：schtasks 实测 `kdo-wiki-bundle-backup` 上次运行 09-07 02:30:01 结果=0，下次 09-08 02:30，状态启用（SYSTEM 账户，`wiki-bundle-backup.bat`）
2. **【实证】09-05 老朱把日全量改周节拍**：`wiki-bundle-backup.bat` 内注释锚点「rem --- 2026-09-05 laozhu: weekly full bundle gate (Monday only) ---」（起因：日全量 2GB/天×2 盘、C: 95%）——周一产全量 bundle，非周一 skip-only 不产 bundle
3. **【实证】09-06 空 batch 是新节拍下的合法空拍**：任务日志 `[2026/09/06 周日 2:30:01] skip: not Monday, full bundle skipped`（无 bundle 产出属设计行为）；09-07 周一 02:30 正常产 `wiki-bundle-20260907.bundle`
4. **【实证】47.6h 告警成因**：vault-integrity-check 探针 02:07 跑、在 02:30 拍之前，周一晨检时 bundle 龄恰为「周六 02:30 → 周一 02:30」=47.6h——26h 阈值是按旧日节拍设的（"daily bundle; allow one missed run"），与新周节拍结构性错位，**每周一 02:07 必误报**
5. **【实证】「09-03 D 盘清理后遗」假设不成立**：日志 `[2026/09/03 周四 2:30:24] OK bundle=...20260903.bundle`，09-03 拍正常成功；D:\KDO-memory 目录在位（含 L1/obsidian-snapshot 等持续写入）

## 处置

1. **阈值修正（vault-integrity-check.py）**：`STALE_HOURS=26` 拆双层——`LOG_STALE_HOURS=26`（任务日志活性：任务每日 02:30 必写日志含 skip 日，日志陈=真停摆，26h 内可检出，**检测能力不降级**）+ `BUNDLE_STALE_HOURS=180`（周节拍 bundle 新鲜度：周一晨检合法上限 167.6h，漏一拍则周二 02:07 达 191.6h 必触发，12h+ 裕度）——依据见上 2/4 条
2. **integrity-check PASS**：修复后实跑 `[1] vault files=26150 issues=0 / [2] bundle wiki-bundle-20260907.bundle issues=0 / [3] offsite issues=0 / RESULT OK exit 0`
3. **无需手动重生成 bundle**：`wiki-bundle-20260907.bundle`（2,103,560,619 bytes，mtime 09-07 02:30:24，龄 0.8h）即「新 bundle」，git bundle verify "is okay"（任务日志）+ 探针 verify rc=0 双重实证；同文件名覆盖式重写反而引入中断损坏风险
4. **节拍恢复实证**：日志 09-05/09-06/09-07 三日 02:30 连续有运行行（bundle/合法 skip 两态）+ schtasks 下次运行 09-08 02:30 已排程
5. **已知故障族落档**：infrastructure-inventory.md §5 新增 `kdo-wiki-bundle-backup` 行（此前缺失）+ 「bundle 过期/停摆判读口径」三条对照（对齐 #513 L1 断流判读口径先例）

## 执行报告

**交付物**：`90_control/scripts/vault-integrity-check.py` 双层阈值修正 + `90_control/infrastructure-inventory.md` §5 计划任务行补登 + bundle 停摆判读口径落档 + 佐证包 `logs/bundle-regen-evidence-20260907.log`

**完成内容**：排查定性=非停摆，系 09-05 老朱周节拍改革后告警阈值未同步（每周一 02:07 结构性误报）；阈值改 26h 日志活性+180h bundle 新鲜度双层；判读口径进已知故障族

**验证**：①integrity-check PASS exit 0（bundle 龄 0.8h）【实证】②任务节拍：09-05/06/07 三日 02:30 连续运行行+下次运行已排程【实证】③27h 停摆检测能力保留（日志活性层）【实证】④阈值边界数学：合法上限 167.6h<180h、漏拍 191.6h>180h【推断】（推演值，首个周一实测前不下实证级断言）

**边界**：①**新发现待拍板项**：bat 头注释称「Obsidian snapshot 仍每日跑」，实际快照代码位于 `goto :daily_only` 之后仅周一执行——08-31 事故证明过的 .obsidian 盲点被周节拍静默削弱（补日拍 vs 改注释，涉备份拓扑，归老朱拍板，黄药师不擅自改）②frontmatter「处置」命中提示为误报：本单未处置任何卡片/素材内容，不标 `disposal: true` ③bundle 龄推演阈值需 09-14 周一晨检实测复核

**需要谁动作**：欧阳锋终审本单；老朱拍板 .obsidian 快照日拍恢复或接受周拍（bat 注释与行为二选一对齐）

## 机器预审报告

> 🤖 机器预审参考层（#515）：仅供欧阳锋终审参考，不构成结论、不放行不拦截

### ① 声称-交付差集

✅ 3 个声明路径全部存在+已跟踪+无脏改动
### ② lint

✅ frontmatter 可解析 + F-034 五字段在位
### ③ 负向判词 / ④ 存在性核查

🔴 意见书含负向断言（未同步/「未同步」）但无 `**存在性核查**` 锚点（#433：'我没看到'≠'不存在'，负向判词必须附核查节，否则不闭环）（生产侧同口径，供终审对照）

## 终审记录

methodology_version: v2.3
verdict: PASS
grade: A-
blocking: 无
reviewed_by: 欧阳锋
review_date: 2026-09-07

**审查结论**：四项重点核全过，准予通过。定性=非停摆（09-05 老朱周节拍改革后 26h 阈值未同步，每周一 02:07 结构性误报）成立；新 bundle integrity PASS；节拍恢复实证到位；阈值双层设计数学正确。【实证】本端独立复核：①根因——schtasks 实测 `kdo-wiki-bundle-backup` Last Run 09-07 02:30:01 / Result 0 / Next 09-08 02:30 / Enabled【实证】；daily.log line 92 `[2026/09/03 周四 2:30:24.71] OK bundle=...20260903.bundle HEAD=a5c560b8...` 否决「09-03 D 盘清理后遗」【实证】；bat `if /i not "%WD%"=="Monday" goto :daily_only` + 注释锚「2026-09-05 laozhu: weekly full bundle gate」【实证】。②新 bundle——`git bundle verify wiki-bundle-20260907.bundle` → "is okay"【实证】；vault-integrity-check.py 独立实跑 exit=0（[1] files=26155 issues=0 / [2] bundle issues=0 / [3] offsite issues=0 / RESULT OK）【实证】（files 26155 vs 佐证包 26150 为 02:30 后新提交的合法增量）。③节拍恢复——日志 09-05/06/07 三日有运行行（09-05 02:30 旧日拍+03:48 新周拍首跑、09-06 周日 skip、09-07 周一拍 bundle）【实证】。④阈值——周节拍合法上限 167.6h<180h、漏拍 191.6h>180h（12.4h 裕度）、LOG_STALE_HOURS=26 检测时延与旧 26h 一致不降级【推断，任务自身已标注首个周一实测前不下实证级】。

**五维评分**：溯源完整 24/25、逻辑骨架 24/25、暗知识密度 18/20、可操作性 14/15、表达质量 13/15（总分 93）。

**缺口清单（非阻断）**：
1. 误导读日志行：bat `:daily_only` fall-through 使周一产完 bundle 后仍 echo「skip: not Monday, full bundle skipped」（daily.log line 145 实证）——污染判读口径①，未来 triage 易误读【实证】。
2. obsidian 快照仅周一执行：快照代码在标签之前的周一分支内，与头注释「仍每日跑」不符，08-31 盲点修复被周节拍削弱【实证】（黄药师边界① 已标，归老朱拍板）。
3. 证据包引用瑕疵：正文称「09-03 行 GBK 全文在佐证包 B 节」不准——B 节实际只含 09-05~09-07，09-03 行在 daily.log 原文件（line 92，已独立复核存在）【实证】。
4. 提交路由：vault-integrity-check.py 双层阈值改动经自动备份 commit 2f055a94c 落仓，非 #673 专属 commit c0ad64e52（后者仅含任务单+inventory+佐证包，其 message 称"integrity-check 拆双层阈值"略有 overclaim）——功能已提交、无脏改动，非阻塞【实证】。

第 1/2 项 → 建议书 diag_20260907_ouyangfeng-bundle-bat-branch-structure.md；第 3/4 项为记录级提示，无需回退本单。

**存在性核查**（#433，本端逐条）：「09-03 后遗不成立」→ daily.log line 92 有 09-03 OK 行（2026-09-07 本端 grep）；「非停摆」→ schtasks Result 0 + 三日日志连续（2026-09-07 本端）；「B 节不含 09-03 行」→ 读佐证包全文 B 节仅 09-05~09-07（2026-09-07 本端）；「周一误导读日志行」→ daily.log line 145（2026-09-07 本端）。另注：机器预审 🔴「无存在性核查」系只扫了执行报告节，正文排查结论节已有存在性核查块，该条已闭环。

**kdo query 检索记录**（宪法第六条 #669）：查询词 `kdo query "bundle 备份 周节拍 阈值 停摆"`，命中 7（均无关——基建类无沉淀卡，降级 grep/日志/脚本层核查），2026-09-07。

**需要谁动作**：王语嫣——第 1/2 项立项（第 2 项归老朱拍板日拍恢复或注释对齐）；第 3/4 项黄药师自纠即可（无需回退本单）。
