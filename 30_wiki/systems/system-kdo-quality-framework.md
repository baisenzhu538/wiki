---
id: system-kdo-quality-framework
title: "KDO 质量体系：双三角模型在知识工厂的落地"
type: system
status: draft
domain:
  - kdo
  - master
author: 黄药师
reviewed_by: 待审
review_date: 2026-08-08
confidence: 0.85
trust_level: observed
source_refs:
  - 00_inbox/人机协作双三角/一堂双三角-人机协作模型-口述.txt
  - cap_hub/features.json
created_at: 2026-08-08
updated_at: 2026-08-08
tags:
  - audience:huangyaoshi
  - audience:ouyangfeng
  - scene:reference
  - skill-level:advanced
aliases:
  - KDO质量体系
  - KDO双三角
  - 知识工厂质量
discoverable_by:
  - KDO质量体系
  - KDO双三角
  - 知识工厂质量
diagnostic_signals:
  - signal: 'KDO 有 8 道门禁 + 12 个 Feature，但没有一张卡描述整体质量框架'
    severity: high
    implication: '新 Agent 入职或黄药师失忆恢复时，无法快速理解 KDO 的质量体系全貌'
  - signal: '人类三角中的"体系"角最弱——KDO 的方法论框架分散在多个文件中'
    severity: medium
    implication: '没有单一入口回答"KDO 的质量是怎么保证的"'
related:
  - '[[concept-kdo-feature-registry]]'
  - '[[concept-kdo-component-library]]'
  - '[[framework-kdo-modeling-methodology]]'
  - '[[kdo-moc]]'
  - '[[master-moc]]'
  - '[[framework-kdo-self-attack]]'
---

# KDO 质量体系：双三角落地

> **定位**：KDO 的质量框架总纲——用 Truman 双三角模型描述知识工厂的质量保证体系。回答"KDO 的质量是怎么保证的"。

## 人类三角（人永远是主体，口述 L1457）

| 角 | Truman 定义 | KDO 映射 | 当前水平 |
|:--|:--|:--|:--|
| **审美** | 偏结果——对最佳实践的追求（L692-716） | 欧阳锋五轴审查标准 / 卡片质量标准 | 有（欧阳锋审查方法论 v2.0） |
| **体系** | 偏过程——完备的知行合一框架（L698） | 门禁栈 + 四层审查管线 + Feature 注册表 | 🟡 分散在多文件中，缺总纲 |
| **创造力** | 偏创新——跳出原有流程（L704） | E010/P-42/Feature注册表 = 事故驱动的创新 | 有（每次事故后提取方法论） |

## AI 三角（系统思维用 AI，口述 L1457-1466）

| 角 | Truman 定义 | KDO 映射 | 当前水平 |
|:--|:--|:--|:--|
| **基本功** | Feature 思维——原子化最小技术单位（L1402-1450） | 12 个注册 Feature / kdo_lint / pre-submit | ✅ Feature 注册表已建 |
| **数据** | 知识资产的积累和组织（L1188） | 2500 张卡 + Graph RAG + BM25 + 溯源 | ✅ 检索架构 v2 |
| **场景** | 不同场景使用不同工具组合（L1188） | 六角色分工 / 生产→审查→入队流水线 | ✅ 角色体系清晰 |

## 质量保证链路

```
新卡提交 → Feature 门禁（8 道原子规则，逐个独立验证）
         → 四层审查管线（L1 机械门禁 / L2 自攻击 / L3 欧阳锋终审 / L4 王语嫣升级）
         → 入库（索引刷新 + 搜索可达性验证）
         → 事故驱动进化（E 系列 dk 卡 + Feature 迭代）
```

## Feature 门禁栈（基本功角的核心）

| 顺序 | Feature | 拦什么 |
|:--|:--|:--|
| 1 | F1_UPDATED_AT | 缺日期——无法判断过时 |
| 2 | DUP_KEY | 重复键——#222/#223 根因 |
| 3 | F3_DUPLICATE_ID | 重复 ID——文件冗余 |
| 4 | R6_SEARCH | 空 title——外部 Agent 搜不到 |
| 5 | DK_7_SECTIONS | dk 缺段——结构不完整 |
| 6 | SEC_TYPO | 拼写错误——段名失效 |
| 7 | F2_BACKLINK | 断链——知识网络断裂 |
| 8 | F4_MOC_DEADLINK | MOC 死链——导航失效 |

## 审查四层管线（体系角的核心）

| 层 | 执行者 | 检查什么 |
|:--|:--|:--|
| L1 机械门禁 | kdo lint + schema | YAML / 必填字段 / source_refs / Feature 门禁栈 |
| L2 自攻击 | 老顽童 | 四路 Agent 攻击（逻辑/证据/完整性/时效性） |
| L3 终审 | 欧阳锋 | O0 溯源 + 五轴审查 + 魔鬼代言人 |
| L4 方向升级 | 王语嫣 | 跨域争议 / 新需求 / 方向异议 |

## 事故驱动进化循环（创造力角的核心）

```
事故 → 根因定位 → 提取 Feature → 注册入库 → 门禁升级
#222/#223 → E010 重复键 → DUP_KEY Feature → 门禁栈 +1
#224 争议 → P-42 核查缺位 → card_review_checklist Feature → 提交自检
搜索盲区 → delivery Path bug → F4_MOC_DEADLINK Feature → MOC 死链门禁
```

## 当前评估

| 双三角合拢度 | 自评 | 说明 |
|:--|:--|:--|
| 审美×基本功 | ✅ | 欧阳锋审查标准 + Feature 门禁栈 |
| 体系×数据 | 🟡 | 体系分散，数据组织好但导航（MOC）刚建 |
| 创造力×场景 | ✅ | 事故驱动进化 + 六角色协作 |

**下一个重点**：人类三角的"体系"角——把分散的质量框架（门禁/审查/Feature/角色）收敛为一张总纲卡（本卡）。建成后 KDO 的双三角完整合拢。
