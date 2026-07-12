---
id: concept-yihang-dual-triangle-core
title: 一行双三角：人机协作的元模型
type: concept
status: draft
author: 王语嫣
reviewed_by: pending
confidence: 0.88
trust_level: high
language: zh-CN
created_at: 2026-07-03
updated_at: 2026-07-11
domain:
- yitang
- ai-collaboration
- personal-os
- organizational-transformation
source_refs:
- 00_inbox/人机协作双三角/一堂双三角-人机协作模型-逐字稿.md
- 00_inbox/人机协作双三角/一堂双三角-人机协作模型-笔记.txt
- 00_inbox/人机协作双三角/_processed/洪七公_双三角深度理解.md
- 00_inbox/人机协作双三角/_processed/一堂双三角-AI时代的竞争力武器库_vlm.md
- 00_inbox/人机协作双三角/_processed/AI组织行为学的口述_text.md
- https://arxiv.org/abs/2506.12469
- https://www.databricks.com/blog/agent-learning-human-feedback-alhf-databricks-knowledge-assistant-case-study
- https://www.faros.ai/blog/harness-engineering
- https://atlan.com/know/harness-engineering-vs-prompt-engineering/
related:
- "[[framework-yihang-dual-triangle-weapon-library]]"
- "[[yt-business-formula-parameter-iceberg]]"
- "[[yt-tool-business-formula-parameter-arsenal]]"
- "[[framework-yihang-dual-triangle-ten-year-map]]"
- "[[framework-yihang-dual-triangle-three-stages-six-changes]]"
- "[[framework-yihang-dual-triangle-ai-landing-five-steps]]"
- "[[tool-yihang-dual-triangle-canvas]]"
- "[[agent-spec-dual-triangle-canvas-filler]]"
- "[[method-dual-triangle-flywheel-engine]]"
- "[[人机协作决策-双三角模型]]"
- "[[concept-AI时代双三角竞争力]]"
- "[[concept-一堂-AI时代基本功变与不变]]"
- "[[yt-decision-y-model]]"
- "[[system-yitang-Y-model-os]]"
- '"[[case-yihang-dual-triangle-tianmo-design-delivery]]"'
- '"[[case-yihang-dual-triangle-ahao-product-selection]]"'
- '"[[case-yihang-dual-triangle-huazao-synthetic-data]]"'
- '"[[case-yihang-dual-triangle-chentian-knowledge-agent]]"'
- '"[[case-yihang-dual-triangle-truman-feishu-to-slide-ppt-evolution]]"'
- '"[[framework-yitang-y-model-dual-triangle-synergy]]"'
- "[[agent-spec-yitang-dual-triangle-cross-domain-diagnostician]]"
- "[[tool-yitang-dual-triangle-domain-registry]]"
- "[[framework-一堂-业务公式拆解-总纲]]"
  - "[[concept-yihang-data-pack-ethics]]"
  - "[[concept-yihang-human-in-the-loop-dual-triangle]]"
  - "[[concept-yihang-methodology-production-pipeline]]"
  - "[[concept-yihang-research-driven-company]]"
  - "[[concept-yitang-education-formula]]"
- "[[master-decision-hygiene]]"
- "[[lean-startup-domain-digest]]"
aliases:
- 一行双三角
- 一堂双三角
- 缪斯模型
- MUSE模型
---

# 一行双三角：人机协作的元模型

> **一句话定义**：一行双三角是一个解释「人类与 AI 如何高水平协作」的元模型——把人的竞争力拆成「审美、体系、创造力」，把 AI 的落地能力拆成「场景、数据、基本功」，两个三角相互咬合，形成自增强飞轮。
>
> 课程原称「一堂双三角」，别名「缪斯模型 / MUSE」。本知识库统一使用「一行双三角」。

---

## 一、模型提出的背景

### 1.1 时代背景

2023 年之后，AI 工具快速免费化，出现了一个悖论：

- **短期**：会用提示词、Coze、Agent 的人获得了超额收益。
- **长期**：工具越普及，工具本身越贬值，人与人之间的差距反而越来越大。

一堂的判断是：AI 时代最不稳定的是工具，只有结构才是最可靠的地基。于是用「控制变量法」推导：

1. 假设大家都会用 AI，人与人的差距在哪里？→ **审美、体系、创造力**
2. 假设人都是专家，AI 落地效果的差距在哪里？→ **场景、数据、基本功**

把两组要素组合，就形成了双三角。

### 1.2 与主流范式的关系

一行双三角与 2025-2026 年学术界和工业界的主线高度同构。以下是经全网调研验证后的对应关系：

