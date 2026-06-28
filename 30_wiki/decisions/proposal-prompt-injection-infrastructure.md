---

title: 提案：提示词自动注入体系 — 从手动Read到运行时自动加载
type: improvement-plan
status: draft
domain: master
created_at: 2026-06-02
updated_at: '2026-06-16'
target_roles:
- src_unknown
- src_unknown
reviewer: 待定
related:
  - [[tool-yitang-job-intelligence-research]]
  - [[agent-ecosystem-design]]
  - [[meta-prompt-eng]]
  - [[design-ai-image-generation]]
  - [[ai-short-drama-framework-three-axes]]
  - [[plan_20260531_data-curator-v1.3]]
id: proposal-prompt-injection-infrastructure
author: unknown
source_context: KDO improvement plan — internal process record （原始 source 无法追溯，已标记为
  src_unknown，待后续补充）
source_refs:
- src_unknown
reviewed_by: pending
confidence: 0.6
trust_level: low
---# 提案：提示词自动注入体系

> **触发**：2026-06-02 欧阳锋写了递归深挖法 prompt 和 Judge 三问 prompt，用户问"这些提示词如何自动注入执行计划的大模型中"。
>
> **问题**：当前 prompts/ 目录下有可复用的提示词，但每个 Agent 需要手动 Read 文件再手动注入。依赖"知道有这个东西"且"记得去找"。
>
> **目标**：Agent 领任务时自动加载所需的提示词，不需要人干预。

---

## 分层方案

### Level 0 — 当前状态（手动）

```python
prompt_text = read_file("40_outputs/capabilities/prompts/judge-three-questions-prompt.md")
# 然后手动注入到对话中
```

能用，但依赖每个 Agent 知道路径且记得去找。

### Level 1 — `kdo prompt` 命令（短期）

```bash
kdo prompt judge-three-questions
# → 输出 prompt 内容到 stdout
kdo prompt list
# → 列出所有可用 prompt
```

**改动量**：新增 `kdo/commands/prompt.py`，~50 行。从 `40_outputs/capabilities/prompts/` 读文件，按 frontmatter title 索引。

**价值**：不再需要记路径。`kdo prompt list` 能看到全部。

### Level 2 — Skill→Prompt 绑定（中期）

在 SKILL.md frontmatter 中声明依赖的 prompt：

```yaml
# skills/deep-synthesis/SKILL.md
required_prompts:
  - src_unknown
  - src_unknown
```

Agent 加载 skill 时自动去 prompts/ 读对应文件，注入上下文。

**改动量**：定义 frontmatter 约定，修改 skill-loader。~1h。

### Level 3 — Task→Prompt 绑定（中期）

在任务文件 frontmatter 中声明：

```yaml
# tasks/task-xxx.md
required_prompts:
  - src_unknown
  - src_unknown
```

Agent 领任务时：
```
读任务 → 看 required_prompts → 自动加载 → 开干
```

**改动量**：定义 frontmatter 约定，修改 task-reader。~1h。

### Level 4 — 运行时自动注入（远期）

Agent session 启动时自动完成：
```
读 context.md → 看 active_task → 找任务文件 → 读 required_prompts
→ 自动注入所有 prompt 到系统提示词 → 全程无人干预
```

**改动量**：依赖 Level 2+3 先就绪。需要各 Agent 的启动脚本改造。

---

## 当前 prompt 资产清单

| prompt 文件 | 用途 | 对应 Skill |
|:------------|:-----|:-----------|
| `judge-three-questions-prompt.md` | 深度合成文章独立判断层 | deep-synthesis（待建） |
| `recursive-deepen-prompt.md` | 递归深挖法——三反馈飞轮 | `skills/recursive-deepen` |
| `label-prompt-v10-final.md` | 自动标注管线 prompt | `skills/data-curator` |

---

## 不做什么

- src_unknown
- src_unknown
- src_unknown

---

## 下一步

下次用户看到这个文件时，决定：
1. 是否先从 Level 1（`kdo prompt`）开始？
2. Level 2（Skill→Prompt）和 Level 3（Task→Prompt）哪个优先级更高？
3. 是否把这个提案排进 Sprint？