---

id: tool-Y模型STEPS策略集
title: Y模型STEPS策略集：五步策略框架
type: tool
status: pending_review
author: 老顽童
reviewer: 欧阳锋
reviewed_by: 欧阳锋
confidence: 0.85
trust_level: high
language: zh-CN
domain:
- yitang
- decision-science
- methodology
source_refs:
- 30_wiki/methods/method-yitang-y-model-engine-cycle.md
- 30_wiki/frameworks/framework-yitang-y-model-cross-domain-fusion.md
- 60_feedback/diagnosis/diag_20260708_yitang-y-model-cross-domain-fusion-deep-dive-v2.md
aliases:
  - Y模型STEPS策略集
  - Y模型STEPS策略集：五步策略框架
  - 五步策略框架
  - 策略框架
  - 策略集
discoverable_by:
  - Y模型STEPS策略集：五步策略框架
  - Y模型STEPS策略集
  - 五步策略框架
related:
- '[[yt-decision-y-model]]'
- '[[method-yitang-y-model-engine-cycle]]'
- '[[framework-yitang-y-model-cross-domain-fusion]]'
- '[[agent-spec-yitang-Y-model-cross-domain-coach]]'
- '[[tool-Y模型实操工作流]]'
- '[[tool-yitang-Y-model-application]]'
- '[[dk-yitang-Y-model-pitfalls]]'
created_at: 2026-06-29
updated_at: 2026-07-08 17:38:57+00:00
tags:
- audience:executor
- scene:execution
- skill-level:advanced
---

# Y模型STEPS策略集：五步策略框架

## 一句话

> **一句话**：Y模型 STEPS 策略集 = 把 [[method-yitang-y-model-engine-cycle|Y模型引擎循环]] 封装成「收束 → 立论 → 求据 → 破界 → 同步」五步跨域策略，帮助人和 Agent 在需求分析、产品、五步法、销售、时间管理、AI 落地等域快速定位当前该做什么。

## 目的

本工具解决的核心问题：**Y模型 引擎循环步骤多、跨域映射复杂，使用者容易在「现在该走哪一步」上卡住**。

STEPS 不是另一套方法论，而是 Y模型 引擎循环的**跨域导航缩写**：

- **S（Scope / 收束）**：界定真问题，对应引擎循环步骤 1；
- **T（Thesis / 立论）**：写下粗糙 V1 框架认知，对应引擎循环步骤 2；
- **E（Evidence / 求据）**：关键假设 + 验证成本阶梯 + 事实 / 假设 / 信念分离，对应引擎循环步骤 4–6；
- **P（Paradigm / 破界）**：理论端科学类比 + 解放思想挑战隐含假设，对应引擎循环步骤 3 和 7；
- **S（Sync / 同步）**：更新 V2 + 知行合一 + 飞轮日志，对应引擎循环步骤 8–10。

通过把五步映射到各域的具体动作，STEPS 让跨域迁移有抓手、单域循环有节奏。

> 跨域融合框架参见 [[framework-yitang-y-model-cross-domain-fusion]]；单域 Coach 参考 [[agent-spec-yitang-Y-model-cross-domain-coach]]。

## When to Use

| 触发场景 | 典型信号 | 第一个动作 |
|:---|:---|:---|
| 不确定当前该走 Y模型 哪一步 | 面对复杂问题，不知道先拆变量还是先验证 | 用 STEPS 定位当前所处阶段 |
| 需要跨域迁移 | 想把 A 域的洞察用到 B 域 | 抽象源域的 STEPS 模式，映射到目标域 |
| 单域循环卡壳 | 分析很多但认知没升级 | 检查 STEPS 哪一步被跳过或停留太久 |
| 团队对齐方法论语言 | 各成员对 Y模型 使用节奏不一致 | 用 STEPS 作为统一导航 |
| Agent 引导用户走 Y模型 | 需要一套简洁的跨域话术 | 用 STEPS 五步作为会话节奏 |

## When NOT to Use

| 场景 | 原因 | 替代方案 |
|:---|:---|:---|
| 一次性、低风险的微型决策 | 五步导航 overhead 过高 | 直接决策或快速 A/B 测试 |
| 已有成熟 SOP 的执行任务 | 不需要重新建模 | 按 SOP 执行，事后飞轮复盘 |
| 问题完全属于单一领域且已有域 Agent | 不需要跨域导航 | 直接调用该域 Agent/框架卡 |
| 品味 / 意义型决策 | 不可证伪，不适合假设驱动 | 用 [[framework-taste-as-judgment-system]] |
| 团队尚未建立基本假设驱动习惯 | STEPS 需要一定认知基础 | 先练习把「我认为」改成「我假设」 |

## 操作步骤

### STEPS 与 Y模型引擎循环总览

