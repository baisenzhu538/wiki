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
| **Architect** | 审查产出、提炼选项、记录决策 | 与 Builder 在同一文件内 append | 仅当与 Builder 无法达成共识时 |
| **Builder** | 执行 KDO 流水线 | 在 Architect 评估文件内 append 回应 | 不主动发起架构讨论 |

核心原则：Architect + Builder 的辩论不消耗用户注意力。达成共识的事项直接执行。
