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

6. **格式门禁通过不代表卡片合格——理解门禁是欧阳锋审查的硬标准**
   - `kdo lint`、`source_refs` 非空、`related` 非空只能检测格式，检测不到"搬运 vs 理解"。
   - 每张卡必须包含 `## Constraints & Boundaries` 节，且每条 constraint 满足：具体场景 + 解释了为什么在该场景下失效 + 可验证的失败症状。
   - 欧阳锋审查时随机抽检 2-3 张卡，只读 Constraints 节，用三个信号判定：
     - **反例具体性**：有具体场景和失效机制，而非"需要灵活运用"的万金油
     - **案例筛选**：从素材中挑了最有区分度的案例（能说明该工具独特价值），而非课程里最早出现的
     - **跨域连接**：Synthesis 的连接有实质说明（为什么相关、何时组合用），而非薄标签
   - 发现"格式完整但思维空洞"（无 Constraints 节、Claims 纯摘录、无反例、无案例筛选）→ 返工。
   - 此标准适用于所有新卡建设和旧卡重写，不分域。参见 C-8。
