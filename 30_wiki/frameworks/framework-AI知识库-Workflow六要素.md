---
id: framework-AI知识库-Workflow六要素
title: Workflow 六要素 + 节点拆细降模型门槛
type: framework
status: reviewed
confidence: 0.9
trust_level: high
domain:
- ai-knowledge
- knowledge-management
author: 老顽童
reviewed_by: 欧阳锋
created_at: '2026-08-23'
updated_at: '2026-09-07'
quality_labels:
- actionable
- insight
quality_score: 9
reuse_direction: "AI 工作流设计评审，自动化任务拆分，token 成本优化，Agent 流水线搭建"
aliases:
- Workflow六要素
- 节点拆细
- 工作流六要素
- AI知识库-Workflow六要素
- 半肥猫
- AI×知识管理-开放麦-逐字稿
- AI知识库-知识库搭建与落地-半肥猫-口述
- 标签示例
source_refs:
- 10_raw/sources/banfeimao-openmic/AI知识库-知识库搭建与落地-半肥猫-口述.txt:1084-1100
- 10_raw/sources/banfeimao-openmic/AI×知识管理-开放麦-逐字稿.md:1-1043
- 10_raw/sources/banfeimao-openmic/给王语嫣的任务编排建议-半肥猫开放麦-AI知识库.md:20-28
- 60_feedback/diagnosis/diag_20260823_wangyuyan-banfeimao-ai-kb-diagnosis.md
- 10_raw/sources/banfeimao-openmic/标签示例.yaml:1-65
related:
- framework-AI知识库-五阶段演进
- framework-AI知识库-知识卡片公式
- concept-AI知识库-原子化拆分
- framework-AI知识库-分库与映射表
- framework-AI知识库-加卡片加标签双原则
tags:
- audience:ceo
- scene:diagnosis
- skill-level:advanced
- 知识管理
- 工作流
review_date: 2026-09-07
---
# Workflow 六要素 + 节点拆细降模型门槛

> **定位**：半肥猫《AI×知识管理》阶段 3 核心框架——工作流不是把任务丢给 AI，而是六个要素配齐 + 节点拆细到「小模型也能稳定跑」。

> 一句话：一个能跑的 AI 工作流 = 知识库 + Prompt 规则 + 检索方式 + 明确任务 + 输入输出标准 + 验收方法；而把任务拆得越细，越不挑模型、越省 token。

## 一、Workflow 六要素（核心结构）

| # | 要素 | 定义 | 例 |
|:--|:--|:--|:--|
| 1 | **知识库** | 燃料（可检索的知识资产） | 分库 + 标签的卡片库 |
| 2 | **Prompt 规则** | 提示词约定/角色/边界 | 「你是选题 Agent，只输出 3 个选题」 |
| 3 | **检索方式** | AI 如何查知识库 | RAG/关键词/映射表联动 |
| 4 | **明确任务** | 一次只做一个任务 | 选题/脚本/润色分开，不混 |
| 5 | **输入输出标准** | 输入格式 + 输出格式约定 | 输入=标题，输出=Markdown 表格 |
| 6 | **验收方法** | 怎么判断做对了 | 质量检查/人工验收/关键节点人验收 |

## 二、节点拆细降模型门槛（暗知识 №5）

> 口述稿 L1084-L1100：
> 「你拆的越多，我的注意越集中，那么它的能力越强……如果你把路由意图、提纲、文案、润色、校验全部写到一个大的提示词里面去，能不能实现呢？没问题也能实现，但是**他挑模型**，还有可能不稳定。**如果说你把这个拆得很细的时候，可能他就不怎么挑模型了**——小的模型、国产的模型、便宜模型它也能做出来，而且它很稳定。」

| 拆分程度 | 效果 | 适用 |
|:--|:--|:--|
| 大提示词（全任务一锅） | 挑模型、不稳定、贵 | 演示/简单任务 |
| **节点拆细**（每步一任务） | 不挑模型、稳定、省 token | 生产级工作流 |

**与 KDO 三目标直接呼应**：拆越细越省 token（KDO 三目标之一）——半肥猫的节点拆细 = KDO「省 token」的外部印证。

## 三、行动框架（Workflow 搭建六步）

