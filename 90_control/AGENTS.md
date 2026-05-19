# AGENTS.md

You are operating inside a Knowledge Delivery OS workspace.

## 关键路径

| 用途 | 路径 |
|------|------|
| **Obsidian Vault** | `C:\Users\Administrator\Desktop\wiki\` |
| **KDO CLI 源码** | `C:\Users\Administrator\Knowledge Delivery OS 0.0.1\kdo\` |
| **KDO CLI 入口** | `C:\Users\Administrator\Knowledge Delivery OS 0.0.1\kdo\cli.py` |
| **OCR Pipeline** | `C:\Users\Administrator\ocr-pipeline\` |

## Prime Directive

Turn inputs into durable knowledge, then into deliverable assets. Never treat the wiki as the source of truth; raw sources are the source of truth.

## Routing Rules

- One-off expression -> `40_outputs/content/`.
- Cross-session facts and user preferences -> `20_memory/`.
- Reusable knowledge -> `30_wiki/`.
- Original source material -> `10_raw/`.
- Executable utilities and templates -> `40_outputs/code/`.
- Repeatable intelligent workflows -> `40_outputs/capabilities/`.
- Feedback, failures, comments, and corrections -> `60_feedback/`.

## Structural Change Policy

Structural changes are suggestion-first:

1. Explain what should move or change.
2. Identify affected files.
3. Explain why the current structure is insufficient.
4. Wait for human approval before making broad reorganizations.

## Source Discipline

- Important claims need source references.
- Conflicts should be recorded, not silently merged.
- Derived pages should link back to source IDs.
- If a source is stale, mark the derived page stale rather than hiding the issue.

## Output Discipline

Every deliverable needs an Artifact Spec with:

- artifact_id
- type
- title
- target_user
- source_refs
- wiki_refs
- definition_of_done
- status
- delivery_channel
- feedback_source

## Built-in Skills

Three skills are registered at workspace init (`origin: builtin`).
Use them directly — they do not need source_refs or wiki_refs.

| Skill file | Purpose |
| --- | --- |
| `40_outputs/capabilities/skills/knowledge-curator/SKILL.md` | Capture → ingest → wiki enrichment |
| `40_outputs/capabilities/skills/delivery-producer/SKILL.md` | Wiki knowledge → shipped artifact |
| `40_outputs/capabilities/skills/system-linter/SKILL.md` | Workspace health check and improvement plan |

## Built-in Workflows

Three workflow documents are available at workspace init.
They orchestrate the built-in skills and define the standard operating cadence.

| Workflow file | Purpose |
| --- | --- |
| `40_outputs/capabilities/workflows/daily-capture-flow.md` | Daily input capture and ingestion session |
| `40_outputs/capabilities/workflows/produce-and-ship-flow.md` | Knowledge → artifact → delivery pipeline |
| `40_outputs/capabilities/workflows/feedback-improve-flow.md` | Feedback triage and improvement cycle |

Feedback routing rules live at `90_control/workflows/feedback-routing-rules.md`.

## 角色协作协议

KDO 知识工厂五角色分工，协作规则定义在 `90_control/debate-protocol.md`：

### 五角色总览

| 角色 | 代号 | 职责 | 执行接口 |
|------|------|------|---------|
| **用户** | — | 定方向、定优先级、定角度。只做 ≤3 选项的选择题 | 直接对话 |
| **Architect** | 欧阳锋 | 审查全部产出、任务分配与协调、架构决策、质量标准制定。审而不改 | 通过 vault 文件异步派发工单 |
| **Builder** | 黄药师 | KDO CLI 开发、质量门自动化、Graph RAG、基础设施。不接卡片量产 | WSL tmux `claude`，顺序执行工单 |
| **Producer** | 老顽童 | 卡片量产、文章/内容产出、跨域合成、新域编译。产能主力 | 飞书 Hermes agent，顺序执行任务队列 |
| **Multimodal** | 洪七公 | **多模态知识仲裁者**——主业：知识→视觉资产（信息图/Excalidraw/SVG/视频/音频）；副业：VA 过程中发现源文件与编译物的归属错位/不一致，反馈给欧阳锋。只标记差异+建议修正方向，不自行修改卡片主体结构 | 飞书 Hermes agent，从 dashboard 领任务，产出写入固定输出路径 |
| **Publisher** | 段王爷 | 发布管线——`kdo ship`→渠道分发、反馈收集→`60_feedback/`、版本发布记录 | 待定义 |

### 协作流程

```
用户定方向
  ↓
欧阳锋（审查+协调）
  ├── 黄药师 ← 工厂建设工单（基础设施）
  ├── 老顽童 ← 内容生产工单（卡片/文章）
  ├── 洪七公 ← 多模态工单（视觉/设计输出）
  └── 段王爷 ← 发布工单（分发/反馈）
