# Project Continuity

## Session 2026-05-03 Evening

**Human**: Linhai Zhu
**Context**: KDO vault 结构评审 + 多库架构咨询

### Key Decisions Made (历史记录 — 部分已被用户终决覆盖)

> **注意：** 以下第 1、2 项的文件夹前缀方案已被用户否决。最终决策见下方 `## 最终定案` 章节。

1. ~~**Vault Architecture: 1 + N (Deferred)**~~
   ~~- 当前阶段**不拆多库**，采用单库 + 文件夹前缀隔离 + Workspaces Plus 工作区方案~~
   ~~- 三个领域文件夹：`_master/`（通用方法论）、`_healthcare/`（医疗信息化）、`_ai-saas/`（AI产品与组织方法论）~~
   ~~- 未来当单一领域超过 500 篇笔记或客户数据有强合规隔离需求时，再物理拆库~~
   → **被用户否决，改用 domain 字段方案。详见下方最终定案。**

2. ~~**单库内隔离方案**~~
   ~~- 使用下划线前缀 `_` 让领域文件夹排在文件树顶部~~
   ~~- 安装 Workspaces Plus 插件，预设三个工作区快速切换~~
   ~~- 跨领域搜索可用 `path:(_healthcare)` 等语法过滤~~
   → **被用户否决。不装 Workspaces Plus，不用前缀目录。**

3. **Obsidian 切换 Vault 的真实成本**
   - 原生切换需重新加载（2-5秒），打断心流
   - 如未来必须拆库，使用 Obsidian URI + AutoHotkey 快捷键降低摩擦
   - 软链接方案（Symlink）风险高，不推荐
   → **仍有效，但与当前 domain 方案无关。**

4. **Wiki 健康度评审结论（历史记录）**
   - 20_memory/ 之前全是占位符，本次开始填充
   - 12 sources ingested / 0 fully enriched — 已由 Builder 后续 session 解决，enrich 链路已突破 0
   - 8/10 artifacts 为空壳 — 部分已由 Builder 填充，部分仍待完成
   - 14 broken wikilinks 待修复 — 状态未知，需重新审查
   - 8 个旧 improvement plan 未标记 superseded — 已由 Builder 处理
   - 紫鲸AI重复页面已处理
   → **多数项已过时。当前状态应以最新评估文件为准。**

---

## 用户最终定案（2026-05-03）

**背景：** 另一 agent session 提议了文件夹前缀方案 + Workspaces Plus。用户评估后选择了更轻量的方案。

| 维度 | 原提议（被否决） | 最终决策 |
|------|----------------|---------|
| 领域隔离方式 | 下划线前缀目录 `_master/` `_healthcare/` `_ai-saas/` | frontmatter `domain:` 字段 |
| 例 | `30_wiki/_master/一堂调研方法论.md` | `domain: master` |
| 跨域标签 | 不支持 | `domain: ['master', 'ai-saas']` |
| 工作区切换 | Workspaces Plus 插件 | **不安装插件**，用 Dataview 按 domain 过滤 |
| 现有文件 | 需搬迁到新目录 | **不动目录**，只加一行 frontmatter |
| 执行人 | 未定 | 黄药师（已完成 ✅ 2026-05-03） |

---

### Next Session Priorities (由 Human 决定启动)

- [ ] 调研方法论 artifact 填充（角度已定：面向创业者的实操指南，等 Builder 执行）
- [ ] 继续 enrich 下一批一堂课程
- [ ] 修复 broken wikilink（上次排查 14 个，需重新审查当前数量）
- [ ] 给 contradictions.md 写第一条真矛盾
