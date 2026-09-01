---
id: diag_20260902_fengqingyang-substitute-scatter-audit
title: 审计报告：替代工作期（08-28~09-01）散点全面审计与修复建议（建议稿，待王语嫣裁决）
type: diagnosis
status: draft
audience: 王语嫣
author: 风清扬
created_at: '2026-09-02'
trigger: 老朱 2026-09-02 直令（Kimi 额度恢复期，飞书端四角色替代工作后 Obsidian 出现大量散点）
---

# 替代工作期散点全面审计（建议稿，待王语嫣裁决）

> 审计 = 事后复核 + 建议。本报告只做事实认定与修复建议，**所有执行动作请王语嫣裁决后编排分发**（基建修复→黄药师；流程裁定→王语嫣；凭据处置→需老朱知情）。审计方法：全部负向断言均做存在性核查，关键结论经字节级独立复验（md5sum / git diff / 源码行号）。

## 一、这几天发生了什么（时间线摘要）

替代期 5 天共 **385 次 git 提交**（08-28:89 / 08-29:9 / 08-30:49 / 08-31:51 / 09-01:171），全负荷运转且产线本身健康——队列流转、终审 PASS、新角色 skills-assistant 上线均有完整留痕。但同期发生了与散点直接相关的四类事件：

| 时间 | 事件 | 与散点的关系 |
|---|---|---|
| 08-31 02:00 | **vault 整树消失事故**（24811 文件被掏空后重建） | 事故同刻（02:03–02:09）产生一批**重定向事故散点**：根目录 `--help`（含 douyin cookie）、`%TEMP%upgrade_plan.json`、`C:UsersAdministrator...txt` ×2、`C\uf03a/` 假盘符目录树、`60_feedback/_sg_cookie.txt` |
| 08-31 22:09 | wechat 管线空总结事故 → #584 根治 | 修复期间跨天重跑 promote，触发**去重 bug**（见三-1） |
| 09-01 全天 | 171 次提交高密度作业 + 双实例并发 + relay bug | 大量一次性脚本（`_tmp_*`/`tmp_*`）随手落盘未清理；dispatch 台账激增无消费端 |
| 全程 | 应急节奏优先，「落盘即正义」 | 93 个已跟踪文件改动 + 165 个未跟踪文件**未提交**（截至 09-02 01:00），含 skill frontmatter 补齐后的 BOM 清洗批次 |

结论：**散点不是哪个 agent 乱来，而是「事故应急 + 高产节奏 + 三个真实 bug」叠加的系统性产物**。替代工作本身完成了任务，但收尾纪律（清理/提交/归档）在应急中被让渡。

## 二、散点清单与实证（按严重度）

### P0-A 凭据类文件裸露（安全，建议老朱知情后立即处置）

| 文件 | 实证 | 来源判定 |
|---|---|---|
| `./--help`（5409B, 08-31 02:08） | 字节级核查：Netscape cookie 文件，含 douyin.com 会话凭据 | 某命令把 `--help` 当输出文件名的重定向事故。注意：git porcelain 不显示它（`--help` 被 git 解析为选项），引用须写 `./--help` |
| `60_feedback/_sg_cookie.txt`（473B, 08-31 02:03） | curl 生成的 cookie 文件 | 同期下载事故残留 |
| `duanzhixing/feishu_user_token.json` | 飞书 user token 裸露在顶层非编号目录 | 存量问题，本次审计顺带发现 |

### P0-B 真实 Bug（不修则散点持续再生产）

1. **`kdo-tools/wechat_promote.py:59-62` 去重键含当天日期**——`src_{date.today()}_wechat_{hash}.md`，`target.exists()` 只查「今天+hash」，跨天重跑必复制。实证：`346efef2737b383b` 三天副本 md5 完全相同（`42a851c5…` ×3）。**后果：17 篇文章 × 3 天 = 51 个重复源文件，且每天还在增加**。
2. **同脚本第 66 行 `shutil.copy2` 不删 inbox 原件**——00_inbox 与 10_raw 双份并存，同内容最多 4 份（inbox 原件 ×1 + sources 副本 ×3）。
3. **`seen_links.txt` 链接级去重失效**——同一文章以 `&`/`&amp;`/带 exportkey 等 URL 变体各存一行。
4. **watch_inbox 扫描器无目录树裁剪**——`dispatch_20260830_181102.md` 达 863KB / 7908 行，把 `00_inbox\Handle`（1513 次）等整棵目录扫进 dispatch。
5. **dispatch 无消费端**——grep 全库无任何文件签收这 17 个 dispatch（目录总计 49 个文件），发了没人读。

### P1 历史遗留散点（替代期放大，非当期新造）

