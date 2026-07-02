---
id: task_20260702_laowantong-opc-sales-agent-testing-wave1
title: "OPC 销售智能体实测 Wave 1：7 张 agent-spec 真实模型验证"
type: task
status: in_progress
priority: P1
assignee: 老顽童(Kimi)
reviewer: 欧阳锋
started_at: 2026-07-02
created_at: 2026-07-02
updated_at: 2026-07-02
expected_outputs:
  - "7 张 agent-spec 卡在 Claude/GPT 真实环境的测试记录"
  - "每个 agent-spec 至少 2 个真实场景的迭代日志更新"
  - "失败/成功案例归档"
  - "触发的 KDO 回流清单"
dependencies:
  - "[[task_20260702_laowantong-opc-sales-agent-specs-production]]"
  - "[[task_20260702_laowantong-opc-sales-agent-incremental-specs]]"
source_refs:
  - "[[tool-agent-spec-yitang-customer-segmentation]]"
  - "[[tool-agent-spec-yitang-value-proposition]]"
  - "[[tool-agent-spec-yitang-sales-process-tracker]]"
  - "[[tool-agent-spec-yitang-sales-performance-monitor]]"
  - "[[tool-agent-spec-yitang-opening-3min]]"
  - "[[tool-agent-spec-yitang-objection-handler]]"
  - "[[tool-agent-spec-yitang-self-motivation]]"
  - "[[tool-opc-sales-dialogue-assistant]]"
  - "[[opc-ai-sales-agent-architecture]]"
related:
  - tool-agent-spec-yitang-customer-segmentation
  - tool-agent-spec-yitang-value-proposition
  - tool-agent-spec-yitang-sales-process-tracker
  - tool-agent-spec-yitang-sales-performance-monitor
  - tool-agent-spec-yitang-opening-3min
  - tool-agent-spec-yitang-objection-handler
  - tool-agent-spec-yitang-self-motivation
  - tool-opc-sales-dialogue-assistant
  - opc-ai-sales-agent-architecture
  - agent-native-card-design
---

# OPC 销售智能体实测 Wave 1：7 张 agent-spec 真实模型验证

> 任务来源：欧阳锋在 `#47` / `#49` 终审中指出的首要可改进点——「System Prompt 尚未在 Claude/GPT 真实环境运行」。
> 目标：把 #47 + #49 共 7 张 agent-spec 的 System Prompt 放到真实模型里跑一遍，用真实销售对话验证可用性，并触发 KDO 回流。
> 原则：测试不是为了证明 Agent 完美，而是为了发现边界问题和回流素材。

---

## 一、7 张待测 agent-spec

| 编号 | 卡片 | 来源任务 | 核心功能 |
|---:|:---|:---|:---|
| 1 | `tool-agent-spec-yitang-customer-segmentation` | #47 | 客户 S/A/B/C 自动分级 |
| 2 | `tool-agent-spec-yitang-value-proposition` | #47 | 差异化卖点生成 |
| 3 | `tool-agent-spec-yitang-sales-process-tracker` | #47 | 销售阶段追踪与卡点预警 |
| 4 | `tool-agent-spec-yitang-sales-performance-monitor` | #47 | 业绩 Gap 与周会建议 |
| 5 | `tool-agent-spec-yitang-opening-3min` | #49 | 开场 3 分钟话术（双模式） |
| 6 | `tool-agent-spec-yitang-objection-handler` | #49 | 客户异议处理 |
| 7 | `tool-agent-spec-yitang-self-motivation` | #49 | OPC 创始人自我驱动 |

---

## 二、测试场景矩阵

每个 agent-spec 至少覆盖 **2 个场景**，整体覆盖以下 4 个行业域：

| 场景域 | 代表业务 | 测试重点 |
|:---|:---|:---|
| 医药零售 B2B | 智能药柜 / 医保局对接 | 已有场景，验证稳定性 |
| SaaS / 企业服务 | 剧本杀 SaaS / 商标设计 / 销售工具 | 长周期、多决策者 |
| 门店零售 / 美业 | 美容院 / 教培 / 餐饮 | 高情感、快节奏 |
| 传统工业分销 | 涂料 / 建材 / 设备 | 海量线索、低转化率 |

