---
id: diag_20260708_yitang-demand-analysis-deep-dive-v2
title: 五步法之需求分析域二次深挖诊断报告（v2）：知识已验证，缺 Agent 封装
type: diagnosis
status: active
source: 00_inbox/五步法之需求分析
source_refs:
  - 00_inbox/五步法之需求分析/一堂-需求分析-方法论-口述.txt L80-L122,L224-L276,L332-L460,L1074-L1126,L1262-L1272,L1308-L1318,L2176-L2206
  - 00_inbox/五步法之需求分析/一堂-需求分析-找到精准需求-口述.txt
  - 00_inbox/五步法之需求分析/一堂-需求分析-剥离需求-口述.txt L110,L1228-L1232,L1336-L1342
  - 00_inbox/五步法之需求分析/一堂-需求分析-需求评估-口述.txt L476-L536,L1104-L1186,L1720-L1796,L1962-L1976
  - 00_inbox/五步法之需求分析/一堂-需求分析-空间测算-口述.txt L322-L344,L1308-L1320,L1308-L1870,L2252-L2278,L2348
  - 00_inbox/五步法之需求分析/一堂-需求分析-JTBD理论-口述.txt L1034-L1044
  - 00_inbox/五步法之需求分析/AI场景推演教练提示词.txt
  - 00_inbox/五步法之需求分析/AI辅助探讨需求选项的提示词.md
  - 00_inbox/五步法之需求分析/需求分析提示词.txt
reviewer: 欧阳锋
created_at: 2026-07-08
updated_at: 2026-07-08
related:
  - "[[domain-demand-analysis-index]]"
  - "[[framework-demand-iceberg]]"
  - "[[framework-demand-opportunity-spectrum]]"
  - "[[framework-demand-usp-model]]"
  - "[[framework-demand-validation-pipeline]]"
  - "[[yt-demand-decision-chain]]"
  - "[[yt-demand-early-validation]]"
  - "[[yt-demand-jtbd-application]]"
  - "[[yt-demand-scenario-reconstruction]]"
  - "[[tool-demand-assessment-triangle]]"
  - "[[tool-demand-blindspot-checklist]]"
  - "[[tool-demand-four-forces]]"
  - "[[tool-demand-iceberg-l1-user]]"
  - "[[tool-demand-iceberg-l6-hypothesis]]"
  - "[[tool-demand-report-template]]"
  - "[[prompt-demand-ai-coach]]"
  - "[[yt-demand-insight-extraction]]"
  - "[[case-demand-milkshake-jtbd]]"
  - "[[case-demand-silver-parenting]]"
  - "[[tool-agent-spec-yitang-Y-model-coach]]"
---

# 五步法之需求分析域二次深挖诊断报告（v2）

## 执行摘要

需求分析域是“**知识密度高、官方已验证、Agent 适配度极高**”的域。课程已经把拆推评算、冰山六层、USP 因果链、需求评估三角形、天花板四层（TAM/SAM/SOM/BEL/CR1）讲透，并且官方已经打磨出可直接使用的 `AI场景推演教练提示词.txt`。当前 wiki 侧骨架完整（domain-index + 6 张 framework + 6 张 L1-L6 工具卡 + cases + dk + prompt-methodology），但存在**半成品峡谷**：

1. **6 张 L1-L6 工具卡大量 `src_unknown` 和执行占位符未填**；
2. **官方 `AI场景推演教练提示词.txt` 未迁移为 `.agent/prompts/` 下的 Agent Spec**；
3. **缺少“需求评估三角形打分器”“天花板测算教练”“RAT 生成器”“微观体感脚本生成器”等可调用工具卡**；
4. **案例未与冰山 L1-L6 形成结构化 few-shot 库**。

**评级：A（建议作为下一批 Agent 生产重点）**。

---

## 一、现有覆盖度速览

### 1.1 素材侧：官方已给出“人+机”三件套

- **方法论层**：拆推评算四步法、JTBD 六层冰山、USP 因果链、需求评估三角形、天花板四层框架。
- **工具层**：一页纸模板、6 张 L1-L6 工具卡、`tool-demand-report-template.md`。
- **AI 层**：`AI场景推演教练提示词.txt`（官方打磨，方法论-口述 L2176-L2206 称其为“三件套”之一）。

