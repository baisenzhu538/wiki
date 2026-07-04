---
id: task_20260704_wangyuyan-dual-triangle-canvas-agent-cli
type: task
status: reviewed
assignee: 黄药师
reviewer: 欧阳锋
reviewed_by: 欧阳锋
review_date: 2026-07-04
priority: P1
created_at: 2026-07-04
updated_at: 2026-07-04
source_task: null
related:
- "[[agent-spec-dual-triangle-canvas-filler]]"
- "[[tool-yihang-dual-triangle-canvas]]"
- "[[concept-yihang-dual-triangle-core]]"
- "[[framework-yihang-dual-triangle-weapon-library]]"
- "[[method-dual-triangle-flywheel-engine]]"
---

# 任务 #69：双三角画布 Agent CLI 交付

## 目标

交付一个可运行、可测试的一行双三角画布填充 CLI Agent（`kdo-tools/canvas-agent.py`），让用户通过命令行完成九层深挖对话，最终输出标准化双三角画布，并自动记录飞轮迭代。

**角色定位（TCPR）**：画布 Agent 默认以 **C（Coach/教练）** 身份运行——通过追问、挖掘、结构化，把用户零散表达沉淀到画布，不下判断、不给标准答案。但 TCPR 身份是运行时协议，用户可以通过指令让 Agent 切换到 T/P/R 模式，不应把画布 Agent 的行为模式固定死。

**建设方法**：这个 Agent 本身必须用 Truman PPT 案例所展示的同一套方法建设——以双三角六要素为设计支架，用 Y模型 作为迭代发动机，先跑起来再每天迭代，而不是一次性追求完美。它是 KDO Agent 化的第一个试点，后面会有一系列 Agent 用同样流水线产出。

## 验收标准

- `python kdo-tools/canvas-agent.py run` 能完成至少 3 个真实场景的交互式九层画布填充。
- `python kdo-tools/canvas-agent.py test --scenario <name>` 能非交互运行预设场景并输出 trace。
- 输出画布符合 `tool-yihang-dual-triangle-canvas.md` 的标准格式。
- 画布每个六要素格子都有用户确认依据，不编造。
- 会话结束时自动触发飞轮四问，并能把用户反馈写入 `flywheel_log`。
- agent-spec v2 必须声明默认 `tcp_role: C`，并定义切换到 T/P/R 的触发条件。
- 通过 `kdo pre-submit` 和至少 5 组真实模型测试。
- 欧阳锋终审通过。

## 依赖

1. **王语嫣先完成 agent-spec v2**：`30_wiki/tools/agent-spec-dual-triangle-canvas-filler.md` 必须升级到 v2，补全 TCPR 字段、输入/输出门、动态裁剪规则、真实案例 few-shot。
2. **本任务不阻塞第一批 14 张卡修复**，但 Agent 质量依赖双三角卡片深度。
3. **飞书 / Hermes Agent 本期不做**，列入停车场。

## 任务分解

| 子任务 | 负责人 | 输出 | 阻塞 |
|:---|:---|:---|:---|
| 1. agent-spec v2 | 老顽童/王语嫣 | `30_wiki/tools/agent-spec-dual-triangle-canvas-filler.md` v2 | 无；必须基于 #64/#65 完成后 dual-triangle 最新理解 |
| 2. CLI 工具实现 | 黄药师 | `kdo-tools/canvas-agent.py` | 依赖子任务 1 |
| 3. 测试场景设计 | 王语嫣 | `60_feedback/agent-traces/canvas-agent/scenarios.json` | 依赖子任务 1 |
| 4. 真实模型测试 | 老顽童 | `60_feedback/agent-traces/canvas-agent/2026-07-0X/` trace | 依赖子任务 2、3 |
| 5. 文档与注册 | 黄药师 | README 登记 + 工具卡更新 + 队列更新 | 依赖子任务 2、4 |
| 6. 每日迭代机制 | 老顽童 | 每日/每周基于真实使用 trace 微调 prompt 和状态机 | Agent 上线后持续进行；不阻塞初次交付 |

**关键原则**：
- 子任务 1 的 agent-spec v2 不再由王语嫣单独写，而是由老顽童基于 #64/#65 产出的最新 dual-triangle 理解来生产，王语嫣负责方向把关。这与 Truman 做 partner 的方法一致：先双三角画布，再 Agent。
- Agent 必须具备「模型/体系边界意识」：默认根据用户问题判断任务类型（决策型 / 执行型 / 探索型 / 验证型），再选择对应框架或工具；不能把所有问题都塞进 ROI 或双三角画布。
- Agent 调用的 method/tool 卡必须显式说明其适用边界，不能编造。

## Agent 设计支架：用双三角六要素自检

在写 agent-spec v2 和实现 CLI 之前，必须先填一张该 Agent 自身的双三角画布：

