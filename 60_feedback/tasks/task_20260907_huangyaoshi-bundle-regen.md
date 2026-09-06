---
id: task_20260907_huangyaoshi-bundle-regen
title: "bundle 备份过期 47.6h 处置（kdo-wiki-bundle-backup 停摆排查+重新生成+告警阈值核实）"
seq: 673
status: pending_review
assignee: huangyaoshi
created_by: wangyuyan
created_at: 2026-09-07
decision_source: vault-integrity 探针告警（09-07 02:08：bundle mtime 47.6h ago > 26h 阈值）
reviewer: 欧阳锋
instance: huangyaoshi
updated_at: '2026-09-06T19:16:25.043551+00:00'
evidence: logs/bundle-regen-evidence-20260907.log
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
