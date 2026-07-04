---
id: agent-card-skill-execution-pattern
type: design
status: draft
phase: 1
related:
  - '[[agent-os]]'
  - '[[agent-native-card-design]]'
  - '[[framework-yitang-y-model-dual-triangle-synergy]]'
  - '[[tool-yihang-dual-triangle-canvas]]'
  - '[[method-yihang-aesthetic-fast-build]]'
  - '[[tool-aesthetic-library-builder]]'
  - '[[task_20260704_wangyuyan-agent-card-skill-execution-pattern]]'
---

# Agent 基于 KDO 卡片/Skill 解决实际问题的执行模式（Phase 1 设计骨架）

> 直接回应用户质疑：「Agent 怎么根据知识库里面的卡片/Skill 解决实际问题？」
> 本文件为 Phase 1 设计骨架；Phase 2 将基于本骨架实现 `kdo-tools/agent-solver.py` 原型。

---

## 一、背景与目标

### 1.1 当前状态

- KDO 已经有大量 concept/framework/method/tool/case/dk 卡和 skill。
- Agent 规范（agent-os.md、agent-native-card-design.md、TCPR 角色层）已就位。
- 但 Agent 运行时如何**主动检索、组合、调用**这些资产来解决用户具体问题，还没有形成可执行模式。

### 1.2 核心目标

让 Agent 把 KDO 卡片/Skill 当成「活的知识库」：

1. **知道何时查哪张卡**。
2. **用双三角/Y模型 方法引导用户把问题拆清楚**。
3. **根据任务类型选择合适框架/工具**，而不是硬套某个模型。
4. **调用 Skill/Tool 完成实际任务**。
5. **把过程沉淀为飞轮日志，回流到 KDO**。

---

## 二、设计原则

1. **不背卡，只查卡**：Agent 不需要记住所有卡片，但必须知道检索路径。
2. **先拆问题，再给建议**：默认用双三角画布把用户问题结构化。
3. **框架有边界**：根据任务类型（决策/执行/探索/验证）选择对应模型/工具。
4. **调用可追溯**：每次调用 Skill/Tool 都要向用户报告「调用了什么、为什么、结果是什么」。
5. **缺口即任务**：知识库缺卡时，自动生成任务单草稿，而不是编造。
6. **人在环**：人类保持最终判断权；Agent 只输出建议、计划和可验证的下一步。

---

## 三、分层架构

### 3.1 检索层：Agent 怎么找到该用哪张卡？

```
用户问题
  ↓
意图识别 + 关键词提取
  ↓
kdo query --related <seed-card> --limit 5 --domain <domain> --type <type>
  ↓
confidence 高 → 直接引用 top N 卡片
confidence 低 → kdo link-suggest --from <card-id>
  ↓
返回相关卡片列表（concept → framework → method → tool → case → dk）
```

**过滤规则**：

| 用户问题类型 | 优先查询 domain | 优先卡片类型 |
|:---|:---|:---|
| 决策型 | `yitang`、`decision-science` | framework、method、dk |
| 执行型 | 对应业务 domain | method、tool、case |
| 探索型 | `yitang`、`ai-collaboration` | concept、framework、method |
| 验证型 | `yitang`、`research` | method、tool、case |

**处理知识缺口**：

- 如果检索结果 confidence 均 < 阈值，Agent 应声明：「我缺少 X 类卡片，建议先补 X」。
- 禁止用通用漂亮话搪塞。

### 3.2 规划层：Agent 怎么把问题映射到双三角画布？

默认流程：

1. 用 `tool-yihang-dual-triangle-canvas` 清单版，把用户问题填成六要素草稿。
2. 对每一要素追问用户确认：
   - **审美**：好结果的标准是什么？
   - **体系**：解决这类问题的稳定流程是什么？
   - **创造力**：有哪些隐含假设可以挑战？
   - **场景**：高价值切口在哪里？
   - **数据**：有什么数据/最佳实践可用？
   - **基本功**：需要哪些工具组合？
3. 当某个格子为空或弱时，Agent 主动调用相关 method/tool 卡补充。
4. **任务类型判断**：在画布填充前，先判断问题是决策型/执行型/探索型/验证型，并记录到 session context。

### 3.3 执行层：Agent 怎么调用 Skill/Tool 解决实际问题？

统一调用接口（伪代码）：

```python
agent.run(
    user_query="帮我为商业培训 PPT 建立审美库",
    task_type="执行型",
    steps=[
        {
            "action": "query_cards",
            "args": {"topic": "商业培训 PPT 审美", "type": ["method", "tool", "case"]}
        },
        {
            "action": "fill_canvas",
            "args": {"canvas": "tool-yihang-dual-triangle-canvas", "topic": "商业培训 PPT"}
        },
        {
            "action": "run_tool",
            "tool": "kdo-tools/aesthetic-library-builder.py",
            "args": ["init", "ppt-commercial-training"],
            "boundary": "适用于需要批量建立审美库的高价值重复任务；不适用于一次性直觉创作。"
        },
        {
            "action": "run_method",
            "card": "method-yihang-aesthetic-fast-build",
            "args": {"topic": "商业培训 PPT"},
            "boundary": "需要先有可判断维度和标杆案例。"
        },
        {
            "action": "summarize_plan",
            "args": {"output": "executable_next_steps.md"}
        }
    ]
)
```

**调用纪律**：

