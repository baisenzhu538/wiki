---
id: framework-encapsulation-methodology
title: "封装方法论——把一次性工作经验固化成可调用资产的六层形态与频次引擎"
type: framework
status: reviewed
author: 老顽童
reviewed_by: 欧阳锋
confidence: 0.84
trust_level: high
language: zh-CN
created_at: 2026-09-06
updated_at: 2026-09-06
domain:
- ai-collaboration
- kdo
aliases:
- 封装方法论
- 封装
- 六层形态
- DataPack
- 封装频次引擎
- 胶水传纸条
- 借假修真
- AI友好
- src_wechat_4b6327b374540e2e
- 宣讲会：一堂-2026下半年AI大航海-口述
- 封装的定义
- 封装的实现
- d1-aidahangha-oral-notes
source_person: 一堂·AI大航海 20260905（宣讲会封装正式节 + AI实战路径第三层，一堂创始人口径）
source_context:
- 定义出自宣讲会封装正式节（抢答互动：搭 OPT 最重要的动词=封装，B37）；六层形态出自视觉主图《封装的定义》（IMG1 直读）
- 引语已对逐字稿行号逐条回验；九个爽清单为台账结构化压缩（原文为连续问句），逐条锚已标
source_refs:
- 00_inbox/wechat-collect/src_wechat_4b6327b374540e2e.md
- 00_inbox/AI大航海20260905/宣讲会：一堂-2026下半年AI大航海-口述.txt:340-430
- 00_inbox/AI大航海20260905/宣讲会：一堂-2026下半年AI大航海-口述.txt:554-590
- 00_inbox/AI大航海20260905/AI实战路径-五个层级全解析-口述.txt:178-212
- 00_inbox/AI大航海20260905/封装的定义.png
- 00_inbox/AI大航海20260905/封装的实现.png
- 60_feedback/diagnosis/working/d1-aidahangha-oral-notes.md
related:
- '[[framework-ai-five-layer-architecture]]'
- '[[framework-ai-native-working-paradigm]]'
- '[[tool-ai-skill-engineering-guide]]'
- '[[method-anthropic-skill-design-patterns]]'
- '[[agent-spec-skills-assistant]]'
- '[[bridge-yitang-kdo-document-over-session]]'
- '[[bridge-yitang-kdo-skill-center-network]]'
- '[[case-yitang-eason-truth-delivery-audit]]'
- '[[framework-truman-feature-layered-system]]'
- '[[skill-five-layer-positioning]]'
discoverable_by:
- 封装
- 六层形态
- DataPack
- 数据包
- 频次引擎
- 借假修真
- AI友好
- 上下文文档
- 九个爽
- 胶水传纸条
quality_labels:
- framework
- principle
- actionable
- cited
tags:
- 封装
- 上下文工程
- 数据包
- 技能封装
- 复利
- 频次
- 避坑
- 口述
review_date: 2026-09-06
---
# 封装方法论

> **定位声明**：本卡是一堂 2026 大航海体系里「搭 OPT 最重要的动词」（宣讲会抢答互动，台账 B37）的展开——封装的定义、对象、去处、频次、形态与失败模式。它是资产化操作方法论，**不是**五层架构（[[framework-ai-five-layer-architecture]]，本卡服务于其中第三层「资产层」），**不是**某个具体工具的使用说明，也**不替代**本库已有的 Skill 工程卡（[[tool-ai-skill-engineering-guide]] / [[method-anthropic-skill-design-patterns]]——那两张讲「怎么做一个好 Skill」，本卡讲「为什么要封装、封装成什么、多久封装一次」）。
>
> **知行合一判据（用户拿着能直接做什么）**：项目做完收尾时，强制回答一个问题——这次学到的什么，能固化成「下次同类问题不用从零开始」的东西？答不出=白干一次；答得出，按 §六层形态 选个形态封装掉。

## 正式定义（主锚）

宣讲会正式节（L346，逐字回验）：面对「一次性的工作经验」，「封装的意思是我要尝试把它固化」——固化进未来可被调用的结构（台账 B38）。

一句话版（L352，逐字回验）：「封装的意思是把经验沉淀成系统」。

概念澄清（L358，逐字回验）：封装是「一个抽象和固化的过程」——是抽象+建模，不是把文件打包塞进文件夹（台账 B39）。**判断标准**：封出来的东西没有经过抽象（换个场景还能不能用？），就只是归档，不是封装。

## 封装什么：四对象与频次引擎

**四对象**（L362，逐字回验）：「要封装知识封装能力封装流程封装角色」（台账 B40：知识/能力/流程/角色）。

**频次引擎**（L362，逐字回验）：「（封装这个工作）是以天为单位做的，还是以周为单位做的，还是以月为单位做的？直接就决定了你的那个 OPT 的进化速度」——封装频次是 OPT 进化速度的一阶变量，不是并列变量之一。

