---
id: task_20260704_wangyuyan-agent-card-skill-execution-pattern
title: Agent 基于 KDO 卡片/Skill 解决实际问题的执行模式设计
type: task
status: queued
assignee: 黄药师
reviewer: 欧阳锋
priority: P1
created_at: 2026-07-04
updated_at: 2026-07-04T19:25:00+00:00
reviewed_by: pending
source_refs:
- 00_inbox/人机协作双三角/一堂双三角-人机协作模型-口述.txt
- kdo-tools/aesthetic-library-builder.py
related:
- "[[agent-os]]"
- "[[agent-native-card-design]]"
- "[[framework-yitang-y-model-dual-triangle-synergy]]"
- "[[tool-yihang-dual-triangle-canvas]]"
- "kdo-tools/aesthetic-library-builder.py"
---

# 任务 #73：Agent 基于 KDO 卡片/Skill 解决实际问题的执行模式设计

## 问题背景

用户提出尖锐问题：「如果我们以后要建 agent，你如何让他们根据知识库里面的卡片也好，skills也好，怎么帮助他们解决实际的问题呢？」

这不是一个抽象的设计问题，而是 KDO Agent 化的核心落地问题。当前状态：
- KDO 已经有大量卡片（concept/framework/method/tool/case/dk）和 skill。
- Agent 规范（agent-os.md、agent-native-card-design.md、TCPR 角色层）已就位。
- 但 Agent 运行时如何**主动检索、组合、调用**这些资产来解决用户具体问题，还没有形成可执行模式。

本任务要求黄药师设计并实现一个可运行的模式，让 Agent 能把 KDO 卡片/Skill 当成「活的知识库」，而不是静态背诵材料。

---

## 核心命题

1. **Agent 不应该背会所有卡片，而应该知道何时查哪张卡。**
2. **Agent 不应该只给答案，而应该用双三角/Y模型 方法引导用户把问题拆清楚。**
3. **Agent 的 system prompt 不应该手写所有知识，而应该由 `agent-prompt-compiler` 动态编译：OS 层 + 域卡 + 相关 case/method/tool。**
4. **Agent 解决完问题后，必须把过程沉淀为飞轮日志，回流到 KDO。**

---

## 设计目标

产出：
1. 一份可执行的设计文档 `60_feedback/design/agent-card-skill-execution-pattern.md`
2. 一张可复用框架/方法卡 `framework-kdo-agent-card-skill-execution-pattern`（或 `method-kdo-agent-uses-cards`），把执行模式固化为 KDO 资产
3. 一个最小可运行原型 `kdo-tools/agent-solver.py`

设计文档必须明确：

| 模块 | 目标 |
|:---|:---|
| 检索层 | Agent 如何根据用户问题调用 `kdo query` / `kdo link-suggest` / `kdo cards` 找到相关卡片 |
| 规划层 | Agent 如何把问题映射到双三角画布，判断缺哪些要素；**同时判断任务类型，不把决策框架硬套到执行问题** |
| 执行层 | Agent 如何调用 Skill/Tool（包括 `aesthetic-library-builder.py` 这类新工具）完成任务 |
| 输出层 | Agent 如何给出可落地、可验证、可追溯的结果 |
| 回流层 | Agent 如何把对话/结果写入 `flywheel_log`，更新相关卡片 `related` |

---

## 必须回答的具体问题

### Q1：Agent 怎么找到该用哪张卡？

要求实现以下检索链路：

```
用户问题 → 关键词/意图识别 → kdo query --related <id> --limit 5
         → 若 confidence 低，调用 kdo link-suggest --from <card-id>
         → 返回 top N 相关卡片（概念卡/方法卡/工具卡/案例卡）
         → Agent 在 system prompt 中引用这些卡片的核心内容
```

- 必须支持按 domain 过滤（如只查 `ai-collaboration` / `yitang`）。
- 必须支持按卡片类型过滤（如优先 method/tool，再 case）。
- 必须处理「卡片存在但内容不够」的情况：Agent 应标记缺口，而不是编造。

### Q2：Agent 怎么把问题映射到双三角画布？

要求 Agent 默认走以下流程：

1. 用 `tool-yihang-dual-triangle-canvas` 的清单版，把用户问题填成六要素草稿。
2. 对每一要素，追问用户确认：
   - 审美：好结果的标准是什么？
   - 体系：解决这类问题的稳定流程是什么？
   - 创造力：有哪些隐含假设可以挑战？
   - 场景：高价值切口在哪里？
   - 数据：有什么数据/最佳实践可用？
   - 基本功：需要哪些工具组合？
3. 当某个格子为空或弱时，Agent 主动调用相关 method/tool 卡补充。

### Q3：Agent 怎么调用 Skill/Tool 解决实际问题？

要求实现一个统一调用接口，示例：

```python
# 伪代码
agent.run(
    user_query="帮我为商业培训 PPT 建立审美库",
    steps=[
        {"tool": "kdo-tools/aesthetic-library-builder.py", "args": ["init", "ppt-commercial-training"]},
        {"skill": "aesthetic-fast-build", "args": {"topic": "商业培训 PPT"}},
        {"card": "method-yihang-aesthetic-fast-build"},
    ]
)
```

