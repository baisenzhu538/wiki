---
id: tool-cangjie-skill
title: 仓颉 cangjie-skill：把书/长视频/播客蒸馏成可执行 Agent Skills（开源原版）
type: tool
status: draft
confidence: 0.9
trust_level: high
language: zh-CN
created_at: 2026-08-19
updated_at: 2026-08-19
domain:
- knowledge-management
- ai-collaboration
aliases:
- 仓颉
- cangjie
- cangjie-skill
- 蒸馏书
- 拆书 skill
- book2skill
discoverable_by:
- 蒸馏 一本书
- 拆书
- 把书做成 skill
- 仓颉
- cangjie
author: 黄药师（登记）；原作者 袋鼠帝 kangarooking
reviewed_by: 待审
source_refs:
- 40_outputs/capabilities/skills/cangjie-skill/SKILL.md
- 30_wiki/cases/case-wechat-e7536bf1d8f1a7b1.md
related:
- tool-yizhan-shendeng
- tool-kdo-wechat-serendipity-collect
tags:
- audience:all-agents
- scene:execution
- method:automation
- content-format:tool
quality_labels:
- actionable
- validated
- cited
diagnostic_signals:
- signal: 用户说"蒸馏这本书/拆书/把书做成 skill"，且已读懂原书、追求最高质量
  lens: 仓颉是重型全流水线（RIA-TV++ 七阶段含压力测试），适合深蒸馏；小白/未读书先转一盏神灯
  follow_up: 调用 40_outputs/capabilities/skills/cangjie-skill/SKILL.md 的七阶段流程
---

# 仓颉 cangjie-skill（开源原版）

> 作者：袋鼠帝（GitHub kangarooking，AGPL v3，6.8K star）。
> 仓库：https://github.com/kangarooking/cangjie-skill ｜ 官网：https://cangjie-skill.com/
> 本地副本：`40_outputs/capabilities/skills/cangjie-skill/`（2026-08-19 经 gh-proxy 克隆，含 methodology/extractors/templates 全套）

## 能力

把书、长视频转写、播客、课程、访谈等长内容蒸馏成一组**原子化、可被 agent 真实调用**的 skills。

**RIA-TV++ 七阶段流水线**：
1. Adler 整书理解（分析阅读法四步）→ `BOOK_OVERVIEW.md`
2. 5 个提取器并行（框架/原则/案例/反例/术语）→ 候选池
3. 三重验证筛选（≥2 处独立佐证 / 有预测力 / 非常识，通过率通常 25-50%）
4. RIA++ 构造（原文引用/重写/书中案例/触发场景/可执行步骤/边界盲点）
5. Zettelkasten 链接 → `INDEX.md` + `GLOSSARY.md`
6. 压力测试（含跨 skill 混淆诱饵题，不过回炉）
7. 交付 `DIGEST.md` 精华长文 + 安装到 skills 目录

## 安装位置

| 环境 | 路径 |
|:--|:--|
| KDO | `40_outputs/capabilities/skills/cangjie-skill/` |
| WorkBuddy | `~/.workbuddy/skills/cangjie-skill/`（2026-08-19 已装） |

## 边界

- ✅ 蒸馏：方法论/决策框架/清单/原则/概念体系
- ❌ 不做：书摘/读后感/作者角色扮演（后者是 nuwa-skill 的活）
- 小白/未读懂原书场景 → 用适配版 `tool-yizhan-shendeng`（一盏神灯）
- 生态咬合：nuwa 蒸馏人 / cangjie 蒸馏书 / darwin 让 skill 进化
