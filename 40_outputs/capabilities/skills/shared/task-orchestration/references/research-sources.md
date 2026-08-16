# 编排者调研溯源（2026-08-09）

> 每条硬规则的外部文献溯源 + 反例 + 边界论证。SKILL.md 只存精简规则，完整论证在此。

## 调研方法

- 3 组主题 6 个 WebSearch 查询，动态饱和达成（≥2 独立来源交叉验证 or 1 来源否定 or 3 搜索词无果→存疑）
- 6 层交叉验证：来源/时间/逻辑/数据/反例/行动六层全过（诊断报告 diag_20260809_wangyuyan-orchestrator-evolution.md §二）
- 9 层深挖：L1 业务公式 → L4 失败模式（KDO 实证 #201/#197/E019/E018）→ L9 决策框架（§三）

## 硬规则 1：审查返工 3 轮封顶

**外部来源**：
1. Reflexion（Shinn et al.）/ Self-Refine（Madaan et al.）生产实践综述：bounded loops with stop rules——cap at 1-3 rounds，quality goes flat by pass 3 and negative by pass 5（over-optimization）；early-exit 当 critic 无 actionable issues（taskade.com/blog/self-improving-ai-agents-reflection, futureagi.com reflection tuning）
2. Addy Osmani Code Agent Orchestra (2026-03)：loop guardrails——hard iteration caps、kill and reassign after 3+ stuck iterations；"Generation is no longer the bottleneck. Verification is."

**KDO 内部实证**：#201 解放思想探索营七轮审查（2026-07-26）、#197 欧阳锋三审（初审 FAIL→二审误判→三审 PASS）

**反例与边界**：
- 反模式：uncapped loops over-correct（无限循环过度修正）；sycophantic critics（谄媚审查——用 rubric 约束）
- 边界：适用于"同一任务的审查循环"；跨任务迭代、开放创意探索不封顶
- 误用风险：第 3 轮"随便过"——配套升级路径（人工裁定/整卡重写）保证质量追求不消失只换路径

## 硬规则 2：WSJF 轻量分诊

**外部来源**：
1. SAFe WSJF = Cost of Delay / Job Size，CoD = Business Value + Time Criticality + Risk Reduction（Fibonacci 相对打分）
2. agentic-dev-orchestrator（danieleschmidt）：用 WSJF 排序分派编码任务给 agent workers（含重试处理）
3. loop-engineering issue-triage：P0-P3 分桶 + human ownership of P0/P1 + 连续分诊状态文件

**KDO 内部实证**：P0/P1/P2 直觉排序无量化复算（E013 队列协议违反、#234 返工教训说明排序决策需要可复现依据）

**反例与边界**：WSJF 全量打分过重（Fibonacci 20 点）——本 skill 用 1/2/3 粗粒度；WSJF 是相对排序不是绝对值，两任务分数相同则按队列原则（用户意图优先/依赖后置）

## 硬规则 3：首交通过率跟踪

**外部来源**：
1. Content ops playbook（teambench.ai / thinkitmedia / headlesscms.guide 2026 多篇）：first-submission pass rate 是最重要指标；AI quality gates 把人工从 30-60min 降到 5-10min（人做判断不做检查清单）；quality gate 阈值 65→82 随成熟度上升
2. RankDraft enterprise content ops：1,000+ pieces/month 场景 tiered four-gate review + weekly quality scorecards

**KDO 内部实证**：dashboard 无此字段；E019 状态流转 4 次违反依赖人提醒——指标化可让纪律可见

**反例与边界**：首交率不是"打压返工"的鞭子——返工轮次是规格质量的反馈信号（首交率低 = 编排侧规格问题，先查任务单规格再查生产执行）

## 机制 4：队列健康例行扫描

**外部来源**：
1. sipag triage：automated backlog review against VISION/ARCHITECTURE——CLOSE/ADJUST/KEEP/MERGE 处置 + dry-run/apply 模式
2. loop-engineering issue-triage：discover→deduplicate→score→bucket→state file，连续运行

**KDO 内部实证**：#265 通道 4 每周一例行已存在（进化信号周报+反馈闭环）——队列健康扫描是其天然扩展

## 机制 5：Cascade reflection

**外部来源**：
1. Cascade reflection 模式：先跑 fast deterministic checker，只对 flagged 调用 critic-then-refiner，省 50-80% 成本（反射循环生产实践）
2. 不同模型做 generator/critic 打破共享盲点（reflection 实践共识）
3. Anthropic common workflow patterns：evaluator-optimizer 只在质量可测提升时值得

**KDO 内部实证**：kdo pre-submit/lint 确定性检查已前置；老顽童(deepseek) vs 欧阳锋(kimi) 跨模型审查天然优势——显式化为原则而非巧合

## 反例全集（调研发现的常见陷阱）

| 陷阱 | 说明 | 本 skill 对策 |
|:--|:--|:--|
| uncapped loops | 无限返工循环过度修正 | 硬规则 1 三轮回台封顶 |
| sycophantic critic | 谄媚审查"看起来很好" | 轮次+首交率数据化，欧阳锋 rubric 约束 |
| 同模型双角色 | 生成与审查共享盲区 | 保持跨模型审查（KDO 现状） |
| LLM 自生成规则有害 | ETH Zurich：LLM 生成 AGENTS.md -3% success/+20% cost，人工写 +4% | 本 skill 规则全部人工调研+人工裁定 |
| 集中式 vs 去中心化摇摆 | 集中式更易观察/治理（多数生产系统选择） | KDO 集中式编排（王语嫣+欧阳锋）保持 |
| schema 过度设计 | 一次性设计全字段（王语嫣 2026-08-09 教训） | WSJF 用 1/2/3 粗粒度，够用即可 |
