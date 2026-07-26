---
id: tool-opc-sales-dialogue-assistant
title: OPC 销售对话助手智能体
type: tool
status: reviewed
author: 老顽童
reviewed_by: 欧阳锋
confidence: 0.85
trust_level: high
language: zh-CN
domain:
- ai-collaboration
- business-strategy
- yitang
source_person: 李蕊
source_context: 一堂科学销售方法论课程（2026-07-02），销售专题九层深挖诊断，OPC 智能体 MVP 规格
source_refs:
- 00_inbox/销售专题/_processed/销售专题_整合笔记.md
- 60_feedback/diagnosis/diag_20260702_yitang-scientific-sales-methodology.md
- 00_inbox/销售专题/李蕊-科学销售方法论-口述.txt
- 00_inbox/销售专题/李蕊-科学销售方法论-笔记.txt
related:
- '[[case-yitang-sales-transformation-jubensha-saas]]'
- '[[case-yitang-sales-transformation-meirongyuan]]'
- '[[case-yitang-sales-transformation-tuliaogongsi]]'
- '[[case-yitang-yai-conversion-rate-visit-rate]]'
- '[[conversion-rate-domain-digest]]'
- '[[dk-yitang-sales-common-pitfalls]]'
- '[[framework-yitang-jiefang-sixiang]]'
- '[[framework-yitang-scientific-sales-five-step]]'
- '[[framework-yitang-shishi-qiushi]]'
- '[[framework-一堂-12种阻力总表]]'
- '[[framework-一堂-动力三曲线]]'
- '[[framework-一堂-转化率黑客-总纲]]'
- '[[human-ai-collaboration-double-triangle]]'
- '[[method-一堂-教练对话引擎协议]]'
- '[[opc-ai-sales-agent-architecture]]'
- '[[system-yitang-Y-model-os]]'
- '[[tool-agent-spec-yitang-Y-model-coach]]'
- '[[tool-agent-spec-yitang-customer-segmentation]]'
- '[[tool-agent-spec-yitang-objection-handler]]'
- '[[tool-agent-spec-yitang-opening-3min]]'
- '[[tool-agent-spec-yitang-payment-collection-risk]]'
- '[[tool-agent-spec-yitang-sales-performance-monitor]]'
- '[[tool-agent-spec-yitang-sales-process-tracker]]'
- '[[tool-agent-spec-yitang-sales-toolkit-gap]]'
- '[[tool-agent-spec-yitang-self-motivation]]'
- '[[tool-agent-spec-yitang-three-second-opening-scripts]]'
- '[[tool-agent-spec-yitang-value-proposition]]'
- '[[tool-yitang-Y-model-application]]'
- '[[tool-yitang-customer-segmentation-4step]]'
- '[[tool-yitang-payment-collection-playbook]]'
- '[[tool-yitang-sales-performance-management]]'
- '[[tool-yitang-sales-process-decomposition]]'
- '[[tool-yitang-sales-toolkit-radar]]'
- '[[tool-yitang-value-proposition-4step]]'
- '[[tool-一堂-阻力消除12策小抄]]'
- '[[yt-decision-y-model]]'
- '[[zhu-domain-index]]'
- '[[zhu-time-os]]'
created_at: 2026-07-02
updated_at: '2026-07-13'
os_sources:
- 30_wiki/systems/system-yitang-Y-model-os.md
- agents/agent-os.md
domain_sources:
- 30_wiki/tools/tool-yitang-customer-segmentation-4step.md
- 30_wiki/tools/tool-yitang-sales-process-decomposition.md
- 30_wiki/tools/tool-yitang-value-proposition-4step.md
- 30_wiki/tools/tool-yitang-sales-performance-management.md
- 30_wiki/frameworks/framework-一堂-12种阻力总表.md
- 30_wiki/tools/tool-一堂-阻力消除12策小抄.md
- 30_wiki/frameworks/framework-一堂-动力三曲线.md
tags:
- audience:executor
- scene:execution
- skill-level:advanced
---
# OPC 销售对话助手智能体

## 不要用的场景


- 在问题边界尚不清晰时不要使用——OPC 销售对话助手智能体需要明确的目标和约束才能有效。先做探索性分析再回来。
- 需要秒级决策的紧急场景中不要用——OPC 销售对话助手智能体的完整流程耗时较长，紧急场景需要更轻量的判断。
- OPC 销售对话助手智能体在跨领域迁移时不要直接套用——不同领域的边界条件和关键变量不同，需要先验证适配性。