---

## 三、每张卡的实测任务

### 1. `tool-agent-spec-yitang-customer-segmentation`

- **输入**：5-10 条真实脱敏线索（公司/行业/规模/职位/来源/行为）
- **测试目标**：
  - 分级结果是否稳定
  - 同一批线索多次运行是否一致
  - 当缺少关键信息时是否给出降级提示
- **成功标准**：≥70% 分级与人工判断一致
- **输出**：更新迭代日志，记录误判案例

### 2. `tool-agent-spec-yitang-value-proposition`

- **输入**：3-5 个真实客户画像 + 产品/服务简介
- **测试目标**：
  - 卖点是否匹配客户场景
  - 是否避免夸大或无法兑现的承诺
  - 微信/电话/邮件/PPT 四版话术是否可用
- **成功标准**：每个画像产出 ≥3 个差异化卖点，且逻辑自洽
- **输出**：更新迭代日志，补充失败模式

### 3. `tool-agent-spec-yitang-sales-process-tracker`

- **输入**：2-3 段多轮真实销售对话（≥5 轮）
- **测试目标**：
  - 阶段判断是否与人工一致
  - 卡点识别是否准确
  - 下一步建议是否可执行
- **成功标准**：阶段判断准确率 ≥75%
- **输出**：更新迭代日志，记录阶段误判

### 4. `tool-agent-spec-yitang-sales-performance-monitor`

- **输入**：1 个真实 pipeline（≥10 个客户）+ 月度目标
- **测试目标**：
  - Gap 分析是否合理
  - 重点客户推荐是否符合直觉
  - 策略建议是否具体
- **成功标准**：推荐重点客户中 ≥60% 与人工判断一致
- **输出**：更新迭代日志，补充案例

### 5. `tool-agent-spec-yitang-opening-3min`

- **输入**：5 个真实首次接触场景
- **测试目标**：
  - 模式 A（首条消息草稿）是否严格 50-80 字
  - 模式 B（首通电话攻略）是否完整且可执行
  - 用户自然语言问法触发是否正确模式
- **成功标准**：模式 A 输出格式合规率 100%；模式 B 可用率 ≥70%
- **输出**：更新迭代日志，补充模式切换示例

### 6. `tool-agent-spec-yitang-objection-handler`

- **输入**：8-10 个真实客户异议（价格/时机/权限/信任/竞品/需求不明确各 ≥1）
- **测试目标**：
  - 异议类型判断是否准确
  - 回复选项是否可直接使用或微调
  - 是否避免贬低竞品或过度承诺
- **成功标准**：异议类型准确率 ≥75%，回复可用率 ≥70%
- **输出**：更新迭代日志，补充反模式

### 7. `tool-agent-spec-yitang-self-motivation`

- **输入**：2-3 个真实周目标/进度组合
- **测试目标**：
  - 最小可执行动作是否合理
  - 动机提醒是否有效且不制造焦虑
  - 倦怠预警信号是否敏感
- **成功标准**：建议动作可执行率 ≥80%
- **输出**：更新迭代日志，考虑补充「工作节律/能量曲线」输入门

---

## 四、测试方法

1. **使用真实模型**：Claude（推荐）或 GPT-4 以上模型。
2. **System Prompt 直接复制**：不修改 prompt 核心结构，只填入测试输入。
3. **记录完整输入/输出**：保存为 markdown 文件，路径：`60_feedback/agent-traces/2026-07-02/`。
4. **人工评判**：老顽童输出后，用户或欧阳锋做可用性评分。
5. **问题分级**：
   - P0（阻塞）：输出错误、有害、违反边界
   - P1（需修复）：输出可用但不稳定
   - P2（可优化）：输出可用但体验不够好
   - P3（建议）：新的场景或功能需求

---

## 五、KDO 回流机制

根据 `agent-native-card-design.md` 的回流规则，本次测试必须产出：

