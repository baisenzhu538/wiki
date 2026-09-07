---
id: force-exception-labeling-baseline-20260831-0906
title: "force 放行率人工标注基线报告（#678）：35 例逐例标注，真误判率 0%，代理值 20.8% 高估"
type: improvement-plan
status: reviewed
domain: infrastructure
author: 老顽童
reviewed_by: 欧阳锋（王语嫣抽 5 复核双签在案，2026-09-07 终审 PASS A-）
confidence: 0.9
trust_level: high
created_at: '2026-09-07'
updated_at: '2026-09-07'
source_refs:
  - 90_control/force-exceptions.log
  - 90_control/quality-metrics-spec-v1.md
  - 60_feedback/auto/quality-metrics/2026-08-31_2026-09-06.md
  - 60_feedback/diagnosis/diag_20260907_xiaozhao-three-day-audit.md
  - kdo-tools/quality_metrics.py
  - 90_control/scripts/queue_transition.py
  - kdo-tools/conveyor_probe.py
  - .agent/friction-log.md
aliases:
  - force-exceptions
  - force 放行率
  - 真误判率基线
  - queue_transition
  - quality_metrics
  - conveyor_probe
tags:
  - audience:ouyangfeng
  - scene:gate-tuning
  - 队列门禁
  - force台账
  - 误判率标注
  - 质量周报
  - 状态机
  - 审查等待期
related:
  - "[[quality-metrics-spec-v1]]"
  - "[[diag_20260907_xiaozhao-three-day-audit]]"
---

# force 放行率人工标注基线报告（#678，窗口 2026-08-31 ~ 2026-09-06）

> **任务**：task_20260907_laowantong-force-exception-labeling（小昭三天审计建议 1，王语嫣裁定立项 P1）
> **执行**：老顽童（laowantong）2026-09-07 ｜ **验收**：35/35 标注表 + 本基线报告 + 王语嫣抽 5 复核
> **机读对账**：`90_control/force-exception-labels-20260831-0906.json`（35 行，逐行含台账行号/task/instance/bypass/阻塞类型/判定/理由）

## 一句话结论

**35/35 全部标注为「合法逃生门」，真误判率基线 = 0%（0/35）**【实证——逐例锚点见第三节表】。20.8% 的 force 放行率作为「门禁误判」代理值**严重高估**：其中 8.6%（3/35）是机器豁免记账根本不是人工绕行，57%（20/35）是 #504 渠道缺口（已由 #655 --sequence 根治），26%（9/35）正是 --force 的设计意图场景（跨 assignee 并行）。**不建议按代理值直接收口**；收口方案见第五节，核心是「分类收口」而非「一刀切」。

## 一、口径与范围（35 例怎么数出来的）

| 步骤 | 数值 | 锚点 |
|:--|:--|:--|
| force-exceptions.log 全量 | 44 行【实证】 | `90_control/force-exceptions.log`（08-25 起） |
| 落在周报窗口 08-31~09-06 | 37 行【实证】 | 日期切片实测 |
| 周报口径（脚本只认 `HH:MM:SS｜` 格式行） | **35 例**【实证】 | `kdo-tools/quality_metrics.py:39` `_FORCE_RE`——09-06 12:20/12:25 两条王语嫣手工破窗记录（无秒位格式）**天然不入分子**，属 #537 破窗台账另一族，不在本表 |
| 周报代理值 | 20.8% = 35÷168【实证】 | `60_feedback/auto/quality-metrics/2026-08-31_2026-09-06.md:10` |
| spec 对「真误判」的定义 | 需人工标注「拦截是否正确」【实证】 | `90_control/quality-metrics-spec-v1.md` §4（本件即该条要求的标注样本） |

## 二、kdo query 检索记录（宪法第六条 #669）

