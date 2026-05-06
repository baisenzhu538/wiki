# CLAUDE.md

## 新 Agent 入职指引

第一次进入此知识库，按顺序完成以下步骤：

### Step 1 — 读规则

| 文件 | 内容 |
|------|------|
| `90_control/AGENTS.md` | 角色分工、禁止清单（必读！已发生过的事故列在禁止清单里） |
| `90_control/debate-protocol.md` | 协作辩论协议——你和谁怎么沟通 |
| `20_memory/corrections.md` | 走过的弯路，不要重蹈覆辙 |
| `20_memory/operating-principles.md` | 知识库运作原则 |

### Step 2 — 认识知识库

- 概念卡在 `30_wiki/concepts/`（三步编译法，浓缩→质疑→对标）
- 系统架构在 `30_wiki/systems/`（KDO 怎么工作的）
- 所有知识按 `domain:` 标签分三类：`master`（通用方法论）、`ai-saas`（AI 产品）、`healthcare`（医疗）
- Graph RAG 检索层正在建设中，完成后可通过检索层查询关联知识

### Step 3 — 了解当前状态

- `60_feedback/assessments/` 里有最新的体检报告和评估
- `00_inbox/` 里是否有积压素材
- `20_memory/project-continuity.md` 里有项目上下文和待办

### Step 4 — 知道找谁

| 角色 | 职责 | 怎么触发 |
|------|------|---------|
| **用户（决策者）** | 定方向、定角度、拍板 | 直接对话 |
| **欧阳锋（Architect）** | 设计规则、审查产出、技术决策 | 用户在对话中切换 |
| **黄药师（Builder）** | 高质量内容提炼、KDO 开发、执行流水线 | 用户在对话中切换 |

---

## 角色定义

- **研究员 (Researcher)**：从 `10_raw/` 原始资料中提取核心信息，执行三步编译法。
- **图书管理员 (Librarian)**：将整理后的信息归档到 `30_wiki/` 对应页面，维护 `30_wiki/log.md` 和 `30_wiki/index.md`。
- **知识仲裁者 (Arbiter)**：检查 `30_wiki/contradictions.md`，解决不同资料间的矛盾，确保知识库一致性。

## KDO 工作空间结构

```
00_inbox/              ← 入口：低摩擦捕获
  ideas/               ← 文本 / 想法
  links/               ← URL 捕获
  ai-chats/            ← AI 对话导入
  voice-notes/         ← 语音笔记
  screenshots/         ← 截图
10_raw/                ← 不可变原始资料（kdo ingest 自动创建）
  sources/             ← 编译后的 .md 源文件
  web/                 ← 网页存档
  papers/              ← 论文
  transcripts/         ← 转录文本
  meetings/            ← 会议记录
  assets/              ← 二进制附件
20_memory/             ← 跨会话连续性记忆
  user-preferences.md
  project-continuity.md
  corrections.md
  operating-principles.md
30_wiki/               ← 编译后的可复用知识层
  concepts/            ← 抽象概念 / 知识卡片（三步编译法的产出）
  entities/            ← 人 / 公司 / 组织
  projects/            ← 项目知识
  decisions/           ← 决策记录 / 改进计划
  systems/             ← 系统架构知识
  trends/              ← 趋势分析
  index.md             ← 概念索引
  log.md               ← 操作日志
  contradictions.md    ← 矛盾追踪
40_outputs/            ← 交付物：三类资产
  content/             ← articles, videos, audio, tutorials, courses, reports
  code/                ← apps, plugins, templates, scripts, packages
  capabilities/        ← skills, agents, workflows, evals, playbooks
50_delivery/           ← 交付与发布记录
  published/           ← 已发布记录
  briefs/              ← 交接简报纸
  releases/            ← 版本发布
  deployments/         ← 部署记录
  channels/            ← 渠道配置
  analytics/           ← dashboard 输出
60_feedback/           ← 反馈信号
  comments/            ← 评论反馈
  issues/              ← 问题追踪
  usage-logs/          ← 使用日志
  eval-results/        ← 评测结果
  corrections/         ← 纠正记录
70_product/            ← 产品执行层
  projects/            ← 产品项目
  tasks/               ← 执行任务
  connectors/          ← 外部连接器
  roadmaps/            ← 路线图
90_control/            ← 控制面板
  schemas/             ← 模式定义
  workflows/           ← 工作流规则
  quality-gates/       ← 质量门
  AGENTS.md            ← Agent 行为规则
  routing-rules.md     ← 路由规则
  source-registry.yaml ← 源注册表
  artifact-registry.yaml ← 产物注册表
.kdo/                  ← 机器状态
  state.json           ← 核心状态文件
```