### 1.2 Wiki 侧：骨架完整，执行层半成品

| 类型 | 代表卡 | 状态 |
|---|---|---|
| domain-index | `domain-demand-analysis-index.md` | 可用 |
| framework | `framework-demand-iceberg.md`、`framework-demand-usp-model.md`、`framework-demand-validation-pipeline.md`、`framework-demand-opportunity-spectrum.md` | 骨架完整 |
| tool | `tool-demand-iceberg-l1-user` 至 `l6-hypothesis` | **大量 `src_unknown` / 占位符** |
| tool | `tool-demand-assessment-triangle.md`、`tool-demand-four-forces.md`、`tool-demand-blindspot-checklist.md` | 可用但缺口述细节 |
| tool | `tool-demand-report-template.md` | 缺融资版/经营版区分 |
| case | `case-demand-milkshake-jtbd`、`case-demand-silver-parenting` 等 | 散落，未结构化 few-shot |
| dk | `dk-demand-feature-stacking`、`dk-demand-hidden-need`、`dk-demand-misjudgment-rate` 等 | 可用 |
| prompt-methodology | `prompt-demand-ai-coach.md` | 可用但非 Agent Spec |

**关键缺口**：没有一张 `.agent/prompts/` 下的需求分析专属 Agent Spec。

---

## 二、未被吸收的暗知识 / 操作细节

| # | 暗知识/操作细节 | 精确来源 | 现有卡覆盖 | 建议动作 |
|---|----------------|---------|-----------|---------|
| 1 | **拆推评算不是严格工作流，而是可跳步/滑步的组合工具箱** | `空间测算-口述.txt:322-344` | 多数卡按四步线性呈现 | 升级 `domain-demand-analysis-index` 或新建 `tool-demand-chai-tui-ping-suan-guide` |
| 2 | **需求的本质是“跟你无关的客观事实”** | `剥离需求-口述.txt:1228-1232` | 概念卡提及但未强调 | 升级 `yt-demand-hierarchy-model` 或 `concept-yt-demand-objectivity` |
| 3 | **硬剥离：连产品形态都要忍住不提，用 10% 至 1% 成本验证需求** | `剥离需求-口述.txt:1336-1342` | 未覆盖 | 新建 DK `dk-demand-hard-stripping` |
| 4 | **JTBD 任务描述公式 = 动词 + 对象 + 情境（不含产品名）** | `JTBD理论-口述.txt:1034-1044` | `yt-research-user-jtbd` 有公式但可强化 | 升级 `yt-research-user-jtbd` |
| 5 | **四种力量公式：(推力 + 拉力) > (焦虑 + 习惯)** | `方法论-口述.txt:80-122` | `tool-demand-four-forces.md` 已覆盖 | 补充口述行号和马术课案例 |
| 6 | **三种任务决定溢价：功能/情感/社交任务可支撑 10-100 倍溢价** | `方法论-口述.txt:224-276` | `framework-demand-usp-model` 有提及 | 升级并补马术课/安全座椅案例 |
| 7 | **微观体感 = 像素级感官还原，常等于信任状** | `方法论-口述.txt:332-460` | 未系统工具化 | 新建 `tool-demand-micro-experience-script` |
| 8 | **需求评估核心动作：多选项 × 对比 × 维度 × 信心** | `需求评估-口述.txt:476-536` | `tool-demand-assessment-triangle` 有框架 | 升级为带打分流程的工具卡 |
| 9 | **普遍性 / 频次 / 刚性是“不可能三角”，最怕错配** | `需求评估-口述.txt:1104-1186` | 三角形三轴已覆盖 | 补充“错配而非小”判断规则 |
| 10 | **频次有四个层级：问题发生/真实解决/使用产品/付费** | `需求评估-口述.txt:1720-1796` | 三角形只画一个“频次”轴 | 升级工具卡，打分前先对齐层级 |
| 11 | **刚性的真正尺度是“愿意付出多少成本”** | `需求评估-口述.txt:1962-1976` | 未深入 | 升级 `tool-demand-assessment-triangle` |
| 12 | **天花板有“融资视角”与“经营视角”两套话语** | `空间测算-口述.txt:1308-1320` | 未区分 | 升级 `tool-demand-report-template` |
| 13 | **TAM/SAM/SOM 之外还要算 CR1（头部天花板）和 BEL（生存线）** | `空间测算-口述.txt:1788-1870,2252-2278` | 未覆盖 | 新建 `framework-demand-ceiling-four-lines` |
| 14 | **关键假设优先原则：前置假设优先、验证单一、风险高的优先** | `方法论-口述.txt:1262-1272` | `framework-demand-validation-pipeline` 有提及 | 补口述行号与决策规则 |
| 15 | **AI 在需求洞察上“小颗粒度表现非常好”，但人不能退场** | `方法论-口述.txt:1074-1126,1308-1318` | `prompt-demand-ai-coach` 有提及 | 作为 Agent 边界写入 Spec |

