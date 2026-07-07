---
id: concept-token-capital
title: Token Capital：AI 时代的第三种资本结构
type: concept
status: enriched
author: 老顽童
reviewed_by: 欧阳锋
confidence: 0.82
trust_level: medium
language: zh-CN
created_at: 2026-07-08
updated_at: 2026-07-08
domain:
- ai-native
- management
- strategy
source_refs:
- 00_inbox/AI前哨站第2集/AI前哨站第2集-水水拆书.md
- 00_inbox/AI前哨站第2集/水水-AI前哨-第二期-口述.txt
- pending_archive:Satya Nadella，Possible.fm Podcast：《Satya Nadella on Making Human and Token Capital Compound》（2026-06）
quality_labels:
- insight
- principle
- cited
related:
- "[[framework-ai-native-organization-two-modes]]"
- "[[concept-ai-native-organization-five-steps]]"
- "[[tool-月白-Token效价比决策法]]"
- "[[tool-月白-Token智甲比控制法]]"
- "[[dk-ai-builder-illusion]]"
- "[[framework-taste-as-judgment-system]]"
- "[[concept-jevons-paradox-in-ai]]"
- "[[agent-spec-codex-teammate]]"
- "[[concept-AI时代双三角竞争力]]"
aliases:
- token capital
- 第三种资本结构
- AI 时代资本结构
---

# Token Capital：AI 时代的第三种资本结构

> **Burn line**: AI 时代公司的资本结构不再只是「人力资本 + 数字资产」，还要加上「token capital」——把知识、流程、反馈、判断变成可被模型使用、可复利、可控制的智能资产。

---

## 一句话

**Token capital** 是公司把自己的人、知识、流程、反馈、工作轨迹转化为可被 AI 模型使用、可复利、可控制的智能资产的能力。它正在成为 AI 时代企业竞争力的核心变量之一。

---

## 1. 三种资本结构

| 资本类型 | 传统定义 | AI 时代的新含义 | 关键问题 |
|:---|:---|:---|:---|
| **人力资本** | 员工的知识、技能、经验 | 人不再只是执行者，而是判断者、品味守护者、问题定义者 | 如何让人的判断被模型学习和复用？ |
| **数字资产** | 数据、代码、文档、系统 | 从静态仓库变成可被 agent 实时读取和更新的活资产 | 哪些数字资产是 AI 可读且可更新的？ |
| **Token capital** | 知识、流程、反馈、判断、工作轨迹的可复利智能资产 | 公司把组织智慧转化为模型可消费的「上下文资本」 | 你公司有多少东西能变成 token capital？ |

> 来源：拆书稿「Satya Nadella：AI 不是一个技术项目，而是公司的未来形态」；口述稿 L1084-L1098。

---

## 2. Token Capital 的组成

### 2.1 知识资产（Knowledge Assets）

- 领域 know-how
- 业务规则与判断标准
- 客户洞察与用户需求
- 竞品分析与市场认知

### 2.2 流程资产（Process Assets）

- 标准化工作流
- 决策节点与审批规则
- 异常处理路径
- 人机协作边界

### 2.3 反馈资产（Feedback Assets）

- 专家纠正记录
- 评估标准与成败案例
- 用户反馈与迭代历史
- 模型输出的好坏标注

### 2.4 轨迹资产（Trajectory Assets）

- 任务下达方式
- Agent 尝试执行记录
- 专家如何纠正结果
- 系统如何改进下一轮

> Nadella 原话：「企业真正应该积累的，不只是数据，而是人如何下达任务、agent 如何尝试执行、专家如何纠正结果、评估如何判断成败、下一次系统如何改进。」[确认]

---

## 3. Token Capital 的积累路径

```
Step 1: 记录所有工作痕迹（artifacts）
    ↓
Step 2: 把痕迹结构化，变成 AI 可读的上下文
    ↓
Step 3: 让 agent 在真实任务中调用并学习
    ↓
Step 4: 用专家反馈持续校正模型输出
    ↓
Step 5: 把校正后的知识固化回 token capital
    ↓
Step 6: 形成复利循环：更多任务 → 更多痕迹 → 更准模型
```

### 3.1 记录痕迹（YC Dream Cycle 模式）

Pete Koomen 提到 YC 的做法：所有 agent 对话对全职员工可见，每天晚上自动读取当天对话，寻找可改进之处 [确认]。

这不是记录结论，而是记录**所有痕迹**——包括错误的尝试、中间的假设、被否定的方向。

### 3.2 结构化上下文

痕迹本身不等于 token capital。需要把痕迹转化为：
- 可检索的知识库
- 可注入 prompt 的 context
- 可评估模型的 private eval
- 可自动更新的规则文件（如 AGENTS.md）

### 3.3 专家反馈闭环

Token capital 不是自动增长的，需要：
- 人定义什么是对的
- 人纠正 agent 的错误
- 人判断什么应该被固化到系统里

---

## 4. 治理原则

### 4.1 可控性：知道自己的 AI 供应链