### dk：封装频次引擎
- **维度标签**：频次复利
- 一句话：封装的计量单位（天/周/月）直接决定体系进化速度——把「要不要封装」变成「多久封装一次」，方法论就从意愿问题变成了排程问题。
- 锚：宣讲会:L362（台账 B40）
- 使用边界：适用于个人与团队的资产化节奏管理；不衡量单次封装的质量（质量看抽象度与可调用性）。

## 封装到哪去：六层形态（主图 IMG1 直读）

视觉主图《封装的定义》给出的系统形态（D2 直读，台账 IMG1）：

| 层形态 | 内容示例 | 本库同构 |
|:--|:--|:--|
| **Data Pack**（数据包） | 用户画像/行业洞察/竞品分析/案例库 | 10_raw/sources + DataPack 卡 |
| **Skill**（技能） | 调研分析/需求洞察/文案撰写/方案设计 | 40_outputs/capabilities/skills/ |
| **Role**（角色设定） | 角色身份/边界/汇报线 | 30_wiki/agent-specs/ |
| **Knowledge Base**（知识库） | 公司/行业/方法论/案例 | 30_wiki/ |
| **Workflow**（工作流） | 需求收集→信息调研→分析洞察→方案输出→复盘迭代 | KDO capture→ship→feedback 流水线 |
| **Routing Rules**（路由规则） | 关键词匹配/条件判断/优先级策略/负载均衡 | 检索路由 + queue 分派 |
| **→ 全部汇入 Agent** | 智能体 | agents/ |

主图口径：封装不是限制，而是让智能体更懂你更能干；配套记忆三层——Session（临时）←AI Memory（个性化）←文档知识库（权威），展开见桥接卡 [[bridge-yitang-kdo-document-over-session]]。

**复杂度阶梯**（L430-434，逐字回验）：简单→聊天框；复杂一点→配一套上下文；再复杂→搭团队、自动化的 Agent；再往上→尝试 Vibe Coding 成一个工作台。配套判断句（L434）：「该在哪层用哪层，该封装到哪层就封装到哪层」，不用纠结工具好坏。

**封装复杂度四层级**（L554-558，逐字回验，台账 B59）：

1. 数据包/文档/小技能/小提示词。
2. 知识结构系统/复杂工作流。
3. 角色（背后挂着一堆体系）。
4. 角色调角色（每个研究员背后又是一套体系）——「Agent 会做事只是单点，Agent 之间打开调度才会更好」（台账 B59）。

## DataPack：被单独定义的一种封装

L384，逐字回验：它是 Markdown、结构化、易于调用、相对完整（台账 B43）。要点：

1. **DataPack 不是 Skill**——没有太多规则，是加载后直接抬升上下文质量的弹药（台账 B43）。
2. **加载效果**：加载后上下文补充，表现全面上升（台账 B43）。
3. **最重要的动作**：提高封装的宽度和频次（台账 B43，与 §频次引擎 互证）。

## AI 友好：封装的新增验收维度

L402，逐字回验：「今年有大量的工作都是面向 AI 的做的」——知识管理的要求从「人能看懂」升级为「AI 能调用」（台账 B46 + IMG2 口径：知识不仅要能被人看懂，还要能被 AI 调用）。

**操作判据**：封完问一句——一个没见过这个项目的 Agent，拿到这份资产能否不开口问人就正确使用？不能，就是「人友好」不是「AI 友好」。

## 为什么要封装：胶水问题

第三层的病根（实战路径:L178，逐字回验）：人「在做的最低级最卑微的工作就是当胶水，反复传纸条」，「全程都在不断的去复制粘贴当胶水，所以整个效率特别特别低」。封装是把「传纸条的人」替换成「自助取用的资产」：上下文模式=主动构建相对安全且开放的公共数据系统，各 Agent 自助取用（实战路径:L180-182）。

### dk：胶水传纸条
- **维度标签**：失败模式
- 一句话：人在多 Agent 协作里最高频的实际角色不是「定义目标」，而是当胶水传纸条——识别它的信号是「我今天的工作是复制粘贴」，修复它的动作是把被传递的内容固化成公共资产。
- 锚：实战路径:L178（台账 A30）；反面参照宣讲会:L310
- 使用边界：诊断个人工作效率结构用；不否定临时性传话（一次性协作传话成本低于封装成本）。

## 借假修真：封装的底层心法

L374，逐字回验：「封装的核心其实是借假修真」——把过去那些经验视作假的（可抛弃的具体项目），修的是真的（沉淀下来的系统）。同构三源：实战路径:L210「每一个项目都是为了修炼这套系统」（逐字回验）、L212 自我定义=经营者/长期的业务负责人、L452「我不能光做事儿，借假修真」（ASR 原文「机假修真」系「借假修真」误听，已校正；台账 A36/A66 成对）。

