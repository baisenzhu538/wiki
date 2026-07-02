---
id: task_20260702_laowantong-opc-sales-agent-specs-production
title: "OPC 销售智能体军团首批规格卡：从 #44 方法论卡片编译 4 张 agent-spec"
type: task
status: in_progress
priority: P1
assignee: 老顽童(Kimi)
reviewer: 欧阳锋
created_at: 2026-07-02
updated_at: 2026-07-02
started_at: 2026-07-02
expected_cards: 4
dependencies:
  - "[[task_20260702_laowantong-yitang-scientific-sales-methodology-production]]"
source_refs:
  - "[[KDO-Agent化审计报告-20260702]]"
  - "[[framework-yitang-scientific-sales-five-step]]"
  - "[[tool-yitang-customer-segmentation-4step]]"
  - "[[tool-yitang-value-proposition-4step]]"
  - "[[tool-yitang-sales-process-decomposition]]"
  - "[[tool-yitang-sales-performance-management]]"
  - "[[tool-opc-sales-dialogue-assistant]]"
  - "[[opc-ai-sales-agent-architecture]]"
related:
  - tool-agent-spec-yitang-customer-segmentation
  - tool-agent-spec-yitang-value-proposition
  - tool-agent-spec-yitang-sales-process-tracker
  - tool-agent-spec-yitang-sales-performance-monitor
  - framework-yitang-scientific-sales-five-step
  - tool-yitang-customer-segmentation-4step
  - tool-yitang-value-proposition-4step
  - tool-yitang-sales-process-decomposition
  - tool-yitang-sales-performance-management
  - tool-opc-sales-dialogue-assistant
  - opc-ai-sales-agent-architecture
  - human-ai-collaboration-double-triangle
---

# OPC 销售智能体军团首批规格卡：从 #44 方法论卡片编译 4 张 agent-spec

> 任务来源：`KDO-Agent化审计报告-20260702` 审计结论：KDO 不缺方法论卡，缺的是「智能体规格卡」层。本任务把 `#44` 销售专题中的 4 张核心 tool 卡编译成可直接作为 system prompt 使用的 agent-spec 卡。
> 依赖：必须等待 `#44` 对应方法论卡终审通过后再开始生产，但任务单可以提前准备。
> 原则：Agent 做带宽，人做判断；这些智能体只输出建议，不自动执行关键销售动作。

---

## 一、4 张目标 Agent 规格卡

### Card 1: `tool-agent-spec-yitang-customer-segmentation`

**类型**：tool-agent-spec  
**主域**：personal-os / ai-sales-agent / sales  
**来源卡**：`tool-yitang-customer-segmentation-4step`  
**confidence**：0.86  
**trust_level**：high

**解决场景**：
- 创始人拿到一份潜在客户名单/聊天记录，需要快速判断谁值得重点跟进。
- 线索太多，销售精力有限，需要自动化分级。

**输入**：
- 客户基本信息（公司/行业/规模/职位）
- 客户行为数据（是否咨询过、咨询内容、来源渠道）
- 当前阶段销售目标（要利润/要标杆/要流水）
- 产品/服务特性描述

**输出**：
1. S/A/B/C 等级
2. 分级理由（一句话）
3. 推荐跟进策略（S 级 1 小时内/ A 级今天/ B 级 3 天内/ C 级放弃或自动培育）
4. 需要进一步验证的假设

**触发条件**：
- 新线索进入时
- 每周对现有线索重新分级时
- 销售目标变化时

**边界与风险提示**：
- 分级结果只是建议，创始人做最终决策
- 涉及客户隐私数据需本地/合规处理
- 不替代深度客户调研

**依赖的方法论卡**：
- `tool-yitang-customer-segmentation-4step`
- `framework-yitang-scientific-sales-five-step`

**System Prompt 模板**：需提供可直接复制到 Claude/GPT 自定义指令的精简模板。

**Related**：≥5 条。

---

### Card 2: `tool-agent-spec-yitang-value-proposition`

**类型**：tool-agent-spec  
**主域**：personal-os / ai-sales-agent / sales  
**来源卡**：`tool-yitang-value-proposition-4step`  
**confidence**：0.85  
**trust_level**：high

**解决场景**：
- 面对不同客户，需要生成差异化的卖点表达。
- 销售话术不统一，各说各话。

**输入**：
- 目标客户画像/分层等级
- 客户当前阶段（接触/购买/付款/履约）
- 客户已表达的需求/痛点
- 产品/服务核心能力
- 竞品信息（可选）

