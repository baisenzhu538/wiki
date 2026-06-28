---

id: three-party-data-alignment
title: 三方认知对齐：KDO 数据管线 6+1 框架
type: decision
status: draft
domain: master
tags:
- src_unknown
- src_unknown
created_at: 2026-05-31
updated_at: '2026-06-16'
target_roles:
- src_unknown
- src_unknown
- src_unknown
author: unknown
source_context: KDO internal record （原始 source 无法追溯，已标记为 src_unknown，待后续补充）
source_refs:
- src_unknown
reviewed_by: pending
confidence: 0.6
trust_level: low
related:
  - [[dk-modeling-ai-compound-leverage]]
  - [[plan_20260531_data-curator-v1.3]]
  - [[dk-modeling-ai-judgment-limit]]
  - [[data-curator-role-division]]
  - [[ouyangfeng-data-alignment-response]]
---
# 三方认知对齐：KDO 数据管线 6+1 框架

## 为什么需要这份文档

- src_unknown
- src_unknown
- src_unknown

**三方对齐的目标**：三人在以下六个核心理念上达成一致。此后黄药师的产出按此标准审查，用户的方向按此框架决策，欧阳锋的审查按此视角执行。

---

## 一、核心理念：从"查字典"到"食材"

**旧思维**：数据是给人查的——结构化、准确、一致。评估标准是"字段填没填、格式对不对"。

**新思维**：数据是给 AI 吃的——AI 理解了能产出好东西就行。评估标准是"**AI 用了这数据之后，输出变好了吗？**"

这意味着审查卡片时不再只看 frontmatter 完整度，更要看：
- src_unknown
- src_unknown
- src_unknown

---

## 二、6+1 管线框架（A.D.U.C.I.T + Governance）

```
预判(A) → 识别(D) → 收集(U) → 处理(C) → 使用(I) → 反馈(T) → 回到预判(A)
                                                              ↑
                          治理(Governance) ← 贯穿全程，不是第七步
```

| 步骤 | 一句话 | KDO 对应 |
|------|--------|---------|
| **A 预判** | 以终为始，先想清楚数据未来怎么用 | 入库前估值（微观/中观/宏观），不是拦住，是给优先级 |
| **D 识别** | 盘点眼下有什么，找到被忽略的高价值数据 | 出遗漏清单——暗知识、过程数据、BA对比 |
| **U 收集** | 湖仓：先扔湖里（inbox）养着，别过度思考 | inbox=湖，wiki=仓。关键是升仓决策 |
| **C 处理** | 三层工序：粗加工→精加工→**注入灵魂** | clean→tag+chunk→萃取指南 |
| **I 使用** | 五级深度：投喂→封装→检索→配置→训练。别跳级 | kdo query→Data Pack→Graph RAG |
| **T 反馈** | 三种模式：人工/监督/鱿鱼游戏。没反馈 = AI永远不听劝 | kdo feedback 需闭环回卡片 |
| **治理** | 防泄露/防污染/防过期/防幻觉当事实 | data_generation 标记 + expiry + rights |

---

## 三、湖仓架构

```
00_inbox/ (湖) — 低门槛快速捕获，截图/录音/链接/笔记，什么都往里扔
     ↓ 升仓决策：预判(A)→识别(D)→ROI 为正？
30_wiki/ (仓) — 经过全链路处理的高质量数据
```

**三方共识点**：
- src_unknown
- src_unknown
- src_unknown

---

## 四、暗知识（最重要的一条）

**定义**：不是大模型内置的，只有你有的，需要提炼才能用的知识。

**KDO 已经积攒但从未处理的暗知识**：
- src_unknown
- src_unknown
- src_unknown
- src_unknown
- src_unknown

**三方共识点**：三步编译法（Condense→Question→Synthesize）的设计目标是提取稳定知识，不是捕获暗知识。暗知识需要独立的捕获管线（六字段模板），不是套用三步编译法。

---

## 五、真原子粒度

| | 旧（假原子） | 新（真原子） |
|------|-----------|-----------|
| **粒度** | heading 级，200-2000 字/块 | **主张/事实/规则级，30-200 字/块** |
| **块数/卡** | 5-16 | **20-80** |
| **能否独立回答 query** | 部分能 | **每条都能** |
| **能否独立被反驳** | 不能 | **能 — 矛盾检测的前提** |

**三方共识点**：当前的 `##` heading 级切分不是真正的原子化。真正的原子是"一条知识 = 一块"，可被独立引用、独立验证、独立反驳。

---

## 六、双轨捕获

```
口述/分享/对话 → 原始素材
                    ├── 产品轨（已有）：三步编译法 → 概念卡 → wiki
                    │     产出：结论、边界、关联
                    │
                    └── 过程轨（新增）：六字段模板 → 暗知识卡 → wiki
                          产出：工作流、工具用法、失败记录、学习路径、个人体悟
```

**三方共识点**：不是否定三步编译法——它适合提取稳定知识。但需要新增平行的暗知识捕获管线。暗知识卡的 type 是 `dark-knowledge`，有自己的 frontmatter 字段（source_person, source_context, dark_knowledge_type）。

---

## 七、三人的角色边界

| 角色 | 在数据管线中的职责 |
|------|------------------|
| **用户（决策者）** | 定方向：哪些暗知识优先捕获？湖仓升仓的优先级？宏观层的长期预判？ |
| **欧阳锋（Architect）** | 审标准：管线产出是否符合 6+1 框架？暗知识卡质量是否达标？治理护栏是否到位？**审而不改** |
| **黄药师（Builder）** | 建管线：实现 A→D→U→C→I→T 各阶段脚本、双轨捕获模板、湖仓升仓逻辑。**按此框架执行，产出一致** |

---

## 八、当前状态

**方案文档**：`30_wiki/decisions/plan_20260531_data-curator-v1.3.md`（完整版，含月白案例、暗知识清单、修正记录）

**阶段**：方案制定完成。Pilot 待执行。Skill 脚本已创建（`40_outputs/capabilities/skills/data-curator/scripts/`）。

**下一步**：等待欧阳锋审查本对齐文档 + 方案 v1.3，确认三方认知一致后进入实施。
