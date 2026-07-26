---
id: framework-strategy-business-design
title: 业务设计六要素×三步骤——冉鹏战略规划核心操作框架（源于IBM BLM）
type: framework
status: reviewed
confidence: 0.95
trust_level: high
domain: strategy
source_refs:
- 00_inbox/战略专题/冉鹏PPT截图/引擎点火20260110 战略破局（冉鹏）(1)_97_vlm_desc.md
- 00_inbox/战略专题/冉鹏PPT截图/引擎点火20260110 战略破局（冉鹏）(1)_99_vlm_desc.md
- 00_inbox/战略专题/引擎点火20260110 战略破局（冉鹏）(1)_ocr.md
quality_labels:
- principle
- validated
created_at: '2026-06-21'
updated_at: '2026-06-29'
author: 老顽童（初版）→ 黄药师（PPT _97+_99 补强 v2）
reviewed_by: 欧阳锋
related:
- '[[strategy-domain-digest]]'
- '[[framework-strategy-blm]]'
- '[[pending_unknown]]'
- '[[pending_unknown]]'
- '[[pending_unknown]]'
- tool-strategy-five-see-three-set
- yt-business-model-canvas
- case-strategy-exit-remove
tags:
- audience:ceo
- scene:diagnosis
- skill-level:advanced
aliases:
- 冉鹏PPT截图
- 引擎点火
---
# 业务设计六要素×三步骤

> 源于 IBM BLM（Business Leadership Model）。冉鹏 30 年中国实战改编。六要素是"设计什么"，三步骤是"怎么设计"。

## 六要素清单

- **客户选择**：我们到底为谁创造价值？谁是最重要的客户？
- **价值主张**：我们提供什么独特价值？为什么客户选我们？
- **价值获取**：如何从提供的价值中获利？盈利模式是什么？
- **活动范围**：自己做什么？外包什么？在价值链哪个环节？
- **战略控制**：护城河在哪？如何保持差异化不被复制？
- **风险管理**：业务设计有哪些关键风险？如何应对？

## 框架全景（PPT _97）

```
                    领导力
                      ↓
    ┌─────────────────────────────────┐
    │  战略                           │  执行                    │
    │  市场洞察 → 战略意图             │  气氛与文化 → 关键任务    │
    │      ↓                          │      ↓                  │
    │  ██ 业务设计 ██ → 创新焦点      │  正式组织 → 人才         │
    └─────────────────────────────────┘
                      ↓
                  市场结果
              (业绩差距 + 机会差距)
                      ↑
                    价值观
```

业务设计是 BLM 战略侧的**核心模块**（红色高亮）——市场洞察和战略意图是输入，业务设计是产出，创新焦点是延伸。

## 六要素

| # | 要素 | 核心问题 | 操作卡 |
|:--|:--|:--|:--|
| 1 | **客户选择** | 我们到底为谁创造价值？谁是最重要的客户？ | `tool-strategy-customer-selection` |
| 2 | **价值主张** | 我们提供什么独特价值？为什么客户选我们？ | `tool-strategy-value-proposition` |
| 3 | **价值获取** | 如何从提供的价值中获利？盈利模式是什么？ | `tool-strategy-value-capture` |
| 4 | **活动范围** | 自己做什么？外包什么？在价值链哪个环节？ | `tool-strategy-activity-scope` |
| 5 | **战略控制** | 护城河在哪？如何保持差异化不被复制？ | `tool-strategy-control-points` |
| 6 | **风险管理** | 业务设计有哪些关键风险？如何应对？ | `tool-strategy-risk-management` |

## 三步骤（PPT _99 — 工作坊模板）

冉鹏在 `_99` 号 PPT 中提供了标准工作坊模板：六要素各走三步。

```
步骤1: 诊断现有业务设计
  → 每个要素，我们现在是什么？
     ↓
步骤2: 设计期望业务设计  
  → 基于市场洞察和差距分析，理想状态是什么？
     ↓
步骤3: 识别执行挑战
  → 从现有→期望的差距中，最大的执行障碍？
```

### 空白工作坊模板

| 六要素 | 内涵（引导问题） | 步骤1 诊断现有 | 步骤2 设计期望 | 步骤3 执行挑战 |
|:--|:--|:--|:--|:--|
| 客户选择 | 我们到底为谁创造价值？ | | | |
| 价值主张 | 客户为什么选我们？ | | | |
| 价值获取 | 我们如何获利？ | | | |
| 活动范围 | 我们做什么/不做什么？边界？ | | | |
| 战略控制 | 护城河在哪？ | | | |
| 风险管理 | 最大的风险是什么？ | | | |

**使用方式**：战略工作坊中，团队分组→各自填写→汇总碰撞→形成共识。

## Agent 执行指令

```python
def business_design_workshop(company_context: str):
    """运行业务设计六要素×三步骤工作坊"""
    elements = ["客户选择", "价值主张", "价值获取", "活动范围", "战略控制", "风险管理"]
    results = {}
    for elem in elements:
        current = ask(f"我们现在的「{elem}」是什么？具体描述。")
        desired = ask(f"基于市场洞察和差距分析，我们期望的「{elem}」应该是什么？")
        challenges = ask(f"从现有→期望的差距中，「{elem}」最大的执行障碍？")
        results[elem] = {"现有": current, "期望": desired, "挑战": challenges}
    return results
```

## 与 KDO 五步法的关系

业务设计六要素是**战略层**操作框架，五步法是**业务层**执行框架：

| 六要素 | 五步法对应 | 关系 |
|:--|:--|:--|
| 客户选择 + 价值主张 | Step 1 需求分析 | 战略定义"为谁创造什么价值" → 五步法验证"需求是否真实" |
| 价值获取 + 活动范围 | Step 3 商业模式 | 战略定义盈利模式和边界 → 五步法做单元模型和盈利验证 |
| 战略控制 | Step 5 壁垒 | 战略定义护城河方向 → 五步法做壁垒深度分析 |

## 与 Business Model Canvas 对比

| BM Canvas 九要素 | 业务设计六要素 | 差异 |
|:--|:--|:--|
| 客户细分/客户关系/渠道 | 客户选择 | 六要素合并——"选择谁"比"怎么触达"更上游 |
| 价值主张 | 价值主张 | 一致 |
| 收入来源/成本结构 | 价值获取 | 六要素合并——先定义"怎么赚钱"再拆收入和成本 |
| 关键业务/核心资源/重要伙伴 | 活动范围 | 六要素关注"边界"——做什么不做什么 |
| — | **战略控制点** | BMC 没有——BLM 独有优势 |
| — | **风险管理** | BMC 没有——冉鹏从咨询实战加入 |

## 外部验证

| 主张 | 验证 | 来源 |
|:--|:--|:--|
| 源于 IBM BLM | ✅ 与 IBM BLM Business Design 模块一致 | IBM BLM 官方文档 |
| 六要素 vs 七要素 | ✅ PPT _97+_99 明确六个操作要素。第七个"总结"是步骤不是要素 | PPT VLM 描述直接确认 |
| 麦肯锡 7S | ✅ 冉鹏引用为风险管理工具 | slide 128 |

---

*老顽童初版 · 黄药师 PPT _97+_99 补强 v2 · 2026-06-21*
