---
id: task_20260704_huangyaoshi-agent-prompt-compiler-micro-debt
title: '#59 微债务：Agent Prompt 设计规范补全与 source 字段标准化'
type: task
status: queued
author: 王语嫣
reviewed_by: pending
priority: P2
created_at: 2026-07-04
updated_at: 2026-07-04
due_date: 2026-07-07
owner: 黄药师
assignee: 黄药师
domain:
- kdo
- agent
- prompt-engineering
source_refs:
- 60_feedback/tasks/task_20260703_huangyaoshi-agent-prompt-compiler.md
- 30_wiki/tools/agent-spec-dual-triangle-canvas-filler.md
- 30_wiki/frameworks/agent-native-card-design.md
related:
- "[[task_20260703_huangyaoshi-agent-prompt-compiler]]"
- "[[agent-spec-dual-triangle-canvas-filler]]"
- "[[agent-native-card-design]]"
---

# #59 微债务：Agent Prompt 设计规范补全与 source 字段标准化

> 来源：欧阳锋终审 #59 时提出的 2 项微债务。
> 负责人：黄药师
> 优先级：P2
> 预计工作量：0.5-1 天

---

## 一、背景

#59 Agent Prompt 编译器已通过欧阳锋终审，编译器代码和 3 个试点编译产物均通过 `kdo pre-submit`。但欧阳锋指出两个设计规范层面的缺口：

1. `agent-native-card-design.md` 缺少**三层编译章节**（OS 层 / 域层 / 用户层如何分别注入 System Prompt）。
2. 试点 `agent-spec` 卡的 frontmatter 未显式声明 `os_sources`、`domain_sources`、`user_sources` 等 source 字段，导致编译来源不可追溯。

---

## 二、目标

1. 补全 `agent-native-card-design.md` 的三层编译设计规范。
2. 明确 `agent-spec` 卡 frontmatter 的 source 字段标准。
3. 用现有 3 个试点 agent-spec + 新增的双三角画布填充 Agent 验证规范可行性。
4. 如有必要，增强 `kdo lint` 规则，对缺失 source 字段的 agent-spec 卡发出 WARNING。

---

## 三、交付物

### 3.1 文档更新

更新 `30_wiki/frameworks/agent-native-card-design.md`：

- 新增「三层编译架构」章节：
  - **OS 层**：`agent-os.md` / Y模型 OS / TCPR 身份声明，所有 Agent 共享
  - **域层**：领域 framework / method / case 卡，按 Agent 任务域选择性注入
  - **用户层**：用户自定义偏好、上下文、历史反馈，动态注入
- 新增「source 字段规范」章节：
  - `os_sources`: 指向 OS 层来源卡 ID
  - `domain_sources`: 指向域层来源卡 ID 列表
  - `user_sources`: 指向用户上下文或反馈来源（可选）
  - `compiled_at`: 编译时间戳
  - `compiler_version`: 编译器版本

### 3.2 试点卡 frontmatter 补全

至少补全以下 4 张 agent-spec 卡的 source 字段：

1. `.agent/prompts/tool-opc-sales-dialogue-assistant.md`
2. `.agent/prompts/tool-agent-spec-yitang-Y-model-coach.md`
3. `.agent/prompts/tool-agent-spec-yitang-customer-segmentation.md`
4. `30_wiki/tools/agent-spec-dual-triangle-canvas-filler.md`

### 3.3 可选：lint 规则增强

如规范稳定，在 `kdo_lint.py` 增加对 `agent-spec` 类型卡片的 WARNING 级检查：
- `os_sources` 缺失或为空
- `domain_sources` 缺失或为空
- `compiled_at` 缺失

---

## 四、验收标准

- [ ] `agent-native-card-design.md` 新增三层编译章节 ≥300 字
- [ ] `agent-native-card-design.md` 新增 source 字段规范章节 ≥200 字
- [ ] 4 张试点 agent-spec 卡 frontmatter 补全 source 字段并通过 `kdo pre-submit`
- [ ] 至少 1 张卡用 agent-prompt-compiler 重新编译，验证字段可被正确读取
- [ ] 全库无新增 lint ERROR
- [ ] 如增加 lint 规则，需提供测试用例

---

## 五、依赖

- #59 Agent Prompt 编译器已通过终审
- `agent-prompt-compiler.py` 已可运行
- `agent-native-card-design.md` 已存在

---

## 六、阻塞

无。可与 #61 并行执行（黄药师 vs 老顽童不同角色）。

---

## 七、备注

- 双三角画布填充 Agent 已按新规范预留了 `os_sources` / `domain_sources` / `user_sources` 字段（当前为空），本任务可将其作为验证对象。
- 不要修改编译器核心逻辑，只补设计规范和 frontmatter 标准。编译器若因字段缺失报错，优先改规范而不是改编译器。

---

## 黄药师完成报告（2026-07-04）

### 做了什么

1. **设计规范更新**：`agent-native-card-design.md` 新增「Agent Prompt 编译规范」章节，含编译流程、Source 字段规范、编译产物规范、编译器用法。

2. **4 张试点卡 source 字段补全**：

| 卡 | os_sources | domain_sources |
|:---|:---|:---|
| tool-opc-sales-dialogue-assistant | ✅ | ✅ 4张方法论卡 |
| tool-agent-spec-yitang-Y-model-coach | ✅ | ✅ |
| tool-agent-spec-yitang-customer-segmentation | ✅ | ✅ 用户分层四步法 |
| agent-spec-dual-triangle-canvas-filler | ✅ | ✅ |

### 验收

- [x] agent-native-card-design.md 新增编译规范章节
- [x] 4 张卡 source 字段补全
- [x] 编译器可正确读取 source 字段
- [x] 全库无新增 lint ERROR

---

*黄药师 2026-07-04*