---

## 三、可直接 Agent 化的环节

| # | Agent 环节 | 解决的问题 | 输入 | 输出 | 调用卡 | 边界风险 |
|---|---|---|---|---|---|---|
| 1 | **冰山推演教练** | 用户从模糊想法拆到 L6 可验证假设 | 一句话创业想法 | L1-L6 完整推演 + 机会卡片 + RAT×3 | `framework-demand-iceberg`、`tool-demand-iceberg-l1-l6` | L4/L5 前禁止产品方案 |
| 2 | **拆推评算段位诊断** | 判断用户当前处于哪一层，决定下一步最小动作 | 用户已有材料 + 自述进度 | 当前段位 + 下一步工具 + 可选跳步 | `domain-demand-analysis-index` | 避免强制走完四步 |
| 3 | **需求评估三角形打分器** | 多选项对比排序 | 3-10 个需求选项 | 普遍性/频次/刚性评分 + 排序 + 信心值 | `tool-demand-assessment-triangle` | 先对齐频次层级 |
| 4 | **天花板测算教练** | 10-15 分钟对话估算市场大小 | 业务描述 + 目标用户 + 付费模式 | TAM/SAM/SOM/CR1/BEL 报告 | 新建 `framework-demand-ceiling-four-lines` | 区分融资/经营视角 |
| 5 | **RAT 生成器** | 从 L5 洞察抽取最危险假设 | L5 洞察清单 | 3-5 个关键假设 + 验证方法 + 优先级 | `tool-demand-iceberg-l6-hypothesis` | 不能替代真实验证 |
| 6 | **需求选项探讨与纠偏** | 用户初步想法后追问、控变量、找盲区 | 初步产品/需求想法 | 3 个选项 + 盲区清单 + USP 追问 | `framework-demand-usp-model`、`tool-demand-blindspot-checklist` | 不直接给最终方案 |
| 7 | **微观体感访谈脚本生成** | 根据崩溃环节生成 5 感访谈问题 | L4 关键崩溃环节 | 访谈问题清单 + 观察要点 | 新建 `tool-demand-micro-experience-script` | 不能替代真实访谈 |
| 8 | **2B/2C 需求字典适配** | 按业务类型切换评估尺子和访谈重点 | 业务类型 + 初步描述 | 适配后的冰山问题模板 | `需求分析提示词.txt` 拆解 | 避免字典僵化 |

---

## 四、矛盾 / 差异点

| # | 差异点 | 口述稿/OCR 原文 | 现有卡/提示词 | 建议处理 |
|---|--------|----------------|--------------|---------|
| 1 | **拆推评算是四步工作流还是工具箱？** | 空间测算-口述 L322：可跳步、滑步 | 多数卡按四步线性 | 在 Agent 和工具卡中显式声明“可跳步” |
| 2 | **L3 要求方案中立，L6 才允许产品形态** | 冰山方法论 | L6 卡模板已有产品形态字段 | 在 Agent Spec 中 hard-code 阶段纪律 |
| 3 | **天花板报告要区分融资/经营视角** | 空间测算-口述 L1308-1320 | `tool-demand-report-template` 未区分 | 模板增加版本选择 |
| 4 | **频次有四个层级，三角形只有一个轴** | 需求评估-口述 L1720-1796 | `tool-demand-assessment-triangle` 一个频次轴 | 打分前必须先对齐层级 |
| 5 | **AI 被鼓励又被警告“不要纯 AI 作业”** | 方法论-口述 L1074-1126,1308-1318 | `prompt-demand-ai-coach` 偏鼓励 | Agent Spec 增加“人在环”强制确认点 |
| 6 | **同学作业提示词 vs 官方提示词属性不同** | `优秀提示词合集.md` 为学员习作 | `AI场景推演教练提示词.txt` 为官方 | 仅迁移官方提示词为 Agent Spec，学员习作作 few-shot/反例 |