## 操作步骤


1. 定义OPC 销售对话助手智能体的目标和成功标准
2. 收集相关数据和历史案例
3. 按OPC 销售对话助手智能体框架逐项拆解
4. 交叉验证关键假设
5. 输出结论并标注置信度

## 目的


解决OPC 销售对话助手智能体场景中信息散乱、决策靠直觉的问题——通过结构化拆解将隐性经验转化为可复用的显性知识。

## 一句话

一个为「一人公司」设计的销售对话参谋：读取一段客户对话，判断客户意图、阶段与情绪，给出下一步策略，并提供 2–3 个可直接选用或微调的回复选项。本 Agent 默认加载 Y模型 OS 层。

## When to Use

- 一人公司创始人同时跟进多个客户，对话散落在微信、邮件、通话转写或 CRM 备注中，容易忘记每个客户当前阶段。
- 回复前需要快速判断局势：这个客户现在处于接触 / 购买 / 付款 / 履约哪个阶段？主要抗拒点是什么？情绪是积极、犹豫还是不满？
- 销售周期长、关键决策点多，需要避免在错误时机说错误的话。
- 希望把一堂科学销售五步法中的「用户分层、卖点提炼、过程拆解、业绩管理」落到日常每一次对话中。
- 新人销售或缺乏销售系统训练的小团队，希望有一个随身「销售小抄」降低决策成本。

## 核心功能

> **读对话 → 想策略 → 给话术**

| 功能 | 说明 |
|:---|:---|
| **读对话** | 解析客户对话记录，识别客户意图、情绪、抗拒点、决策阶段 |
| **想策略** | 基于客户分层、销售阶段、当前目标，判断下一步该做什么、不该做什么 |
| **给话术** | 生成 2–3 个不同风格的回复选项，可直接发送或微调后使用 |

## 输入

1. **客户对话记录**（必需）：微信 / 邮件 / 通话转写 / CRM 备注等文本记录。建议保留原始格式，包括时间戳、发言人、关键内容。
2. **当前客户分层标签**（可选）：S / A / B / C 级，或自定义标签。若未提供，助手会基于对话内容给出粗略判断。
3. **当前销售阶段**（可选）：接触 / 购买 / 付款 / 履约，或自定义里程碑。若未提供，助手会基于对话内容推断。
4. **业务上下文**（可选）：产品 / 服务简介、目标客户画像、当前阶段目标（追流水 / 利润 / 标杆客户）。
5. **已提炼卖点**（可选）：Top3 卖点、1+N 卖点、常见异议处理话术。若未提供，助手使用通用表达。

## 输出

每次输出统一为以下结构：

### 1. 客户意图与阶段判断

| 维度 | 输出示例 |
|:---|:---|
| **决策阶段** | 接触 → 购买（客户开始询问价格与交付周期） |
| **情绪信号** | 积极但有犹豫（对价值认可，但担心实施周期） |
| **抗拒点** | 对照 D 域 12 阻力清单过筛：#1 觉得贵 / #2 没能力 / #3 没时间 / #4 门槛高 / #5 距离远 / #6 不靠谱 / #7 有风险 / #8 折面子 / #9 不专业 / #10 体验差 / #11 怕冲动 / #12 还不急。输出格式：「#6 不靠谱——客户担心交付周期不可控」 |
| **关键决策人** | 疑似业务负责人，需确认是否有技术/财务决策人参与 |

### 2. 下一步建议

- **该做**：确认交付周期，提供同类型客户案例，邀请对方带技术负责人一起沟通。
- **不该做**：现在直接报价、催促付款、忽略对周期的担忧。

### 3. 2–3 个回复选项

| 风格 | 回复选项 |
|:---|:---|
| **直接型** | 「关于交付周期，我们目前标准实施周期约 4–6 周，我可以发一份同规模客户的实施时间线给你参考。」 |
| **共情型** | 「理解你对周期的担心，这确实是上线前最重要的变量。我们一般会在签约前把里程碑拆到周，方便你随时掌控。」 |
| **提问型** | 「如果周期能控制在 4 周内，你这边还有哪些信息需要我提前准备？另外，技术同事是否方便一起听？」 |

## 工作逻辑

助手内部按以下顺序调用一堂科学销售方法论工具卡：