**输出**：
1. 针对该客户的 Top 3 卖点
2. 每个卖点的一句话表达（好听好记）
3. 匹配场景的落地话术（微信/电话/邮件/PPT 各一版）
4. 需要避免的表达（反模式）

**触发条件**：
- 准备跟进某个客户前
- 收到客户需求/抗拒点后
- 要生成提案/报价前

**边界与风险提示**：
- 卖点必须基于真实产品能力，不能夸大
- 创始人需最终审核关键承诺
- 法律/合规敏感表达需人工复核

**依赖的方法论卡**：
- `tool-yitang-value-proposition-4step`
- `framework-brand-three-degree`
- `tool-strategy-value-proposition`

**System Prompt 模板**：需提供。

**Related**：≥5 条。

---

### Card 3: `tool-agent-spec-yitang-sales-process-tracker`

**类型**：tool-agent-spec  
**主域**：personal-os / ai-sales-agent / sales  
**来源卡**：`tool-yitang-sales-process-decomposition`  
**confidence**：0.84  
**trust_level**：medium

**解决场景**：
- 同时跟进多个客户，忘记每个客户卡在哪个阶段。
- 销售周期长，需要预警"卡了很久"的客户。

**输入**：
- 客户对话记录（微信/邮件/通话转写/CRM 备注）
- 当前里程碑清单（来自 `tool-yitang-sales-process-decomposition`）
- 历史跟进记录

**输出**：
1. 当前阶段判断（接触/购买/付款/履约）
2. 距离下一个里程碑还差什么
3. 卡点识别（客户犹豫点/未回复/未履约）
4. 下一步建议动作
5. 风险预警（停滞超过 X 天）

**触发条件**：
- 每次客户互动后
- 每日/每周销售巡检时
- 收到客户新消息后

**边界与风险提示**：
- 不自动发送催促消息
- 对"停滞"的判断需结合业务常识
- 关键节点的人际沟通仍需人来做

**依赖的方法论卡**：
- `tool-yitang-sales-process-decomposition`
- `framework-yitang-scientific-sales-five-step`

**System Prompt 模板**：需提供。

**Related**：≥5 条。

---

### Card 4: `tool-agent-spec-yitang-sales-performance-monitor`

**类型**：tool-agent-spec  
**主域**：personal-os / ai-sales-agent / sales  
**来源卡**：`tool-yitang-sales-performance-management`  
**confidence**：0.83  
**trust_level**：medium

**解决场景**：
- 一人公司没有销售周会，但需要 Gap 分析和下周计划。
- 业绩目标完不成时，不知道差距在哪。

**输入**：
- 月度/季度销售目标
- 当前 pipeline（客户清单 + 阶段 + 预期金额 + 概率）
- 历史成交数据
- 时间范围

**输出**：
1. 目标完成率与 Gap
2. 按客户/阶段/渠道的拆解
3. 需要重点推进的 3-5 个客户
4. 下周/下月建议策略（含 Plan B）
5. 需要关注的风险信号

**触发条件**：
- 每周日晚上/周一早上
- 月度目标 review 时
- 业绩出现明显波动时

**边界与风险提示**：
- 预测基于概率，不是保证
- 创始人需结合外部信息调整策略
- 不替代财务/现金流判断

**依赖的方法论卡**：
- `tool-yitang-sales-performance-management`
- `yt-management-goal-management`
- `yt-business-formula-six-level-logic`

**System Prompt 模板**：需提供。

**Related**：≥5 条。

---

## 二、与 `tool-opc-sales-dialogue-assistant` 的关系

`tool-opc-sales-dialogue-assistant`（#44 中的 Card 12）是**总体 MVP 对话助手**，它把读对话/想策略/给话术三件事合在一起。

本任务产出的 4 张 agent-spec 卡是它的**底层能力模块**：

| 模块 | 功能 | 被对话助手调用 |
|:---|:---|:---:|
| `tool-agent-spec-yitang-customer-segmentation` | 判断客户等级 | 是 |
| `tool-agent-spec-yitang-value-proposition` | 生成差异化卖点 | 是 |
| `tool-agent-spec-yitang-sales-process-tracker` | 识别阶段和卡点 | 是 |
| `tool-agent-spec-yitang-sales-performance-monitor` | 判断推进优先级 | 是 |

也就是说，`tool-opc-sales-dialogue-assistant` 是用户直接面对的"销售教练"，而这 4 张卡是它背后的"专业技能库"。

---

## 三、关键纠偏与边界

