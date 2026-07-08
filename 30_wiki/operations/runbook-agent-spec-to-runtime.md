---
id: runbook-agent-spec-to-runtime
title: Agent Spec → 可运行 Agent 部署路径 Runbook
type: doc
status: pending_review
author: 老顽童
reviewer: 欧阳锋
reviewed_by: 欧阳锋
domain:
  - yitang
  - operations
  - ai-collaboration
source_refs:
  - 70_product/tasks/task_20260708_wangyuyan-dual-triangle-cross-domain-agent.md
  - .agent/prompts/agent-spec-yitang-dual-triangle-cross-domain-diagnostician.md
related:
  - "[[agent-spec-yitang-dual-triangle-cross-domain-diagnostician]]"
  - "[[opc-ai-sales-agent-architecture]]"
created_at: 2026-07-08
updated_at: 2026-07-08
---

# Agent Spec → 可运行 Agent 部署路径 Runbook

## 目的

把 `.agent/prompts/` 下的 Agent Spec 文件（如 `agent-spec-yitang-dual-triangle-cross-domain-diagnostician.md`）跑起来，形成一次可调试、可验证、可复用的 Agent 运行时对话。本 Runbook 是 #143 任务的部署路径试点，目标是为后续 #139-#142 域 Agent 建立可复制模板。

---

## When to Use

- 刚完成一张 `agent-spec` 卡，需要验证 System Prompt 是否生效。
- 需要把 `.agent/prompts/` 的 Agent Spec 加载到 Kimi Code CLI / Hermes CLI 进行对话测试。
- 需要检查 Agent 是否按默认 C 身份启动、是否能正确切换 T/P/R、输出模板是否完整。
- 需要排查「Agent 不声明身份」「不调用域卡」「输出格式错乱」等常见故障。

---

## 环境准备（Kimi Code CLI / Hermes CLI）

### 1. 工作目录

所有操作默认在仓库根目录执行：

```bash
cd /c/Users/Administrator/Desktop/wiki
```

### 2. 前置检查

```bash
# 确认 KDO CLI 可用
python -m kdo --version

# 确认目标 Agent Spec 存在
ls .agent/prompts/agent-spec-yitang-dual-triangle-cross-domain-diagnostician.md

# 确认 OS 与域卡存在
ls 30_wiki/systems/system-yitang-Y-model-os.md
ls agents/agent-os.md
ls 30_wiki/concepts/concept-yihang-dual-triangle-core.md
ls 30_wiki/frameworks/framework-yitang-y-model-dual-triangle-synergy.md
ls 30_wiki/tools/tool-yihang-dual-triangle-canvas.md
```

### 3. 可选：生成 Vault 状态快照

```bash
python 90_control/scripts/vault-snapshot.py
```

运行后会生成 `90_control/vault-status.md`，可在调试前快速了解最近变更和质量提示。

---

## 读取文件清单（startup.md + role context + agent-spec + 相关卡）

启动一次调试对话前，按顺序读取以下文件：

| # | 文件 | 作用 |
|:---:|:---|:---|
| 1 | `.agent/startup.md` | 了解工厂全局、当前阻塞、铁律 |
| 2 | `.agent/<角色>-context.md` | 当前 Agent 实例的角色上下文（如 `laowantong-context.md`） |
| 3 | `.agent/prompts/agent-spec-yitang-dual-triangle-cross-domain-diagnostician.md` | 目标 Agent Spec |
| 4 | `30_wiki/systems/system-yitang-Y-model-os.md` | Y模型共享思考底座（OS 层） |
| 5 | `agents/agent-os.md` | TCPR 身份协议与启动规范 |
| 6 | `30_wiki/concepts/concept-yihang-dual-triangle-core.md` | 双三角六要素官方定义 |
| 7 | `30_wiki/frameworks/framework-yitang-y-model-dual-triangle-synergy.md` | Y模型 × 双三角协同框架 |
| 8 | `30_wiki/tools/tool-yihang-dual-triangle-canvas.md` | 双三角画布工具 |
| 9 | `30_wiki/tools/tool-yitang-dual-triangle-scenario-router.md` | 场景路由表（占位，随 #143 填充） |
| 10 | `30_wiki/tools/tool-yitang-dual-triangle-agent-handoff-protocol.md` | 子域 Agent 转交协议（占位，随 #143 填充） |
| 11 | `30_wiki/tools/tool-yitang-dual-triangle-domain-registry.md` | 域注册与扩展协议（占位，随 #143 填充） |
| 12 | `30_wiki/personal-os/opc-ai-sales-agent-architecture.md` | 参考已有域 Agent 军团架构 |

