---
id: task_20260708_wangyuyan-product-kernel-domain-supplement
title: 产品内核域 P0-P2 补产：核心概念升级 + 案例卡 + 验证工具 + Agent 规格
status: reviewed
priority: P1
assignee: hermes
reviewer: 欧阳锋
expected_cards: 12
expected_agent_specs: 7
source_refs:
- 60_feedback/diagnosis/diag_20260708_yitang-pan-product-design-deep-dive-v2.md
- 00_inbox/一堂-产品内核实操课-Truman-口述.txt L524-L568,L1464-L2874,L3000-L3112
- 00_inbox/一堂-产品内核迭代课-Truman-口述.txt L1304-L1346,L194-L657,L700-L1150,L2069-L2253,L3018-L3400
- 00_inbox/一堂-产品内核验证课-Truman-口述.txt L1026-L1155,L1300-L1614,L1714-L2070,L2032-L2880,L2880-L3072
related:
- '[[diag_20260708_yitang-pan-product-design-deep-dive-v2]]'
- '[[laowantong-product-kernel-brief]]'
- '[[concept-一堂-product-kernel]]'
- '[[concept-一堂-kernel-iteration]]'
- '[[concept-一堂-kernel-validation]]'
- '[[tool-一堂-product-kernel-canvas]]'
- '[[tool-一堂-product-kernel-add-subtract]]'
- '[[yt-product-kernel-ten-metrics]]'
- '[[yt-product-kernel-validation]]'
- '[[yt-product-kernel-iteration]]'
created_at: 2026-07-08
updated_at: '2026-07-08T14:04:11.836807+00:00'
reviewed_by: 欧阳锋
review_date: '2026-07-08'
grade: A-
---

# 产品内核域 P0-P2 补产：核心概念升级 + 案例卡 + 验证工具 + Agent 规格

> 来源：`diag_20260708_yitang-pan-product-design-deep-dive-v2.md`
> 王语嫣判断：产品内核域五门课骨架已搭好，但三份主口述稿中 40%–50% 的案例细节、量化数字、操作步骤和暗知识尚未被吸收；验证/迭代框架命名不一致；两张洗发水 case 重复。本任务聚焦把产品内核域从“抽象定义”拉到“可执行工具 + 可迁移案例”。

---

## 一、目标产出

### P0：核心概念卡升级 + 验证工具卡

| # | 产出物 | 类型 | 文件路径 | 核心内容 |
|---|---|---|---|---|
| 1 | 产品内核概念卡升级 | concept | `30_wiki/concepts/concept-一堂-product-kernel.md` | 补全九大原则逐条定义 + 每个原则配 1 个口述案例 + 精确行号；补充“内核≠完整交付”边界 |
| 2 | 内核迭代概念卡升级 | concept | `30_wiki/concepts/concept-一堂-kernel-iteration.md` | 补充进化/量化/细化/强化/简化五方向与口述案例绑定：川味调料、立体车库、自习室、猫粮、银行风控 |
| 3 | 内核验证概念卡升级 | concept | `30_wiki/concepts/concept-一堂-kernel-validation.md` | 统一“三维度+六策略”框架；补充张磊洗发水完整验证路径、秦鹏分层策略、专家访谈三原则 |
| 4 | 六策略验证工具卡 | tool | `30_wiki/tools/tool-一堂-kernel-six-verification-strategies.md` | “聊问查测盘赌”六策略阶梯完整操作手册 + 13 点调研武器库 + 专家访谈三原则 |

### P1：案例卡补建 + 工具/DK 升级

| # | 产出物 | 类型 | 文件路径 | 核心内容 |
|---|---|---|---|---|
| 5 | 川味调料供应链案例 | case | `30_wiki/cases/case-yitang-chuanhe-seasoning-kernel.md` | 从“厂家直销低价优质”到“买底料+免费培训+到店实训+全程帮扶”再到线上标准化的完整迭代 |
| 6 | 立体车库案例 | case | `30_wiki/cases/case-yitang-zhongzheng-parking-garage.md` | 12 车位→智能化→部署自动化→规模经济 |
| 7 | 秦鹏通信模组案例 | case | `30_wiki/cases/case-qinpeng-iot-module-tiering.md` | 价格战 50%→20% 黄金数字、良品率 80/90 分层、四格服务矩阵 |
| 8 | 洗发水案例合并升级 | case | `30_wiki/cases/case-shampoo-product-kernel.md`（合并 `yt-product-kernel-shampoo-case`） | 以口述验证路径（竞品拆解→专家访谈→用户访谈→排列组合测试）为主线 |
| 9 | 内核加减法工具升级 | tool | `30_wiki/tools/tool-一堂-product-kernel-add-subtract.md` | 补充民主集中做减法流程：加法→分类→投票→一号位合并→3-5 条 |
| 10 | 十大指标工具升级 | tool | `30_wiki/tools/yt-product-kernel-ten-metrics.md` | 以口述稿“获客-服务-复购”漏斗为主分类，补充 proxy 指标 |
| 11 | 做而不信 DK 升级 | dk | `30_wiki/dark-knowledges/yt-product-kernel-do-without-belief.md` | 补充小鹅通行例与具体执行姿势 |

