---
id: framework-ai-native-working-paradigm
title: "AI Native 工作范式——整链路以 AI 为主、人提供最小必要支持的组织设计法"
type: framework
status: reviewed
author: 老顽童
reviewed_by: 欧阳锋
confidence: 0.82
trust_level: high
language: zh-CN
created_at: 2026-09-06
updated_at: 2026-09-06
domain:
- ai-collaboration
- strategy
aliases:
- AI Native
- AI原生
- AI Native工作范式
- 人撤出
- 最小必要支持
- ANAT
- src_wechat_4b6327b374540e2e
- AI实战路径-五个层级全解析-口述
- 宣讲会：一堂-2026下半年AI大航海-口述
- AI native的工作链路
- d1-aidahangha-oral-notes
source_person: 一堂·AI大航海 20260905（宣讲会官宣 + AI实战路径案例互证，一堂创始人口径）
source_context:
- 定义出自宣讲会正式节（单源）；案例侧证出自 AI实战路径口述（同讲者第二场合讲）；「AI Native 无共识、正式课不提」（B33）——本卡是内部口径编译，非业界通用定义
- 引语已对逐字稿行号逐条回验；ASR 将 AI Native 误听为「ANAT」处已校正并标注
source_refs:
- 00_inbox/wechat-collect/src_wechat_4b6327b374540e2e.md
- 00_inbox/AI大航海20260905/宣讲会：一堂-2026下半年AI大航海-口述.txt:298-326
- 00_inbox/AI大航海20260905/宣讲会：一堂-2026下半年AI大航海-口述.txt:1482-1518
- 00_inbox/AI大航海20260905/AI native的工作链路.png
- 60_feedback/diagnosis/working/d1-aidahangha-oral-notes.md
related:
- '[[framework-ai-five-layer-architecture]]'
- '[[framework-encapsulation-methodology]]'
- '[[framework-lobster-opt-one-person-team]]'
- '[[case-360-overnight-course-rebuild]]'
- '[[case-ai-performance-review-trial]]'
- '[[case-digital-avatar-pricing-review]]'
- '[[bridge-yitang-kdo-dual-triangle-verification]]'
- '[[skill-five-layer-positioning]]'
- '[[agent-spec-kouspeng-task-decomposer]]'
- '[[concept-wanghuan-ai-native-definition]]'
- '[[framework-ai-native-organization-two-modes]]'
discoverable_by:
- AI Native
- AI原生
- 人撤出
- 最小必要支持
- 七问设计法
- 错误自动化
- 追浪造船
- 工作范式
quality_labels:
- framework
- principle
- actionable
- cited
tags:
- AI Native
- 五层架构
- 多Agent协作
- 编排
- 上下文工程
- 避坑
- 口述
- OPT
review_date: 2026-09-06
---
# AI Native 工作范式

> **定位声明**：本卡是一堂 2026 大航海两大主题（OPT × AI Native）中**组织维度**的那一半（讲者原话：一个目标是 OPT 个人维度、一个是 AI Native 组织维度，宣讲会:L320-326）。本卡回答「一条业务链路该怎么围绕 AI 重新设计」，是设计原则+设计工具，**不是**成熟度评级，**不是**「用 AI 多=Native」的进度条，也**不是**五层架构的替代（[[framework-ai-five-layer-architecture]] 回答用哪层，本卡回答链路怎么重构）。
>
> **知行合一判据（用户拿着能直接做什么）**：拿一条你正在跑的业务流程，过一遍 §七问设计法——七问里有三问答不上来，说明你只是在旧流程上「加点 AI」，还不是 Native。

## 正式定义（主锚）

讲者在宣讲会给出的思考原则（宣讲会:L304，逐字回验）：「我们能不能尝试着整个链路完全基于 AI 去设计」——从工作第一天开始，数据、整理、处理、执行全以 AI 为主，**把人撤出去**；人只在目标边界和关键判断节点提供支持（台账 B34）。

反面参照（L310，逐字回验）：传统模式下 AI 只在一个环节配合人，「人是那个过程中呢，我们叫这个传纸条」——人当胶水，贯穿全程。

**反例（什么不叫 Native）**（L300，逐字回验）：「在一个原有的流程，在这儿加点 AI」——在旧流程上叠加 AI 工具，不是 Native（台账 B33：AI Native 无共识、内部正式课也不提，这是讲者的内部口径而非业界通用定义）。

**走偏模式·错误自动化**（L318，逐字回验）：「追求所谓的自动化是容易的，但是它可能质量不够，数据不够，规则不清楚」，结果是「做了很多错误的自动化，没有意义」——对正确性敏感的业务，自动化先行=放大错误（台账 B35）。

