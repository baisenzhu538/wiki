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

| 旧文件名 | 新文件名（欧阳锋命名） | yitang.map | yitang.module |
|----------|----------|:--:|------|
| 一堂-课程地图精华串讲 | `yt-system-course-map-lecture.md` | — (meta) | — |
| 一堂-调研武器库课程 | `yt-research-weaponry-course.md` | — (跨地图) | 调研方法论 |
| 一堂-调研行动营启动_智能优化 | `yt-research-action-camp-launch.md` | — (跨地图) | 调研方法论 |
| 一堂-案例必修课_智能优化 | `yt-case-mandatory-cases.md` | — (跨地图) | 案例学习 |

> 注：调研和案例为跨地图工具，暂不限定单一 map。Phase 2 课程清单提取后按欧阳锋的 map 分类统一分配。

---

## 最终交付报告（2026-05-06，黄药师 → 欧阳锋）

### Phase 1 + 合龙 全部产出

| 文件 | 状态 | 关键属性 |
|------|:--:|------|
| `yt-system-course-map-lecture.md` | reviewed | `yitang: {module: 课程体系总览, course_type: method, level: foundational, series: true}` |
| `yt-research-weaponry-course.md` | reviewed | `yitang: {map: entrepreneur, module: 调研方法论, course_id: yt-research-003, course_type: method, level: core}` |
| `yt-research-action-camp-launch.md` | reviewed | `yitang: {map: entrepreneur, module: 调研方法论, course_id: yt-research-camp-001, course_type: method, level: foundational}` — title 已与 `一堂调研行动营-ai辅助系统式调研方法论` 区分 |
| `yt-case-mandatory-cases.md` | reviewed | `yitang: {map: entrepreneur, module: 案例学习, course_id: yt-case-001, course_type: method, level: foundational}` |

### 质量检查

| 检查项 | 结果 |
|--------|:--:|
| 4 张卡 frontmatter 符合 concept.yaml schema（`additionalProperties: false`） | ✅ |
| 4 张卡 H1 标题无转录 artifacts | ✅ |
| 4 张卡 Summary 为课程摘要（非转录开场白） | ✅ |
| 4 张卡有 Synthesis 对标（2-3 wikilink） | ✅ |
| 重叠卡已声明关系（武器库↔13招 源-精，行动营↔原文润色 同源精炼） | ✅ |
| 文件名符合 `yt-{domain}-{slug}.md` convention | ✅ |
| 全局 wikilink 无断链（Obsidian MCP move_note 自动更新） | ✅ |
| 总图 section 八 已包含 4 张新课卡 | ✅ |
| 总图 Phase 2 Step 2.1 已标记完成 | ✅ |
| 总图顶部已链接 `[[yitang-course-map]]` Dataview 列表页 | ✅ |
| `yitang-course-map.md` Dataview 查询已适配 `yitang.map` | ✅ |
| 模板 `tpl-yitang-course-concept.md` 已切换为 `yitang:` 嵌套 schema | ✅ |

### 已知延后

| 项 | 原因 |
|----|------|
| course_id 格式统一（纯数字 vs `yt-xxx-nnn`） | Phase 2 提取完整课程清单时统一 |
| 调研/案例卡暂未限定单一 map | 跨地图工具，Phase 2 按欧阳锋分类统一分配 |

### 发现的 KDO 管线问题

1. **CJK enrich 跳过**：`curation.py:175-182` 的 `has_todos()` 只检测英文 `"TODO:"` 字面量，中文 ASR 页面被静默跳过。workaround：手动在 frontmatter 加 `TODO:` 触发。
2. **ingest 中文标题提取**：regex 提取器产出随机开场白作为标题。workaround：ingest 后手动 rename + 修 H1。

## Phase 2.2 交付报告（2026-05-06，黄药师）

### 产出

| 文件 | 变更 | 关键属性 |
|------|------|------|
| `30_wiki/systems/一堂方法论体系总图.md` | 替换管理/创业地图占位列表 → 详细课程表；新增无限修炼课程清单；新增八点五 Phase 2.2 提取总结；标记 Phase 2.2 完成 | — |

### 提取统计

| 地图 | 确认 ID | 识别名称（缺 ID） | 小计 |
|------|:--:|:--:|:--:|
| 个人修炼 | 12 | 1 | ~13 |
| 管理修炼 | 3 | 14 | ~17 |
| 创业修炼 | 2 | 21 | ~23 |
| 无限修炼 | 0 | 3 | ~3 |
| **合计** | **17** | **39** | **~56** |

### 质量检查

| 检查项 | 结果 |
|--------|:--:|
| 四张地图课程清单完整提取（从 3724 行 ASR） | ✅ |
| 已确认 course_id 与源文件口播一致 | ✅ |
| 缺失 course_id 标注 ⚠️ 待查 | ✅ |
| 课程归属地图交叉验证（串讲上下文） | ✅ |
| Phase 2 Step 2.2 checkbox 标记完成 | ✅ |
| 提取总结含关键发现和下一步 | ✅ |

### 关键发现

1. ASR 转录的局限性：Trumen 大量使用互动口令代替编号口播，仅 ~30% 课程有明确 ID
2. 完整的 ~120 门方法课清单需从一堂选课中心/实体大地图补全
3. 案例课（~80 门）本次串讲未逐一列举，需 Phase 3c 单独处理

### 已知延后

| 项 | 原因 |
|----|------|
| ~60 门课程 course_id 补全 | 需访问一堂选课中心或实体大地图 |
| 案例课 ~80 门清单 | 不在本次串讲范围（串讲只覆盖方法课） |
| 421 编号归属确认（总图列在个人地图 vs ASR 出现在管理段） | ASR 噪声，需选课中心交叉验证 |