| # | 查询词 | 命中数 | 相关命中 | 日期 |
|:--|:--|:--|:--|:--|
| 1 | force 放行率 门禁 收口 基线 | 8 | 0（Christensen 等无关卡） | 2026-09-07 |
| 2 | 小昭 三天审计 force-exceptions 误判 | 8 | 0 | 2026-09-07 |
| 3 | force 例外 台账 逃生门 队列门禁 | 5 | 0（queue-transition SKILL 仅 0.02 弱命中） | 2026-09-07 |
| 4 | gate force exception ledger misjudge baseline（英文变体） | 5 | 0 | 2026-09-07 |

**降级说明**：4 次检索 0 相关命中 → 按宪法第六条降级口径②（非知识类检索：日志/代码/配置）使用 grep/git 定位证据。本域全部证据源为工程工件：`90_control/force-exceptions.log`、`kdo-tools/quality_metrics.py`、`90_control/scripts/queue_transition.py`、`kdo-tools/conveyor_probe.py`、`.agent/friction-log.md`、git log（生产队列文件）。

## 三、35/35 标注表

**判定标准**（对齐任务单口径）：
- **真误判**＝不该放行：门禁拦得对，force 属违规绕行（越权生产/破坏审查次序/造成返工或质量事故）。
- **合法逃生门**＝force 设计意图内：拦截对象是数据残缺/渠道缺口/他单并行占位，force 是台账留痕的正当补救。