## 双目标定位（OPT 与 AI Native 的关系）

| | OPT（个人维度） | AI Native（组织维度） |
|:--|:--|:--|
| 时间性 | 今天可确定性锻炼的路径 | 「我们长期去追求，并且一定程度上可抵达的方向」（L322-326，逐字回验；ASR 将 AI Native 误听为 ANAT，已校正） |
| 单位 | 一个人+一队 AI | 一条业务链路/一家公司 |
| 关系 | OPT 是 AI Native 的训练场；「OPC 只是 OPT 的一个小子集」（宣讲会:L216-270 OPT/OPC 完整论述段；台账该段跳号无 B26，以行号锚为准） | AI Native 是 OPT 积累到质变后的组织形态 |

**积累判据**（L586-588，逐字回验）：「你啥不做，怎么可能 AI Native 呢」——AI Native「不是许愿许出来」的，不是一蹴而就，是积累到一定程度之后的质变。配套自检清单：九个爽（见 [[framework-encapsulation-methodology]] §九个爽自检）。

## 七问设计法（设计工具，IMG7 直读）

把一条既有工作链拆开重问（视觉主图《AI native的工作链路》，D2 直读）：

1. 问题从哪里进入？
2. 资料如何收集？
3. 哪些对象需要建模？
4. 任务如何拆分？
5. 谁负责执行、谁负责验证？
6. 结果如何沉淀？
7. 新的认知如何重新写回系统、影响下一轮？

用法：七问逐条过现有流程；凡是「人在做」的环节，先问「这问能不能不改流程直接交给 AI」——能，是封装问题（[[framework-encapsulation-methodology]]）；不能且环节本身多余，才是流程重构问题。

## 人的位置（Native 不是无人）

1. **头尾在场，中间撤出**（A25，台账转述）：360 案例中人的位置=头部产品定义+尾部 1.5 小时细节把关，中间全 AI（实战路径:L144-148；案例展开 [[case-360-overnight-course-rebuild]]）。
2. **判断力是产出边界**（L1498，逐字回验）：「一个人的产出，来自于你的判断力」（L1498 逐字回验；同句后半列举判断对象：问题/标准/知识/封装）——撤出执行不撤出判断。
3. **人是瓶颈的清醒**（L1134，逐字回验）：「很多时候人是 AI 的瓶颈」——讲者发现自己加入某些业务环节效率反而变低；撤出+给足分工机制后系统表现更好。
4. **法权兜底（业界补充，2026-09 口径建议半年复核）**：目前没有任何法域承认无人公司，人名义上必须在位（对标节 ComplexDiscovery/Florio 观察）——Native 是工作范式，不是法人形态。

## 三场景（AI 落地在哪发生，L934-940 逐字回验）

1. **乙方 case 制**：帮别的公司一个 case 一个 case 做落地。
2. **一号位自落地**：自己就是公司一号位，在本公司跨场景落地——「我自己就是我自己公司的 To B」。
3. **内部 AIBP 流通**：一定规模的公司设 1-3 个 AI Business Partner，在各业务线之间流通（讲者口径：今年培养约 100 人，台账 B87）。

## 相信 AI 与打通一切（态度层，L1482-1490 逐字回验）

1. **相信 AI**：「我们相信 AI 作为一个生产力，它已经形成了足够强的技术能力」——不要因为偶尔犯错否定它（台账 B108：新人也会犯错；不行是我不行）。
2. **打通一切**：「AI 联动打通一切」——打通工具（不只给建议要执行）、打通角色、打通反馈、打通人和 AI 的关系（台账 B109）。
3. **高优情报**（L1488-1490，逐字回验）：「我们可能会正式发布 YI 和 CLI」——Agent 接上 CLI=接上一堂方法论（五步法/转化/人红点/清单体笔记）。对本库含义：见 Action Triggers 第 4 条。

## 业界对标（WebSearch 实测，2026-09-06）