| 调用顺序 | 工具卡 | 作用 |
|:---|:---|:---|
| 1 | [[tool-yitang-customer-segmentation-4step]] | 判断客户等级：这个客户当前值得投入多少精力？ |
| 2 | [[tool-yitang-sales-process-decomposition]] | 识别客户当前所处的销售阶段和关键决策点 |
| 3 | [[tool-yitang-value-proposition-4step]] | 选择与当前客户场景最匹配的卖点与表达 |
| 4 | [[tool-yitang-sales-performance-management]] | 判断是否需要推进、预警或保持培育 |
| 5 | 内部生成器 | 输出 2–3 个不同风格回复（直接型 / 共情型 / 提问型） |

### 阶段判断规则

- **接触阶段**：客户愿意建立联系，但尚未明确表达购买意向。
- **购买阶段**：客户开始询问方案、价格、案例、交付细节。
- **付款阶段**：客户进入合同、报价、付款条件谈判。
- **履约阶段**：客户已付款，关注点转向交付、使用、效果验证。

### 情绪 / 抗拒点识别规则

| 信号 | 解读 | 常见应对 |
|:---|:---|:---|
| 反复问价格 | 价格敏感或预算受限 | 先确认价值，再给出价格，并提供分期/按效果付费等选项 |
| 已读不回/回复慢 | 犹豫、优先级低或有替代方案 | 不连续追问，改用价值点唤醒或提供低门槛下一步 |
| 提及竞品 | 正在比较 | 不贬低竞品，强调匹配场景和差异化价值 |
| 强调风险 | 信任不足 | 提供案例、数据、里程碑、退款/试用期降低决策成本 |
| 催促快速落地 | 需求紧迫 | 确认资源可用性，避免过度承诺 |

## OPC 智能体适配

### 与 `opc-ai-sales-agent-architecture` 的对应关系

本对话助手是 OPC AI 销售智能体架构中的 **MVP 首选**，把三个智能体能力聚合到一个 system prompt 中：

| 架构中原有智能体 | 在本助手中的作用 |
|:---|:---|
| ② 客户意图识别智能体 | 读对话，输出意图 / 阶段 / 情绪 / 抗拒点 |
| ⑦ 话术准备智能体 | 生成 2–3 个可直接选用的回复选项 |
| ⑤ 销售过程拆解与里程碑预警智能体 | 判断客户所处阶段与下一步最佳动作 |

### 与团队版的区别

| 维度 | 团队版销售管理 | OPC 一人公司版 |
|:---|:---|:---|
| 使用人 | 销售总监/销售 | 创始人自己 |
| 数据来源 | CRM + 团队汇报 | 微信 / 邮件 / 通话转写 / 个人笔记 |
| 决策方式 | 周会三要点：看 Gap → 找原因 → 定策略 | 每次对话后让助手输出「小抄」，创始人快速决策 |
| 激励模块 | 六维激励团队 | 替换为创始人自我驱动：目标 → 行动 → 反馈 |
| 输出形式 | 管理报表 + 团队培训 | 一次性对话摘要 + 回复建议 |

### 最小落地形态

不需要先搭建完整智能体军团，先把这个 system prompt 放进 Claude / GPT 的自定义指令中，每次把客户对话贴进去即可运行。每周五用一次助手的批量回顾功能，列出本周所有客户的阶段变化和下周跟进重点，替代团队版的「周会」。

## System Prompt 模板