```
S 收束(Scope)     → 步骤 1：界定真问题
T 立论(Thesis)    → 步骤 2：写下粗糙 V1
E 求据(Evidence)  → 步骤 4–6：关键假设 / 验证 / 事实·假设·信念分离
P 破界(Paradigm)  → 步骤 3 + 7：理论端类比 + 解放思想挑战隐含假设
S 同步(Sync)      → 步骤 8–10：V2 / 知行合一 / 飞轮日志
```

### S — 收束（Scope）：界定真问题

**引擎循环对应**：步骤 1 — 定义真问题。

**核心动作**：

1. 把问题写成一句话：主语 + 动词 + 可观察结果。
2. 连续问 3 次「为什么会这样」，区分症状与根因。
3. 定义成功指标和决策边界。

**跨域映射**：

| 域 | S 的具体动作 | 关键引用 |
|:---|:---|:---|
| 需求分析 | 把「用户不满意」收束为「某场景下某类用户完成某任务的流失率」 | [[framework-demand-iceberg]] |
| 产品内核 | 把「产品不够好」收束为「关键假设 X 在当前场景下是否成立」 | [[framework-一堂五步法-泛产品设计]] |
| 一堂五步法 | 把「增长乏力」收束为「价值假设已验证 vs 增长假设未验证」 | [[yt-five-step-method-complete]] |
| 科学销售 | 把「业绩不好」收束为「Pipeline 缺口 vs 转化率缺口 vs 客单价缺口」 | [[framework-yitang-scientific-sales-five-step]] |
| 时间管理 | 把「时间不够」收束为「单位时间产出或任务匹配度问题」 | [[framework-yitang-five-step-to-time-management]] |
| AI 落地 | 把「AI 效果不好」收束为「上下文 / 人在环 / 工作流哪个环节断裂」 | [[framework-yihang-dual-triangle-ai-landing-five-steps]] |

### T — 立论（Thesis）：写下粗糙 V1

**引擎循环对应**：步骤 2 — 写下朴素框架认知。

**核心动作**：

1. 列出 3–10 条当前对问题的理解，允许粗糙、允许不全、允许部分会错。
2. 标注每条认知来自事实、假设还是信念。
3. 把 V1 外化——写下来才能被审视和挑战。

**跨域映射**：

| 域 | T 的具体动作 | 关键引用 |
|:---|:---|:---|
| 需求分析 | 写出用户对某场景的当前理解（冰山 L1-L3） | [[framework-demand-iceberg]] |
| 产品内核 | 写出产品要解决的关键假设和边界 | [[framework-一堂五步法-泛产品设计]] |
| 一堂五步法 | 写出业务公式 / 单元模型的第一版 | [[yt-five-step-method-complete]] |
| 科学销售 | 写出销售过程拆解的第一版 | [[framework-yitang-scientific-sales-five-step]] |
| 时间管理 | 写出三门模型（任务 / 时间 / 匹配）的初始版本 | [[framework-yitang-five-step-to-time-management]] |
| AI 落地 | 写出双三角六要素的初始框架 | [[framework-yihang-dual-triangle-ai-landing-five-steps]] |

### E — 求据（Evidence）：关键假设 + 验证 + 三列分离

**引擎循环对应**：步骤 4–6 — 关键假设、最小验证、实事求是。

**核心动作**：

1. 把 V1 中的「我认为」「应该是」改写成可证伪的关键假设。
2. 按验证成本阶梯选择最低成本验证方式：常识 → 情报 → 小实验 → 全量。
3. 运行实验后，把认知拆成事实 / 假设 / 信念三列。

**跨域映射**：

| 域 | E 的具体动作 | 关键引用 |
|:---|:---|:---|
| 需求分析 | 拆推评算 + RAT（风险假设测试） | [[framework-demand-iceberg]] |
| 产品内核 | 聊问查测盘赌六策略 + 三问验证 | [[framework-一堂五步法-泛产品设计]] |
| 一堂五步法 | 价值假设 / 增长假设验证，不要过早复制 | [[yt-five-step-method-complete]] |
| 科学销售 | 前三秒 A/B 测试、Pipeline 事实反馈 | [[framework-yitang-scientific-sales-five-step]] |
| 时间管理 | 时间审计 + 双周假设实验 | [[framework-yitang-five-step-to-time-management]] |
| AI 落地 | AI 落地五部曲「快验证」 | [[framework-yihang-dual-triangle-ai-landing-five-steps]] |

### P — 破界（Paradigm）：理论端类比 + 解放思想

**引擎循环对应**：步骤 3（理论端）+ 步骤 7（解放思想）。

**核心动作**：

1. 找 2–3 个跨域类比，把 V1 整合为临时模型。
2. 挑战「信念」列和「只能这样做」的隐含假设。
3. 区分「过时的行业惯例」与「真实的因果规律」。

