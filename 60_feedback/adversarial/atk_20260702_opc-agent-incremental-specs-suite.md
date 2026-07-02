---

id: atk_20260702_opc-agent-incremental-specs-suite
title: 自攻击报告：OPC 销售智能体增量 3 张 agent-spec 卡
type: report
status: draft
author: 老顽童
reviewed_by: 欧阳锋
created_at: 2026-07-02
updated_at: '2026-07-02'
related:
  - "[[tool-agent-spec-yitang-opening-3min]]"
  - "[[tool-agent-spec-yitang-objection-handler]]"
  - "[[tool-agent-spec-yitang-self-motivation]]"
  - "[[tool-opc-sales-dialogue-assistant]]"
  - "[[opc-ai-sales-agent-architecture]]"
  - "[[framework-kdo-self-attack]]"

---

# 自攻击报告：OPC 销售智能体增量 3 张 agent-spec 卡

> 依据 [[framework-kdo-self-attack]]，在提交欧阳锋终审前对 #49 任务产出的 3 张 agent-spec 卡进行四路对抗检查。

---

## 一、攻击范围

| 卡片 | 功能 |
|:---|:---|
| [[tool-agent-spec-yitang-opening-3min]] | 首次接触客户时生成 30 秒自我介绍 + 价值钩子 + 开放问题 |
| [[tool-agent-spec-yitang-objection-handler]] | 客户提出价格/时机/权限/信任等异议时输出应对策略 |
| [[tool-agent-spec-yitang-self-motivation]] | 一人公司创始人自我驱动，把六维激励改编为个人行动系统 |

---

## 二、四路攻击发现

### 2.1 逻辑攻击

| 卡片 | 问题 | 级别 | 修复 |
|:---|:---|:---:|:---|
| `opening-3min` | 开场脚本可能让创始人听起来像推销员 | 🟡 | System Prompt 中强调「价值钩子」不卖产品，第一个问题争取提问权 |
| `objection-handler` | 异议分类可能把真实抗拒误判为借口 | 🟡 | 输出中要求区分「真实顾虑」与「表面借口」，并给出验证问题 |
| `self-motivation` | 把团队激励模型改编为个人系统，可能制造自我压力 | 🟡 | 明确边界「不制造虚假紧迫感」，区分「忙」和「有效推进」 |

### 2.2 证据攻击

| 问题 | 级别 | 修复 |
|:---|:---:|:---|
| System Prompt 示例输出基于合成/任务单测试场景，未在真实模型中运行 | 🔴 | 迭代日志说明基于脱敏合成数据；建议终审时抽 1 段真实对话实测 |
| 测试场景单一（主要为 B2B 销售） | 🟡 | 在内部局限中说明其他场景需补充测试 |

### 2.3 完整性攻击

| 问题 | 级别 | 修复 |
|:---|:---:|:---|
| 3 张卡是否都包含输入门/方法论溯源/迭代日志 | 🟢 | 已按要求全部包含 |
| `opc-ai-sales-agent-architecture.md` 正文是否补充 7 张 agent-spec 调用关系 | 🟢 | 已新增「四、已落地的 7 张 agent-spec 卡」章节 |
| `tool-opc-sales-dialogue-assistant` 是否回链 3 张新卡 | 🟢 | related 已更新 |

### 2.4 时效性攻击

| 问题 | 级别 | 修复 |
|:---|:---:|:---|
| 模型输出格式可能随版本变化 | 🟡 | System Prompt 中明确 Markdown 标题结构 |
| 隐私合规要求变化 | 🟡 | 每张卡边界中提示本地/合规处理 |

---

## 三、已修复问题

1. 3 张卡均包含输入门、方法论溯源、迭代日志、System Prompt 示例。
2. `opc-ai-sales-agent-architecture.md` 正文新增 7 张 agent-spec 调用关系图和场景表。
3. 3 张新卡互相链接，并与 #47 的 4 张 agent-spec 链接。
4. `opc-ai-sales-agent-architecture.md` 和 `tool-opc-sales-dialogue-assistant.md` related 已加入 3 张新卡回链。
5. 置信度统一使用「高/中/低」，避免伪精确小数。

---

## 四、未修复问题及理由

| 问题 | 理由 |
|:---|:---|
| 未在真实 Claude/GPT 环境中实测 | 当前环境无模型 API；迭代日志基于任务单测试基准和合成数据 |
| 测试场景以 B2B 为主 | 任务单提供的测试用例为药店/医保局/智能药柜场景 |

---

## 五、验证

- `kdo lint`：3 张新卡、`opc-ai-sales-agent-architecture.md`、`tool-opc-sales-dialogue-assistant.md` 目标范围内无 ERROR。
- 3 张新卡 `related` ≥5 且含跨域链接。

---

## 六、结论

未发现致命逻辑错误。主要风险是「System Prompt 尚未在真实模型中实测」，已通过迭代日志和测试基准降级。建议提交欧阳锋终审。

---

*攻击框架：[[framework-kdo-self-attack]] | 日期：2026-07-02*
