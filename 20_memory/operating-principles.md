# Operating Principles

## KDO Vault 运作原则

1. **先 Enrich 后 Produce**
   - 禁止在 wiki 知识卡片未完成 Condense / Critique / Synthesis 三步编译法前，进入 Produce 阶段生成 artifact。
   - 空壳 artifact（draft < 200 字）禁止标记为 ready 或 ship。

2. **源文件是唯一真相源**
   - `10_raw/` 和 `00_inbox/` 只读不改。
   - Wiki 是编译后的知识层，所有重要声明必须可追溯到 source_id。

3. **单库优先，物理拆库需触发条件**
   - 默认在单库内用 frontmatter `domain:` 字段标记领域归属。**不使用文件夹前缀方案。**
   - domain 值分三类：`master`（通用方法论）、`ai-saas`（AI 产品）、`healthcare`（医疗信息化）。
   - 跨领域页面使用数组：`domain: ['master', 'ai-saas']`。
   - 使用 Dataview 按 domain 过滤查询，不依赖目录结构隔离。
   - 仅当单一领域超过 500 篇笔记，或客户数据有强合规隔离需求时，才物理拆库。
   - 拆库后，90_control/ 的核心文件以主库为唯一真相源。

4. **跨会话连续性依赖 20_memory/**
   - 每次会话开始时读取 `20_memory/` 全部文件加载上下文。
   - 关键决策、待办事项、用户偏好必须写入持久化文件，而非仅依赖对话历史。

5. **结构变更须建议先行**
   - 自动变更目录结构、重命名文件、批量修改 frontmatter 前，必须先向用户提议并获批准。
   - 例外：修复 broken wikilink、补充缺失的 frontmatter 字段、标记 superseded 等低风险操作。
