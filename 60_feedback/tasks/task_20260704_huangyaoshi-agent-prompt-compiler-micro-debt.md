---
id: task_20260704_huangyaoshi-agent-prompt-compiler-micro-debt
title: "#59 微债务：Agent Prompt 设计规范补全与 source 字段标准化"
type: task
status: queued
priority: P2
assignee: 黄药师
reviewer: 欧阳锋
reviewed_by: pending
created_at: 2026-07-04
updated_at: 2026-07-04
expected_outputs:
  - "30_wiki/systems/agent-native-card-design.md 新增『Agent Prompt 三层编译』章节"
  - "agent-native-card-design.md 定义 os_sources / domain_sources / user_sources 字段规范"
  - "3 张试点 agent-spec 卡显式声明上述 source 字段（或确认编译器默认值已写入）"
  - "kdo_lint.py 增加/完善对上述 source 字段的校验规则"
  - "kdo pre-submit 全部 PASS，lint 0 新增 ERROR"
dependencies:
  - "#59 reviewed（已满足）"
source_refs:
  - 60_feedback/tasks/task_20260703_huangyaoshi-agent-prompt-compiler.md
  - 60_feedback/tasks/task_20260703_huangyaoshi-agent-prompt-compiler-report.md
  - 30_wiki/systems/agent-native-card-design.md
---

# #59 微债务：Agent Prompt 设计规范补全与 source 字段标准化

## 背景

#59「Agent Prompt 编译器」已 reviewed。编译器能把 `agent-os.md` + 域卡编译为可注入的 system prompt，并产出 3 个试点编译产物。但欧阳锋终审时发现两项不阻塞通过的微债务：

1. `30_wiki/systems/agent-native-card-design.md` 仍缺少「Agent Prompt 三层编译」章节与 `os_sources` / `domain_sources` / `user_sources` 字段规范。
2. 3 张试点 agent-spec 卡未显式声明上述 source 字段，当前靠编译器默认值兜底。

本任务负责把这两个缺口补上，使 Agent Prompt 编译流程从「能跑」变成「有规范可遵循」。

## 目标

让 `agent-native-card-design.md` 成为 Agent Prompt 编译的权威设计规范，并让现有/未来 agent-spec 卡在 frontmatter 中显式声明 prompt 来源。

## 交付物

### 1. 更新 `30_wiki/systems/agent-native-card-design.md`

新增或补全以下章节：

- **Agent Prompt 三层编译**：
  - OS 层：从 `agents/agent-os.md` 或 `system-yitang-Y-model-os.md` 提取的共享 prompt
  - 域层：从 domain framework/tool/concept 卡提取的域特定知识
  - 用户层：从用户配置、历史决策、个人 OS 提取的上下文
- **source 字段规范**：
  - `os_sources`: 字符串或字符串列表，指向 OS 层来源卡 id
  - `domain_sources`: 字符串或字符串列表，指向域层来源卡 id
  - `user_sources`: 字符串或字符串列表，指向用户层来源或占位
  - 每个字段的必填/选填规则、格式（bare id 或带路径 wikilink）、示例

### 2. 更新 3 张试点 agent-spec 卡

检查并补充以下卡的 frontmatter source 字段：

- `30_wiki/tools/tool-agent-spec-yitang-customer-segmentation.md`
- `30_wiki/tools/tool-agent-spec-yitang-value-proposition.md`
- `30_wiki/tools/tool-agent-spec-yitang-sales-process-tracker.md`
- （如有）`tool-agent-spec-yitang-sales-performance-monitor.md`
- （如有）`tool-agent-spec-yitang-opening-3min.md`
- （如有）`tool-agent-spec-yitang-objection-handler.md`
- （如有）`tool-agent-spec-yitang-self-motivation.md`

> 若编译器默认值已在产物中写入，需回写到原始 agent-spec 卡的 frontmatter，确保源头规范。

### 3. 更新 lint 规则

在 `90_control/scripts/kdo_lint.py` 中：

- 对 `type: agent-spec` 或包含 `tcp_role` 字段的卡，检查 `os_sources` / `domain_sources` 是否存在（`user_sources` 可选）。
- 空字符串 `""` 应报 WARNING。
- 字段值应为列表或字符串，格式符合规范。

### 4. 验证

- `python -m kdo pre-submit --files <修改的文件>` 全部 PASS
- `python 90_control/scripts/kdo_lint.py <修改的文件>` 0 新增 ERROR
- 编译器重新运行后，产物 frontmatter 与源卡一致

## 验收标准

1. `agent-native-card-design.md` 包含完整的三层编译章节与 source 字段规范。
2. 所有试点 agent-spec 卡显式声明 source 字段，且值有效。
3. lint 规则能捕获缺失 source 字段或空字符串的情况。
4. pre-submit 全部 PASS，lint 0 新增 ERROR。

## 依赖

- #59 Agent Prompt 编译器 reviewed ✅

## 边界

- 不改变 #59 编译器的核心逻辑。
- 不扩展新的编译器功能。
- 如规范与现有代码有冲突，优先修正规范描述，再视情况修代码。
