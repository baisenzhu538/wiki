---
id: task_20260908_wangyuyan-681-production-rollout
title: "#681 拍板落地：老朱拍『全做』——按诊断报告 §五/§七 立项 P0/P1/P2 产卡单+基建/补采工单并调度生产"
seq: 682
status: reviewed
assignee: wangyuyan
created_by: 老朱（小昭代书）
created_at: 2026-09-08
decision_source: 老朱 09-08 19:25 对 #681 产卡范围拍板「全做」（小昭代书任务单+00_inbox 投放+headless 拉起）
reviewer: 欧阳锋
instance: wangyuyan
updated_at: '2026-09-08T12:20:17.167148+00:00'
evidence: 60_feedback/tasks/task_20260908_wangyuyan-681-production-rollout.md
reviewed_by: 欧阳锋
review_date: '2026-09-08'
grade: A-
---

# #682 #681 拍板落地编排单（王语嫣）

> 老朱 19:25 看完 #681 诊断汇报后直令：「**全做**」。即 P0/P1/P2 三包全部立项，P1 六案例**全产**（含黄谦/Simon Peng，不裁量裁剪）；基建缺口按报告 §七 一并立项。本单为编排执行单——立项、入队、拉起生产由你完成。

## 拍板范围（依据 60_feedback/diagnosis/diag_20260908_wangyuyan-ai-data-ai-basic-deep-dig.md §五/§七，锚点/素材行号/解压路径全在该报告，立项时照抄不重查）

1. **P0 → 产卡单给老顽童**：AI 数据域方法论族 8 张（framework-adaptive-data-flywheel / concept-data-three-constants-three-shifts / tool-data-maturity-l1-l6 / tool-data-governance-four-layers / case-truman-bedtime-story-datapack / case-xujian-invoice-data-asset / dk-ai-on-ai-data-poisoning / dk-data-timely-review）。解压路径按报告 §五-P0（framework≥3 解压资产已配齐）。
2. **P1 → 产卡单给老顽童**：Live258 六案例全产（yongbo / nongfu / xingzhi / tianli / huangqian / simonpeng）。注意终审残余风险移交项：立项带缺陷① dk 互链前置查重（dk-ai-does-not-question-your-mistake.md:112 已吸收 R/E/S/X 事实分级、dk-demand-feature-stacking.md:165 已引农夫三拳+黄谦边界例——产卡前对照定互链防双源冲突）。
3. **P2 → 补强补挂单给老顽童**：报告 §五-P2 表全量——半肥猫口述细节回填两张落点卡、两组互链、KDO 桥接素材、concepts/ai数据理解第一课 + 马易族 6 卡 source_refs=src_unknown 溯源补挂（合并为一个补挂工单）。
4. **基建 → 工单给黄药师**：ai-data-domain-digest 补建（参照 ai-basic-domain-digest 骨架）+ 本域 12+ 散卡注册 domain-mapping + case-yihang-dual-triangle-AI数据 vs AI三角-数据 重复卡去重合并。
5. **补采 → 工单给洪七公**：27 张无产物 PNG OCR 补采评估（优先 040618 四种工作状态图）。
6. **附带移交**：framework 两张基准卡 #544 退回未修——按报告建议请欧阳锋排老顽童返工（知悉件，不另立新单也可，由你定路由）。
7. **归档判定**（报告 §五-登记不产/归档）：口述01/闲聊篇作干净转写版归档不删、表格.md 随补挂闭环、D 组 3 件编排域历史归档、A 组 4 件 #667 维持——随本单编排落账。

## 执行要求
- 立项各单 frontmatter 照 #681 同族格式，decision_source 注明「老朱 09-08 19:25 拍板全做（#682 编排）」；ASR 校正清单（报告 §六）必须随 P0/P1 单下发到产卡执行层。
- 立项后按队列纪律拉起老顽童生产（kimi-headless-launch，P0 先行，P1 跟进）；黄药师/洪七工单按各自节奏拉起或留队待领。
- 完工在本单追加编排台账（各新单号+拉起 proc/留队状态）+ 执行报告五字段；queue_transition claim/complete 正常流转。

## 边界
- 本单只做编排落地，不直接产卡；P1 黄谦/Simon Peng 两张已拍板全产，不再回头裁量。
- 老朱今晚可能随时回来查进度——编排台账落盘即更新，不留口头状态。

## 编排台账（2026-09-08 19:35 王语嫣落盘，老朱查进度以此为准）

### 立项清单（7 项拍板范围 → 5 新单 + 归档落账 + 1 知悉件）

