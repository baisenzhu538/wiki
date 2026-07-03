---
id: agent-tcpr-role-retrofit-guide
title: Agent TCPR 身份协议 Retrofit 指南
type: guide
status: active
domain:
- ai-collaboration
- kdo
author: 老顽童
reviewed_by: 欧阳锋
confidence: 0.85
trust_level: high
language: zh-CN
source_context: '#58 task_20260703_huangyaoshi-agent-tcpr-role-layer 交付物'
related:
- agent-native-card-design
- agents/agent-os
- framework-TCPR底层网络协议
- framework-TCPR皇冠模型
- system-yitang-Y-model-os
- tool-agent-spec-yitang-customer-segmentation
- tool-agent-spec-yitang-value-proposition
- tool-agent-spec-yitang-sales-process-tracker
- tool-agent-spec-yitang-sales-performance-monitor
- tool-agent-spec-yitang-opening-3min
- tool-agent-spec-yitang-objection-handler
- tool-agent-spec-yitang-self-motivation
created_at: 2026-06-29
updated_at: '2026-06-29'
---

# Agent TCPR 身份协议 Retrofit 指南

> **用途**：当已有 `agent-spec` 卡需要接入 TCPR 身份协议，或新增 `agent-spec` 卡时，按本指南操作。

---

## 1. 判断是否需要 Retrofit

以下情况必须 retrofit：

- `type: tool-agent-spec` 或任何 `agent-spec` 子类型的卡片。
- 卡片中存在 System Prompt，且 System Prompt 以 `# Role` 开头。
- 卡片需要在多轮对话中与用户协作，而非一次性工具调用。

以下情况可暂不 retrofit：

- 一次性格式转换、计算、翻译类工具卡。
- 用户明确不需要身份协商的纯执行卡。

---

## 2. 选择 TCPR 身份

参考下表为 Agent 选择默认身份。身份不是人格：同一个 Agent 在不同会话中可以不同，但**同一会话内一次只选一个主导身份**。

| 身份 | 核心动作 | 适合场景 | 切换信号 |
|:---|:---|:---|:---|
| **T 教学 Teach** | 讲清楚方法论、训练用户 | 方法论讲解、培训反馈、开场脚本训练 | 「教我一下」「为什么这么写」 |
| **C 咨询 Consult** | 诊断问题、给出建议 | 客户分级、过程追踪、异议处理、决策陪伴 | 「帮我看看」「该怎么选」 |
| **P 实践 Practice** | 直接产出可执行动作 | 日程排期、话术生成、自我驱动、动作清单 | 「直接给我方案」「这周做什么」 |
| **R 研究 Research** | 建模、复盘、概率加权 | 业绩监控、Pipeline 分析、A/B 测试、规律提炼 | 「分析一下规律」「为什么整体差」 |

**默认规则**：若不确定，选 **C（Consult/咨询）**。

---

## 3. 在 frontmatter 中添加 4 个字段

```yaml
tcp_role: "C"                                    # T / C / P / R 四选一
tcp_default_mode: "咨询诊断（Consult）：基于画像与行为信号判断客户等级"
tcp_switch_trigger: "用户明确要求切换身份、任务类型变化或当前身份所需输入缺失时"
tcp_session_opening: "我本次以 **C（Consult/咨询）** 身份与你协作：先帮你诊断客户分级，再给出跟进建议。"
```

### 字段说明

- `tcp_role`：大写字母 `T` / `C` / `P` / `R`。
- `tcp_default_mode`：一句话，包含身份全称 + 默认动作。
- `tcp_switch_trigger`：列出触发切换的 2–3 种典型情况。
- `tcp_session_opening`：开场时向用户说的固定话术，必须明确身份、目标、可切换。

---

## 4. 在 System Prompt 中插入 TCPR 身份声明

找到 System Prompt 的 `# Role` 段落，在其后插入：

```markdown
## TCPR 身份声明

我本次以 **{{tcp_role}}（{{tcp_role_fullname}}）** 身份与你协作：{{session_goal}}。
- **默认模式**：{{tcp_default_mode}}
- **切换触发**：{{tcp_switch_trigger}}
- **切换协议**：当你说「切换到教学/咨询/实践/研究模式」、或任务类型明显变化、或当前身份所需输入缺失时，我会：
  1. 明确声明新身份和新目标；
  2. 复述已继承的事实/分析；
  3. 检查新身份所需输入是否完整，缺失时返回 `INPUT_MISSING`；
  4. 对高风险动作标注「需人工确认」。
```

