---
name: task-orchestration
description: 任务编排者工作台——分诊排序、返工轮次护栏、首交通过率跟踪、队列健康例行扫描。触发词：排任务、入队、队列排序、分诊、这个任务什么优先级、返工几轮了、首交率、队列健康检查、审查循环、WSJF。负面例子：不要用于诊断素材内容本身（那是 stage-1-diagnose）、不要用于卡片生产（那是 content-production）。
version: 1.0.2
author: 王语嫣（2026-08-09 全网调研进化，溯源见 references/research-sources.md）
metadata:
  hermes:
    tags: [编排, 任务单, 队列, 分诊, 轮次护栏, 首交率, 编排者]
    related_skills: [entry-quality-gate, stage-1-diagnose, agent-self-iteration, six-layer-cross-validation, method-external-agent-feedback-production-loop]
---

# 任务编排者工作台（Task Orchestration）

> 王语嫣编排 = Feature 分层体系 L5 组织层的实战（framework-truman-feature-layered-system）。本 skill 把 2026-08-09 全网调研的三条硬规则 + 两个机制固化为编排日常动作。**每条规则都有外部文献溯源 + KDO 内部实证，完整溯源见 references/research-sources.md。**

## 触发词

排任务、入队、队列排序、优先级、分诊、这个任务什么优先级、返工几轮了、审查循环、首交率、队列健康检查、队列对齐

## 任务编排铁律（E025/E026，2026-08-09 用户确立——不可违反）

1. **修改另开新任务**：任何对已入队任务（queued/claimed/pending_review/reviewed）的调整（改名/规格/依赖/内容）一律**新增任务**，原任务单和队列行冻结不动（E025——污染审查链 = 乱套）
2. **一个任务 = 一个角色**：任务单 assignee 单一，跨角色工作必须**拆成独立任务 + 前后依赖**（E026）
3. **禁止双角色同任务**：同一任务禁止双 assignee；发现需要其他角色的工作 → 立即拆新任务，原任务注明"已拆出 #X"
4. **依赖衔接**：A 角色完成 → B 角色新任务依赖 A reviewed——用依赖链表达流程，不塞进同一任务

## 索引日常纪律（E028，2026-08-09 用户确立——检索索引随卡更新；2026-08-17 升级为强制项）

**每张卡生产完成（终审闭环）即写检索索引——日常增量，不做批量补救**：
1. **终审闭环时强制抽查（不可跳过）**：`kdo query` 用**自然语言**（用户会怎么问就怎么查，不只精确卡名）抽查 1-2 张新卡可命中——E028 两次复发（8-09/8-16）都是编排侧漏抽查，索引停在生产前、当天新卡检索不到
2. 索引滞后 = 检索盲区（卡在磁盘但查不到=不存在）——E028：85 卡落盘但 state.sqlite 停 7-19；8-16 索引停 04:38 当天 45 卡不可检（PatrolKit 查不到）
3. 编排侧：每批终审闭环时"索引抽查"为**强制收尾项**（与 E012 五步同步并列），不可因批次多/节奏快跳过
4. 工具侧：kdo 增量写入（单卡 index）由黄药师基建（#305 配套）；索引异常先重建（`kdo index`）再抽查

## 编排启动检查清单（2026-08-09 补丁，E021/E022 教训）

**任何编排动作前必跑两步（跳过 = 重复踩 E021/E022）**：

1. **队列全量对账**：任务单 frontmatter（id/status）vs 队列行全量比对——不信任何"已 closed/看板全清"类总结，只信对账结果。方法：脚本扫 60_feedback/tasks/ + 70_product/tasks/ 的 frontmatter status，与 production-queue.md 行比对；发现不一致 → 登记修复（E019 家族）
2. **域清单枚举**：新素材编排前查 `90_control/domain-mapping.md`（域清单单一真相源）枚举相关域 + grep 同域已有任务单的 domain 字段（如 human-insights）——以用户的认知地图（域）为坐标系，不以收件箱批次为坐标系（E022）


## 项目顶层文档（#339 制度，2026-08-16 生效——楚门"顶层文档制度"KDO 落地）

**项目立项 = 建顶层文档，作为编排固定动作**（试点：top-doc-爆炸式调研.md，终审 PASS A-）：

1. **何时建**：项目首个任务单入队时（跨 ≥3 任务单/有素材目录/长期演进/多角色——四条件满足即可）
2. **结构**：必知必会前置（30 秒读完：定位/核心产出/方法论/当前状态/约束）+ 参与方表 + 关键文档索引（素材/诊断/任务/产出卡/Agent 分类链接后置）+ 下一步
3. **维护节奏**：每批终审闭环时更新"当前状态"+"下一步"（顶层文档状态不得过期——制度第一个测试者就是它自己）
4. **命名**：`70_product/tasks/top-doc-<项目名>.md`（统一前缀，检索即得）
5. **定位**：顶层文档=项目总览态（任务单=生产态、队列=状态流、域 digest=域级顶层——同一思想的项目层）