**操作含义**：项目验收标准加一条——除了交付物，这次沉淀了什么资产？没有，项目做完即结束；有，项目成为体系的养料。

## 九个爽自检清单（L574-588，台账 B62 结构化）

原文为连续问句（讲者逐个问「你有没有……」），台账压缩为九项，可直接当封装存量盘点单用：

1. 舍得反复用的提示词——「你们就不舍得删，每次都会用」（L576，逐字回验）。
2. 持续解题的 Partner。
3. 真正好用的 Skill。
4. 高频调用的资产数据包。
5. 设计宪法的高质量文档。
6. 用 AI 打通一切数据。
7. 训练过的数字员工。
8. 训练过的硅基分身。
9. 龙虾协同+工作台开发（场景级 Agent 变工作台）。

配套判据（L586-588，逐字回验）：「你啥不做，怎么可能 AI Native 呢」——九项数量是 AI Native 的前置指标（[[framework-ai-native-working-paradigm]] §积累判据）。

## 失败模式

| 失败 | 症状（可识别信号） | 修复（今晚能做的动作） |
|:--|:--|:--|
| 只聊天不封装 | 「好多同学过去没这根弦儿」（L386，逐字回验）——聊得很多、留不下东西 | 从今天起每次会话结尾强制 10 分钟封装动作 |
| 归档当封装 | 文件存了但换个场景不能用，没经过抽象 | 用「换场景还能不能用」判据重做一次抽象 |
| 存量封装决定起点差 | 换新工具完全像新人（台账 B44：装新工具完全新人 vs 做过封装的一上手就是巅峰水平） | 优先封装跨工具不变的资产（方法/判断框架/数据包） |
| 层级匹配错位 | 教练类提示词放进 Agent 循环拖拉慢 | 「封装就应该封装到第一层」——简单可控响应快（L292，逐字回验） |
| 只封装给人看 | 资产只有作者自己能用 | AI 友好判据：陌生 Agent 不开口问人能正确使用 |
| 新工具狂 hoarder | 收藏/装了一堆，没有一件是自己的资产 | 九个爽清单盘点，先做出第 1 项（不舍得删的提示词） |

## 业界对标（WebSearch 实测，2026-09-06）

| 一堂口径 | 业界同构 | 独立来源 |
|:--|:--|:--|
| 上下文是资产、要主动构建 | Context engineering：上下文是稀缺资源，要策划管理 | Anthropic「Effective Context Engineering for AI Agents」；Sourcegraph「Context Engineering: A Practical Guide」 |
| 六层形态（资产分类） | Write/Select/Compress/Isolate 四操作；模块化 agent-consumable 资产 | Atlan「Context Engineering Techniques」（Karpathy 四操作口径） |
| AI 友好（AI 能调用） | AI-ready knowledge asset 是 KM 团队的一等交付物 | Enterprise Knowledge「Anatomy of an AI-Ready Knowledge Asset」；KMWorld living knowledge base |
| Skill 即封装 | 把领域知识封装成可复用 agent skills 的开源实践 | GitHub「agent-skills-for-context-engineering」；Anthropic Agent Skills |

**对标来源清单（URL＋检索时点 2026-09-06；均为检索摘要级证据，未逐一直连核验，引用按 L3 多源/L5 单源分层对待）**：

1. Anthropic「Effective Context Engineering for AI Agents」：https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents
2. Sourcegraph「Context Engineering: A Practical Guide」：https://sourcegraph.com/blog/context-engineering
3. Atlan「Context Engineering Techniques for AI Agents」：https://atlan.com/know/ai-agent/context-engineering/context-engineering-techniques-ai-agents/
4. Enterprise Knowledge「Anatomy of an AI-Ready Knowledge Asset」：https://enterprise-knowledge.com/enterprise-ai-architecture-series-how-to-extract-knowledge-from-unstructured-content-part-2/
5. GitHub「agent-skills-for-context-engineering」：https://github.com/muratcankoylan/agent-skills-for-context-engineering

**对标结论**：①「资产要 AI 可调用」与业界 AI-ready content 共识一致（≥2 独立来源，不标存疑）；② 一堂版**增量**=把封装频次（天/周/月）立为体系进化的一阶变量——业界谈「what」多、谈「how often」少；③ 一堂六层形态与业界「skills/知识库/workflow/路由」分类高度同构，Routing Rules 作为独立形态在业界同类图里较少单列。
**存疑标注**：Anthropic/Atlan 等来源讲的是上下文管理技术，与一堂「封装」不完全等价——对标只证同构方向，引用时注明口径差异。