| 主流范式 | 来源 | 验证状态 | 与一行双三角的对应 |
|:---|:---|:---|:---|
| **五级 Agent 自主性** | Feng, McDonald & Zhang (2025), *Levels of Autonomy for AI Agents*, arXiv:2506.12469 | ✅ 已验证 | 自主性不是能力结果，而是设计决策。双三角的六要素帮助决定每个任务该用哪一级自主性。 |
| **人在环 / 人在环上 / 人在环外** | HITL/HOTL 工业界实践 + DRCF 2026 五级自主性光谱 | ⚠️ 概念存在，但「ApFramework (2026)」作为单一命名框架未独立核实 | Human-in-the-Loop / on-the-Loop / out-of-the-Loop 对应双三角中「人必须做的事」的边界。 |
| **Harness Engineering** | Mitchell Hashimoto / Martin Fowler / Ryan Lopopolo 等 2026 年工程实践论述 | ⚠️ 作为工程趋势已验证，但作为正式命名框架的边界待进一步明确 | 从 Prompt Engineering → Context Engineering → Harness Engineering，对应人在双三角中从「执行者」漂移为「意图设定者」。 |

**关键外部来源**：
- Feng et al. (2025): https://arxiv.org/abs/2506.12469
- Databricks ALHF 案例研究（32 条反馈提升 4 倍质量）: https://www.databricks.com/blog/agent-learning-human-feedback-alhf-databricks-knowledge-assistant-case-study
- Harness Engineering 讨论: https://www.faros.ai/blog/harness-engineering, https://atlan.com/know/harness-engineering-vs-prompt-engineering/

### 1.3 人 × AI，不是人 + AI

主流范式常默认「人 + AI」——人做一部分，AI 做一部分，互补即可。

一行双三角用的是 **「人 × AI」** 思维：

> 任一个关键维度如果接近空白，整体产出会被严重拉低。

**这是启发式比喻，不是数学公式。** 实际产出更可能是「加权组合 + 阈值效应」，但用乘法思维可以提醒自己：
- 审美 50 分 × 基本功 80 分 ≈ 40 分产出（被短板拖累）
- 数据是 0，体系再强也白搭

**行动 implication**：不是补最长板，而是先识别并补最短板。当前多数团队的最短板是「数据资产化意识」和「审美反馈结构化」。

---

## 二、六要素的官方定义

### 人类三角（Human Triangle）

| 要素 | 定义 | 同义词 | 关键问题 |
|:---|:---|:---|:---|
| **审美** | 对结果质量的高水平判断力 | 品味、见识、判断力 | 「好结果长什么样？差在哪？」 |
| **体系** | 解决一类问题的成熟、稳定的思考与执行框架 | 框架、工作流、思维模型 | 「这件事的标准流程是什么？」 |
| **创造力** | 敢于跳出原有经验和惯例，提出新解法、新设想 | 创新、提假设、大胆设想 | 「还能怎么做？本质是什么？」 |

**结构关系**：审美 + 体系 → 撑起创造力。没有底座的创造力是瞎想。

### AI 三角（AI Triangle）

| 要素 | 定义 | 同义词 | 关键问题 |
|:---|:---|:---|:---|
| **场景** | 发掘高匹配、高价值细分场景的能力 | AI 机会探索、AI 价值预判、落地边界 | 「AI 在哪个环节最能创造价值？」 |
| **数据** | 主动搜集和积累高质量 AI 可用数据资产 | AI 数据资产、AI 数据建设 | 「有什么正面/负面案例和 Domain Knowledge？」 |
| **基本功** | 熟练使用 AI 工具与范式解决问题——包括提示词工程、上下文工程、智能体协作、全网调研（扩展定义见 [[concept-一堂-AI时代基本功变与不变]]） | AI 工具、AI 技术、AI 实操能力 | 「用什么工具、什么 Feature 来做？给 AI 搭了什么上下文？」 |

**结构关系**：基本功 + 数据 → 撑起场景。没有底座，场景只是空想。

### 两个三角的咬合

```
        创造力 ←——————→ 场景
          ↑      ×      ↑
        审美 ←——体系——→ 基本功 ——→ 数据
          \      |      /
           人类三角 × AI三角
```

- **横向支撑**：审美 + 体系 → 创造力；基本功 + 数据 → 场景。
- **纵向协作**：人类三角定方向、定标准、定流程、提假设；AI 三角找场景、练基本功、攒数据、做执行。
- **循环增强**：人变强了 → 调教更强 AI → 省出时间 → 人继续变强。

