---
id: annotation-ai-feature-inventory-research
type: annotation
status: active
source_refs:
  - 00_inbox/人机协作双三角/一堂双三角-人机协作模型-口述.txt
  - 00_inbox/人机协作双三角/_processed/龙虾和skills训练的口述_page001-004_vlm.md
related:
  - '[[concept-yihang-ai-feature-thinking]]'
  - '[[tool-ai-feature-inventory]]'
---

# AI 工具特性清单全网调研入口标注

> 用户追问：Truman 提到上下文工程、提示词、Hermes、龙虾、Codex 都有特性，是否需要建设特性列表并全网调研深挖？
> 答案：是。本标注是 Feature 清单建设的调研入口，先汇总已掌握的公开/内部特性，再开任务做系统深挖。

---

## 一、为什么要做特性清单

Truman 的 Feature 思维（行 1402-1468）要求：

1. **不要盯着工具名字，要盯着最小技术特性**。
2. **所有工具拆完后，一共也就几十个特性**，在这些特性上工作即可。
3. **评估新工具时只问「它多了哪几个 Feature」**。

因此，KDO 需要一张**可维护的 AI 工具特性清单（Feature Inventory）**，把热门工具按特性原子化拆解，而不是每出一个新工具就追一张工具卡。

---

## 二、Truman 在课程中明确提到的特性领域

| 领域 | 原文提示 | 需要深挖的方向 |
|:---|:---|:---|
| **上下文工程** | 「上下文工程里面又有大概 5 到 10 个特性」（行 1420） | 长上下文、RAG、记忆分层、上下文压缩、选择性注入、状态检查点、工具选择等 |
| **提示词工程** | 「提示词工程里面有大概十个左右的特性」（行 1420） | Zero/Few-shot、CoT、Self-Consistency、ReAct、ToT、Meta-prompting、结构化输出、角色约束等 |
| **Hermes** | 作为内部 Agent/自动化系统被提及 | 定时任务、多终端推送、Web 搜索/抓取、Agent 调度、模型切换等 |
| **龙虾 / OpenClaw** | 「龙虾之所以火，是因为它有三四个核心特性」（行 1422） | 个人自动化、多 Agent 协作、Skill 封装、跨工具编排等 |
| **Codex** | 作为 AI 编程 Agent 案例 | 多文件编辑、GitHub 集成、云端沙箱、并行任务、计算机控制、浏览器、动态思考时间等 |

---

## 三、公开资料已识别的特性清单（初稿）

### 3.1 上下文工程特性（Context Engineering）

来源：LangGraph/LangSmith、Vectara、agenta.ai、arXiv 等公开资料。

| 特性 | 说明 | 适用场景 |
|:---|:---|:---|
| **长上下文窗口** | 直接塞入大量文本（200K-1M tokens） | 书籍、合同、长文档 |
| **RAG / 检索增强** | 先切分、检索、再注入相关片段 | 需要来源可追溯的问答 |
| **记忆分层** | 工作记忆 + 情景记忆 + 语义记忆 | 多会话、个性化 Agent |
| **上下文压缩** | 摘要、截断、去噪，降低 token 成本 | 日志、长对话、冗余输入 |
| **滑动窗口 / 注意力沉降** | 保留最近 + 关键初始 token | 流式、长对话 |
| **选择性检索 / 语义工具选择** | 按任务动态选择工具/记忆 | 多工具 Agent |
| **状态检查点 / Checkpointing** | 每一步状态可恢复 | 长程 Agent、容错 |
| **Reflexion / 反思记忆** | 把失败经验写入记忆，避免重犯 | 持续学习型 Agent |
| **层级化摘要** | 按章节/主题逐级压缩 | 结构化长文档 |
| **相关性重排序** | 检索后再排序，提升注入质量 | RAG 优化 |

### 3.2 提示词工程特性（Prompt Engineering）

来源：promptingguide.ai、ml4devs、Towards Data Science 等。

| 特性 | 说明 | 适用场景 |
|:---|:---|:---|
| **Zero-shot** | 无示例直接问 | 通用、简单任务 |
| **Few-shot** | 给 2-5 个示例 | 格式/领域特定任务 |
| **Chain-of-Thought (CoT)** | 要求逐步推理 | 数学、逻辑、规划 |
| **Self-Consistency** | 多次采样投票 | 高 stakes 决策 |
| **ReAct** | Thought → Action → Observation 循环 | 工具使用 Agent |
| **Tree-of-Thoughts (ToT)** | 多路径探索与回退 | 复杂搜索/设计 |
| **Plan-and-Execute** | 先规划再执行 | 多步骤任务 |
| **Meta-prompting** | 让模型自己生成/优化提示词 | 提示词工程不确定时 |
| **Step-back Prompting** | 先抽象一般原理再回答具体问题 | 科学/医疗/复杂问题 |
| **结构化输出 / JSON Mode** | 强制输出格式 | 程序消费、API 调用 |
| **Function Calling / Tool Use** | 模型调用外部函数 | 数据库、搜索、计算 |
| **角色分配 / Role Prompting** | 给模型设定专家身份 | 专业领域输出 |
| **Prompt Chaining** | 多提示词串行/并行 | 复杂生成 pipeline |
| **Dynamic Skill Prompting (DSP)** | 动态选择技能 | 个性化、多任务 |