---

## 五、建议新建 / 升级清单

### P0：Agent 封装与工具卡补全

| # | id | 类型 | 核心内容 | source_refs |
|---|---|---|---|---|
| 1 | `agent-spec-demand-iceberg-coach` | agent-spec | 迁移 `AI场景推演教练提示词.txt` 为 TCPR 格式 Agent Spec，含完整 System Prompt 模板 | `AI场景推演教练提示词.txt`；`方法论-口述.txt:2176-2206` |
| 2 | `tool-demand-iceberg-l1-user` 至 `l6-hypothesis` | tool | 补全 6 张工具卡的 `src_unknown`、执行占位符、口述案例、精确行号 | 6 份口述稿对应章节 |
| 3 | `tool-demand-chai-tui-ping-suan-guide` | tool | 拆推评算“工具箱而非工作流”使用指南，含跳步/滑步规则 | `空间测算-口述.txt:322-344` |
| 4 | `tool-demand-assessment-triangle` | tool | 升级：普遍性×频次×刚性打分流程，含频次四层对齐 | `需求评估-口述.txt:476-536,1104-1186,1720-1796` |

### P1：新增框架/工具/模板

| # | id | 类型 | 核心内容 | source_refs |
|---|---|---|---|---|
| 5 | `framework-demand-ceiling-four-lines` | framework | TAM/SAM/SOM/CR1/BEL 四层天花板线，融资版 vs 经营版 | `空间测算-口述.txt:1308-1870,2252-2278` |
| 6 | `tool-demand-ceiling-coach` | tool | 10-15 分钟对话输出天花板报告的操作流程 | `空间测算-口述.txt:2348` |
| 7 | `tool-demand-rat-generator` | tool | 从 L5 洞察自动生成最危险假设清单 | `方法论-口述.txt:1262-1272` |
| 8 | `tool-demand-micro-experience-script` | tool | 基于 L4 崩溃点生成 5 感 + 情绪 + 决策瞬间访谈脚本 | `方法论-口述.txt:332-460` |
| 9 | `tool-demand-option-explorer` | tool | 用户初步想法后的 USP 追问、控变量、找盲区流程 | `AI辅助探讨需求选项的提示词.md` |
| 10 | `tool-demand-report-template` | tool | 升级：区分融资版与经营版输出 | `空间测算-口述.txt:1308-1320` |

### P2：案例库、知识库、Skill

| # | id | 类型 | 核心内容 | source_refs |
|---|---|---|---|---|
| 11 | `case-demand-iceberg-few-shot` | case | 奶昔 / 银发育儿 / 挂脖空调 / 马术课 结构化 few-shot，映射 L1-L6 | 口述稿与现有 case |
| 12 | `knowledge-demand-2b-dictionary` | knowledge | 2B 需求字典：角色/决策链/采购周期/隐性需求 | `需求分析提示词.txt` |
| 13 | `knowledge-demand-2c-dictionary` | knowledge | 2C 需求字典：场景/频次/情感任务/替代方案 | `需求分析提示词.txt` |
| 14 | `skill-demand-analysis` | skill | 把 Agent + 卡片 + 案例 + 字典打包为 Skill | 综合 |

---

## 六、需求分析专属 Agent 设计：`demand-iceberg-coach`

### 6.1 定位

- **名称**：`agent-spec-demand-iceberg-coach`
- **一句话**：基于一堂五步法需求分析方法论，引导用户从模糊创业想法一路拆到 L6 可验证需求假设的商业需求深度洞察教练。
- **边界**：只处理需求分析域；不进入产品设计、商业模式设计、融资路演；不替代真实用户访谈。