| 步骤 | 动作 | 判断标准 |
|:--|:--|:--|
| 1. 定任务 | 明确一次要自动化什么 | 单一明确任务（不混） |
| 2. 拆节点 | 按语义拆成小步骤 | 每节点一个小任务，可独立验收 |
| 3. 配要素 | 六要素逐项落实 | 知识库/Prompt/检索/任务/IO/验收全有 |
| 4. 建流程 | 节点串联成工作流 | 前置节点输出=后置节点输入 |
| 5. 试跑 | 用真实数据跑通 | 输出符合验收标准 |
| 6. 换模型 | 用便宜模型验证稳定性 | 小模型也能稳定输出=拆分到位 |

## 四、不要用的场景（Synthesis）

| 场景 | 为什么失效 | 替代方案 |
|:--|:--|:--|
| 一次性/演示任务 | 搭六要素工作流成本高于收益 | 直接对话完成 |
| 没有可检索知识库就建 Workflow | 工作流空转（AI 没燃料） | 先完成阶段 1-2（知识资产化） |
| 拆节点过度（每句话一节点） | 流程碎片化，维护成本爆炸 | 按「语义原子」拆节点（同原子化判定） |

## 五、Action Triggers

| 触发场景 | 第一个动作 | 成功指标 |
|:--|:--|:--|
| 自动化任务不稳定/挑模型 | 把大提示词拆成细节点 | 便宜小模型也能稳定输出 |
| 设计 AI 工作流 | 六要素逐项检查 | 六要素全配齐，缺一不可 |
| KDO 流水线讨论 | 对照六要素（capture→ingest→enrich→produce） | 每个环节有明确输入输出标准+验收 |

## 复用指引（标签治理 v1.1，#668 转正批补齐）

> 本卡为标签治理 v1.1（`diag_20260906_wangyuyan-bfm-template-distilled.md §二·六`）方法论引用源；三节骨架与 reuse_direction 字段级 gold example=`10_raw/sources/banfeimao-openmic/标签示例.yaml`（10_raw 原件升格链接）。

**适用场景**
- 自动化任务不稳定、挑模型、贵时
- 设计/评审一个 AI 工作流方案
- KDO 流水线环节对照（capture→ingest→enrich→produce）

**可复用方式**
- Agent 按六要素清单逐项检查：知识库/Prompt/检索/任务/IO 标准/验收
- 用「节点拆细→便宜小模型也能稳定输出」判断拆分是否到位
- 前置节点输出=后置节点输入的串联检查

**注意事项**
- 一次性/演示任务直接对话完成，不建工作流
- 没有可检索知识库先别建 Workflow（空转，AI 没燃料）
- 拆节点过度（每句话一节点）维护成本爆炸——按语义原子拆

## 六、Critique

- **内部局限**：节点拆细增加搭建与维护成本（「workflow 拉线维护，小 bug 调两天」——诊断书 L5 隐性成本）；拆多细没有公式，靠试错。
- **外部攻击（系统工程视角）**：节点拆细 vs 整体提示词是经典 trade-off——拆细省 token 但增加编排复杂度和错误传播面（每节点都要调试）；大型模型（2026 主流）能力增强后整体提示词也能稳定，拆细的收益边际递减——但半肥猫的实证（小模型稳定）对成本敏感场景仍成立。
- **外部攻击（KDO 实证）**：KDO 的 kdo 流水线（capture→ingest→enrich→produce）正是节点拆细的工业实例——每环节独立、可验收；#373 等批次任务证明拆细后小模型可稳定执行批量判定。

## 迭代日志

- **2026-08-23 v1.0**：基于口述稿 L1084-1100（节点拆细原话）+ 洪七公建议书 §2.3（六要素）+ 诊断书暗知识 №5（省 token 呼应）编写。
- **2026-09-07 v1.1（#668 转正批）**：四节补齐（`reuse_direction` + 适用场景/可复用方式/注意事项，gold example=`10_raw/sources/banfeimao-openmic/标签示例.yaml:1-65`）；自攻击：无内容性发现（机械核查 0 死链 0 缺源）；补四节；status draft→pending_review 提审转正；本卡登记为标签治理 v1.1（`diag_20260906_wangyuyan-bfm-template-distilled.md §二·六`）方法论引用源（与词表线 90_control/tags-vocab 互链待规范侧回填）。