- Skill 必须能被编译进 system prompt。
- Tool 必须能被 Agent 通过 CLI 调用并解析结果。
- 每次调用后 Agent 必须向用户报告：调用了什么、为什么调用、结果是什么。

### Q4：Agent 怎么保证不编造、不抽象？

- 所有引用卡片必须标注卡片 ID。
- 所有建议必须对应到 method/tool 卡的具体步骤。
- 所有案例必须对应到 case 卡的人物/动作/结果。
- 当知识库没有直接答案时，Agent 应说「我缺少 X 卡，建议先补 X」，而不是用漂亮话搪塞。

### Q5：Agent 怎么回流知识到 KDO？

- 每次会话结束调用 `kdo-tools/flywheel.py log` 记录：问题、使用的卡片、用户反馈、缺口。
- 对反复出现的缺口，自动生成 `60_feedback/tasks/` 任务单草稿，提醒王语嫣/老顽童补卡。

---

## 最小可运行原型要求

1. 一个 Python 脚本：`kdo-tools/agent-solver.py`
2. 功能：
   - 接收用户自然语言问题
   - 调用 `kdo query` 找到相关卡片
   - 用双三角画布引导用户澄清问题
   - 根据画布结果调用 1-2 个 tool/skill（先以 `aesthetic-library-builder.py` 为试点）
   - 输出一份可执行的下一步计划
   - 把过程写入 flywheel log
3. 测试场景（至少 3 个）：
   - 「我想为商业培训 PPT 建立审美库」
   - 「我想用 AI 做论文初审，但不知道怎么开始」
   - 「我想让团队用双三角模型协作，但大家不知道怎么填画布」

---

## 阶段划分

| 阶段 | 输出 | 依赖 | 是否阻塞主线 |
|:---|:---|:---|:---:|
| Phase 1：设计文档 + 框架卡 | `60_feedback/design/agent-card-skill-execution-pattern.md` + `framework-kdo-agent-card-skill-execution-pattern` | #59 已 reviewed，可立即启动 | 否 |
| Phase 2：最小可运行原型 | `kdo-tools/agent-solver.py` + 3 个测试场景通过 | #72 审美库工具卡 reviewed（作为试点工具） | 是 |
| Phase 3：与 #69 画布 Agent 集成 | 把执行模式接入画布 Agent 的 tool 调用层 | #69 agent-spec v2 + CLI 实现 | 否 |

**说明**：Phase 1 可以独立产出；Phase 2 需要等 #72 审美库工具卡产出后才能用真实工具做端到端测试；Phase 3 是可选增强，不阻塞本任务验收。

---

## 模型/体系边界意识

Agent 不能默认把所有问题都塞进双三角画布或 ROI 框架。设计文档和原型必须包含：

1. **任务类型判断**：用户问题是决策型、执行型、探索型还是验证型？
2. **框架选择规则**：决策型优先调用 `yt-decision-y-model` / ROI 相关卡；执行型优先调用 method/tool 卡；探索型优先调用解放思想/关键假设相关卡；验证型优先调用实事求是/定量研究相关卡。
3. **边界声明**：每次调用 method/tool 卡时，Agent 必须向用户说明该工具的适用边界和不适用场景。
4. **不自作聪明**：当知识库没有直接答案时，Agent 必须说「我缺少 X 卡，建议先补 X」，而不是用漂亮话搪塞。

---

## 输入素材

- `00_inbox/人机协作双三角/一堂双三角-人机协作模型-口述.txt` 行 2852-2900（partner 用法）
- `kdo-tools/agent-prompt-compiler.py`
- `kdo-tools/aesthetic-library-builder.py`
- `kdo-tools/flywheel.py`
- `30_wiki/system/agent-os.md`
- `30_wiki/system/agent-native-card-design.md`
- `60_feedback/tasks/task_20260704_wangyuyan-dual-triangle-canvas-agent-cli.md`

---

## 验收标准

- 设计文档 `60_feedback/design/agent-card-skill-execution-pattern.md` 完成，覆盖上述 5 个问题
- 框架/方法卡 `framework-kdo-agent-card-skill-execution-pattern`（或等效 ID）产出并 `kdo pre-submit` 通过
- `kdo-tools/agent-solver.py` 可运行，并通过至少 3 个测试场景
- 原型必须真实调用 `kdo query` 和 `aesthetic-library-builder.py`，不伪造结果
- 输出必须引用具体卡片 ID，不是抽象建议；必须能说明所用工具的边界
- `kdo pre-submit` 通过
- 欧阳锋终审通过

---

## 依赖

- #59 Agent Prompt 编译器（已 reviewed，可用）
- #72 审美库采集工具卡（产出后作为试点工具）
- #69 双三角画布 Agent CLI（可选，不阻塞本任务原型）

---

## 备注

本任务直接回应用户对「Agent 如何活用知识库」的质疑。设计文档和原型必须避免漂亮话，每一步都要对应到可执行的命令、可引用的卡片、可验证的结果。王语嫣将持续跟踪，确保设计不偏离「解决实际问题」的目标。