---

## 三、飞轮：模型真正值钱的地方

双三角不是静态分类工具，而是**自增强飞轮**。

### 核心循环

```
人提升审美/体系/创造力
        ↓
AI 在场景中表现更好
        ↓
大幅减少人的工作时间
        ↓
人有时间继续升级审美/体系/创造力
        ↓
（循环）
```

### 三个交叉回路

| 回路 | 名称 | 运转方式 |
|:---|:---|:---|
| **审美 ↔ 场景** | 判断力回路 | 审美判断 → 改进 Agent Prompt → 场景表现更好 → 人做更高层判断 |
| **体系 ↔ 数据** | 方法论回路 | 方法论卡 → Agent 调用 → 执行结果 → 发现方法论 gap → 更新方法论卡 |
| **创造力 ↔ 基本功** | 杠杆回路 | 新 Agent/新域设计 → 工具/编译器降低建 Agent 成本 → 能设计更多 Agent |

### 飞轮的启动难点

- **启动很难**：系统早期又复杂又无趣，没有即时成就感。
- **先难后易**：一旦转起来，会产生复利级效果。
- **最大卡点**：不是技术，而是「审美判断没有被记录」。

---

## 四、暗知识：六个最容易被忽略的判断

### 1. AI 不创造标准，只放大标准

> 「AI 极度依赖规则，它能放大标准，但无法创造标准。你们没有标准，AI 做不了。」——硬件公司专利案例外部专家

**含义**：AI 落地前，必须先把业务流程拆到规则级。规则不清，AI 只能放大混乱。

### 2. 数据不够的时候，让 AI 先造数据

> 「用 AI 创造性地挑战快速学习上限；提出“让 AI 先造数据”的破局假设。」——花总案例

**含义**：真实数据稀缺时，可用仿真/合成数据先跑起来，不要等数据完美。

### 3. 人机协同的关键不是让 AI 像人，而是让人只做「人才能做的事」

> 「人机协同的关键不是让 AI 做得像人，而是让人只去做需要人才能做的事。」——酒店 AI 标签案例

**含义**：每次分工都要问：这个环节如果没有人，能不能跑？能，尽量交给 AI；不能，人守住。

### 4. 审美标准可以在短期内快速建立

> 「审美是可以建立的，不是靠你过去，你可以现场建立审美，靠的是极短的时间内快速学习。」——天末案例

**含义**：进入新场景时，先用 AI 调研全球最佳实践、拆到最小原子、锁定标杆，快速建立判断标准。

**前提**：这种方法对「有专业基础、需要快速对齐新场景标准」的人有效；对完全零基础的人，仍需要长期训练。

### 5. 能写成函数的判断，不要交给大模型

> 「打标签就判断标签这件事情能用 Python 别用大元模型……模型有两个巨大的问题，随机概率不稳定，第二贼贵。」——阿豪案例

**含义**：规模化落地的稳定性与成本，取决于是否把确定性判断从概率模型迁到确定性代码。

### 6. 意图是当前技术路径下人的核心比较优势

> 「如果模型最终能超长程地完成抽象目标，人在工作链路中的唯一价值是什么？答案是：意图（Intention）。」——Harness Engineering 范式

在当前技术路径下，模型可以被训练得无比强大，但它没有「想做点什么」的内在动机。人类三角的三个要素恰好构成意图：
- **创造力** = 提出值得做的假设
- **审美** = 判断什么算做得好
- **体系** = 让做对的事情可持续

**含义**：人机协作的最高形态，不是 AI 替人干活，而是人不断产生更高质量的意图，AI 不断把意图落地为更高质量的结果，人再从结果中获得新的洞察——循环往复，螺旋上升。

**开放性**：这一判断基于当前 AI 技术路径。未来如果模型通过目标函数、奖励模型或环境反馈形成「类意图」行为，该结论需要重新评估。

---

## 五、常见误用

| 误用 | 表现 | 修正 |
|:---|:---|:---|
| **强行一一对应** | 认为审美=数据、体系=基本功、创造力=场景 | 官方结构是「审美+体系→创造力」「基本功+数据→场景」，实践中六要素会交叉喂养，但不要把玄学映射当真理 |
| **把框架当检查清单** | 每次填完六个格子就认为做完了 | 画布只是起点，真正价值来自执行后的反馈和迭代 |
| **跳过人类三角追工具** | 只学提示词、Coze、Agent | 工具会贬值，审美/体系/创造力才是长期壁垒 |
| **等数据完美了才开始** | 觉得没有高质量数据就不能用 AI | 先用最小数据跑通 MVP，缺什么补什么 |
| **把 AI 当黑箱许愿机** | 希望 AI 一次性出 90 分结果 | 高水平结果是多轮反馈的产物，审美判断是核心驱动力 |