1. **不替代人际信任建立**：这些智能体处理的是判断带宽，不是关键信任节点。关键谈判、冲突处理、深度共情仍需人来做。
2. **不自动执行**：所有智能体只输出建议，不自动发送消息、不改 CRM、不承诺客户。
3. **隐私与合规**：客户数据在本地或合规环境中处理；system prompt 中不硬编码真实客户信息。
4. **依赖 #44 终审**：必须等 `#44` 对应方法论卡通过欧阳锋终审后，才能开始编译 agent-spec。
5. **MVP 优先**：本任务只产出 4 张规格卡，不铺开全部 8-10 个智能体；验证有效后再扩展。
6. **System Prompt 必须可运行**：每张卡提供的 system prompt 模板需经过至少一次 Claude/GPT 实测，确保输出格式稳定。

---

## 四、验收标准

- [ ] 4 张 agent-spec 卡 `kdo pre-submit` PASS，无新增 ERROR。
- [ ] 4 张 agent-spec 卡 `kdo lint` 0 ERROR；新增 WARNING 需在任务单中说明。
- [ ] 每张卡包含：When to Use、输入、输出、触发条件、边界与风险、依赖的方法论卡、System Prompt 模板、Related。
- [ ] 每张卡包含「输入门」表格：必需输入 / 可选输入 / 缺失时行为。
- [ ] 每张卡 System Prompt 要求输出「方法论溯源」模块：说明调用了哪些 KDO 卡、哪些被跳过及原因。
- [ ] 每张卡 Related ≥5，且至少 2 条跨域。
- [ ] System Prompt 模板在 Claude 或 GPT 中实测可运行，输出格式稳定。
- [ ] 实测输出必须包含方法论溯源模块，且溯源内容与卡片设计一致。
- [ ] `opc-ai-sales-agent-architecture.md` 的 related 已加入 4 张新卡回链，并补充这 4 个模块在智能体军团中的位置。
- [ ] `tool-opc-sales-dialogue-assistant` 的 related 已加入 4 张模块卡回链。
- [ ] 欧阳锋终审通过。

---

## 五、生产顺序建议

| 批次 | 卡片 | 说明 |
|:---|:---|:---|
| 第一批 | `tool-agent-spec-yitang-customer-segmentation` | 数据最清晰，最容易验证 |
| 第二批 | `tool-agent-spec-yitang-value-proposition` | 依赖客户分层结果 |
| 第三批 | `tool-agent-spec-yitang-sales-process-tracker` | 依赖过程拆解卡 |
| 第四批 | `tool-agent-spec-yitang-sales-performance-monitor` | 综合前三个模块，放在最后 |

---

## 六、队列位置

- **入队编号**：`#47`
- **状态**：`queued`
- **依赖**：`#44` 终审通过后开始生产
- **预计工时**：老顽童生产 3-4 天 + 欧阳锋终审 1 天

---

## 七、真实对话测试基准与迭代要求

> 本节记录了一次前置测试的结果，作为老顽童生产时的迭代基准。

### 7.1 测试背景

- **测试时间**：2026-07-02
- **测试对象**：一个基于 `tool-opc-sales-dialogue-assistant` 风格的 system prompt 原型
- **输入素材**：`D:\Backup\Downloads\133 7050 9008_20260702143456.m4a.txt`（药店/医保局/智能药柜销售对话录音转写）
- **测试目的**：验证「读对话 → 想策略 → 给话术」四段式输出在真实 B2B 销售场景中的可用性

### 7.2 测试结果：基本可用，达到 MVP 门槛

**做得好的地方**：
- 阶段判断准确（购买阶段）
- 客户分层合理（A 级，有 S 级潜力）
- 下一步建议具体可执行（发案例型资料、准备分步报价、约定下次沟通时间）
- 回复选项有区分度（直接型/共情型/提问型）
- 风险提示到位（价格一致性、数据合规、竞品风险）

**需要迭代的问题**：

| 问题 | 表现 | 修正方向 |
|:---|:---|:---|
| 微信第一条消息过长/过界 | 共情型开场「您这边想得很清楚」显得过度奉承 | 收敛共情尺度，第一条消息控制在 50-80 字，避免越界认可 |
| 缺少 contingency | 客户最大卡点是「医保局是否给接口」，但建议中没有「如果拿不到接口」的 B 计划 | 增加「关键卡点不可行时的替代路径」输出项 |
| 高价值信号未转化为验证问题 | 「基金+全国投放」只在风险提示中列出，没有直接问客户 | 在提问型回复或下一步建议中给出具体验证问题 |
| 置信度伪精确 | 输出「置信度 0.75」给人虚假精确感 | 改用「高/中/低」或「7/10」等更克制的表达方式 |
| 价格/合规提醒位置偏后 | 价格一致性和数据合规只在风险提示出现 | 把「口头报价需后续书面确认」「数据安全责任边界」前置到「下一步建议」中 |

