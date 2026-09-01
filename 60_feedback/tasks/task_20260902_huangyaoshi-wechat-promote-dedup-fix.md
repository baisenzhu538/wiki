---
id: task_20260902_huangyaoshi-wechat-promote-dedup-fix
title: wechat_promote 去重根治 + sources 存量 147 份重复处置（散点审计 R2/R3 + 欧阳锋建议书，P0）
seq: 601
status: reviewed
assignee: huangyaoshi
created_by: wangyuyan
created_at: 2026-09-02
priority: P0
updated_at: '2026-09-01T18:33:51.002327+00:00'
instance: huangyaoshi
reviewed_by: 欧阳锋
review_date: '2026-09-02'
grade: A-
---

# #601 wechat_promote 去重根治 + 存量去重

## 背景

`kdo-tools/wechat_promote.py:59-62` 去重键含 `date.today()`，跨天重跑必复制。欧阳锋字节级实证：`10_raw/sources/src_*_wechat_*.md` 163 个文件仅 16 个唯一内容，**147 个纯重复**，每日 +17 继续增长（bug 自 08-18 上线即存在）。建议书：`60_feedback/diagnosis/diag_20260902_ouyangfeng-wechat-src-daily-dup.md`。

## 范围（四件）

1. **修 bug**：`promote_transcript()` 存在性检查改为按 hash 全历史匹配——`any(SOURCES_DIR.glob(f"src_*_wechat_{hash_id}.md"))`。
2. **回归测试**：同 hash 跨天重跑必须 skip（断言生效计数，#426 断言纪律）；红绿自证。
3. **seen_links.txt URL 归一化**：`&`/`&amp;`/exportkey 变体归一后查重（风清扬 P0-B-3）。
4. **存量 147 份处置（引用感知）**：
   - 有卡引用的 hash 保留**被引用的那份**（欧阳锋已查实 2 组：`src_2026-08-20_wechat_2404c1658025473c` 被引用 6 次、`src_2026-08-19_wechat_e7536bf1d8f1a7b1` 被引用 1 次——动手前重新 grep 对账，以实测为准）；
   - 无引用组保留最早日期份；
   - 冗余份**不直接删**——移到 `90_control/.sandbox/quarantine-20260902/sources-dup/` 隔离区，观察 7 天无碍后清除；
   - 处置后跑 `kdo index --incremental`。

## 明确不做（王语嫣裁定）

- **inbox 原件不删不移**：`00_inbox/wechat-collect/src_wechat_*` 是 case 卡 `source_refs` 的锚点（F-KDO-015 不断溯源链）。风清扬 R2 的「promote 后移走 inbox 原件」裁定驳回——重复治理只动 10_raw/sources 层。
- 不动 30_wiki 任何卡片正文。

## 安全栏

1. 批量三问：dry-run 输出全量清单 → 范围声明 → 隔离区非空不覆盖。
2. 删/移前全库 grep 引用对账（含 pending-cards 与 30_wiki），对账表附执行报告。
3. 引用路径含中文，清单生成用 `git ls-files -z` / Python NUL 分隔（铁律 §10）。

## 验收

欧阳锋终审：bug 修复后连续两天跑 promote 零新增重复 + 回归测试过 + 147→0（隔离区计数一致）+ 被引用 2 组实测未断链。

## 执行报告

**交付物**：
- `kdo-tools/wechat_promote.py`（去重根治：存在性判定改按 hash 全历史 glob，与日期解耦）
- `kdo-tools/wechat_link_monitor.py`（seen_links 读入归一化：每行注入 canonical_key，封死 &/&amp;/exportkey 历史变体）
- `kdo-tools/tests/test_wechat_promote.py`（+3 跨天去重回归用例）
- `kdo-tools/tests/test_wechat_link_monitor.py`（+4 canonical_key 变体归一用例）
- `90_control/.sandbox/quarantine-20260902/sources-dup/`（143 份冗余源文件隔离区，含 dry-run 全量清单 sources-dup-plan.md）
- `10_raw/sources/`（存量治理：163 → 20 份 date-prefixed wechat 文件）

**完成内容**：四件全落地——①promote_transcript 去重键根除日期成分（`src_*_wechat_<hash>.md` 全历史 glob，命中即 skip 并打印在仓版本名）；②回归测试红绿自证（stash 修复后 2 用例红，恢复后 7/7 绿）；③seen 读入归一化 + canonical_key 变体归一测试（&amp;/exportkey/chksm 追踪参数全归一）；④存量 147→143 份冗余移隔离区（实测口径差异见验证④），追踪件 git mv / 未追踪件 mv，逐件 exists() 双向复核，计数断言 KEEP 20 / MOVED 143 通过。inbox 原件零触碰（遵守「明确不做」）；30_wiki 卡片正文零触碰。

**验证**：①修复后实跑 `python kdo-tools/wechat_promote.py`——17 个逐字稿全部 skip 零新增复制（此前每天 +17）；②`kdo index --incremental` 已跑：-143（total 4171）；③回归：wechat 相关 11/11 过，全量 kdo-tools/tests 227 passed + 2 failed（均实证与本单无关：test_queue_archive stash 基线复现失败=既有；test_infra_status 未登记资产=tmp_* 18 个属 #603 处置范围）；④引用对账实测与任务单估计有差——全库语料实测 **17 份被引用**（非欧阳锋估计的 2 组）：2 份为 30_wiki 卡 source_refs 真引用（08-20_2404c x5、08-19_e7536 x1），15 份为 `.agent/laowantong-context.md` 处理台账引用（08-26 批次）；按「引用感知+不碰他角色文件」保守口径全部保留；⑤保留/隔离计数断言通过，dry-run 全量清单落 quarantine/sources-dup-plan.md。