## 硬规则 1：审查返工 3 轮封顶

**同一任务的审查循环第 3 轮仍未通过 → 停止循环，升级路径二选一：人工裁定（欧阳锋/用户拍板）或整卡重写。**

- 溯源：Reflexion/Self-Refine 生产实践——返工第 3 轮质量持平、第 5 轮过度优化转负（taskade 2026 / Reflexion 综述）；KDO 内部实证：#201 解放思想探索营七轮审查、#197 欧阳锋三审
- 执行：任务单记录审查轮次（初审/复审/R1/R2…）；达到第 3 轮时编排者主动发起升级，不等待
- 边界：只针对"同一任务的审查循环"；跨任务迭代不受限；开放创意探索不硬封顶

## 硬规则 2：WSJF 轻量分诊

**新任务入队排序 =（业务价值 + 紧急性 + 风险降低）÷ 体量，每项 1/2/3 粗粒度打分，复算 P0/P1/P2 直觉。**

- 溯源：SAFe WSJF（Weighted Shortest Job First）+ agentic-dev-orchestrator 实践
- 执行：入队时打分填任务单（value/urgency/risk/size 四字段），P0 要求 ≥6 分（如 2+2+2/1）；两任务难分先后时用分数决断，不用感觉
- 价值参考：用户明确意图/战略结论=3；高 ROI 桥接=2；修补=1。紧急性：阻塞依赖/有截止=3；本周=2；可排期=1。风险降低：无卡覆盖的新域=3；补链=2；格式修补=1。体量：≤3 卡=1；4-10 卡=2；>10 卡=3

## 硬规则 3：首交通过率跟踪

**编排侧记录每次任务"pre-submit 一次通过 / 返工 N 次"，月度汇入 dashboard。**

- 溯源：content ops playbook 共识——first-submission pass rate 是内容团队最重要的运营指标（teambench/thinkitmedia/headlesscms 2026）
- 执行：任务单验收记录增加"返工轮次"字段；每月从队列统计首交率 = 一次通过任务数 ÷ 总任务数；首交率持续 <50% → 规格质量问题（编排侧）而非执行问题（生产侧）
- 基线：从 #267+ 起记录，2026-08 底出首个基线

## 机制 4：队列健康例行扫描（CLOSE/ADJUST/KEEP/MERGE）

**并入 #265 通道 4 每周一例行：扫描队列全量任务，逐项对齐检查后给出处置。**

- 溯源：sipag triage（对齐 VISION 的自动 backlog 审查）+ loop-engineering issue-triage（连续分诊+状态文件）
- 检查项：① 是否仍对齐当前进化方向（kb-evolution-direction）② 是否被后到任务取代 ③ 优先级是否仍正确 ④ 是否重复
- 处置：CLOSE（已过时/已取消）/ ADJUST（优先级或规格修正）/ KEEP（保持）/ MERGE（与现有任务合并）
- 产出：一行队列健康摘要写回 kb-evolution-direction 或 dashboard

## 机制 5：Cascade reflection 显式化

**确定性检查先行，人工 critic 只处理 flagged 项。**

- 溯源：反射循环生产实践（先跑确定性 checker，critic-then-refiner 只在 flagged 时触发，省 50-80% 成本）+ Anthropic 编排模式
- 执行：生产端先跑 kdo pre-submit / lint（确定性），欧阳锋 critic 只审 flagged 差异项——人做判断，不做检查清单
- KDO 优势确认：跨模型审查（老顽童 deepseek vs 欧阳锋 kimi）天然打破共同盲区，保持现状不破坏

## 反模式（禁止）

- ❌ 无限审查循环："再改一轮就好了"——第 3 轮必须升级
- ❌ 直觉排序代替量化：两任务犹豫时必打分
- ❌ 自标 reviewed 无终审记录（E018）——首交率数据才会诚实
- ❌ 用本 skill 做素材内容诊断（那是 stage-1-diagnose 的职责）

## 适用边界

- 适用：任务单设计、队列排序、审查轮次管理、例行队列健康、首交率统计
- 不适用：素材内容诊断（stage-1-diagnose）、卡片生产（content-production）、卡片内容审查（欧阳锋职责）

## 关联

- `references/research-sources.md`——三条硬规则完整溯源 + 反例 + 边界论证
- `stage-1-diagnose`——诊断先行，本 skill 在诊断之后
- `entry-quality-gate`——提交质量门禁（首交率的数据源）
- `method-external-agent-feedback-production-loop`——#265 四回路（队列健康扫描并入其通道 4）
- `agent-self-iteration`——工具/配置问题走五步闭环，本 skill 不管配置层