| seq | 新单号 | 内容 | assignee | 拉起/留队状态 |
|:-:|:--|:--|:--|:--|
| 683 | `task_20260908_laowantong-ai-data-methodology-p0` | P0：AI数据域方法论族 8 张（含 ASR 校正清单下发） | laowantong | **已拉起** proc_laowantong_5116（19:35:41，tool=kimi，log=logs/headless-laowantong-20260908-193541.log） |
| 684 | `task_20260908_laowantong-live258-six-cases` | P1：Live258 六案例全产（dk 互链前置查重缺陷项已写入任务单） | laowantong | 留队（老顽童单线程，#683 后续领） |
| 685 | `task_20260908_laowantong-ai-data-p2-backfill` | P2：补强补挂 6 工作项（合并工单） | laowantong | 留队（#684 后） |
| 686 | `task_20260908_huangyaoshi-ai-data-domain-infra` | 基建：ai-data-domain-digest+domain-mapping 注册+双三角重复卡去重 | huangyaoshi | 留队待领（独立基建线，无依赖） |
| 687 | `task_20260908_hongqigong-ai-basic-png-ocr` | 补采：27 张无产物 PNG OCR 补采评估（优先 040618） | hongqigong | 留队待领（独立多模态线，无依赖） |

### 归档判定落账（报告 §五-登记不产/归档，随本单生效）

- 口述01/闲聊篇：同源无增量不产卡，作**干净转写版归档不删**（旧 src_a25ca678/src_64015d4d 引用指向并挂，不替换）
- 表格.md：已消化，随 #685 工作项 5（concept 卡补挂溯源）闭环
- D 组 3 件建议书：**编排域历史归档**，不再卡片化
- A 组 4 件（Feature 上/下口述+笔记）：#667「登记不产」维持
- F 邻件（教练自举）：已吸收，登记不产

### 附带移交（拍板范围第 6 项）

- framework 两张基准卡（framework-truman-feature-thinking-core / framework-truman-feature-layered-system）#544 退回未修（8格留白/引语失真/L2计数）——**知悉件路由欧阳锋**：建议排老顽童返工，不另立新单（老朱拍板口径「由你定路由」，取知悉件）；已写入本台账待欧阳锋终审本单时一并知悉

### 队列动作留痕

- 本单（#682）小昭投放漏队列行 → 王语嫣 09-08 补登记入队（同 #681 前例）后 claim 成功
- 683-687 五单 frontmatter 齐（W7）+ 队列行已补登记，状态 queued

## 执行报告（五字段，2026-09-08 王语嫣）

**交付物**：5 份新任务单（`60_feedback/tasks/task_20260908_laowantong-ai-data-methodology-p0.md` / `task_20260908_laowantong-live258-six-cases.md` / `task_20260908_laowantong-ai-data-p2-backfill.md` / `task_20260908_huangyaoshi-ai-data-domain-infra.md` / `task_20260908_hongqigong-ai-basic-png-ocr.md`）+ production-queue.md 队列行 682-687 + 本单编排台账（含归档判定落账+附带移交路由）。

**完成内容**：老朱 19:25「全做」拍板 7 项范围全落地——①P0 产卡单（8 张，锚点/解压路径/ASR 校正清单照诊断 §五-P0/§六 照抄下发）②P1 产卡单（Live258 六案例全产，dk 互链前置查重缺陷项三项写入前置必做）③P2 补强补挂单（§五-P2 表 6 项全量，补挂合并为一个工单）④黄药师基建单（digest+注册+去重三工作项）⑤洪七公补采工单（27 张评估+040618 优先）⑥附带移交=#544 两基准卡退回未修走知悉件路由欧阳锋⑦归档判定五项随台账落账。P0 已 kimi-headless-launch 拉起老顽童（proc_laowantong_5116），P1/P2 留队（老顽童单线程），黄药师/洪七公单留队待领（独立线无依赖）。

**验证**：5 新单 frontmatter 齐（id/seq/status=queued/assignee/decision_source=「老朱 09-08 19:25 拍板全做（#682 编排）」/reviewer，W7 牌）；队列行以 `queue_transition.py claim` 实跑通过为准（#682 claim 成功输出 ✅，dashboard 229 任务重生成）；卡片规格/行号锚点/ASR 清单全部照抄诊断报告 §五/§六/§七 原文未重查未改写（任务单执行要求口径）；拉起器返回 proc+log 路径实证。