**未做项**：①隔离区 143 份观察 7 天后清除（任务单约定）；②被引用 08-26 批次 15 份的台账引用是否可随老顽童 context 更新而释放（归老顽童 context 维护节奏）；③头条/公众号的其他历史去重形态（exportkey 以外参数族）如有新变体再补。

**需要谁动作**：欧阳锋——终审 #601（重点：去重键修复+红绿自证+143 隔离计数+被引用 17 份实测未断链）；老朱——知会（隔离区观察 7 天，09-09 后无碍可清除）；另观察到 `90_control/tmp/_launch_hy600.py` 等 headless 启动件 01:49 出现（疑编排层起了 #600/#601 的 headless 实例）——本单已由交互实例完成，请防双工。

## 机器预审报告

> 🤖 机器预审参考层（#515）：仅供欧阳锋终审参考，不构成结论、不放行不拦截

### ① 声称-交付差集

✅ 4 个声明路径全部存在+已跟踪+无脏改动
### ② lint

✅ frontmatter 可解析 + F-034 五字段在位
### ③ 负向判词 / ④ 存在性核查

✅ 执行报告无负向断言词（检查面=执行报告节）

## 终审记录

**结论：PASS A-**（欧阳锋，2026-09-02，methodology v2.3）

### 通过维度（全部终审者独立复跑/亲读，非转述）

1. **版本对齐三问（代码类门禁）**：交付 commit 6923b058a（01:50）在仓；147 处置的 rename 批在 e02798f81（01:46，`git log --follow` 实证）在仓；HEAD 0925d41f0 晚于交付；promote/link_monitor 为按需脚本无长驻进程，生效性以 dry-run 实跑验证 ✅
2. **去重根治**：wechat_promote.py L62-65 `existing = sorted(SOURCES_DIR.glob(f"src_*_wechat_{hash_id}.md"))` 按 hash 全历史匹配，与日期解耦；对照 `git show 6923b058a^` 旧代码（`target.exists()` 键含 `date.today()`）实证带病形态真实 ✅
3. **红绿自证成立**：新增 3 用例用 `_FakeDate` 模拟跨天 + `after == before` 零新增断言——旧代码下跨天 target 文件名必变、必复制，测试必红，红绿逻辑自洽 ✅；wechat 相关 11/11 终审者亲跑 PASS ✅
4. **seen_links 归一化**：wechat_link_monitor.py L439-443 读入逐行注入 `canonical_key`；新增 4 用例覆盖 `&`/`&amp;`/exportkey/chksm/追踪参数变体，亲跑全绿 ✅
5. **存量处置计数断言复核**：163 = 20 保留 + 143 隔离（双向清点一致）；`md5sum` 全库去重实测唯一内容=16，与原始审计吻合；同 hash 组跨保留/隔离件 md5 全同（纯重复，非误删）✅
6. **引用感知未断链**：30_wiki 引用的 2 个 hash（2404c1658025473c ×5 卡引用、e7536bf1d8f1a7b1 ×1）对应文件在仓；台账引用 08-26 份按保守口径保留 ✅
7. **「明确不做」边界核验**：commit 仅含 5 文件（2 脚本+2 测试+任务单），30_wiki 正文零触碰；inbox 原件未动（dry-run 实跑显示 17 逐字稿全部 skip）✅
8. **实跑验证**：`wechat_promote.py --dry-run` 亲跑——17 逐字稿全 skip 零新增复制（验收①等效）；`kdo index --incremental` 亲跑 total 4171 与报告吻合且幂等（-143 已落）✅
9. **全量回归**：kdo-tools/tests 227 passed + 2 failed 与报告逐字吻合；2 失败终审者单独亲跑复现（queue_archive 既有基线 / infra_status tmp_* 属 #603 范围），与本单无关 ✅
10. **五字段执行报告在位**（未做项=边界），机器预审 4 项全 ✅

### 缺陷与残余风险（均不阻断）

- 🟡 sources-dup-plan.md 头部写「唯一 17」，终审者实测全库唯一内容=16（kept+quarantine 合并 md5 去重）——口径笔误（疑把引用计数混入），处置正确性不受影响
- 🟡 报告「隔离区…含 dry-run 全量清单」表述——实际 plan 文件在 `quarantine-20260902/` 层级，非 `sources-dup/` 子目录内
- 🟡 被引用台账份数：报告称 15 份，终审者 grep `.agent/laowantong-context.md` 得 14 个唯一 src 引用——口径小差，保守全保留的方向正确
- 残余：隔离区 143 份观察期至 09-09（老朱知会项）；inbox→sources 双份天然共存的设计性冗余未动（任务单裁定驳回项，非本单范围）

### 溯源要点

源=建议书 `diag_20260902_ouyangfeng-wechat-src-daily-dup.md`（本人 09-02 凌晨所立）+ 旧代码 `git show 6923b058a^` 字节级对照 + 全库 md5 独立去重计数。审查动作均为终审者亲跑，无转述采信。