### 3.3 Codex 特性（公开资料初稿）

来源：OpenAI 官方、Qodo、Dextralabs、FastGPTPlus 等。

| 特性 | 说明 |
|:---|:---|
| **Ask / Code 双模式** | Ask 只读分析，Code 读写执行 |
| **多文件编辑** | 跨文件协调修改 |
| **GitHub 集成** | 理解 PR 上下文、创建 PR |
| **云端沙箱执行** | 独立容器运行代码 |
| **并行任务处理** | 同时处理多个独立任务 |
| **计算机控制** | 直接操作桌面 UI |
| **内置浏览器** | 无需切换应用即可查资料 |
| **图像生成** | 桌面端直接生成图片 |
| **自动化记忆** | 记住偏好和重复任务 |
| **插件支持** | 第三方扩展生态 |
| **动态思考时间** | 根据任务复杂度调整推理时间 |
| **Agent Kit / Responses API** | 构建生产级 Agent 的工具包 |
| **Evals / Trace Grading** | 评估 Agent 决策过程 |
| **Connectors Registry** | 安全连接企业工具 |

### 3.4 龙虾 / OpenClaw 特性（内部资料初稿）

来源：`00_inbox/人机协作双三角/_processed/龙虾和skills训练的口述_page001-004_vlm.md`。

| 特性/能力 | 说明 |
|:---|:---|
| **深度交叉验证式调研** | 不是单次搜索，而是多源交叉验证 |
| **双 AI 并行** | 一个翻译/一个教学，互相校准 |
| **最佳实践拆解** | 把官方教程、市场教程拆成模块并对比 |
| **交叉打分** | 让 AI 对多个教程互相打分，减少幻觉 |
| **引导式系统提示词 + DataPack** | 逻辑放提示词，关键参考放数据包 |
| **YI/YAI 集成** | 配置到 YI 中直接对话测试 |
| **5-7 个里程碑节点** | 把基本功拆成稳定节点 |
| **宽到窄、喜提 6000 级、奥斯卡模型** | 调研方法论的封装 |
| **足够多 Feature 时的优化自信** | 「只要有足够多的 feature 特性，我总能优化上去」 |

> **注意**：龙虾/OpenClaw 的公开资料极少，以上主要基于内部口述稿。需要进一步确认「龙虾」是否等同于「OpenClaw」，以及是否有更多官方文档。

### 3.5 Hermes 特性（内部资料初稿）

来源：`.agent/context.md`、任务文件、`00_inbox/ideas/` 等。

| 特性/能力 | 说明 |
|:---|:---|
| **个人自动化** | 定时任务、多终端推送 |
| **Web 搜索/页面抓取** | 通过 REST API 接入搜索和读取能力 |
| **Agent 调度/运行** | 作为老顽童的生产运行环境 |
| **模型切换/Provider 管理** | 支持 DeepSeek 等模型切换 |
| **CLI/飞书双入口** | 老顽童用 CLI，段王爷用飞书 |
| **批量卡片生产** | 大规模 KDO 卡片生成 |

> **注意**：Hermes 是内部系统，公开资料有限。需要找黄药师/老顽童确认完整特性清单。

---

## 四、当前缺口

| 缺口 | 说明 |
|:---|:---|
| **特性边界不清** | 很多特性有重叠（如 RAG vs 长上下文），需要明确各自适用域。 |
| **内部工具特性不全** | Hermes、龙虾/OpenClaw 的特性清单依赖内部口述，缺少结构化文档。 |
| **缺少组合规则** | 哪些 Feature 常一起用？哪些互相排斥？需要沉淀。 |
| **缺少评估标准** | 如何测试一个 Feature 是否有效？需要 AB 测试方法。 |
| **版本管理** | 模型和工具快速迭代，Feature 清单需要版本化。 |

---

## 五、建议产出

| 产出 | ID | 类型 | 优先级 |
|:---|:---|:---:|:---:|
| AI 工具特性清单 | `tool-ai-feature-inventory` | tool | P0 |
| 上下文工程特性方法卡 | `method-ai-context-engineering-features` | method | P1 |
| 提示词工程特性方法卡 | `method-ai-prompt-engineering-features` | method | P1 |
| Codex 特性工具卡 | `tool-openai-codex-features` | tool | P1 |
| Hermes 特性工具卡 | `tool-hermes-features` | tool | P2 |
| 龙虾/OpenClaw 特性工具卡 | `tool-openclaw-crayfish-features` | tool | P2 |

---

## 六、下一步

1. 启动全网调研任务（#75），系统收集公开资料并验证内部工具特性。
2. 对上下文工程、提示词工程、Codex 做深度 web research。
3. 对 Hermes、龙虾/OpenClaw 找黄药师/老顽童做内部访谈/文档梳理。
4. 产出 `tool-ai-feature-inventory` 和至少 2 张领域特性方法/工具卡。
