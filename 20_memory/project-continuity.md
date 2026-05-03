# Project Continuity

## Session 2026-05-03 Evening

**Human**: Linhai Zhu
**Context**: KDO vault 结构评审 + 多库架构咨询

### Key Decisions Made

1. **Vault Architecture: 1 + N (Deferred)**
   - 当前阶段**不拆多库**，采用单库 + 文件夹前缀隔离 + Workspaces Plus 工作区方案
   - 三个领域文件夹：`_master/`（通用方法论）、`_healthcare/`（医疗信息化）、`_ai-saas/`（AI产品与组织方法论）
   - 未来当单一领域超过 500 篇笔记或客户数据有强合规隔离需求时，再物理拆库

2. **单库内隔离方案**
   - 使用下划线前缀 `_` 让领域文件夹排在文件树顶部
   - 安装 Workspaces Plus 插件，预设三个工作区快速切换（零加载摩擦）
   - 跨领域搜索可用 `path:(_healthcare)` 等语法过滤

3. **Obsidian 切换 Vault 的真实成本**
   - 原生切换需重新加载（2-5秒），打断心流
   - 如未来必须拆库，使用 Obsidian URI + AutoHotkey 快捷键降低摩擦
   - 软链接方案（Symlink）风险高，不推荐

4. **Wiki 健康度评审结论（Pending Actions）**
   - 20_memory/ 之前全是占位符，本次开始填充
   - 12 sources ingested / 0 fully enriched —— enrich 链路是最大瓶颈
   - 8/10 artifacts 为空壳，draft < 200 字不应 ship
   - 14 broken wikilinks 待修复
   - 8 个旧 improvement plan 未标记 superseded
   - 紫鲸AI重复页面已发现一个标记为 superseded，但 index.md 中仍列出

### Next Session Priorities (由 Human 决定启动)

- [ ] 设计单库内的 `_master` / `_healthcare` / `_ai-saas` 文件夹结构并迁移现有文件
- [ ] 配置 Workspaces Plus 的三个工作区
- [ ] 完成 1 个 wiki 页面的完整 enrich（推荐：互联网医院或鑫港湾HIS）
- [ ] 修复 14 个 broken wikilink
- [ ] 标记 8 个旧 plan 为 superseded
- [ ] 给 contradictions.md 写第一条真矛盾（YC 去人力化 vs 街顺重人力客服）

### Open Questions

- 用户是否接受单库 + 工作区方案？（已口头确认）
- 医疗客户数据是否有合规隔离的硬需求？（当前判断：暂无，未来可能出现）
