# CLAUDE.md

**!!! 启动第一个动作：Read `.agent/context.md` → `.agent/pitfalls.md` → `.agent/toolkit.md`。!!!**

**!!! 每次会话快结束时：必须 Update `.agent/context.md`（更新 active_task、进度、blockers），有新坑追加到 `pitfalls.md`。!!!**

**禁止用 Claude Code `/memory` 替代 `.agent/` 文件**。`/memory` 是工具私有记忆，换电脑/换工具就丢。`.agent/` 是项目公共记忆，跟着 git 走。后者是唯一真相源。

## 关键路径

| 用途 | 路径 |
|------|------|
| Vault 根目录 | `C:\Users\Administrator\Desktop\wiki\` |
| KDO CLI 源码 | `C:\Users\Administrator\Knowledge Delivery OS 0.0.1\kdo\` |

## 新 Agent 入职指引

### Step 1 — 读规则

| 文件 | 内容 |
|------|------|
| `90_control/kdo-industrialization-manual.md` | 内容工厂的工业化手册——质量门禁、铁律、防呆、失败模式 |
| `90_control/tool-card-excellence-standard.md` | Tool Card 卓越标准——基于 T4（A+）的结构逆向工程 |
| `90_control/AGENTS.md` | 角色分工、禁止清单（必读！已发生过的事故列在禁止清单里） |
| `20_memory/corrections.md` | 走过的弯路，不要重蹈覆辙 |
| `20_memory/operating-principles.md` | 知识库运作原则 |

**Step 1 完成后，消化 Core 层卡片建立知识骨架**：读 `30_wiki/index.md` Core 层的 55 张卡（全部 framework + 主域方法论 + 跨域桥梁 + 系统/目录）。日常任务用 `kdo query "<问题>"` 按需检索 Extended 层卡片，不逐张翻。

### `/new` 接力模式

如果用户用 `/new` 重开会话且第一句指令简短（如"继续"、"领任务"），**跳过以上所有规则文件**。只读 `70_product/tasks/` 下最新任务文件，直接执行。完成后更新 `20_memory/project-continuity.md`。

### Step 2-3 — 认识知识库 + 当前状态

- 概念卡在 `30_wiki/concepts/`（三步编译法：浓缩→质疑→对标）
- 系统架构在 `30_wiki/systems/`
- 当前状态看 `.agent/context.md` + `70_product/tasks/dashboard.md`

### Step 4 — 知道找谁

KDO 知识工厂五角色分工（详见 `90_control/AGENTS.md`）：

| 角色 | 代号 | 职责 |
|------|------|------|
| **用户（决策者）** | — | 定方向、定角度、拍板 |
| **Architect** | 欧阳锋 | 审查全部产出、任务分配、架构决策、质量标准。审而不改 |
| **Builder** | 黄药师 | KDO CLI 开发、质量门、Graph RAG、基础设施。不接卡片量产 |
| **Producer** | 老顽童 | 卡片量产、文章/内容、跨域合成、新域编译。产能主力 |
| **Multimodal** | 洪七公 | 知识→视觉资产、OCR→结构化、图片→prompt |
| **Publisher** | 段王爷 | `kdo ship`→渠道分发、反馈收集、版本发布 |

欧阳锋是唯一协调节点——角色之间不互相派活，都通过欧阳锋中转。

---

## 角色定义

- **研究员 (Researcher)**：从 `10_raw/` 原始资料中提取核心信息，执行三步编译法。
- **图书管理员 (Librarian)**：将整理后的信息归档到 `30_wiki/`，维护 `30_wiki/log.md` 和 `30_wiki/index.md`。
- **知识仲裁者 (Arbiter)**：检查 `30_wiki/contradictions.md`，解决不同资料间的矛盾。

## 核心原则

- **输入输出分离**：`10_raw/` 和 `00_inbox/` 里的原始文件只读不改。
- **源文件是唯一真相**：wiki 是编译后的知识层，重要声明必须可追溯到源文件。
- **双向溯源**：`source → wiki → artifact` 和 `artifact → source_refs → source → derived_outputs`。
- **KDO 完整流水线**：`capture → ingest → enrich → produce → validate → ship → feedback → improve`
- **零运行时依赖**：纯 Python 标准库，Markdown + JSON + YAML 文本存储。
- **结构变更须建议先行 (suggestion-first)**：自动变更须先提议，等待批准。

## 三步编译法

1. **浓缩 (Condense)**：把原文压缩为 3-5 条核心观点。只保留核心结论和关键证据。
2. **质疑 (Question)**：评估每条结论的前提假设、边界与反例、可靠性（高/中/低，附理由）。
3. **对标 (Synthesize)**：创建与现有卡片的 `双向链接`，标注冲突/互补/可迁移场景。

## 工作流速查

| 指令 | 关键步骤 |
|------|------|
| **Ingest** | 格式检查（.docx/.pdf → Python转.md）→ `kdo ingest` → 三步编译法 → `kdo enrich --all` → 更新 log.md + index.md |
| **Query** | `kdo query "..."`（语义+图检索）→ 查阅 wiki + raw → 用 `双向链接` 引用已有概念 |
| **Produce** | `kdo query` 确认覆盖 → `kdo produce <type>/<subtype> --topic` → 读 `kdo brief` → 填 TODO → `kdo validate` |
| **Ship** | `kdo validate` → `kdo ship --channel` → `kdo feedback` |
| **Lint** | `kdo lint` → `kdo validate --write-report` → 检查 contradictions.md → 孤立页面 → 过时信息 → `kdo improve` |

## 格式规范

- 使用 `[[概念名称]]` 创建内部链接。创建前先检查是否已有同名页面。
- 知识卡片 frontmatter：`title`, `type` (concept/entity/comparison/improvement-plan), `status` (draft/reviewed/stable/needs-review), `source_refs`, `created_at`, `updated_at`。
- `10_raw/sources/` 中的源文件包含 `source_id`、`captured_at`、`kind`、`trust_level`、`freshness`、`rights` 等元数据。

## 工具与能力

> 忘了命令就 `kdo --help` 或 Read `90_control/cli-reference.md`。不需要每轮加载。

- **KDO CLI 完整速查**：`90_control/cli-reference.md` 或 `.agent/toolkit.md`
- **本地工具**（OCR / Git）：见 `.agent/toolkit.md`
- **内置 Skills**：Knowledge Curator / Delivery Producer / System Linter / Image OCR / Design Prompt Iteration
- **内置 Workflows**：`40_outputs/capabilities/workflows/`
- **质量门**：Content（读者+论点+结构+溯源+反馈）/ Code（安装+示例+验证+失败模式）/ Capability（边界+IO+权限+失败+评测）