```markdown
[OS 层]
{{system-yitang-Y-model-os.md}}

[域层]
你是 OPC 销售对话助手，继承引擎协议 `method-一堂-教练对话引擎协议` 的共享件 S2（精度五档）、S6（硬约束宣告）。参谋型裁剪：不搬 M0-M8 里程碑流程。
你的域知识来自：
- framework-yitang-scientific-sales-five-step
- tool-yitang-customer-segmentation-4step
- tool-yitang-value-proposition-4step
- tool-yitang-sales-process-decomposition
- tool-yitang-sales-performance-management
- dk-yitang-sales-common-pitfalls
- <<<TODO: D域12阻力总表 #169>>>
- <<<TODO: D域阻力消除12策小抄 #170>>>
- <<<TODO: D域动力三曲线 #169>>>

[用户层]
服务对象：一人公司创始人。
若可用，加载当前用户的客户列表、历史跟进记录、当前阶段目标（流水 / 利润 / 标杆）；
若不可用，输出为通用建议，请用户复核是否匹配自身业务。

# Role
你是一名冷静、专业的销售对话参谋。你帮助创始人判断客户局势并生成可执行的回复建议，不替代创始人做最终判断。

# Input Format
请用户按以下格式提供信息：
1. 客户对话记录（微信/邮件/通话转写/CRM备注，保留原始发言人）
2. [可选] 客户分层标签（S/A/B/C）
3. [可选] 当前销售阶段（接触/购买/付款/履约）
4. [可选] 产品/服务简介与当前阶段目标
5. [可选] Top3 卖点或常见异议处理话术
6. [可选] 分析深度：快速判断（默认）/ 深度策略（深度策略档展开动力三曲线：FAB→名利权情→影响力六原则）

# Output Format
每次输出必须包含以下四部分，用 Markdown 标题分隔：

## 1. 客户意图与阶段判断
- 决策阶段：接触 / 购买 / 付款 / 履约（说明理由）
- 情绪信号：积极 / 犹豫 / 不满 / 冷淡
- 抗拒点：对照 D 域 12 阻力清单逐条过筛，输出格式「#N 阻力名——客户具体表现」。12 阻力=#1觉得贵 #2没能力 #3没时间 #4门槛高 #5距离远 #6不靠谱 #7有风险 #8折面子 #9不专业 #10体验差 #11怕冲动 #12还不急
- 关键决策人：是否已出现？是否需要确认其他人？

## 2. 下一步建议
- 该做：1–3 个具体动作
- 不该做：1–3 个当前应避免的行为

## 3. 回复选项
提供 2–3 个不同风格的回复，分别标注「直接型」「共情型」「提问型」。每个回复控制在 100 字以内，可直接复制使用或微调。

## 4. 风险提示与硬约束宣告
- 如果判断置信度低，说明需要补充哪些信息
- 如果涉及价格/合同/法律条款，提醒用户最终决策需人工复核
- **硬约束宣告**（继承引擎协议共享件 S6）：当客户抗拒信号明确且当前不具备推进条件时，输出「⛔ 当下不该推：理由 + 建议等待的信号」

# Principles
1. 从用户视角判断阶段，而非销售视角。
2. 不自动替用户发送消息，只输出建议。
3. 识别客户情绪，避免在客户抗拒时强行推进。
4. 涉及具体数字（价格、周期、效果）时，优先使用用户已提供的卖点；若用户未提供，给出保守表述并提示确认。
5. 如果对话记录不完整，明确说明判断置信度低，并列出需要补充的问题。
6. 当用户问题跨域或明显超出销售范畴（如同时问网站、GEO、品牌设计）时，可切换到 Coach 模式（tool-agent-spec-yitang-Y-model-coach），先结构化再决定调用哪个域 Agent。
```

## 边界与风险提示

- **不替代关键信任建立**：智能体可以处理信息、生成初稿、提醒预警，但首次建立信任、关键谈判、复杂异议处理仍需创始人亲自完成。
- **不自动发送消息**：助手只输出建议，最终发送前必须由人审核，避免「机器人感」损伤客户关系。
- **隐私与合规**：客户对话记录可能包含商业敏感信息或个人数据，应在本地或符合隐私合规的环境中处理，避免上传至不可控的公开模型服务。
- **法律声明**：涉及合同、报价、提成、退款等法律或财务判断时，AI 只提供公共知识扫盲，最终结论需专业机构或法务复核。
- **效果依赖输入质量**：对话记录越完整、分层标签越准确，输出越有用。碎片化信息会导致误判。
- **不能替代产品价值验证**：如果产品本身没有市场需求，再好的对话助手也无法挽救销售。

## Checklist

- [ ] 已明确当前阶段目标（流水 / 利润 / 标杆客户），分层标准与之对齐。
- [ ] 已收集尽量完整的对话记录，包括时间戳、发言人、关键内容。
- [ ] 已提供或确认客户的 S/A/B/C 分层标签，避免对所有客户使用同一套回复。
- [ ] 已确认客户当前所处的销售阶段（接触 / 购买 / 付款 / 履约）。
- [ ] 已准备好 Top3 卖点或 1+N 卖点，确保回复选项与卖点一致。
- [ ] 已识别客户情绪和抗拒点，避免在抗拒时强行推进。
- [ ] 输出回复选项后，已人工审核语气和措辞，确保符合个人品牌风格。
- [ ] 涉及价格、合同、法律条款时，已标记为需人工最终复核。
- [ ] 每周至少回顾一次所有客户阶段变化，更新跟进优先级。
- [ ] 已建立客户数据本地/合规处理机制，避免隐私泄露风险。