### 7.3 对老顽童的迭代要求

1. **每张 agent-spec 卡必须用真实对话测试**：至少 1-2 段脱敏后的真实销售对话（微信/邮件/通话转写），不能只用假设场景验证。
2. **把测试中发现的问题写进卡片**：作为该 agent 的 Anti-patterns 或「常见失败模式」小节。
3. **System Prompt 模板必须包含示例输出**：至少 1 个优质示例 + 1 个失败示例 + 1 条修正说明。
4. **迭代日志格式**：每张卡在 `## 迭代日志` 中记录测试轮次、发现的问题、修正动作。
5. **最终验收标准增加**：欧阳锋终审时，除检查卡片结构外，还需抽查至少 1 段测试对话和对应的 agent 输出。

### 7.4 需要固化到 `tool-opc-sales-dialogue-assistant` 的要点

- 输出「回复选项」时，第一条微信消息长度优先控制在 80 字以内。
- 当对话中出现「外部审批/接口/政策依赖」等关键卡点时，必须输出 contingency。
- 当客户透露出「资金/规模/扩张」等高价值信号时，必须输出至少 1 个验证问题。
- 置信度评分禁用伪精确小数，统一使用三档或 10 分制。

---

## 八、方法论溯源与激活条件要求

> 本节基于 Agent 的自我反馈形成。Agent 不仅能调用 KDO 卡，还应该能解释自己调用了哪些卡、为什么调用、哪些卡因缺上下文没有激活。

### 8.1 每张 agent-spec 卡必须定义「输入门」

在 System Prompt 或卡片正文中，必须明确：

| 输入类型 | 说明 | 缺失时的行为 |
|:---|:---|:---|
| 必需输入 | 没有这些输入，Agent 无法给出可靠判断 | 明确告知用户缺什么，并停止输出或给出降级建议 |
| 可选输入 | 有这些输入，输出精度更高 | 说明「如果提供 X，我可以给出更精准的判断」 |
| 上下文输入 | 历史记录、目标、产品信息等 | 缺失时使用默认值或保守假设，并在输出中标注 |

例如 `tool-agent-spec-yitang-value-proposition`：
- 必需输入：目标客户画像、客户当前阶段
- 可选输入：Top3 卖点、竞品信息
- 缺失行为：如果没有 Top3 卖点，Agent 只能从对话中自然提取价值点，并在溯源中说明「未调用 `tool-yitang-value-proposition-4step`，因为缺少正式卖点输入」。

### 8.2 输出必须包含「方法论溯源」模块

每张 agent-spec 卡的 System Prompt 必须要求输出中包含一个独立模块（可放在「风险提示」之前或之后）：

```markdown
## 方法论溯源
- 本次分析直接调用的 KDO 卡：...
- 本次分析间接使用的方法论：...
- 因缺少上下文未调用的 KDO 卡：...（说明缺失的输入）
- 如果补充以下信息，输出会更精准：...
```

这个模块的作用是：
- 让用户知道建议从哪里来
- 方便调试：如果输出质量差，可以追溯到哪张卡没被正确调用
- 为 KDO 沉淀「卡片使用热力图」数据

### 8.3 Agent 角色分层

基于这次测试，明确两类 Agent 卡：

| 类型 | 代表 | 用户交互方式 | 调用关系 |
|:---|:---|:---|:---|
| 主 Agent 卡 | `tool-opc-sales-dialogue-assistant` | 用户直接面对 | 调用多个技能 Agent |
| 技能 Agent 卡 | `#47` 产出的 4 张 agent-spec | 主 Agent 内部调用，也可独立使用 | 被主 Agent 调用 |

`tool-opc-sales-dialogue-assistant` 的 System Prompt 中，应该明确告知它在哪些场景下调用这 4 张技能卡，以及如何整合它们的输出。

### 8.4 测试用例保存要求

这次测试使用的 `D:\Backup\Downloads\133 7050 9008_20260702143456.m4a.txt` 应该作为 `tool-opc-sales-dialogue-assistant` 的**标准测试用例**保存到任务单或卡片附录中（脱敏后）。

后续每张 agent-spec 卡生产时，都应该有类似的 1-2 个标准测试用例。

---

*王语嫣 2026-07-02*
