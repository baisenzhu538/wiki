---
name: strategy
description: 企业战略总入口——冉鹏30年经验，判断阶段+路由子Skill
version: 1.0.0
author: 黄药师
license: MIT
platforms: [linux, macos, windows]
metadata:
  hermes:
    tags: [战略, 冉鹏, BRM, 六阶段, 战略规划]
    related_skills: [strategy]
---

# Strategy（企业战略总入口）

冉鹏 · 30年战略咨询经验。核心主张：**战略不是定目标（三年100亿），是明确从现状到目标的路径。**

## Constraints

<hard_limits>
- 战略分析必须先判断企业所处阶段——不同阶段的战略奥义完全不同
- 战略是一号位的核心基本功——最终选择由一号位拍板，Agent 只提供分析框架
</hard_limits>

## 意图分类

| 场景 | 路由到 | 示例 |
|:--|:--|:--|
| 不知道战略从哪开始 | `/strategy-brm` | "帮我看下我们公司的战略问题在哪" |
| 不确定公司处于什么阶段 | `/strategy-lifecycle` | "我们该追求增长还是利润？" |
| 战略执行出了问题 | `/strategy-diagnose` | "为什么战略定了但推不下去？" |
| 需要做差距分析 | `/strategy-brm`（Step 1） | "我们和目标的差距在哪？" |

## 战略的核心洞察

1. **战略不是定目标**——"三年100亿"是目标不是战略。战略是从现状到目标的路径。
2. **不同阶段不同打法**——初创期"独木桥"和吃好期"建壁垒"是完全不同的战略逻辑
3. **三个悖论**：80%战略培训讲执行、90%公司无战略部、99%战略项目存在断层
4. **战略是一号位的核心基本功**——因为只有一号位对选择结果负责

## 参考卡片
- `strategy-domain-digest` — 域索引入口
- `framework-strategy-six-stages` — 六阶段模型