- 每次调用必须声明工具/方法的来源卡片 ID。
- 每次调用必须说明适用边界。
- 每次调用后必须向用户报告结果和下一步建议。

### 3.4 输出层：Agent 怎么给出可落地、可验证、可追溯的结果？

输出模板：

```markdown
## 问题理解
- 用户原始问题：...
- 判断任务类型：决策型 / 执行型 / 探索型 / 验证型
- 使用的双三角画布：...

## 检索到的 KDO 资产
- [[method-yihang-aesthetic-fast-build]]
- [[tool-aesthetic-library-builder]]
- [[case-yihang-truman-aesthetic-library-practices]]

## 执行动作
1. 调用了 `kdo-tools/aesthetic-library-builder.py init ppt-commercial-training`
2. 依据 `method-yihang-aesthetic-fast-build` 的四步法，建议下一步收集案例

## 可执行的下一步计划
1. ...
2. ...

## 边界与假设
- 本建议基于 X 卡，适用于 Y 场景，不适用于 Z 场景。
- 当前知识库缺口：...
```

### 3.5 回流层：Agent 怎么把过程沉淀到 KDO？

每次会话结束：

1. 调用 `kdo-tools/flywheel.py log` 记录：
   - 用户问题
   - 使用的卡片/工具
   - 用户反馈
   - 知识库缺口
2. 对反复出现的缺口，自动生成 `60_feedback/tasks/` 任务单草稿（如「建议补 X 卡」）。
3. 可选：把高质量会话 trace 归档到 `60_feedback/agent-traces/`，用于后续 prompt 迭代。

---

## 四、模型/体系边界意识

Agent 必须内化的边界规则：

| 任务类型 | 适合的框架/工具 | 不适合的框架/工具 |
|:---|:---|:---|
| 决策型 | ROI、关键决策拆推评算、Y模型 | 直接执行工具 |
| 执行型 | method/tool/case、工作流 | ROI（除非资源分配决策） |
| 探索型 | 解放思想、关键假设体系、科学类比 | 过早定量、过早体系化 |
| 验证型 | 实事求是、定量研究清单、验证成本阶梯 | 空想、跳过低成本验证 |

**强制输出**：每次建议必须附带一句话边界说明。

---

## 五、与已有 KDO 基础设施的衔接

| 已有能力 | 在本模式中的作用 |
|:---|:---|
| `agent-prompt-compiler.py` | 把 agent-os.md + 域卡 + 相关卡片编译成 system prompt |
| `kdo query` / `kdo link-suggest` | 检索相关卡片 |
| `kdo-tools/aesthetic-library-builder.py` | 第一个试点工具 |
| `tool-yihang-dual-triangle-canvas` | 问题结构化画布 |
| `kdo-tools/flywheel.py` | 会话回流和缺口记录 |
| `queue_transition.py` | 自动生成的任务单最终通过队列脚本入队 |

---

## 六、Phase 计划

| Phase | 目标 | 输出 | 状态 |
|:---|:---|:---|:---:|
| Phase 1 | 设计文档 + 可复用框架卡 | 本文档 + `framework-kdo-agent-card-skill-execution-pattern` | 进行中 |
| Phase 2 | 最小可运行原型 | `kdo-tools/agent-solver.py` + 3 个测试场景 | 待启动 |
| Phase 3 | 与 #69 画布 Agent 集成 | 把执行模式接入画布 Agent 的 tool 调用层 | 可选 |

---

## 七、依赖

- **#59 Agent Prompt 编译器**：已 reviewed，可用。
- **#72 审美库采集工具卡**：产出后作为 Phase 2 试点的真实工具。
- **#69 双三角画布 Agent CLI**：Phase 3 可选集成，不阻塞 Phase 1/2。

---

## 八、测试场景（Phase 2 必须覆盖）

1. **「我想为商业培训 PPT 建立审美库」**
   - 应检索到 `method-yihang-aesthetic-fast-build`、`tool-aesthetic-library-builder`、`case-yihang-truman-aesthetic-library-practices`。
   - 应调用 `aesthetic-library-builder.py init ppt-commercial-training`。

2. **「我想用 AI 做论文初审，但不知道怎么开始」**
   - 应先判断为探索型/验证型。
   - 应调用双三角画布，追问场景、数据、基本功。
   - 应检索到相关 method/tool/case，或声明缺口。

3. **「我想让团队用双三角模型协作，但大家不知道怎么填画布」**
   - 应调用 `tool-yihang-dual-triangle-canvas`。
   - 应以 C 角色引导用户逐层澄清，而不是直接给答案。

---

## 九、待决策问题

1. **检索置信度阈值**：多少 confidence 以下触发 `link-suggest`？建议 Phase 2 先用 0.6。
2. **卡片引用深度**：Agent 是把卡片全文注入 prompt，还是只注入摘要？建议先用摘要 + 关键 section。
3. **工具调用安全**：CLI 工具是否需要在沙箱中运行？`aesthetic-library-builder.py` 当前只读/写本地目录，风险低。
4. **回流自动化程度**：flywheel log 自动生成任务单草稿后，是否需要王语嫣人工确认再入队？

---

## 十、下一步

1. 欧阳锋/用户审阅本设计骨架。
2. 王语嫣基于本骨架产出 `framework-kdo-agent-card-skill-execution-pattern` 卡。
3. 黄药师启动 Phase 2，实现 `kdo-tools/agent-solver.py`。