## 知行合一：用户拿着能直接做什么

1. **收尾一问**：项目结束必答「这次固化了什么」——答不出，补 10 分钟封装再散会。
2. **选形态**：按六层形态表对号入座（数据/技能/角色/知识库/工作流/路由），不新造分类。
3. **定频次**：把封装写进日/周/月排程（频次引擎），不靠灵感。
4. **盘点存量**：用九个爽清单数自己的封装存量，季度复盘一次增量。

## Critique

### 外部攻击

**攻击 1（同义反复风险）**：「封装=把经验沉淀成系统」——「系统」未定义，定义可能循环（封装就是沉淀，沉淀就是封装）。
1. 回应：部分成立。本卡用三件可操作物补齐定义的可检验性：六层形态（封成什么）、频次引擎（多久封一次）、AI 友好判据（封完算不算数）——三件任何一件缺失即不算完成封装。
2. 残余风险：「抽象度」仍无量化标尺（「换个场景还能不能用」是二元判断），跨人评审时可能分歧。

**攻击 2（沉没成本偏置）**：「每个项目都是为了修炼这套系统」可能变成给低价值项目找意义的合理化话术——什么都封=什么都封不好。
1. 回应：成立，采纳。处置：失败模式表已加「只聊天不封装」的镜像病「什么都封」的克制条款——封装优先级判据=复用预期（预计同类问题再来 ≥2 次才值得封），单次性内容留在会话层。
2. 讲者口径侧证：筛选机制里「掉队者别组队」（B67）同理——机制设计处处在对抗「平均用力」。

### 不要用的场景

| 场景 | 为什么失效 | 替代方案 |
|:--|:--|:--|
| 一次性、不复用的事务 | 封装成本>复用收益 | 直接做，留会话记录即可 |
| 还没跑通一次的流程 | 没有「一次经验」可抽象，封出来是空架子 | 先跑通再封装（与跳级失败同构） |
| 需要严格合规审计的文档体系 | 六层形态无权限/合规字段 | 按 ISO 27001/等保类框架另建治理层 |
| 替代具体 Skill 工程方法 | 本卡不讲怎么做 Skill | [[tool-ai-skill-engineering-guide]] / [[method-anthropic-skill-design-patterns]] |

## Constraints & Boundaries

- 适用：个人/团队资产化路线设计、封装存量盘点、AI 化知识管理的验收口径
- 不适用：一次性事务、未跑通的流程、合规审计替代、具体 Skill 制作工艺
- 溯源纪律：定义与清单为一堂单源口径；九个爽为台账结构化压缩（原文连续问句）；业界对标只证同构方向

## Synthesis

三步编译收束：封装方法论的独立价值在三处：①**频次引擎**（L362）——把资产化从意愿问题变成排程问题，这是本卡区别于一切「知识管理最佳实践」的核心增量；②**六层形态**（IMG1）——给了封装产物一个有限枚举的分类学，Routing Rules 单列成层提示「调度逻辑本身是资产」；③**胶水传纸条**（L178）——把封装的动因落在可体感的工作状态上（你今天在复制粘贴吗）。与库内关系：本卡是五层架构第三层的方法论展开，向上支撑 AI Native 的积累判据（九个爽数量），向左与本库 Skill 工程线（[[tool-ai-skill-engineering-guide]]）互补——本卡管 why/when/what，工程卡管 how。KDO 视角：本库的 10_raw→30_wiki→40_outputs 三层目录、pre-submit 门禁、queue 流转，全部是「六层形态+频次引擎」的在跑实例；KDO 的封装频次目前是「任务驱动」（有单才封），对照 L362 判据，下一个进化方向是把封装排程化。

## Action Triggers

| 触发场景 | 第一个动作 | 成功指标 |
|:--|:--|:--|
| 项目/会话收尾 | 回答「这次固化了什么」 | 每次收尾产出 ≥1 个资产或明确记录「无可封装」 |
| 不知道封成什么 | 查六层形态表对号入座 | 产物落在六类之一，无新造分类 |
| 体系感觉长得慢 | 检查封装计量单位 | 天/周级封装动作出现在日历上 |
| 新工具上手 | 先带存量资产再干活 | DataPack/Skill 在新工具里第一天可用 |
| 团队汇报 AI 产出 | 用九个爽清单盘点 | 汇报含封装存量数而非工具清单 |

## 迭代日志

- 2026-09-06 v1.0：#654 batch1 生产，据 D1 金矿台账（B37-B48/B52/B59/B62）+ IMG1/IMG2 直读萃取；引语逐条回验逐字稿行号；业界对标 5 独立来源（Anthropic/Sourcegraph/Atlan/Enterprise Knowledge/GitHub）。