**跨域映射**：

| 域 | P 的具体动作 | 关键引用 |
|:---|:---|:---|
| 需求分析 | 挑战「用户说的就是要的」；用场景推演替代直接相信 | [[framework-demand-iceberg]] |
| 产品内核 | 做减法 / 划边界；挑战「功能越多越好」 | [[framework-一堂五步法-泛产品设计]] |
| 一堂五步法 | 两次跃迁的换挡条件；挑战商业模式默认前提 | [[yt-five-step-method-complete]] |
| 科学销售 | 挑战「销售必须靠关系」等行业惯例 | [[framework-yitang-scientific-sales-five-step]] |
| 时间管理 | 挑战「必须 8 小时工作制」「所有会都要参加」 | [[framework-yitang-five-step-to-time-management]] |
| AI 落地 | 打破「必须用 PPT 软件做 PPT」等工具迷信 | [[framework-yihang-dual-triangle-ai-landing-five-steps]] |

### S — 同步（Sync）：V2 + 知行合一 + 飞轮

**引擎循环对应**：步骤 8–10 — 更新认知、知行合一、飞轮日志。

**核心动作**：

1. 基于新事实和新视角重写框架认知 V2。
2. 用 V2 做一个真实决策或动作，不要停留在纸上。
3. 写飞轮日志，明确下一轮要回答的新问题。

**跨域映射**：

| 域 | S 的具体动作 | 关键引用 |
|:---|:---|:---|
| 需求分析 | 更新机会卡 / 需求假设库 | [[framework-demand-iceberg]] |
| 产品内核 | 沉淀产品内核文档 / 验证清单 | [[framework-一堂五步法-泛产品设计]] |
| 一堂五步法 | 更新单元模型 / 业务公式 / 壁垒假设 | [[yt-five-step-method-complete]] |
| 科学销售 | 更新销售话术库 / 业绩管理画布 | [[framework-yitang-scientific-sales-five-step]] |
| 时间管理 | 沉淀个人时间操作系统 | [[framework-yitang-five-step-to-time-management]] |
| AI 落地 | 沉淀组织上下文资产 / AI 原生工作流 | [[framework-yihang-dual-triangle-ai-landing-five-steps]] |

### STEPS 使用节奏

```
S → T：先收束再立论，没有真问题不要写 V1
T → E：V1 必须外化，没有外化不要验证
E → P：先实事求是，再解放思想
P → S：没有真实动作和飞轮记录，循环不算完成
S → S'：下一轮用更高分辨率的问题重新开始
```

## 示例

### 示例 1：把销售话术迁移到内容钩子（跨域迁移）

| STEPS | 销售域（源域） | 内容创作域（目标域） | 跨域 Coach 动作 |
|:---|:---|:---|:---|
| S | 问题：电话销售前三秒如何抓住注意力 | 问题：短视频前 3 秒如何留住用户 | 抽象共同目标：前三秒注意力捕获 |
| T | V1：前三秒 = 痛点钩子 + 身份确认 | V1：前三秒 = 冲突前置 + 结果承诺 | 建立临时模型：注意力 = 冲突 × 相关性 × 不确定性 |
| E | 验证：A/B 测试不同开场白的接通率 | 验证：A/B 测试不同开头的 3 秒完播率 | 设计目标域最小验证 |
| P | 挑战：销售必须「先自报家门」 | 挑战：内容必须「先讲背景」 | 列出 source/target 差异 |
| S | 沉淀销售话术库 | 沉淀内容钩子模板 | 在目标域跑一轮验证后归档 |

> 跨域迁移的核心纪律：类比只作说明，不作论证；迁移后必须在目标域跑一轮最小验证。

### 示例 2：产品增长停滞（单域循环卡壳）

- **S**：把「增长停滞」收束为「新用户注册转化率从 15% 降至 10%」。
- **T**：V1： landing page 信息密度过高，导致用户决策成本大。
- **E**：关键假设：精简 landing page 可使注册转化率回升到 13% 以上；验证方式：A/B 测试；实事求是：事实（当前转化率 10%）、假设（精简有效）、信念（用户喜欢简洁）。
- **P**：解放思想：挑战「landing page 必须在首屏展示全部功能」的隐含假设；替代路径：首屏只留一个核心场景故事。
- **S**：V2：注册转化 = 场景匹配度 × 首屏信息效率 × 信任信号；行动：上线新 landing page；飞轮：记录结果，下一轮验证信任信号。

### 示例 3：个人时间管理（自管理域）

