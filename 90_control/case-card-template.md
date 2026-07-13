# Case 卡模板（案例库）

> 案例卡记录**真实发生的事**——"谁做过、什么场景、什么结果"。
> 和概念卡（"是什么"）、技能卡（"怎么做"）互补。

## Frontmatter

```yaml
---
id: case-{short-name}
title: "案例：{一句话描述}"
type: case
status: draft
problem_domains:            # ← 核心检索维度：按问题类型
  - 网上获客
  - 商机发现
industry: {行业}
scale: {个人/团队/公司/平台}
source_person: {谁说的}
source_context: {场合}
source_refs: []
wiki_refs: []
definition_of_done:
  - 问题描述清晰
  - 方案可理解
  - 可迁移点明确
tags:
  - "#case"
  - "#problem/{问题域}"
  - "#industry/{行业}"
  - "#method/{方法}"
  - "#source/{来源}"
related_skills: []
related_concepts: []
related_cases: []
created_at: YYYY-MM-DD
updated_at: YYYY-MM-DD
---
```

## 正文

```markdown
# 案例：{标题}

## 原始表述
> {原文引用，越简短越好。保留口语感}

## 问题
{这个案例解决的是什么问题？}

## 方案
{怎么解决的？可以反推操作方法}

## 结果
{效果如何？有具体数字更好}

## 可迁移
- {类似场景1：谁可以用这个方法}
- {类似场景2}
- {AI时代怎么升级}

## 关键标签
- 问题域：{网上获客、商机发现...}
- 行业：{企业服务、餐饮...}
- 方法：{全网扫描、自动筛选...}

## 关联
- 技能：[[skill-xxx]] — {这个案例可以配合什么技能}
- 概念：[[concept-xxx]] — {背后的理论}
- 案例：`[[case-xxx]]` — {类似的案例}

## 来源
- {谁}，{场合}，{日期}

## Feedback Path
- 60_feedback/comments/ — 反馈
```
