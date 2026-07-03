---
id: task_20260703_huangyaoshi-agent-prompt-compiler
title: Agent Prompt 编译器：把 agent-os.md + 域卡编译为可注入的 system prompt
type: task
status: queued
priority: P1
assignee: 黄药师
reviewer: 欧阳锋
created_at: 2026-07-01
updated_at: 2026-07-01
source_context: 用户判定 agent-os.md 不能依赖 Claude 的 Read 文件能力，Kimi/Hermes 需要静态 system prompt 注入；要求单列任务建设编译器
estimated_outputs:
- 1 个 CLI 命令或 skill：`kdo agent-build-prompt <agent-id>`
- 1 张设计规范更新：`agent-native-card-design.md` 增加 prompt 编译字段
- 至少 3 个编译后 prompt 文件：Y模型 OS、Y模型 Coach、1 个 OPC 销售 agent-spec
- 1 份使用说明 / 集成示例
dependencies:
- task_20260703_laowantong-yitang-Y-model-os（reviewed 或 pending_review）：提供 system-yitang-Y-model-os.md
- task_20260703_huangyaoshi-agent-tcpr-role-layer（queued）：提供 agent-os.md 中的 TCPR 身份协议，编译器需识别 tcp_role 字段
---

# Agent Prompt 编译器：把 agent-os.md + 域卡编译为可注入的 system prompt

## 背景

当前 `agents/agent-os.md` 假设 Agent 启动时可以通过 `Read` 文件加载 OS 层。这在 Claude Code 里可行，但 Kimi / Hermes 等 Agent 没有原生文件读取能力，只能依赖启动时注入的 system prompt。

黄药师提出三个解法：
1. System prompt 注入（现在做）
2. `kdo query` 动态查询（补充）
3. MCP server（将来做）

王语嫣独立判断：**采用解法1，但必须补一个编译器和版本控制机制**，否则 prompt 会随着 KDO 卡片更新而腐烂。

## 目标

做一个 `kdo agent-build-prompt` 编译器（或 skill），自动把以下三层内容编译成一段可注入的 system prompt：

- **元层**：`agents/agent-os.md` + `system-yitang-Y-model-os.md`
- **域层**：每个 agent-spec 卡声明的核心 framework / tool / case / dk 卡
- **用户层**：用户个人 OS / 偏好 / 上下文（预留接口）

编译后的 prompt 写入 `.agent/prompts/<agent-id>.md`，Agent 启动时直接加载该文件，无需在运行时读卡。

## 交付物

### 1. 编译器实现

- [ ] 新增 CLI 命令或 skill：`kdo agent-build-prompt <agent-id>`
  - 读取 agent-spec 卡 frontmatter 中的 `os_sources`、`domain_sources`、`user_sources`
  - 按顺序拼接 OS 层、域层、用户层
  - 生成 `.agent/prompts/<agent-id>.md`
  - 在文件头部写入 metadata：`source_hash`、`updated_at`、`estimated_tokens`

- [ ] 支持两种输出模式：
  - `full`：嵌入完整卡片正文（适合核心卡）
  - `claims`：只嵌入 Claims 列表（适合内容较长的卡片，未来扩展）

- [ ] 编译失败时给出明确错误：缺少 source、source 不存在、frontmatter 字段缺失等。

### 2. 设计规范更新

- [ ] 更新 `30_wiki/systems/agent-native-card-design.md`
  - 新增「Agent Prompt 三层编译」章节
  - 所有 `agent-spec` 类型卡片必须声明：
    - `os_sources`: [agent-os.md, system-yitang-Y-model-os.md, ...]
    - `domain_sources`: [framework-xxx, tool-yyy, ...]
    - `user_sources`: [可选，个人 OS 路径]
  - System Prompt 不再手写，而是引用 `.agent/prompts/<agent-id>.md`

### 3. 试点编译

- [ ] 为以下至少 3 个 Agent 生成编译后 prompt：
  - `system-yitang-Y-model-os`（OS 本身，作为基础示例）
  - `tool-agent-spec-yitang-Y-model-coach`（Coach 模式）
  - `tool-agent-spec-yitang-customer-segmentation` 或任意 1 张 OPC 销售 agent-spec

- [ ] 每个编译后 prompt 必须通过 `kdo pre-submit`。

### 4. 使用说明

- [ ] 产出 `40_outputs/agent-prompt-compiler-usage.md` 或写入任务单
  - 如何运行编译器
  - Agent 启动时如何加载 `.agent/prompts/<agent-id>.md`
  - 卡片更新后如何重新编译
  - 与 `kdo query`（解法2）的协作边界

## 验收标准

1. `kdo agent-build-prompt <agent-id>` 可稳定运行，输出文件格式正确。
2. `agent-native-card-design.md` 新增 prompt 编译字段要求，并通过 `kdo pre-submit`。
3. 至少 3 个试点 Agent 的编译后 prompt 文件通过 `kdo pre-submit`。
4. 编译器能检测 source 文件变更：当 source 文件 `updated_at` 晚于 prompt 文件时，给出 stale 警告。
5. 不阻塞 #58：#58 的 agent-spec retrofit 可以先手工写 prompt，本任务完成后通过编译器统一迁移。

## 依赖与阻塞

- `#55` Y模型 OS：提供 `system-yitang-Y-model-os.md` 作为元层核心来源。
- `#58` TCPR 角色层：提供 `agents/agent-os.md` 中的 TCPR 身份协议；编译器需能识别 `tcp_role` / `tcp_default_mode` 等字段并注入到 prompt 中。

## 与现有方案的关系

| 方案 | 定位 | 本任务边界 |
|:---|:---|:---|
| 解法1：System prompt 注入 | **主路径** | 本任务负责把注入流程工程化（编译器 + 版本控制） |
| 解法2：`kdo query` | 补充查询 | 不在本任务实现，但使用说明中定义边界 |
| 解法3：MCP server | 未来方案 | 不入队，放停车场 |

## 用户决策

- **单列执行**：本任务独立成 #59，不与 #55/#58 合并。
- **入队方式**：按顺序追加到队列末尾。
- **终局方案**：MCP server 现在不做，等 Agent 数量 ≥10 再评估。

## 备注

- 编译器不要一次性处理全库所有 agent-spec，先试点 3 个，验证流程后再批量推广。
- 编译后 prompt 的文件路径 `.agent/prompts/<agent-id>.md` 是建议，实际路径可由 `kdo` CLI 配置决定。
- 用户层（personal-os）当前未实现，编译器只需预留接口，不要求真实加载。
