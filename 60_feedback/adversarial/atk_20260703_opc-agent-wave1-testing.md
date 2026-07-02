---

id: atk_20260703_opc-agent-wave1-testing
title: 自攻击报告：OPC 销售智能体 Wave 1 真实模型测试
type: report
status: reviewed
author: 老顽童
reviewed_by: 欧阳锋
created_at: 2026-07-03
updated_at: '2026-07-03'
related:
  - "[[case-opc-agent-wave1-real-model-testing]]"
  - "[[tool-agent-spec-yitang-customer-segmentation]]"
  - "[[tool-agent-spec-yitang-value-proposition]]"
  - "[[tool-agent-spec-yitang-sales-process-tracker]]"
  - "[[tool-agent-spec-yitang-sales-performance-monitor]]"
  - "[[tool-agent-spec-yitang-opening-3min]]"
  - "[[tool-agent-spec-yitang-objection-handler]]"
  - "[[tool-agent-spec-yitang-self-motivation]]"
  - "[[framework-kdo-self-attack]]"

---

# 自攻击报告：OPC 销售智能体 Wave 1 真实模型测试

> 依据 [[framework-kdo-self-attack]]，在提交欧阳锋终审前对 #50 任务产出进行四路对抗检查。

---

## 一、攻击范围

- 7 张 agent-spec 卡在 deepseek-v4-pro 真实模型中的 14 个场景测试。
- 测试结果、trace 文件、迭代日志更新、prompt v1.1 修复与复测。
- 回流产物：KDO 回流清单、case 归档卡。

---

## 二、四路攻击发现

### 2.1 逻辑攻击

| 问题 | 级别 | 修复 |
|:---|:---:|:---|
| 用 deepseek-v4-pro 代替 Claude/GPT 是否影响结论 | 🟡 | 已在报告和 case 卡中说明：长度问题是通用问题，后续需在 Claude/GPT 补测 |
| 14 个场景是否足以验证 7 个 Agent | 🟡 | 已在 case 卡中说明 Wave 1 目标是暴露边界，非统计验证 |
| 人工评判由老顽童完成，可能有确认偏误 | 🟡 | 已在 case 卡内部局限中说明，建议欧阳锋抽检 2-3 个 trace |

### 2.2 证据攻击

| 问题 | 级别 | 修复 |
|:---|:---:|:---|
| 测试输入为合成数据，非真实客户对话 | 🟡 | 已在 case 卡中说明输入基于 #44 课程案例脱敏改编，真实客户测试需创始人提供 |
| 未发现 P0 有害/违法输出 | 🟢 | 7 张卡均通过边界检查，无越界 |
| P1 截断问题是否真正修复 | 🟢 | customer-segmentation 和 performance-monitor 已 v1.1 复测，输出完整 |

### 2.3 完整性攻击

| 问题 | 级别 | 修复 |
|:---|:---:|:---|
| 7 张卡迭代日志是否都更新 | 🟢 | 已统一追加 Wave 1 测试轮次 |
| KDO 回流清单是否产出 | 🟢 | 已在任务单第七节追加 |
| 是否至少新建/更新 1 个 case 卡 | 🟢 | 已新建 [[case-opc-agent-wave1-real-model-testing]] |
| 是否保存 traces 到指定目录 | 🟢 | 已保存到 `60_feedback/agent-traces/2026-07-02/` |

### 2.4 时效性攻击

| 问题 | 级别 | 修复 |
|:---|:---:|:---|
| 模型能力迭代后 prompt 可能失效 | 🟡 | 已在 case 卡局限中说明，建议每季度回归测试 |
| API 端点或密钥可能变化 | 🟡 | harness 脚本从环境变量读取，不硬编码；已在脚本中说明 |

---

## 三、已修复问题汇总

1. **P1 截断**：customer-segmentation、performance-monitor 增加输出长度控制，v1.1 复测通过。
2. **P2 默认值**：sales-process-tracker 增加默认四阶段框架。
3. **P2 输出格式**：opening-3min 模式 A 限制为三部分；value-proposition PPT 版限制 3 行。
4. **P2 边界**：objection-handler 增加竞品报价转交创始人；self-motivation 进度预测去百分比。
5. **回流**：任务单 KDO 回流清单、case 卡、7 张 agent-spec 迭代日志均完成。

---

## 四、未修复问题及理由

| 问题 | 理由 |
|:---|:---|
| 未在 Claude/GPT 上实测 | 当前环境仅有 deepseek-v4-pro 可用 |
| 测试输入为合成脱敏数据 | 真实客户对话需创始人授权和提供 |
| 未做双盲人工评分 | 资源限制；建议欧阳锋抽检 |
| 未覆盖传统工业分销等更多行业 | Wave 1 聚焦边界问题，后续 Wave 扩展 |

---

## 五、验证

- `kdo lint`：7 张 agent-spec 卡、case 卡、opc 架构卡、对话助手卡目标范围内无 ERROR。
- 14 个首轮 trace + 2 个 v1.1 复测 trace 均保存完整。
- 复测证明 P1 截断问题已修复。

---

## 六、结论

未发现致命逻辑错误或证据造假。P1 截断问题已修复并复测通过。建议在欧阳锋终审时抽检 customer-segmentation、performance-monitor 两个 v1.1 trace 确认效果。建议提交终审。

---

*攻击框架：[[framework-kdo-self-attack]] | 日期：2026-07-03*