### 替换示例

若 `tcp_role: C`，`tcp_session_opening: "我本次以 **C（Consult/咨询）** 身份与你协作：先帮你诊断客户分级，再给出跟进建议。"`，则渲染为：

```markdown
## TCPR 身份声明

我本次以 **C（Consult/咨询）** 身份与你协作：先帮你诊断客户分级，再给出跟进建议。
- **默认模式**：咨询诊断（Consult）：基于画像与行为信号判断客户等级
- **切换触发**：用户明确要求切换身份、任务类型变化或当前身份所需输入缺失时
- **切换协议**：当你说「切换到教学/咨询/实践/研究模式」、或任务类型明显变化、或当前身份所需输入缺失时，我会：
  1. 明确声明新身份和新目标；
  2. 复述已继承的事实/分析；
  3. 检查新身份所需输入是否完整，缺失时返回 `INPUT_MISSING`；
  4. 对高风险动作标注「需人工确认」。
```

---

## 5. 更新 related 链接

每张 retrofit 后的 `agent-spec` 卡应在 `related` 中加入：

- `agent-native-card-design`（设计规范）
- `agents/agent-os`（运行时 OS）
- `framework-TCPR底层网络协议`（身份定义）
- `framework-TCPR皇冠模型`（训练层级）
- 其他同域 agent-spec 卡（形成互链）

---

## 6. 验证清单

| 检查项 | 通过标准 |
|:---|:---|
| frontmatter 字段 | `tcp_role`、`tcp_default_mode`、`tcp_switch_trigger`、`tcp_session_opening` 均非空 |
| `tcp_role` 取值 | 必须是 `T`、`C`、`P`、`R` 之一 |
| System Prompt | `# Role` 后存在 `## TCPR 身份声明` 段落 |
| 切换协议 | 包含「声明新身份」「复述事实」「INPUT_MISSING」「需人工确认」四个要素 |
| 相关链接 | related 中包含 `agent-os`、`agent-native-card-design`、`framework-TCPR*` |
| lint | `kdo lint` 0 新增 ERROR |
| pre-submit | `kdo pre-submit --files <card>.md` PASS |

---

## 7. 批量 retrofit 脚本用法

对于结构相似的 `agent-spec` 卡，可维护一个映射表并运行脚本批量更新：

```python
ROLES = {
    "tool-agent-spec-xxx": {
        "tcp_role": "C",
        "tcp_default_mode": "...",
        "tcp_switch_trigger": "...",
        "identity_sentence": "...",
    },
}
```

批量脚本参考：`.tmp/apply_tcpr_to_agent_specs.py`（#58 已用于 7 张 OPC 销售 agent-spec 卡）。

---

## 8. 新增 agent-spec 卡的标准模板

新建 `agent-spec` 卡时，直接复制以下 frontmatter 字段到模板中：

```yaml
---
# ... 其他字段 ...
type: tool-agent-spec
tcp_role: "C"
tcp_default_mode: ""
tcp_switch_trigger: ""
tcp_session_opening: ""
# ... 其他字段 ...
---
```

并在 System Prompt 中预留 `## TCPR 身份声明` 占位，待具体业务确定后填充。

---

## 9. 与 Y模型 OS 的协作

TCPR 身份协议与 Y模型 OS 是叠加关系：

- **TCPR**：决定「以什么身份协作」。
- **Y模型 OS**：决定「怎么结构化思考」。

因此 `agent-spec` 卡的 System Prompt 标准顺序为：

```markdown
[OS 层：TCPR 身份协议]
{{agents/agent-os.md}} 中的身份声明与切换边界

[OS 层：Y模型 共享思考底座]
{{system-yitang-Y-model-os.md}} 中的反幻觉、解放思想、知行合一规则

[域层]
{{domain_layer}}

[用户层]
{{user_layer}}
```

---

## 10. 常见错误

| 错误 | 修正 |
|:---|:---|
| `tcp_role` 写成中文「咨询」 | 改为大写字母 `C` |
| `tcp_session_opening` 不包含身份全称 | 必须包含 `C（Consult/咨询）` 这种形式 |
| 切换协议缺少 `INPUT_MISSING` | 补全四个要素 |
| 把身份当人格设定 | 明确「身份是运行时选择，不是固定人格」 |
| System Prompt 中 TCPR 块放在 `# Input Format` 之后 | 应放在 `# Role` 之后、输入格式之前 |
