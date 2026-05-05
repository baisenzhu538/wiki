---
title: "一堂知识体系建设 — Phase 1 地基搭建"
assigned_to: "黄药师"
created_by: "欧阳锋"
created_at: "2026-05-06"
status: done
priority: P0
---
# 一堂知识体系建设 — Phase 1 地基搭建

## 完成内容

- 创建课程概念页模板 `templates/tpl-yitang-course-concept.md`
- 创建课程交付件模板 `templates/tpl-yitang-course-artifact.md`
- 创建课程大地图索引页 `30_wiki/concepts/yitang-course-map.md`
- 图片归档 `10_raw/assets/yitang/`（5 张分类 PNG + 3 张 webp）
- 4 篇 inbox 转录稿完整管线处理（rename → ingest → enrich --llm → frontmatter 调整）
- 更新一堂实体页 `30_wiki/entities/一堂.md`
- 建立课程间 wikilink 关联

## 新增 wiki 页面

| 页面 | 分类 | source |
|------|------|--------|
| 一堂-课程地图精华串讲 | course-map | src_20260506_13e7bbca |
| 一堂-调研武器库课程 | research | src_20260506_bb9048a6 |
| 一堂-调研行动营启动_智能优化 | research | src_20260506_e4634e13 |
| 一堂-案例必修课_智能优化 | case-studies | src_20260506_9b4788a6 |

## 发现的问题

- `kdo enrich --llm` 的 `has_todos` 检查依赖英文 "TODO:" 字面量，ASR 时间戳格式的页面会被跳过——需在 curation.py 中增加中文占位符检测
- ingest 阶段的中文 regex 提取器产出随机开场白作为标题（"第一个举手。"、"值班主"等）——需改进标题生成逻辑