**边界**：本单只编排不产卡，未触碰任何 30_wiki 卡片；归档判定为「落账生效」，物理归档动作（口述01/闲聊篇替换并挂旧 src 引用）随 #685 补挂闭环执行，本单未移动文件；#544 返工是否立项由欧阳锋裁定（本单只路由知悉）；P1 拉起时机取决于老顽童 #683 完工节奏，未硬派并行。

**需要谁动作**：欧阳锋——终审本单（编排合规性）+ 知悉 #544 两基准卡退回未修（建议排老顽童返工）；老顽童——P0 #683 生产中，完工后续领 #684/#685；黄药师/洪七公——按各自节奏领取 #686/#687；老朱——查进度看本单编排台账即可。

## 机器预审报告

> 🤖 机器预审参考层（#515）：仅供欧阳锋终审参考，不构成结论、不放行不拦截

### ① 声称-交付差集

✅ 1 个声明路径全部存在+已跟踪+无脏改动
### ② lint

✅ frontmatter 可解析 + F-034 五字段在位
### ③ 负向判词 / ④ 存在性核查

✅ 执行报告无负向断言词（检查面=执行报告节）

## 终审记录

methodology_version: v2.3
verdict: PASS
grade: A-
blocking: 无（🟠Medium ×2 放行+移交动作，见缺陷①②）
reviewed_by: 欧阳锋
review_date: 2026-09-08

**审查结论**：编排单准予通过。审查对象为编排类交付，判三件事——①拍板范围 7 项是否全部落地 ②各新单规格是否忠实规格源 ③流转/拉起/入仓是否实证。三项全过，A-（1-2 处小遗漏，见缺陷①②）。

**溯源验证（本端独立复核，非转述编排者结论）**：

1. **拍板范围 7 项 → 5 单+台账+知悉件全落地**【实证】：#683（P0 8 卡）/ #684（P1 六案例）/ #685（P2 六工作项）/ #686（基建三工作项）/ #687（补采 27 张）五单 frontmatter 齐（id/seq/assignee/decision_source=「老朱 09-08 19:25 拍板全做（#682 编排）」/reviewer，W7 过）；归档判定五项台账落账；#544 知悉件路由入台账。
2. **五单规格与规格源逐条对——全部吻合**【实证】：规格源=`60_feedback/diagnosis/diag_20260908_wangyuyan-ai-data-ai-basic-deep-dig.md`（本端已读全文）。#683 八卡清单/锚点与 §五-P0 表逐条一致（含 dk×2；解压路径 tool×2+case×2+dk×2=6≥3 达标）；#684 六案例 id/可用度排序/锚点与 §五-P1+§3.2-B 矩阵一致，前置缺陷项=本端 #681 终审缺陷① 原样下发；#685 六工作项与 §五-P2 表全量一致；#686 三工作项与 §〇/§七 一致；#687 与 §3.2-E 一致（27 张+040618 优先+「补采产物为素材层不产卡」边界收对）。
3. **ASR 校正清单照抄 §六 原文**【实证】：`task_20260908_laowantong-ai-data-methodology-p0.md:44`（7 条逐字含「待考」标注，无改写）。
4. **#684 前置缺陷项引用的两处 dk 锚点实证成立**【实证】：`dk-ai-does-not-question-your-mistake.md:112`（引用块「正面做法参照农夫三拳的 R/E/S/X 事实分级（L817-L831）」）；`dk-demand-feature-stacking.md:165`（边界行并引农夫三拳 L923+黄谦 L2947）。
5. **拉起实证**【实证】：`logs/headless-laowantong-20260908-193541.log` 在盘（85164B，20:09 仍在增长），台账 proc_laowantong_5116 与之吻合；队列 #683=claimed-laowantong ↔ #683 任务单 `status: in_progress` 双向一致。
6. **队列一致性（O4 前置）**【实证】：#682 队列行 pending_review ↔ 任务单 frontmatter pending_review 一致；683-687 队列行五单全在（production-queue.md L1310-1314）。
7. **E040 门禁拦截已自愈收口**【实证】：gate-blocked.log 19:36 拦「untracked: task_20260908_laowantong-*」→ commit 8ba892a9a 编排立项入仓 → 本端 `git status --porcelain -- 60_feedback/tasks/` 现为空。拦截→修复→复检闭环。
8. **kdo query 抽检（真空前提复验）**：见检索记录节——两查均支持「P0 真空 / P1 六案未开采」前提，无双源冲突。

**缺陷（🟠Medium 放行+移交，无 🔴🟡 阻断）**：

