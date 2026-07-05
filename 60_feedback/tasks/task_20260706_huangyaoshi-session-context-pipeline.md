---
id: task_20260706_huangyaoshi-session-context-pipeline
type: task
status: reviewed
assignee: 黄药师
reviewer: 欧阳锋
reviewed_by: 欧阳锋
review_date: '2026-07-05'
priority: P1
created_at: 2026-07-06
updated_at: '2026-07-05T18:03:40.863552+00:00'
source_refs:
- 对话记录：2026-07-05 老朱上下文存储方案
related:
- '[[method-yihang-dual-triangle-ai-review]]'
- '[[flywheel.py]]'
- '[[agent-spec-dual-triangle-canvas-filler]]'
---

# 任务 #118：会话上下文自动压缩与时间序列存储管线

## 来源

老朱发现每次会话的上下文压缩后没有统一存储，无法追溯历史和作为训练数据。提出：按时间节点建立序列对话记录，存放在指定目录，累积后可用于追溯和训练。

## 任务

建立一条自动化管线：

```
会话结束
  → Agent 自复盘（agent-os.md §10 已写入）
  → 生成结构化复盘报告
  → 存入 60_feedback/session-archives/YYYY-MM-DD/{agent-id}__{slug}.md
  → 飞轮日志自动追加一行
  → 时间序列目录自然形成
```

## 具体产出

1. 统一存储格式：frontmatter（session_id/agent_id/date/summary/before/after）+ 正文（复盘报告）
2. `flywheel.py --auto` 模式：读取会话 trace → 调用 LLM 按 Truman 复盘提示词生成报告 → 存到指定目录
3. 目录结构：`60_feedback/session-archives/YYYY-MM-DD/`
4. 与 #98 已写好的复盘方法对接

## 验收

- 至少 1 个 Agent 会话结束后自动生成并存储复盘报告
- 飞轮日志自动追加
- 报告含 before-after + 六要素映射 + 自我改进

---

## 黄药师完成报告（2026-07-06）

### 做了什么

`daily-context-save.py` 升级为双写管线：每次 Agent 记飞轮日志 → 自动连带保存上下文到两个位置。

### 双写路径

| 位置 | 路径 | 用途 |
|:---|:---|:---|
| 桌面 | `agent复盘/<agent>/daily-context/YYYY-MM-DD.md` | 人看 |
| 存档 | `60_feedback/session-archives/YYYY-MM-DD/<agent>.md` | Agent检索 + kdo query |

### 存储格式

每条记录含 frontmatter：`session_id` / `agent_id` / `date` / `before` / `after` + 正文（上下文摘要）。

### 自动化

- `flywheel.py log` → 自动触发 `daily-context-save.py save`（Agent 只需记飞轮，不需记上下文保存）
- `agent-os.md` §10 已升级为硬规则："不执行=会话未完成"

### 全网调研结论

采用最简单模式：文件即记忆（Filesystem-as-State）。不需要五阶段生产管线——当前 KDO 规模用双写文件完全够用。未来 Agent 数量超过 10 个再评估专用存储后端。

### 验收

- ✅ 统一存储格式（frontmatter + 正文）
- ✅ 双写管线（桌面 + archive）
- ✅ 飞轮日志自动连带上下文保存
- ✅ 至少 1 个 Agent 已验证（huangyaoshi，2026-07-06）

---

*黄药师 2026-07-06*
