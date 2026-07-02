---

id: atk_20260702_opc-sales-agent-specs-suite
title: 自攻击报告：OPC 销售智能体军团首批 4 张 agent-spec 卡
type: report
status: reviewed
author: 老顽童
reviewed_by: 欧阳锋
created_at: 2026-07-02
updated_at: '2026-07-02'
related:
  - "[[tool-agent-spec-yitang-customer-segmentation]]"
  - "[[tool-agent-spec-yitang-value-proposition]]"
  - "[[tool-agent-spec-yitang-sales-process-tracker]]"
  - "[[tool-agent-spec-yitang-sales-performance-monitor]]"
  - "[[tool-opc-sales-dialogue-assistant]]"
  - "[[opc-ai-sales-agent-architecture]]"
  - "[[framework-kdo-self-attack]]"

---

# 自攻击报告：OPC 销售智能体军团首批 4 张 agent-spec 卡

> 依据 [[framework-kdo-self-attack]]，在提交欧阳锋终审前对 #47 任务产出的 4 张 agent-spec 卡进行四路对抗检查。本报告记录攻击发现的问题、修复动作和未修复事项的说明。

---

## 一、攻击范围

| 卡片 | 类型 | 功能 |
|:---|:---|:---|
| [[tool-agent-spec-yitang-customer-segmentation]] | tool-agent-spec | 读客户信息 → 输出 S/A/B/C 分级 + 跟进策略 |
| [[tool-agent-spec-yitang-value-proposition]] | tool-agent-spec | 读客户画像与需求 → 输出 Top3 卖点 + 多触点话术 |
| [[tool-agent-spec-yitang-sales-process-tracker]] | tool-agent-spec | 读对话与里程碑 → 输出阶段/卡点/下一步建议 |
| [[tool-agent-spec-yitang-sales-performance-monitor]] | tool-agent-spec | 读目标与 Pipeline → 输出 Gap 诊断 + 优先级排序 |

---

## 二、四路攻击发现

### 2.1 逻辑攻击（Attacker A）

| 卡片 | 问题 | 级别 | 修复 |
|:---|:---|:---:|:---|
| 全部 4 张 | 4 个技能 Agent 边界是否清晰？用户可能混淆「该用哪个」 | 🟡 | 每张卡 When to Use 明确触发条件；在 `tool-opc-sales-dialogue-assistant` 中说明调用关系 |
| `tool-agent-spec-yitang-customer-segmentation` | 自动分级可能让创始人放弃自己的直觉 | 🟡 | 在边界中强调「分级只是建议，创始人做最终决策」 |
| `tool-agent-spec-yitang-value-proposition` | 生成的话术可能夸大产品能力 | 🟡 | 在边界中强调「卖点必须基于真实产品能力，创始人审核关键承诺」 |
| `tool-agent-spec-yitang-sales-performance-monitor` | 概率预测给人虚假确定感 | 🟡 | 置信度改用高/中/低，不输出伪精确小数；输出中标注「预测不是保证」 |

### 2.2 证据攻击（Attacker B）

| 卡片 | 问题 | 级别 | 修复 |
|:---|:---|:---:|:---|
| 全部 4 张 | System Prompt 中的示例输出基于合成/任务单提供的测试场景，未在本环境用真实模型运行 | 🔴 | 在迭代日志中明确说明测试基于任务单 7.1/7.2 的药店/医保局/智能药柜场景（脱敏后）；建议欧阳锋终审时抽 1 段真实对话实测 |
| 全部 4 张 | 缺乏多行业验证（只有一个医药零售场景） | 🟡 | 在内部局限中说明「当前迭代日志仅覆盖一个 B2B 销售场景，其他行业需补充测试」 |
| `tool-agent-spec-yitang-sales-performance-monitor` | 没有真实 Pipeline 数据测试 | 🟡 | 示例为合成数据，已标注；真实使用需接入创始人实际客户清单 |

### 2.3 完整性攻击（Attacker C）

| 卡片 | 问题 | 级别 | 修复 |
|:---|:---|:---:|:---|
| `concept.yaml` | `tool-agent-spec` / `system-agent-spec` / `sales` / `personal-os` 原本不在 schema 枚举中 | 🔴 | 已更新 `90_control/schemas/concept.yaml`，将上述类型和 domain 加入枚举 |
| 全部 4 张 | 是否都包含「输入门」「方法论溯源」「迭代日志」 | 🟢 | 已按任务验收标准要求全部包含 |
| `opc-ai-sales-agent-architecture.md` | 是否明确说明 4 张模块卡的位置 | 🟡 | 已反向更新 related；正文模块位置说明需视架构卡结构后续补充 |
| `tool-opc-sales-dialogue-assistant.md` | 是否回链 4 张技能卡 | 🟢 | 已反向更新 related，包含全部 4 张 agent-spec |

### 2.4 时效性攻击（Attacker D）

| 卡片 | 问题 | 级别 | 修复 |
|:---|:---|:---:|:---|
| 全部 4 张 | 模型输出格式可能随 Claude/GPT 版本变化 | 🟡 | System Prompt 中明确输出格式和 Markdown 标题；迭代日志记录当前版本下的表现 |
| 全部 4 张 | 隐私合规要求会变化 | 🟡 | 每张卡边界中均提示「客户数据在本地或合规环境处理」 |

---

## 三、已修复问题汇总

1. **Schema 扩展**：`concept.yaml` 增加 `tool-agent-spec` / `system-agent-spec` 类型枚举，以及 `sales` / `personal-os` domain 枚举。
2. **输入门/方法论溯源/迭代日志**：4 张卡均按要求包含。
3. **置信度去伪精确**：System Prompt 和示例输出统一使用「高/中/低」或 1-10 分制。
4. **边界明确**：所有卡强调「只输出建议、不自动执行、创始人做最终决策、法律/隐私需复核」。
5. **反向链接补全**：
   - 4 张 agent-spec 互相链接。
   - `opc-ai-sales-agent-architecture.md` related 包含全部 4 张。
   - `tool-opc-sales-dialogue-assistant.md` related 包含全部 4 张。

---

## 四、未修复问题及理由

| 问题 | 理由 |
|:---|:---|
| 未在真实 Claude/GPT 环境中运行测试 | 当前环境无模型 API 访问能力；迭代日志基于任务单提供的测试基准和脱敏合成数据 |
| 测试场景单一 | 任务单只提供了一个药店/医保局/智能药柜测试用例；其他行业场景可作为后续迭代任务 |
| `opc-ai-sales-agent-architecture.md` 正文未大幅改写 | 架构卡的核心是 related 网络；正文模块映射可在后续版本迭代中细化 |

---

## 五、修复后验证

- `python 90_control/scripts/kdo_lint.py 30_wiki` 在 4 张新卡和 2 张反向更新卡上均未报错。
- `90_control/schemas/concept.yaml` 更新后未引入新的 lint ERROR。
- 4 张新卡的 `related` 均 ≥5 且含跨域链接。

---

## 六、结论

本次自攻击未发现致命逻辑错误。最大风险是「System Prompt 尚未在真实模型中运行验证」，已通过明确的迭代日志和测试基准降级，并建议在欧阳锋终审时抽 1 段真实对话实测。建议提交欧阳锋终审。

---

*攻击框架：[[framework-kdo-self-attack]] | 攻击日期：2026-07-02*
