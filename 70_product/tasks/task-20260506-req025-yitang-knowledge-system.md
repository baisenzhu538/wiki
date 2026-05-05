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

## Phase 1.5 — 合龙（2026-05-06）

欧阳锋的 [[30_wiki/systems/一堂方法论体系总图|一堂方法论体系总图]] 与黄药师的 Phase 1 产出完成合龙：

| 合龙项 | 操作 | 结果 |
|--------|------|------|
| Hub 定位 | 总图保持为权威 Hub，yitang-course-map 降级为 Dataview 列表页 | 不重复 |
| Frontmatter 迁移 | 4 张新课概念卡从 flat (`subtype`/`category`/`course_id`) → `yitang:` 嵌套 schema | 兼容 concept.yaml `additionalProperties: false` |
| 文件命名 | 中文文件名 → `yt-{map}-{slug}.md` 英文 convention（Obsidian MCP move_note 自动更新 wikilink） | 可编程访问 |
| 模板更新 | `tpl-yitang-course-concept.md` 切换为 `yitang:` 嵌套 schema | 未来卡片一致 |
| 总图更新 | 八/九/审查清单 更新，标记 Phase 2 Step 2.1 完成 | 状态同步 |
| H1 修复 | 4 页垃圾标题（"值班主"/"第一个举手。"等）→ 正确中文标题 | 可读 |
| ASR 清理 | 调研行动营 Summary 的 ASR 时间戳文本 → 人工撰写摘要 | 可读 |
| Schema 验证 | 移除 `subtype`/`category`/`course_id`（不在 schema 中），`status: enriched` → `reviewed` | schema 兼容 |

### 当前文件映射

| 旧文件名 | 新文件名 | yitang.map | yitang.module |
|----------|----------|:--:|------|
| 一堂-课程地图精华串讲 | `yt-course-map-lecture.md` | — (meta) | — |
| 一堂-调研武器库课程 | `yt-entrepreneur-research-weapons.md` | entrepreneur | 调研方法论 |
| 一堂-调研行动营启动_智能优化 | `yt-entrepreneur-research-camp.md` | entrepreneur | 调研方法论 |
| 一堂-案例必修课_智能优化 | `yt-entrepreneur-case-method.md` | entrepreneur | 案例学习 |