| 台账行 | 时间 | 任务 | 实例 | bypass | 阻塞类型 | 判定 | 理由（含锚点） |
|:--|:--|:--|:--|:--|:--|:--|:--|
| 4 | 08-31 02:17 | #537 | conveyor_probe | matrix 登记核查（matrix_exempt） | exempt-bookkeeping(非拦截,机器留痕) | 合法逃生门 | 机器豁免记账：conveyor_probe.py:1386-1391 对任务单声明 §3.19 豁免者自动写台账，非人工绕行决策；任务单豁免声明存在性核查 3/3 命中。建议移出 force 放行率分子 |
| 5 | 08-31 02:17 | #580 | conveyor_probe | matrix 登记核查（matrix_exempt） | exempt-bookkeeping(非拦截,机器留痕) | 合法逃生门 | 同 L4：机器豁免记账非人工绕行；任务单声明 §3.19 豁免（grep 命中） |
| 6 | 09-01 06:17 | #586 | laowantong | F-034 交付五字段 | complete-gate(F-034) | 合法逃生门 | 状态机残缺值修复：队列行裸 claimed（08-31 headless 残写）归一化为 claimed-laowantong 走正规 complete 门禁；交付 7 commit 已入仓（61e755cc5..cc981dd7b，reason 原文）；终审 PASS A- |
| 7 | 09-01 07:20 | #586 | laowantong | F-034 交付五字段 | complete-gate(F-034) | 合法逃生门 | 终审 FAIL 返工重提：6 项清单修复+pre-submit 16/16 PASS+faa13f1ff 入仓（reason 原文）；该场景后经 #580/F-064 制度化（rework:true 自动豁免）；终审 PASS A- |
| 8 | 09-01 10:14 | #590 | huangyaoshi | pending_review 阻塞（#504 审查等待期占位） | fifo-other | 合法逃生门 | FIFO 他单阻塞（#587 王语嫣单）——--force 设计意图正中（queue_transition.py:684 不同 assignee 并行）；终审 PASS A- |
| 9 | 09-01 10:37 | #588 | huangyaoshi | pending_review 阻塞（#504 审查等待期占位） | own-pending(#504) | 合法逃生门 | own-pending 连发链：老朱直令派活撞 #504（friction-log.md:106 同族实证）；相邻 claim 间隔 23min 链序特征；终审 PASS A- |
| 10 | 09-01 11:49 | #592 | huangyaoshi | pending_review 阻塞（#504 审查等待期占位） | own-pending(#504) | 合法逃生门 | 同链第 3 单（#590→#591 占位）；终审 PASS B+ |
| 11 | 09-02 00:09 | #596 | laowantong | pending_review 阻塞（#504 审查等待期占位） | fifo-other | 合法逃生门 | FIFO 他单阻塞（#595）——设计意图内；终审 PASS A- |
| 12 | 09-02 00:10 | #598 | wyy-cli-0902 | pending_review 阻塞（#504 审查等待期占位） | fifo-other | 合法逃生门 | FIFO 他单阻塞（#595）——设计意图内。附注：instance=wyy-cli-0902 与 assignee=huangyaoshi 不一致，代持 86min 后 release 让渡（git 8cc84591c→aed390eb5→b8699dd86），生产由 huangyaoshi 完成并 PASS A-，无越权产出 |
| 13 | 09-02 00:53 | #599 | skills-assistant | pending_review 阻塞（#504 审查等待期占位） | fifo-other | 合法逃生门 | FIFO 他单阻塞（#596）——设计意图内；终审 PASS A- |
| 14 | 09-02 01:36 | #598 | huangyaoshi | pending_review 阻塞（#504 审查等待期占位） | fifo-other | 合法逃生门 | FIFO 他单阻塞（#602）——散点治理批编排（git 42ba61a31 09-02 01:27 立项 #600-#605，老朱拍板）后正式领取；终审 PASS A- |
| 15 | 09-02 01:37 | #600 | huangyaoshi | pending_review 阻塞（#504 审查等待期占位） | own-pending(#504) | 合法逃生门 | own-pending 连发链：编排批（42ba61a31）第 2 单，立项后 10min；终审 PASS A |
| 16 | 09-02 01:39 | #601 | huangyaoshi | pending_review 阻塞（#504 审查等待期占位） | own-pending(#504) | 合法逃生门 | own-pending 连发链：编排批第 3 单；终审 PASS A- |
| 17 | 09-02 01:55 | #603 | huangyaoshi | pending_review 阻塞（#504 审查等待期占位） | own-pending(#504) | 合法逃生门 | own-pending 连发链：编排批第 4 单（git 9246bf063 #601 complete 同分钟接续）；终审 PASS A- |
| 18 | 09-02 02:27 | #606 | laowantong-kimi | pending_review 阻塞（#504 审查等待期占位） | fifo-other | 合法逃生门 | FIFO 他单阻塞（#601 huangyaoshi 在产单）——设计意图内；终审 PASS A- |
| 19 | 09-02 08:10 | #611 | laowantong-kimi | pending_review 阻塞（#504 审查等待期占位） | fifo-other | 合法逃生门 | FIFO 他单阻塞（#608）——设计意图内；终审 PASS A- |
| 20 | 09-02 23:12 | #621 | huangyaoshi-kimi | pending_review 阻塞（#504 审查等待期占位） | own-pending(#504) | 合法逃生门 | own-pending 连发链（huangyaoshi-kimi 会话）；终审 PASS A |
| 21 | 09-03 00:21 | #625 | huangyaoshi-kimi | pending_review 阻塞（#504 审查等待期占位） | own-pending(#504) | 合法逃生门 | own-pending 连发链【推断：模式同 friction-log.md:139-140 实证族，相邻 claim 分钟级；结局 PASS A-】 |
| 22 | 09-03 00:38 | #620 | huangyaoshi | pending_review 阻塞（#504 审查等待期占位） | own-pending(#504) | 合法逃生门 | own-pending 连发链【推断：同上】；终审 PASS A- |
| 23 | 09-03 00:38 | #623 | huangyaoshi | pending_review 阻塞（#504 审查等待期占位） | own-pending(#504) | 合法逃生门 | own-pending 连发链（与 L22 同分钟双连）【推断：同上】；终审 PASS A- |
| 24 | 09-03 01:07 | #620 | conveyor_probe | matrix 登记核查（matrix_exempt） | exempt-bookkeeping(非拦截,机器留痕) | 合法逃生门 | 机器豁免记账（同 L4）；任务单声明 §3.19 豁免 |
| 25 | 09-03 01:34 | #628 | huangyaoshi | pending_review 阻塞（#504 审查等待期占位） | own-pending(#504) | 合法逃生门 | own-pending 连发链：#627/#628 双单同会话（git 91f177379 提审留痕实证）；终审 PASS A- |
| 26 | 09-05 03:46 | #646 | huangyaoshi | pending_review 阻塞（#504 审查等待期占位） | own-pending(#504) | 合法逃生门 | own-pending：编排直令（git 558dd4182 09-05 03:45『编排：#646 Sysmon CAS溯源+冻结止血+坚果云轮换』）；终审 PASS A- |
| 27 | 09-05 04:27 | #646 | huangyaoshi | pending_review 阻塞（#504 审查等待期占位） | claimed-lock(#503) | 合法逃生门 | claimed-lock 交接竞态：04:11 release #646 避让 #645 返工（git dfbc14a17——无双开作业实证）→ 04:27 #645 complete（1c9e52c6e）同分钟 #646 再 claim，锁未清即领；无并发生产危害，两单均 PASS A- |
| 28 | 09-05 04:28 | #643 | laowantong | pending_review 阻塞（#504 审查等待期占位） | own-pending(#504) | 合法逃生门 | own-pending 同会话链：git 04:25 #642 claim→04:27 complete→04:28 #643 claim；decision_source=老朱 09-05 检验设计直令；终审 PASS A- |
| 29 | 09-06 01:56 | #647 | huangyaoshi | pending_review 阻塞（#504 审查等待期占位） | own-pending(#504) | 合法逃生门 | own-pending 连发链：friction-log.md:139 实证『用户一指令派两单』族；终审 PASS A- |
| 30 | 09-06 02:04 | #648 | huangyaoshi | pending_review 阻塞（#504 审查等待期占位） | own-pending(#504) | 合法逃生门 | own-pending 连发链（同 L29 族）；终审 PASS A- |
| 31 | 09-06 02:53 | #649 | huangyaoshi | pending_review 阻塞（#504 审查等待期占位） | own-pending(#504) | 合法逃生门 | own-pending 连发链（同 L29 族）；终审 PASS A- |
| 32 | 09-06 03:47 | #650 | huangyaoshi | pending_review 阻塞（#504 审查等待期占位） | own-pending(#504) | 合法逃生门 | own-pending 连发链：friction-log.md:140 实证『用户一指令派三单链』；终审 PASS A- |
| 33 | 09-06 04:17 | #651 | huangyaoshi | pending_review 阻塞（#504 审查等待期占位） | own-pending(#504) | 合法逃生门 | own-pending 连发链（同 L32 族）；终审 reviewed/欧阳锋 |
| 34 | 09-06 04:33 | #652 | huangyaoshi | pending_review 阻塞（#504 审查等待期占位） | own-pending(#504) | 合法逃生门 | own-pending 连发链（同 L32 族）；终审 PASS A- |
| 35 | 09-06 05:54 | #653 | huangyaoshi | pending_review 阻塞（#504 审查等待期占位） | own-pending(#504) | 合法逃生门 | own-pending 连发链（同 L32 族）；终审 PASS A- |
| 36 | 09-06 06:03 | #655 | huangyaoshi | pending_review 阻塞（#504 审查等待期占位） | own-pending(#504) | 合法逃生门 | own-pending 连发链末单＝#655 本尊：claim --sequence 修复任务自身亦只能 force 领取——渠道缺口生于痛点自证；上线后同场景走 --sequence 不再入台账（queue_transition.py:686-687）；终审 PASS A- |
| 39 | 09-06 12:44 | #661 | duanwangye | pending_review 阻塞（#504 审查等待期占位） | fifo-other | 合法逃生门 | FIFO 他单阻塞（#658 laowantong 单）——设计意图内（段王爷 datapack 并行）；终审 PASS A- |
| 40 | 09-06 12:44 | #660 | hongqigong | pending_review 阻塞（#504 审查等待期占位） | fifo-other | 合法逃生门 | FIFO 他单阻塞（#658）——设计意图内（洪七公 datapack 并行）；终审 PASS A- |