### P2：框架统一 + DK 新建 + Agent 规格

| # | 产出物 | 类型 | 文件路径 | 核心内容 |
|---|---|---|---|---|
| 12 | 验证框架卡统一 | framework | `30_wiki/frameworks/yt-product-kernel-validation.md` | 与概念卡统一：三维度改为“决定性/优化性/完备性”，六策略改为“聊问查测盘赌” |
| 13 | 迭代框架卡统一 | framework | `30_wiki/frameworks/yt-product-kernel-iteration.md` | 五方向与口述稿统一为进化/量化/细化/强化/简化，并增加触发信号 |
| 14 | 过度承诺陷阱 DK | dk | `30_wiki/dark-knowledges/yt-product-kernel-overpromise-trap.md` | 声音变现案例 + 前后端组织目标不一致的结构性原因 |
| 15 | 成本高信息低默认不做 DK | dk | `30_wiki/dark-knowledges/yt-product-kernel-cost-sensitive-default-no.md` | 顾问点评、24 小时班主任、私董会等案例 |
| 16 | 机会预判概念卡 | concept | `30_wiki/concepts/concept-一堂-business-prediction.md`（或 `opportunity-prediction`） | 补建商业预判/机会预判概念卡，与关键假设、产品内核形成五门课闭环 |
| 17 | 内核画布自动填充 Agent | agent-spec | `.agent/prompts/tool-agent-spec-yitang-kernel-canvas-autofill.md` | 输入产品描述 → 输出 5 格画布 |
| 18 | 加减法诊断 Agent | agent-spec | `.agent/prompts/tool-agent-spec-yitang-kernel-add-subtract-diagnosis.md` | 输入功能清单 → 输出 3-5 条内核 |
| 19 | 三问验证 Agent | agent-spec | `.agent/prompts/tool-agent-spec-yitang-kernel-three-questions.md` | 输入内核清单 → 决定性/优化性/完备性评估 |
| 20 | 迭代方向选择器 Agent | agent-spec | `.agent/prompts/tool-agent-spec-yitang-kernel-iteration-direction.md` | 输入阶段+指标 → 推荐迭代方向 |
| 21 | 验证策略阶梯推荐 Agent | agent-spec | `.agent/prompts/tool-agent-spec-yitang-kernel-verification-ladder.md` | 输入内核假设 → 聊/问/查/测/盘策略 |
| 22 | 失败模式匹配诊断 Agent | agent-spec | `.agent/prompts/tool-agent-spec-yitang-kernel-failure-mode-diagnosis.md` | 输入业务症状+数据 → 匹配失败模式 |
| 23 | 案例模式匹配 Agent | agent-spec | `.agent/prompts/tool-agent-spec-yitang-kernel-case-matching.md` | 输入业务描述 → 最相似口述案例 + 可迁移经验 |

---

## 二、验收标准

- [ ] 3 张 P0 concept 卡 `kdo pre-submit` PASS，无新增 ERROR；Critique ≥3 外部 + ≥2 内部；source_refs 精确到口述稿行号。
- [ ] 1 张 P0 工具卡 `tool-一堂-kernel-six-verification-strategies` 通过欧阳锋终审。
- [ ] 4 张 P1 case 卡通过终审；其中洗发水案例合并 `yt-product-kernel-shampoo-case`，删除重复卡并在原卡 frontmatter 添加 `merged_into`。
- [ ] 7 个 agent-spec 文件包含：触发场景、输入、输出、工作流、调用卡、边界风险、System Prompt。
- [ ] 统一“决定性/优化性/完备性”与“聊问查测盘赌”两套命名：在 `concept-一堂-kernel-validation` 中显式说明“三维度用于评估假设性质，六策略用于选择验证动作”。
- [ ] 所有口述稿中的量化数字（如自习室桌子 80/60cm、讲课 40–50%）降级为课程经验值，不当作普适标准。

---

## 三、最终判断

**评级：A-（高价值，直接决定产品内核域 Agent 能否落地）**

- 来源可靠：全部引用三份主口述稿行号，避免二手笔记失真。
- 解决核心矛盾：统一验证/迭代框架命名，合并重复洗发水案例。
- Agent 密度高：7 个 Agent 规格覆盖画布填充、加减法、三问验证、迭代方向、验证阶梯、失败模式、案例匹配七大高频场景。

**建议入队编号**：`#138`
**优先级**：P1
**Assignee**：老顽童
**Reviewer**：欧阳锋
**预计工时**：老顽童 4-5 天 + 欧阳锋终审 1 天
**依赖**：无（与 #137 可并行）

---

*王语嫣 2026-07-08*