- **S**：把「每天都很忙但产出低」收束为「上午 3 小时被碎片化会议切割」。
- **T**：V1：需要更高效的会议工具。
- **E**：时间审计事实：上午平均 4.2 个会议，每个会议间隔 <15 分钟；假设：把会议集中到下午可提升深度工作时长；信念：「同事都需要随时找到我」。
- **P**：解放思想：挑战「必须随时响应」；替代路径：设定深度工作时段 + 异步沟通机制。
- **S**：V2：时间产出 = 深度工作块时长 × 任务匹配度；行动：试行「上午无会议」两周；飞轮：记录产出变化。

## Critique

### 外部攻击者

1. **Daniel Kahneman（判断心理学 /《噪声》）**：把复杂循环压缩成五步缩写，可能让团队误以为每一步都有清晰边界，忽视判断噪声。当不同成员对「当前处于 E 还是 P」有分歧时，STEPS 会把噪声包装成精确的阶段标签。
   - **回应**：STEPS 是导航草案而非终审；每步必须标注置信度、列出反例，并通过迭代复盘收敛噪声。

2. **Gary Klein（自然决策理论）**：专家在高压情境下依赖模式识别（RPD）往往优于结构化阶段分析。强制先用 STEPS 定位阶段，可能拖慢高段位专家的决策速度。
   - **回应**：STEPS 只在跨域、卡壳或团队需要统一语言时触发；答案已知或有成熟 SOP 的场景直接执行。

3. **Paul Feyerabend（科学哲学，《反对方法》）**：创新并非都遵循统一阶段。把 Y模型 包装成 STEPS 五步，可能让团队误以为科学做事就是「先收束再立论再求据」，忽视论辩、偶然和直觉的作用。
   - **回应**：STEPS 是可逆的导航，不是线性流程；在需要时可以从 P 回到 S，或在 E 中发现需要重新 T。

4. **Clayton Christensen（颠覆式创新）**：渐进式优化（E 步骤）做得越好，越容易错过范式级颠覆机会。STEPS 把「破界」放在第四步，可能让团队在前面三步停留太久，错过窗口期。
   - **回应**：STEPS 明确允许「快速破界」——当隐含假设代价极高或行业惯例明显失效时，可以直接进入 P；S 和 T 只需最小化完成。

### 内部局限

1. **缩写可能变成新迷信**：团队可能把 STEPS 当作必须填完的模板，而不是 Y模型 引擎循环的导航。这是从「Y模型 迷信」升级为「STEPS 迷信」。

2. **跨域映射需要持续维护**：随着各域框架卡更新，STEPS 与各域的映射关系需要同步更新，否则会变成过期导航。

3. **对初学者仍有一定门槛**：即使有了 STEPS，零基础者仍可能写不出 V1 或设计不出可证伪假设。需要配套 [[tool-Y模型实操工作流|实操工作流]] 的模板使用。

4. **阶段判断依赖输入质量**：用户问题越模糊，当前处于 STEPS 哪一步的判断越依赖推断，容易误判。

5. **同步步骤最容易被跳过**：很多团队在前四步分析得很完整，但不做知行合一和飞轮日志，导致循环中断。

## Synthesis

Y模型 STEPS 策略集是 [[method-yitang-y-model-engine-cycle|Y模型引擎循环]] 的跨域导航缩写，也是 [[framework-yitang-y-model-cross-domain-fusion|跨域融合框架]] 的运行时简化版。它不是为了替代引擎循环，而是让使用者在复杂、跨域、团队协作者场景下，能快速判断「现在该做什么」。

与 [[tool-Y模型实操工作流|Y模型实操工作流]] 配合，STEPS 提供导航，实操工作流提供模板和检查清单；与 [[agent-spec-yitang-Y-model-cross-domain-coach|跨域 Coach Agent]] 配合，可以作为 Agent 引导用户的默认会话节奏；与 [[dk-yitang-Y-model-pitfalls|六大陷阱]] 配合，可以在每一步识别经验主义、理论迷信、知行分裂等风险。

使用提醒：STEPS 不是线性 SOP，而是可逆的循环导航。真正重要的不是走完五步，而是每一步都推动认知从 V1 向 V2 升级。

## Related

- [[yt-decision-y-model]]
- [[method-yitang-y-model-engine-cycle]]
- [[framework-yitang-y-model-cross-domain-fusion]]
- [[agent-spec-yitang-Y-model-cross-domain-coach]]
- [[tool-Y模型实操工作流]]
- [[tool-yitang-Y-model-application]]
- [[dk-yitang-Y-model-pitfalls]]
- [[framework-demand-iceberg]]
- [[framework-一堂五步法-泛产品设计]]
- [[yt-five-step-method-complete]]
- [[framework-yitang-scientific-sales-five-step]]
- [[framework-yitang-five-step-to-time-management]]
- [[framework-yihang-dual-triangle-ai-landing-five-steps]]