## 核心原则

- **输入输出分离**：`10_raw/` 和 `00_inbox/` 里的原始文件只读不改。所有操作结果写入 `30_wiki/`、`40_outputs/`、`60_feedback/`。
- **源文件是唯一真相**：wiki 是编译后的知识层，不是最终真相。重要声明必须可追溯到源文件。
- **双向溯源**：`source → wiki → artifact` 和 `artifact → source_refs → source → derived_outputs`。
- **KDO 完整流水线**：`capture → ingest → enrich → produce → validate → ship → feedback → improve`
- **零运行时依赖**：纯 Python 标准库，Markdown + JSON + YAML 文本存储。
- **结构变更须建议先行 (suggestion-first)**：自动变更须先提议，等待批准。

## 三步编译法

对每条核心结论，按以下结构写入 `30_wiki/concepts/` 的知识卡片：

1. **浓缩 (Condense)**：把原文压缩为 3-5 条核心观点。只保留核心结论和关键证据。
2. **质疑 (Question)**：以 `### [Critique]` 为标题，评估每条结论的：
   - 前提假设
   - 边界与反例
   - 可靠性评估（高 / 中 / 低，附理由）
3. **对标 (Synthesize)**：以 `### [Synthesis]` 为标题，创建：
   - 与 `30_wiki/concepts/` 或 `30_wiki/entities/` 中现有页面的联系，使用 `[[双向链接]]`
   - 与哪些已有概念冲突或互补
   - 可迁移到哪些场景

## 完整工作流

### 指令：Ingest `[文件描述]`

看到新资料在 `00_inbox/` 后：

1. **格式检查**：KDO 的 `kdo ingest` 只处理 `.md`。如遇 `.docx`/`.pdf`，先用 Python 转换为 `.md`（.docx 是 ZIP 包，用 `zipfile` + `xml.etree.ElementTree` 提取 `word/document.xml` 中 `w:t` 元素的文本）。
2. **kdo ingest**：让 KDO 创建 `10_raw/sources/` 副本和 `30_wiki/concepts/` 骨架。
3. **三步编译法**：手动执行 Condense → Question → Synthesize，填充骨架中的 TODO 占位。
4. **kdo enrich --all**：自动补填剩余的 TODO（如有）。
5. **日志更新**：记录到 `30_wiki/log.md` 和 `30_wiki/index.md`。

### 指令：Query `[你的问题]`

1. 运行 `kdo query "<问题>"` 搜索 memory、wiki、outputs 和 raw sources。
2. 查阅 `30_wiki/` 和 `10_raw/` 中的相关内容。
3. 用 `[[双向链接]]` 引用已有概念。
4. 若有新见解，写入 `30_wiki/` 对应页面。
5. 输出到 `40_outputs/` 或直接回答。

### 指令：Produce `[类型]` `[主题]`

1. 运行 `kdo query "<主题>"` 确认有足够 wiki/source 覆盖。
2. 运行 `kdo produce <type>/<subtype> --topic "<主题>" --target-user "<目标用户>" --channel <渠道>`。
3. 读取 `kdo brief --artifact-id <id>` 获取完整上下文。
4. 填充所有 TODO 占位符，引用具体 source_id。
5. 运行 `kdo validate <artifact_id>` 通过所有检查。

### 指令：Ship `[artifact_id]`

1. 运行 `kdo validate <artifact_id>` 确保通过。
2. 运行 `kdo ship <artifact_id> --channel <channel> [--url <url>]`。
3. 记录初始反馈：`kdo feedback "<observation>" --kind comments --artifact-id <id>`。

### 指令：Lint

1. 运行 `kdo lint` 检查工作空间结构和状态一致性。
2. 运行 `kdo validate --write-report` 检查所有 artifact 质量。
3. 检查 `30_wiki/contradictions.md` 中的矛盾记录。
4. 检查孤立页面（无内链指向的页面）。
5. 检查过时信息（超过 30 天无更新的页面）。
6. 运行 `kdo improve` 生成改进计划。

## 格式规范

- 使用 `[[概念名称]]` 创建内部链接。创建前先检查是否已有同名页面。
- 知识卡片 frontmatter：`title`, `type` (concept/entity/comparison/improvement-plan), `status` (draft/reviewed/stable/needs-review), `source_refs`, `created_at`, `updated_at`。
- `10_raw/sources/` 中的源文件包含 `source_id`、`captured_at`、`kind`、`trust_level`、`freshness`、`rights` 等元数据。

## KDO CLI 速查

