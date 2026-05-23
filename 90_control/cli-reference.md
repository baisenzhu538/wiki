# KDO CLI 完整参考

> 本文件从 CLAUDE.md 中抽离，按需 Read。不需要每轮加载。

## CLI 速查

| 命令 | 用途 |
|------|------|
| `kdo init [path]` | 初始化 KDO 工作空间 |
| `kdo capture <input> [--title] [--kind]` | 捕获文本/URL/文件到 00_inbox |
| `kdo fetch-url <url> [--title] [--timeout]` | 抓取 URL 并提取文本到 00_inbox/links |
| `kdo import-chat <path> [--title] [--format]` | 导入 AI 对话到 00_inbox/ai-chats |
| `kdo ingest [--limit N] [--dry-run] [--title] [--kind]` | 编译 inbox → raw sources + wiki 骨架 |
| `kdo enrich [--wiki-path] [--all] [--dry-run]` | 自动填充 wiki 骨架中的 TODO 占位 |
| `kdo query <question> [--limit N]` | 语义+图检索（LightRAG），回退到 BM25 → 关键词 |
| `kdo graph rebuild` | 重建 Graph RAG 索引（内容变更后运行） |
| `kdo graph query <question> [--json]` | 直接查 Graph RAG，输出实体+关系+chunks |
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
| `kdo lint [--strict] [--baseline <ref>] [--diff] [--accept-baseline] [--structure-report]` | 检查工作空间结构完整性 |
| `kdo backup [--output <dir>]` | 备份 KDO 源码到 zip |
| `kdo cards [--type] [--domain] [--has] [--missing] [--count]` | 按条件列出/统计概念卡片 |
| `kdo status` | 显示工作空间库存盘点 |
| `kdo clean-transcript <path> [--rules]` | 清理口述稿 |
| `kdo ocr <path> [--capture] [--method] [--lang] [--pages]` | MinerU 深度文档解析 |
| `kdo video <subcommand>` | 视频资产管理 |

## 完整工作流

### Ingest `[文件描述]`

1. **格式检查**：`kdo ingest` 只处理 `.md`。`.docx`/`.pdf` 先转换。
2. **kdo ingest**：创建 `10_raw/sources/` 副本 + `30_wiki/concepts/` 骨架。
3. **三步编译法**：Condense → Question → Synthesize，填充 TODO。
4. **kdo enrich --all**：自动补填剩余 TODO。
5. **日志更新**：`30_wiki/log.md` + `30_wiki/index.md`。

### Query `[问题]`

1. `kdo query "<问题>"` 语义+图检索。
2. 查阅 `30_wiki/` 和 `10_raw/` 相关内容。
3. 用 `[[双向链接]]` 引用概念。
4. 新见解写入 `30_wiki/`。

### Produce `[类型]` `[主题]`

1. `kdo query "<主题>"` 确认 wiki/source 覆盖。
2. `kdo produce <type>/<subtype> --topic "<主题>" --target-user "<目标用户>" --channel <渠道>`。
3. `kdo brief --artifact-id <id>` 获取上下文。
4. 填充 TODO，引用 source_id。
5. `kdo validate <artifact_id>` 通过检查。

### Ship `[artifact_id]`

1. `kdo validate <artifact_id>` 确保通过。
2. `kdo ship <artifact_id> --channel <channel> [--url]`。
3. `kdo feedback "<observation>" --kind comments --artifact-id <id>`。

### Lint

1. `kdo lint` 检查结构。
2. `kdo validate --write-report` 检查 artifact 质量。
3. 检查 `30_wiki/contradictions.md`。
4. `kdo improve` 生成改进计划。

## 内置能力 (Skills)

| Skill | 路径 | 用途 |
|-------|------|------|
| Knowledge Curator | `40_outputs/capabilities/skills/knowledge-curator/SKILL.md` | Capture → ingest → wiki enrichment |
| Delivery Producer | `40_outputs/capabilities/skills/delivery-producer/SKILL.md` | Wiki knowledge → shipped artifact |
| System Linter | `40_outputs/capabilities/skills/system-linter/SKILL.md` | Workspace health check |
| Image OCR | `40_outputs/capabilities/skills/image-ocr/SKILL.md` | PaddleOCR v5 中文图片文本提取 |
| Design Prompt Iteration | `40_outputs/capabilities/skills/design-prompt-iteration/SKILL.md` | 视觉反馈 → prompt 修改 |

## 本地工具

| 工具 | 命令 |
|------|------|
| OCR 单张 | `powershell 40_outputs/capabilities/skills/image-ocr/ocr-image.ps1 <image>` |
| OCR 批量 | `powershell 40_outputs/capabilities/skills/image-ocr/ocr-image.ps1 "*.png" -Batch` |
| OCR 直接 | `node C:\Users\Administrator\ocr-pipeline\ocr-paddle.cjs <image>` |

> OCR 运行时在 `C:\Users\Administrator\ocr-pipeline\`（不进 git）。

## 内置工作流

| Workflow | 路径 |
|----------|------|
| Daily Capture Flow | `40_outputs/capabilities/workflows/daily-capture-flow.md` |
| Produce and Ship Flow | `40_outputs/capabilities/workflows/produce-and-ship-flow.md` |
| Feedback Improve Flow | `40_outputs/capabilities/workflows/feedback-improve-flow.md` |

## 质量门

- **Content**: 目标读者明确、核心论点明确、结构完整、声明有源可溯、反馈路径已声明。
- **Code**: 安装路径已记录、使用示例存在、验证步骤存在、失败模式已命名、版本/发布路径已声明。
- **Capability**: 任务边界明确、输入输出明确、工具权限已声明、失败处理已记录、评测案例存在或已计划。

## 工作空间目录结构

```
00_inbox/              ← 低摩擦捕获入口
10_raw/                ← 不可变原始资料（kdo ingest 创建）
20_memory/             ← 跨会话连续性记忆
30_wiki/               ← 编译后的可复用知识层
  concepts/            ← 知识卡片（三步编译法产出）
  entities/            ← 人/公司/组织
  systems/             ← 系统架构
  index.md / log.md / contradictions.md
40_outputs/            ← 交付物（content/code/capabilities）
50_delivery/           ← 发布记录
60_feedback/           ← 反馈信号
70_product/            ← 产品执行层（tasks/projects/roadmaps）
90_control/            ← 控制面板（schemas/workflows/quality-gates）
.kdo/state.json        ← 机器状态
```
