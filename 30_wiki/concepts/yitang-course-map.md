---
title: "一堂课程大地图"
type: concept
subtype: hub
domain: ["yitang"]
status: stable
tags: ["yitang", "course-map", "index", "dataview"]
created_at: "2026-05-06"
updated_at: "2026-05-06"
---

# 一堂课程大地图

> Dataview 驱动的课程列表页。方法论框架和体系解读见 [[30_wiki/systems/一堂方法论体系总图|一堂方法论体系总图]]（权威 Hub）。

![[一堂进步大地图.png]]

## 按地图浏览

```dataview
TABLE yitang.module AS "模块", yitang.level AS "层级", yitang.course_type AS "类型", status
FROM "30_wiki/concepts"
WHERE domain = "yitang" AND yitang.map = "personal"
SORT yitang.module ASC, file.name ASC
```

```dataview
TABLE yitang.module AS "模块", yitang.level AS "层级", yitang.course_type AS "类型", status
FROM "30_wiki/concepts"
WHERE domain = "yitang" AND yitang.map = "management"
SORT yitang.module ASC, file.name ASC
```

```dataview
TABLE yitang.module AS "模块", yitang.level AS "层级", yitang.course_type AS "类型", status
FROM "30_wiki/concepts"
WHERE domain = "yitang" AND yitang.map = "entrepreneur"
SORT yitang.module ASC, file.name ASC
```

```dataview
TABLE yitang.module AS "模块", yitang.level AS "层级", yitang.course_type AS "类型", status
FROM "30_wiki/concepts"
WHERE domain = "yitang" AND yitang.map = "infinite"
SORT yitang.module ASC, file.name ASC
```

## 全部课程卡片

```dataview
TABLE yitang.map AS "地图", yitang.module AS "模块", yitang.course_type AS "类型", status
FROM "30_wiki/concepts"
WHERE domain = "yitang" AND yitang
SORT yitang.map ASC, yitang.module ASC, file.name ASC
```

## 相关页面

- [[30_wiki/systems/一堂方法论体系总图|一堂方法论体系总图]] — 权威方法论 Hub，含四张地图详解、十层解读、学习路径
- [[30_wiki/entities/一堂|一堂实体页]] — 公司背景与方法论总览
- [[yt-course-map-lecture|一堂课程地图精华串讲]] — 2025 开学第一课转录
- [[一堂调研武器库13招]] — 调研方法论武器库
- [[一堂调研行动营 — AI辅助系统式调研方法论]] — AI 协同调研范式
