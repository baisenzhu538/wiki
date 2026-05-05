---
title: "一堂课程大地图"
type: concept
subtype: hub
domain: ["yitang"]
status: stable
tags: ["yitang", "course-map", "index"]
created_at: "2026-05-06"
updated_at: "2026-05-06"
---

# 一堂课程大地图

> 一堂 200+ 门课程的结构化知识索引。按五条修炼路径组织，每门课提取核心方法论、关键洞见和案例索引。

## 课程体系总览

![[一堂进步大地图.png]]

## 五条修炼路径

| 路径 | 对应 | 核心命题 | 课程数（约） |
|------|------|---------|:--:|
| [[#个人修身]] | 修身 | 突破成长上限 | ~30 |
| [[#管理修炼]] | 齐家 | 操盘更复杂资源 | ~30 |
| [[#创业修炼]] | 治国 | 让 1% 成功率翻十倍 | ~40 |
| [[#案例库]] | — | 从真实商业案例中学习 | ~40+ |
| [[#调研方法]] | — | 科学调研的武器库 | ~10 |

## 课程列表

```dataview
TABLE category, instructor, status
FROM "30_wiki/concepts"
WHERE domain = "yitang" AND subtype = "course"
SORT category ASC, file.name ASC
```

## 个人修身

![[个人修身课程.png]]

```dataview
TABLE instructor, status
FROM "30_wiki/concepts"
WHERE domain = "yitang" AND subtype = "course" AND category = "personal-growth"
SORT file.name ASC
```

## 管理修炼

![[管理课程.png]]

```dataview
TABLE instructor, status
FROM "30_wiki/concepts"
WHERE domain = "yitang" AND subtype = "course" AND category = "management"
SORT file.name ASC
```

## 创业修炼

![[创业课程.png]]

```dataview
TABLE instructor, status
FROM "30_wiki/concepts"
WHERE domain = "yitang" AND subtype = "course" AND category = "entrepreneurship"
SORT file.name ASC
```

## 案例库

![[案例课程.png]]

```dataview
TABLE instructor, status
FROM "30_wiki/concepts"
WHERE domain = "yitang" AND subtype = "course" AND category = "case-studies"
SORT file.name ASC
```

## 调研方法

```dataview
TABLE instructor, status
FROM "30_wiki/concepts"
WHERE domain = "yitang" AND subtype = "course" AND category = "research"
SORT file.name ASC
```

## 相关页面

- [[30_wiki/entities/一堂|一堂实体页]] — 公司背景与方法论总览
- [[一堂方法论体系总图]] — 四张地图的详细拆解
- [[一堂调研武器库13招]] — 调研方法论武器库
- [[一堂调研行动营 — AI辅助系统式调研方法论]] — AI 协同调研范式