### 6.2 TCPR 身份

- **T（Task）**：作为需求分析域教练，完成 L1-L6 冰山推演。
- **C（Context）**：用户是创业者/业务负责人/产品经理，面对新业务或产品机会。
- **P（Personality）**：循循善诱的资深顾问；主动给 3 个选项让用户确认；在 L4/L5 前严格方案中立。
- **R（Rules）**：
  1. L4/L5 之前禁止讨论具体产品功能。
  2. 每进入一步先 3-5 句话解释原理。
  3. 每次输出必须让用户做选择或确认，不能仅陈列。
  4. 所有数字标注置信度（✅/⚠️/🔮）。
  5. 最终必须输出机会卡片 + 最危险假设（RAT）。

### 6.3 触发场景

1. “我有一个创业想法，帮我看看需求靠不靠谱。”
2. “按一堂五步法拆一下这个机会。”
3. 用户给出一个模糊产品点子，需要先剥离需求。
4. 用户已有多个方向，需要做需求评估三角形对比。
5. 用户想估算某个需求的市场天花板。
6. 用户已有用户访谈材料，想生成 L5 洞察和 RAT。

### 6.4 工作流

```
Step 0: 项目启动 → 索要“一句话创业想法”
Step 1: L1 & L2 维度拆解与画像锚定 → 输出 3 个“用户+场景+痛点”组合选项
Step 2: L3 核心任务定义 → 输出 3 个“动词+对象+情境”任务陈述
Step 3: L4 任务地图推演 → 8 步地图 + 1-3 个关键崩溃环节
Step 4: L5 隐藏洞察 → 三种任务 + 四种力量 + 微观体感内心独白
Step 5: L6 机会卡片 → 3-5 张卡片，每张含 RAT×3
Step 6: 评估三角形 / 天花板入口 → 必要时转交 ceiling-coach 或 triangle-evaluator
```

### 6.5 调用卡

- `framework-demand-iceberg`
- `framework-demand-usp-model`
- `tool-demand-iceberg-l1-user` 至 `tool-demand-iceberg-l6-hypothesis`
- `tool-demand-assessment-triangle`
- `tool-demand-report-template`
- 跨域时转交 `tool-agent-spec-yitang-Y-model-coach`

### 6.6 边界风险

| 风险 | 防控措施 |
|---|---|
| AI 幻觉给出脱离事实的洞察 | 每步输出标注“假设待验证”，强制用户确认 |
| 用户跳过 L3 直接要方案 | Agent 拒绝进入 L6，提示“请回到核心任务” |
| 把学员习作当官方方法 | 系统提示词源仅引用 `AI场景推演教练提示词.txt` |
| 数字被当作真理 | 所有估算带 ✅⚠️🔮 置信度，并提示“课程经验值，非普适真理” |
| 与 Y模型 Coach 冲突 | 本 Agent 聚焦需求域；跨域时先进入 Y模型 Coach 再转回 |
| 纯 AI 作业 | 每步保留“人在环”强制确认点 |

---

## 七、最终判断与入队建议

**评级：A**

- 知识完整度 A：课程已经把拆推评算、冰山六层、评估三角形、天花板四层讲透。
- AI 适配度 A：官方已验证 AI 教练在 L1-L6 推演和天花板测算上表现稳定。
- Wiki 现状 B+：骨架完整，但工具卡半成品、Agent Spec 缺失、提示词未迁移。
- Agent 投产优先级：**A / 建议作为下一批 Agent 生产重点**。

**建议入队编号**：`#140`
**任务名称**：`task_20260708_wangyuyan-demand-analysis-agent-supplement`
**优先级**：P0（用户明确“需求是极其重要的域”）
**Assignee**：老顽童
**Reviewer**：欧阳锋
**预计产出**：
- 1 张 Agent Spec（P0）
- 6 张 L1-L6 工具卡补全（P0）
- 2 张工具卡升级（P0-P1）
- 3 张新工具卡（P1）
- 1 张 framework 卡（P1）
- 1 张 case few-shot 卡（P2）
- 2 个知识库（P2）
- 1 张 Skill（P2）

---

*王语嫣 2026-07-08*