## 四、基线统计

| 阻塞类型 | 例数 | 占比 | 判定 | 性质 |
|:--|:--:|:--:|:--:|:--|
| exempt-bookkeeping（matrix 豁免机器留痕） | 3 | 8.6% | 合法逃生门 | **非绕行**——记账噪音，污染分子 |
| complete-gate（F-034） | 2 | 5.7% | 合法逃生门 | 状态残缺修复×1 + 返工重提×1（后者已制度化 #580/F-064） |
| fifo-other（他单 FIFO 占位） | 9 | 25.7% | 合法逃生门 | **设计意图正中**（queue_transition.py:684）——特性非缺陷 |
| own-pending（#504 审查等待期） | 20 | 57.1% | 合法逃生门 | **渠道缺口**——#504 不区分「等终审空闲 vs 显式连单/编排直令」（friction-log.md:106,139,140），已由 #655 --sequence 根治 |
| claimed-lock（#503 同实例锁） | 1 | 2.9% | 合法逃生门 | 交接竞态（release→complete 同分钟 re-claim），git 实证无双开作业 |
| **真误判（不该放行）** | **0** | **0%** | — | — |

**结局核查**【实证】：35 例涉及 31 个唯一任务，**31/31 终审 PASS（A/A-/B+）且 status=reviewed/reviewed_by=欧阳锋**（production-queue.md 划销行+任务单 frontmatter 双源核对）；关键阻塞任务（#645 等）亦全部收口。零因 force 引发的越权生产、审查次序破坏、FAIL 返工或卡死。断言三级标注：表内 31 例为【实证】（git/文件锚点在列），L21/L22/L23 的连发链归因为【推断】（模式与结局实证、派单指令原文未逐条留存）。