- **vault 根目录 59 个 `_tmp_/_debug/_fix/tmp_*` 散落脚本与 txt**（如 `_fix_source_refs_step1/2/3/final.py` 四版并存、`_pq_table.bak`）；其中 `_tmp_skill_health.json`（29KB）**被 `建议书_20260901_skill健康度勘察与检测方法论.md:146` 引用，清理前须先改引用**。
- `kdo-tools/tmp_*` 25 个一次性脚本（3 个转写变体、3 个抓视频版本、1 个读凭据的 `tmp_publish_md.py`），多数有正式替代品。
- `00_inbox/` 根级平铺 236 个 md/json/txt；含字符变体重复对（`Harness Engineering-…md` vs `Harness Engineering：…md`，md5 相同）。
- `C\uf03a/` 假盘符目录树（`:` 被写成 Unicode PUA 字符，WSL 写 `C:\...` 路径事故产物）。
- `60_feedback/wechat-collect/*.mp4` 6 个共约 120MB 放反馈层（素材应去 10_raw，系脚本既定行为）。

### P2 未提交积压

`git diff --stat` = **93 文件 +13063/-331 未提交**（大头 logs 日志 +9473 行）；其中 37 个 shared SKILL.md 是 #595 之后的 BOM 清洗（去 `﻿---`），无害但应尽快落账，否则下次批量改动无法审查。

### 误报澄清（存在性核查后排除）

- `50_delivery/published/del_20260901_*` 8 目录：manifest 完整且全部已登记 `delivery-registry.md`——**合规，非散点**。
- `60_feedback/inbox-queue/dispatch_*` 17 个新件：内容各异，**非 relay bug 重发**；问题是无人消费（见 P0-B-5）。
- `_tmp_oyp_brief.txt`/`_tmp_oyp_review.py`：已不存在，点名单过时。

## 三、根因（三问拆解）

1. **壳在数据流断**：dispatch 有壳（17 个文件在落盘）无消费（零签收）——「建好壳≠在记账」的又一样本。
2. **去重口径缺陷**：promote 去重键设计成「日期+hash」，隐含「一天只跑一次」假设；事故应急跨天重跑即破防。
3. **应急期无收尾环节**：事故（02:00 整树消失、22:09 空总结、14:32 自伤截断、23:07 relay bug）连环发生，所有会话都在救火，临时脚本与未提交改动无人收摊。

## 四、修复建议（建议稿，待王语嫣裁决后编排）

| # | 动作 | 归属建议 | 前置条件 |
|---|---|---|---|
| R1 | 凭据三件套处置（`./--help`、`_sg_cookie.txt` 移出 vault 或删除；`feishu_user_token.json` 归位+评估轮换 token） | 老朱知情 → 黄药师执行 | 注意 `--help` 需以 `./--help` 引用操作 |
| R2 | 修 `wechat_promote.py` 去重：按 hash glob 全目录查重；promote 后移走 inbox 原件；`seen_links.txt` URL 归一化 | 黄药师（基建） | 先单卡 dry-run 再批量（禁止清单 #9） |
| R3 | 10_raw/sources 51→17 去重：每 hash 保留最早日期一份，删 09-01/09-02 副本 | 黄药师 | 删前核对无其他文件按新日期文件名引用 |
| R4 | 93 个未提交改动分三批落账：①SKILL BOM 清洗批 ②todos/队列留痕批 ③logs 批 | 各 owner 自检后提交 | 王语嫣确认无在途冲突 |
| R5 | 根目录 59 个 + kdo-tools 25 个 tmp 脚本清理：先处理 `_tmp_skill_health.json` 引用，其余归档 `_tmp/` 或删除 | 黄药师执行，王语嫣裁定口径 | 批量操作三问（dry-run/范围声明/非空不覆盖） |
| R6 | dispatch 机制二选一：接消费端（王语嫣时钟值守纳入签收）或停发；watch_inbox 加目录树裁剪 | 王语嫣裁定 → 黄药师施工 | — |
| R7 | `C\uf03a/` 假盘符树、Harness 重复对、mp4 归位 10_raw | 黄药师 | — |

## 五、顺带发现（不新立案，记录备查）

- 王语嫣自报 09-01 02:50 已写 `agent复盘/wangyuyan/daily-context/2026-09-01.md`，但该文件现不在盘上——复盘落盘缺口，是否追查归王语嫣定（复盘是各角色自己的事，我只记录差异）。
- `90_control/todos/wangyuyan.md` 在 08-31 事故中被恢复至 01:31 快照，08-31 前收件箱历史不可考。
- 08-31 整树消失事故根因停在「候选 c：懂 .git plumbing 的程序化未知操作者」，四项加固待老朱拍板——本审计期散点与该事故同源的仅是重定向事故族，不能据此排除或坐实入侵说。

## 六、可固化资产候选

1. **审计判词**：「应急期散点 = 事故同源产物 + 去重口径缺陷 + 无收尾环节」——凡大事故后 48h 内必做散点扫描（根目录 `_tmp/--help/%TEMP%` 特征 + git status 未跟踪计数）。
2. **审计判词**：「去重键含时间字段 = 跨周期必重」——凡去重逻辑审查，先问「键里有没有今天」。
3. **运维判词**：「git 不认的文件名（`--help` 等选项形态）会逃出 porcelain 视野」——散点扫描须用 `find`/Glob 兜底，不可只信 `git status`。

---

*风清扬（观察者）· 2026-09-02 · 只审计、不执行；执行编排归王语嫣*