---

## 六、Critique

### 内部局限

1. **模型边界**：双三角解释的是「高水平人机协作」，不是「所有 AI 应用」。对于一次性、低风险的简单任务，直接提示词工程即可，不需要画布。
2. **启动门槛**：需要用户先有一定业务认知。完全零基础的人连问题都描述不清，画布填出来也是空的。
3. **组织依赖**：组织级落地需要一号位决心和配套机制，仅靠个人掌握模型不够。
4. **文化情境限制**：「审美」「创造力」的定义高度依赖个人主义和专业分工文化。在集体主义或高度等级制组织中，这两个要素的权重和表达方式可能不同。
5. **小团队 overload**：六要素矩阵对 1-3 人小团队可能过于复杂。小团队应先用「场景 + 审美 + 基本功」三要素简化版跑起来，再逐步补全。
6. **案例样本量**：D 同学、天末、阿豪、陈天等案例均来自个体经验（n=1），不能简单泛化为普适规律。

### 外部攻击

**Daniel Kahneman 的噪声批判**：即使两个人都用双三角分析同一任务，他们对「审美标准」「场景 ROI」的判断也可能差异巨大。框架减少偏差，不减少噪声。

**Henry Mintzberg 的管理教育批判**：把协作拆成六个格子，可能制造「知道框架 = 具备能力」的幻觉。真正的高手协作依赖共同语境和快速适配，而不是每次都画三角。

**Nassim Taleb 的反脆弱性质疑**：过度依赖结构化画布和流程，可能降低团队应对意外场景的能力。框架应是脚手架，不是牢笼。

**Luciano Floridi 的数据尊严批判**：把人的反馈全部结构化并喂给 AI，可能让人变成「数据奶牛」。需要确保人对数据有控制权和解释权。

**技术时效性攻击**：「能写成函数的判断不要交给大模型」这一原则可能只有 1-2 年半衰期。随着模型能力提升，越来越多今天需要规则化的判断未来可能被模型可靠执行。

---

## 七、Synthesis

### 与已有卡的关系

| 关系 | 目标节点 | 说明 |
|:---|:---|:---|
| 前身/旧版 | [[人机协作决策-双三角模型]] | 旧卡描述三阶段成熟度模型，本卡是课程正式版方法论 |
| 前身/旧版 | [[concept-AI时代双三角竞争力]] | 旧卡侧重竞争力描述，本卡补充推导、飞轮、暗知识 |
| 决策基础 | [[yt-decision-y-model]] | 双三角是 Y 模型在 AI 协作时代的实例化 |
| 运行时 OS | [[system-yitang-Y-model-os]] | TCPR 身份协议和角色 context 是双三角运转的操作系统 |
| 能力展开 | [[framework-yihang-dual-triangle-weapon-library]] | 六要素 × 四级修炼的完整能力矩阵 |
| 段位路径 | [[framework-yihang-dual-triangle-ten-year-map]] | L1-L6 的十年进阶地图 |
| 落地场景 | [[framework-yihang-dual-triangle-three-stages-six-changes]] | X光/心法/画布/拼图/地图/底牌 |
| 落地流程 | [[framework-yihang-dual-triangle-ai-landing-five-steps]] | 定场景→做计划→快验证→工程化→做迭代 |
| 操作工具 | [[tool-yihang-dual-triangle-canvas]] | 空版+解释版+清单版三合一画布 |
| 智能体 | [[agent-spec-dual-triangle-canvas-filler]] | 九层深挖对话式画布填充 Agent |

---

## Action Triggers

| 触发场景 | 第一个动作 | 成功指标 |
|:---|:---|:---|
| 要开始一个 AI 协作项目 | 先填一行双三角画布，不要直接丢模糊需求 | 六要素中至少 4 个有具体答案 |
| AI 输出质量不稳定 | 诊断：缺审美？缺数据？缺体系？缺场景？ | 能指出是哪个要素导致偏差 |
| 团队争论「AI 能不能替代人」 | 用「人才能做的事」原则重新划分边界 | 每个环节明确人/AI 分工 |
| 学了很多 AI 工具但效果一般 | 停止追工具，回到人类三角补审美和体系 | 能用自己的话定义「好结果」和「标准流程」 |
| 组织级 AI 落地受阻 | 检查：规则是否显性化？一号位是否坚定？ | 规则文档化、一号位公开承诺 |