```

核心原则：欧阳锋是唯一协调节点。角色之间不互相派活——都通过欧阳锋中转。

### 各角色输入/输出路径（固定，不可混用）

每个角色从固定路径接收任务和工作素材，产出写入固定路径。不跨角色翻别人的输出目录找活干。

| 角色 | 接收任务 | 工作素材 | 知识/内容产出 | 视觉/代码产出 | 勘误/反馈 |
|------|---------|---------|-------------|-------------|----------|
| **欧阳锋** | 用户指令 + 全员产出 | — | `70_product/tasks/` 任务文件 + `.agent/` 决策记录 | — | 审查结论写入对应任务文件 |
| **老顽童** | `70_product/tasks/laowantong-next-tasks.md` | `00_inbox/` 新素材 → `10_raw/sources/` 已 ingest 素材 | `30_wiki/concepts/` 知识卡片 + `40_outputs/content/articles/` 文章 | `40_outputs/capabilities/skills/` 操作手册类 skill | 编译中发现问题 → 卡片内注释 + `60_feedback/corrections/` |
| **黄药师** | `70_product/tasks/huangyaoshi-next-tasks.md` | KDO CLI 源码（外部目录） | `90_control/` 方法论/标准/质量门文档 | `kdo/` 代码 + `70_product/tasks/` 工单 | pytest 结果 + CLI 日志 → `70_product/tasks/` 对应工单 |
| **洪七公** | `70_product/tasks/dashboard.md` 洪七公任务区 | `30_wiki/concepts/` 待可视化卡片 + `10_raw/assets/` 原图/截图 | **静态视觉**：`40_outputs/content/images/infographics/`（信息图/Excalidraw/SVG/ASCII/VA报告）**动态视觉**：`40_outputs/content/videos/`（视频/动画/ASCII视频/后期）**音频**：`40_outputs/content/audio/`（TTS播客/AI音乐/可视化）**演示**：`40_outputs/content/presentations/`（PPT）**网页**：`40_outputs/code/templates/` | `40_outputs/capabilities/skills/` 自建多模态 skill | 归属错位/视觉不一致 → `60_feedback/corrections/`（不改卡片主体） |
| **段王爷** | `70_product/tasks/dashboard.md` 段王爷任务区 | `40_outputs/` 中待发布 artifact | `50_delivery/` 发布记录 | `50_delivery/channels/` 渠道配置 | 外部反馈 → `60_feedback/comments/` + `60_feedback/issues/` |

**查找规则**：
- 想知道谁在做什么 → 看 `dashboard.md`
- 想要老顽童/黄药师的产出 → 去他们的产出路径找
- 想要洪七公的视觉资产 → `40_outputs/content/images/infographics/`
- 想要洪七公的勘误 → `60_feedback/corrections/`
- 想要段王爷的发布状态 → `50_delivery/`
- 角色间疑问 → 异步疑问传递机制（见下节）

### 异步疑问传递机制

各角色不在同一对话实例中，通过 vault 文件异步传递疑问：

```
某角色有疑问
  → 在被质疑的文件末尾 append，格式： ## {角色名}疑问（日期）
  → 用户通知欧阳锋："{角色}在 xx文件 留了疑问"
  → 欧阳锋在同一文件末尾 append 回应
  → 用户通知对应角色："欧阳锋在 xx文件 回应了"
```

**规则：**
1. 所有疑问留在**被讨论的那个文件里**，不开新文件
2. 用固定标题：`## {角色名}疑问（日期）` 或 `## 欧阳锋回应（日期）`
3. 用户只传一句话："去 xxx文件看回复"，不需要转发内容
4. 达成共识后，双方确认并将结论更新到表格或决策记录中

## 禁止清单

以下操作已造成过实际事故。违反前请确认你理解了对应的失败模式。

| 编号 | 禁止行为 | 失败模式 | 正确做法 |
|:----:|----------|----------|----------|
| 1 | **不准对中文内容执行 `kdo enrich`** | F-KDO-001 | 中文页面走 Agent 三步编译（浓缩→质疑→对标），不要调用 `kdo enrich --all` |
| 2 | **不准在非 wiki 根目录执行 pipeline 命令** | F-KDO-004 | 始终 `cd /mnt/c/Users/Administrator/Desktop/wiki` 后执行 |
| 3 | **不准用 `kdo ingest` 处理 .txt 文件** | F-KDO-002 | 先 `cp file.txt file.md` 转换后再 ingest |
| 4 | **不准删除 feedback 文件不同步清理 state.json** | F-KDO-005 | 删除 `60_feedback/` 下文件时，同步从 `.kdo/state.json` 的 `feedback` 列表中移除 |
| 5 | **不准在 state.json 被其他进程持有时执行写操作** | F-KDO-003 | 执行 `improve --apply` 前确认没有并发的 kdo 进程 |
| 6 | **不准在 AGENTS.md 中只写"应该做什么"不写"不准做什么"** | — | 新增约束必须同时写入本禁止清单 |
| 7 | **不准一次性给黄药师派 ≥3 个独立任务** | F-KDO-012 | 单轮只发一个任务（≤5 分钟完成），完成后再发下一个。大任务拆成多个 `--new` 会话接力 |

完整失败模式库：`90_control/failure-modes.md`。下一个 Agent session 启动时必读。

## 工业化规范

KDO 知识生产的完整工业化标准定义在 `90_control/kdo-industrialization-manual.md`（内容工厂的工业化手册，对标 EC 工业化规范手册 v2.8.0）。内容包括：
- 三层质量门禁（L1 结构完整性 / L2 内容质量 / L3 管线一致性）
- 22 条铁律（KF-001~022，含高密度素材专用 KF-019~022）
- 管线阶段门禁（标准+复合编译变体）与举证标准
- 高密度素材复合编译规范（§十二）与 Visual Analysis 五维分析法
- 模板系统（标准版/精简版/复合版）与反馈闭环
- 技术笔记（BOM/CRLF 修复等）

所有 Agent 在执行 enrich/produce/validate 操作前应参考该手册的质量标准。