| 一堂口径 | 业界同构 | 独立来源 |
|:--|:--|:--|
| 整链路基于 AI 设计、人撤出 | Zero-person startup：从第一天起按最小人工参与设计、Agent 承担决策执行 | ComplexDiscovery「Zero-Person Startups」；MIT Paul Cheek 的 Antonomy 实验 |
| AI 为主、人做关键判断 | 「AI handles the doing, people focus on deciding」 | McKinsey「AI-Native Operating Models vs Virtual AI Workers」框架 |
| 人撤出后效率反而高 | Agent-centric enterprise：Cursor 以约 60-100 人做到 $100M ARR（口径不一：MIT Press-HDSR 称 60 人，Bloomberg 2025 年初口径约 100 人，待独立核实） | MIT Press / Harvard Data Science Review「The Agent-Centric Enterprise」（2026） |
| 人在头尾=交接设计 | 交接流程的设计比监督本身更决定成败 | Dartmouth Tuck 实证研究（even with humans in the loop, handoff design matters more） |
| 错误自动化没有意义 | 无节制加人工审查与盲目自动化同属失败模式 | HoolaHoop「AI-Native Trust Paradox」；arXiv「AI Agents Push Humans Out of the Loop」 |

**对标来源清单（URL＋检索时点 2026-09-06；均为检索摘要级证据，未逐一直连核验，引用按 L3 多源/L5 单源分层对待）**：

1. ComplexDiscovery「Zero-Person Startups」：https://complexdiscovery.com/zero-person-startups-how-agentic-ai-is-shaping-a-new-business-frontier/
2. MIT Press / Harvard Data Science Review「The Agent-Centric Enterprise」（2026）：https://hdsr.mitpress.mit.edu/pub/0mrfxamu
3. McKinsey AI-Native Operating Models 口径（社媒转述，未直连原文，仅作方向参考）
4. Dartmouth Tuck（handoff design 实证）：https://tuck.dartmouth.edu/news/articles/even-with-humans-in-the-loop-agentic-ai-systems-struggle
5. arXiv「AI Agents Push Humans Out of the Loop」：https://arxiv.org/html/2608.23642v1
6. SiliconANGLE「Why 'human in the loop' falls short」（2026-05）：https://siliconangle.com/2026/05/31/human-loop-falls-short/
7. HoolaHoop「Agentic AI Governance」：https://hoolahoop.io/articles/cto-coaching/agentic-ai-governance/

**对标结论**：①「人撤出+最小必要支持」与 2026 年业界「zero-person/agent-centric」方向一致（≥2 独立来源，不标存疑）；② 一堂版的**增量**=把「错误自动化」立为明确反模式（业界多在谈治理，少把「自动化了错误的东西」立为一等失败模式）；③ 一堂版**保留判断力作为产出边界**，与 McKinsey 的 doing/deciding 二分同构。
**存疑标注**：业界「zero-person company」仍是愿景叙事+法律上不可达（无法域承认）；本卡的「人撤出」只主张工作层面，不主张法人层面。

## 知行合一：用户拿着能直接做什么

1. **七问体检**：拿一条在跑的流程过七问（§七问设计法），答不上三问=还没 Native，先补哪问问哪问。
2. **头尾站位**：画出你在这条链里的位置——如果你在中间（传纸条），把中间段封装掉，人挪到头尾。
3. **错误自动化自查**：任何自动化上线前问「这一步错了谁发现、多快发现」——答不出就先加验证节点，不自动化。
4. **追浪 vs 造船**：见 §dk。

### dk：追浪造船
- **维度标签**：长期主义
- 一句话：「有人追浪，有人造船。浪追完了，也就没了。船造好了，可能能陪着咱们走很远很远」（宣讲会:L1518，逐字回验）——追工具=追浪，封装体系=造船；AI Native 是船，不是浪。
- 锚：宣讲会:L1518（台账 B111）
- 使用边界：用于对抗工具焦虑；不用于拒绝评估新工具（该评估用 Feature 思维，见 [[framework-truman-feature-layered-system]]）。

## 失败模式

| 失败 | 症状（可识别信号） | 修复（今晚能做的动作） |
|:--|:--|:--|
| 旧流程加点 AI | AI 只在一个环节配合人，人还在中间传话 | 跑七问设计法，找出可整体删除的中间环节 |
| 错误自动化 | 自动化产出的错误没人发现、越积越多 | 每个自动化节点配一个验证节点+责任人 |
| 把「用了 AI」当 Native | 汇报里全是工具名，没有链路重构描述 | 用九个爽清单数封装存量，不数工具数量 |
| 人撤成放羊 | 撤出后质量崩、没人知道哪错了 | 先建分工机制与协作规则，再撤人（人是瓶颈的前提=机制已建） |
| 追浪式转型 | 每个新工具都重做一遍链路 | 按「相信 AI+打通一切」选一个主线工具栈，季度内不换 |

## Critique

### 外部攻击