| 要素 | 本 Agent 的画布答案（初版，会迭代） |
|:---|:---|
| 审美 | 输出的画布要「结构完整、不编造、用户可确认」；默认 C 角色以教练式追问为主，不替代用户判断 |
| 体系 | 九层深挖状态机 → 场景 → 审美 → 体系 → 创造力 → 数据 → 基本功 → 飞轮四问 → 输出画布；支持运行时 TCPR 切换 |
| 创造力 | 不替代用户思考，而是把用户零散表达结构化；未来可扩展到 voice/飞书/多 Agent 协作 |
| 场景 | 用户面对一个复杂 AI 协作目标，需要快速搭出双三角画布；适合 CLI 单用户深度会话 |
| 数据 | 双三角核心概念卡、案例卡、方法卡作为 RAG 来源；用户历史画布作为个人数据 |
| 基本功 | Python CLI、DeepSeek API、YAML agent-spec、可选 card-reader RAG、flywheel log、TCPR 运行时切换协议 |

**说明**：这张画布本身就是第一版朴素框架认知，会随着 Agent 上线后的真实使用而迭代。

## CLI 功能规格

### 状态机

```python
class CanvasSession:
    state: Literal[
        "task", "scenario", "aesthetic", "system",
        "creativity", "data", "fundamental", "flywheel", "canvas"
    ]
    context: dict              # 累计用户输入
    layer_outputs: dict        # 每层结论
    complexity: Literal["full", "light", "mini"]  # 动态裁剪
```

### 子命令

- `python kdo-tools/canvas-agent.py run`：交互式对话，按状态机推进。
- `python kdo-tools/canvas-agent.py test --scenario <name>`：非交互运行预设场景，输出到 `60_feedback/agent-traces/canvas-agent/`。
- `python kdo-tools/canvas-agent.py compile`：调用 `agent-prompt-compiler.py` 重新编译 prompt。

### LLM 调用

- 默认 DeepSeek API（Anthropic-compatible endpoint，与 `run_agent_spec_tests.py` 一致）。
- 支持 `--model` 覆盖。

### RAG 集成（可选开关 `--rag`）

- 启动 `card-reader.py` 子进程。
- 在第 2/3/4/7 层自动查询相关卡片（场景/审美/体系/基本功）。
- 默认关闭，避免增加复杂度。

### 飞轮记录

- 会话结束前自动问飞轮四问。
- 用户回答后调用 `python kdo-tools/flywheel.py log ...`。

### 输出纪律

- 每层结束时用一句话总结当前层结论。
- 只有完成所有层后才输出完整画布。
- 画布中每个要素都标注用户原话或确认依据。

## 停车场

| 项目 | 原因 | 重启条件 |
|:---|:---|:---|
| Hermes / 飞书 Agent | 本期聚焦 CLI 验证；飞书部署复杂，需额外处理并发、鉴权、消息格式 | CLI Agent 通过欧阳锋终审，且用户明确需要群聊/多用户版本时 |
| 多 Agent 协作画布 | 本期先让单 Agent 跑通；多 Agent 协作（如 10 个 Agent 同时填画布）是下一阶段 | 单 Agent 日活稳定、用户反馈闭环跑通后 |

## 系列化规划

画布 Agent 是 KDO 用「双三角 + Y模型」方法建设的**第一个 Agent**。后续可用同一流水线建设：
- 审美反馈 Agent
- 数据飞轮设计 Agent
- Y模型 迭代教练 Agent
- 案例拆解 Agent

每个 Agent 都遵循：**先画自身双三角画布 → 写 agent-spec → CLI 验证 → 每日 trace 迭代**。

## 风险

- 双三角卡片深度不足会拉低 Agent 输出质量。
- DeepSeek API 波动或限流会影响测试。
- `flywheel.py` 表结构需确认 `impact_loop` 等字段当前是否可空。

## 备注

- 计划文件：`C:/Users/Administrator/.kimi-code/sessions/wd_administrator_52e285c74c1f/session_19fdfc9e-c26f-4ddf-88a4-fc6b14bc65e0/agents/main/plans/jubilee-taskmaster-forager.md`

---

## 王语嫣暗知识补充 (2026-07-04)

### 画布不只是一个填充工具——它是风险判断工具

口述稿 L4595-4604 Truman 透露了一堂内部的关键操作细节：

> "我们周二周三的时候内部规定，只要他能把双三角画布画出来，我们就敢对外承诺。过去是从来没有过的，就胆子达到这种程度了。只要双三角我们有信心，有足够多的feature，有足够多的没有出的牌，我们就算是给你们承诺了，说这周有它，那最后给我们24小时或者48小时，我们硬干也搞出来。"

**洞察**：画布填满 ≠ 计划完成。画布填满 = **风险可控**。因为填满了意味着你知道每个角有什么牌可打，即使现在没做出来，也知道缺什么、怎么补。

对 Agent 的影响：
- `canvas-agent.py` 的输出不仅是画布本身，还应该输出一个**风险判断**：哪些格子的填充是"确认"（有真实资产），哪些是"假设"（还需要验证），哪些是"空白"（高风险）。
- 如果某个格的置信度低，Agent 应主动追问、补数据。
- 填满的画布 = "可以承诺交付"，而不是"已经做完了"。