| 测试发现 | 回流动作 | 目标文件 |
|:---|:---|:---|
| system prompt 表达不清 | 更新 agent-spec 卡 | 对应 agent-spec 文件 |
| 源方法论卡有 gap | 更新源 tool/framework 卡 | `#44` 对应方法论卡 |
| 反复出现的用户错误 / Agent 误用 | 新建/更新 dk 卡 | `dk-ai-collaboration-pitfalls` 或新建 |
| 典型成功/失败场景 | 新建/更新 case 卡 | `60_feedback/cases/` |
| 跨 Agent 通用设计模式 | 新建/更新 framework/concept 卡 | `agent-native-card-design` 等 |

**回流清单格式**：在 `#50` 任务单末尾追加「KDO 回流清单」表格。

---

## 六、验收标准

- [ ] 7 张 agent-spec 卡均完成真实模型测试，每张 ≥2 个场景。
- [ ] 每个 agent-spec 的 `## 迭代日志` 已更新，含测试日期、输入摘要、发现的问题、修正动作。
- [ ] 所有测试输入/输出记录保存到 `60_feedback/agent-traces/2026-07-02/`（或等效路径）。
- [ ] 至少产出 1 份「KDO 回流清单」，列明需要回流的卡片和原因。
- [ ] 至少产出 1 个新的 `case` 卡或更新 1 个现有 `case` 卡。
- [x] 若发现 P0/P1 问题，对应 agent-spec 卡必须修复后重新测试。
- [ ] 欧阳锋终审通过。

---

## 七、KDO 回流清单

| 发现 | 回流动作 | 目标文件 | 状态 |
|:---|:---|:---|:---:|
| customer-segmentation 5 线索场景输出截断 | 在 System Prompt 中增加长度控制：≥5 线索时先输出分级总表 + Top 3 详细分析 | `30_wiki/tools/tool-agent-spec-yitang-customer-segmentation.md` | 已完成 |
| performance-monitor 10 客户 Pipeline 输出截断 | 增加 Pipeline 客户数 ≥8 时仅展开 Top 5，其余合并为长尾策略 | `30_wiki/tools/tool-agent-spec-yitang-sales-performance-monitor.md` | 已完成 |
| performance-monitor 使用具体百分比 | 完成率/概率统一改用高/中/低三档定性描述 | `30_wiki/tools/tool-agent-spec-yitang-sales-performance-monitor.md` | 已完成 |
| sales-process-tracker 缺里程碑时降级为粗略草案 | 默认使用「接触→购买→付款→履约」四阶段框架，仍给高/中/低置信度 | `30_wiki/tools/tool-agent-spec-yitang-sales-process-tracker.md` | 已完成 |
| opening-3min 模式 A 输出篇幅偏大 | 明确模式 A 仅输出自我介绍脚本 + 价值钩子 + 开放问题 | `30_wiki/tools/tool-agent-spec-yitang-opening-3min.md` | 已完成 |
| value-proposition PPT/海报版文字堆叠 | 增加「每版 3 行以内，每行一个视觉记忆点」限制 | `30_wiki/tools/tool-agent-spec-yitang-value-proposition.md` | 已完成 |
| objection-handler 竞品报价处理不足 | 增加「客户透露竞品报价时立即转交创始人」边界 | `30_wiki/tools/tool-agent-spec-yitang-objection-handler.md` | 已完成 |
| self-motivation 进度预测用百分比 | 完成率预测改用高/中/低或乐观/中性/悲观描述 | `30_wiki/tools/tool-agent-spec-yitang-self-motivation.md` | 已完成 |
| Wave 1 测试过程本身有价值 | 新建 case 卡归档测试方法、发现、修复、教训 | `30_wiki/cases/case-opc-agent-wave1-real-model-testing.md` | 已完成 |

---

## 八、可扩展方向（不在本任务内，仅记录）

1. **Wave 2**：针对 Wave 1 修复后的 agent-spec，增加更多行业场景和边缘 case。
2. **底层逻辑域升级**：科学理念 / 实事求是 / 解放思想三张卡重写。
3. **`self-motivation` 个人节律调参**：补充创始人工作节律/能量曲线输入门。
4. **`#28` lint 内容债分批清理**：长线任务，待统一拆批。

---

## 八、队列位置

- **入队编号**：`#50`
- **状态**：`queued`
- **依赖**：`#47` / `#49` 已终审通过
- **预计工时**：老顽童测试 2-3 天 + 欧阳锋终审 1 天

---

*王语嫣 2026-07-02*