## 五、对门禁收口的含义（以基线为据，供欧阳锋/王语嫣裁定）

1. **不要按 20.8% 一刀切收口**——代理值由三类性质迥异的成分构成，直接压 force 会误伤跨 assignee 并行（设计意图）与编排直令连发（已开正道）。
2. **分子去噪（低成本高收益）**：`quality_metrics.py` 把 `bypass=matrix 登记核查（matrix_exempt）` 移出分子或单列「豁免记账」——3/35 是 conveyor_probe 自动写账（conveyor_probe.py:1386-1391），不是人力绕行。去噪后本周真实 force 放行率 ≈ 32/168 = 19.0%。
3. **own-pending 类转 HARD 的时机已到**：#655 --sequence 上线（09-06）后，「编排直令连发」有预期流正道（不入 force 台账，queue_transition.py:686-687）。建议观察 1-2 周确认 --sequence 被实际采用后，把 own-pending force 从「留痕放行」升为「默认拒绝、需更强理由」——这是唯一一类该收口的。
4. **fifo-other 保留现状**：这是 --force 的设计场景，建议只观察占比不设上限；配合拦截率分母改良（spec 已注明 claim 无机器留痕）另案。
5. **F-034/claimed-lock 保留**：低频（2+1 例/周）且均为修复型使用，台账+胶囊事件留痕已足够（#444/#504/#511 机制运转正常）。
6. **窗口外参考**【实证】：09-07 新增 4 条（L41-44）中 L42 的门禁报错已自动提示「编排指令多单连发场景用 claim --sequence（#655）」——根治机制在引导用户走正道，收口可期。

## 六、边界

- 本标注只覆盖 08-31~09-06 窗口（周报 35 例口径）；窗口外 9 条（3 条 08 月 + 09-07 的 4 条 + 2 条手工破窗）未标注，不影响本周基线。
- 「真误判=0」是**本窗口**结论，不是 force 无害的一般性结论——0 主要因为渠道缺口已被 #655/#580 及时根治；若未来同类 force 再密集出现且无正道，应重开标注。
- 终审 PASS ≠ 内容零缺陷（抽验级质量由欧阳锋终审把关）；本报告只用它回答「force 是否造成流转层伤害」。
- 王语嫣抽 5 复核建议覆盖异类：L12（实例不一致代持）、L27（claimed-lock 竞态）、L6（状态残缺修复）、L36（#655 自身）+ 任一 fifo-other。