**攻击 1（概念空转风险）**：讲者自己承认「AI Native 无共识（内部也没有，正式课不提）」（B33，台账）——一个没有共识的概念，凭什么立框架卡？
1. 回应：成立一半。本卡的处理是把「无共识」显式写进 source_context，并只锚定讲者的操作化定义（整链路 AI 为主+人最小必要支持+七问设计法）——本卡主张的是「一堂内部口径」，不是业界标准。消费者引用时应写「一堂口径的 AI Native」。
2. 残余风险：跨库交流时与业界 AI-native（技术栈原生，如 AI-native database）撞名——那是技术架构术语，本卡是工作范式术语，引用时带全称区分。
3. **库内口径并存（#654 抽检发现）**：[[concept-wanghuan-ai-native-definition]]（王欢 06-18 口径：AI Native=默认把 AI 纳入流程）是比本卡更弱的版本；[[framework-ai-native-organization-two-modes]]（控制台 vs 平台）是本范式的组织形态落位。三卡并存记录不合并——引用时注明口径版本（强口径=本卡，弱口径=王欢版）。

**攻击 2（幸存者+规模偏差）**：所有 Native 案例来自一个 30+ AI 并行的高手与其小团队；「完全循环的老业务比例不高」是讲者自己承认的现状（B35，台账）。
1. 回应：成立，采纳。处置：本卡全部案例锚到 case 卡并逐条标「自述口径待独立核实」；卡内明确「转型难、比例低」是基线现状，不是例外未提。
2. 存疑保留：3-6 个月涌现 10-几十个 Native 榜样的预期（B36）是讲者判断，无基线数据，不写入本卡主张。

### 不要用的场景

| 场景 | 为什么失效 | 替代方案 |
|:--|:--|:--|
| 正确性敏感且无验证手段的业务 | 错误自动化没有意义（L318） | 先建验证节点，再谈自动化 |
| 一次性小任务 | 链路重构成本高于收益 | 留在对话层/Agent 层（[[framework-ai-five-layer-architecture]] 层级经济学） |
| 团队没人会用上下文文档 | Native 的地基是封装与文档，缺地基必塌 | 先做第三层资产化（[[framework-encapsulation-methodology]]） |
| 评估技术栈选型（AI-native DB 等） | 本卡是工作范式术语，非技术架构术语 | 按技术架构评审流程另议 |

## Constraints & Boundaries

- 适用：业务链路的 AI 化重构设计、组织 AI 转型的目标定义、判断「真假 AI 化」
- 不适用：单点工具选型、正确性敏感且无验证手段的场景、法人形态层面的「无人公司」主张
- 溯源纪律：AI Native 为一堂内部口径（无业界共识），引用需带出处；业界对标只证方向一致，不等价

## Synthesis

三步编译收束：AI Native 的独立价值不在造词，而在三个可执行件：①**反例定义**（原有流程加点 AI 不叫 Native，L300）——给了一个证伪标准，比正面定义更锋利；②**七问设计法**（IMG7）——把「重构链路」从口号变成一张可以逐条打勾的清单；③**错误自动化**反模式（L318）——把「自动化质量不足」从技术问题升格为方向问题。与库内关系：OPT（[[framework-lobster-opt-one-person-team]]）是个人维度训练场，本卡是组织维度方向；五层架构（[[framework-ai-five-layer-architecture]]）是路径，本卡是路径的终点形态。与 KDO 的关系：本库的 queue 门禁+写审分离+文档体系是一堂口径 AI Native 的同构物——人（老朱）只做方向与拍板，产能与质检由 Agent 角色分工承担。

## Action Triggers

| 触发场景 | 第一个动作 | 成功指标 |
|:--|:--|:--|
| 老板说「我们要 AI 化」 | 用反例定义先问：是加点 AI 还是重构链路 | 会议纪要里出现链路图而不是工具清单 |
| 接手一条旧流程 | 跑七问设计法 | 七问每问有一句话答案或标「待建模」 |
| 自动化方案评审 | 查错误自动化三件套：质量/数据/规则 | 每个自动化节点有验证节点 |
| YI+CLI 发布（跟进情报） | 评估 Agent 接 CLI 的成本收益 | 本库产出一份接入评估纪要 |
| 团队出现工具焦虑 | 用追浪造船 dk 对话 | 季度内主线工具栈不换 |

## 迭代日志

- 2026-09-06 v1.0：#654 batch1 生产，据 D1 金矿台账（B33-B36/B87/B108-B110）+ IMG7 直读萃取；引语逐条回验逐字稿行号；业界对标 6 独立来源（ComplexDiscovery/MIT Press-HDSR/McKinsey/Dartmouth Tuck/arXiv/HoolaHoop）。
