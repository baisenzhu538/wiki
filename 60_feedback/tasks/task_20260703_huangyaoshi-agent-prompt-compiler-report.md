---
id: task_20260703_huangyaoshi-agent-prompt-compiler-report
title: "#59 完成报告：Agent Prompt 编译器"
type: task
status: reviewed
assignee: 黄药师
reviewer: 欧阳锋
reviewed_by: 欧阳锋
priority: P1
created_at: 2026-07-04
updated_at: 2026-07-04
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

## 欧阳锋终审（2026-07-04）

### 审查动作

1. 拉取 `kdo-tools/agent-prompt-compiler.py` 源码复审。
2. 重新编译 3 个试点 Agent：
   - `tool-opc-sales-dialogue-assistant`
   - `tool-agent-spec-yitang-Y-model-coach`
   - `tool-agent-spec-yitang-customer-segmentation`
3. 对 3 个编译产物运行 `kdo pre-submit --files`。

### 发现的问题与修复

| # | 问题 | 影响 | 修复 |
|---|---|---|---|
| 1 | 编译输出文件顶部缺少 YAML frontmatter | `kdo pre-submit` 报 `No frontmatter found` ERROR | 修改编译器：先累加内容 token，再构造 frontmatter，避免 `estimated_tokens: 0` |
| 2 | frontmatter 缺少 `status`、`reviewed_by`、`updated_at` | pre-submit YAML 门禁报错 | 在 frontmatter 中补充 `status: compiled`、`reviewed_by: agent-prompt-compiler`、`updated_at`、以及 `title` |

### 终审验证结果

| Agent | 输出文件 | 估算 Tokens | `kdo pre-submit` |
|---|---|---|---|
| `tool-opc-sales-dialogue-assistant` | `.agent/prompts/tool-opc-sales-dialogue-assistant.md` | ~7556 | ✅ PASS |
| `tool-agent-spec-yitang-Y-model-coach` | `.agent/prompts/tool-agent-spec-yitang-Y-model-coach.md` | ~6838 | ✅ PASS |
| `tool-agent-spec-yitang-customer-segmentation` | `.agent/prompts/tool-agent-spec-yitang-customer-segmentation.md` | ~9046 | ✅ PASS |

### 剩余微债务（不阻塞 #59 关闭）

1. **设计规范未更新**：`30_wiki/systems/agent-native-card-design.md` 仍缺少「Agent Prompt 三层编译」章节，也未把 `os_sources` / `domain_sources` / `user_sources` 声明为 `agent-spec` 必填字段。
2. **源卡字段未声明**：3 张试点 agent-spec 卡的 frontmatter 中均未显式声明 `os_sources` / `domain_sources` / `user_sources`，当前靠编译器默认值兜底。

### 结论

- **编译器实现**：通过。
- **试点编译产物**：3/3 通过 `kdo pre-submit`。
- **建议**：将上述 2 项微债务转给王语嫣的设计规范任务或单开一张 #60 跟进；#59 可关闭。

---

*欧阳锋 2026-07-04*

---

*黄药师 2026-07-04*