> 注：当前 #143 的子任务 2-4 尚未完成，因此路由表、转交协议、域注册协议为占位文件。调试时若涉及这些文件，先确认其内容是否已更新。

---

## 启动命令

### Kimi Code CLI（推荐本任务使用）

Kimi Code CLI 没有内嵌 Agent 调度器，需要手动把 Agent Spec 的 System Prompt 注入对话上下文。推荐两种做法：

#### 方式 A：直接复制 System Prompt

1. 打开 `.agent/prompts/agent-spec-yitang-dual-triangle-cross-domain-diagnostician.md`。
2. 复制 `## System Prompt（完整，可复用）` 代码块中的内容。
3. 把 `{{system-yitang-Y-model-os.md}}` 和 `{{agents/agent-os.md}}` 占位符替换为对应文件正文。
4. 将替换后的完整文本作为 system prompt 粘贴到新的 Kimi Code CLI 会话顶部。
5. 发送测试输入：

```text
我想做一款 AI 工具帮律师审合同，但不确定该从哪切入。
```

#### 方式 B：使用 KDO `prompt` 命令辅助加载

```bash
# 列出可用 prompts
python -m kdo prompt --list

# 如果未来 Agent Spec 被注册到 capabilities/prompts/，可直接加载
python -m kdo prompt <agent-id> --body-only
```

当前该命令主要用于 `capabilities/prompts/` 下的模板，Agent Spec 仍需手动加载。

### Hermes CLI

Hermes CLI 支持通过 `CLAUDE.md` 或系统 prompt 文件启动 Agent：

1. 将替换占位符后的 System Prompt 写入 `hermes/prompts/agent-spec-yitang-dual-triangle-cross-domain-diagnostician.md`。
2. 在 Hermes 配置中指定该文件为当前会话的 system prompt。
3. 启动会话后，确认 Agent 第一句话包含 TCPR 身份声明。

> 当前 Hermes 实例负载较高（#140 进行中），本任务建议由 Kimi Code CLI 实例执行。

---

## 调试步骤

### Step 1：验证身份声明

发送任意测试输入后，检查 Agent 第一句话是否为：

```text
我本次以 **C（Consult/咨询）** 身份与你协作：帮你用一行双三角六要素做元诊断……
```

若不是，检查 System Prompt 中 `## TCPR 身份声明` 是否被截断或覆盖。

### Step 2：验证边界确认

输入一个明显超出边界的问题，例如：

```text
帮我判断这份合同有没有法律风险。
```

Agent 必须声明：不做法律最终判断，并建议人工复核。

### Step 3：验证六要素扫描

输入一个典型跨域问题：

```text
我想做一款 AI 工具帮律师审合同，靠谱吗？
```

Agent 应输出包含六要素扫描表的诊断报告，并指出 1-2 个最短板。

### Step 4：验证子域匹配

在 Step 3 之后，检查 Agent 是否推荐了合适的子域 Agent 或框架卡，例如 `agent-spec-demand-iceberg-coach` 或 `agent-spec-dual-triangle-canvas-filler`。

### Step 5：验证身份切换

输入：

```text
切换到教学模式，给我讲讲双三角的六要素。
```

Agent 应声明切换到 T 身份，并解释六要素含义。

### Step 6：验证轻量任务降级

输入：

```text
帮我写一封邮件。
```

Agent 应判断为一次性简单任务，推荐通用 Agent，不强行走六要素扫描。

---

## 验证 System Prompt 生效的方法

| 验证项 | 通过标准 |
|:---|:---|
| 身份声明 | 开场第一句话包含默认 C 身份与目标 |
| 边界声明 | 对法律/医疗/合规问题声明不替代专业人士 |
| 六要素扫描 | 输出包含「强/弱/无/未知」状态表 |
| 短板识别 | 明确指出 1-2 个最短板并给出理由 |
| 子域匹配 | 推荐 1-3 个入口 Agent/框架卡 |
| 输出模板 | 使用 Agent Spec 中定义的 Markdown 模板结构 |
| 身份切换 | 用户说「切换到教学模式」后，Agent 明确声明新身份 |
| 飞轮四问 | 会话结束前询问 before/after/why better/next try |

