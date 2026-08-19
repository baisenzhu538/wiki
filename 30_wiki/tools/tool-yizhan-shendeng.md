---
id: tool-yizhan-shendeng
title: 一盏神灯：小白友好的蒸馏术（仓颉的 WorkBuddy 新手适配版·复刻）
type: tool
status: draft
confidence: 0.85
trust_level: high
language: zh-CN
created_at: 2026-08-19
updated_at: 2026-08-19
domain:
- knowledge-management
- ai-collaboration
aliases:
- 一盏神灯
- yizhan-shendeng
- 蒸馏书 小白
- 带读 蒸馏
discoverable_by:
- 一盏神灯
- 蒸馏 这本书
- 没读懂 蒸馏
- AI 带读
author: 黄药师（按视频描述复刻）；原版作者 袋鼠帝（知识星球分发，未公开）
reviewed_by: 待审
source_refs:
- 40_outputs/capabilities/skills/yizhan-shendeng/SKILL.md
- 30_wiki/cases/case-wechat-e7536bf1d8f1a7b1.md
- 10_raw/sources/src_2026-08-19_wechat_e7536bf1d8f1a7b1.md
related:
- tool-cangjie-skill
- tool-kdo-wechat-serendipity-collect
- framework-serendipity-five-channels
tags:
- audience:all-agents
- scene:execution
- method:automation
- content-format:tool
quality_labels:
- actionable
- cited
diagnostic_signals:
- signal: 用户说"用一盏神灯帮我蒸馏这本书/这篇论文/这份访谈"，或想蒸馏但没读懂原材料
  lens: 一盏神灯 = 仓颉前置"AI 带读"的新手适配版——先帮用户读懂再蒸馏
  follow_up: 调用 40_outputs/capabilities/skills/yizhan-shendeng/SKILL.md 四阶段流程
---

# 一盏神灯（仓颉新手适配版·复刻）

> 复刻自袋鼠帝视频《蒸馏就是AI时代的合法抢劫》（视频号，2026-08-19 偶遇采集入库）。
> 原版由作者在知识星球分发（未公开索引）；本卡为黄药师按视频描述+仓颉开源方法论的复刻实现。

## 与仓颉的分工（视频原话的设计意图）

| 用户状态 | 用哪个 |
|:--|:--|
| 还没读懂 / 没时间精读 | **一盏神灯**（先 AI 带读，再蒸馏） |
| 已读懂且有相当认知 | 仓颉（全流水线 + 压力测试，质量上限更高） |

## 四阶段流程

1. **AI 带读**（独有加法）：结构地图 + 核心概念表 + 章节要点，先给用户过目
2. **分型定向**：工具书蒸方法论（拿来直接用）/ 非工具书蒸思维框架（拿来思考）
3. **提炼+轻验证**：框架/原则/案例/反例/术语五路提取；依据可溯、非常识
4. **安装交付**：技能包写入 `~/.workbuddy/skills/`，交付"什么时候用哪个"指南

## 安装位置

| 环境 | 路径 |
|:--|:--|
| KDO | `40_outputs/capabilities/skills/yizhan-shendeng/` |
| WorkBuddy | `~/.workbuddy/skills/yizhan-shendeng/`（2026-08-19 已装） |

## 边界

- 蒸馏 ≠ 抄书：只保留可操作精华，禁止大段复制原文
- 每个技能包可独立使用，不依赖用户读过原书
- 原材料不足以支撑蒸馏时如实告知，不硬凑数量
- 姊妹技能：`distill-own-skill`（蒸馏用户自己的技能，含成长功能），同目录