| 命令 | 用途 |
|------|------|
| `kdo init [path]` | 初始化 KDO 工作空间 |
| `kdo capture <input> [--title] [--kind]` | 捕获文本/URL/文件到 00_inbox |
| `kdo fetch-url <url> [--title] [--timeout]` | 抓取 URL 并提取文本到 00_inbox/links |
| `kdo import-chat <path> [--title] [--format]` | 导入 AI 对话到 00_inbox/ai-chats |
| `kdo ingest [--limit N] [--dry-run]` | 编译 inbox → raw sources + wiki 骨架 |
| `kdo enrich [--wiki-path] [--all] [--dry-run]` | 自动填充 wiki 骨架中的 TODO 占位 |
| `kdo query <question> [--limit N]` | 关键词搜索 memory/wiki/outputs/raw |
| `kdo produce <content\|code\|capability>/<subtype> --topic <topic>` | 创建 artifact 骨架到 40_outputs |
| `kdo validate [artifact_id] [--advisory] [--write-report]` | 按质量门校验 artifact |
| `kdo ship <artifact_id> --channel <channel> [--url]` | 记录交付事件到 50_delivery |
| `kdo feedback <text> [--kind] [--artifact-id]` | 记录反馈信号到 60_feedback |
| `kdo improve [--output] [--print] [--apply]` | 从反馈生成改进计划到 30_wiki/decisions |
| `kdo brief --topic <topic> \| --artifact-id <id>` | 生成交接简报纸到 50_delivery/briefs |
| `kdo eval <capability_artifact_id> --input --expected [--actual]` | 记录/评分 capability 评测 |
| `kdo project <name> [--goal] [--set-status] [--set-stage]` | 产品项目管理 |
| `kdo task <title> [--project-id] [--priority] [--done]` | 产品任务管理 |
| `kdo connector <name> [--kind] [--target] [--run]` | 外部连接器管理 |
| `kdo dashboard [--output] [--view] [--serve]` | 生成静态 HTML dashboard |
| `kdo lint [--strict]` | 检查工作空间结构完整性 |
| `kdo status` | 显示工作空间库存盘点 |

## 内置能力 (Built-in Skills)

| Skill | 路径 | 用途 |
|-------|------|------|
| Knowledge Curator | `40_outputs/capabilities/skills/knowledge-curator/SKILL.md` | Capture → ingest → wiki enrichment |
| Delivery Producer | `40_outputs/capabilities/skills/delivery-producer/SKILL.md` | Wiki knowledge → shipped artifact |
| System Linter | `40_outputs/capabilities/skills/system-linter/SKILL.md` | Workspace health check and improvement plan |
| **Image OCR** | `40_outputs/capabilities/skills/image-ocr/SKILL.md` | 从图片提取中文文本（本地 PaddleOCR v5） |

## 本地工具 (Local Tools)

这些不在 KDO 管线内，但可在需要时直接调用：

| 工具 | 路径 | 用途 |
|------|------|------|
| OCR 单张 | `powershell 40_outputs/capabilities/skills/image-ocr/ocr-image.ps1 <image>` | 提取单张图片中文文本→ `*_paddle_ocr.txt` |
| OCR 批量 | `powershell 40_outputs/capabilities/skills/image-ocr/ocr-image.ps1 "*.png" -Batch` | 批量处理 |
| OCR 直接 | `node C:\Users\Administrator\ocr-pipeline\ocr-paddle.cjs <image>` | Node.js 直接调用 |

> **OCR 运行时在 wiki 外面**：`C:\Users\Administrator\ocr-pipeline\`（models ~20MB + node_modules ~670MB，不进 git）。
> **关键教训**：dict 索引不能 filter 空行。

## 内置工作流 (Built-in Workflows)

| Workflow | 路径 | 用途 |
|----------|------|------|
| Daily Capture Flow | `40_outputs/capabilities/workflows/daily-capture-flow.md` | 每日输入捕获和摄入会话 |
| Produce and Ship Flow | `40_outputs/capabilities/workflows/produce-and-ship-flow.md` | 知识 → artifact → 交付管线 |
| Feedback Improve Flow | `40_outputs/capabilities/workflows/feedback-improve-flow.md` | 反馈分流和改进周期 |

## 质量门 (Quality Gates)

- **Content**: 目标读者明确、核心论点明确、结构完整、声明有源可溯、反馈路径已声明。
- **Code**: 安装路径已记录、使用示例存在、验证步骤存在、失败模式已命名、版本/发布路径已声明。
- **Capability**: 任务边界明确、输入输出明确、工具权限已声明、失败处理已记录、评测案例存在或已计划。

## 启动确认

配置完成后，说"你是谁"，应列出：研究员、图书管理员、知识仲裁者 三个角色，并确认 KDO 工作空间路径。
