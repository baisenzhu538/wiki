---
id: atk_20260703_yitang-Y-model-os-suite
title: 自攻击报告：Y模型 OS 共享底层 prompt + Coach 模式
type: adversarial
status: pending
language: zh-CN
reviewed_by: pending
related:
- "[[task_20260703_laowantong-agent-spec-yitang-Y-model-coach]]"
- "[[system-yitang-Y-model-os]]"
- "[[tool-agent-spec-yitang-Y-model-coach]]"
- "[[agent-native-card-design]]"
- "[[tool-opc-sales-dialogue-assistant]]"
created_at: 2026-07-03
updated_at: '2026-07-03'
---

# 自攻击报告：Y模型 OS 共享底层 prompt + Coach 模式

## 审查范围

- 任务单：`task_20260703_laowantong-yitang-Y-model-os`
- 目标文件：
  - `30_wiki/systems/system-yitang-Y-model-os.md`
  - `30_wiki/tools/tool-agent-spec-yitang-Y-model-coach.md`
  - `30_wiki/systems/agent-native-card-design.md`（更新）
  - `30_wiki/tools/tool-opc-sales-dialogue-assistant.md`（集成示例更新）
- 真实模型测试：
  - `60_feedback/agent-traces/2026-07-03/tool-opc-sales-dialogue-assistant__智能药柜多轮推进_WITH_OS.md`
  - `60_feedback/agent-traces/2026-07-03/tool-agent-spec-yitang-Y-model-coach__瑜伽馆网站加GEO_v2.md`

## 生产结果

- `system-yitang-Y-model-os.md` 已创建：包含角色声明、协作原则、反幻觉规则、解放思想规则、知行合一规则、个人域加载规则。
- `agent-native-card-design.md` 已增加「Agent Prompt 三层结构」章节，强制所有 agent-spec 卡加载 OS 层。
- `tool-agent-spec-yitang-Y-model-coach.md` 已创建：定位为可选 Coach 模式，非调度器。
- `tool-opc-sales-dialogue-assistant.md` 已更新 System Prompt，展示 OS 层 + 域层 + 用户层加载方式。
- 真实模型测试完成 2 个场景：医药零售 B2B 销售对话、瑜伽馆网站+GEO 跨域结构化。

## 验证结果

- `python 90_control/scripts/kdo_lint.py <target files>`：**PASS**，0 ERROR。
- `python -m kdo pre-submit --files <target files>`：**PASS**，4/4 通过。

## 攻击维度与发现

### 1. 逻辑一致性

- **OS 层与域层边界清晰**：OS 层只回答「怎么思考」，域层回答「思考什么」，未出现 OS 层越俎代庖提供销售/GEO 专业判断的情况。
- **Coach 模式定位正确**：不是独立 Agent，也不是调度器，只是「可选入口」；System Prompt 中明确说明「只使用 OS 层和通用对话，不调用具体域方法论卡」。
- **潜在弱点**：`system-yitang-Y-model-os.md` 中「个人域加载规则」目前只是预留，未给出具体读取格式或 fallback 示例，可能在实现前造成歧义。

### 2. 来源与证据强度

- `system-yitang-Y-model-os.md` 的 `source_refs` 指向了 Y模型底层逻辑域全部 7 张卡 + 原始口述/笔记素材，来源链完整。
- `tool-agent-spec-yitang-Y-model-coach.md` 的 `source_refs` 指向 OS 卡和 Y模型相关卡，符合其派生性质。
- **风险**：OS 层 prompt 的有效性目前仅通过 2 个真实场景验证，样本量有限；不同模型对 OS 层规则的遵循程度可能有差异。

### 3. 真实模型测试

#### OPC 销售对话助手（加载 OS 层后）

- **阶段判断**：购买阶段（与无 OS 层版本一致）。
- **OS 层影响**：
  - 输出中明确出现「判断置信度：中高」并解释理由，符合反幻觉规则。
  - 对「法务兜底」等绝对化表述的警觉提升，建议替换为更保守的合规描述。
  - 风险提醒前置，提到「如果周四面谈后客户仍不推进，需重新定位」。
- **未发现致命问题**。

#### Y模型 Coach 模式（瑜伽馆网站 + GEO）

- **第一轮输出问题**：缺少显式风险提示段落，仅有成功/失败标准。
- **修复**：在 System Prompt 和示例中增加「必须输出失败条件/风险提示」原则；复测后输出包含「重要风险提示」段落，指出 3 个月排第一的高难度、预算聚焦风险、GEO 持久性风险。
- **复测结果**： Coach 模式输出符合要求，结构化清晰，候选域建议合理。

### 4. Schema 与状态合规

- `system-yitang-Y-model-os.md` 类型为 `system`，`tool-agent-spec-yitang-Y-model-coach.md` 类型为 `tool-agent-spec`，符合 schema。
- `agent-native-card-design.md` 类型为 `system`，相关 `related` 字段已更新为 bare id 格式。
- `tool-opc-sales-dialogue-assistant.md` 的 `related` 已补充 `system-yitang-Y-model-os` 和 `tool-agent-spec-yitang-Y-model-coach`。

### 5. 内容完整度

- 4 个目标文件均包含完整的标准 section（When to Use / System Prompt / Critique / Synthesis / Related 等）。
- `tool-agent-spec-yitang-Y-model-coach.md` 包含触发条件、输入门、输出格式、边界、Anti-patterns、Critique、Synthesis。
- `agent-native-card-design.md` 新增章节包含分层图、强制要求、模板示例、责任矩阵。

### 6. 与下游任务的关系

- `#55` 完成后，`#47/#49` OPC 销售智能体军团可默认加载 OS 层。
- 未来新域 Agent 均按「OS 层 + 域层 + 用户层」三层结构设计。
- `tool-yitang-Y-model-application` 中建议的 `tool-agent-spec-yitang-Y-model-coach` 已正式产出。

## 剩余风险与后续动作

1. **个人域格式未定义**：当前 OS 层只写「预留」，建议后续任务明确个人域的读取格式（如 `.agent/personal-os.md` 或 KDO 个人域卡）。
2. **Coach 模式域卡片不全**：示例中 SEO/GEO/网站设计域 Agent 尚不存在，候选建议只能写「待建」；后续域建设完成后需回流更新本卡。
3. **真实模型测试样本有限**：当前 2 个场景覆盖销售 + 跨域；建议后续在更多域（如设计、个人成长）中验证 OS 层的鲁棒性。
4. **lint 工具对 agent-spec 卡的 OS 层检查尚未自动化**：当前依赖人工审查；建议黄药师在 `kdo lint` 中增加规则，检查 `tool-agent-spec` 卡的 System Prompt 是否包含 `{{system-yitang-Y-model-os.md}}`。

## Verdict

- **4 个目标文件**：全部通过 lint 与 pre-submit。
- **0 个致命问题**；已修复 1 个轻微问题（Coach 示例缺少风险提示）。
- **可进入欧阳锋终审**。