每次调试后，把观察结果记录到 `20_memory/` 或当前任务文件的 `## 迭代日志` 中。

---

## 常见故障

| 故障现象 | 可能原因 | 修复方法 |
|:---|:---|:---|
| Agent 不声明身份 | System Prompt 中 TCPR 身份声明被截断；或会话上下文被重置 | 重新注入完整 System Prompt；检查上下文长度 |
| 输出没有六要素扫描表 | System Prompt 中输出模板未被遵循；或用户输入过短 | 在 System Prompt 中强化「每次诊断必须输出模板」的纪律 |
| 推荐子域 Agent 为空或不相关 | 域注册表未加载；或相关占位文件未更新 | 检查 `tool-yitang-dual-triangle-scenario-router.md` 是否已填充 |
| Agent 直接跳到解决方案 | 默认 C 身份失效；或用户输入被模型误判为 P 模式 | 在 System Prompt 顶部重申默认身份和「先诊断再给方案」的纪律 |
| 跨域迁移缺少关键差异 | System Prompt 中跨域迁移规则被忽略 | 在输出模板中强制加入「关键差异」小节 |
| 输出包含未经验证的数字 | 反幻觉规则未生效 | 检查 OS 层是否已加载 `system-yitang-Y-model-os.md` |
| 占位符未替换导致提示词泄漏 | 部署时未替换 `{{...}}` | 使用编译脚本或手动替换后再注入 |

---

## Critique

### 外部攻击

1. **部署工程派**：「手动复制 System Prompt 太低效，应该有一个自动编译和注入脚本。」
   - **回应**：同意。本 Runbook 当前是手动路径试点。下一步应基于 `kdo-tools/agent-prompt-compiler.py` 把 Agent Spec 自动编译为 `.agent/prompts/<agent-id>.md`，并提供 `kdo run-agent <agent-id>` 命令一键启动。

2. **Hermes 运维派**：「不同 CLI 的 System Prompt 注入方式不同，一份 Runbook 无法覆盖所有环境。」
   - **回应**：本 Runbook 先覆盖 Kimi Code CLI 和 Hermes CLI 两种主要环境。未来应抽象出「环境适配器」，把读取文件清单、替换占位符、注入 system prompt 封装成统一 CLI 命令。

3. **安全审计派**：「把 OS 层和域卡全文复制进 System Prompt 会增加提示词注入风险，且上下文很长。」
   - **回应**：当前试点阶段使用完整加载，便于调试。未来应支持分层加载与 hash 校验，只加载必要片段，并验证卡片未被篡改。

### 内部局限

1. **依赖占位文件**：`tool-yitang-dual-triangle-scenario-router` 等三张工具卡当前为占位文件，完整调试需等待 #143 子任务 2-4 完成。
2. **未自动化**：当前路径仍需要人工替换占位符、复制粘贴，尚未形成「一键运行」的体验。
3. **验证依赖人工判读**：System Prompt 生效的 8 项验证标准目前靠人工检查，未来应转化为可自动评分的 eval cases。
4. **跨 CLI 差异未完全消除**：Hermes CLI 的具体配置路径可能与 Kimi Code CLI 不同，需在实际运行时补充截图或命令示例。

---

## Synthesis

- 本 Runbook 是 `task_20260708_wangyuyan-dual-triangle-cross-domain-agent.md` 中「Agent Spec 部署路径试点」的落地文档。
- 核心消费链路：`.agent/startup.md` → 角色 context → `[[agent-spec-yitang-dual-triangle-cross-domain-diagnostician]]` → OS 层 → 域层 → 用户层。
- 参考架构：`[[opc-ai-sales-agent-architecture]]` 展示了已有域 Agent 军团的分层设计，可作为后续子域 Agent 部署的参照。
- 下一步自动化方向：把本 Runbook 中的手动步骤沉淀为 `kdo run-agent <agent-id>` CLI 命令，并配套自动 eval cases。
