# AGENTS.md

You are operating inside a Knowledge Delivery OS workspace.

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

当前工作空间有三个操作角色，协作规则定义在 `90_control/debate-protocol.md`：

| 角色 | 职责 | 内部辩论 | 用户介入点 |
|------|------|---------|-----------|
| **用户** | 定方向、定优先级、定角度 | 不参与 | 只做 ≤3 选项的选择题 |
| **Architect（欧阳锋）** | 审查产出、提炼选项、记录决策 | 与黄药师在同一文件内 append | 仅当与黄药师无法达成共识时 |
| **黄药师（Builder）** | 高质量内容提炼/KDO开发/执行流水线 | 在 Architect 评估文件内 append 回应 | 不主动发起架构讨论 |

核心原则：Architect + 黄药师的辩论不消耗用户注意力。达成共识的事项直接执行。Architect 的唯一执行接口是黄药师。

### 疑问传递机制

欧阳锋和黄药师不在同一对话实例中，通过 vault 文件异步传递疑问：

```
黄药师有疑问
  → 在被质疑的文件末尾 append，格式： ## 黄药师疑问（日期）
  → 用户通知欧阳锋："黄药师在 xx文件 留了疑问"
  → 欧阳锋在同一文件末尾 append 回应
  → 用户通知黄药师："欧阳锋在 xx文件 回应了"
```

**规则：**
1. 所有疑问留在**被讨论的那个文件里**，不开新文件
2. 用固定标题：`## 黄药师疑问（日期）` 或 `## 欧阳锋回应（日期）`
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

完整失败模式库：`90_control/failure-modes.md`。下一个 Agent session 启动时必读。
