---
id: "corr-20260612-laowantong-design-domain-missing-batch1"
title: "纠正记录：王语嫣勘误——4 张课程概念卡 + 3 张待定卡 domain 修正"
type: "correction"
status: "closed"
created_at: "2026-06-12"
updated_at: "2026-06-12"
author: "laowantong"
domain: ["diagnosis", "design", "ai-saas"]
source_refs:
  - "60_feedback/corrections/correction_20250611_design-domain-missing.md"
---

## 背景

源勘误记录 `correction_20250611_design-domain-missing.md` 指出：

1. 4 张课程/框架概念卡当前 domain 为 `ai-saas`，但内容主体是 AIGC 设计方法论/视觉 Prompt 系统，应补充 `design` 域。
2. 3 张中置信度卡片是否加 `design` 需要人工判断。

本次纠正仅处理上述 7 张卡片，遵循 **"标内容，不标出身"** 的 domain 标注规则。

---

## 修改清单

### 一、4 张课程概念卡补 design domain

| 文件 | 原 domain | 新 domain | 判断依据 |
|:---|:---|:---|:---|
| `30_wiki/concepts/aigc设计基础01ai生图原理与提示词基本功.md` | `["ai-saas"]` | `["ai-saas", "design"]` | 月白 AIGC 设计入门课，主讲 AI 生图原理、提示词基本功、逆向提示词法，属于设计工作流底层能力 |
| `30_wiki/concepts/aigc设计师实操培训01口喷设计范式与电商ai设计全流程.md` | `["ai-saas"]` | `["ai-saas", "design", "business-strategy"]` | 口喷设计范式、四改图法、电商 AI 设计三步（白底图→场景图→详情页），直接服务电商商业转化 |
| `30_wiki/concepts/aigc文创案例设计课leo文创ip从0到1全流程.md` | `["ai-saas"]` | `["ai-saas", "design"]` | 文创 IP 从角色确立、材质选择、表情包量产到电商物料的完整设计案例 |
| `30_wiki/concepts/视觉prompt三层操作系统-srom-visual-os.md` | `["ai-saas"]` | `["ai-saas", "design"]` | 视觉 Prompt 三层操作系统（L1 视觉基因库 / L2 场景组件库 / L3 组装公式），是设计方法论 |

### 二、3 张待定卡人工判断

| 文件 | 原 domain | 新 domain | 判断结论 |
|:---|:---|:---|:---|
| `30_wiki/tools/yt-tool-ai-ppt-maker.md` | `personal`（字符串，非数组，且 `personal` 不在枚举中） | `["design", "personal-growth"]` | 内容是 AI 对话式 PPT 生成器，核心能力是排版风格定义与视觉一致性，应加 `design`；同时作为个人效率工具，归入 `personal-growth` |
| `30_wiki/concepts/skill-马易-AIGC项目ROI评估.md` | `""`（空字符串，无效） | `["business-strategy", "ai-collaboration"]` | 主题是 AIGC 项目投入产出评估与商业回报验证，属于商业决策，**不加 `design`** |
| `30_wiki/concepts/skill-马易-工作流优先于AIGC的决策方法.md` | `""`（空字符串，无效） | `["ai-collaboration", "business-strategy"]` | 主题是工作流与 AIGC 的选型决策，属于人机协作方法论，**不加 `design`** |

---

## 规范化处理

- 所有修改卡片的 `updated_at` 已更新为 `2026-06-12`。
- 将 `domain` 统一为数组格式，剔除空字符串、非标量等不规范写法。
- `domain` 值全部来自 `90_control/schemas/concept.yaml` 枚举列表。

---

## 验证

使用 Python + PyYAML 对 7 张卡片的 frontmatter 进行验证：

- `domain` 均为非空数组
- 所有 domain 值均在 schema 枚举范围内
- 4 张课程概念卡、yt-tool-ai-ppt-maker 均包含 `design`
- 2 张马易 skill 卡未包含 `design`（符合内容判断）

结果：**全部通过**。

---

## 未处理项说明

源勘误记录还列出 127 张 `skill-月白-*.md` 设计技能卡 domain 为空，建议统一补充 `design`。本次任务仅处理明确的 4+3 张卡片，127 张月白技能卡的批量修正待后续任务安排。