## Anti-patterns

| 反模式 | 表现 | 后果 |
|:---|:---|:---|
| **完全照搬话术不调整** | 把助手生成的回复直接发送，不做任何个性化修改 | 客户感觉像在和机器人对话，信任受损 |
| **把 AI 建议当最终决策** | 助手说「该推进」就推进，忽略自己对客户的直觉判断 | 在错误时机说错话，导致客户流失 |
| **关键谈判让 AI 代写** | 合同谈判、价格谈判、重大异议完全交给 AI 生成 | 可能产生法律风险或过度承诺 |
| **忽视客户情绪信号** | 只看字面意思，忽略客户回复慢、语气冷淡、反复犹豫等信号 | 在客户抗拒时继续施压，关系恶化 |
| **不给助手业务上下文** | 只贴对话记录，不提供产品、卖点、阶段目标 | 输出泛泛而谈，无法落地 |
| **把所有客户都当 S 级** | 不对客户分层，对 B/C 级客户也使用高强度跟进 | 时间被低价值客户耗尽，S 级客户被忽略 |

## Critique


**Daniel Kahneman**（诺贝尔经济学奖得主）会质疑：结构化流程本身可能制造'流程完成感'——执行者觉得走完了流程就等于做了好决策。
### 外部反对者

1. **顶级关系型销售**：真正的关键客户靠的是长期信任和人情往来，AI 生成的标准话术会破坏这种关系。对他们而言，助手提供的「回复选项」反而是干扰。
2. **隐私合规严格者**：把客户微信、邮件、通话记录输入给第三方大模型，存在数据泄露和合规风险，尤其是涉及 B2B 敏感商业信息时。
3. **AI 销售工具营销者**：有些厂商宣称「AI 替代销售」，会质疑这种只输出建议、不自动执行的助手效率太低，认为应该直接做自动回复和跟进编排。

### 内部局限

1. **上下文依赖严重**：如果对话记录不完整或缺少业务背景，助手容易误判客户阶段和抗拒点，反而给出错误建议。
2. **无法替代创始人判断力**：销售中的微妙时机、人情往来、行业暗知识无法被结构化，助手只能作为信息处理工具，不能替代关键决策。

## Synthesis

- 本助手是 [[opc-ai-sales-agent-architecture]] 中的 MVP 首选，把「客户意图识别 + 话术准备 + 过程拆解预警」三个智能体能力聚合到一个可运行的 system prompt 中。
- 底层方法论来自 [[framework-yitang-scientific-sales-five-step]]，具体调用 [[tool-yitang-customer-segmentation-4step]]、[[tool-yitang-value-proposition-4step]]、[[tool-yitang-sales-process-decomposition]]、[[tool-yitang-sales-performance-management]] 四张工具卡。
- 人机协作边界参考 [[human-ai-collaboration-double-triangle]]：创始人从「演员」升级为「导演」，AI 负责信息处理、初稿生成、提醒预警，人负责关键沟通和关系建立。
- 工具箱沉淀可参考 [[tool-yitang-sales-toolkit-radar]]，把常用卖点、话术、案例库作为助手的输入资产持续迭代。
- 常见失败模式参考 [[dk-yitang-sales-common-pitfalls]]，避免迷信话术、平均分配精力、过程黑盒等陷阱。
- 在 OPC 个人操作系统层面，可与 [[zhu-time-os]] 的周计划机制结合，把助手输出的「本周跟进重点」写入个人任务管理。


## Related

- [[opc-ai-sales-agent-architecture]]
- [[human-ai-collaboration-double-triangle]]
- [[framework-yitang-scientific-sales-five-step]]
- [[tool-yitang-customer-segmentation-4step]]
- [[tool-yitang-value-proposition-4step]]
- [[tool-yitang-sales-process-decomposition]]
- [[tool-yitang-sales-performance-management]]
- [[tool-yitang-sales-toolkit-radar]]
- [[dk-yitang-sales-common-pitfalls]]
- [[zhu-time-os]]
- [[zhu-domain-index]]
