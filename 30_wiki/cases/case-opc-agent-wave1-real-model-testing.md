---

id: case-opc-agent-wave1-real-model-testing
title: 案例：OPC 销售智能体 Wave 1 真实模型测试
type: case
status: enriched
author: 老顽童
reviewed_by: 欧阳锋
confidence: 0.85
trust_level: medium
language: zh-CN
domain:
- ai-collaboration
- sales
- yitang
source_person: 老顽童
source_context: OPC 销售智能体军团 #47/#49 产出后，欧阳锋在终审中指出 System Prompt 尚未在真实模型运行，遂启动 #50 Wave 1 实测
source_refs:
- 60_feedback/tasks/task_20260702_laowantong-opc-sales-agent-testing-wave1.md
- 60_feedback/agent-traces/2026-07-02/_summary.json
related:
  - "[[tool-agent-spec-yitang-customer-segmentation]]"
  - "[[tool-agent-spec-yitang-value-proposition]]"
  - "[[tool-agent-spec-yitang-sales-process-tracker]]"
  - "[[tool-agent-spec-yitang-sales-performance-monitor]]"
  - "[[tool-agent-spec-yitang-opening-3min]]"
  - "[[tool-agent-spec-yitang-objection-handler]]"
  - "[[tool-agent-spec-yitang-self-motivation]]"
  - "[[tool-opc-sales-dialogue-assistant]]"
  - "[[opc-ai-sales-agent-architecture]]"
  - "[[human-ai-collaboration-double-triangle]]"
  - "[[framework-kdo-self-attack]]"
created_at: 2026-07-03
updated_at: '2026-07-03'

---

# 案例：OPC 销售智能体 Wave 1 真实模型测试

> 核心结论：把 7 张 agent-spec 卡放到 deepseek-v4-pro 真实模型中跑 14 个场景，发现的主要问题不是「答案错」，而是「答案太长被截断」「阶段判断依赖缺失输入」「输出格式不够紧凑」。修复后复测，截断问题消失，输出完整可用。

---

## 一、Background：为什么测

- #47 和 #49 产出了 7 张 OPC 销售智能体 agent-spec 卡，每张都带 System Prompt 模板。
- 欧阳锋终审时的首要改进点：System Prompt 尚未在 Claude/GPT 真实环境运行，存在「纸上谈兵」风险。
- 目标：用真实模型 + 真实销售对话场景验证可用性，触发 KDO 回流，形成可复用的 Agent 测试工作流。

## 二、Problem：核心矛盾

| 矛盾 | 说明 |
|:---|:---|
| Prompt 很长，模型输出有上限 | 7 张卡的 System Prompt 平均约 2000-3000 token，加上复杂输入，容易触及 4096 token 输出上限 |
| 场景复杂，输入信息不完整 | 创始人实际使用时不会每次都提供完整里程碑、分层标签、历史记录 |
| 需要区分「可用」与「完美」 | 测试不是为了证明 Agent 完美，而是发现边界问题和回流素材 |

## 三、Decision：关键决策

1. **用真实 API 测，不用本地小模型糊弄**。
   环境中有 `ANTHROPIC_BASE_URL` 指向 deepseek-v4-pro 的 Anthropic 兼容端点，直接调用 `/v1/messages`。
2. **14 个场景覆盖 4 个行业域**。
   医药零售 B2B、SaaS/企业服务、门店零售/美业、OPC 创始人自我驱动。
3. **发现问题后修复 prompt 并复测**。
   不是只记录问题，而是回到 agent-spec 卡升级 System Prompt，再跑一轮验证修复效果。

## 四、Process：测试流程

| 步骤 | 动作 |
|:---|:---|
| 1. 搭建 harness | 编写 `run_agent_spec_tests.py`，自动提取 System Prompt、读取测试场景、调用 API、保存 trace |
| 2. 准备场景 | 每个 agent-spec 2 个场景，共 14 个；输入均为脱敏合成数据 |
| 3. 首轮实测 | 2026-07-03 跑完 14 个场景，保存到 `60_feedback/agent-traces/2026-07-02/` |
| 4. 人工评判 | 老顽童逐条检查输出完整性、可用性、边界合规性 |
| 5. 修复 prompt | 对 customer-segmentation、performance-monitor、sales-process-tracker、opening-3min、self-motivation 升级 v1.1 |
| 6. 复测 | 对 customer-segmentation 和 performance-monitor 两个截断场景再跑一轮，确认截断消失 |
| 7. 回流 | 更新 7 张 agent-spec 迭代日志，产出 KDO 回流清单，新建本 case 卡 |

