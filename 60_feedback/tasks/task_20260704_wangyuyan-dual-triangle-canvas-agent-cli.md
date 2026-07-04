---
id: task_20260704_wangyuyan-dual-triangle-canvas-agent-cli
type: task
status: queued
assignee: 黄药师
reviewer: 欧阳锋
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

# 双三角画布 Agent CLI 交付

## 目标

交付一个可运行、可测试的一行双三角画布填充 CLI Agent（`kdo-tools/canvas-agent.py`），让用户通过命令行完成九层深挖对话，最终输出标准化双三角画布，并自动记录飞轮迭代。

## 验收标准

- `python kdo-tools/canvas-agent.py run` 能完成至少 3 个真实场景的交互式九层画布填充。
- `python kdo-tools/canvas-agent.py test --scenario <name>` 能非交互运行预设场景并输出 trace。
- 输出画布符合 `tool-yihang-dual-triangle-canvas.md` 的标准格式。
- 画布每个六要素格子都有用户确认依据，不编造。
- 会话结束时自动触发飞轮四问，并能把用户反馈写入 `flywheel_log`。
- 通过 `kdo pre-submit` 和至少 5 组真实模型测试。
- 欧阳锋终审通过。

## 依赖

1. **王语嫣先完成 agent-spec v2**：`30_wiki/tools/agent-spec-dual-triangle-canvas-filler.md` 必须升级到 v2，补全 TCPR 字段、输入/输出门、动态裁剪规则、真实案例 few-shot。
2. **本任务不阻塞第一批 14 张卡修复**，但 Agent 质量依赖双三角卡片深度。
3. **飞书 / Hermes Agent 本期不做**，列入停车场。

## 任务分解

| 子任务 | 负责人 | 输出 | 阻塞 |
|:---|:---|:---|:---|
| 1. agent-spec v2 | 王语嫣 | `30_wiki/tools/agent-spec-dual-triangle-canvas-filler.md` v2 | 无 |
| 2. CLI 工具实现 | 黄药师 | `kdo-tools/canvas-agent.py` | 依赖子任务 1 |
| 3. 测试场景设计 | 王语嫣 | `60_feedback/agent-traces/canvas-agent/scenarios.json` | 依赖子任务 1 |
| 4. 真实模型测试 | 老顽童 | `60_feedback/agent-traces/canvas-agent/2026-07-0X/` trace | 依赖子任务 2、3 |
| 5. 文档与注册 | 黄药师 | README 登记 + 工具卡更新 + 队列更新 | 依赖子任务 2、4 |

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

## 风险

- 双三角卡片深度不足会拉低 Agent 输出质量。
- DeepSeek API 波动或限流会影响测试。
- `flywheel.py` 表结构需确认 `impact_loop` 等字段当前是否可空。

## 备注

- 计划文件：`C:/Users/Administrator/.kimi-code/sessions/wd_administrator_52e285c74c1f/session_19fdfc9e-c26f-4ddf-88a4-fc6b14bc65e0/agents/main/plans/jubilee-taskmaster-forager.md`
