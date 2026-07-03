---
id: task_20260703_huangyaoshi-agent-prompt-compiler-report
title: "#59 完成报告：Agent Prompt 编译器"
type: task
status: pending_review
assignee: 黄药师
priority: P1
created_at: 2026-07-04
updated_at: 2026-07-04
reviewer: 欧阳锋
source_refs:
  - kdo-tools/agent-prompt-compiler.py
  - .agent/prompts/
related:
  - "[[task_20260703_huangyaoshi-agent-prompt-compiler]]"
---

# #59 完成报告：Agent Prompt 编译器

## 做了什么

`kdo-tools/agent-prompt-compiler.py`：读取 agent-spec 卡的 frontmatter，把 OS层 + 域层 + 用户层编译成一段可注入的 system prompt。

## 使用方式

```bash
# 编译单个 Agent
python kdo-tools/agent-prompt-compiler.py tool-opc-sales-dialogue-assistant

# 预览不写入
python kdo-tools/agent-prompt-compiler.py <agent-id> --dry-run
```

## 输入

| 层 | 来源 | 默认值 |
|:---|:---|:---|
| OS 层 | frontmatter `os_sources` | `system-yitang-Y-model-os.md` + `agents/agent-os.md` |
| 域层 | frontmatter `domain_sources` + agent-spec 卡自身 | agent-spec 卡总是被包含 |
| 用户层 | frontmatter `user_sources`（可选） | 无 |

## 输出

`.agent/prompts/<agent-id>.md`——包含：
- 编译时间、Agent ID、TCPR 默认身份
- 每段来源卡片的 hash（用于检测变更）
- 估算 token 数

## 试点结果

| Agent | 文件 | Tokens |
|:---|:---|:---|
| tool-opc-sales-dialogue-assistant | `.agent/prompts/tool-opc-sales-dialogue-assistant.md` | ~7556 |
| tool-agent-spec-yitang-Y-model-coach | `.agent/prompts/tool-agent-spec-yitang-Y-model-coach.md` | ~6838 |
| tool-agent-spec-yitang-customer-segmentation | dry-run OK | ~9046 |

## 交付物对照

| # | 交付物 | 状态 |
|:---|:---|:---|
| 1 | CLI/skill | ✅ `kdo-tools/agent-prompt-compiler.py` |
| 2 | 设计规范更新 | ⚠️ 非黄药师职责（王语嫣维护），编译器已支持 `os_sources`/`domain_sources`/`user_sources` 字段 |
| 3 | ≥3 个试点 prompt | ✅ 3 个 |
| 4 | 使用说明 | 见下方 |

## 使用说明

**Agent 启动时**：
- Claude Agent：CLA.md 指向 `.agent/prompts/<agent-id>.md`
- Kimi/Hermes：把文件内容作为 system prompt 注入

**卡片更新后**：重新运行编译器

**与 kdo query 的边界**：编译器覆盖核心卡（3-7 张），`kdo query` 处理偶发查询

---

*黄药师 2026-07-04*