## 五、Result：主要发现

| 类别 | 数量 | 代表问题 |
|:---|:---:|:---|
| P0 阻塞 | 0 | 无有害、违法、越界输出 |
| P1 需修复 | 2 | customer-segmentation 5 线索场景输出截断；performance-monitor 10 客户 Pipeline 输出截断 |
| P2 可优化 | 5 | 过程追踪缺里程碑时降级为「粗略草案」；开场模式 A 回复篇幅偏大；卖点 PPT 版文字堆叠；异议处理竞品报价提醒不足；自我激励预测用百分比 |
| P3 建议 | 若干 | 增加更多行业场景、增加工作节律输入门等 |

**修复后复测结果**：

- customer-segmentation 医药零售 5 线索 v1.1：输出 4061 字符，完整覆盖 5 条线索，方法论溯源未截断。
- performance-monitor 智能药柜 10 客户 v1.1：输出 4400 字符，完整覆盖 Top 5 + 长尾策略 + 方法论溯源，未截断。

## 六、Lessons：可迁移教训

1. **System Prompt 必须跑真实模型才能发现长度问题**。人在写 prompt 时很难感知 4096 token 输出上限。
2. **「输入门」设计要包含「超长怎么办」**。如果用户一次塞太多线索或客户，Agent 需要主动建议分批或输出摘要。
3. **默认框架能显著提升可用性**。当用户没提供定制里程碑时，用通用四阶段框架兜底，不要让 Agent 直接说「我没法判断」。
4. **完成率/概率要用高中低，不要用具体百分比**。伪精确会削弱 Agent 的可信度。
5. **测试自动化脚本要保留**。`run_agent_spec_tests.py` 和场景 JSON 可以作为 Wave 2、Wave 3 的复用基础。

## 七、Failure Modes：常见踩坑

| 失败模式 | 症状 | 修复 |
|:---|:---|:---|
| Prompt 太长导致截断 | 输出到一半突然结束，丢失最后部分 | 增加输出长度控制，长列表先给摘要再展开 Top N |
| 缺输入就降级为粗略草案 | Agent 反复说「需要补充里程碑清单」 | 提供默认框架，先给判断再提示可优化 |
| 模式 A 输出冗余 | 用户只要首条消息，Agent 给了 7 个 section | 明确模式 A 只输出三部分 |
| 用百分比表示不确定 | 「完成率约 35%-60%」 | 改用高/中/低三档 |
| 没规定竞品报价处理 | 客户透露竞品报价时只给通用提醒 | 明确转交创始人 |

## 八、Synthesis：关联卡片

| 已有卡 | 在本案例中的位置 |
|:---|:---|
| [[tool-agent-spec-yitang-customer-segmentation]] 等 7 张 | 测试对象，迭代日志已更新 |
| [[tool-opc-sales-dialogue-assistant]] | 风格参考和主 Agent 调用入口 |
| [[opc-ai-sales-agent-architecture]] | 7 张 agent-spec 的架构位置已补充 |
| [[human-ai-collaboration-double-triangle]] | Agent 做带宽、人做判断 |
| [[framework-kdo-self-attack]] | 测试前的对抗检查框架 |

## 九、Critique：质疑与局限

### 外部反对者

1. **「用 deepseek-v4-pro 代替 Claude/GPT 不够严谨。」**
   - 回应：环境中仅有 deepseek-v4-pro 可用；其输出结构与 Claude 相似，长度问题具有通用性。后续应在 Claude/GPT 上补测。
2. **「14 个场景太少，不能代表真实销售复杂度。」**
   - 回应：Wave 1 的目标是暴露边界问题，不是建立统计显著性。后续 Wave 应增加真实客户对话。
3. **「合成输入毕竟不是真实客户。」**
   - 回应：所有输入已脱敏，且基于 #44 真实课程案例改编；真实客户测试需创始人提供对话记录。

### 内部局限

1. **未做双盲人工评分**：评判由老顽童完成，可能带有确认偏误。
2. **未覆盖所有行业域**：传统工业分销场景仅出现在输入中，未专门测试。
3. **API 响应时间不稳定**：部分调用耗时较长，未做批量并发优化。

---

*卡片类型：case | 来源：#50 Wave 1 实测*
