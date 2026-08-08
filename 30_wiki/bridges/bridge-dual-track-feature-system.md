---
id: bridge-dual-track-feature-system
title: 「桥接：双轨Feature体系——quality-gate vs capability」
type: bridge
status: reviewed
confidence: 0.88
trust_level: high
domain:
  - ai-basic
  - kdo
author: 老顽童
source_refs:
  - 10_raw/sources/feature-periodic-table-v0.8.json
source_person: 欧阳锋/王语嫣
source_context: 欧阳锋洞察3：cap_hub质量门禁Feature ≠ 课程解题Feature——双轨体系
reviewed_by: 欧阳锋
aliases:
  - 双轨Feature
  - quality-gate
  - capability
  - feature-periodic-table-v0.8
discoverable_by:
  - 双轨Feature
  - quality-gate
  - capability
  - cap_hub
related:
  - framework-truman-feature-layered-system
  - framework-truman-feature-thinking-core
  - concept-kdo-feature-registry
  - tool-ai-feature-inventory
  - agent-spec-复盘教练
tags:
  - method:feature-system
  - method:cross-domain
  - scene:architecture
  - audience:developers
  - content-format:bridge
created_at: 2026-08-08
updated_at: 2026-08-08
quality_labels:
  - insight
  - principle
---

> 桥接AI基本功域（Feature思维）与KDO基础设施域（cap_hub quality gate）——两个"Feature注册表"的分工与边界。
> **定位**：属于 [[framework-truman-feature-thinking-core]] 的第 0 步（体系架构层），桥接 [[framework-truman-feature-layered-system]] 的 L0-L5 分层与 cap_hub 质量门禁体系。

# 双轨Feature体系：quality-gate vs capability

> 一句话：KDO有两个Feature注册表——cap_hub的12个quality-gate Feature管"卡片本身不坏"，课程周期表的100个capability Feature管"AI解题更强"。同源（都源自Truman Feature思维），不同用——混编=拿lint规则当解题武器。

---

## 双轨对照

| | quality-gate轨 | capability轨 |
|:---|:---|:---|
| **来源** | cap_hub/features.json | 课程周期表 V0.8 |
| **数量** | 12 | 100 |
| **定义** | KDO基础设施的质量门禁 | 提升AI解题水平的最小实践单位 |
| **回答的问题** | "这张卡合格吗？" | "怎么用AI解决这个问题？" |
| **使用者** | KDO生产者/审查者 | AI使用者 |
| **例子** | F1_UPDATED_AT（检查updated_at存在）、F4_MOC_DEADLINK（检查死链） | 最终意图、温度参数、状态机、Skill封装 |
| **误用后果** | — | 拿"检查双aliases"当解题武器→无关 |
| **执行方式** | 自动化lint脚本 | 人+AI协作使用 |

---

## 为什么不能混编

| 混编场景 | 后果 |
|:---|:---|
| 把quality-gate Feature放进解题菜单 | 用户面对"检查updated_at"无所适从——这不是解题武器 |
| 把capability Feature当质量门禁用 | "最终意图"无法自动化检查——不是门禁 |
| 两个注册表放一起 | 消费端不知道哪个是"查自己"，哪个是"查卡片" |

**双轨设计的本质**：quality-gate轨是KDO的"免疫系统"——自动检查卡片健康度。capability轨是KDO的"武器库"——让人从菜单中点菜。两个系统都需要，但不能互相替代。

---

## 消费端区分指引

| 场景 | 用哪个轨 |
|:---|:---|
| 提交卡片前自检 | quality-gate（跑lint看Pass/Fail） |
| 面对AI任务不知道从哪下手 | capability（从周期表点5-10个Feature提假设） |
| 审查卡片质量 | quality-gate（检查结构/溯源/一致性） |
| 优化AI工作流 | capability（叠Feature：换模型→版本管理→Skill→Agent） |

## 桥接到KDO已有卡

- `[[concept-kdo-feature-registry]]`：锚定quality-gate轨——本卡补充capability轨的分工说明
- `[[tool-ai-feature-inventory]]`：AI Feature盘点——本卡提供双轨区分让它不混编
- `[[framework-truman-feature-layered-system]]`：capability轨的L0-L5分层体系