- 哪些知识被模型吸收？
- 模型在什么样的环境里学习？
- 哪些数据不会被外部模型带走？

### 4.2 可验证性：建立 Private Eval

公开 benchmark 衡量通用能力，但不能衡量一家公司的具体工作。每家公司都需要自己的 private eval：
- 真实业务任务
- 内部专家标注
- 持续回归测试

### 4.3 可复利性：避免一次性消耗

Token capital 不是一次性的 prompt 工程，而是可以被多任务、多 agent 复用的资产。判断标准：
- 同一知识是否被多个 agent 调用？
- 同一反馈是否能改进多个任务？
- 新任务是否能继承已有 token capital？

### 4.4 人机共治：不是数据独裁

Token capital 的质量取决于人的判断。不能把所有痕迹都喂给模型，需要人筛选：
- 哪些是高质量信号？
- 哪些是噪音或错误？
- 哪些知识应该被保留在人的脑中而非模型中？

---

## 5. Token Capital 与 Token 效价工具的关系

| 层次 | 概念 | 关系 |
|:---|:---|:---|
| **概念层** | Token Capital | 企业层面的战略资产：把组织智慧转化为模型可消费的上下文资本 |
| **工具层** | `tool-月白-Token效价比决策法` | 个人/团队层面的操作工具：判断什么任务值得用贵模型、什么任务用便宜模型 |
| **控制层** | `tool-月白-Token智甲比控制法` | 个人/团队层面的操作工具：控制 token 消耗与输出质量的平衡 |

Token capital 是「为什么要积累 token 资产」的战略回答；token 效价工具是「如何花好每一笔 token」的战术回答。两者互补。

---

## 6. 外部攻击：Token Capital 会被模型厂商稀释吗？

### 攻击 1：模型越来越通用，公司的私有知识优势会被拉平

**回应**：通用模型解决的是「知道」，token capital 解决的是「知道这家公司具体怎么做」。私有 eval、私有流程、私有反馈仍然是壁垒。

### 攻击 2：模型厂商可能通过 API 吸收企业数据

**回应**：这正是可控性原则的重要性。企业需要：
- 明确数据使用协议
- 在可控环境（私有云/本地）中训练/微调
- 区分「可外传数据」和「核心知识资产」

### 攻击 3：token capital 积累太慢，不如直接用最新模型

**回应**：最新模型解决的是通用能力上限，token capital 解决的是「把通用能力适配到具体业务」的效率。没有 token capital，每次任务都要从零写 prompt、从零解释背景。

---

## 7. 失败模式

| 失败模式 | 症状 | 根因 | 修复动作 |
|:---|:---|:---|:---|
| **把数据当 token capital** | 买了大量数据，但 agent 还是用不起来 | 数据没有结构化、没有与业务任务对齐 | 从具体任务出发，反向定义需要什么 token capital |
| **痕迹不记录** | 每次任务从零开始，专家经验无法复用 | 没有系统化记录 artifacts 的机制 | 建立「所有 agent 对话可见」和「工作痕迹自动归档」机制 |
| **模型学错东西** | agent 输出越来越差，重复历史错误 | 低质量痕迹被喂给模型，没有专家过滤 | 建立人主导的 feedback loop 和 private eval |
| **token capital 私有化过度** | 所有知识都锁在本地，无法与外部最佳实践对齐 | 过度防御，错失模型进步红利 | 区分核心知识（私有）和通用方法（可借用外部） |
| **忽视合规与隐私成本** | 敏感数据被意外用于模型训练 | 没有清晰的 AI 供应链审计 | 建立数据分级制度和模型调用审计日志 |

---

## 8. Decision Triggers

| 触发场景 | 第一个动作 |
|:---|:---|
| 评估公司 AI 成熟度 | 问：我们有哪些知识/流程/反馈已经被转化为 token capital？ |
| 启动一个 AI 项目 | 问：这个项目能沉淀什么 token capital？ |
| 选择模型供应商 | 问：我们的核心 token capital 是否会在供应商环境中暴露？ |
| 评估 AI 投资回报 | 不只算降本增效，算 token capital 的复利积累速度 |
| 招聘 AI 相关人才 | 优先找能把隐性判断显性化、变成 token capital 的人 |

---

## 9. 与其他知识的关联

- [[framework-ai-native-organization-two-modes]]：Agent 平台形态的运转依赖 token capital。
- [[concept-ai-native-organization-five-steps]]：YC 五步法中的「上下文资产 > 代码资产」与 token capital 直接对应。
- [[tool-月白-Token效价比决策法]] / [[tool-月白-Token智甲比控制法]]：token 资本概念在操作层的落地工具。
- [[dk-ai-builder-illusion]]：没有 token capital 积累，builder 做出来的东西无法复利。
- [[concept-jevons-paradox-in-ai]]：token 成本下降会激发更多 token capital 需求。
- [[agent-spec-codex-teammate]]：Codex 使用规范中 AGENTS.md、技能固化都是积累 token capital 的具体动作。
