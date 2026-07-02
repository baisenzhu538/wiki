---
id: task_20260702_laowantong-opc-sales-agent-incremental-specs
title: "OPC 销售智能体军团增量：开场/异议/自我驱动 3 张 agent-spec"
type: task
status: in_progress
priority: P2
assignee: 老顽童(Kimi)
reviewer: 欧阳锋
created_at: 2026-07-02
updated_at: 2026-07-02
started_at: 2026-07-02
expected_cards: 3
dependencies:
  - "[[task_20260702_laowantong-yitang-scientific-sales-methodology-production]]"
  - "[[task_20260702_laowantong-opc-sales-agent-specs-production]]"
source_refs:
  - "[[framework-yitang-scientific-sales-five-step]]"
  - "[[tool-yitang-value-proposition-4step]]"
  - "[[tool-yitang-sales-process-decomposition]]"
  - "[[framework-yitang-sales-incentive-6d]]"
  - "[[tool-yitang-sales-toolkit-radar]]"
  - "[[tool-opc-sales-dialogue-assistant]]"
  - "[[opc-ai-sales-agent-architecture]]"
related:
  - tool-agent-spec-yitang-opening-3min
  - tool-agent-spec-yitang-objection-handler
  - tool-agent-spec-yitang-self-motivation
  - tool-agent-spec-yitang-customer-segmentation
  - tool-agent-spec-yitang-value-proposition
  - tool-agent-spec-yitang-sales-process-tracker
  - tool-agent-spec-yitang-sales-performance-monitor
  - tool-opc-sales-dialogue-assistant
  - opc-ai-sales-agent-architecture
---

# OPC 销售智能体军团增量：开场/异议/自我驱动 3 张 agent-spec

> 任务来源：用户提出「边做边玩」地补充销售智能体军团缺口。本任务作为 `#47` 的增量，覆盖一堂科学销售域中尚未 agent 化的三个高频场景：开场前 3 分钟、客户异议处理、一人公司创始人的自我驱动与复盘。
> 依赖：`#44` 终审通过；建议 `#47` 完成至少 2 张卡后再启动，但任务单可以提前准备。
> 原则：Agent 做带宽，人做判断；只输出建议，不替代关键人际信任建立。

---

## 一、3 张目标 Agent 规格卡

### Card 1: `tool-agent-spec-yitang-opening-3min`

**类型**：tool-agent-spec  
**主域**：personal-os / ai-sales-agent / sales  
**来源卡**：`framework-yitang-scientific-sales-five-step`（接触决策部分）、`tool-yitang-sales-toolkit-radar`  
**confidence**：0.84  
**trust_level**：medium

**解决场景**：
- 首次电话/微信接触客户，不知道第一句话说什么。
- 开场容易变成产品倾销或冷场。

**输入**：
- 客户来源（主动搜索/转介绍/展会/线索列表）
- 已知客户背景（行业、公司规模、职位、痛点线索）
- 当前阶段目标（接触决策：建立信任 + 争取提问权）
- 产品/服务一句话定位

**输出**：
1. 30 秒自我介绍脚本
2. 价值钩子（点出客户处境 + 给出希望，不卖产品）
3. 第一个开放式问题（争取提问权）
4. 过渡句（自然进入诊断）
5. 反模式提醒

**触发条件**：
- 新客户首次接触前
- 添加微信后第一句话
- 电话接通后前 3 分钟

**边界与风险提示**：
- 不替代真实人际信任建立
- 不夸大产品能力
- 不涉及报价或合同细节

**依赖的方法论卡**：
- `framework-yitang-scientific-sales-five-step`
- `tool-yitang-sales-toolkit-radar`
- `tool-yitang-customer-segmentation-4step`

**System Prompt 模板**：需提供。

**Related**：≥5 条。

---

### Card 2: `tool-agent-spec-yitang-objection-handler`

**类型**：tool-agent-spec  
**主域**：personal-os / ai-sales-agent / sales  
**来源卡**：`tool-yitang-value-proposition-4step`、`tool-yitang-sales-process-decomposition`、`dk-yitang-sales-common-pitfalls`  
**confidence**：0.83  
**trust_level**：medium

**解决场景**：
- 客户提出价格太贵、再考虑一下、要跟竞品比、没预算、领导没批等异议。
- 创始人不知道异议背后是真实抗拒还是借口。

**输入**：
- 客户异议原文
- 当前销售阶段
- 客户分层等级
- 已传递的卖点
- 历史对话上下文

**输出**：
1. 异议类型判断（价格/时机/权限/信任/竞品/需求不明确）
2. 异议背后的真实顾虑（1-2 个）
3. 应对策略（先共情 → 澄清 → 给证据 → 推进）
4. 2-3 个回复选项（直接型/共情型/提问型）
5. 是否需要升级处理（如需要创始人亲自出面）

**触发条件**：
- 客户明确表达抗拒或犹豫时
- 客户提及竞品时
- 客户拖延决策时

**边界与风险提示**：
- 不贬低竞品
- 不承诺无法兑现的效果
- 对法律/价格/合同敏感问题提醒人工复核