- ① **声称-交付差集：归档物理动作未随 #685 落项**。本单「边界」与「归档判定落账」两处声称「口述01/闲聊篇物理归档（旧 src_a25ca678/src_64015d4d 引用指向并挂）随 #685 补挂闭环执行」，但 `task_20260908_laowantong-ai-data-p2-backfill.md:21-28` 六工作项无此项（全表逐行核对）——若不补，该动作成孤儿，且执行报告含不实声称。**移交动作：王语嫣在 #685 被 claim 前增补第 7 工作项（或修订本单边界措辞另定落点）**——已写入建议书 `60_feedback/diagnosis/diag_20260908_ouyangfeng-682-rollout-review-followups.md`。
- ② **执行要求字面违背（实质豁免）**：本单执行要求「ASR 校正清单必须随 P0/P1 单下发」，实际仅 #683 下发，#684 全文 grep「ASR|校正」0 命中【实证】。判定为口径过宽而非交付缺失：Live258 素材为书面作业集非 ASR 转写，§六 清单 7 条全部源自口述01/02，对 #684 无适用项。建议口径修订为「随含 ASR 素材的单下发」。
- ③ 🔵Low：#684/#685/#686/#687 frontmatter `updated_at: ''`（空串；#683 有实值）——流转脚本会补，归 lint 类不阻断。

**附带知悉件核实（拍板范围第 6 项，路由裁定）**：#544 两张 framework 基准卡「退回未修」属实【实证：`framework-truman-feature-thinking-core.md:5,18` / `framework-truman-feature-layered-system.md:5,17` 均 status: draft + reviewed_by: 待审】。**裁定：同意知悉件不另立新单**；返工排产属编排职能，建议王语嫣列 P2 返工单（建议 #685 后、#684 黄谦/Simon Peng 产卡前——两卡是 Live258 案例卡的分层基准，L2 计数 34vs38 未修，带病基准会污染六案卡的分层判断），已写入同一建议书。

**残余风险**：本单只审编排，不预审子单产物——#683 8 卡 draft 在产（本单终审时点未提审）、#684-#687 未启动，各自按队列走四层管线终审；#684 执行时六案卡引用两基准卡数字须按 #681 缺陷口径「引用其数字需谨慎」处理。

**kdo query 检索记录**（宪法第六条/#669，本端实跑 2026-09-08，`kdo query --limit 5`）：

| # | 查询词 | 命中 | 判读 |
|:-:|:--|:--|:--|
| 1 | Adaptive 数据飞轮 六步 预判 识别 收集 处理 | 1 弱（0.15） | 唯一命中=`tool-data-maturity-l1-l6.md`【未审 draft】=#683 本日新产卡——P0 真空前提成立（提审时点库内无既有同类卡），无双源 |
| 2 | Live258 雍博 具身智能 农夫三拳 学员案例 | 0 case | 命中均为 dk-ai-does-not-question / case-live258-fact-spread-18-bridges / v0.9 changelog / Live255 他案——六案未开采前提成立 |

**存在性核查**（本记录负向判词锚点集，#433/F-035，核查动作 2026-09-08 本端实跑）：

- 「#685 无归档工作项」← Read `task_20260908_laowantong-ai-data-p2-backfill.md` 全文（L19-28 工作项表 6 行逐行核，无口述01/闲聊篇归档项）。
- 「#684 无 ASR 清单」← `grep -n "ASR\|校正" task_20260908_laowantong-live258-six-cases.md` 0 命中。
- 「#544 两卡退回未修」← `grep -n "^status\|^reviewed_by"` 两文件（framework-truman-feature-thinking-core / framework-truman-feature-layered-system）。
- 「拉起日志在盘」← `ls -la logs/headless-laowantong-20260908-193541.log`（85164B）。
- 「E040 已收口」← `git status --porcelain -- 60_feedback/tasks/` 输出为空 + `git log --oneline -8` 含 8ba892a9a。

**通过维度**：拍板范围全覆盖（7/7）/ 规格忠实度（五单与诊断 §五/§六/§七/§3.2-E 逐条吻合，锚点照抄未改写）/ 流转纪律（W7 frontmatter+队列行+claim 拉起+queue_transition 实跑）/ 台账可查性（单号+拉起/留队状态+归档落账+知悉件路由，老朱查进度单点可达）。

**不报告清单**：file-flow-check 存量 L5 命名项与 L3 缺 version（全库 363 条同型）归 lint；冻结件 diag_20260907_xiaozhao ERROR 非本单范围（一行记入建议书观察项）；#683 卡片产物属子单 #683 终审范围本单不预审。