**依赖的方法论卡**：
- `tool-yitang-value-proposition-4step`
- `tool-yitang-sales-process-decomposition`
- `dk-yitang-sales-common-pitfalls`

**System Prompt 模板**：需提供。

**Related**：≥5 条。

---

### Card 3: `tool-agent-spec-yitang-self-motivation`

**类型**：tool-agent-spec  
**主域**：personal-os / ai-sales-agent / sales  
**来源卡**：`framework-yitang-sales-incentive-6d`（OPC 改编版）  
**confidence**：0.80  
**trust_level**：medium

**解决场景**：
- 一人公司没有销售团队，创始人自己跟进客户时容易懈怠、拖延、内耗。
- 需要把「六维激励」改编成个人自我驱动系统。

**输入**：
- 本周/本月销售目标
- 当前 pipeline 状态
- 已完成的销售动作
- 用户自定义的激励方式（如完成目标后奖励自己什么）

**输出**：
1. 本周/今日最小可执行动作清单
2. 动机提醒（为什么这个目标重要）
3. 进度反馈（已完成 vs 目标）
4. 小胜利庆祝建议
5. 倦怠预警信号

**触发条件**：
- 每周一早晨
- 每天工作开始前
- 连续 3 天没有跟进客户时
- 目标完成率低于 50% 时

**边界与风险提示**：
- 不替代真实销售动作
- 不制造虚假紧迫感
- 提醒用户区分「忙」和「有效推进」

**依赖的方法论卡**：
- `framework-yitang-sales-incentive-6d`
- `tool-yitang-sales-performance-management`

**System Prompt 模板**：需提供。

**Related**：≥5 条。

---

## 二、与 `#44` / `#47` 的关系

这三张卡是 `#47` 的增量，进一步完善智能体军团：

```
#44 方法论卡
    ↓
#47 核心技能 Agent（4张：分层/卖点/追踪/业绩）
    ↓
#49 增量 Agent（3张：开场/异议/自我驱动）
    ↓
主 Agent：tool-opc-sales-dialogue-assistant
```

`tool-opc-sales-dialogue-assistant` 可以根据对话上下文调用：
- 开场阶段 → `tool-agent-spec-yitang-opening-3min`
- 客户表达异议 → `tool-agent-spec-yitang-objection-handler`
- 周初/月初 → `tool-agent-spec-yitang-self-motivation`

---

## 三、关键纠偏与边界

1. **不替代真实人际互动**：开场和异议处理是信任建立的关键节点，Agent 只提供草稿，创始人必须自己发送。
2. **不制造销售压力**：自我驱动助手的目标是帮助用户持续行动，而不是制造焦虑。
3. **`#47` 已终审通过**：本任务现在正式启动，依赖已全部满足。
4. **System Prompt 必须可运行**：每张卡提供 system prompt 后，需用 1-2 段真实对话测试。
5. **输出需包含方法论溯源**：调用哪些 KDO 卡、跳过哪些卡、为什么跳过。

---

## 四、验收标准

- [ ] 3 张 agent-spec 卡 `kdo pre-submit` PASS，无新增 ERROR。
- [ ] 3 张 agent-spec 卡 `kdo lint` 0 ERROR；新增 WARNING 需在任务单中说明。
- [ ] 每张卡包含：When to Use、输入、输出、触发条件、边界与风险、依赖的方法论卡、System Prompt 模板、Related。
- [ ] 每张卡包含「输入门」表格：必需输入 / 可选输入 / 缺失时行为。
- [ ] 每张卡 System Prompt 要求输出「方法论溯源」模块。
- [ ] 每张卡 Related ≥5，且至少 2 条跨域。
- [ ] System Prompt 模板在 Claude 或 GPT 中实测可运行，输出格式稳定。
- [ ] `opc-ai-sales-agent-architecture.md` 的 related 已加入 3 张新卡回链，并补充其在智能体军团中的位置。
- [ ] `opc-ai-sales-agent-architecture.md` 正文中补充 7 张 agent-spec 卡（#47 的 4 张 + #49 的 3 张）的调用关系图和场景说明。
- [ ] `tool-opc-sales-dialogue-assistant` 的 related 已加入 3 张新卡回链。
- [ ] 3 张新 agent-spec 的 System Prompt 在真实对话中实测，并记录迭代日志。
- [ ] 欧阳锋终审通过。

---

## 五、生产顺序建议

| 批次 | 卡片 | 说明 |
|:---|:---|:---|
| 第一批 | `tool-agent-spec-yitang-opening-3min` | 开场是所有对话的入口，优先做 |
| 第二批 | `tool-agent-spec-yitang-objection-handler` | 直接提升对话助手回复质量 |
| 第三批 | `tool-agent-spec-yitang-self-motivation` | 偏个人 OS，放在最后 |

---

## 六、队列位置

- **入队编号**：`#49`
- **状态**：`in_progress`
- **依赖**：`#44` 已终审通过；`#47` 已终审通过
- **预计工时**：老顽童生产 2-3 天 + 欧阳锋终审 1 天

---

*王语嫣 2026-07-02*
